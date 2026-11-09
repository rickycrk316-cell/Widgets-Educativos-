# Brief común · ejecutores del widget de apertura

Repo `/home/user/Widgets-Educativos-`. No hagas commit ni push; no toques archivos que no te asignaron. Carpeta de trabajo: `widgets/trastornos_neurocognitivos/apertura/`.

## Lee primero (por secciones)
- `widgets/trastornos_neurocognitivos/PLAN.md` § «Widget B · Apertura» (términos, prerrequisitos, pid, problemas, jerarquía, hipótesis, diagramas, reparto) y § «Citas y verificación».
- Contrato: `fuentes/skill_apertura_v1.md` (completo, es corto) y, donde no diga nada, `.claude/skills/definiciones/SKILL.md` (alcance del paso 1, prerrequisitos con plantillas A/B/C, fuente única, contenido por pestaña, recall, clases con kit).
- `docs/DECISIONES_v11.md` § 7 (cero marcas, Vancouver).
- Caso: `fuentes/casos/caso_saquisili_trastornos_neurocognitivos.md`.
- Modelo hecho (estructura y clases exactas; no copies contenido): `widgets/trastornos_animo/apertura/` (`p05_c0`, `p10_t1`, `p91_pb`, `p92_jq`, `p93_hx`, `p96_js`). Imita su marcado: `section.tab#tK` que empieza con `h2`, `.hb`, `.pre>.pre-t` + `.acc.op`, `.rem-line` con `.chip-rs`, `.card`, `.card.fey`, `.card.ej`, `.card.vin` con `span.pid`, `.acc.no`, `.rc#rc-tK` con sus ids `-n -c -b -e`, `.gloss`, etc.

## Reglas clave
- **Alcance de apertura:** qué es, qué lo distingue, cómo se reconoce; sin tratamiento, dosis, algoritmos de manejo ni pronóstico numérico. **No resuelvas el caso**: el ejemplo de anclaje y la card «Por qué importa en este caso» vinculan el término a los `pid` sin afirmar el diagnóstico.
- **Fuente única:** cada prerrequisito se desarrolla solo en su pestaña canónica (tabla del PLAN); en las demás, solo `.rem-line` `↪ Prerrequisito ya desarrollado en «…»: … ` + recordatorio ≤20 palabras.
- **Cero marcas:** ni `[VERIFICAR EN FUENTE]` ni badge «Fuente por verificar». Cada definición con badge púrpura `b-pu` (fuente + año + `[@clave]`). Lo que no puedas confirmar, no lo escribas.
- Diseño: solo clases del kit de apertura (las del modelo). Prohibido `style=`, `<style>`, `<img>`, `<svg>`, `<a>`, recursos remotos, `...` ASCII, emojis (✅ ⚠️ ❌ incluidos), `↩` (usa `↪`). Tablas con `thead`/`tbody` en `div.tw`; tipo oración; párrafos ≤90 palabras; un `<b>` por párrafo; coma decimal; español de Ecuador.
- Diagramas: solo `figure.dg` (`dg-t`, `dg-row`, `dg-col`, `dg-n.b|p|s|fr|ac|ro` con ≤12 palabras por nodo, `dg-ar>span.dg-lab`, `figcaption.mini`).

## Citas
- `[@clave]` del catálogo `widgets/trastornos_neurocognitivos/_refs_catalogo.tsv`. Fuente nueva: verifícala con PubMed (ToolSearch `select:mcp__PubMed__search_articles,mcp__PubMed__get_article_metadata,mcp__PubMed__lookup_article_by_citation`), Consensus o WebSearch/WebFetch, y añádela a `apertura/_refs_<X>.tsv` (`clave<TAB>Vancouver`; PMID/DOI solo si la herramienta los devolvió; guías con `Disponible en: URL`). Claves nuevas con prefijo de tu letra (p. ej. `k_plum2019`).
- Cifras y umbrales (p. ej. osmolalidad plasmática, diuresis nocturna, Roma IV, Glasgow) con `[@clave]` y fuente leída. Anota en `apertura/_pend_<X>.tsv` (`dato<TAB>pestaña<TAB>fuente`) cada cifra y con qué la confirmaste.

## Mazos
No escribas `p96_js`. Escribe tus mazos en `apertura/_mazos_<X>.json`: `{"t1":[{"q":"…","a":"…","h":"…"}, …], …}`. Cloze con `{{…}}` dentro de `q` (y `a` = el texto ocultado). Reglas del recall de definiciones (atómicas, 1–2 de prerrequisito estructura→función o función→signo, ≥1 de discriminación, ≥1 que conecta con el caso, nada adivinable, sin listas >3). Cuántas: lo que diga tu tarea. En el HTML de cada pestaña con simulador pon el contenedor `.rc` igual que el modelo (`<div class="rc" id="rc-tK"><div class="rc-t">Simulador · Recall de …</div><div class="rc-count" id="rc-tK-n"></div><div class="rc-card" id="rc-tK-c"></div><div class="rc-btns" id="rc-tK-b"></div><div id="rc-tK-e"></div></div>`).

## Comprobación y entrega
- Partes largas: escribe en varias llamadas (Write + `cat >>`) cortando en límites estructurales; truncar en silencio es el único fallo inaceptable.
- Comprueba balance de etiquetas con python (`html.parser`), que tu JSON de mazos carga con `json.load`, y cadenas prohibidas.
- Informe final breve: por pestaña, nº de prerrequisitos canónicos (acordeones dentro de `.pre`), nº de `.rem-line`, nº de tarjetas; claves nuevas; datos eliminados por no confirmarse.
