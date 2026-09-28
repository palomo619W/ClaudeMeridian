#!/usr/bin/env python3
"""Crea un libro de Excel (.xlsx) con una hoja por tabla o por archivo de datos.

Uso:
    python3 exportar_xlsx.py salida.xlsx entrada1 [entrada2 ...]

Cada entrada puede ser:
  - .csv  -> una hoja con el nombre del archivo
  - .xlsx -> copia su primera hoja
  - .md   -> una hoja por cada tabla Markdown del texto, con el nombre del encabezado anterior
Los números y porcentajes se guardan como valores numéricos para poder calcular en Excel.
No requiere librerías externas.
"""
import argparse
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ooxml import markdown_tables, read_xlsx_rows, write_xlsx  # noqa: E402


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("salida")
    p.add_argument("entradas", nargs="+")
    a = p.parse_args()
    if not a.salida.lower().endswith(".xlsx"):
        sys.exit("La salida debe terminar en .xlsx")

    hojas = []
    for ruta in a.entradas:
        nombre = os.path.splitext(os.path.basename(ruta))[0]
        ext = os.path.splitext(ruta)[1].lower()
        if ext == ".csv":
            with open(ruta, newline="", encoding="utf-8-sig") as f:
                hojas.append((nombre, [row for row in csv.reader(f)]))
        elif ext == ".xlsx":
            hojas.append((nombre, read_xlsx_rows(ruta)))
        elif ext in (".md", ".txt"):
            with open(ruta, encoding="utf-8") as f:
                tablas = markdown_tables(f.read())
            if not tablas:
                print(f"Aviso: {ruta} no contiene tablas Markdown")
            hojas.extend(tablas)
        else:
            sys.exit(f"Formato no soportado: {ruta}")
    if not hojas:
        sys.exit("No hay datos para exportar.")
    os.makedirs(os.path.dirname(os.path.abspath(a.salida)), exist_ok=True)
    write_xlsx(a.salida, hojas, title=os.path.splitext(os.path.basename(a.salida))[0])
    print(f"Libro creado: {a.salida} ({len(hojas)} hoja(s): {', '.join(h[0][:31] for h in hojas)})")


if __name__ == "__main__":
    main()
