# Guía para comparar respuestas CON y SIN la skill

**Skill:** Asistente de Marketing · **Iteración:** 1 · **Fecha:** 28-09-2026

Esta guía te ayuda a revisar los 3 casos de prueba y a decidir qué mejorar en la skill. No necesitas conocimientos técnicos.

## 1. Archivos de esta carpeta

| Archivo | Para qué sirve |
|---|---|
| `respuestas-con-skill.md` | Las 3 respuestas generadas **usando** la skill |
| `respuestas-sin-skill.md` | Las mismas 3 preguntas respondidas **sin** la skill (línea base) |
| `visor-evaluacion.html` | Visor interactivo. Ábrelo en el navegador: en la pestaña **Outputs** ves cada caso lado a lado y puedes escribir comentarios; en **Benchmark** están los números. Al terminar pulsa **Submit All Reviews** y descarga `feedback.json` |
| `guia-comparacion.md` | Este documento |

Los archivos que creó la skill en cada caso (fichas de marca e historiales) están en `asistente-de-marketing-workspace/iteration-1/<caso>/with_skill/run-1/outputs/marketing/`.

## 2. Cómo hacer la revisión (15-20 minutos)

1. **Lee primero la respuesta SIN skill** de un caso. Imagina que eres el dueño de ese negocio: ¿te sirve? ¿qué harías después de leerla?
2. **Lee la respuesta CON skill** del mismo caso y hazte las mismas preguntas.
3. **Califica con la tabla de la sección 4** (1 a 5).
4. **Anota lo que cambiarías**, aunque la respuesta con skill haya ganado. Esos comentarios son los que mejoran la skill.
5. Repite con los otros 2 casos.

> Consejo: pregúntate más "¿qué haría con esto un dueño de negocio real?" que "¿cuál es más larga?". Una respuesta más larga no siempre es mejor.

## 3. Los 3 casos y qué mirar en cada uno

### Caso 1 — Tienda de ropa deportiva en México (primer contacto)
**Mensaje:** *"hola, tengo una tienda online de ropa deportiva para mujer en México y quiero empezar a hacer anuncios en Instagram, ¿me ayudas?"*
**Qué pone a prueba:** si la skill pide la información "de forma atinada" cuando no conoce la marca.

| Mira esto | Con skill | Sin skill |
|---|---|---|
| ¿Repite preguntas de datos que el usuario ya dio? | No: los confirma en una línea | No |
| Número de preguntas | 7, con opciones y ejemplos | 8, al final de un plan largo |
| ¿Acepta "no sé"? | Sí, con valores por defecto | No lo menciona |
| ¿Guarda lo aprendido? | Crea la ficha de marca (29 % completa) | No |
| ¿Da valor inmediato? | Un adelanto breve (5 viñetas) | Un plan completo en 7 bloques |

**Para pensar:** la respuesta sin skill entrega **más contenido** de inmediato: configuración técnica, métodos de pago en México y un plan de 4 semanas. La de la skill es más corta y se centra en recoger datos. ¿Qué prefieres como primer mensaje: más contenido o un mejor proceso?

### Caso 2 — Ortodoncia invisible en Lima ("Quiero pautar")
**Mensaje:** *"Quiero pautar mi servicio de ortodoncia invisible en Lima. Cobro 2500 dólares el tratamiento, tengo 800 dólares al mes para anuncios y atiendo por WhatsApp de 9 a 7."*
**Qué pone a prueba:** el formato obligatorio de campaña y la adaptación a un **servicio de salud** local.

| Mira esto | Con skill | Sin skill |
|---|---|---|
| Formato de 20 secciones + DECISIÓN DEL TRAFFICKER | Sí, completo | No (9 secciones propias) |
| Reparto del presupuesto | Prospección 520 / Remarketing 120 / Experimentación 160 | Por canal: Meta 560 / Google 240 |
| Techos económicos | Costo máximo por paciente, por evaluación y por conversación | Solo "hasta US$500 por paciente" |
| Creativos | 3 conceptos con hook de 0-3 s, guion y formato 9:16 | Ideas de formatos y 2 textos |
| Preguntas de calificación | 5, con puntaje | No |
| Reglas de salud en Meta | Sí | Sí |
| Horario de WhatsApp | Mensaje de ausencia | Programar anuncios o respuesta automática |

**Para pensar:** la respuesta con skill es unas **3 veces más larga** (~26 000 caracteres). ¿Un dueño de clínica la leería completa? Quizá convenga un resumen ejecutivo al inicio o una versión corta del plan. La versión sin skill tiene buenas ideas que la skill no incluyó, como "vender la evaluación, no el tratamiento" y el guion de WhatsApp para no dar el precio en frío.

### Caso 3 — Software de facturación para pymes (análisis de resultados)
**Mensaje:** *"Te paso los resultados de la semana pasada. Vendemos software de facturación a pymes y mi CPL calificado objetivo es 40 USD. ¿Qué apago y qué escalo?"*
**Qué pone a prueba:** decisiones basadas en datos y aprendizaje continuo.

| Mira esto | Con skill | Sin skill |
|---|---|---|
| Decisión correcta (escalar A, apagar B) | Sí | Sí |
| Cálculos (CPL calificado 10,94 y 50,60) | Sí (con el script de la skill) | Sí |
| Detecta que se cambiaron varias variables a la vez | Sí | Sí |
| Cuánto dinero mover | +3 USD/día al ganador y 12 USD/día al test, con fecha de revisión | +20-30 % cada 3-4 días |
| Registro del aprendizaje | Sí: historial (GANADOR / PERDEDOR) y ficha creada | No |

**Para pensar:** aquí las dos versiones llegan a la **misma conclusión**. La skill aporta orden, fechas concretas y memoria (historial). ¿Te basta esa diferencia o esperabas más?

## 4. Tabla de calificación (llénala tú)

Califica de 1 (malo) a 5 (excelente).

| Criterio | Caso 1 con | Caso 1 sin | Caso 2 con | Caso 2 sin | Caso 3 con | Caso 3 sin |
|---|---|---|---|---|---|---|
| Utilidad real para el dueño del negocio | | | | | | |
| Claridad y facilidad de lectura | | | | | | |
| Decisiones concretas (números, fechas) | | | | | | |
| Adaptación al tipo de negocio | | | | | | |
| Forma de pedir información | | | | | | |
| Largo adecuado (ni poco ni demasiado) | | | | | | |
| **Total** | | | | | | |

## 5. Resultados de la evaluación automática

Cada respuesta se revisó con una lista de criterios verificables (7 a 9 por caso).

| Caso | Con skill | Sin skill |
|---|---|---|
| 1. Tienda de ropa (primer contacto) | **7/7 (100 %)** | 4/7 (57 %) |
| 2. Ortodoncia ("Quiero pautar") | **9/9 (100 %)** | 4/9 (44 %) |
| 3. Software pymes (resultados) | **8/8 (100 %)** | 7/8 (88 %) |
| **Promedio** | **100 %** | **63 %** |
| Tiempo promedio por respuesta | ~170 s | ~64 s |
| Consumo promedio (tokens) | ~80 000 | ~47 000 |

**Cómo leer estos números:**
- Los criterios revisan sobre todo que **se cumpla lo que pediste en la especificación**: formato de 20 secciones, reparto en 3 bolsas, ficha de marca, supuestos, historial. Por eso la skill gana con claridad. Pero no miden si la estrategia es **mejor**; eso lo decides tú en la sección 4.
- En el caso 3 la diferencia es pequeña: sin skill el modelo ya sabe analizar resultados. La skill suma el registro del aprendizaje y más precisión.
- La skill tarda y consume más porque lee sus guías y ejecuta scripts. Es el costo de respuestas más completas y consistentes.

## 6. Problemas ya detectados (se corregirán en la siguiente iteración)

1. **La columna "presupuesto" del CSV es ambigua:** no dice si es diaria, semanal o total. Se aclarará el nombre de la columna.
2. **El verificador de la ficha se confunde** cuando un campo tiene la palabra "PENDIENTE" en una nota al margen: marca como pendiente un dato que sí está completo. Se ajustará.
3. **El script de presupuesto** cambia al reparto de "presupuesto bajo" (80/20/0) cuando se le pasa un CPL objetivo alto, aunque la campaña optimice hacia un evento más barato. Se revisará la regla.
4. **Respuestas de campaña muy largas** (caso 2): falta evaluar si conviene un resumen ejecutivo al inicio.

## 7. Preguntas para tu retroalimentación

Responde las que quieras. Con eso preparo la iteración 2:

1. En el **caso 1**, ¿prefieres que el primer mensaje sea corto y con preguntas (con skill) o más completo, con un plan general desde el inicio (sin skill)? ¿O una mezcla?
2. En el **caso 2**, ¿el plan de 20 secciones tiene el largo correcto o debería tener un **resumen ejecutivo de una página** al inicio?
3. ¿Hay ideas de las respuestas **sin skill** que quieras incorporar a la skill (por ejemplo, "vender la evaluación, no el tratamiento", o los métodos de pago locales)?
4. ¿El tono es el adecuado para tus usuarios (dueños de negocio sin formación técnica)?
5. ¿Quieres agregar otros casos de prueba (otro país, otro tipo de negocio, un presupuesto muy bajo)?

Puedes contestar directamente en el chat o escribir tus comentarios en el visor y enviarme el `feedback.json`.
