# Medición y KPIs

## Fórmulas
| KPI | Fórmula |
|---|---|
| CPM | gasto / impresiones × 1000 |
| CTR (enlace) | clics en el enlace / impresiones |
| CPC | gasto / clics en el enlace |
| CPL | gasto / leads |
| Costo por conversación | gasto / conversaciones iniciadas |
| Tasa de conversión (landing) | leads / visitas a la landing |
| Lead → lead calificado | leads calificados / leads |
| Lead calificado → oportunidad | oportunidades / leads calificados |
| Oportunidad → cotización | cotizaciones / oportunidades |
| Cotización → venta | ventas / cotizaciones |
| CPL calificado (CPLc) | gasto / leads calificados |
| Costo por oportunidad | gasto / oportunidades |
| CAC (pauta) | gasto / ventas |
| ROAS | facturación atribuida / gasto |
| ROI de marketing | (margen bruto atribuido − gasto) / gasto |

**Jerarquía:** Costo por venta y ROI > costo por oportunidad > CPLc > CPL > CPC/CTR/CPM. Las métricas de arriba deciden; las de abajo solo diagnostican.

## Cómo medir las ventas originadas por publicidad
1. **UTMs** en todos los enlaces: `utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`.
2. **Formularios instantáneos:** conectar al CRM (integración nativa, Zapier/Make o descarga diaria) guardando el *lead ID*, la campaña y el anuncio.
3. **WhatsApp:** anuncios *Click-to-WhatsApp* con mensaje prellenado que incluya un código por campaña (p. ej. "Hola, quiero cotizar un bus escolar [ESC01]"). El asesor registra el código.
4. **CRM:** campos obligatorios de fuente, campaña, anuncio, puntaje de calificación, etapa, valor y fecha de cierre.
5. **Retroalimentación a la plataforma:** subir las etapas (lead calificado, oportunidad, venta) como eventos offline o de CRM con la API de conversiones de Meta y como conversiones offline en Google Ads.
6. **Atribución de ciclo largo:** evaluar por *cohortes de mes de generación del lead*, no por mes de cierre. Una venta de septiembre puede venir de un lead de abril.
7. **Pregunta de autodeclaración** en la primera llamada: "¿Cómo se enteró de Miral?"

## Reglas de lectura
- No juzgues un anuncio con menos de ~1 000 impresiones ni un conjunto con menos de ~50 conversiones de optimización (fase de aprendizaje de Meta). Etiquétalo como *datos insuficientes*.
- Compara siempre contra la campaña anterior equivalente y contra `lineas-base.md`.
- Cuando el volumen sea bajo, informa rangos y no conclusiones absolutas.
