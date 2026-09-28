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
| Ficha de marca | **.docx** | `perfil-marca.docx` |
| Historial de campañas (aprendizaje) | **.xlsx** | `historial-campanas.xlsx` |

Si el usuario pide expresamente otro formato (PDF, PowerPoint, Google Docs, texto en el chat), respeta su pedido.

## Cómo generarlos (sin librerías externas)
1. Redacta el contenido en Markdown en un archivo temporal (carpeta temporal o de trabajo, no en la carpeta de la skill), con la plantilla de `assets/plantillas/` que corresponda.
2. Conviértelo:
   - Documento: `python3 scripts/exportar_docx.py borrador.md <salida>.docx [--titulo "…"]`
   - Tablas del mismo borrador: `python3 scripts/exportar_xlsx.py <salida>.xlsx borrador.md`. Crea una hoja por tabla, con el nombre de la sección.
   - Datos (CSV o XLSX): `python3 scripts/exportar_xlsx.py <salida>.xlsx resultados.csv [historial.csv …]`. Crea una hoja por archivo.
3. Guarda los archivos finales:
   - Si puedes escribir en la carpeta de trabajo del usuario: `marketing/<marca>/entregables/`.
   - Si el entorno tiene una carpeta de salida para descargas (por ejemplo `/mnt/user-data/outputs/`), guarda ahí una copia y preséntala con la herramienta de archivos disponible.
4. Borra los borradores .md temporales: el usuario solo recibe .docx y .xlsx.

## Qué se escribe en el chat
- Un resumen de 3 a 6 líneas con la decisión principal y los archivos entregados.
- Las preguntas que la skill necesita hacer (onboarding o datos faltantes) van **en el chat**, no en un archivo. Una pregunta no es un entregable.

## Lectura de archivos del usuario
Los scripts leen tanto los formatos de entrega como los de trabajo:
- `verificar_perfil.py` acepta la ficha en `.docx` o `.md`.
- `calcular_kpis.py` acepta resultados en `.xlsx` (exportación directa del Administrador de anuncios) o `.csv`.
- `registrar_aprendizaje.py` acepta el historial y las filas nuevas en `.xlsx` o `.csv`. Si el historial es `.xlsx`, lo actualiza en ese mismo formato.
