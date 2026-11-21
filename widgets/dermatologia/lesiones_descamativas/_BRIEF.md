# Brief común para ejecutores · Widget v11 «Lesiones descamativas» (multi, 6 entidades)

Carpeta: `widgets/dermatologia/lesiones_descamativas/`. Lee ANTES de escribir:
1. `.claude/skills/widget-ensenanza/SKILL.md` — §7 (componentes), §9 (layout multi, bloque `eK`), §10, §11 (contrato de marcado). Es obligatorio cumplirlo al pie de la letra.
2. Modelo de una entidad secundaria ya validada: `widgets/trastornos_animo/depresion_bipolar_suicidio/22_e2.html` (y `21_e1.html` si eres e1). Cópiale la estructura, no el contenido. Mira también cómo están escritos los simuladores en `.../90_sim.html` (helpers `sel num out rd`, funciones `par hv vacio` NO existen en el kit: si las necesitas, defínelas con prefijo propio, p. ej. `e3par`).
No leas `kit/`. No ejecutes construir.py (lo hace el orquestador).

## Router (fijo)
`Modo: multi · Entidades: e1=D. atópica (principal), e2=D. seborreica, e3=D. contacto, e4=Psoriasis, e5=P. rosada, e6=P. versicolor · Amenaza: e4 · Override: sí (6 entidades por excepción del estudiante)`

Textos exactos de botón: `D. atópica` · `D. seborreica` · `D. contacto` · `Psoriasis` · `P. rosada` · `P. versicolor`.
Presentación común: **placa o mancha eritematosa con escama (lesión descamativa) en consulta de primer nivel**. Eje: eccemas → papuloescamosa inmunomediada crónica → papuloescamosa autolimitada → infección superficial.
Sílabo: 2.ª rotación, Caso 8 «Lesiones dérmicas»: «dermatitis atópica, dermatitis seborreica, dermatitis de contacto y su diagnóstico diferencial con tiñas, pitiriasis y psoriasis»; «relación médico-paciente-familia en infantes con lesiones crónicas». Etiqueta `puce` solo para contenido nombrado ahí. «Tiña versicolor» = pitiriasis versicolor. La tiña del cuerpo (*tinea corporis*) es vecina fuera del grupo (va en «No confundir con…»).
Lo común al grupo lo escribe `vis` (presentación, cómo describir la lesión descamativa, KOH como prueba común del diferencial, emolientes como base común, corticoides tópicos por potencia —la escalera de potencias va en `vis`—). En tu entidad remite con `<span class="rem">↪ Escalera de potencias de corticoides en «Visión»</span>` cuando lo necesites y desarrolla solo lo propio. El botón de vis se llama `Visión`.

## Qué entregas (escribe archivos, no los muestres en el chat)
1. `2K_eK.html` (K = tu número): `<section class="tab" data-tab="eK">…</section>` completa según §9 «eK»: `hb az` «Frente a [vecina con texto de botón]» → PG (e1: 3–5; secundarias exactamente 3) → `div.nucleo` (3–5 li, ≤35 palabras, con citas) → badge(s) `b-pu` (guía, sociedad, año) → exactamente 7 `h2` hijos directos de la section: `Qué es` · `Epidemiología` (tabla 4 filas: Frecuencia · Edad · Sexo · Factores clave, con citas) · `Cadena` (`ol.tl` con nodos `li.nodo#eK-m-n[data-clin][data-paso]` + `.det` + `p.man` con xref; diagrama causa-efecto `figure.dg` si aclara; Feynman) · `Qué verás` (`.qv` con ≥4 estados + 1 `k`; fichas `.signo#eK-s-n`; tabla de signos menores opcional; e1 segundo Feynman aquí) · `Diagnóstico` (`ol.steps.tg` vocabulario dx con `data-paso` en cada li, un `1.º`; tabla de pruebas `Prueba · S · E · VPP/VPN · Utilidad · Notas · Ref.`; e1 simulador aquí) · `Tratamiento` (`ol.steps.tg` vocabulario tx, un `De elección`; diagrama de mecanismo de acción si aclara; tabla de fármacos `Fármaco · Mecanismo de acción · Dosis · Vía · Frecuencia · Duración · Notas/ajustes · Ref.` con `.xref` `← Paso` en Mecanismo; simulador) · `Seguimiento` (complicaciones por mecanismo con xref al nodo).
   - Ids: `eK-m-1…`, `eK-s-1…` consecutivos en orden DOM; xref `ir('eK','eK-m-3')`, solo dentro de tu entidad; enlaces recíprocos nodo↔signo (≤3 por nodo, ≤2 por signo; todo nodo `data-clin="1"` enlaza a signo).
   - Feynman: e1 exactamente 2 (tras Cadena y tras Qué verás); secundarias exactamente 1 (en Cadena).
   - Perlas `aside.perla[data-ex]` junto al tema (3–5 en secundarias, 5–8 en e1) con criterio fijo de etiquetas (§7.2c).
   - Pasos dx y tx: e4 (amenaza) debe tener `Alarma` en Diagnóstico y `Evita` en Tratamiento (p. ej. evitar corticoide sistémico por rebote pustuloso/eritrodérmico).
   - Remisiones: fuera de la tabla de fármacos, posología con `span.rem` «↪ Posología en «Tratamiento»»; en el h2 Tratamiento `↓ En la tabla`. S/E solo en tabla de pruebas.
   - Secundarias ≤1 200 palabras aprox. (delta); e1 profundidad completa (≤2 800 palabras).
   - Dermatología: «Qué verás» = lesión elemental + distribución; signos = Auspitz, Koebner, collarete, medallón heráldico, signo de la uñada (Besnier), signo de Hertoghe, Dennie-Morgan, luz de Wood, KOH «espagueti con albóndigas», dermatoscopia, prueba del parche, etc., cada uno con mecanismo.
   - Prohibido: estilos, `<style>`, `<a>`, `<img>`, `...` ASCII (usa …), `[VERIFICAR EN FUENTE]`, preguntas de opción múltiple, clases inventadas. Todo `button` con `type="button"`.
2. `_sim_eK.js`: el/los cuerpo(s) `function dcEKx(dc){…}` (sin etiqueta `<script>`) de tus simuladores (`div.dc[data-fn=dcEKx]`, p. ej. `dcE1dx`, `dcE1tx`, `dcE3tx`). Salida con posología completa y citas `[@clave]`; selección vacía → mensaje guía; dosis por peso con `rd()` y `Math.min` con tope; termina en `span.cf` contrafactual. Prohibido calcular VPP/VPN/LR/probabilidades. Todo fármaco del simulador está en tu tabla.
3. `_refs_eK.txt`: una línea por referencia NUEVA que cites (no las de la base): `@clave | Vancouver estricto completo, con doi:… y PMID: n solo si PubMed te los devolvió`. Clave con prefijo `eK_` (p. ej. `@e2_gupta2015`).
4. `_vis_eK.txt`: (a) las 9 celdas de tu columna para la tabla de `vis` (≤12 palabras cada una, en el orden de las 9 preguntas de §9), coherentes con tu `.qv` (fila 5 = tu celda `k`) y tus pasos (fila 7 = tu `1.º`/`Confirma`); (b) 1–2 banderas rojas; (c) etapa de Panorama: párrafo 70–110 palabras (dónde cae en el eje → mecanismo en una frase → signo que la delata → conducta decisiva → puente a la siguiente entidad) + perla ≤20 palabras; (d) lista `nucleo` para Anki (≤7 ítems, texto literal de tus `data-paso` de nodos `data-clin=1`, celda `k`, pasos `1.º` y `De elección`); (e) conteos: pg, fey, nodos, signos, simuladores; (f) 1–2 «errores que no se pueden cometer»; (g) chips útiles para el simulador diferencial de vis (hallazgo → por qué apunta a tu entidad).

## Citas: CLAVES, no números
Cita SIEMPRE con claves entre corchetes: `[@weidinger2018]`, varias `[@a][@b]`. El orquestador las convertirá a `[n]`. Toda cifra, dosis, umbral, criterio diagnóstico o algoritmo lleva cita. Cero marcas: si un dato no se confirma, elimínalo o reescribe sin la cifra.

Base común (puedes usarla sin verificar; el orquestador la confirma):
- `@bolognia5` Bolognia JL, Schaffer JV, Cerroni L, editors. Dermatology. 5th ed. Elsevier; 2024.
- `@fitzatlas9` Saavedra AP, Roh EK, Mikailov A, editores. Fitzpatrick. Atlas de dermatología clínica. 9.ª ed. McGraw Hill; 2023. (sílabo)
- `@guzman8` Guzmán R, editor. Dermatología. Atlas, diagnóstico y tratamiento. 8.ª ed. McGraw Hill; 2024. (sílabo)
- `@soutor2` Soutor C, Hordinsky MK, editores. Dermatología clínica. 2.ª ed. McGraw Hill; 2023. (sílabo)
- `@harrison22` Harrison's Principles of Internal Medicine 22.ª ed. 2025.
- `@sidbury2023` Guía AAD 2023 dermatitis atópica, tópicos (JAAD).
- `@davis2024` Guía AAD 2024 dermatitis atópica, fototerapia y sistémicos (JAAD).
- `@wollenberg2022` EuroGuiDerm atopic eczema 2022 (JEADV).
- `@weidinger2018` Weidinger S et al. Atopic dermatitis. Nat Rev Dis Primers 2018.
- `@langan2020` Langan SM et al. Atopic dermatitis. Lancet 2020.
- `@palmer2006` Palmer CN et al. Filaggrin loss-of-function. Nat Genet 2006.
- `@fonacier2015` Fonacier L et al. Contact dermatitis practice parameter update 2015 (JACI Pract).
- `@griffiths2021` Griffiths CEM et al. Psoriasis. Lancet 2021.
- `@menter2019` AAD-NPF psoriasis biológicos 2019. `@elmets2021` AAD-NPF tópicos 2021. `@menter2020` AAD-NPF sistémicos no biológicos 2020. `@elmets2019foto` AAD-NPF fototerapia 2019. `@elmets2019comorb` AAD-NPF comorbilidades 2019.
- `@ely2014` Ely JW et al. Diagnosis and management of tinea infections. Am Fam Physician 2014.
Para cualquier otra referencia (revisiones de seborreica, rosada, versicolor, fichas técnicas DailyMed, GPC MSP), BÚSCALA y verifícala tú con PubMed (`ToolSearch` "select:mcp__PubMed__search_articles,mcp__PubMed__get_article_metadata") o Consensus, y anótala en `_refs_eK.txt`. Las dosis que cambian conducta deben salir de una guía o ficha técnica leída (resumen PubMed o ficha); si no la confirmas, quítala.

## Al terminar
Responde en ≤15 líneas: archivos escritos, conteos (pg, fey, nodos, signos, perlas, simuladores), datos eliminados por no confirmarse, y dudas.
