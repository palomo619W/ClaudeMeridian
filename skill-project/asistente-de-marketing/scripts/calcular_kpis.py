#!/usr/bin/env python3
"""Calcula KPIs de pauta y de embudo comercial y sugiere APAGAR / MANTENER / ESCALAR.

Uso:
    # Modelos con leads (servicios, B2B, ticket alto)
    python3 calcular_kpis.py resultados.csv --cplc-objetivo 40 [--cpl-objetivo 10] [--ticket 5000] [--tasa-cierre 0.15]
    # E-commerce
    python3 calcular_kpis.py resultados.csv --cpa-objetivo 12 [--roas-minimo 2.5] --moneda MXN

El archivo (.csv o .xlsx) debe tener las columnas de assets/plantillas/resultados-campana.csv (las que falten se toman como 0).
Las reglas replican references/optimizacion.md.
"""
import argparse
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ooxml import read_xlsx_rows, write_xlsx  # noqa: E402

NUM_COLS = ["presupuesto", "gasto", "impresiones", "clics", "leads", "conversaciones",
            "leads_calificados", "oportunidades", "cotizaciones", "ventas", "facturacion"]
PCT = ("CTR", "%Calif", "Calif->Opor", "Opor->Cot", "Cot->Venta")


def num(value):
    try:
        return float(str(value).replace("$", "").replace(",", "").strip() or 0)
    except ValueError:
        return 0.0


def div(a, b):
    return a / b if b else None


def kpis(r):
    contactos = r["leads"] + r["conversaciones"]
    return {
        "CPM": div(r["gasto"] * 1000, r["impresiones"]),
        "CTR": div(r["clics"], r["impresiones"]),
        "CPC": div(r["gasto"], r["clics"]),
        "CPL": div(r["gasto"], contactos),
        "Costo/conv": div(r["gasto"], r["conversaciones"]),
        "%Calif": div(r["leads_calificados"], contactos),
        "Calif->Opor": div(r["oportunidades"], r["leads_calificados"]),
        "Opor->Cot": div(r["cotizaciones"], r["oportunidades"]),
        "Cot->Venta": div(r["ventas"], r["cotizaciones"]),
        "CPLc": div(r["gasto"], r["leads_calificados"]),
        "Costo/opor": div(r["gasto"], r["oportunidades"]),
        "CPA": div(r["gasto"], r["ventas"]),
        "ROAS": div(r["facturacion"], r["gasto"]),
        "_contactos": contactos,
    }


def decidir(r, k, a):
    contactos = k["_contactos"]
    if r["impresiones"] < 1000:
        return "DATOS INSUFICIENTES", "menos de 1 000 impresiones"
    if a.cpa_objetivo and r["ventas"] == 0 and r["gasto"] >= 2 * a.cpa_objetivo:
        return "APAGAR", f"gasto >= 2x CPA objetivo ({2 * a.cpa_objetivo:,.0f}) sin ventas"
    if a.roas_minimo and a.cpa_objetivo and k["ROAS"] is not None and r["gasto"] >= 3 * a.cpa_objetivo \
            and k["ROAS"] < 0.5 * a.roas_minimo:
        return "APAGAR", "ROAS < 50 % del mínimo con gasto >= 3x CPA objetivo"
    if a.cplc_objetivo and r["leads_calificados"] == 0 and r["gasto"] >= 3 * a.cplc_objetivo:
        return "APAGAR", f"gasto >= 3x CPLc objetivo ({3 * a.cplc_objetivo:,.0f}) sin leads calificados"
    if a.cpl_objetivo and contactos == 0 and r["gasto"] >= 2 * a.cpl_objetivo:
        return "APAGAR", f"gasto >= 2x CPL objetivo ({2 * a.cpl_objetivo:,.0f}) sin leads"
    if a.cplc_objetivo and contactos >= 20 and (k["%Calif"] or 0) < 0.10:
        return "APAGAR", "menos del 10 % de leads calificados con 20 o más leads"
    if r["impresiones"] > 2000 and r["clics"] and (k["CTR"] or 0) < 0.005:
        return "CAMBIAR HOOK", "CTR < 0,5 % con más de 2 000 impresiones"
    if a.cpa_objetivo and k["CPA"] is not None and k["CPA"] <= 0.8 * a.cpa_objetivo and r["ventas"] >= 10:
        return "ESCALAR", "CPA <= 80 % del objetivo con 10 o más ventas (+20 % cada 48-72 h)"
    if a.cplc_objetivo and k["CPLc"] is not None and k["CPLc"] <= 0.8 * a.cplc_objetivo and r["leads_calificados"] >= 5:
        return "ESCALAR", "CPLc <= 80 % del objetivo con 5 o más calificados (+20 % cada 48-72 h)"
    objetivo, actual = (a.cpa_objetivo, k["CPA"]) if a.cpa_objetivo else (a.cplc_objetivo, k["CPLc"])
    if objetivo and actual is not None and actual > 1.2 * objetivo:
        return "REVISAR", "métrica final > 120 % del objetivo"
    return "MANTENER", "dentro de rango o acumulando datos"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv", help="Resultados en .csv o .xlsx")
    p.add_argument("--cplc-objetivo", type=float, help="CPL calificado objetivo")
    p.add_argument("--cpl-objetivo", type=float, help="CPL objetivo")
    p.add_argument("--cpa-objetivo", type=float, help="Costo por venta objetivo (e-commerce o venta directa)")
    p.add_argument("--roas-minimo", type=float, help="ROAS mínimo aceptable (break-even = 1 / margen)")
    p.add_argument("--ticket", type=float, help="Valor promedio de venta, para estimar el ROAS potencial")
    p.add_argument("--tasa-cierre", type=float, default=0.15, help="Oportunidad -> venta (por defecto 0.15)")
    p.add_argument("--moneda", default="USD")
    p.add_argument("--xlsx", metavar="SALIDA", help="Guarda también la tabla de KPIs por anuncio en un .xlsx")
    a = p.parse_args()

    def fmt(key, v):
        if v is None:
            return "-"
        if key in PCT:
            return f"{v * 100:.1f}%"
        if key == "ROAS":
            return f"{v:.2f}x"
        return f"{v:,.2f} {a.moneda}"

    if a.csv.lower().endswith(".xlsx"):
        tabla = read_xlsx_rows(a.csv)
        encabezado = [str(h).strip() for h in tabla[0]] if tabla else []
        rows = [dict(zip(encabezado, fila)) for fila in tabla[1:]]
    else:
        with open(a.csv, newline="", encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("El CSV no tiene filas.")

    total = {c: 0.0 for c in NUM_COLS}
    if a.cpa_objetivo:
        show = ["CPM", "CTR", "CPC", "CPA", "ROAS"]
    else:
        show = ["CPM", "CTR", "CPC", "CPL", "%Calif", "CPLc", "Costo/opor", "CPA", "ROAS"]
    print("| Anuncio | Gasto | Leads | Calif. | Ventas | " + " | ".join(show) + " | Decisión | Motivo |")
    print("|" + "---|" * (len(show) + 7))
    hoja = [["Anuncio", "Gasto", "Leads", "Calificados", "Ventas"] + show + ["Decisión", "Motivo"]]
    for raw in rows:
        r = {c: num(raw.get(c, 0)) for c in NUM_COLS}
        for c in NUM_COLS:
            total[c] += r[c]
        k = kpis(r)
        dec, motivo = decidir(r, k, a)
        nombre = raw.get("anuncio") or raw.get("conjunto") or raw.get("campana") or "?"
        print(f"| {nombre} | {fmt('g', r['gasto'])} | {k['_contactos']:.0f} | {r['leads_calificados']:.0f} | "
              f"{r['ventas']:.0f} | " + " | ".join(fmt(s, k[s]) for s in show) + f" | **{dec}** | {motivo} |")
        hoja.append([nombre, round(r["gasto"], 2), k["_contactos"], r["leads_calificados"], r["ventas"]]
                    + [("" if k[s] is None else round(k[s], 4)) for s in show] + [dec, motivo])

    k = kpis(total)
    print("\n## Totales")
    for key in ["CPM", "CTR", "CPC", "CPL", "Costo/conv", "%Calif", "Calif->Opor", "Opor->Cot",
                "Cot->Venta", "CPLc", "Costo/opor", "CPA", "ROAS"]:
        if k[key] is not None:
            print(f"- {key}: {fmt(key, k[key])}")
    print(f"- Gasto total: {fmt('g', total['gasto'])} · Leads/conversaciones: {k['_contactos']:.0f} · "
          f"Calificados: {total['leads_calificados']:.0f} · Oportunidades: {total['oportunidades']:.0f} · "
          f"Ventas: {total['ventas']:.0f} · Facturación: {fmt('g', total['facturacion'])}")
    if a.ticket and total["oportunidades"] and total["gasto"]:
        potencial = total["oportunidades"] * a.tasa_cierre * a.ticket / total["gasto"]
        print(f"- ROAS potencial estimado ({a.tasa_cierre:.0%} de cierre de oportunidades, "
              f"ticket {a.ticket:,.0f} {a.moneda}): {potencial:.2f}x")
    if a.xlsx:
        totales = [["KPI", "Valor"]] + [[key, ("" if k[key] is None else round(k[key], 4))] for key in
                                        ["CPM", "CTR", "CPC", "CPL", "Costo/conv", "%Calif", "Calif->Opor",
                                         "Opor->Cot", "Cot->Venta", "CPLc", "Costo/opor", "CPA", "ROAS"]]
        totales += [["Gasto total", round(total["gasto"], 2)], ["Moneda", a.moneda]]
        write_xlsx(a.xlsx, [("KPIs por anuncio", hoja), ("Totales", totales)], title="KPIs")
        print(f"\nKPIs guardados en {a.xlsx} (tasas como fracción: 0.013 = 1,3 %)")


if __name__ == "__main__":
    main()
