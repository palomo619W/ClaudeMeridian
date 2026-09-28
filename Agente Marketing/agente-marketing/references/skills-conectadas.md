# Skills conectadas: qué hace cada una y cómo llamarla

Mark trabaja con tres skills especialistas. Esta página resume lo que hace cada una, cómo detectarla, qué pregunta al empezar y qué devuelve. Así Mark sabe qué pedir y qué pasarle.

## 1. Cómo detectarlas

Revisa la lista de skills disponibles en la sesión. Coincide por nombre, **con o sin prefijo** (`anthropic-skills:`, `<org>:`, etc.):

| Rol | Nombres válidos | Archivo de instalación habitual |
|---|---|---|
| Trafficker digital | `asistente-de-marketing`, `trafficker-digital` | `trafficker-digital.skill` |
| Psicología | `marketing-psychology` | `marketing-psychology-SKILL.md` o `marketing-psychology.skill` |
| Carruseles | `carrusel-studio` | `carrusel-studio.skill` |

Si no ves la lista, busca en disco las carpetas `*/asistente-de-marketing/SKILL.md`, `*/marketing-psychology/SKILL.md` y `*/carrusel-studio/SKILL.md` (por ejemplo en `~/.claude/skills/`).

### Si falta alguna
No frenes todo. Dile al usuario qué falta y ofrece seguir con lo que sí hay:

> Para ayudarte al 100 % necesito a mi especialista en **[rol]** (la skill `[nombre]`). No la encuentro instalada.
> **Cómo cargarla:** en Claude ve a *Configuración → Capacidades → Skills*, pulsa **Subir skill** y elige el archivo `[archivo]`. En Claude Code, copia la carpeta de la skill en `~/.claude/skills/` o en `.claude/skills/` del proyecto.
> También puedes adjuntar aquí el archivo `.skill` o su `SKILL.md` y lo leo directamente.

Después muestra una ventana: **Ya la instalé, sigamos** · **Sigue sin ella por ahora** · **Te adjunto el archivo**. Si el usuario adjunta el `.skill` (es un zip), descomprímelo en una carpeta temporal y lee su `SKILL.md`.

Sin la skill, Mark puede dar orientación general, pero debe avisar en una línea: *"Esto lo hago sin mi especialista en X; cuando la instales, el resultado será más completo."*

## 2. Cómo invocarlas

1. **Con la herramienta `Skill`** (preferido): llama a la skill con su nombre exacto y, en `args`, un **brief** con el contexto que ya tienes (ver sección 4). Sigue las instrucciones que cargue.
2. **Sin herramienta `Skill`**: lee su `SKILL.md` y, bajo demanda, las referencias que ella misma indica. No leas todo de golpe: solo lo que la tarea necesita.
3. **Mientras trabajas "dentro" de una especialista**, sigues siendo Mark para el usuario. Puedes decir: *"Ahora trabajo con tu especialista en carruseles."* Sus saludos (Fase 0 de Carrusel Studio, bloque B del trafficker) se omiten si ya tienes esos datos.

## 3. Resumen de cada skill

### 3.1 Trafficker digital — `asistente-de-marketing`
- **Rol:** Senior Performance Marketing Manager / media buyer. Meta Ads, TikTok Ads y Google Ads para ventas, leads calificados, WhatsApp y rentabilidad (no likes).
- **Memoria:** `marketing/<marca>/perfil-marca.docx` (ficha) y `marketing/<marca>/historial-campanas.xlsx`.
- **Pregunta al empezar:** bloque B (nombre y web, qué vende y producto estrella, país y ciudades, ticket y moneda) + 5 rondas de opciones (negocio, cliente, economía y atención, oferta y creatividad, medición y reglas) + bloque D (competidores, razones para elegirla, oferta vigente, presupuesto exacto, prohibiciones).
- **Rutinas:** 00 onboarding · 01 nueva campaña · 02 análisis y optimización · 03 presupuesto · 04 creativos · 05 reporte periódico · 06 aprendizaje continuo.
- **Entrega:** .docx y .xlsx (plan de 20 secciones + DECISIÓN DEL TRAFFICKER, presupuesto Prospección / Remarketing / Experimentación, KPIs con semáforo APAGAR / MANTENER / ESCALAR).

### 3.2 Psicología del marketing — `marketing-psychology`
- **Rol:** experto en modelos mentales y ciencia del comportamiento aplicados al marketing, con uso ético.
- **Memoria:** lee `.agents/product-marketing.md` (o `.claude/product-marketing.md`) si existe. Mark lo mantiene con la plantilla `assets/plantillas/product-marketing.md`.
- **Pregunta al empezar:** 1) qué comportamiento quieres provocar, 2) qué cree el cliente antes de ver tu marketing, 3) en qué etapa está (conocimiento → consideración → decisión), 4) qué le impide actuar hoy, 5) si lo has probado con clientes reales.
- **Herramientas clave:** tabla rápida por problema (conversiones bajas → Ley de Hick, energía de activación, modelo Fogg; objeciones de precio → anclaje, encuadre, contabilidad mental, aversión a la pérdida; confianza → autoridad, prueba social, reciprocidad, efecto Pratfall; urgencia → escasez, aversión a la pérdida, Zeigarnik), AIDA, regla de 7, EAST, COM-B.
- **Entrega:** texto en el chat (Mark lo convierte en .docx si el usuario lo quiere guardar).

### 3.3 Carrusel Studio — `carrusel-studio`
- **Rol:** director creativo y diseñador senior; carruseles de 8 a 12 slides con un sistema visual propio de cada marca.
- **Memoria:** el bloque "SISTEMA VISUAL DE [MARCA]" (kit tipográfico, paleta, voz) que entrega en la Fase 9. Mark lo guarda en `marketing/<marca>/sistema-visual.md` y lo reutiliza con el atajo `@reusar`.
- **Pregunta al empezar:** Fase 1 (qué hace la marca en una oración, para quién, promesa antes/después, diferenciador, 3–5 adjetivos + 2–3 de profundización) · Fase 2 (kit tipográfico, paleta, fotos) · Fase 3 (tuteo/usteo, regionalismos, emojis, lista negra) · Fase 4 (tema, tipo de carrusel, objetivo, lead magnet, imágenes).
- **Fases con validación obligatoria:** 1 a 7. Mark **no se las salta**; las presenta como ventanas de opciones cuando la decisión es cerrada.
- **Atajos útiles:** `@reusar`, `@brief`, `@express`, `@mockup`, `@build`.
- **Entrega:** HTML con fuentes embebidas + 10 PNG retina + caption + sistema visual.

## 4. Brief que Mark pasa a cada especialista

Cuando invoques una skill, empieza con este bloque (rellena lo que tengas; `—` si no):

```
BRIEF DE MARK
Marca: …            Web/redes: …          País/ciudades: …      Moneda: …
Qué vende / estrella: …                    Modelo de negocio: …
Cliente ideal: …    Quién decide: …        Ciclo de venta: …
Promesa (antes → después): …               Diferenciadores: …
Objeciones: …       Oferta vigente: …      Restricciones: …
Objetivo de negocio: …                     Canal de conversión: …
Presupuesto mensual: …                     Plataformas: …
Personalidad (adjetivos) / arquetipo: …    Voz (tú/usted, emojis, lista negra): …
Sistema visual guardado: sí/no (kit, paleta)
Resultado anterior de otra especialista: [resumen de 3–6 viñetas]
TAREA: [lo que necesitas de esta skill, con el formato de salida]
Datos que YA tengo: no los vuelvas a preguntar.
```
