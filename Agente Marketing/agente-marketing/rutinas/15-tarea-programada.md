# Rutina 15 — Recordatorio diario (tarea programada)

**Objetivo:** que Mark le escriba al usuario **todos los días** para trabajar juntos (check-in de la rutina 14).
**Cuándo ofrecerlo:** al terminar el onboarding, al cerrar una estrategia compuesta, o cuando el usuario lo pida. Si `estado-mark.md` dice que ya existe, no lo vuelvas a ofrecer.

## 1. Preguntar lo mínimo (una ventana)

| header | Pregunta | Opciones |
|---|---|---|
| Hora | ¿A qué hora te escribo? | 8:00 a. m. (Recomendado) · 12:30 p. m. · 6:00 p. m. |
| Días | ¿Qué días? | Lunes a viernes (Recomendado) · Todos los días · Lunes, miércoles y viernes |
| Permisos | ¿Cómo trabajo en la tarea? | Pedir aprobación (Recomendado) · Aprobar automáticamente |

Recomienda **Pedir aprobación** porque así, aunque Mark solo lea tu información y te escriba el resumen, cualquier acción con conectores (Meta Ads, CRM) espera tu visto bueno. Si elige aprobar automáticamente, recuerda que la tarea tiene prohibido publicar, pautar o cambiar presupuestos.

La **zona horaria** sale de la ficha (país/ciudad). Si no está clara, pregúntala. Ejemplo: Ecuador continental = `America/Guayaquil`.

## 2. El contenido de la tarea (igual en cualquier entorno)

- **Nombre:** `Mark – check-in diario de marketing`
- **Instrucciones (prompt):**
  ```
  Usa la skill agente-marketing (Mark) y ejecuta su rutina 14 de check-in diario para la marca [Marca].
  Lee la memoria del proyecto (marketing/[marca]/estado-mark.md, perfil-marca.docx, historial-campanas.xlsx,
  sistema-visual.md y .agents/product-marketing.md). Salúdame como Mark y dame en máximo 6 líneas: qué toca hoy
  según el calendario, cómo van los resultados si hay datos, y una recomendación del día con su porqué.
  Termina con el menú "¿Qué quieres hacer hoy?". No publiques, no pautes ni cambies presupuestos.
  ```
- **Frecuencia:** diaria (o los días elegidos) a la hora elegida.
- **Modelo:** el predeterminado.

## 3. Crear la tarea según el entorno

Busca entre tus herramientas una que cree tareas programadas (nombres con *scheduled task*, *schedule*, *routine*, *trigger* o *cron*). Si hay una herramienta de búsqueda de herramientas, busca "scheduled task" primero.

| Entorno | Cómo |
|---|---|
| **Claude escritorio / Cowork** con herramienta de tareas programadas | Créala con el nombre, las instrucciones y la expresión cron. Ejemplo L–V 8:00 → `0 8 * * 1-5` (hora local del equipo). |
| **Claude Code en la web** (Routines: `create_trigger`) | `cron_expression` = `CRON_TZ=<zona> 52 7 * * 1-5` (adelanta unos minutos respecto a la hora en punto para evitar demoras), `create_new_session_on_fire: true`, notificaciones `{push: true}`, `initiation: human_request`. |
| **Claude Code CLI** (`CronCreate`) | Solo dura mientras la sesión está abierta: avísalo y sugiere la opción web o de escritorio para un recordatorio permanente. |
| **Sin herramienta** (p. ej. claude.ai web) | Guía al usuario para crearla a mano (sección 4). |

Confirma con el resultado real de la herramienta (nunca digas que quedó creada si no lo viste) y guarda en `estado-mark.md`: entorno, ID de la tarea, hora, días y fecha de creación.

## 4. Creación manual (ventana "Crear tarea programada")

Muéstrale exactamente qué poner en cada campo:

> Abre **Tareas programadas → Crear tarea programada** y completa:
> - **Nombre:** `Mark – check-in diario de marketing`
> - **Instrucciones:** *(pega el texto de la sección 2)*
> - **Modelo:** Modelo predeterminado
> - **Frecuencia:** Diaria → [hora elegida] (o los días elegidos)
> - **Permisos:** [la opción elegida]
> - Pulsa **Guardar**.
>
> Cuando la tengas, dime "listo" y la anoto en tu memoria.

## 5. Cambiar o pausar

Si el usuario pide otra hora, pausarla o quitarla, usa la misma herramienta (actualizar o borrar por ID) y actualiza `estado-mark.md`. Sin herramienta, indícale dónde editarla a mano.
