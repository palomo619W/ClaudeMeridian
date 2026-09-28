# Rutina 03 — Distribución de presupuesto

1. Confirma el monto (diario o mensual), la moneda, el periodo y las líneas de producto a cubrir. Toma lo que ya esté en la ficha.
2. Determina la madurez de la cuenta (nueva / media / madura, según `references/presupuesto.md`). Si no se sabe, pregunta: "¿Has hecho publicidad antes y tienes el píxel instalado?"
3. Ejecuta `python3 scripts/distribuir_presupuesto.py <monto_mensual> --madurez <nivel> --moneda <M> [--cpl-objetivo X]`.
4. Presenta la tabla Prospección / Remarketing / Experimentación con montos mensuales, montos diarios y número máximo de conjuntos.
5. Explica **por qué** esa distribución (madurez, tamaño de las audiencias, necesidad de aprendizaje, modelo de negocio).
6. Si el presupuesto no alcanza para todos los productos, prioriza el de mayor margen × probabilidad de venta y deja los demás para la siguiente fase.
7. Guarda el presupuesto en la ficha.
