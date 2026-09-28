# Rutina 02 — Análisis de resultados y optimización

**Entrada:** capturas, tabla pegada, CSV o Excel exportado, o datos leídos desde un conector.
**Salida:** `assets/plantillas/reporte-optimizacion.md`.

## Pasos
1. **Obtener los datos.** Si hay conector (`references/conectores.md`), lee el periodo actual y el anterior equivalente. Si no, pide la exportación con las columnas de `assets/plantillas/resultados-campana.csv`. Pide también los datos del CRM: leads calificados, oportunidades, cotizaciones, ventas y facturación.
2. **Normalizar.** Convierte los datos al formato CSV de la plantilla y ejecuta:
   `python3 scripts/calcular_kpis.py resultados.csv --cplc-objetivo <X> [--cpl-objetivo <Y>] [--ticket <T>]`
   Si no hay un objetivo definido, derívalo con `references/metodologia.md` (techos económicos).
3. **Comparar** contra el periodo anterior, el historial (`data/historial-campanas.csv`) y `references/lineas-base.md`.
4. **Diagnosticar** con el protocolo de 7 puntos de `references/optimizacion.md`, empezando por las métricas de negocio y bajando hasta las de plataforma.
5. **Decidir:** tabla Apagar / Mantener / Escalar con el motivo, más los movimientos de presupuesto en USD.
6. **Nuevo test:** una sola variable, con hipótesis, presupuesto, duración y métrica de decisión.
7. **Aprender:** invoca la rutina 06 para registrar los resultados.

## Qué no hacer
- Decir "funcionó bien" o "funcionó mal" sin números ni causas.
- Cambiar audiencia, creativo y presupuesto al mismo tiempo en el mismo conjunto.
- Apagar conjuntos en fase de aprendizaje por un mal día.
