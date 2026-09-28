# Rutina 02 — Análisis de resultados y optimización

**Entrada:** capturas, tabla pegada, CSV o Excel exportado, o datos leídos desde un conector.
**Salida:** reporte con la estructura de `assets/plantillas/reporte-optimizacion.md`, entregado como **.docx** y con las tablas de KPIs en **.xlsx** (`references/formato-entrega.md`). Los resultados pueden llegar en .xlsx o .csv.

## Pasos
1. **Contexto:** lee la ficha de marca (objetivos, techos económicos, modelo de negocio). Si no hay objetivos, pregunta el ticket y el margen **en una sola ventana de opciones** junto con cualquier otro dato que falte (`references/cuestionario-marca.md`, sección 5), o calcula con los valores por defecto marcados como SUPUESTO. Genera el reporte una sola vez, cuando tengas todo.
2. **Obtener los datos:** si hay conector (`references/conectores.md`), lee el periodo actual y el anterior equivalente. Si no, pide la exportación con las columnas de `assets/plantillas/resultados-campana.csv`. Pide también los datos de negocio: leads calificados, oportunidades, ventas y facturación (CRM o tienda).
3. **Normalizar y calcular:** convierte los datos al CSV de la plantilla y ejecuta:
   `python3 scripts/calcular_kpis.py resultados.csv --cplc-objetivo <X> | --cpa-objetivo <Y> [--ticket <T>] [--tasa-cierre <p>] --moneda <M>`
4. **Comparar** contra el periodo anterior, el historial de la marca y `references/lineas-base.md`.
5. **Diagnosticar** con el protocolo de 7 puntos de `references/optimizacion.md`, de las métricas de negocio hacia las de plataforma.
6. **Decidir:** tabla Apagar / Mantener / Escalar con el motivo, más los movimientos de presupuesto.
7. **Nuevo test:** una sola variable, con hipótesis, presupuesto, duración y métrica de decisión.
8. **Aprender:** ejecuta la rutina 06 y actualiza la línea base propia en la ficha si hay 4 semanas o más de datos.
9. **Entregar:** `AAAA-MM-DD_reporte-optimizacion.docx` + `.xlsx`, con un resumen breve en el chat.

## Qué no hacer
- Decir "funcionó bien" o "funcionó mal" sin números ni causas.
- Cambiar audiencia, creativo y presupuesto al mismo tiempo en el mismo conjunto.
- Apagar conjuntos en fase de aprendizaje por un mal día.
