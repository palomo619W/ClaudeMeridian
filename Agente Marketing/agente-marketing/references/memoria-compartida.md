# Memoria compartida del proyecto

Claude no recuerda entre conversaciones. Mark usa los archivos que ya generan las skills especialistas y agrega uno propio. Así, si el proyecto ya usó alguna de las skills, Mark aprovecha lo guardado.

## 1. Archivos (todos dentro de la carpeta de trabajo del usuario, nunca en la carpeta de la skill)

| Archivo | Lo crea | Contenido | Formato |
|---|---|---|---|
| `marketing/<marca>/perfil-marca.docx` | Trafficker (Mark lo alimenta) | Ficha de marca: negocio, cliente, economía, oferta, medición, registro de cambios | .docx (plantilla y scripts del trafficker) |
| `marketing/<marca>/historial-campanas.xlsx` | Trafficker | Resultados y aprendizajes por campaña | .xlsx |
| `marketing/<marca>/sistema-visual.md` | Mark, con la salida de Carrusel Studio | Kit tipográfico, paleta, voz, arquetipo, lista negra | .md (texto corto para `@reusar`) |
| `.agents/product-marketing.md` | Mark (lo lee la skill de psicología) | Contexto de producto: promesa, trabajo a realizar, creencias y objeciones del cliente, disparadores que funcionaron | .md (`assets/plantillas/product-marketing.md`) |
| `marketing/<marca>/estado-mark.md` | Mark | Última sesión, tareas en curso, recomendaciones (propuestas / aceptadas / rechazadas), recordatorio diario | .md (`assets/plantillas/estado-mark.md`) |
| `marketing/<marca>/entregables/` | Todas | Planes, reportes, carruseles (HTML/PNG), estrategias | .docx, .xlsx, .html, .png |

`<marca>` en kebab-case (p. ej. `solar-andes`). Varias marcas = varias carpetas.

## 2. Al empezar cada conversación

1. Ejecuta `python3 <carpeta-de-esta-skill>/scripts/detectar_contexto.py [carpeta-de-trabajo]`. Devuelve en JSON qué marcas y archivos hay.
2. Si no puedes ejecutar scripts, busca a mano los mismos archivos (`marketing/*/perfil-marca.docx` o `.md`, `marketing/*/sistema-visual.md`, `.agents/product-marketing.md`, `.claude/product-marketing.md`, `marketing/*/estado-mark.md`). Revisa también si el usuario adjuntó o pegó una ficha o un bloque "SISTEMA VISUAL DE …".
3. Si hay **memoria del proyecto** del entorno (instrucciones del proyecto, archivos del proyecto de claude.ai, `CLAUDE.md`, memoria de Cowork), léela también: puede contener la ficha o decisiones anteriores.
4. **Varias marcas** → pregunta con cuál trabajar (ventana de opciones con los nombres).
5. **Una marca** → salúdala por su nombre y di en una línea qué recuerdas: *"Tengo tu ficha de Solar Andes, tu sistema visual (kit Modern Clean) y 2 recomendaciones pendientes."*
6. **Ninguna** → marca nueva: `rutinas/02-onboarding-unificado.md`.

## 3. Al guardar

- Guarda **en cuanto aparece un dato nuevo**, sin esperar a que lo pidan, y avisa en una línea: *"Guardé en tu ficha: margen = 35 %."*
- La ficha `.docx` se actualiza con los scripts y la plantilla del trafficker (`references/formato-entrega.md` de esa skill). No crees una ficha paralela en otro formato.
- El sistema visual se guarda **tal como lo entrega Carrusel Studio** en la Fase 9, más la fecha.
- `estado-mark.md` se actualiza al final de cada sesión: qué se hizo, qué quedó pendiente y el próximo paso sugerido.

## 4. Si no puedes escribir archivos (chat sin carpeta de trabajo)

Al final de la sesión entrega los archivos actualizados (ficha `.docx`, sistema visual y estado de Mark) y pide: *"Guárdalos y adjúntalos al empezar la próxima conversación, o súbelos a los archivos de tu proyecto para que siempre los tenga."* Si el entorno no permite archivos, entrega el resumen en el chat como último recurso.
