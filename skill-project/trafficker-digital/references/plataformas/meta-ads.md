# Meta Ads (Facebook + Instagram)

## Qué definir en cada campaña
Objetivo · arquitectura campaña → conjunto → anuncios · presupuesto (CBO o ABO) · ubicación geográfica · audiencias · segmentación · exclusiones · remarketing · lookalikes · canal de conversión · creativos · copies · CTA · hipótesis.

## Objetivo según la meta de negocio
| Meta de negocio | Objetivo de Meta | Evento de optimización |
|---|---|---|
| Llenar audiencias (TOFU) | Interacción o Reconocimiento | ThruPlay / reproducción de video |
| Ventas online | Ventas (Advantage+ shopping, catálogo) | Purchase (con valor) |
| Conversaciones | Interacción o Clientes potenciales → mensajes | Conversaciones por WhatsApp, Messenger o IG |
| Leads con datos | Clientes potenciales | Formulario instantáneo (volumen o mayor intención) |
| Leads o citas en la web | Clientes potenciales / Ventas | Lead / Schedule (píxel + API de conversiones) |
| Calidad (cuenta madura) | Clientes potenciales | Lead calificado desde el CRM |

## Arquitectura tipo (presupuesto medio)
```
C1 | PROSP | [Producto] | [Canal]     (CBO)
   ├── AS1 Amplia [país/zona] (sin intereses; el creativo filtra)
   └── AS2 Intereses agrupados del cliente ideal
        └── Anuncios: 3 conceptos (A/B/C)
C2 | RMK | [Producto] | [Canal]      (ABO)
   └── AS1 Video 50 % + interacción IG/FB + visitantes web (ventanas según el modelo)
        └── Anuncios: testimonio, objeción, oferta
C3 | TEST | [Hipótesis]               (ABO, presupuesto fijo)
```
Nomenclatura: `ETAPA | PRODUCTO | CANAL | AUDIENCIA | FECHA`.

## Audiencias
- **Amplia:** país o zonas de la ficha, rango de edad del cliente ideal, Advantage+ audience. Con un buen creativo suele ganar.
- **Intereses:** agrupa varios intereses afines al cliente ideal en un solo conjunto; no hagas un conjunto por interés.
- **Lookalike:** solo con semillas de al menos 100 personas y de calidad (compradores, leads calificados), al 1–3 %.
- **Listas de clientes:** solo bases con consentimiento para comunicaciones.
- **Categorías especiales** (crédito, empleo, vivienda, temas sociales): la segmentación es limitada. Decláralas y ajusta la estrategia.

## Exclusiones
- Quienes ya convirtieron en prospección (7–30 días).
- Clientes actuales cuando se busca captación (salvo campañas de recompra o upsell).
- Empleados y proveedores si existe la lista.
- Audiencias que generan ruido (p. ej. intereses de empleo si llegan postulantes).

## Canal de conversión
| Canal | Úsalo cuando | Ventaja | Riesgo |
|---|---|---|---|
| Web / catálogo | E-commerce con píxel y API de conversiones | Compra directa, ROAS medible | Depende de la web y el checkout |
| Formulario instantáneo | Hay que escalar volumen con filtro de preguntas | Poca fricción, CPL bajo | Leads fríos, datos falsos |
| WhatsApp | Hay quien atienda rápido; mercados donde se compra por chat | Conversación inmediata | Saturación si no se filtra |
| Landing page | El producto necesita explicarse y hay medición | Mayor intención, mejor atribución | CPL más alto |

Elige según el modelo (`modelos-de-negocio.md`) y la capacidad de atención de la ficha. Prueba el segundo mejor canal en la bolsa de experimentación.

## Ubicaciones
Advantage+ placements, revisando el reparto. Si Audience Network trae tráfico o leads de mala calidad, exclúyelo.
