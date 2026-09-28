# Proyecto: Skill "Asistente de Marketing"

Skill **genérica** de Claude que actúa como **trafficker digital / Senior Performance Marketing Manager** para **cualquier marca**: e-commerce, servicios, negocios locales, B2B, B2G, educación o SaaS. Primero aprende la marca con un cuestionario breve y una **ficha de marca** que se va retroalimentando. Después diseña, presupuesta, mide y optimiza campañas de Meta, TikTok y Google Ads orientadas a resultados de negocio.

## Cómo funciona para el usuario
1. **Primera vez:** la skill pide 7 datos esenciales, con opciones y aceptando "no sé". Si el usuario comparte su web o un brief, los lee y solo confirma.
2. **Ficha de marca:** guarda lo aprendido en `marketing/<marca>/perfil-marca.md` o, en el chat, la entrega para que el usuario la guarde y la adjunte en la próxima conversación.
3. **Uso diario:** "Quiero pautar [producto]", "analiza estos resultados", "¿cómo reparto mi presupuesto?", "dame 3 ideas de video".
4. **Retroalimentación:** cada dato nuevo o resultado real se incorpora a la ficha y al historial de campañas. Los datos que faltan se piden cuando hacen falta, no todos al inicio.

## Estructura
```
skill-project/
├── asistente-de-marketing/              ← LA SKILL (carpeta que se empaqueta)
│   ├── SKILL.md                         ← Rol, paso cero (conocer la marca), enrutador, principios, formatos
│   ├── rutinas/                         ← Flujos paso a paso
│   │   ├── 00-onboarding.md             ← Cuestionario adaptativo y creación de la ficha
│   │   ├── 01-nueva-campana.md          ← "Quiero pautar [PRODUCTO]" (20 secciones + Decisión)
│   │   ├── 02-analisis-optimizacion.md
│   │   ├── 03-presupuesto.md
│   │   ├── 04-creativos.md
│   │   ├── 05-reporte-periodico.md
│   │   └── 06-aprendizaje-continuo.md
│   ├── references/                      ← Guías
│   │   ├── cuestionario-marca.md        ← Preguntas por nivel, con opciones, valores por defecto y para qué sirven
│   │   ├── memoria-de-marca.md          ← Dónde se guarda la ficha y el historial, y cómo se retroalimentan
│   │   ├── modelos-de-negocio.md        ← Métricas, canal y funnel según cómo vende la marca
│   │   ├── metodologia.md · funnel.md · creativos.md · leads-calificacion.md
│   │   ├── medicion-kpis.md · optimizacion.md · presupuesto.md · lineas-base.md
│   │   ├── conectores.md                ← Meta/Google/TikTok Ads, GA4, tiendas, CRM, WhatsApp
│   │   └── plataformas/                 ← meta-ads.md · tiktok-ads.md · google-ads.md
│   ├── assets/
│   │   ├── plantillas/                  ← perfil-marca.md, respuesta-campana.md, reporte-optimizacion.md,
│   │   │                                   brief-creativo.md, resultados-campana.csv, historial-campanas.csv
│   │   └── ejemplos/                    ← Ficha de ejemplo completa (solo ilustrativa)
│   ├── scripts/                         ← verificar_perfil.py · calcular_kpis.py ·
│   │                                       distribuir_presupuesto.py · registrar_aprendizaje.py
│   └── evals/evals.json                 ← Casos de prueba (no se empaquetan)
├── dist/asistente-de-marketing.skill    ← Paquete instalable
└── docs/skill_config_original.md        ← Especificación conceptual original
```

## Instalación
- **Claude.ai / app:** Configuración → Capacidades → Skills → subir `dist/asistente-de-marketing.skill`.
- **Claude Code:** copiar `asistente-de-marketing/` a `~/.claude/skills/` (o a `.claude/skills/` del proyecto).

## Volver a empaquetar
Desde la carpeta de scripts de skill-creator: `python -m scripts.package_skill <ruta>/asistente-de-marketing dist/`
