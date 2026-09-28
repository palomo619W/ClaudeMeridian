# Conectores y fuentes de datos

La skill funciona sin conectores: pide al usuario capturas o archivos CSV/Excel exportados. Si en la sesión hay conectores o servidores MCP disponibles, úsalos para leer datos reales antes de opinar. No inventes métricas.

## Conectores recomendados
| Fuente | Uso en la skill | Datos a leer | Si no está disponible |
|---|---|---|---|
| **Meta Ads (Marketing API / MCP de Meta Ads)** | Resultados por campaña, conjunto y anuncio | Gasto, impresiones, alcance, frecuencia, clics, CTR, leads, conversaciones, ThruPlay | Exportar desde el Administrador de anuncios (columnas en `assets/plantillas/resultados-campana.csv`) |
| **Google Ads** | Search / Performance Max / YouTube | Gasto, clics, CPC, conversiones, términos de búsqueda | Exportar el informe de campañas |
| **TikTok Ads Manager** | Prospección con video | Gasto, impresiones, CTR, leads, retención de video | Exportar el informe |
| **GA4 / Google Tag Manager** | Comportamiento en la landing | Sesiones por UTM, tasa de conversión, eventos | Captura del informe de adquisición |
| **CRM (HubSpot, Zoho, Pipedrive, Salesforce, Google Sheets)** | Calidad del lead y ventas | Etapa, puntaje, valor, fuente, campaña, fecha de cierre | CSV con lead_id, campaña, etapa, valor |
| **WhatsApp Business (Cloud API / plataforma de mensajería)** | Conversaciones y códigos de campaña | Conversaciones iniciadas, respondidas, calificadas | Conteo manual por código de campaña |
| **Google Drive / Sheets** | Historial y material creativo | `historial-campanas`, briefs | Archivo local en `data/` |

## Cómo actuar
1. Revisa qué herramientas o conectores de la lista existen en la sesión.
2. Si existen, lee los datos del periodo pedido y del periodo anterior equivalente para poder comparar.
3. Si no existen, pide la exportación y explica qué columnas necesitas.
4. Nunca ejecutes acciones de escritura (pausar, activar o cambiar presupuesto) desde un conector sin la confirmación explícita del usuario: afectan dinero real.

## Configuración (para el usuario)
Los conectores se activan desde la configuración de Claude (Conectores / servidores MCP) o, en Claude Code, en el archivo de configuración de MCP del proyecto. La skill no guarda credenciales ni tokens.

## Eventos que conviene enviar a las plataformas
| Evento | Cuándo | Plataforma |
|---|---|---|
| Lead | Envío del formulario o primer mensaje | Meta / Google / TikTok |
| LeadCalificado | Puntaje ≥ 3 en el CRM | API de conversiones de Meta (evento offline/CRM), conversión offline en Google |
| Oportunidad | Etapa "Oportunidad" en el CRM | Igual |
| Venta (Purchase) | Contrato firmado, con valor | Igual |
