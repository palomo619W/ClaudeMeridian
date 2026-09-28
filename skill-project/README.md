# Proyecto: Skill "Asistente de Marketing" — Miral Autobuses

Skill de Claude que actúa como **Trafficker Digital / Senior Performance Marketing Manager** de Miral Autobuses (Grupo Miral, Ecuador). Diseña, presupuesta, mide y optimiza campañas de Meta, TikTok y Google Ads orientadas a leads calificados y ventas de autobuses.

## Estructura
```
skill-project/
├── asistente-de-marketing/          ← LA SKILL (carpeta que se empaqueta)
│   ├── SKILL.md                     ← Rol, principios, enrutador y formatos obligatorios
│   ├── rutinas/                     ← Flujos de trabajo paso a paso
│   │   ├── 00-onboarding.md
│   │   ├── 01-nueva-campana.md      ← "Quiero pautar [PRODUCTO]" (20 secciones + Decisión)
│   │   ├── 02-analisis-optimizacion.md
│   │   ├── 03-presupuesto.md
│   │   ├── 04-creativos.md
│   │   ├── 05-reporte-periodico.md
│   │   └── 06-aprendizaje-continuo.md
│   ├── references/                  ← Guías y conocimiento de apoyo
│   │   ├── contexto-miral.md        ← Contexto de la marca y datos pendientes
│   │   ├── metodologia.md · funnel.md · creativos.md · leads-calificacion.md
│   │   ├── medicion-kpis.md · optimizacion.md · presupuesto.md
│   │   ├── lineas-base.md           ← Benchmarks de referencia y línea base propia
│   │   ├── conectores.md            ← Meta/Google/TikTok Ads, GA4, CRM, WhatsApp
│   │   └── plataformas/             ← meta-ads.md · tiktok-ads.md · google-ads.md
│   ├── assets/plantillas/           ← Respuesta de campaña, reporte, brief, CSV de resultados
│   ├── data/historial-campanas.csv  ← Memoria de aprendizaje continuo
│   ├── scripts/                     ← calcular_kpis.py · distribuir_presupuesto.py · registrar_aprendizaje.py
│   └── evals/evals.json             ← Casos de prueba (no se empaquetan)
├── dist/asistente-de-marketing.skill ← Paquete instalable
└── docs/skill_config_original.md     ← Especificación conceptual original
```

## Instalación
- **Claude.ai / app:** Configuración → Capacidades → Skills → subir `dist/asistente-de-marketing.skill`.
- **Claude Code:** copiar `asistente-de-marketing/` a `~/.claude/skills/` (o a `.claude/skills/` del proyecto).

## Volver a empaquetar
Desde la carpeta de scripts de skill-creator: `python -m scripts.package_skill <ruta>/asistente-de-marketing dist/`
