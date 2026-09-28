# Medición y KPIs

## Fórmulas
| KPI | Fórmula |
|---|---|
| CPM | gasto / impresiones × 1000 |
| CTR (enlace) | clics en el enlace / impresiones |
| CPC | gasto / clics en el enlace |
| CPL | gasto / (leads + conversaciones) |
| Costo por conversación | gasto / conversaciones iniciadas |
| Tasa de conversión (landing) | conversiones / visitas a la landing |
| Lead → lead calificado | leads calificados / leads |
| Lead calificado → oportunidad | oportunidades / leads calificados |
| Oportunidad → cotización | cotizaciones / oportunidades |
| Cotización → venta | ventas / cotizaciones |
| CPL calificado (CPLc) | gasto / leads calificados |
| Costo por oportunidad | gasto / oportunidades |
| CPA / CAC (pauta) | gasto / ventas |
| ROAS | facturación atribuida / gasto |
| ROI de marketing | (margen bruto atribuido − gasto) / gasto |

**Jerarquía:** la métrica final del modelo de negocio (ver `modelos-de-negocio.md`) decide. Las métricas de plataforma (CPM, CTR, CPC) solo diagnostican.

## Cómo medir las ventas originadas por publicidad
1. **UTMs** en todos los enlaces: `utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}` (o las variables equivalentes de cada plataforma).
2. **Píxel + API de conversiones** (Meta), píxel de TikTok y etiqueta de Google con los eventos del modelo (Purchase, Lead, Contact, Schedule).
3. **Formularios instantáneos:** conectarlos al CRM o a una hoja de cálculo guardando el ID del lead, la campaña y el anuncio.
4. **WhatsApp:** anuncios click-to-WhatsApp con mensaje prellenado que incluya un código por campaña (p. ej. "Hola, quiero info [PROMO01]"). Quien atiende registra el código.
5. **CRM o registro de ventas:** campos de fuente, campaña, anuncio, puntaje, etapa, valor y fecha.
6. **Retroalimentación a la plataforma:** subir las etapas de ventas o leads calificados como eventos offline o de CRM (API de conversiones de Meta, conversiones offline de Google).
7. **Ciclos largos:** evaluar por cohortes del mes en que se generó el lead, no por el mes de cierre.
8. **Autodeclaración:** preguntar "¿Cómo nos conociste?" en el primer contacto o en el checkout.

## Reglas de lectura
- No juzgues un anuncio con menos de ~1 000 impresiones ni un conjunto con menos de ~50 conversiones de optimización (fase de aprendizaje). Etiquétalo como *datos insuficientes*.
- Compara siempre contra el periodo anterior equivalente, el historial de la marca y `lineas-base.md`.
- Con volúmenes bajos, informa rangos y no conclusiones absolutas.
