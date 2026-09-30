#!/usr/bin/env python3
"""Detecta la memoria de marketing guardada en una carpeta de trabajo.

Busca los archivos que usan Mark y sus skills especialistas (ficha de marca,
historial de campañas, sistema visual, contexto de producto y estado de Mark)
y devuelve un resumen en JSON.

Uso:
    python3 detectar_contexto.py [carpeta_de_trabajo]
"""

import json
import re
import sys
import zipfile
from datetime import date, datetime
from pathlib import Path

ARCHIVOS_MARCA = {
    "perfil_marca": ["perfil-marca.docx", "perfil-marca.md"],
    "historial_campanas": ["historial-campanas.xlsx", "historial-campanas.csv"],
    "sistema_visual": ["sistema-visual.md"],
    "estado_mark": ["estado-mark.md"],
}
CONTEXTO_PRODUCTO = [
    ".agents/product-marketing.md",
    ".claude/product-marketing.md",
    "product-marketing-context.md",
]
IGNORAR = {".git", "node_modules", "__pycache__", ".venv", "venv"}


def texto_docx(ruta: Path) -> str:
    """Extrae el texto plano de un .docx sin librerías externas."""
    try:
        with zipfile.ZipFile(ruta) as z:
            xml = z.read("word/document.xml").decode("utf-8", "ignore")
    except (zipfile.BadZipFile, KeyError, OSError):
        return ""
    xml = re.sub(r"</w:p>", "\n", xml)
    return re.sub(r"<[^>]+>", "", xml)


def leer_texto(ruta: Path) -> str:
    if ruta.suffix == ".docx":
        return texto_docx(ruta)
    try:
        return ruta.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def info_archivo(ruta: Path) -> dict:
    modificado = datetime.fromtimestamp(ruta.stat().st_mtime).date()
    return {
        "ruta": str(ruta),
        "modificado": modificado.isoformat(),
        "dias_desde_cambio": (date.today() - modificado).days,
    }


def resumen_ficha(ruta: Path) -> dict:
    texto = leer_texto(ruta)
    return {
        "pendientes": len(re.findall(r"PENDIENTE", texto)),
        "supuestos": len(re.findall(r"SUPUESTO", texto, re.IGNORECASE)),
    }


def calcular_fase(marca: dict) -> str:
    """'activo' si la marca ya tiene contenido creado; si no, 'onboarding'."""
    estado = marca.get("estado_mark")
    if estado:
        texto = leer_texto(Path(estado["ruta"]))
        m = re.search(r"Fase de Mark:\*{0,2}\s*(activo|onboarding)\b", texto, re.IGNORECASE)
        if m:
            return m.group(1).lower()
    carpeta = Path(marca["carpeta"]) / "entregables"
    if carpeta.is_dir() and any(p.suffix in (".html", ".png") for p in carpeta.rglob("*")):
        return "activo"
    visual = marca.get("sistema_visual")
    if visual and re.search(r"Kit tipogr[aá]fico:\s*kit_", leer_texto(Path(visual["ruta"])), re.IGNORECASE):
        return "activo"
    return "onboarding"


def buscar_marcas(raiz: Path) -> list:
    """Cada carpeta que contenga algún archivo de marca cuenta como una marca."""
    carpetas = {}
    nombres = {n: clave for clave, lista in ARCHIVOS_MARCA.items() for n in lista}
    for ruta in raiz.rglob("*"):
        if any(p in IGNORAR for p in ruta.parts) or not ruta.is_file():
            continue
        clave = nombres.get(ruta.name)
        if not clave:
            continue
        marca = carpetas.setdefault(str(ruta.parent), {"carpeta": str(ruta.parent), "marca": ruta.parent.name})
        # Prefiere el formato de entrega (.docx/.xlsx) sobre los antiguos.
        if clave not in marca or ruta.suffix in (".docx", ".xlsx"):
            marca[clave] = info_archivo(ruta)
            if clave == "perfil_marca":
                marca[clave].update(resumen_ficha(ruta))
    for marca in carpetas.values():
        marca["fase"] = calcular_fase(marca)
    return sorted(carpetas.values(), key=lambda m: m["carpeta"])


def main() -> None:
    raiz = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not raiz.is_dir():
        print(json.dumps({"error": f"No existe la carpeta {raiz}"}, ensure_ascii=False))
        sys.exit(1)

    contexto = [info_archivo(raiz / r) for r in CONTEXTO_PRODUCTO if (raiz / r).is_file()]
    marcas = buscar_marcas(raiz)

    if not marcas and not contexto:
        siguiente = "Marca nueva: ejecutar rutinas/02-onboarding-unificado.md"
    elif len(marcas) > 1:
        siguiente = "Varias marcas: preguntar con cuál trabajar"
    elif marcas and marcas[0]["fase"] == "activo":
        siguiente = "Marca activa: saludo con headlines del día (rutinas/03-saludo-headlines.md)"
    else:
        siguiente = "Marca conocida sin contenido aún: presentación completa y menú"

    print(json.dumps(
        {"carpeta": str(raiz), "marcas": marcas, "contexto_producto": contexto, "siguiente_paso": siguiente},
        ensure_ascii=False, indent=2,
    ))


if __name__ == "__main__":
    main()
