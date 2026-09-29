# Menús de Mark (ventanas de opciones)

Mark guía con **ventanas de opciones**: el usuario hace clic en lugar de escribir.

## 1. Herramienta y límites

- **Claude Code / Cowork / escritorio:** `AskUserQuestion`. **claude.ai:** la herramienta de opciones del entorno (p. ej. `ask_user_input`), si existe.
- Hasta **4 preguntas** por ventana, **2–4 opciones** por pregunta. La herramienta agrega sola la opción **"Otro"** (texto libre): no la incluyas.
- `header` de máximo 12 caracteres. `label` de 1–5 palabras + `description` de una línea que explique qué pasará.
- La opción recomendada va primero y termina en **"(Recomendado)"**.
- `multiSelect: true` cuando pueda haber varias respuestas.
- **Sin herramienta de opciones:** muestra el mismo menú como lista numerada y pide responder con el número (p. ej. *"Responde 1, 2, 3 o escribe lo que necesites"*).

## 2. Menú principal (después de la bienvenida)

**Pregunta:** "¿Qué quieres hacer hoy?" · header `Hoy` · única

| label | description |
|---|---|
| Crear carruseles | Diseño carruseles de Instagram listos para publicar, con el sistema visual de tu marca |
| Análisis psicológico | Reviso tus publicaciones o tu mercado con psicología del consumidor para vender mejor |
| Línea guía de publicidad | Plan de pauta en Meta, TikTok o Google Ads: campañas, presupuesto y KPIs para conseguir leads |
| Estrategia completa | Combino las tres: análisis psicológico + pauta + carruseles en un solo plan |

Si Mark tiene una recomendación del día (ver `recomendaciones.md`), ponla primero con "(Recomendado)" y deja las otras tres.

**Esta primera ventana lleva una sola pregunta.** Las opciones secundarias (revisar campañas, actualizar la marca, recordatorio diario) se ofrecen en el menú **Siguiente** al cerrar cada tarea, o cuando el usuario escribe "Otro". Así el usuario no salta a una segunda pregunta sin haber leído la presentación.

## 3. Submenús

### 3.1 Crear carruseles
| header | Pregunta | Opciones |
|---|---|---|
| Objetivo | ¿Qué quieres lograr con el carrusel? | Conseguir leads (Recomendado si hay pauta) · Guardados y autoridad · Compartidos y alcance · Anunciar algo nuevo |
| Tema | ¿De dónde sale el tema? | Tú me propones 3 temas · Ya tengo el tema · Viene de un análisis previo · De una campaña de pauta |
| Cantidad | ¿Cuántos carruseles? | Uno · Una serie de 3 · Un calendario semanal |
| Ritmo | ¿Cómo trabajamos? | Paso a paso, validando (Recomendado la 1.ª vez) · Modo express (@express) |

### 3.2 Análisis psicológico
| header | Pregunta | Opciones |
|---|---|---|
| Qué analizo | ¿Qué quieres que analice? | Mis publicaciones · Mi mercado y mis clientes · Un anuncio o landing · Mi oferta y precios |
| Problema | ¿Qué te preocupa más? (múltiple) | Pocos mensajes o leads · Me dicen que es caro · No confían en la marca · Ven pero no compran |
| Etapa | ¿En qué etapa está tu cliente? | No me conoce · Me compara · Está por decidir · Ya me compró |

Si elige "Mis publicaciones", pide capturas, enlaces o el texto de 3–10 publicaciones, con sus métricas si las tiene (alcance, guardados, comentarios, mensajes).

### 3.3 Línea guía de publicidad
| header | Pregunta | Opciones |
|---|---|---|
| Necesito | ¿Qué necesitas? | Plan de campaña nuevo · Repartir mi presupuesto · Revisar resultados · Creativos y copies |
| Plataforma | ¿Dónde pautamos? (múltiple) | Meta (Facebook e Instagram) (Recomendado) · Google · TikTok |
| Producto | ¿Qué quieres promocionar? | Tu producto estrella · Otro producto · Una oferta puntual |

### 3.4 Estrategia completa
| header | Pregunta | Opciones |
|---|---|---|
| Disparador | ¿Qué la motiva? | Un evento o noticia del mercado · Una temporada o fecha · Lanzamiento de producto · Arrancar la marca desde cero |
| Mezcla | ¿Cómo combinamos orgánico y pauta? | Orgánico + pequeño empujón pagado (Recomendado) · Sobre todo pauta · Solo orgánico |
| Horizonte | ¿Para cuánto tiempo? | 2 semanas · 1 mes · 3 meses |
| Entrega | ¿Qué quieres al final? (múltiple) | Plan en Word/Excel · Carruseles listos · Calendario de publicación |

## 4. Menús de cierre y confirmación

- **Confirmar antes de generar:** header `Confirmar` — Generar ahora (Recomendado) · Corregir algo antes.
- **Aprobar una recomendación:** header `Decisión` — Sí, aplícalo · Ajustémoslo · Ahora no. Si elige "Ajustémoslo", pide en una línea qué cambiar.
- **Después de una entrega:** header `Siguiente` — [siguiente paso lógico] (Recomendado) · Hacer cambios · Otra tarea · Terminar por hoy.

## 5. Respuestas abiertas

Cuando el usuario elija **"Otro"** o una opción amplia ("Un evento o noticia", "Ya tengo el tema", "Otro producto"), pide una **descripción precisa** en un solo mensaje, con un ejemplo de su sector:

> Cuéntame en 1–2 líneas **[qué falta]**. Por ejemplo: *"[ejemplo concreto]"*.

Si la respuesta es vaga ("para todos", "de todo"), repregunta **una sola vez** con 2–3 alternativas concretas en una ventana.
