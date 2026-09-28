# Rutina 01 — "Quiero pautar [PRODUCTO]"

**Resultado:** respuesta completa con las 20 secciones más la **DECISIÓN DEL TRAFFICKER**, según `assets/plantillas/respuesta-campana.md`.

## Paso 1 — Contexto de la marca
- Lee la ficha de marca. Si no existe, haz primero el Nivel 1 de `00-onboarding.md` (puede ir en el mismo mensaje si el usuario ya dio casi todo).
- Identifica el modelo de negocio y aplica su columna de `references/modelos-de-negocio.md`.

## Paso 2 — Diagnóstico (metodología)
- Recorre la cadena Producto → … → Venta (`references/metodologia.md`).
- Si falta el **producto** o la **zona**, pregunta y detente.
- Si faltan datos de Nivel 2 que cambian la estrategia (presupuesto, canal de atención, margen), pregúntalos en un solo bloque de máximo 4 preguntas **o** avanza con SUPUESTOS explícitos si el usuario pidió rapidez.
- Calcula los techos económicos.

## Paso 3 — Revisar el historial
- Si hay historial de la marca, ejecuta `python3 scripts/registrar_aprendizaje.py --historial <ruta> --resumen`.
- Reutiliza lo que ganó como control. No repitas lo que perdió sin una hipótesis nueva.

## Paso 4 — Estrategia
- Define el funnel y la etapa de entrada según el modelo y la madurez de la cuenta (`references/funnel.md`).
- Elige plataformas según la ficha: Meta como base general; Google Search si hay demanda de búsqueda; TikTok si el público y el producto encajan (`references/plataformas/`).
- Elige el canal de conversión y justifícalo.

## Paso 5 — Presupuesto
- `python3 scripts/distribuir_presupuesto.py <monto> --madurez <nivel> --moneda <moneda>` o `references/presupuesto.md`.
- Ajusta el número de conjuntos al presupuesto (regla de concentración).

## Paso 6 — Creativos
- Mínimo 3 conceptos con ficha completa (`references/creativos.md`), usando los dolores, objeciones y diferenciadores de la ficha. Cada concepto con su hipótesis.

## Paso 7 — Leads y medición
- Preguntas de calificación adaptadas a la marca (`references/leads-calificacion.md`), o su reemplazo en e-commerce (eventos de compra).
- Plan de medición y atribución (`references/medicion-kpis.md`).

## Paso 8 — Redacción
- Completa la plantilla sección por sección.
- Termina con la DECISIÓN DEL TRAFFICKER: qué se lanza HOY, cuánto por campaña y qué hipótesis se valida.
- Cierra con "Supuestos usados" y "Preguntas para mejorar la ficha" (máximo 3).
- Actualiza la ficha con los datos nuevos que hayan surgido.

## Paso 9 — Entrega en Word y Excel
- Genera `AAAA-MM-DD_plan-campana_<producto>.docx` con `scripts/exportar_docx.py` y `…xlsx` con las tablas del plan usando `scripts/exportar_xlsx.py` (ver `references/formato-entrega.md`).
- En el chat: resumen de 3 a 6 líneas (DECISIÓN DEL TRAFFICKER + archivos entregados) y las preguntas para mejorar la ficha.

## Autorrevisión antes de entregar
- [ ] ¿Están las 20 secciones más la Decisión?
- [ ] ¿La moneda, el país y el cliente ideal salen de la ficha, sin supuestos ocultos?
- [ ] ¿Cada campaña o conjunto tiene una hipótesis?
- [ ] ¿El presupuesto por conjunto alcanza para salir del aprendizaje?
- [ ] ¿Hay criterios numéricos para apagar y escalar, basados en los techos?
- [ ] ¿Los copies evitan frases corporativas genéricas y promesas no confirmadas?
- [ ] ¿La métrica principal es la métrica final del modelo de negocio?
- [ ] ¿El plan se entregó en .docx (y sus tablas en .xlsx), sin archivos .md?
