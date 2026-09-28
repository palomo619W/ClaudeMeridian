# Rutina 13 — Estrategia compuesta (las tres skills en cadena)

**Cuándo:** el usuario pide un resultado que mezcla análisis, pauta y contenido. Es el caso de uso principal de Mark.

**Ejemplo real de petición:**
> "Mark, con la información de la marca arma una estrategia. Escuché que los cortes de energía en Ecuador están cada vez más cerca. Con psicología analiza el mercado para una publicidad asertiva que traiga leads; combínalo con el trafficker y dime qué contenido promocionar. Quiero crecer orgánico con un pequeño empujón de Meta Ads desde el inicio. Al final, con el material elegido, crea con la herramienta de carruseles los carruseles necesarios para publicar."

## 0. Entender y planear (antes de producir)

1. **Descompón la petición** en: disparador (evento/temporada), objetivo (leads), mezcla (orgánico + empujón pagado), plataformas (Meta), entregables (estrategia + qué pautar + carruseles).
2. **Revisa la memoria** y lista lo que falta con `mapa-de-datos.md`. Lo típico que falta: presupuesto del empujón, horizonte, canal de leads. Pregúntalo en **una** ventana con el submenú 3.4 de `menus.md`, omitiendo lo que la petición ya dice (en el ejemplo, "Mezcla" y "Disparador" ya están respondidos).
3. **Muestra el plan de trabajo** en 4 líneas (Contexto → Psicología → Pauta → Carruseles) con lo que entregarás, y pide **Confirmar** (Adelante (Recomendado) · Cambiar algo). No preguntes más durante la cadena salvo en las validaciones creativas de Carrusel Studio.

## 1. Contexto de mercado (verificado)

- Busca en la web el evento: estado actual, fechas, zonas afectadas, fuentes oficiales o medios confiables. Cita fuente y fecha de cada dato.
- Si no puedes verificarlo, dilo y trabaja con escenarios ("si los cortes se confirman…"). **Nunca** inventes cifras ni exageres para generar miedo.
- Resume: qué cambia en la vida del cliente ideal de la ficha, qué necesidad nueva o más urgente aparece y cómo se relaciona con lo que vende la marca. Si la relación es débil, **dilo** y recomienda un ángulo más honesto.

## 2. Psicología → insight y ángulos (`marketing-psychology`)

Pásale el contexto + la ficha. Pide:
- **Creencias y miedos** del cliente frente al evento (lo que cree antes de ver la publicidad).
- **Modelos que aplican** y por qué (p. ej. aversión a la pérdida y sesgo del presente ante un riesgo cercano; prueba social; autoridad; anclaje y contabilidad mental para el precio; Ley de Hick para simplificar la oferta).
- **3–5 ángulos de mensaje** con: disparador, promesa, hook, prueba que lo respalda, CTA y etapa del embudo (conocimiento / consideración / decisión).
- **Límites éticos:** qué urgencia es real y cuál sería manipulación.

## 3. Trafficker → qué pautar y cómo (`asistente-de-marketing`)

Pásale los ángulos. Pide (rutina `01-nueva-campana.md`, adaptada a "empujón"):
- **Qué contenido promocionar:** ranking de los ángulos por potencial de leads, con la hipótesis de cada uno.
- **Estructura de Meta Ads** para presupuesto pequeño: pocas campañas y bien financiadas (normalmente 1 de prospección con 2–3 creativos + remarketing a quienes interactuaron con el contenido orgánico), objetivo según canal (mensajes de WhatsApp o formulario), audiencias, ubicaciones.
- **Presupuesto** repartido en Prospección / Remarketing / Experimentación, en la moneda de la ficha.
- **KPIs y techos** (CPL/CPA máximo) y cuándo apagar o escalar.
- **Preguntas de calificación** del lead si el modelo lo requiere.

## 4. Unir orgánico y pagado

Tabla de **calendario** (2 semanas o el horizonte elegido): día · pieza · formato · ángulo · orgánico o pautado · objetivo · CTA. Regla: primero se publica en orgánico, se mide 48–72 h, y la pieza con mejor señal (guardados, compartidos, mensajes) recibe el empujón pagado. Marca qué carruseles se crean en el paso 5.

## 5. Carruseles (`carrusel-studio`)

- Produce los carruseles marcados en el calendario (normalmente 2–4: uno por ángulo principal + uno de prueba social o preguntas frecuentes). Sigue `10-carruseles.md`: reutiliza el sistema visual; la Big Idea parte del ángulo psicológico; el CTA lleva al canal de leads.
- Si el usuario tiene poco tiempo, ofrece `@express` desde el segundo carrusel.
- Adapta al menos uno como **creativo de anuncio** (versión 4:5, CTA directo) para la campaña del paso 3.

## 6. Entrega final

1. **Resumen en el chat** (5–8 líneas): el insight central, qué se pauta, cuánto, y qué se publica primero.
2. **Documento** `marketing/<marca>/entregables/<fecha>_estrategia_<tema>.docx` con `assets/plantillas/estrategia-compuesta.md` (y `.xlsx` con las tablas de presupuesto, calendario y KPIs), usando los scripts del trafficker.
3. **Carruseles** (HTML + PNG + caption) en `marketing/<marca>/entregables/carruseles/`.
4. **Recomendaciones** (máx. 3, "Te recomiendo… porque…") y ventana **Decisión**.
5. **Seguimiento:** registra en `estado-mark.md` las fechas de publicación y de revisión de resultados; ofrece el recordatorio diario si no existe.

## Otros ejemplos compuestos que usan esta misma rutina
- "Se viene el Día de la Madre: qué promocionar, cuánto invertir y 3 carruseles."
- "Mis anuncios traen leads caros: analiza por qué desde la psicología, corrige la campaña y rehaz los creativos como carruseles."
- "Voy a lanzar un servicio nuevo: estrategia de lanzamiento de 1 mes, orgánico + Meta."
