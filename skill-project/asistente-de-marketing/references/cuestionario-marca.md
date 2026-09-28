# Entrevista de marca: cómo captar toda la información

Para una **marca nueva**, la skill capta **toda** la información inicial en una sola entrevista guiada **antes de generar cualquier archivo**. Así los documentos se crean una sola vez, completos, en lugar de regenerarse cada vez que aparece un dato nuevo.

La entrevista tiene dos tipos de preguntas:
- **Cerradas → ventana de opciones (pop-up):** el usuario solo hace clic. Es lo rápido y lo que más reduce errores.
- **Abiertas → un único mensaje de detalle:** nombre, web, productos, cifras exactas. Se piden todas juntas en un solo mensaje, con un ejemplo de respuesta.

---

## 1. Cómo mostrar las ventanas de opciones

Usa la herramienta de preguntas interactivas del entorno:
- **Claude Code / Cowork / escritorio:** `AskUserQuestion`.
- **claude.ai:** la herramienta de entrada con opciones (por ejemplo `ask_user_input`), si está disponible.

Reglas de diseño (son los límites de `AskUserQuestion`; respétalos también en otras herramientas):
| Regla | Valor |
|---|---|
| Preguntas por ventana | Hasta 4 (si la herramienta admite menos, divide la ronda) |
| Opciones por pregunta | Entre 2 y 4. La herramienta agrega sola la opción "Otro" (texto libre); **no** la incluyas tú |
| Encabezado (`header`) | Máximo 12 caracteres (p. ej. "Modelo", "Público", "Presupuesto") |
| Opción múltiple | `multiSelect: true` cuando puede haber varias respuestas (público, canales, material) |
| Cada opción | `label` corto (1–5 palabras) + `description` de una línea que explique qué implica |
| Recomendación | Si una opción es la recomendada para ese negocio, ponla primero y agrega "(Recomendado)" |

**Si no hay herramienta de ventanas** (o falla), muestra la misma ronda como texto: preguntas numeradas con opciones con letra, y pide responder en una línea, por ejemplo: *"1b · 2a,c · 3d · 4: no sé"*.

### Cuándo pedir detalle después de una opción
Si el usuario elige **"Otro"**, o una opción que por naturaleza es amplia (por ejemplo "Varios segmentos", "Mixto", "Otra categoría regulada"), anota la pregunta y pídele una **descripción precisa en el mensaje de detalle** (sección 3), con un ejemplo: *"Describe en una línea a ese público: cargo, tipo de empresa y tamaño. Ej.: 'jefes de compras de constructoras medianas'"*.

---

## 2. Flujo para una marca nueva (captación completa)

Todo ocurre **antes** de crear archivos. Tiempo estimado para el usuario: 3–5 minutos de clics y un mensaje corto.

| Paso | Qué haces | Formato |
|---|---|---|
| **A. Extraer** | Si el usuario adjuntó o pegó web, brief, catálogo o PDF, léelo. Todo lo que puedas deducir se **confirma** en lugar de preguntarse | — |
| **B. Datos base** | Pide en un solo mensaje los datos abiertos esenciales (bloque B) | Mensaje de texto |
| **C. Rondas 1–5** | Muestra las 5 ventanas de opciones (sección 4), una tras otra, **sin comentarios largos entre ellas** (una línea como máximo: "Perfecto, sigamos con tu cliente") | Pop-up |
| **D. Detalle** | Un único mensaje con las preguntas abiertas que quedaron (bloque D) y los "Otro" que requieren precisión | Mensaje de texto |
| **E. Confirmación** | Muestra un resumen de la ficha en el chat (8–12 viñetas) y una última ventana: *"¿Genero ahora tu ficha y tu primera propuesta?"* → **Generar ahora (Recomendado)** / **Corregir algo antes** | Pop-up |
| **F. Generar una sola vez** | Crea la ficha (`perfil-marca.docx`) y el primer entregable que el usuario pidió, en una sola pasada | Archivos .docx / .xlsx |

**Omite** cualquier pregunta ya respondida en la conversación, deducida en el paso A o presente en una ficha existente. Si una ronda queda con 0 preguntas, sáltala. Si quedan 1–3, igual muéstralas en una ventana.

### Bloque B — Datos base (primer mensaje)
> ¡Hola! Seré tu trafficker digital. Para no hacerte perder tiempo, primero conozco tu marca completa y luego genero todo de una vez. Empecemos con 4 datos (puedes adjuntar tu web, catálogo o brief si lo tienes):
> 1. **Nombre de la marca** y web o redes.
> 2. **Qué vendes** y cuál es tu producto o servicio estrella.
> 3. **País y ciudades** donde vendes.
> 4. **Valor promedio de una venta** y moneda (un rango está bien).
>
> Después te muestro unas preguntas rápidas con opciones para que solo hagas clic.

Con estas respuestas adapta las opciones de las rondas: moneda local, ejemplos del sector, tipo de público.

### Bloque D — Detalle final (mensaje único, solo lo que falte)
Pide en un solo mensaje, numerado y con ejemplo en cada punto:
1. **Competidores** principales (nombres o cuentas de Instagram).
2. **2–3 razones concretas** por las que te eligen (si en la ronda 4 marcó opciones generales, pide el dato real: "¿entrega en cuántas horas?", "¿qué garantía?").
3. **Oferta o promoción vigente**, si marcó que tiene una (qué es y hasta cuándo).
4. **Presupuesto exacto** si eligió un rango amplio.
5. **Descripción precisa** de cada respuesta "Otro" o amplia de las rondas.
6. **Qué NO se puede decir o prometer**, si marcó una categoría regulada.

"No sé" o "no aplica" son respuestas válidas: aplica el valor por defecto y márcalo como SUPUESTO.

---

## 3. Preguntas abiertas: cómo pedirlas bien
- Todas juntas, en un solo mensaje. Nunca una por mensaje.
- Cada una con un ejemplo concreto del sector del usuario.
- Explica en pocas palabras para qué sirve cuando no sea obvio ("con esto calculo cuánto puedes pagar por cliente").
- Si la respuesta llega vaga ("vendemos de todo", "a todo público"), repregunta **una sola vez**, con 2–3 alternativas concretas.

---

## 4. Rondas de preguntas con opciones

Las opciones marcadas **[adaptar]** cambian según el modelo de negocio (ronda 1) o el sector (bloque B). Los rangos de dinero están en USD como referencia: **conviértelos a la moneda local** del usuario con cifras redondas.

### Ronda 1 — Tu negocio
| Header | Pregunta | Tipo | Opciones (label — description) | Campo de la ficha |
|---|---|---|---|---|
| Modelo | ¿Cómo vendes principalmente? | única | Tienda online — Venden y cobran en su web · Servicio o local — Atienden con cita o en un local · A empresas (B2B) — Sus clientes son empresas · A gobierno (B2G) — Venden por licitaciones o compras públicas | Modelo de negocio |
| Objetivo | ¿Qué resultado quieres de la publicidad? | única | Ventas online · Leads o cotizaciones · Mensajes de WhatsApp · Citas o visitas **[adaptar: recomendada según el modelo]** | Objetivo principal |
| Cobertura | ¿Hasta dónde llegas? | única | Una ciudad o zona · Varias ciudades · Todo el país · Varios países | País, ciudades o zonas |
| Experiencia | ¿Has hecho publicidad pagada antes? | única | Nunca · Solo "Promocionar" en redes · Campañas sin medir bien · Campañas con resultados medidos | Historial de campañas |

### Ronda 2 — Tu cliente
| Header | Pregunta | Tipo | Opciones [adaptar] | Campo de la ficha |
|---|---|---|---|---|
| Público | ¿A qué tipo de público va dirigido? | múltiple | **B2B/B2G:** Gerentes · Empresarios · Dueños de negocio · Instituciones públicas — **B2C:** Mujeres · Hombres · Familias o padres · Jóvenes — **Servicio local:** Vecinos de la zona · Profesionales · Familias · Empresas | Cliente ideal |
| Edad | ¿Qué edad tiene la mayoría de tus clientes? | múltiple | 18–24 · 25–34 · 35–44 · 45 o más | Cliente ideal |
| Decisor | ¿Quién toma la decisión de compra? | única | La misma persona que usa el producto · El dueño o gerente · Un comité, socios o consejo · Compras o licitación | Cliente ideal (quién decide) |
| Ciclo | ¿Cuánto tarda un cliente en decidirse? | única | El mismo día · Unos días · Semanas · Meses | Duración del ciclo de venta |

### Ronda 3 — Economía y atención
| Header | Pregunta | Tipo | Opciones | Campo de la ficha |
|---|---|---|---|---|
| Presupuesto | ¿Cuánto quieres invertir en anuncios al mes? | única | Menos de 300 USD · 300–1 000 USD · 1 000–3 000 USD · Más de 3 000 USD **[convertir a moneda local]** | Presupuesto mensual |
| Margen | ¿Qué margen te queda por venta, aprox.? | única | Menos del 20 % · 20–40 % · 40–60 % · Más del 60 % *(si elige "Otro: no sé", usa el valor por defecto del modelo)* | Margen o CAC máximo |
| Canal | ¿Dónde quieres recibir a los interesados? | múltiple | WhatsApp · Formulario · Web o carrito · Llamada | Canal de conversión |
| Respuesta | ¿Qué tan rápido pueden responder? | única | En menos de 15 minutos · En el mismo día · Al día siguiente · No hay quien atienda | Canal y quién atiende |

### Ronda 4 — Oferta y creatividad
| Header | Pregunta | Tipo | Opciones [adaptar al sector] | Campo de la ficha |
|---|---|---|---|---|
| Diferencial | ¿Por qué te eligen frente a la competencia? | múltiple | Precio · Calidad o garantía · Rapidez o disponibilidad · Atención y posventa | Diferenciadores |
| Objeciones | ¿Qué frena más a tus clientes antes de comprar? | múltiple | El precio · No conocen la marca · El tiempo de entrega · Deben consultarlo con alguien | Objeciones frecuentes |
| Material | ¿Qué material tienes para los anuncios? | múltiple | Fotos profesionales · Videos · Testimonios de clientes · Nada todavía | Material creativo |
| Plataformas | ¿En qué plataformas quieres anunciar? | múltiple | Meta (Facebook e Instagram) (Recomendado) · Google · TikTok · LinkedIn | Plataformas activas |

### Ronda 5 — Medición y reglas
| Header | Pregunta | Tipo | Opciones | Campo de la ficha |
|---|---|---|---|---|
| Píxel | ¿Tienes instalado el píxel de Meta o Google Analytics? | única | Sí, ambos o alguno · No · No sé qué es | Píxel / API / GA4 |
| Registro | ¿Dónde registras tus clientes y ventas? | única | Un CRM (HubSpot, Zoho…) · Excel o Google Sheets · La tienda online · En ningún lado | CRM o registro de ventas |
| Regulado | ¿Tu producto está en una categoría regulada? | única | No · Salud o estética · Finanzas o crédito · Otra (alcohol, vivienda, empleo, política) | Restricciones |
| Oferta | ¿Tienes una oferta que dé razón para comprar ya? | única | Descuento o promoción · Envío gratis o regalo · Pago en cuotas o financiamiento · Ninguna por ahora | Ofertas vigentes |

**Mapeo a la ficha:** guarda la opción elegida con palabras claras (no la letra) en el campo indicado. Por ejemplo: `- **Cliente ideal (quién compra / quién decide)** [N1]: Gerentes y dueños de negocio, 35–44 y 45 o más; decide el dueño`.

---

## 5. Cuando falta información en una tarea posterior

Con la ficha ya creada, si una tarea necesita un dato que no está:
1. **Reúne primero todos los datos que faltan para esa tarea.** No preguntes uno, generes, y luego preguntes otro.
2. Muéstralos en **una sola ventana de opciones** (hasta 4 preguntas), usando las preguntas de la sección 4 que correspondan. Los abiertos van en un solo mensaje corto.
3. Genera el archivo **una sola vez**, con todo. Registra los datos nuevos en la ficha.
4. Si el usuario pide cambios a un archivo ya generado, pregunta en una ventana si hay **algo más que ajustar** (*Solo eso · Quiero cambiar más cosas*) y regenera una sola vez con todos los cambios juntos.

## 6. Valores por defecto (si responde "no sé")
| Dato | Valor por defecto |
|---|---|
| Margen | E-commerce 30 %, servicios 50 %, B2B 15 %, B2G 15 % |
| Ciclo de venta | Según el modelo (`modelos-de-negocio.md`) |
| Canal | WhatsApp si hay quien atienda en el mismo día; si no, formulario |
| Plataformas | Meta |
| Material | Guiones grabables con el celular |
| Píxel | Asumir que no está instalado y proponer la instalación |
| Definición de lead calificado | Criterios por defecto de `leads-calificacion.md` |

Todo valor por defecto se marca como **(SUPUESTO)** en la ficha y en los entregables.
