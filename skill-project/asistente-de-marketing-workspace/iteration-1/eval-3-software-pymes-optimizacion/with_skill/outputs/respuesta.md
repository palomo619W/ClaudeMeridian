# Reporte de optimización — Semana 1 al 7 de septiembre de 2026 · Software de facturación para pymes (Meta Ads)

**Respuesta corta:** **apaga "Hook producto B"** (conjunto Intereses) y **escala "Hook dolor A"** (conjunto Amplia) un +20 %. El dinero que liberas va a un test de una sola variable, así que el gasto total no cambia. El detalle va abajo.

> No encontré una ficha de tu marca, así que te creé una con lo que me contaste (software de facturación para pymes, USD, CPL calificado objetivo = 40 USD). Para no frenarte, trabajé con supuestos marcados. Al final te dejo 3 preguntas para afinar.

## Resumen
Gasto **199,70 USD** · Conversaciones de WhatsApp **59** · Calificados **11** · Oportunidades **3** · Cotizaciones **1** · Ventas **0** · Facturación **0 USD**
Métrica guía: **CPL calificado (CPLc) de 18,15 USD** frente al objetivo de 40 USD (**55 % por debajo del objetivo**). Es la primera semana, así que todavía no hay un periodo anterior con qué comparar.

| Anuncio | Gasto | Conv. | Calif. | % calif. | CPM | CTR | CPC | CPL | **CPLc** | Costo/oport. | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hook dolor A (Amplia · video testimonio) | 98,50 | 38 | 9 | 23,7 % | 3,16 | 1,3 % | 0,24 | 2,59 | **10,94** | 32,83 | **ESCALAR** |
| Hook producto B (Intereses · video producto) | 101,20 | 21 | 2 | 9,5 % | 3,50 | 0,7 % | 0,53 | 4,82 | **50,60** | — (0 oport.) | **APAGAR** |

*(Todo en USD, calculado con `calcular_kpis.py`.)*

## Embudo
| Etapa | Actual | Anterior | Δ % | Línea base orientativa (B2B, Meta LATAM) |
|---|---|---|---|---|
| CPM | 3,32 USD | — | — | 3 – 8 USD ✔ |
| CTR de enlace | 1,0 % | — | — | 0,6 % – 1,5 % ✔ |
| CPC | 0,33 USD | — | — | 0,30 – 1,20 USD ✔ |
| Costo por conversación | 3,38 USD | — | — | 2 – 10 USD ✔ |
| Conversación → calificado | 18,6 % | — | — | 15 % – 35 % ✔ (en la parte baja) |
| Calificado → oportunidad | 27,3 % | — | — | 30 % – 50 % (algo por debajo) |
| Oportunidad → cotización | 33,3 % (1 de 3) | — | — | — |
| Cotización → venta | 0 % (0 de 1) | — | — | Todavía no se puede evaluar |

## 1. Qué funcionó
- **Hook dolor A** (*"¿Sigues perdiendo tiempo con X?"* + video testimonio, audiencia Amplia 25-55): **CPLc de 10,94 USD, un 27 % del objetivo**. Hace falta un CPLc de 32 USD o menos (el 80 % del objetivo) para escalar, y lo supera con holgura.
- Trae casi el doble de conversaciones que B (38 contra 21) con menos gasto, y **2,5 veces más tasa de calificación** (23,7 % contra 9,5 %).
- Es el **único anuncio que generó oportunidades (3) y la única cotización**, a un costo de 32,83 USD por oportunidad.
- Su CTR (1,3 %) es casi el doble que el de B, con un CPC menos de la mitad (0,24 contra 0,53 USD): el mensaje de dolor detiene el scroll.

## 2. Qué empeoró
- **Hook producto B** (*"Conoce nuestro nuevo producto"*, audiencia Intereses): **CPLc de 50,60 USD, un 26 % por encima del objetivo**. Solo 2 calificados de 21 conversaciones (9,5 %) y **ninguna oportunidad**.
- Cumple la regla de apagado: tiene **menos del 10 % de calificación con 20 o más leads**. Además gastó 101 USD (2,5 veces el CPLc objetivo) para conseguir apenas 2 calificados.
- Su CTR del 0,7 % está cerca del umbral de alerta (0,5 %), con un CPM algo más caro (3,50 USD).
- En total, **0 ventas**. Para un SaaS con ciclo de días a semanas, una semana todavía no alcanza para juzgar el cierre. Hay que seguir esta cohorte de leads.

## 3. Por qué posiblemente ocurrió
- **El mensaje de dolor filtra mejor que el de "novedad".** Una pyme no busca "un producto nuevo", busca dejar de perder tiempo (o dinero) facturando. El testimonio además da prueba social, que en software de facturación pesa mucho.
- **"Nuevo producto" atrae curiosos**, no gente con el problema. Eso explica más conversaciones de baja calidad.
- **Ojo, la comparación está contaminada:** entre A y B cambiaron **a la vez** el hook, el creativo (testimonio o producto) y la audiencia (Amplia o Intereses). No podemos afirmar si B perdió por el mensaje, por la audiencia o por ambos. La diferencia de CTR sugiere que pesa sobre todo el mensaje, pero hay que confirmarlo (ver el test del punto 7).
- **El volumen todavía es bajo** (9 y 2 calificados), así que lee los números como rangos. Aun así, aunque A tuviera la mitad de calificados, su CPLc (~22 USD) seguiría muy por debajo de 40.

## 4. Hipótesis a probar
- **H1 (audiencia):** con el mismo hook de dolor + testimonio, la audiencia Amplia da un CPLc igual o mejor que la de Intereses. Si se confirma, conviene concentrar todo en Amplia y dejar que el creativo filtre.
- **H2 (siguiente semana, no ahora):** otras variantes del dolor (por ejemplo, multas o errores con la facturación) pueden igualar o mejorar a A y darnos respaldo cuando llegue la fatiga creativa.

## 5. Decisiones
| Elemento | Acción | Motivo (dato) |
|---|---|---|
| Anuncio **Hook producto B** (conjunto Intereses) | **APAGAR** | CPLc de 50,60 USD (126 % del objetivo), 9,5 % de calificación con 21 leads y 0 oportunidades |
| Anuncio **Hook dolor A** (conjunto Amplia) | **ESCALAR +20 %** | CPLc de 10,94 USD (27 % del objetivo) con 9 calificados, y 3 oportunidades a 32,83 USD cada una |
| Conjunto **Intereses** | **MANTENER solo como test** (con el anuncio A dentro) | No se puede descartar la audiencia mientras siga mezclada con el hook perdedor |
| Campaña **PROSP / Producto A / WhatsApp** | **MANTENER** | Métricas de plataforma dentro de los rangos B2B y CPLc total de 18,15 USD |

## 6. Movimiento de presupuesto
Cada conjunto tenía 105 USD por semana (unos 15 USD al día).

| Desde | Hacia | Monto/día | Motivo |
|---|---|---|---|
| Hook producto B (Intereses) | Hook dolor A (Amplia) | **+3 USD** (de 15 a 18 USD/día, +20 %) | Es el ganador. No subas más del 20-30 % de golpe para no reiniciar el aprendizaje |
| Hook producto B (Intereses) | Test: Hook dolor A dentro de Intereses | **12 USD** | Aislar la variable audiencia (punto 7) |

- **Gasto total: se mantiene en unos 30 USD/día (≈ 210 USD por semana).**
- **Siguiente escalón:** si dentro de 72 h (el **1 de octubre**) el CPLc de A sigue en 32 USD o menos, súbelo otro +20 % (a unos 21,6 USD/día). Repite cada 48-72 h mientras se sostenga.
- **Freno:** si el CPLc de A pasa de 40 USD durante 3 días seguidos, o si la frecuencia supera 4 con el costo subiendo más del 30 %, vuelve al presupuesto anterior y rota el creativo.
- **No toques el anuncio A** (ni el texto, ni el video, ni la audiencia) mientras escala. Solo cambia el presupuesto.

## 7. Nuevo test
- **Variable:** audiencia (solo una).
- **Variante A vs. B:** "Hook dolor A" (el mismo video testimonio y el mismo copy) en **Amplia 25-55** contra el mismo anuncio en **Intereses afines**.
- **Presupuesto:** 12 USD/día en el conjunto Intereses (unos 84 USD en total, cerca de 2 veces el CPLc objetivo). Amplia sigue con su presupuesto de escalado.
- **Duración:** 7 días, del 29 de septiembre al 5 de octubre de 2026.
- **Métrica de decisión (definida antes de empezar):** CPLc, con un mínimo de 5 calificados.
  - Si el CPLc de Intereses es ≥ 30 % peor que el de Amplia → apagar Intereses y consolidar todo en Amplia.
  - Si está dentro de ±30 % y por debajo de 40 USD → mantener ambos (escalado horizontal).
  - Si es ≥ 30 % mejor → pasar más presupuesto a Intereses.

**Para que el escalado rinda (fuera de la pauta):**
- Responde los WhatsApp en menos de 5 minutos en horario laboral. El costo por conversación es bajo, pero se desperdicia si el lead se enfría.
- Pasar de calificado a oportunidad está algo bajo (27 %, frente a un 30-50 % de referencia). Revisa el guion de calificación y ofrece una demo concreta.
- Marca en tu registro de ventas qué anuncio originó cada lead (por ejemplo, con un código en el mensaje prellenado de WhatsApp). Así, cuando cierre la venta, sabremos el CAC real por anuncio.
- Detalle de orden: las campañas dicen "BOFU", pero son de prospección. Y el hook dice "X": confírmame el texto real para registrarlo bien.

## Registro de aprendizaje
- **Filas agregadas** a `marketing/software-facturacion-pymes/historial-campanas.csv`:
  - Hook dolor A: **GANADOR**
  - Hook producto B: **PERDEDOR** (queda en la lista de "no repetir sin una hipótesis nueva")
- **Aprendizaje en una línea:** el hook de dolor + testimonio en Amplia saca un CPLc un 78 % menor que el hook de novedad de producto en Intereses (10,94 contra 50,60 USD). Todavía está confundido con la audiencia, y el test de esta semana lo resuelve.
- **Ficha creada** en `marketing/software-facturacion-pymes/perfil-marca.md`: modelo SaaS B2B para pymes, moneda USD, canal WhatsApp, **CPLc máximo = 40 USD** (confirmado) y una línea base provisional de 1 semana (CPM 3,32 · CTR 1,0 % · CPC 0,33 · CPL 3,38 · CPLc 18,15 USD · 18,6 % de calificación). La línea base propia se consolida cuando haya 4 semanas.

## Supuestos usados
- Modelo **SaaS B2B para pymes** con ciclo de venta de días a semanas (SUPUESTO). Por eso las 0 ventas de esta semana no cuentan todavía como fracaso.
- "Lead calificado" = pyme del perfil correcto con intención de demo o prueba (SUPUESTO). Uso tu conteo tal como viene en el CSV.
- La columna "presupuesto" (105) es semanal por conjunto, unos 15 USD/día (SUPUESTO).
- Las líneas base son rangos orientativos de Meta B2B en LATAM, no datos de tu marca.
- Sin ticket ni tasa de cierre no puedo calcular el CAC ni el ROAS. El CPLc de 40 USD se toma como techo tal como lo diste.

## Preguntas para mejorar la ficha
1. **¿Cuánto vale un cliente?** Precio del plan (mensual o anual) y cuántos meses se queda en promedio. Con eso calculo el CAC máximo y veo si el objetivo de 40 USD está bien puesto o si puedes pagar más por calificado para escalar más rápido.
2. **¿Qué % de las oportunidades o demos terminan comprando, y en cuántos días?** Así sabré cuándo exigirle ventas a esta cohorte.
3. **¿Qué criterio usa tu equipo para marcar un lead como "calificado"?** (Por ejemplo: tiene RUC o NIT activo, emite más de X facturas al mes, es el dueño o el contador.) Con eso afino el filtro del mensaje de WhatsApp.

**Decisión del trafficker:** hoy mismo apaga "Hook producto B". Sube "Hook dolor A" a 18 USD/día, lanza el test de audiencia con ese mismo anuncio en Intereses a 12 USD/día y vuelve a revisar el 1 de octubre para el siguiente +20 %.
