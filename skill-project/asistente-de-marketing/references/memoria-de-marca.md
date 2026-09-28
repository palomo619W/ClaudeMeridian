# Memoria de la marca: ficha y historial

Claude no recuerda nada entre conversaciones. Todo lo que el usuario enseña sobre su marca debe quedar en **dos archivos** que se reutilizan en cada sesión:

| Archivo | Plantilla | Contenido |
|---|---|---|
| `perfil-marca.md` | `assets/plantillas/perfil-marca.md` | La ficha: respuestas del cuestionario, supuestos y confirmaciones |
| `historial-campanas.csv` | `assets/plantillas/historial-campanas.csv` | Resultados y aprendizajes de cada campaña o test |

## Dónde guardarlos
- **Si puedes escribir archivos** (Claude Code, escritorio o una sesión con carpeta de trabajo): créalos en `marketing/<marca-en-kebab-case>/` dentro de la carpeta de trabajo del usuario, **no** dentro de la carpeta de la skill (puede ser de solo lectura y se sobrescribe al actualizarla). Varias marcas = varias carpetas.
- **Si no puedes escribir archivos** (chat): al terminar el onboarding y cada vez que la ficha cambie, entrega la ficha completa en un bloque de código Markdown y pide al usuario que la guarde y la **adjunte o pegue al comenzar la próxima conversación**. Haz lo mismo con las filas nuevas del historial.

## Al iniciar cada conversación
1. Busca `marketing/*/perfil-marca.md` en la carpeta de trabajo, o una ficha adjunta o pegada en el chat.
2. Si existe, léela y **no vuelvas a preguntar** lo que ya está confirmado. Saluda con el nombre de la marca.
3. Si hay varias marcas, pregunta con cuál se trabaja.
4. Si no existe, ejecuta `rutinas/00-onboarding.md`.
5. Para saber qué falta, ejecuta `python3 scripts/verificar_perfil.py <ruta>/perfil-marca.md`.

## Cómo retroalimentar la ficha
- Cualquier dato nuevo que el usuario mencione (un precio, un competidor, una objeción, un resultado) se incorpora a la ficha **sin esperar a que lo pida**. Avísale en una línea: "Actualicé tu ficha: margen = 35 %".
- Un SUPUESTO que el usuario corrige pasa a **confirmado** y se registra con la fecha en "Registro de cambios".
- Cuando los resultados reales contradicen un supuesto (por ejemplo, la tasa de cierre), actualiza la ficha con el dato real y avisa.
