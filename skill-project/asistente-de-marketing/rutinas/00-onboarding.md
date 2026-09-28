# Rutina 00 — Onboarding: conocer la marca y crear su ficha

**Cuándo:** no existe la ficha de la marca, el usuario quiere configurar o actualizar su marca, o empieza con una marca nueva.
**Resultado:** ficha `perfil-marca.md` con al menos el Nivel 1 completo, y una primera recomendación de valor.

## Pasos
1. **Busca una ficha existente** (`references/memoria-de-marca.md`). Si la hay, salta al paso 6.
2. **Extrae lo que ya existe.** Si el usuario compartió una web, redes, un brief, un PDF, un catálogo o texto sobre la marca, léelo y rellena todo lo posible. Si hay herramientas de lectura web disponibles y el usuario dio la URL, úsalas.
3. **Pregunta el Nivel 1** (`references/cuestionario-marca.md`) en un solo mensaje, numerado y con opciones. Omite lo que ya dedujiste y, en su lugar, pide confirmarlo en una línea ("Entiendo que vendes X en Y, ¿correcto?").
4. **Procesa las respuestas:**
   - Rellena la plantilla `assets/plantillas/perfil-marca.md`.
   - "No sé" → valor por defecto + (SUPUESTO).
   - Calcula los techos económicos si hay ticket y margen (sección 7).
5. **Guarda la ficha** según `memoria-de-marca.md`: archivo en `marketing/<marca>/perfil-marca.md` si puedes escribir; si no, bloque de código para que el usuario lo guarde.
6. **Aporta valor de inmediato:** propone en 3–5 viñetas por dónde empezaría (producto a priorizar, canal, presupuesto mínimo sugerido) y pregunta si armas la primera campaña.
7. **Niveles 2 y 3:** no los pidas todos de golpe. Pide cada pregunta cuando una rutina la necesite (ver la columna "Se necesita para"). Si el usuario elige el modo completo, pídelos en dos mensajes más.

## Actualizar una ficha existente
- Ejecuta `python3 scripts/verificar_perfil.py <ruta>/perfil-marca.md` para ver los pendientes por nivel.
- Pregunta solo los 3–5 pendientes de mayor impacto para la tarea actual.
- Registra cada cambio con la fecha en "Registro de cambios".

## Tono
Cercano y breve. El usuario puede no saber qué es un CPL o un píxel: usa lenguaje simple y explica los términos técnicos en pocas palabras la primera vez.
