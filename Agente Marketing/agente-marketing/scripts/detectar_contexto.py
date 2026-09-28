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
    else:
        siguiente = "Marca conocida: bienvenida corta y menú principal"

    print(json.dumps(
        {"carpeta": str(raiz), "marcas": marcas, "contexto_producto": contexto, "siguiente_paso": siguiente},
        ensure_ascii=False, indent=2,
    ))


if __name__ == "__main__":
    main()
