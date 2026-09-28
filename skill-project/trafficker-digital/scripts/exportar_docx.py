#!/usr/bin/env python3
"""Convierte un borrador en Markdown en un documento Word (.docx) listo para entregar.

Uso:
    python3 exportar_docx.py borrador.md salida.docx [--titulo "Plan de campaña · Marca"]

Soporta títulos (#, ##, ###), párrafos, **negrita**, *cursiva*, `código`, listas con viñetas
y numeradas, tablas Markdown, citas (>), bloques de código y separadores (---).
No requiere librerías externas.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ooxml import write_docx  # noqa: E402


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("entrada", help="Archivo Markdown (.md) con el contenido")
    p.add_argument("salida", help="Ruta del .docx a crear")
    p.add_argument("--titulo", help="Título del documento (por defecto, el primer encabezado)")
    a = p.parse_args()

    with open(a.entrada, encoding="utf-8") as f:
        md = f.read()
    titulo = a.titulo
    if not titulo:
        m = re.search(r"^#{1,3}\s+(.+)$", md, re.M)
        titulo = re.sub(r"[*_`]", "", m.group(1)).strip() if m else os.path.splitext(os.path.basename(a.salida))[0]
    if not a.salida.lower().endswith(".docx"):
        sys.exit("La salida debe terminar en .docx")
    os.makedirs(os.path.dirname(os.path.abspath(a.salida)), exist_ok=True)
    write_docx(a.salida, md, title=titulo)
    print(f"Documento creado: {a.salida}")


if __name__ == "__main__":
    main()
