#!/usr/bin/env python3
"""Memoria de campañas de una marca: agrega resultados a su historial y resume aprendizajes.

Uso:
    python3 registrar_aprendizaje.py --historial marketing/mi-marca/historial-campanas.csv --agregar filas.csv
    python3 registrar_aprendizaje.py --historial marketing/mi-marca/historial-campanas.csv --resumen [--por hook]

Si el historial no existe, se crea a partir de assets/plantillas/historial-campanas.csv.
El ranking usa el CPL calificado; si no hay calificados, usa el costo por venta.
"""
import argparse
import csv
import os
import sys
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTILLA = os.path.join(BASE, "assets", "plantillas", "historial-campanas.csv")


def num(v):
    try:
        return float(str(v).replace("$", "").replace(",", "").strip() or 0)
    except ValueError:
        return 0.0


def leer(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def asegurar(hist):
    if not os.path.exists(hist):
        os.makedirs(os.path.dirname(os.path.abspath(hist)), exist_ok=True)
        with open(PLANTILLA, encoding="utf-8") as src, open(hist, "w", encoding="utf-8") as dst:
            dst.write(src.read())
        print(f"Historial creado: {hist}")


def agregar(HIST, path):
    asegurar(HIST)
    with open(HIST, newline="", encoding="utf-8-sig") as f:
        campos = next(csv.reader(f))
    nuevas = leer(path)
    with open(HIST, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos, extrasaction="ignore")
        for fila in nuevas:
            w.writerow({c: fila.get(c, "") for c in campos})
    print(f"{len(nuevas)} fila(s) agregadas a {HIST}")


def resumen(HIST, dimensiones):
    if not os.path.exists(HIST):
        print("Todavía no hay historial para esta marca: no hay aprendizajes registrados.")
        return
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
        def costo(m):
            if m["leads_calificados"]:
                return m["gasto"] / m["leads_calificados"]
            if m["ventas"]:
                return m["gasto"] / m["ventas"]
            return float("inf")
        orden = sorted(g.items(), key=lambda kv: costo(kv[1]))
        print(f"\n## Por {dim}")
        print("| Valor | Registros | Gasto | Calificados | CPLc | Oportunidades | Ventas | CPA | ROAS |")
        print("|---|---|---|---|---|---|---|---|---|")
        for clave, m in orden:
            cplc = f"{m['gasto'] / m['leads_calificados']:,.2f}" if m["leads_calificados"] else "-"
            cpa = f"{m['gasto'] / m['ventas']:,.2f}" if m["ventas"] else "-"
            roas = f"{m['facturacion'] / m['gasto']:.2f}x" if m["gasto"] else "-"
            print(f"| {clave} | {m['n']:.0f} | {m['gasto']:,.2f} | {m['leads_calificados']:.0f} | {cplc} | "
                  f"{m['oportunidades']:.0f} | {m['ventas']:.0f} | {cpa} | {roas} |")
    perdedores = [f for f in filas if (f.get("veredicto") or "").upper() == "PERDEDOR"]
    if perdedores:
        print("\n## No repetir sin una hipótesis nueva")
        for f in perdedores:
            print(f"- {f.get('producto')} · {f.get('audiencia')} · hook «{f.get('hook')}»: {f.get('aprendizaje')}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--historial", required=True, help="Ruta al historial-campanas.csv de la marca")
    p.add_argument("--agregar", metavar="CSV")
    p.add_argument("--resumen", action="store_true")
    p.add_argument("--por", nargs="*", default=["producto", "audiencia", "hook", "formato"])
    a = p.parse_args()
    if a.agregar:
        agregar(a.historial, a.agregar)
    if a.resumen:
        resumen(a.historial, a.por)
    if not (a.agregar or a.resumen):
        p.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
