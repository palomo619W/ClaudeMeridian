# Rutina 01 — "Quiero pautar [PRODUCTO]"

**Resultado:** respuesta completa con las 20 secciones más la **DECISIÓN DEL TRAFFICKER**, según `assets/plantillas/respuesta-campana.md`.

## Paso 1 — Diagnóstico (metodología)
- Recorre la cadena Producto → … → Venta (`references/metodologia.md`).
- Si falta el **producto** o la **zona**, pregunta y detente.
- Para los demás datos faltantes, usa SUPUESTOS explícitos.
- Calcula los techos económicos (CAC máximo, costo máximo por oportunidad, CPLc máximo, CPL máximo).

## Paso 2 — Revisar el historial
- Si existe `data/historial-campanas.csv` con registros, ejecuta `python3 scripts/registrar_aprendizaje.py --resumen` o léelo. Si el usuario tiene el historial en otro lado, pídeselo.
- Identifica lo que ya funcionó (reutilízalo como control) y lo que falló (no lo repitas sin una hipótesis nueva).

## Paso 3 — Estrategia
- Define el funnel y la etapa de entrada según la madurez de la cuenta (`references/funnel.md`).
- Elige plataformas: Meta como base. Añade Google Search si hay demanda de búsqueda y TikTok solo para TOFU (`references/plataformas/`).
- Elige el canal de conversión (formulario, WhatsApp o landing) y justifícalo.

## Paso 4 — Presupuesto
- Ejecuta `python3 scripts/distribuir_presupuesto.py <monto> --madurez <nueva|media|madura>` o aplica `references/presupuesto.md`.
- Ajusta el número de conjuntos al presupuesto (regla de concentración).

## Paso 5 — Creativos
- Mínimo 3 conceptos con la ficha completa (`references/creativos.md`), cada uno con su hipótesis.

## Paso 6 — Leads y medición
- Preguntas de calificación y mecanismos anti-ruido (`references/leads-calificacion.md`).
- Plan de medición y atribución (`references/medicion-kpis.md`).

## Paso 7 — Redacción
- Completa `assets/plantillas/respuesta-campana.md` sección por sección.
- Termina con la DECISIÓN DEL TRAFFICKER: qué se lanza HOY, cuánto por campaña y qué hipótesis se valida.
- Añade al final "Supuestos a validar" y "Preguntas pendientes" si las hay.

## Autorrevisión antes de entregar
- [ ] ¿Están las 20 secciones más la Decisión?
- [ ] ¿Cada campaña o conjunto tiene una hipótesis?
- [ ] ¿El presupuesto por conjunto alcanza para salir del aprendizaje?
- [ ] ¿Hay criterios numéricos para apagar y escalar?
- [ ] ¿Los copies evitan frases corporativas genéricas?
- [ ] ¿La métrica principal es el CPLc, el costo por oportunidad o el CAC, y no el CPL?
