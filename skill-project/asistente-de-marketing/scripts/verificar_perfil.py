#!/usr/bin/env python3
"""Revisa la ficha de marca (perfil-marca.md) y lista qué falta por nivel.

Uso:
    python3 verificar_perfil.py marketing/mi-marca/perfil-marca.md
    python3 verificar_perfil.py marketing/mi-marca/perfil-marca.docx

Lee las líneas con formato `- **Campo** [N1]: valor`. Un campo está pendiente si está vacío
o empieza con PENDIENTE; si contiene SUPUESTO, "por confirmar" o un PENDIENTE parcial, está completo
pero sin confirmar.
El número de pregunta sugerido corresponde a references/cuestionario-marca.md.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ooxml import read_docx_text  # noqa: E402

LINEA = re.compile(r"^-\s+(?:\*\*)?(.+?)(?:\*\*)?\s*\[(N\d)\]:\s*(.*)$")
NIVELES = {"N1": "Esencial (para empezar)", "N2": "Para planificar campañas", "N3": "Medición y optimización"}


def main():
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0 if len(sys.argv) == 2 else 1)
    campos = []
    ruta = sys.argv[1]
    if ruta.lower().endswith(".docx"):
        texto = read_docx_text(ruta)
    else:
        with open(ruta, encoding="utf-8") as f:
            texto = f.read()
    for linea in texto.splitlines():
        m = LINEA.match(linea.strip())
        if m:
            campos.append(m.groups())
    if not campos:
        sys.exit("No encontré campos con el formato de la plantilla assets/plantillas/perfil-marca.md")

    pendientes = {n: [] for n in NIVELES}
    supuestos = []
    for campo, nivel, valor in campos:
        v = valor.strip()
        vu = v.upper()
        # Solo está pendiente si el campo está vacío o empieza con PENDIENTE; un dato con un detalle
        # "PENDIENTE DE CONFIRMAR" o "(por confirmar: …)" cuenta como completo pero sin confirmar.
        if not v or vu.startswith("PENDIENTE"):
            pendientes.setdefault(nivel, []).append(campo)
        elif "SUPUESTO" in vu or "PENDIENTE" in vu or "POR CONFIRMAR" in vu:
            supuestos.append(campo)

    total = len(campos)
    completos = total - sum(len(v) for v in pendientes.values())
    print(f"Ficha completa al {completos / total:.0%} ({completos}/{total} campos)\n")
    for nivel, nombre in NIVELES.items():
        faltan = pendientes.get(nivel, [])
        estado = "completo" if not faltan else f"faltan {len(faltan)}"
        print(f"## {nivel} — {nombre}: {estado}")
        for c in faltan:
            print(f"- {c}")
    if supuestos:
        print("\n## Supuestos o detalles por confirmar")
        for c in supuestos:
            print(f"- {c}")
    if pendientes.get("N1"):
        print("\nSiguiente paso: faltan datos esenciales. Completa la entrevista de marca (rutinas/00-onboarding.md) antes de generar entregables.")
    elif pendientes.get("N2"):
        print("\nSiguiente paso: reúne los pendientes que necesite la tarea y pregúntalos en una sola ventana de opciones (cuestionario-marca.md, sección 5).")
    else:
        print("\nLa ficha permite planificar. Completa N3 para medir y optimizar con precisión.")


if __name__ == "__main__":
    main()
