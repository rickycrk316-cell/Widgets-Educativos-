# Brief común · ejecutores del widget de enseñanza (v11)

Repo `/home/user/Widgets-Educativos-`. No hagas commit ni push; no toques archivos que no te asignaron.

## Lee primero (por secciones)
- `widgets/trastornos_neurocognitivos/PLAN.md` (completo: router, contrato de `vis`, conteos, reparto).
- `.claude/skills/widget-ensenanza/SKILL.md`: §3, §5, §6, §7, §9, §10, §11 (es la regla).
- `docs/DECISIONES_v11.md` (§2, §3, §4, §5, §7, §10).
- Caso: `fuentes/casos/caso_saquisili_trastornos_neurocognitivos.md`. Sílabo: `grep -n "Caso 6" -A 12 fuentes/syllabus_quirurgica2_segunda_rotacion.md`.
- Modelo v11 (estructura y clases, no contenido): `widgets/trastornos_animo/depresion_bipolar_suicidio/` (`05_vis`, `22_e2`, `80_sin`, `90_sim`, `02_pan`).
- Catálogo de citas: `widgets/trastornos_neurocognitivos/_refs_catalogo.tsv`.

## Contenido
- Profundidad de examen (PUCE, CACES, USMLE 1/2, MIR, ENARM). Secundarias: estructura §9 `eK` completa (hb az «Frente a …» → 3 PG → `div.nucleo` 3–5 li → badge `b-pu` → 7 `h2`: Qué es · Epidemiología · Cadena · Qué verás · Diagnóstico · Tratamiento · Seguimiento), 1 Feynman tras «Cadena», `.qv` con su celda `k` (la del PLAN), ids `eK-m-n` / `eK-s-n`, enlaces recíprocos nodo↔signo (§7.6), conteos de nodos y signos del PLAN, simulador bajo «Tratamiento».
- Adaptación al área (§4): «Qué verás» = examen mental/cognitivo y neurológico; signos = escalas y maniobras con su mecanismo; umbrales de escalas con cita.
- Lo común al grupo vive en `vis`; en `eK` remite con `span.rem` `↪ … en «Visión de conjunto»`.
- Tablas de fármacos: `Fármaco · Mecanismo de acción · Dosis · Vía · Frecuencia · Duración · Notas/ajustes · Ref.`; tabla de pruebas: `Prueba · S · E · VPP/VPN · Utilidad · Notas · Ref.`.
- Pasos `ol.steps.tg>li[data-paso]>span.tg` con el vocabulario cerrado de §11 (un `1.º`, un `De elección`), sin dosis.
- Perlas `aside.perla[data-ex]` junto al tema (criterio fijo de DECISIONES §3).

## Citas y verificación (cero marcas)
- Cita con `[@clave]` del catálogo. Fuente nueva: verifícala tú con PubMed (carga con ToolSearch `select:mcp__PubMed__search_articles,mcp__PubMed__get_article_metadata,mcp__PubMed__lookup_article_by_citation`), Consensus o WebSearch/WebFetch (DailyMed para fichas) y añádela a `widgets/trastornos_neurocognitivos/ensenanza/_refs_<X>.tsv` (`clave<TAB>Vancouver`; `PMID: n` y `doi:` solo si la herramienta los devolvió; guías con `Disponible en: URL`). Claves nuevas con prefijo de tu letra para no chocar (p. ej. `b_cummings2023`).
- Toda dosis, umbral, punto de corte o cifra lleva `[@clave]` y está confirmada en una fuente leída. Lo que no confirmes, no lo escribas: cero `[VERIFICAR EN FUENTE]`. Anota en `ensenanza/_pend_<X>.tsv` (`dato<TAB>parte<TAB>fuente`) cada dosis/umbral/cifra y con qué la confirmaste.

## Simuladores
Funciones `dcXxx(dc)` en `ensenanza/_sim_<X>.js` (JS plano, sin `<script>`), con los helpers del kit `sel num out rd` y los comunes `par(t)`, `hv(a,v)`, `vacio(dc,t)` (los define el orquestador en `90_sim`). Selección vacía → mensaje guía. Sin probabilidades, VPP, LR ni Bayes (§7.10). Dosis por peso con `rd()` y `Math.min`. Todo fármaco simulado figura en tu tabla. Salida acaba en `span.cf{Si … → …}`. Citas en el JS también como `[@clave]`.

## Diseño
Solo clases del kit (§11). Prohibido `style=`, `<style>`, `<img>`, `<a>`, recursos remotos, `...` ASCII (usa `…`), emojis, `localStorage`. Tablas con `thead`/`tbody` dentro de `div.tw`; sin recuadros anidados; tipo oración; párrafos ≤90 palabras; un `<b>` por párrafo; coma decimal; todo `button` con `type="button"`; español de Ecuador, voz activa.

## Comprobación y entrega
- Partes largas: escribe en varias llamadas (Write + `cat >>`) cortando en límites estructurales. Truncar en silencio es el único fallo inaceptable.
- Comprueba balance de etiquetas con python (`html.parser`) y cadenas prohibidas.
- Informe final breve: conteos reales (PG, li del núcleo, nodos, signos, Feynman, simuladores), 3–7 ítems literales del núcleo para Anki por entidad (data-paso de nodos clínicos, celda k, paso 1.º, De elección), claves nuevas y datos eliminados por no confirmarse.
