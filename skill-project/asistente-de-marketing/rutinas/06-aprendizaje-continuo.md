# Rutina 06 — Aprendizaje continuo (memoria de campañas)

**Por qué:** la skill no tiene memoria entre conversaciones. Lo que aprende cada marca vive en su archivo `historial-campanas.csv` (ver `references/memoria-de-marca.md`), creado a partir de `assets/plantillas/historial-campanas.csv`.

## Campos que se registran
PRODUCTO · AUDIENCIA · CIUDAD · CREATIVO · HOOK · COPY · FORMATO · PRESUPUESTO · IMPRESIONES · CTR · CPC · CPL · LEADS · LEADS CALIFICADOS · COTIZACIONES · VENTAS · FACTURACIÓN (más fecha, plataforma, hipótesis, veredicto y aprendizaje).

## Pasos
1. Cuando haya resultados cerrados de un periodo o test, arma una fila por anuncio o variante.
2. Regístralas:
   `python3 scripts/registrar_aprendizaje.py --historial marketing/<marca>/historial-campanas.csv --agregar filas.csv`
   El historial puede ser `.csv` o `.xlsx`. Al usuario se le entrega siempre `historial-campanas.xlsx` (si mantienes un .csv de trabajo, conviértelo con `scripts/exportar_xlsx.py`). Si el usuario adjunta su historial en .xlsx, úsalo directamente con `--historial`.
3. Asigna el **veredicto**: GANADOR / PERDEDOR / NEUTRO / INSUFICIENTE, y una línea de **aprendizaje** (p. ej. "El hook de dolor supera al de producto en mujeres de 25 a 34 años: CPA 35 % menor").
4. Antes de cada campaña nueva, ejecuta `--resumen` para ver ganadores y perdedores por producto, audiencia, hook y formato.
5. Una estrategia PERDEDORA no se repite sin una **nueva hipótesis** escrita que explique qué cambió.
6. Con 4 semanas o más de datos, actualiza la línea base propia (sección 8 de la ficha) y, si los datos reales contradicen un SUPUESTO de la ficha (tasa de cierre, ticket), actualízalo y avisa.
