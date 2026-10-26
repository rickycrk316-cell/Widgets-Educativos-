# Guía para Claude · Widgets educativos

Repo solo de estudio médico (Ricardo, Quirúrgica 2 · PUCE, 10.º nivel). Índice de widgets en `README.md`. Sin contenido de marketing ni de otras marcas.

## Dónde mirar (ahorra tokens)

- **Edita y lee las partes**, nunca el HTML final: `widgets/<tema>/<id>/*.html`. El HTML final repite ~27 KB de kit en cada widget.
- No leas `kit/kit_head.html`, `kit/kit_script.html`, `kit/def_head.html` ni `kit/validar.py` salvo que la tarea sea cambiar el kit. Clases y roles de color: `docs/DESIGN.md`.
- Para ubicar algo usa `grep -rn` sobre `widgets/<tema>/<id>/` en vez de abrir archivos enteros.
- `fuentes/prompt_widget_ensenanza_v10.md` (60 KB) es el documento de proyecto con el kit v10 original (CSS v10, no Vademécum). Las reglas completas de la skill están en `fuentes/skill_widget_ensenanza_v10.md` y `fuentes/skill_definiciones_v5.1.md`: léelas solo por secciones cuando haga falta una regla concreta.
- `PLAN.md` de cada tema explica por qué se partió el caso así; léelo antes de añadir o reordenar pestañas.

## Partes de un widget

| Modo | Archivos (orden = orden en el HTML) |
|---|---|
| multi | `01_nav` `02_pan` `05_vis` `21_e1`…`25_e5` `80_sin` `90_sim` |
| mono | `01_nav` `02_pan` `10_def` `11_fis` `12_cli` `13_dx` `14_tx` `15_seg` `16x_*` (extra) `90_sim` |
| definiciones | `p01_nav` `p10_t1`…`p90_t9` `p95_tg` `p96_js` |

`manifiesto.json`: `titulo`, `salida` (HTML final) y `tipo` son del ensamblador; el resto (`modo`, `entidades`, `principal`, `amenaza`, `pg`, `fey`, `nodos`, `signos`, `dc`, `nucleo`) los exige `validar.py`. `nucleo` es la lista para Anki. En definiciones, `terminos`, `prerrequisitos`, `remisiones` y `tarjetas` (listas por pestaña) los exige `validar_definiciones.py`.

Construye siempre con `kit/construir.py`: el kit del repo (`kit/kit_head.html`) es la variante Vademécum y prevalece sobre el CSS del prompt/skill.

Reglas del kit: las partes no llevan `<style>`, estilos en línea, recursos remotos, `localStorage` ni `position:fixed`. Cifras con cita Vancouver `[n]` o marcadas `[VERIFICAR EN FUENTE]`.

## Flujo de revisión

1. Editar la parte.
2. `python3 kit/construir.py widgets/<tema>/<id>` → reensambla y valida; imprime solo errores y la línea `RESULTADO`.
3. Si cambió algo visual o de JS: `node kit/probar_navegador.js file://$PWD/<html> <carpeta_capturas_en_scratchpad>` (las capturas no se versionan). Instalación única de la herramienta: `cd kit && npm ci` (`playwright-core` 1.64.1 fijado en `kit/package.json`; no ejecutar `playwright install`; Chromium de `/opt/pw-browsers` o el de `PW_CHROMIUM`). Para definiciones usa `node kit/probar_definiciones.js` (mismos argumentos).
4. Para definiciones: `python3 kit/auditar_definiciones.py <html> <n_terminos>` (`<n_terminos>` puede ser el manifiesto). Auditoría de diseño/router: `python3 kit/auditar_diseno.py <html> <manifiesto> "<línea del router del PLAN>"`.
4b. (Opcional, cambios visuales) Revisión de accesibilidad/pulido: sigue `.claude/skills/impeccable/SKILL.md` (comandos `audit`, `polish`, `clarify`), leyendo solo la referencia del comando pedido. Es complementaria a `kit/auditar_diseno.py`; ante conflicto mandan `docs/DESIGN.md` y las reglas del kit.
5. Commit de partes + HTML final juntos.

## Widget nuevo

Crear `widgets/<tema>/<id>/` con partes y `manifiesto.json` (con `titulo` y `salida: "../<Nombre>_widget_v10.html"`), añadir una fila en `README.md` y construir. Si el tema es nuevo, escribir su `PLAN.md`.

## Actualizar a una versión nueva (v11)

Re-extraer el kit del nuevo documento de proyecto y comparar con `kit/`: `validar.py` y `kit_script.html` se reemplazan directo; `kit_head.html` se reaplica sobre Vademécum. Luego reconstruir todos los widgets y actualizar `fuentes/skill_*.md`.
