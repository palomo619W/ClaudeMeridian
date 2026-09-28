# Rutina 03 — Distribución de presupuesto

1. Confirma el monto (diario o mensual, en USD), el periodo y las líneas de producto a cubrir.
2. Determina la madurez de la cuenta: **nueva** (sin audiencias ni píxel con datos), **media** (audiencias de menos de 10 000 personas o menos de 3 meses de datos) o **madura**.
3. Ejecuta `python3 scripts/distribuir_presupuesto.py <monto_mensual> --madurez <nivel> [--cpl-objetivo X]`.
4. Presenta la tabla Prospección / Remarketing / Experimentación con USD mensuales, USD diarios y número máximo de conjuntos.
5. Explica **por qué** esa distribución (madurez, tamaño de las audiencias, necesidad de aprendizaje).
6. Si el presupuesto no alcanza para todos los productos, recomienda priorizar uno (el de mayor margen × probabilidad de cierre) y dejar los demás para la siguiente fase.
