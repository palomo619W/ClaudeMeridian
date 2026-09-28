# Conectores y fuentes de datos

La skill funciona sin conectores: pide al usuario capturas o archivos CSV/Excel exportados. Si en la sesión hay conectores o servidores MCP disponibles, úsalos para leer datos reales antes de opinar. Nunca inventes métricas.

## Conectores recomendados
| Fuente | Uso en la skill | Datos a leer | Si no está disponible |
|---|---|---|---|
| **Meta Ads (Marketing API / MCP de Meta Ads)** | Resultados por campaña, conjunto y anuncio | Gasto, impresiones, alcance, frecuencia, clics, CTR, leads, conversaciones, compras, valor de compra | Exportar desde el Administrador de anuncios (columnas de `assets/plantillas/resultados-campana.csv`) |
| **Google Ads** | Search / Shopping / Performance Max / YouTube | Gasto, clics, CPC, conversiones, valor, términos de búsqueda | Exportar el informe de campañas |
| **TikTok Ads Manager** | Prospección con video | Gasto, impresiones, CTR, conversiones, retención | Exportar el informe |
| **GA4 / Google Tag Manager** | Comportamiento en la web | Sesiones por UTM, conversiones, embudo de compra | Captura del informe de adquisición |
| **Tienda online (Shopify, WooCommerce, VTEX, Tiendanube)** | Ventas reales y ticket | Pedidos por UTM, ingresos, recompra | Export de pedidos con UTM |
| **CRM (HubSpot, Zoho, Pipedrive, Salesforce, Kommo, Google Sheets)** | Calidad del lead y ventas | Etapa, puntaje, valor, fuente, campaña, fecha de cierre | CSV con lead_id, campaña, etapa, valor |
| **WhatsApp Business (Cloud API o plataforma de mensajería)** | Conversaciones y códigos de campaña | Conversaciones iniciadas, respondidas, calificadas | Conteo manual por código de campaña |
| **Google Drive / Sheets / archivos locales** | Ficha de marca e historial | `perfil-marca.md`, `historial-campanas.csv`, briefs | Pedir que los adjunte |

## Cómo actuar
1. Revisa qué conectores o herramientas de la lista existen en la sesión.
2. Si existen, lee los datos del periodo pedido y del periodo anterior equivalente, para poder comparar.
3. Si no existen, pide la exportación y explica qué columnas necesitas. Sugiere en una línea qué conector ahorraría ese trabajo.
4. Nunca ejecutes acciones de escritura (pausar, activar o cambiar presupuesto) desde un conector sin la confirmación explícita del usuario: afectan dinero real.

## Configuración (para el usuario)
Los conectores se activan desde la configuración de Claude (Conectores / servidores MCP) o, en Claude Code, en el archivo de configuración de MCP del proyecto. La skill no guarda credenciales ni tokens.

## Eventos que conviene enviar a las plataformas
| Evento | Cuándo | Modelos |
|---|---|---|
| ViewContent / AddToCart / InitiateCheckout / Purchase (con valor) | Navegación y compra en la web | E-commerce |
| Lead / Contact / Schedule | Formulario, primer mensaje, cita | Servicios, B2B, educación |
| LeadCalificado (evento personalizado u offline) | Cuando el CRM marca el lead como calificado | B2B, ticket alto |
| Purchase offline (con valor) | Venta cerrada en el CRM | Todos los que cierran fuera de la web |
