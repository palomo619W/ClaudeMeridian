# Meta Ads (Facebook + Instagram)

## Qué definir en cada campaña
Objetivo · arquitectura campaña → conjunto → anuncios · presupuesto (CBO o ABO) · ubicación geográfica · audiencias · segmentación · exclusiones · remarketing · lookalikes · canal de conversión · creativos · copies · CTA · hipótesis.

## Objetivos recomendados según la meta
| Meta de negocio | Objetivo de Meta | Evento de optimización |
|---|---|---|
| Llenar audiencias (TOFU) | Interacción o Reconocimiento | ThruPlay / reproducción de 2 s |
| Conversaciones con asesores | Clientes potenciales o Interacción → mensajes | Conversaciones por WhatsApp |
| Leads con datos | Clientes potenciales | Formulario instantáneo (mayor intención) |
| Leads en la web | Clientes potenciales o Ventas | Evento Lead (píxel + API de conversiones) |
| Calidad (cuenta madura) | Clientes potenciales | Lead calificado de CRM (conversion leads) |

## Arquitectura tipo (presupuesto medio)
```
C1 | PROSP | [Producto] | Leads-WA        (CBO)
   ├── AS1 Amplia Ecuador 25-65 (sin intereses; el creativo filtra)
   └── AS2 Intereses: transporte, buses, cooperativas, logística, flotas
        └── Anuncios: 3 conceptos (A/B/C)
C2 | RMK | [Producto] | Leads-Form      (ABO)
   └── AS1 Video 50 % 180 d + IG/FB interacción 180 d + web 90 d
        └── Anuncios: testimonio, configuración, oferta/financiamiento
C3 | TEST | [Hipótesis]                  (ABO, presupuesto fijo)
```
Nomenclatura: `ETAPA | PRODUCTO | CANAL | AUDIENCIA | FECHA`.

## Audiencias
- **Amplia:** Ecuador (o provincias prioritarias), 25–65 años, Advantage+ audience. En B2B con buen creativo suele ganar.
- **Intereses:** transporte público, autobús, cooperativas, logística, gestión de flotas, turismo, educación (escolar). Agrupa varios intereses en un conjunto; no hagas un conjunto por interés.
- **Datos demográficos o cargo:** propietarios de pequeñas empresas, cargos de gerencia (disponibilidad limitada en Ecuador).
- **Lookalike:** solo con semillas de al menos 100 personas y de calidad (clientes, leads calificados). 1–3 % en Ecuador.
- **Listas de clientes:** solo bases con consentimiento para comunicaciones.

## Exclusiones
- Leads ya enviados (30 días) en prospección.
- Clientes actuales cuando se busca captación (salvo campañas de renovación).
- Empleados y proveedores si existe la lista.
- Intereses de "empleo" o "busco trabajo" cuando hay ruido de postulantes a chofer.

## Canal de conversión
| Canal | Úsalo cuando | Ventaja | Riesgo |
|---|---|---|---|
| Formulario instantáneo | Hay que escalar volumen con un filtro de preguntas | Poca fricción, CPL bajo | Leads fríos, datos falsos |
| WhatsApp | Hay asesores con respuesta rápida | Conversación inmediata; así se compra en Ecuador | Saturación del equipo si no se filtra |
| Landing page | Hay píxel y API de conversiones, y el producto necesita explicarse | Mayor intención, mejor atribución | CPL más alto; depende de la velocidad de la web |

Recomendación por defecto para Miral: **WhatsApp en prospección y remarketing, formulario de mayor intención en BOFU**. Pruébalo contra la landing en la bolsa de experimentación.

## Ubicaciones
Advantage+ placements, revisando el reparto. Si Audience Network trae leads basura, exclúyelo.
