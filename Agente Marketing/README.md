# Agente Marketing — Mark

Skill **`agente-marketing`**: *Mark*, un asistente de marketing que coordina tres skills ya instaladas en Claude:

| Especialista | Skill |
|---|---|
| Trafficker digital (Meta, TikTok y Google Ads, leads) | `asistente-de-marketing` (`trafficker-digital.skill`) |
| Psicología del marketing | `marketing-psychology` |
| Carruseles de Instagram | `carrusel-studio` |

## Contenido

- `agente-marketing.skill`: el paquete para instalar (es un zip con la carpeta de la skill).
- `agente-marketing/`: el código fuente de la skill.
  - `SKILL.md`: la identidad de Mark, el flujo de cada conversación, el enrutador y las reglas.
  - `rutinas/`: 00 bienvenida · 01 verificar skills y memoria · 03 saludo con headlines del día · 02 entrevista única de marca · 10 carruseles · 11 análisis psicológico · 12 línea guía de publicidad · 13 estrategia compuesta · 14 check-in diario · 15 tarea programada.
  - `references/`: skills conectadas, mapa de datos (para no repetir preguntas), menús de opciones, memoria compartida y recomendaciones.
  - `assets/plantillas/`: estado de Mark, contexto de producto y estrategia compuesta.
  - `scripts/detectar_contexto.py`: encuentra fichas, sistemas visuales y contexto guardado en la carpeta de trabajo.

## Instalación

1. En Claude, ve a **Configuración → Capacidades → Skills → Subir skill** y elige `agente-marketing.skill`.
2. Comprueba que también estén instaladas las tres skills especialistas. Si falta alguna, Mark te lo dirá y te explicará cómo cargarla.
3. Escribe **"Hola Mark"** para empezar.

## Regenerar el paquete

```bash
cd <skill-creator> && python3 -m scripts.package_skill "<ruta>/Agente Marketing/agente-marketing" "<ruta>/Agente Marketing"
```
