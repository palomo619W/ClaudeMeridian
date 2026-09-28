#!/usr/bin/env python3
"""Distribuye un presupuesto mensual entre Prospección / Remarketing / Experimentación.

Uso:
    python3 distribuir_presupuesto.py 1500 --madurez nueva [--cpl-objetivo 12]

Madurez: nueva (sin audiencias), media (audiencias de menos de 10 000 personas), madura.
Las reglas replican references/presupuesto.md.
"""
import argparse

SPLITS = {
    "nueva": (0.65, 0.15, 0.20),
    "media": (0.55, 0.25, 0.20),
    "madura": (0.50, 0.30, 0.20),
}
MIN_CONJUNTO_MES = 450.0  # USD/mes por conjunto (~15 USD/día)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("mensual", type=float, help="Presupuesto mensual en USD")
    p.add_argument("--madurez", choices=SPLITS, default="nueva")
    p.add_argument("--cpl-objetivo", type=float, help="Para estimar el mínimo que permite salir del aprendizaje")
    p.add_argument("--dias", type=int, default=30)
    a = p.parse_args()

    minimo = MIN_CONJUNTO_MES
    if a.cpl_objetivo:
        # 50 conversiones por semana es el umbral de aprendizaje de Meta; en B2B se acepta 50 al mes como mínimo práctico
        minimo = max(minimo, a.cpl_objetivo * 50)

    pro, rmk, exp = SPLITS[a.madurez]
    if a.mensual < 500:
        # Con poco dinero no hay remarketing útil ni margen para tests paralelos
        pro, rmk, exp = 0.80, 0.20, 0.0

    print(f"Presupuesto: ${a.mensual:,.2f}/mes · ${a.mensual / a.dias:,.2f}/día · madurez: {a.madurez}\n")
    print("| Bolsa | % | USD/mes | USD/día | Conjuntos máx. |")
    print("|---|---|---|---|---|")
    for nombre, pct in (("Prospección", pro), ("Remarketing", rmk), ("Experimentación", exp)):
        mes = a.mensual * pct
        conj = int(mes // minimo) if mes >= minimo else (1 if mes > 0 else 0)
        print(f"| {nombre} | {pct * 100:.0f}% | ${mes:,.2f} | ${mes / a.dias:,.2f} | {conj} |")

    total_conj = max(1, int(a.mensual // minimo))
    print(f"\nConjuntos activos recomendados en total: {total_conj} (mínimo ${minimo:,.0f}/mes por conjunto).")
    if a.mensual < 500:
        print("Presupuesto bajo: 1 campaña, 1-2 conjuntos, 3 anuncios. La experimentación se hace entre los anuncios del mismo conjunto.")
    elif a.madurez == "nueva":
        print("Cuenta nueva: se prioriza la prospección para construir audiencias de video y de interacción que alimenten el remarketing.")
    else:
        print("Con audiencias propias, el remarketing suele dar el CPLc más bajo: se le da más peso.")


if __name__ == "__main__":
    main()
