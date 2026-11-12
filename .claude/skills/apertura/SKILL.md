---
name: apertura
description: Apertura del ABP en un solo widget HTML (evoluciona la skill definiciones v5.1): términos desconocidos del caso, problemas biológicos, psicológicos, sociales y factores de riesgo con fisiopatología y diagramas, jerarquización por morbimortalidad e hipótesis diagnósticas, con recall. Úsala cuando el estudiante entregue un caso y una lista de términos para la sesión de apertura.
---

# Apertura ABP (v1)

El contrato completo está en `fuentes/skill_apertura_v1.md`; donde no diga nada, manda `fuentes/skill_definiciones_v5.1.md` (y `.claude/skills/definiciones/SKILL.md`). Léelos por secciones.

**Cero marcas.** Ni `[VERIFICAR EN FUENTE]` ni badge «Fuente por verificar»: se agotan PubMed, Consensus, fichas técnicas, GPC del MSP y web (`fuentes/protocolo_verificacion.md`) y lo no confirmado se elimina.

**Diseño v11.** Los widgets nuevos usarán `kit/v11/apertura_head.html` (restilizada: estilo app, fuente del sistema, acento por tema; `docs/DESIGN.md`) cuando exista; hasta entonces se usa `kit/apertura_head.html`. Las clases no cambian y los widgets ya hechos no se tocan.

## Flujo

1. Guarda el caso en `fuentes/casos/caso_<paciente>_<tema>.md` (transcripción fiel).
2. Escribe `widgets/<tema>/PLAN.md`: router, esqueleto de problemas (B, P, S, FR con ids), jerarquía propuesta, hipótesis y diagramas. Ejemplo: `widgets/sindrome_confusional/PLAN.md`.
3. Crea `widgets/<tema>/apertura/manifiesto.json` con `tipo: "apertura"`, `terminos`, `problemas`, `hipotesis`, `diagramas`.
4. Escribe las partes `p01_nav p05_c0 p10_t1…p90_t9 p91_pb p92_jq p93_hx p95_tg p96_js` con el vocabulario de `kit/apertura_head.html` (clases en `docs/DESIGN.md` y en el contrato). Diagramas solo con `figure.dg` (HTML/CSS, sin imágenes ni SVG).
5. `python3 kit/construir.py widgets/<tema>/apertura` → verde; `node kit/probar_definiciones.js file://$PWD/<html> <capturas_en_scratchpad>`.
6. Añade la fila en `README.md` y haz commit de partes + HTML final.

Trabajo en paralelo (orquestador + ejecutores): citas como `[@clave]` y archivos `_refs_<ejecutor>.tsv` / `_mazos_<ejecutor>.json` en la carpeta del widget; el integrador numera Vancouver por primera aparición, arma `p96_js` y borra los `_*`.
