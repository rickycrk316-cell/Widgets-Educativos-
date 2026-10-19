---
name: impeccable
description: Revisión de calidad de widgets HTML autocontenidos (audit, polish, clarify) del repo de estudio médico. Úsala solo si se pide revisar accesibilidad, pulido final o claridad del texto de un widget tras un cambio visual.
license: Apache 2.0
---

# Impeccable (versión mínima para Widgets educativos)

Origen y modificación: derivada de la skill `impeccable` (Apache 2.0, ver `LICENSE`), recuperada de la rama `claude/dolor-abdominal-widgets`. Este `SKILL.md` está reescrito y reducido; solo se conservan 3 referencias, con una nota de adaptación al inicio de cada una. Se eliminaron scripts, descargas, PRODUCT.md propio, `live` y el resto de comandos.

## Contexto y precedencia

- Lee `docs/DESIGN.md` antes de empezar. No hay paso de setup ni launcher `impeccable context`.
- Si algo de esta skill o sus referencias entra en conflicto, manda `docs/DESIGN.md` y las reglas del kit (`CLAUDE.md`). Los kickers y la numeración de secciones del kit son válidos.
- Widgets autocontenidos y offline: sin recursos remotos, sin fuentes web, sin `<style>` en las partes, sin `position:fixed`, sin `localStorage`. Ignora bundle size, lazy loading e imágenes.
- Edita solo las partes `widgets/<tema>/<id>/*.html` y reconstruye con `python3 kit/construir.py`. Nunca modifiques el kit.

## Comandos

| Comando | Qué hace | Referencia |
|---|---|---|
| `audit` | Informe técnico (a11y, tema, responsive, integridad) con puntuación 0-4 y severidad P0-P3; no corrige | `reference/audit.md` |
| `polish` | Pasada final de consistencia con el sistema del kit | `reference/polish.md` |
| `clarify` | Mejora de etiquetas y microcopy sin alterar el contenido clínico | `reference/clarify.md` |

Lee solo la referencia del comando pedido. Es complementaria a `kit/auditar_diseno.py` y `kit/probar_navegador.js`, no las sustituye. Resultado: informe en el chat.
