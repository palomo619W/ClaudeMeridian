#!/usr/bin/env python3
"""Revisa la ficha de marca (perfil-marca.md) y lista qué falta por nivel.

Uso:
    python3 verificar_perfil.py marketing/mi-marca/perfil-marca.md

Lee las líneas con formato `- **Campo** [N1]: valor`. Un campo está pendiente si está vacío
o contiene PENDIENTE; si contiene SUPUESTO, está sin confirmar.
El número de pregunta sugerido corresponde a references/cuestionario-marca.md.
"""
import re
import sys

LINEA = re.compile(r"^- \*\*(.+?)\*\* \[(N\d)\]:\s*(.*)$")
NIVELES = {"N1": "Esencial (para empezar)", "N2": "Para planificar campañas", "N3": "Medición y optimización"}


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    campos = []
    with open(sys.argv[1], encoding="utf-8") as f:
        for linea in f:
            m = LINEA.match(linea.strip())
            if m:
                campos.append(m.groups())
    if not campos:
        sys.exit("No encontré campos con el formato de la plantilla assets/plantillas/perfil-marca.md")

    pendientes = {n: [] for n in NIVELES}
    supuestos = []
    for campo, nivel, valor in campos:
        v = valor.strip()
        if not v or "PENDIENTE" in v.upper():
            pendientes.setdefault(nivel, []).append(campo)
        elif "SUPUESTO" in v.upper():
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
        print("\n## Supuestos por confirmar")
        for c in supuestos:
            print(f"- {c}")
    if pendientes.get("N1"):
        print("\nSiguiente paso: completar el Nivel 1 antes de planificar (rutinas/00-onboarding.md).")
    elif pendientes.get("N2"):
        print("\nSiguiente paso: pedir solo los campos de N2 que necesite la tarea actual (máx. 4).")
    else:
        print("\nLa ficha permite planificar. Completa N3 para medir y optimizar con precisión.")


if __name__ == "__main__":
    main()
