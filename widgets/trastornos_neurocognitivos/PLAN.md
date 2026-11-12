# Trastornos neurocognitivos — plan del orquestador

Caso: `fuentes/casos/caso_saquisili_trastornos_neurocognitivos.md` (medicatura rural, Centro de Salud de Saquisilí, **sin posibilidad de derivar**; varón que vive solo, traído por su hijo porque «no actúa como él mismo» desde hace dos días, con conciencia que fluctúa entre lúcido y somnoliento o estuporoso; deambuló horas al calor; inquieto el día previo; cuadro viral hace dos semanas; polaquiuria y nocturia con volumen disminuido; estreñimiento de dos semanas; sed aumentada con ingesta de agua reducida; fatiga de meses).

Sílabo: 2.ª rotación, **Caso 6 — Síndrome confusional agudo y demencia** (síndrome confusional agudo; trastornos cognitivos menores por Alzheimer y Parkinson; demencias vascular, con cuerpos de Lewy, en la enfermedad de Parkinson y frontotemporal; trabajo autónomo: envejecimiento cerebral y evaluación cognitiva del adulto mayor). Toca también el **Caso 3 — Síndromes geriátricos** (delirio, demencia, valoración geriátrica integral).

Bibliografía: sílabo de la 2.ª rotación con las ediciones vigentes del protocolo § 4 (el sílabo cita Harrison 19.ª y Farreras 17.ª: **discrepancia**; se usan Harrison 22.ª 2025 y Farreras 20.ª 2024; Snell 7.ª 2010 → Snell 9.ª 2025) + Kane 8.ª 2018 + Ebert 4.ª 2025 + MSP Adultos mayores 2010 + DSM-5-TR 2022 + guías: NICE CG103 delirium (actualizada 2023), SIGN 157 (2019), NICE NG97 demencia (2018), NIA-AA (2011 y revisión 2024), McKeith 2017 (cuerpos de Lewy), Rascovsky 2011 y Gorno-Tempini 2011 (frontotemporal), VASCOG/Sachdev 2014 (vascular), AGS Beers 2023, Comisión Lancet 2024 (factores modificables), y para las causas del caso: ADA 2024 crisis hiperglucémicas, revisiones de hipercalcemia, hipernatremia y golpe de calor.

## Versión del kit

v11 real (rama `claude/happy-mendel-ylorra`): enseñanza con `tipo: "v11"` (`kit/v11/`); apertura con `tipo: "apertura"` (`kit/apertura_head.html`, aún sin cabecera v11). Regla de cero marcas en ambos (`docs/DECISIONES_v11.md`).

## Pistas del caso (sin resolver el caso por el estudiante)

| Pista | Por qué importa | Dónde |
|---|---|---|
| Cambio agudo (2 días) con conciencia que fluctúa entre lúcido y somnoliento/estuporoso | Inicio agudo + curso fluctuante + nivel de conciencia alterado: rasgos cardinales del delirium (CAM) | vis (eje 1 y 2), e1 |
| Inquieto el día previo; luego somnoliento | Pródromo y paso de forma hiperactiva a hipoactiva o mixta | e1 (subtipos) |
| Polaquiuria/nocturia, sed aumentada, estreñimiento, fatiga de semanas | Constelación de **hipercalcemia** (diabetes insípida nefrogénica, hipomotilidad, astenia) y de **hiperglucemia** (diuresis osmótica): causa metabólica del delirium | e1 (tabla de etiología, simulador dx), vis |
| Calor por horas + ingesta de agua reducida pese a la sed | Deshidratación hipertónica, agotamiento o golpe de calor; el adulto mayor pierde sed y capacidad de concentrar | e1 (Cadena, Tratamiento) |
| Cuadro viral hace dos semanas | Precipitante infeccioso clásico (y del estado hiperosmolar) | e1 |
| Vive solo; hijo visita ocasionalmente; reducción de salidas | Detección tardía; ¿demencia previa no reconocida como terreno? El hijo es informante intermitente | vis (no confundir delirium con demencia; delirium sobre demencia), e2 |
| Saquisilí sin derivación | Todo el estudio y manejo inicial en el centro de salud: glucometría capilar, tira de orina, ECG (QT corto en hipercalcemia), hidratación IV, vigilancia | e1 (Diagnóstico y Tratamiento), vis («quién maneja») |
| Altitud de Saquisilí (~2 900 m) | Nota de altitud solo si cambia una conducta (SpO₂ como causa de delirium) | e1, solo si el ejecutor encuentra fuente |

## Widget A · Enseñanza (widget-ensenanza v11, multi) — `ensenanza/`

Router: `Modo: multi · Entidades: e1=Delirium (principal), e2=Enfermedad de Alzheimer, e3=Neurocognitivo vascular, e4=Cuerpos de Lewy, e5=Frontotemporal · Amenaza: e1 · Override: no` (los nombres son los textos de botón; e3 = trastorno neurocognitivo vascular, e4 = enfermedad por cuerpos de Lewy, e5 = degeneración frontotemporal)

- Presentación común: **adulto mayor con cambio cognitivo o conductual («no actúa como él mismo») en el primer nivel**.
- Eje (declarado): tiempo de instalación y curso (horas-días y fluctuante → meses-años y progresivo) y, dentro de lo crónico, el dominio que cae primero (memoria → función ejecutiva escalonada → fluctuación con alucinaciones y parkinsonismo → conducta o lenguaje).
- Principal y amenaza = e1: el delirium es lo más frecuente en urgencias y lo que mata si no se busca la causa.
- Textos de botón (exactos): `Visión de conjunto` · `Delirium` · `Enfermedad de Alzheimer` · `Neurocognitivo vascular` · `Cuerpos de Lewy` · `Frontotemporal` · `Errores`.
- Subtipos: e1 hiperactivo · hipoactivo · mixto (y delirium sobre demencia); e2 TNC leve frente a mayor (DSM-5-TR), inicio temprano/tardío, variantes atípicas (atrofia cortical posterior, afasia logopénica); e3 multiinfarto cortical · subcortical de pequeño vaso · infarto estratégico; e4 demencia con cuerpos de Lewy · demencia en la enfermedad de Parkinson (regla del año; cubre «trastorno cognitivo menor por Parkinson» del sílabo); e5 variante conductual · afasia primaria progresiva semántica · no fluente.
- Vecinas fuera del grupo («No confundir con…»): depresión con quejas cognitivas, hidrocefalia normotensiva, hipotiroidismo y déficit de B12, encefalopatía de Wernicke, enfermedad de Creutzfeldt-Jakob, encefalitis, hematoma subdural crónico.
- Tema de acento: `salud-mental`.

Ejes de `vis` (literales, van a `nucleo.vis`):
1. `Eje 1 — Tiempo y curso: horas o días con fluctuación es delirium hasta demostrar lo contrario; meses o años de declive progresivo es un trastorno neurocognitivo.`
2. `Eje 2 — Atención y conciencia: la inatención y la conciencia alterada definen el delirium; en la demencia temprana se conservan, salvo en cuerpos de Lewy.`
3. `Eje 3 — Todo delirium tiene una causa orgánica que se busca y se corrige: metabólica, infecciosa, farmacológica o por deshidratación.`
4. `Eje 4 — El primer dominio que cae orienta la demencia: memoria, función ejecutiva escalonada, alucinaciones con parkinsonismo, o conducta y lenguaje.`

Contrato de `vis` por entidad (celda «¿Qué hallazgo la delata?» = `k` de la `.qv`; «¿Qué prueba la confirma?» = su paso `1.º` o `Confirma`):

| | Hallazgo que la delata (k) | 1.º dx / Confirma | Conducta inicial |
|---|---|---|---|
| e1 | Inicio agudo con inatención y conciencia que fluctúa | CAM o 4AT en la cabecera + glucemia capilar | Buscar y corregir la causa; medidas no farmacológicas; antipsicótico solo si hay riesgo |
| e2 | Olvido progresivo de lo reciente con fallo para aprender información nueva | MoCA o MMSE + funcionalidad + laboratorio de causas reversibles + neuroimagen | Inhibidor de colinesterasa, intervención no farmacológica y apoyo al cuidador |
| e3 | Declive escalonado, ejecutivo, con signos focales y factores vasculares | Neuroimagen (RM) con lesión vascular que explica el déficit | Control estricto de factores de riesgo vascular y prevención secundaria |
| e4 | Fluctuación cognitiva con alucinaciones visuales y parkinsonismo | Criterios de McKeith 2017 (biomarcador: SPECT de transportador de dopamina) | Inhibidor de colinesterasa; evita antipsicóticos típicos |
| e5 | Cambio temprano de conducta o lenguaje con memoria relativamente conservada | Criterios de Rascovsky o Gorno-Tempini + RM con atrofia frontotemporal | ISRS o trazodona para la conducta; no inhibidores de colinesterasa |

Conteos (manifiesto): `pg` vis 4, e1 5, e2–e5 3 · `fey` e1 2, e2–e5 1 · `nodos` e1 7, e2 6, e3 5, e4 5, e5 5 · `signos` e1 5, e2 4, e3 3, e4 4, e5 3 · `dc` vis, e1, e2, e3, e4, e5. Si un ejecutor necesita otro conteo, lo informa y el orquestador ajusta el manifiesto.

Simuladores: `dcVis` (diferencial desde hallazgos); `dcE1d` (CAM: rasgos → delirium sí/no y subtipo; chips del caso → causa metabólica a buscar primero y qué prueba hacer en el centro de salud, en «Diagnóstico»); `dcE1t` (conducta según causa y agitación; hidratación por peso con tope, antipsicótico solo si hay riesgo, con tope de dosis del adulto mayor, en «Tratamiento»); `dcE2` (estadio por MMSE/MoCA → fármaco con posología); `dcE3` (perfil vascular → prevención secundaria); `dcE4` (síntoma dominante → fármaco y lo que se evita); `dcE5` (síntoma conductual → fármaco; qué no usar).

### Reparto enseñanza (ejecutores `sonnet`)

| Ejecutor | Partes | Simuladores (en `_sim_<X>.js`) |
|---|---|---|
| A | `21_e1` | `dcE1d`, `dcE1t` |
| B | `05_vis` + `22_e2` | `dcVis`, `dcE2` |
| C | `23_e3` + `24_e4` | `dcE3`, `dcE4` |
| D | `25_e5` + `80_sin` (solo `hb ro` «Errores que no se pueden cometer»; el orquestador añade `.acc.refs`) | `dcE5` |
| E (al final) | `02_pan` | — |

El orquestador escribe `01_nav`, une `90_sim` y fija el manifiesto.

## Widget B · Apertura (skill apertura v1) — `apertura/`

Título `Apertura · Trastornos neurocognitivos` · salida `../Apertura_trastornos_neurocognitivos.html` · manifiesto `terminos 9`, `problemas {B:5,P:3,S:3,FR:4}`, `hipotesis 4`, `diagramas 5`.

### Términos (9: los 5 del estudiante + 4 que añade el orquestador por ser fundamentales en el caso)

| Pestaña · término | Prerrequisitos canónicos (tipo) | Remisiones | pid (card.vin) |
|---|---|---|---|
| t1 · Fatiga | Contracción muscular y aporte de ATP (C) · Comando motor central y percepción del esfuerzo (C) | — | B5, FR4 |
| t2 · «No actúa como él mismo» (coloquial → cambio agudo del estado mental respecto de su basal; `.mini.am` con la interpretación) | Dominios cognitivos (B) · Funcionalidad basal: ABVD y AIVD (B) | — | B1, S3 |
| t3 · Lúcido | Sistema activador reticular ascendente (B) · Nivel y contenido de la conciencia (C) · Red atencional (B) | dominios cognitivos (t2) | B1 |
| t4 · Somnoliento | Ciclo sueño-vigilia (C) | SARA (t3) | B1 |
| t5 · Estuporoso | Respuesta al estímulo nociceptivo (C) | SARA (t3) · nivel y contenido de la conciencia (t3) | B1 |
| t6 · Inquietud (añadido) | Circuitos frontosubcorticales y control de la actividad motora (B) | SARA (t3) | P1, P2 |
| t7 · Polidipsia · sed aumentada (añadido) | Osmorregulación: osmorreceptores, sed y ADH (C) · Agua corporal y sed en el envejecimiento (C) | — | B3, P3, FR3 |
| t8 · Nocturia (añadido; «No confundir» con polaquiuria, poliuria y oliguria) | Llenado y vaciado vesical (C) · Concentración de la orina y ritmo circadiano de la diuresis (C) | osmorregulación (t7) | B2, P3 |
| t9 · Estreñimiento (añadido) | Motilidad colónica y reflejo de la defecación (C) · Absorción de agua en el colon (C) | — | B4, FR4 |

Cada término: card `.card.vin` «Por qué importa en este caso» (≤70 palabras, chips `span.pid`), ejemplo de anclaje en el paciente (sin afirmar el diagnóstico) y 6 tarjetas (5 + 1 que conecta con el caso). Tope de prerrequisitos: 5.

### Problemas (ids fijos)

| id | Problema | Dato del caso |
|---|---|---|
| B1 | Alteración aguda y fluctuante de la conciencia y la conducta | «no actúa como él mismo» desde hace dos días; «lúcido un minuto y luego… somnoliento o estuporoso» |
| B2 | Polaquiuria y nocturia con volumen urinario disminuido | «aumento en la frecuencia de micción y nocturia… con disminución significativa del volumen» |
| B3 | Sed aumentada con ingesta de agua reducida (balance hídrico negativo probable) | «aumento de la sed en las últimas semanas»; «ha disminuido la ingesta de agua a pesar de la sed» |
| B4 | Estreñimiento de dos semanas con evacuaciones dolorosas | «una o dos veces por semana», «evacuaciones dolorosas» |
| B5 | Fatiga con menor actividad en los últimos meses | «ha reducido sus salidas en los últimos meses debido a la fatiga» |
| P1 | Inquietud el día previo al cambio | «un día antes… se le vio inquieto» |
| P2 | Deambulación sin rumbo durante horas | «caminando sin dirección en su barrio… por varias horas» |
| P3 | Restricción voluntaria del agua para no orinar de noche | «disminuido la ingesta de agua… por el aumento de la frecuencia urinaria en la noche» |
| S1 | Vive solo; el hijo lo visita ocasionalmente | «vive solo… un hijo que lo visita ocasionalmente» |
| S2 | Medicatura rural sin posibilidad de derivar | «Centro de Salud de Saquisilí… no tiene forma de derivar» |
| S3 | Historia que depende de un informante que no convive con él | el hijo relata; visitas ocasionales |
| FR1 | Exposición prolongada al calor | «clima caliente por varias horas»; «camina en un clima caluroso para sus compras» |
| FR2 | Infección viral reciente | «cuadro viral leve hace dos semanas, con fiebre y malestar general» |
| FR3 | Ingesta de agua reducida pese a la sed | ídem B3/P3 (como argumento) |
| FR4 | Síntomas subagudos (fatiga, sed, estreñimiento) que preceden al cuadro agudo | semanas a meses antes del cambio de conducta |

Datos que faltan (c0 y hx): edad; fármacos (diuréticos, litio, vitamina D, calcio, anticolinérgicos, sedantes); antecedentes (diabetes, cáncer, hiperparatiroidismo, deterioro cognitivo previo, alcohol); signos vitales con temperatura y SpO₂; estado de hidratación; examen neurológico y de focalidad; glucemia capilar; sodio, potasio, calcio corregido o iónico, albúmina, urea, creatinina, osmolalidad; EMO; ECG; diuresis medida; funcionalidad y cognición basales según el hijo.

### Jerarquía propuesta (`ol.rank`, todos los B, P, S una vez)

g1: B1 (delirium: urgencia médica con mortalidad), B3 (deshidratación con riesgo de hiperosmolaridad, lesión renal y golpe de calor). g2: B2 (marcador del trastorno metabólico causal), P2 (golpe de calor, caídas, extravío), S2 (todo se resuelve en el centro de salud), S1 (nadie vigila hidratación ni recurrencia). g3: B4, B5, P1, P3. g4: S3. Los FR no se jerarquizan.

### Hipótesis (`.card.hx`, por probabilidad)

| id | Hipótesis | Probabilidad | Explica | Qué la confirmaría |
|---|---|---|---|---|
| H1 | Delirium (síndrome confusional agudo) de causa médica | Alta | B1, P1, P2 | CAM o 4AT positivos; búsqueda de la causa |
| H2 | Hipercalcemia sintomática | Media | B1, B2, B3, B4, B5, FR4 | Calcio corregido o iónico elevado; QT corto en el ECG; PTH para la causa |
| H3 | Estado hiperosmolar hiperglucémico (diabetes no conocida) | Media | B1, B2, B3, B5, FR2 | Glucemia y osmolalidad efectiva elevadas sin cetoacidosis importante |
| H4 | Deshidratación hipertónica (hipernatremia) con agotamiento o golpe de calor | Media | B1, B3, P2, P3, FR1, FR3 | Sodio sérico elevado; temperatura central; urea/creatinina |

Diferencial (tabla fuera de las cards): hiponatremia, infección urinaria o sepsis, encefalitis viral, ictus, hipoglucemia, trastorno neurocognitivo mayor previo no reconocido (delirium sobre demencia), hipotiroidismo, intoxicación farmacológica.

### Diagramas (`figure.dg`, mínimo 5)

1. `pb` · mapa biopsicosocial: B, P, S y FR convergiendo en «Cambio agudo y fluctuante del estado mental».
2. `pb` · fisiopatología del problema principal: sustrato vulnerable + insulto metabólico → disfunción de la red atencional y del SARA → inatención y conciencia fluctuante.
3. `pb` · círculo vicioso del agua: diuresis aumentada → nocturia → restricción de agua → deshidratación → más concentración y más confusión.
4. `jq` · escalera de gravedad (g1 → g4).
5. `hx` · predisponentes + precipitantes → síndrome → hipótesis H1–H4.

### Reparto apertura (ejecutores `sonnet`)

| Ejecutor | Partes | Mazos |
|---|---|---|
| K | `p05_c0` + `p10_t1` `p20_t2` `p30_t3` | t1–t3 |
| L | `p40_t4` `p50_t5` `p60_t6` | t4–t6 |
| M | `p70_t7` `p80_t8` `p90_t9` | t7–t9 |
| N | `p91_pb` | pb (6–8) |
| O | `p92_jq` + `p93_hx` | jq (5–6), hx (6–8) |

El orquestador escribe `p01_nav`, `p95_tg`, `p96_js` y el manifiesto.

## Citas y verificación (ambos widgets)

- Los ejecutores citan con claves `[@clave]` del catálogo común `widgets/trastornos_neurocognitivos/_refs_catalogo.tsv`; si necesitan otra fuente, la añaden a `_refs_<X>.tsv` en su carpeta de widget (`clave<TAB>Vancouver`), con PMID/DOI solo si PubMed o la web los devolvieron.
- Datos que cambian conducta (dosis, umbrales, puntos de corte) se verifican al redactar con PubMed/Consensus/DailyMed/web; lo no confirmado no se escribe (cero marcas). Cada ejecutor anota en `_pend_<X>.tsv` (`dato<TAB>parte<TAB>fuente`) lo que confirmó y con qué.
- `haiku`: pasada de verificación de catálogo y `_refs_*` (que cada PMID/DOI exista y corresponda) y de una muestra de `_pend_*`.
- Integrador (orquestador): convierte `[@clave]` en `[n]`, arma `ol.vanc` (en `80_sin` y en `p95_tg`), ejecuta `kit/renumerar.py`, une mazos y simuladores, y borra los `_*`.

## Reglas de diseño para ejecutores (ambos widgets)

Las 10 reglas de `widgets/patologia_urinaria_baja/PLAN.md` § «Reglas de diseño para ejecutores» (clases solo del kit; tablas con thead/tbody en `div.tw`; sin recuadros anidados; tipo oración; párrafos ≤90 palabras; un `<b>` por párrafo; voz activa, español de Ecuador; sin emojis; coma decimal; conteos de la skill), más las de v11: `div.nucleo` tras las PG, `aside.perla[data-ex]` junto al tema, `li[data-paso]` en pasos, filas-pregunta en `vis`, columna «Mecanismo de acción» en tablas de fármacos, cero `[VERIFICAR EN FUENTE]`.

## Resultado (2026-11-09)

- Enseñanza: `Trastornos_neurocognitivos_widget_v11.html` (v11, multi), 82 referencias, validador OK (7 avisos de longitud aceptados: profundidad de examen, como en `depresion_bipolar_suicidio`). Apertura: `Apertura_trastornos_neurocognitivos.html`, 36 referencias, validador, auditoría y navegador en verde. Cero marcas en ambos.
- Verificación: catálogo y referencias de ejecutores comprobados por `haiku` en PubMed (78 artículos confirmados, 1 corregido —Cao 2020—, 1 eliminado —estudio poblacional de Lewy 2026 sin registro en PubMed—, con sus cifras).
- Datos eliminados por no poder leerse en la sesión (hosts bloqueados o figura en imagen): umbrales numéricos de glucemia y osmolalidad del estado hiperosmolar (ADA 2024, figura 2B), umbrales numéricos de Roma IV, punto de corte del Mini-Cog y del 4AT, dosis de quetiapina, risperidona, levodopa y melatonina en demencia, nota de altitud de Saquisilí, hidratación por kg en el simulador (se usan las tasas absolutas de ADA 2024). AHA/ASA 2021 y SIGN 157 no se citan (sin acceso al texto).
- Los archivos de trabajo `_refs_*`, `_pend_*`, `_sim_*`, `_recall_*` y los briefs se borraron tras integrar.
