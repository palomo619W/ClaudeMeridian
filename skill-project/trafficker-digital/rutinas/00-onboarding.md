# Rutina 00 — Onboarding: entrevista completa de marca

**Cuándo:** no existe la ficha de la marca, el usuario empieza con una marca nueva, o quiere volver a configurarla.
**Resultado:** ficha `perfil-marca.docx` completa y el primer entregable que el usuario pidió, **generados una sola vez**, al final de la entrevista.

**Por qué así:** si se pregunta poco, se genera, y luego se vuelve a preguntar, el usuario recibe los mismos documentos varias veces y pierde tiempo. Con una marca nueva conviene captar toda la información al inicio (con clics, no con redacción) y generar todo de una vez.

## Pasos
1. **Busca una ficha existente** (`references/memoria-de-marca.md`). Si la hay, no hagas la entrevista: ve a "Actualizar una ficha existente".
2. **Extrae lo que ya existe.** Si el usuario compartió web, redes, brief, PDF, catálogo o texto sobre la marca, léelo y rellena todo lo posible. Si hay herramientas de lectura web y dio la URL, úsalas. Lo deducido se confirma; no se vuelve a preguntar.
3. **Datos base (bloque B):** un solo mensaje con los 4 datos abiertos esenciales (nombre y web, qué vende y producto estrella, país y ciudades, valor promedio de venta y moneda). Omite los que ya tengas. Si el usuario ya pidió algo concreto ("quiero pautar X"), menciónalo: "Primero conozco tu marca y luego te entrego el plan completo".
4. **Rondas 1–5 con ventanas de opciones** (`references/cuestionario-marca.md`, sección 4):
   - Usa `AskUserQuestion` o la herramienta de opciones del entorno. Si no hay ninguna, usa texto numerado con opciones con letra.
   - Adapta las opciones al modelo de negocio y al sector, y los rangos de dinero a la moneda local.
   - Omite lo ya respondido. Entre rondas, como mucho una línea de transición: no generes análisis ni archivos todavía.
5. **Detalle (bloque D):** un único mensaje con las preguntas abiertas que falten y la descripción de cada "Otro" o respuesta amplia.
6. **Confirmación:** resume la ficha en el chat (8–12 viñetas, con los SUPUESTOS marcados) y muestra una ventana: **Generar ahora (Recomendado)** / **Corregir algo antes**. Si elige corregir, recoge todas las correcciones en un solo paso y vuelve a confirmar.
7. **Generar una sola vez:**
   - Rellena `assets/plantillas/perfil-marca.md` con las respuestas en palabras claras. "No sé" → valor por defecto + (SUPUESTO).
   - Calcula los techos económicos (sección 7 de la ficha, `references/metodologia.md`).
   - Exporta `marketing/<marca>/perfil-marca.docx` con `scripts/exportar_docx.py` (`references/formato-entrega.md`).
   - Si el usuario había pedido un entregable (plan de campaña, creativos, presupuesto), genéralo **en esta misma pasada** con la rutina correspondiente. Si no pidió nada, entrega la ficha y una recomendación de 3–5 viñetas sobre por dónde empezar.

## Actualizar una ficha existente
- Ejecuta `python3 scripts/verificar_perfil.py <ruta>/perfil-marca.docx` para ver los campos pendientes.
- Reúne **todos** los pendientes que la tarea actual necesita y pregúntalos en **una sola ventana** de opciones (hasta 4 preguntas de la sección 4 del cuestionario), más un mensaje corto para los datos abiertos.
- Regenera la ficha una sola vez y registra cada cambio con la fecha en "Registro de cambios".

## Tono
Cercano y breve. El usuario puede no saber qué es un CPL o un píxel: usa lenguaje simple y explica en pocas palabras los términos técnicos (también en las descripciones de las opciones).
