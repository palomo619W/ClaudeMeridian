# Memoria de la marca: ficha y historial

Claude no recuerda nada entre conversaciones. Todo lo que el usuario enseña sobre su marca debe quedar en **dos archivos** que se reutilizan en cada sesión:

| Archivo | Plantilla | Contenido |
|---|---|---|
| `perfil-marca.docx` | `assets/plantillas/perfil-marca.md` (se exporta con `exportar_docx.py`) | La ficha: respuestas del cuestionario, supuestos y confirmaciones |
| `historial-campanas.xlsx` | `assets/plantillas/historial-campanas.csv` (lo crea `registrar_aprendizaje.py`) | Resultados y aprendizajes de cada campaña o test |

Ambos se guardan solo en .docx y .xlsx. Cómo actualizarlos: `formato-entrega.md`. Si el usuario trae una ficha o un historial antiguos en .md o .csv, léelos igual (los scripts aceptan ambos formatos) y conviértelos a .docx y .xlsx.

## Dónde guardarlos
- **Si puedes escribir archivos** (Claude Code, escritorio o una sesión con carpeta de trabajo): guárdalos en `marketing/<marca-en-kebab-case>/perfil-marca.docx` y `…/historial-campanas.xlsx` dentro de la carpeta de trabajo del usuario, **no** dentro de la carpeta de la skill (puede ser de solo lectura y se sobrescribe al actualizarla). Varias marcas = varias carpetas.
- **Si no puedes escribir en una carpeta de trabajo permanente** (chat): al terminar el onboarding y cada vez que la ficha cambie, entrega `perfil-marca.docx` (generado con `scripts/exportar_docx.py`) y pide al usuario que lo guarde y lo **adjunte al comenzar la próxima conversación**. Haz lo mismo con `historial-campanas.xlsx`. Si el entorno no permite generar archivos, entrega la ficha en el chat como último recurso.

## Al iniciar cada conversación
1. Busca `marketing/*/perfil-marca.docx` (o un `.md` antiguo) en la carpeta de trabajo, o una ficha adjunta (`.docx`) o pegada en el chat. Si llega en .docx, puedes leerla con `scripts/verificar_perfil.py` o extraer su texto con `read_docx_text` de `scripts/ooxml.py`.
2. Si existe, léela y **no vuelvas a preguntar** lo que ya está confirmado. Saluda con el nombre de la marca.
3. Si hay varias marcas, pregunta con cuál se trabaja.
4. Si no existe, ejecuta `rutinas/00-onboarding.md`.
5. Para saber qué falta, ejecuta `python3 scripts/verificar_perfil.py <ruta>/perfil-marca.docx`.

## Cómo retroalimentar la ficha
- Cualquier dato nuevo que el usuario mencione (un precio, un competidor, una objeción, un resultado) se incorpora a la ficha **sin esperar a que lo pida**. Avísale en una línea: "Actualicé tu ficha: margen = 35 %".
- Un SUPUESTO que el usuario corrige pasa a **confirmado** y se registra con la fecha en "Registro de cambios".
- Cuando los resultados reales contradicen un supuesto (por ejemplo, la tasa de cierre), actualiza la ficha con el dato real y avisa.
