#!/usr/bin/env python3
"""Memoria de campañas: agrega resultados a data/historial-campanas.csv y resume aprendizajes.

Uso:
    python3 registrar_aprendizaje.py --agregar fila.csv     # agrega filas (mismas columnas del historial)
    python3 registrar_aprendizaje.py --resumen [--por hook]  # ranking por CPL calificado
"""
import argparse
import csv
import os
import sys
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HIST = os.path.join(BASE, "data", "historial-campanas.csv")


def num(v):
    try:
        return float(str(v).replace("$", "").replace(",", "").strip() or 0)
    except ValueError:
        return 0.0


def leer(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def agregar(path):
    with open(HIST, newline="", encoding="utf-8-sig") as f:
        campos = next(csv.reader(f))
    nuevas = leer(path)
    with open(HIST, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        for fila in nuevas:
            w.writerow({c: fila.get(c, "") for c in campos})
    print(f"{len(nuevas)} fila(s) agregadas a {HIST}")


def resumen(dimensiones):
    filas = leer(HIST)
    if not filas:
        print("Historial vacío: todavía no hay aprendizajes registrados.")
        return
    for dim in dimensiones:
        g = defaultdict(lambda: defaultdict(float))
        for f in filas:
            clave = f.get(dim) or "(sin dato)"
            for c in ("gasto", "leads", "conversaciones", "leads_calificados", "oportunidades", "ventas", "facturacion"):
                g[clave][c] += num(f.get(c))
            g[clave]["n"] += 1
        orden = sorted(g.items(), key=lambda kv: (kv[1]["gasto"] / kv[1]["leads_calificados"])
                       if kv[1]["leads_calificados"] else float("inf"))
        print(f"\n## Por {dim}")
        print("| Valor | Registros | Gasto | Calificados | CPLc | Oportunidades | Ventas |")
        print("|---|---|---|---|---|---|---|")
        for clave, m in orden:
            cplc = f"${m['gasto'] / m['leads_calificados']:,.2f}" if m["leads_calificados"] else "sin calificados"
            print(f"| {clave} | {m['n']:.0f} | ${m['gasto']:,.2f} | {m['leads_calificados']:.0f} | {cplc} | "
                  f"{m['oportunidades']:.0f} | {m['ventas']:.0f} |")
    perdedores = [f for f in filas if (f.get("veredicto") or "").upper() == "PERDEDOR"]
    if perdedores:
        print("\n## No repetir sin una hipótesis nueva")
        for f in perdedores:
            print(f"- {f.get('producto')} · {f.get('audiencia')} · hook «{f.get('hook')}»: {f.get('aprendizaje')}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--agregar", metavar="CSV")
    p.add_argument("--resumen", action="store_true")
    p.add_argument("--por", nargs="*", default=["producto", "audiencia", "hook", "formato"])
    a = p.parse_args()
    if a.agregar:
        agregar(a.agregar)
    if a.resumen:
        resumen(a.por)
    if not (a.agregar or a.resumen):
        p.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
