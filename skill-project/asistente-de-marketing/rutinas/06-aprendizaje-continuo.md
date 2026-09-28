# Rutina 06 — Aprendizaje continuo (memoria de campañas)

**Por qué:** la skill no tiene memoria entre conversaciones. El conocimiento acumulado vive en `data/historial-campanas.csv`. Si ese archivo no está disponible en la sesión, pide al usuario el historial o genera las filas para que las pegue en su hoja.

## Campos que se registran
PRODUCTO · AUDIENCIA · CIUDAD · CREATIVO · HOOK · COPY · FORMATO · PRESUPUESTO · IMPRESIONES · CTR · CPC · CPL · LEADS · LEADS CALIFICADOS · COTIZACIONES · VENTAS · FACTURACIÓN (más fecha, plataforma, hipótesis y veredicto).

## Pasos
1. Cuando haya resultados cerrados de un periodo o test, arma una fila por anuncio o variante.
2. Registra con:
   `python3 scripts/registrar_aprendizaje.py --agregar fila.csv`
   o edita el CSV directamente.
3. Asigna el **veredicto**: GANADOR / PERDEDOR / NEUTRO / INSUFICIENTE, y una línea de **aprendizaje** ("Hook de costo por km supera al de fabricación local en cooperativas de la Sierra: CPLc 40 % menor").
4. Antes de cada campaña nueva ejecuta `python3 scripts/registrar_aprendizaje.py --resumen` para ver los ganadores y perdedores por producto, audiencia, hook y formato.
5. Si una estrategia fue PERDEDORA, no se repite sin escribir una **nueva hipótesis** que explique qué cambió.
6. Cuando haya 4 semanas o más de datos, actualiza la "Línea base propia" en `references/lineas-base.md`.
