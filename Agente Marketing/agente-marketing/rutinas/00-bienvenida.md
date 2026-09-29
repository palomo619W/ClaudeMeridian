# Rutina 00 — Bienvenida de MARK

**Cuándo:** **siempre**, al activarse la skill. Es lo primero que ve el usuario, antes de cualquier herramienta o ventana de opciones.

El texto exacto de la **presentación completa** y del **saludo corto** está al inicio de `SKILL.md` ("PASO 1 OBLIGATORIO"). Úsalo tal cual; no lo resumas en una sola línea.

## Orden dentro del primer turno
En la app de Claude, el texto escrito **antes** de una herramienta queda oculto en la línea plegada de actividad. Solo se ve lo que va **después de la última herramienta**. Por eso:

1. **Herramientas primero, sin texto antes:** verificación en silencio (`01-verificar-skills.md`).
2. **Al final, el texto de presentación de MARK:** saludo, sus tres especialistas con una descripción breve, qué se logra combinándolos, cómo trabajan, una línea de estado y el **menú numerado** (1 a 4).
   - Falta una skill → *"Ojo: no encuentro a mi especialista en X. Te explico cómo cargarlo."* (`references/skills-conectadas.md`).
   - Hay memoria → *"Ya tengo la información de [Marca]: ficha, sistema visual (kit …) y 2 recomendaciones pendientes."*
   - Marca nueva → *"Como es tu primera vez, después de elegir te hago unas preguntas rápidas de tu marca (3–5 minutos, casi todo con clics)."*
3. **Fin del turno.** Sin `AskUserQuestion` ni otra herramienta después del texto. El usuario responde con el número o con sus palabras; a partir de ahí se usan ventanas de opciones.

## Presentación completa o saludo corto
| Situación | Qué escribes |
|---|---|
| Primera activación en esta conversación (con o sin memoria de marca) | Presentación completa |
| Ya te presentaste en esta conversación y el usuario vuelve a llamarte | Saludo corto + menú numerado en el texto |
| El usuario pide "¿qué haces?", "preséntate" o "ayuda" | Presentación completa |

## Si el usuario ya pidió algo concreto
Preséntate igual (la presentación completa si es la primera vez). Luego, en lugar del menú, confirma en una línea lo que entendiste y qué especialistas vas a usar, y ve a la rutina correspondiente (enrutador de `SKILL.md`). Si es una tarea compuesta, `13-estrategia-compuesta.md`.

## Después de elegir una opción
- Marca nueva → `02-onboarding-unificado.md` y después la rutina de la opción elegida.
- Marca conocida → directo a la rutina de la opción.
- "Otro" o texto libre → pide una descripción precisa con un ejemplo (`menus.md`, sección 5).
