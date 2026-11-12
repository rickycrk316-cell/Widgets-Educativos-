# Guía para Claude · Widgets educativos

Repo solo de estudio médico (Ricardo, Quirúrgica 2 · PUCE, 10.º nivel). Índice de widgets en `README.md`. **Regla de cero marcas** (widgets nuevos y migrados): ningún `[VERIFICAR EN FUENTE]` ni badge «Fuente por verificar» (el dato se confirma o se elimina). Los heredados (v10 congelados y las definiciones de dermatología, consumo de alcohol y ansiedad/pánico) conservan sus marcas hasta que se revisen. Sin contenido de marketing ni de otras marcas.

Fuente de verdad del diseño y del contenido v11: `docs/DECISIONES_v11.md`. Si algo contradice ese documento, se corrige. Skills del repo en `.claude/skills/`: `widget-ensenanza` (v11), `definiciones`, `apertura`, `flashcards` e `impeccable` (revisión, de terceros adaptada).

## Dónde mirar (ahorra tokens)

- **Edita y lee las partes**, nunca el HTML final: `widgets/<tema>/<id>/*.html`. El HTML final repite decenas de KB de kit en cada widget.
- No leas `kit/` (cabeceras, scripts, validadores) salvo que la tarea sea cambiar el kit. Clases y roles de color: `docs/DESIGN.md` y el §10 de `docs/DECISIONES_v11.md`.
- Para ubicar algo usa `grep -rn` sobre `widgets/<tema>/<id>/` en vez de abrir archivos enteros.
- Contratos de las skills de definiciones y apertura: `.claude/skills/definiciones/SKILL.md` y `fuentes/skill_apertura_v1.md` (léelos por secciones). Verificación de fuentes: `fuentes/protocolo_verificacion.md`.
- `PLAN.md` de cada tema explica por qué se partió el caso así; léelo antes de añadir o reordenar pestañas.

## Kits vivos y v10 congelado, según `manifiesto.json`

| `tipo` | Kit vivo | Uso |
|---|---|---|
| `"v11"` | `kit/v11/` (cabecera, script, validador, prueba de navegador) | widgets de enseñanza nuevos y migrados |
| `"definiciones"` | `kit/def_head.html`, `validar_definiciones.py`, `auditar_definiciones.py`, `probar_definiciones.js` | paso 1 del ABP |
| `"apertura"` | `kit/apertura_head.html`, `validar_apertura.py` (+ auditor y prueba de definiciones) | apertura del ABP |
| sin `tipo` (o `"v10"`) | ninguno: **congelado** | 17 widgets de enseñanza v10 |

**Congelado (v10)** = se conservan partes y HTML final versionados, pero no se reconstruyen ni se editan; el kit v10 se retiró. `construir.py` los reconoce (manifiesto sin `tipo`), lo informa y no toca el HTML. Migrar uno a v11 = reescribir sus partes con `tipo: "v11"` según `docs/DECISIONES_v11.md`, y recién entonces se construye.

`manifiesto.json`: `titulo`, `salida` (HTML final), `tipo`, `tema` (acento v11: `ginecologia`, `salud-mental`, `digestivo`, `urologia`, `pediatria-ortopedia`; otro → azul) y el resto que exige el validador (`modo`, `entidades`, `principal`, `amenaza`, `pg`, `fey`, `nodos`, `signos`, `dc`, `nucleo`). `nucleo` es la lista para Anki.

## Partes de un widget

| Modo | Archivos (orden = orden en el HTML) |
|---|---|
| multi | `01_nav` `02_pan` `05_vis` `21_e1`…`25_e5` `80_sin` `90_sim` |
| mono | `01_nav` `02_pan` `10_def` `11_fis` `12_cli` `13_dx` `14_tx` `15_seg` `16x_*` (extra) `90_sim` |
| definiciones | `p01_nav` `p10_t1`…`p90_t9` `p95_tg` `p96_js` |
| apertura | `p01_nav` `p05_c0` `p10_t1`…`p90_t9` `p91_pb` `p92_jq` `p93_hx` `p95_tg` `p96_js` (manifiesto: `terminos` `problemas` `hipotesis` `diagramas`) |
| v11 (multi/mono) | las mismas partes que multi/mono, con `div.nucleo`, `aside.perla`, `th>span.q+span.qx` y `li[data-paso]` (contrato en §10 de las decisiones) |

Reglas del kit (todos): las partes no llevan `<style>`, estilos en línea, recursos remotos, `localStorage` ni `position:fixed`. Cifras con cita Vancouver `[n]`; **cero `[VERIFICAR EN FUENTE]`** en lo nuevo: se agotan PubMed, Consensus, fichas técnicas, GPC del MSP y web, y lo no confirmado se elimina (`fuentes/protocolo_verificacion.md`). Tablas de fármacos con columna «Mecanismo de acción». Sin preguntas de opción múltiple (van en Anki).

## Flujo de revisión

1. Editar la parte.
2. `python3 kit/construir.py widgets/<tema>/<id>` → reensambla y valida; imprime solo errores y la línea `RESULTADO`.
3. `python3 kit/renumerar.py <carpeta>` si cambió el orden o el número de citas (Vancouver por primera aparición).
4. Si cambió algo visual o de JS en un widget v11: `node kit/v11/probar.js file://$PWD/<html> <carpeta_capturas_en_scratchpad>` (las capturas no se versionan). Para definiciones y apertura: `node kit/probar_definiciones.js`. Instalación única: `cd kit && npm ci` (`playwright-core` fijado en `kit/package.json`; no ejecutar `playwright install`; Chromium de `/opt/pw-browsers` o el de `PW_CHROMIUM`).
5. Definiciones: `python3 kit/auditar_definiciones.py <html> <n_terminos>`. Apertura: `python3 kit/validar_apertura.py <html> <manifiesto>` (lo corre `construir.py`) y el auditor de definiciones.
6. (Opcional, cambios visuales) Accesibilidad/pulido: `.claude/skills/impeccable/SKILL.md` (`audit`, `polish`, `clarify`); ante conflicto mandan `docs/DESIGN.md` y las reglas del kit.
7. Commit de partes + HTML final juntos. Si cambió una skill propia: `python3 kit/empaquetar_skills.py` y versionar `dist/*.skill`.

## Widget nuevo

Crear `widgets/<tema>/<id>/` con partes y `manifiesto.json` (`titulo`, `salida: "../<Nombre>_widget_v11.html"`, `tipo: "v11"`, `tema`), añadir fila en `README.md` y construir. Si el tema es nuevo, escribir su `PLAN.md`. Definiciones y apertura nuevas usarán las cabeceras v11 de `kit/v11/` cuando existan; hasta entonces, las de `kit/`. Nunca se crean widgets v10.

## Qué cuenta como éxito

El widget condensa muchas fuentes con la regla 20/80 (núcleo arriba, detalle debajo, nada se recorta), perlas de examen etiquetadas (PUCE, CACES, USMLE 1/2, MIR, ENARM) y recuerdo activo con «Ordenar». Detalle en `docs/DECISIONES_v11.md` y `docs/PRODUCT.md`.
