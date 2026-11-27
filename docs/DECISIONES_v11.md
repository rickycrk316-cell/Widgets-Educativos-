# Widgets de enseñanza v11 · decisiones del estudiante (fuente única)

Acordado con Ricardo en 7 rondas de preguntas (2026-11-07). Todo documento, skill, kit o brief que contradiga esto se corrige o se borra.

## 1 · Propósito

- El widget **condensa muchas fuentes**. Rige primero la **regla 20/80**: el 20 % de la información que hace entender el otro 80 %. Sobre esa base va la información específica que toman en exámenes.
- Exámenes objetivo: **Examen Integral PUCE**, **habilitación CACES (Ecuador)**, **USMLE (Step 1 y Step 2 CK)**, **MIR (España)** y **ENARM (México)**, sumados a los requisitos del sílabo cuando el tema está en él (si no está, sin sílabo: guías vigentes y temarios de examen).
- **No se recorta información**: se reordena. Núcleo arriba, detalle completo debajo.
- Sin preguntas de práctica de opción múltiple: eso va en Anki.

## 2 · Estructura de cada pestaña de contenido

Orden fijo:
1. **Preguntas guía** (se mantienen, como en v10).
2. **Núcleo** (`div.nucleo`): tarjeta destacada con 3–5 ideas (`ul` de 3–5 `li`, ≤35 palabras cada una) que explican el resto de la pestaña: mecanismo central, el dato que lo delata, la conducta decisiva. Es el 20 %. Cada idea con su `[n]` si lleva dato.
3. **Detalle**: todo el contenido actual, reordenado por relevancia (componentes v10: timeline, signos, «Qué verás», tablas, Feynman, simuladores).
4. **Perlas de examen** junto al tema que tocan (`aside.perla`), no agrupadas al final.

Se quitan: tablas «Esquema DSM-5-TR» y cualquier tabla-índice que solo diga dónde está cada cosa; modos «Timeline en blanco» y «Tabla en blanco».
Se mantienen: simuladores de decisión, Feynman, Panorama (pestaña inicial), Errores (multi) y la referencia final.

## 3 · Perlas de examen

`aside.perla[data-ex="…"]>div.perla-t{Perla de examen}+p{dato con [n]}`. `data-ex` lleva uno o varios de: `puce caces usmle1 usmle2 mir enarm`. **Criterio fijo por tipo de dato** (no se afirma frecuencia de preguntas):
- mecanismo, fisiología, farmacología básica, anatomía → `usmle1`;
- conducta clínica, diagnóstico y tratamiento según guías internacionales → `usmle2 mir enarm`;
- dato de una GPC, lineamiento o norma del MSP del Ecuador → `caces`;
- contenido nombrado en el sílabo del caso → `puce`.
El kit muestra las etiquetas como chips y un filtro global por examen (Todos · PUCE · CACES · USMLE 1 · USMLE 2 · MIR · ENARM).

## 4 · Visión de conjunto (multi)

La tabla comparativa usa **filas como preguntas** con una mini explicación de qué hay que responder: `tr>th>(span.q{pregunta}+span.qx{qué se busca, ≤15 palabras})`. Ejemplos: «¿Cuál es el mecanismo principal que explica la enfermedad?» en vez de «Falla central»; «¿En qué persona o población es más frecuente?» en vez de «Terreno típico». Las 9 filas del contrato v10 se mantienen como contenido, reformuladas así.

**Multi ampliado (6–15 entidades en un solo widget).** Cuando el temario del sílabo o del docente agrupa más de 5 entidades y Ricardo lo quiere en un único widget, no se parte: la tabla lleva una columna por entidad, las partes se nombran `2NN_eK` (`201_e1` … `213_e13`), las secundarias admiten 3–5 preguntas guía y 1–2 Feynman, `vis` admite hasta 3 simuladores diferenciales (uno por bloque) y el Panorama crece a ≈110 palabras por etapa. Primer uso: síndromes geriátricos (13 entidades).

## 5 · Recuerdo activo: ordenar pasos

Sustituye a los modos en blanco. Se activa y desactiva con un botón «Ordenar» en cada bloque elegible:
- cadena fisiopatológica (`ol.tl`, frase = `data-paso` de cada nodo),
- algoritmo diagnóstico (`ol.steps.tg` de Diagnóstico),
- escalonamiento del tratamiento (`ol.steps.tg` de Tratamiento).
Cada `li` de `ol.steps` lleva `data-paso` (≤10 palabras, frase clave). Al activar: aparece una caja con las frases desordenadas y una fila de huecos numerados; se **arrastra** (iPad, Mac) o se **toca la frase y luego el hueco** (iPhone; ambos funcionan en todos). Botón «Revisar»: los pasos mal ubicados se recolocan con animación en el orden correcto, se marcan aciertos y errores y se **despliega la explicación** completa de cada paso. «Reiniciar» vuelve a barajar. Nada se guarda.

## 6 · Diagramas

Solo donde aclaran más que el texto (sin mínimos por pestaña). Mismo vocabulario `figure.dg` (`dg-t`, `dg-row`, `dg-col`, `dg-n.fr|b|p|ac|s|ro`, `dg-ar>span.dg-lab`, `figcaption`) con el diseño nuevo. `div.duo` se mantiene para emparejar texto y diagrama.

## 7 · Se mantiene de v10.2

- Columna **«Mecanismo de acción»** en toda tabla de fármacos (`Fármaco · Mecanismo de acción · Dosis · Vía · Frecuencia · Duración · Notas/ajustes · Ref.`).
- **Cero `[VERIFICAR EN FUENTE]`**: se agotan PubMed, Consensus, fichas técnicas (DailyMed, CIMA-AEMPS, EMA, ARCSA), GPC y lineamientos del MSP (www.salud.gob.ec) y web; lo que no se confirme se elimina (`fuentes/protocolo_verificacion.md`). Rige también para definiciones y apertura (sin badge «Fuente por verificar»).
- **Citas Vancouver numeradas** por primera aparición (`kit/renumerar.py`).
- **Referencias con hipervínculos**: cada referencia de `ol.vanc` enlaza a la página de la fuente usada (DOI → doi.org, PMID → PubMed, ficha → DailyMed por su Setid, guía o web → su URL). El script del kit v11 genera los botones a partir del texto Vancouver; por eso cada referencia debe llevar su DOI, PMID, Setid o «Disponible en: URL» cuando existan. Sin identificador (libros), el kit enlaza a una búsqueda en Google Académico.

## 8 · Diseño (UI)

- **Estilo app de estudio moderna**: tarjetas con esquinas suaves (12–16 px), mucho aire, tipografía grande y clara, jerarquía por tamaño y peso, sin filetes de periódico. Inspiración: taste-skill (un sistema, bordes iguales, micro-interacciones discretas), sin fotos ni efectos de sitio web.
- **Fuente del sistema** (San Francisco en Apple): `-apple-system, system-ui, …`. Sin recursos externos; funciona sin internet.
- **Paleta neutra con un acento por tema**: fondo blanco o gris muy claro (negro/gris muy oscuro en modo oscuro automático), texto casi negro, un color de acento por tema declarado en el manifiesto (`"tema"`: `ginecologia` frambuesa, `salud-mental` índigo, `digestivo` verde azulado, `urologia` ámbar oscuro, `pediatria-ortopedia` azul, otro → azul). Rojo, ámbar y verde solo para alarma, precaución y correcto.
- **Navegación adaptable**: iPhone (<760 px) barra inferior fija con las pestañas (icono de texto corto + nombre) y desplazamiento horizontal si no caben; iPad y Mac (≥760 px) menú lateral fijo con las pestañas y, bajo la activa, sus `h2` para saltar dentro de la pestaña. Filtro de perlas accesible desde la barra o el menú.
- **Animaciones sutiles**: transición suave al cambiar de pestaña, tarjetas que se elevan 2 px al pasar el puntero o tocar, aparición escalonada de los pasos al revisar el ejercicio de ordenar. Respeta `prefers-reduced-motion`.
- Tablas: fichas apiladas en iPhone (como v10.2); en iPad/Mac, tablas limpias con cabecera fija dentro del contenedor.
- Sin barra de progreso.

## 9 · Convivencia y alcance

- **Kit v11 aparte**: `kit/v11/` (cabecera, script, validador, prueba de navegador). Solo lo usan los widgets con `"tipo": "v11"` en el manifiesto. Los widgets v10.2 están **congelados** (sin `tipo`; el kit v10 se retiró): conservan partes y HTML, pero no se reconstruyen ni se editan hasta migrarlos.
- **Piloto**: `widgets/ginecologia/menopausia_th` (ciclo ovárico, menopausia y terapia hormonal), **sin sílabo**.
- Skills de definiciones y apertura: adoptan el diseño v11 y la regla de cero marcas para widgets futuros; los widgets ya hechos no se tocan.
- Documentos obsoletos (prompt v10, skill v10 y v10.2, briefs) se **borran**; CLAUDE.md, README, DESIGN.md y PRODUCT.md se reescriben para v11. El kit v10.2 se retiró: los widgets antiguos quedan congelados.

## 10 · Contrato de clases nuevas del kit v11 (kit, validador y skill lo comparten)

| Clase / atributo | Dónde | Qué es |
|---|---|---|
| `div.nucleo>div.nucleo-t{Núcleo}+ul>li` | tras las PG de cada pestaña de contenido | el 20 % |
| `aside.perla[data-ex]>div.perla-t+p` | junto al tema | perla de examen con etiquetas |
| `th>span.q+span.qx` | filas de `table.vis` | pregunta y mini explicación |
| `li[data-paso]` en `ol.steps.tg` | Diagnóstico y Tratamiento | frase clave para ordenar |
| `html[data-tema]` | lo pone `construir.py` desde `manifiesto.tema` | acento del tema |
| `.ord`, `.ord-bank`, `.ord-slots`, `.ord-chip`, `.ord-slot`, `.ord-ok`, `.ord-ko`, `.ord-btns` | generadas por el script | ejercicio de ordenar (no se escriben en las partes) |
| `nav.side`, `nav.bottom`, `.perla-filtro` | generadas por el script a partir de `nav.tabs` | navegación adaptable |

Las partes siguen escribiendo `nav.tabs>button.tb` (01_nav) y el script construye la navegación adaptable a partir de ella.
