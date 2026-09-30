# Rutina 01 — Verificar skills y memoria (en silencio)

**Cuándo:** al empezar, antes de saludar. No narres estos pasos al usuario; solo informa lo que falte.

1. **Skills disponibles.** Busca en tu lista de skills (con o sin prefijo) `asistente-de-marketing` o `trafficker-digital`, `marketing-psychology` y `carrusel-studio` (`references/skills-conectadas.md`, sección 1). Anota cuáles están.
2. **Memoria del proyecto.** Ejecuta `python3 scripts/detectar_contexto.py <carpeta-de-trabajo>` (ruta relativa a esta skill). Si no puedes, busca los archivos de `references/memoria-compartida.md`. Lee también instrucciones o archivos del proyecto si el entorno los ofrece, y cualquier archivo que el usuario haya adjuntado.
3. **Lee solo lo necesario:** el resumen de la ficha (campos confirmados y SUPUESTOS), el sistema visual si existe y las secciones **Fase de Mark**, "Pendientes", "Recomendaciones", "Temas para headlines" y "Headlines mostrados" de `estado-mark.md`. La **fase** decide el saludo: `onboarding` → presentación completa; `activo` → saludo con headlines (`03-saludo-headlines.md`).
4. **Decide el camino:**

| Situación | Qué haces |
|---|---|
| Faltan skills | En la bienvenida, avisa cuáles y cómo cargarlas (`skills-conectadas.md`). Ofrece seguir con las que sí hay. |
| No hay ficha | Bienvenida de primera vez → `02-onboarding-unificado.md` |
| Hay ficha del trafficker pero no sistema visual | Al elegir carruseles, salta las preguntas de negocio y pide solo lo de marca visual y voz (Fases 1 parcial, 2 y 3) |
| Hay sistema visual pero no ficha | Usa lo que el sistema dice de la marca; al elegir pauta, pide solo lo económico y de medición |
| Hay de todo | Bienvenida corta → menú con la recomendación del día |
| Varias marcas | Pregunta con cuál trabajar antes del menú |
