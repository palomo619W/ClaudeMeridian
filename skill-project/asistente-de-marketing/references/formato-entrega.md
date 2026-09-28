# Formato de entrega: archivos .docx y .xlsx

Todo entregable que la skill genere como archivo se entrega en **Word (.docx)** o **Excel (.xlsx)**, nunca en .md. Así el usuario lo abre, edita, imprime o comparte sin herramientas técnicas.

## Qué va en cada formato
| Entregable | Formato | Nombre sugerido |
|---|---|---|
| Plan de campaña ("Quiero pautar") | **.docx** + **.xlsx** con sus tablas (estructura, presupuesto, KPIs, tests, decisión) | `AAAA-MM-DD_plan-campana_<producto>.docx` / `.xlsx` |
| Reporte de optimización o análisis de resultados | **.docx** + **.xlsx** con los KPIs por anuncio | `AAAA-MM-DD_reporte-optimizacion.docx` / `.xlsx` |
| Reporte semanal o mensual | **.docx** + **.xlsx** con el embudo y el ranking | `AAAA-MM-DD_reporte-<periodo>.docx` / `.xlsx` |
| Creativos, hooks, guiones y copies | **.docx** | `AAAA-MM-DD_creativos_<producto>.docx` |
| Distribución de presupuesto | **.xlsx** (y la explicación en el chat) | `AAAA-MM-DD_presupuesto.xlsx` |
| Ficha de marca | **.docx** | `perfil-marca.docx` (en `marketing/<marca>/`) |
| Historial de campañas (aprendizaje) | **.xlsx** | `historial-campanas.xlsx` (en `marketing/<marca>/`) |

Si el usuario pide expresamente otro formato (PDF, PowerPoint, Google Docs, texto en el chat), respeta su pedido.

## Cómo generarlos (sin librerías externas)
1. Redacta el contenido en Markdown en un archivo temporal (carpeta temporal o de trabajo, no en la carpeta de la skill), con la plantilla de `assets/plantillas/` que corresponda.
2. Conviértelo:
   - Documento: `python3 scripts/exportar_docx.py borrador.md <salida>.docx [--titulo "…"]`
   - Tablas del mismo borrador: `python3 scripts/exportar_xlsx.py <salida>.xlsx borrador.md`. Crea una hoja por tabla, con el nombre de la sección.
   - Datos (CSV o XLSX): `python3 scripts/exportar_xlsx.py <salida>.xlsx resultados.csv [historial.csv …]`. Crea una hoja por archivo.
3. Guarda cada archivo final **una sola vez**:
   - **Carpeta de la marca** (si puedes escribir en la carpeta de trabajo del usuario): `marketing/<marca>/perfil-marca.docx`, `marketing/<marca>/historial-campanas.xlsx` y los demás entregables en `marketing/<marca>/entregables/`.
   - **Carpeta de descargas del entorno** (por ejemplo `/mnt/user-data/outputs/`), solo si existe y es **distinta** de la carpeta de trabajo: copia ahí los archivos que entregas en esta respuesta y preséntalos con la herramienta de archivos disponible. Si ambas son la misma carpeta, no dupliques.
4. Borra los borradores .md temporales. La ficha y el historial también se guardan solo en .docx y .xlsx: no mantengas copias .md o .csv, porque los scripts leen esos formatos directamente.

## Cómo actualizar la ficha y el historial
- **Ficha (.docx):** lee su texto con `scripts/verificar_perfil.py` o con `read_docx_text` de `scripts/ooxml.py`. Rehaz el borrador con la plantilla `assets/plantillas/perfil-marca.md` y los valores actuales más los nuevos (conserva el formato `- **Campo** [N1]: valor` y el registro de cambios) y vuelve a exportarlo con `exportar_docx.py`, sobrescribiendo `perfil-marca.docx`.
- **Historial (.xlsx):** `scripts/registrar_aprendizaje.py --historial marketing/<marca>/historial-campanas.xlsx --agregar filas.csv|.xlsx` lo actualiza en su mismo formato.
- **KPIs:** `scripts/calcular_kpis.py … --xlsx <salida>.xlsx` guarda la tabla de KPIs por anuncio directamente en Excel, lista para entregar o combinar con `exportar_xlsx.py`.

## Qué se escribe en el chat
- Un resumen de 3 a 6 líneas con la decisión principal y los archivos entregados.
- Las preguntas que la skill necesita hacer (onboarding o datos faltantes) van **en el chat**, no en un archivo. Una pregunta no es un entregable.

## Lectura de archivos del usuario
Los scripts leen tanto los formatos de entrega como los de trabajo:
- `verificar_perfil.py` acepta la ficha en `.docx` o `.md`.
- `calcular_kpis.py` acepta resultados en `.xlsx` (exportación directa del Administrador de anuncios) o `.csv`.
- `registrar_aprendizaje.py` acepta el historial y las filas nuevas en `.xlsx` o `.csv`. Si el historial es `.xlsx`, lo actualiza en ese mismo formato.
