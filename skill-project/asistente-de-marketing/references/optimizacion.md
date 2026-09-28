# Optimización: reglas para apagar, mantener y escalar

## Protocolo de análisis (siempre en este orden)
1. **Qué funcionó:** métrica, magnitud y comparación con el periodo anterior o la línea base.
2. **Qué empeoró:** lo mismo.
3. **Por qué pudo ocurrir:** hipótesis (fatiga creativa, audiencia saturada, estacionalidad, cambio de oferta, subasta, problema en la landing, lentitud del asesor).
4. **Qué hipótesis probar ahora.**
5. **Qué apagar / mantener / escalar** (tabla).
6. **Cuánto presupuesto mover** (USD y %).
7. **Qué test nuevo ejecutar** (una sola variable).

## Criterios para apagar
| Condición | Acción |
|---|---|
| Gasto ≥ 2× CPL objetivo y 0 leads | Apagar el anuncio |
| Gasto ≥ 3× CPLc objetivo y 0 leads calificados | Apagar el anuncio o conjunto |
| CTR de enlace < 0,5 % con más de 2 000 impresiones (Meta, feed/Reels) | Cambiar el hook; si ya se cambió, apagar |
| Retención a 3 s < 20 % (video) | Cambiar los primeros 3 segundos |
| % de leads calificados < 10 % con ≥ 20 leads | Apagar o endurecer el formulario |
| Frecuencia > 4 en prospección (7 días) con CPL subiendo > 30 % | Rotar creativos o ampliar la audiencia |

## Criterios para mantener
- CPLc dentro de ±20 % del objetivo y volumen estable.
- Datos insuficientes, pero las métricas tempranas (CTR, retención) están sobre la línea base.

## Criterios para escalar
| Condición | Acción |
|---|---|
| CPLc ≤ 80 % del objetivo durante 7 días con ≥ 5 leads calificados | Subir el presupuesto un +20 % cada 48–72 h |
| Costo por oportunidad ≤ objetivo con ≥ 3 oportunidades | Subir +20–30 % y duplicar en una audiencia nueva (escalado horizontal) |
| Anuncio ganador claro en un test A/B (≥ 30 % mejor en CPLc con volumen mínimo) | Pasarlo a la campaña principal y apagar el perdedor |

No subas más del 20–30 % de golpe: reinicia el aprendizaje del algoritmo.

## Diseño de pruebas A/B
- Una variable por test: hook, formato, audiencia, oferta, canal de conversión (formulario, WhatsApp o landing) o CTA.
- Presupuesto parejo entre las variantes y duración mínima de 7 días (idealmente 14 en B2B).
- La métrica de decisión se define ANTES del test (normalmente CPLc).
- Registrar el resultado en `data/historial-campanas.csv` aunque el test pierda: ese es el aprendizaje.
