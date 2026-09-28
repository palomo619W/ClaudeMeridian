#!/usr/bin/env python3
"""Calcula KPIs de pauta y de embudo comercial y sugiere APAGAR / MANTENER / ESCALAR.

Uso:
    python3 calcular_kpis.py resultados.csv --cplc-objetivo 60 [--cpl-objetivo 15] [--ticket 120000]

El CSV debe tener las columnas de assets/plantillas/resultados-campana.csv.
Las reglas replican references/optimizacion.md.
"""
import argparse
import csv
import sys

NUM_COLS = ["presupuesto", "gasto", "impresiones", "clics", "leads", "conversaciones",
            "leads_calificados", "oportunidades", "cotizaciones", "ventas", "facturacion"]


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
        "CPM": div(r["gasto"], r["impresiones"] / 1000) if r["impresiones"] else None,
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
        "CAC": div(r["gasto"], r["ventas"]),
        "ROAS": div(r["facturacion"], r["gasto"]),
        "_contactos": contactos,
    }


def decidir(r, k, cplc_obj, cpl_obj):
    contactos = k["_contactos"]
    if r["impresiones"] < 1000:
        return "DATOS INSUFICIENTES", "menos de 1 000 impresiones"
    if cplc_obj and r["leads_calificados"] == 0 and r["gasto"] >= 3 * cplc_obj:
        return "APAGAR", f"gasto >= 3x CPLc objetivo ({3 * cplc_obj:.0f}) sin leads calificados"
    if cpl_obj and contactos == 0 and r["gasto"] >= 2 * cpl_obj:
        return "APAGAR", f"gasto >= 2x CPL objetivo ({2 * cpl_obj:.0f}) sin leads"
    if contactos >= 20 and (k["%Calif"] or 0) < 0.10:
        return "APAGAR", "menos del 10 % de leads calificados con 20 o más leads"
    if r["impresiones"] > 2000 and (k["CTR"] or 0) < 0.005:
        return "CAMBIAR HOOK", "CTR < 0,5 % con más de 2 000 impresiones"
    if cplc_obj and k["CPLc"] is not None and k["CPLc"] <= 0.8 * cplc_obj and r["leads_calificados"] >= 5:
        return "ESCALAR", "CPLc <= 80 % del objetivo con 5 o más calificados (+20 % cada 48-72 h)"
    if cplc_obj and k["CPLc"] is not None and k["CPLc"] > 1.2 * cplc_obj:
        return "REVISAR", "CPLc > 120 % del objetivo"
    return "MANTENER", "dentro de rango o acumulando datos"


def fmt(key, v):
    if v is None:
        return "-"
    if key in ("CTR", "%Calif", "Calif->Opor", "Opor->Cot", "Cot->Venta"):
        return f"{v * 100:.1f}%"
    if key == "ROAS":
        return f"{v:.1f}x"
    return f"${v:,.2f}"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv")
    p.add_argument("--cplc-objetivo", type=float, help="CPL calificado objetivo (USD)")
    p.add_argument("--cpl-objetivo", type=float, help="CPL objetivo (USD)")
    p.add_argument("--ticket", type=float, help="Valor promedio de venta, para estimar el ROAS potencial")
    a = p.parse_args()

    with open(a.csv, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("El CSV no tiene filas.")

    total = {c: 0.0 for c in NUM_COLS}
    show = ["CPM", "CTR", "CPC", "CPL", "%Calif", "CPLc", "Costo/opor", "CAC", "ROAS"]
    print("| Anuncio | Gasto | Leads | Calif. | " + " | ".join(show) + " | Decisión | Motivo |")
    print("|" + "---|" * (len(show) + 6))
    for raw in rows:
        r = {c: num(raw.get(c, 0)) for c in NUM_COLS}
        for c in NUM_COLS:
            total[c] += r[c]
        k = kpis(r)
        dec, motivo = decidir(r, k, a.cplc_objetivo, a.cpl_objetivo)
        nombre = raw.get("anuncio") or raw.get("conjunto") or raw.get("campana") or "?"
        print(f"| {nombre} | ${r['gasto']:,.2f} | {k['_contactos']:.0f} | {r['leads_calificados']:.0f} | "
              + " | ".join(fmt(s, k[s]) for s in show) + f" | **{dec}** | {motivo} |")

    k = kpis(total)
    print("\n## Totales")
    for key in ["CPM", "CTR", "CPC", "CPL", "Costo/conv", "%Calif", "Calif->Opor", "Opor->Cot",
                "Cot->Venta", "CPLc", "Costo/opor", "CAC", "ROAS"]:
        print(f"- {key}: {fmt(key, k[key])}")
    print(f"- Gasto total: ${total['gasto']:,.2f} · Leads/conversaciones: {k['_contactos']:.0f} · "
          f"Calificados: {total['leads_calificados']:.0f} · Oportunidades: {total['oportunidades']:.0f} · "
          f"Ventas: {total['ventas']:.0f}")
    if a.ticket and total["oportunidades"] and total["gasto"]:
        # ROAS potencial suponiendo un cierre del 15 % de las oportunidades (línea base)
        potencial = total["oportunidades"] * 0.15 * a.ticket / total["gasto"]
        print(f"- ROAS potencial estimado (15 % de cierre de oportunidades, ticket ${a.ticket:,.0f}): {potencial:.1f}x")


if __name__ == "__main__":
    main()
