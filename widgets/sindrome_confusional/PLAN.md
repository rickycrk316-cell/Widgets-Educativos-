# Síndrome confusional — plan del orquestador

Fuentes (prioridad): 1) **Caso de Doña Rosa** (`fuentes/casos/caso_dona_rosa_sindrome_confusional.md`); 2) **sílabo de la segunda rotación, Caso 6 — Síndrome confusional agudo y demencia** (`fuentes/syllabus_quirurgica2_segunda_rotacion.md`), con su bibliografía (Harrison, Farreras, Kane *Principios de geriatría clínica* 8e, Ebert *Psiquiatría* 4e, MSP 2010 adulto mayor); 3) guía vigente más específica (DSM-5-TR, Inouye *Lancet* 2014, AGS Beers 2023, STOPP/START v3, Comisión *Lancet* de demencia 2024, ADA Standards 2025 adultos mayores, ACIP/CDC esquema de adultos vigente, MSP Ecuador).

Skill: **apertura v1** (`.claude/skills/apertura/SKILL.md`), un único widget `apertura/` → `Apertura_sindrome_confusional.html`.

## Router

`Modo: apertura · Términos: 9 · Pestañas: c0, t1–t9, pb, jq, hx, tg · Problema central: síndrome confusional agudo sobre deterioro cognitivo crónico`

| id | Pestaña | Término / contenido |
|---|---|---|
| c0 | Caso | Caso transcrito y marcado B/P/S/FR, incongruencias, datos faltantes |
| t1 | Vacunas | Vacunas del adulto ≥80 años: recomendado frente a lo que tiene Doña Rosa |
| t2 | Losartán | ARA II |
| t3 | Diltiazem | Calcioantagonista no dihidropiridínico |
| t4 | Furosemida | Diurético de asa |
| t5 | Paracetamol | Analgésico-antipirético |
| t6 | Pregabalina | Gabapentinoide |
| t7 | Glucosamina | Suplemento «condroprotector» (Artrin) |
| t8 | Insulina + metformina | Insulina NPH (escrita «HPH» en el caso) + biguanida |
| t9 | Hipotiroidismo subclínico | TSH alta con T4 libre normal |
| pb | Problemas | B/P/S/FR con fisiopatología |
| jq | Jerarquización | Orden por morbimortalidad |
| hx | Hipótesis | Hipótesis diagnósticas y diferencial |
| tg | Repaso global | Mazo mixto + Referencias |

Decisiones: el caso escribe «Tramal» (tramadol), que no está en la lista de términos; se trata **dentro de `pb`** (B3 polifarmacia) y en remisiones, no como pestaña. «HPH» se interpreta como insulina NPH (nota `.mini.am`). «Herpes zorter» = herpes zóster.

## Esqueleto clínico (el ejecutor desarrolla; no cambia el orden sin avisar)

### Problemas

**Biológicos**
- **B1 · Alteración aguda de la conducta y la cognición de 1–2 semanas** (irritabilidad, inversión del ciclo sueño-vigilia, ideas de robo, ve a su difunto esposo) → síndrome confusional agudo (delirium), probablemente hiperactivo o mixto. Fisiopatología: hipótesis neurotransmisora (déficit colinérgico / exceso dopaminérgico), neuroinflamación, estrés oxidativo, red de atención; umbral bajo por reserva cognitiva reducida.
- **B2 · Deterioro cognitivo crónico progresivo de ~2 años con pérdida de actividades instrumentales** (olvida nombres, quema la comida, plancha encendida, no ordena casa, comida ni ropa) → trastorno neurocognitivo mayor probable. Fisiopatología: neurodegeneración (amiloide/tau) y daño vascular (DM2, HTA, IC).
- **B3 · Polifarmacia (≥9 fármacos) con medicamentos potencialmente inapropiados** para el adulto mayor y con efecto sobre el SNC: tramadol + pregabalina (sedación, deliriogénicos, tramadol serotoninérgico e hiponatremia), insulina NPH nocturna (hipoglucemia), furosemida (deshidratación, hiponatremia, hipopotasemia), losartán + furosemida (lesión renal, hiperpotasemia, que a su vez acumula pregabalina y metformina), diltiazem en IC (inotropo negativo, bradicardia), metformina (déficit de B12 a largo plazo). Criterios Beers 2023 / STOPP.
- **B4 · Riesgo de hipoglucemia y disglucemia** en DM2 insulinorrequiriente de 83 años (NPH nocturna + metformina): neuroglucopenia nocturna puede imitar o precipitar delirium. Glucemia no reportada.
- **B5 · Insuficiencia cardiaca hipertensiva NYHA II**: bajo gasto / hipoperfusión cerebral, congestión, nicturia; diltiazem y FEVI desconocida.
- **B6 · Infección de vías urinarias recurrente** (última hace 4 meses, malla de cistopexia, nicturia 2–3) → foco precipitante frecuente de delirium en la mujer mayor; puede no tener fiebre ni disuria.
- **B7 · Dolor crónico osteoarticular** (escoliosis, anterolistesis L5–S1 grado II, lumbociatalgia, gonartrosis): dolor no controlado y sus analgésicos precipitan delirium; limitan movilidad.
- **B8 · Riesgo de caídas y fractura** (osteopenia, pregabalina/tramadol, nicturia, diurético, deterioro cognitivo, lumbociatalgia).
- **B9 · Hipotiroidismo subclínico en observación**: causa potencialmente contribuyente y reversible de deterioro cognitivo a reevaluar.
- **B10 · Esquema de vacunación incompleto para la edad** (sin dT/Tdap, sin zóster recombinante, neumococo una dosis de tipo no especificado, VSR no consignado).
- **B11 · Exposición a humo de leña**: riesgo de EPOC/hipoxemia crónica (dato faltante: síntomas respiratorios, saturación).

**Psicológicos**
- **P1 · Síntomas psicóticos**: ideas delirantes de perjuicio (robo) y alucinaciones visuales (difunto marido).
- **P2 · Irritabilidad y labilidad** («carácter dañado»), con impacto en la relación con el hijo.
- **P3 · Alteración del ciclo sueño-vigilia** (somnolencia diurna, vigilia nocturna).
- **P4 · Duelo / viudez y posible ánimo depresivo** no evaluado (la depresión puede simular deterioro cognitivo).

**Sociales**
- **S1 · Cuidador único (hijo) con riesgo de sobrecarga** y conflicto por las acusaciones de robo.
- **S2 · Inseguridad en el hogar** (plancha encendida, comida quemada: riesgo de quemadura e incendio) y dependencia en actividades instrumentales.
- **S3 · Escolaridad primaria** (menor reserva cognitiva; condiciona la interpretación de las pruebas cognitivas).
- **S4 · Viuda, adulta mayor de 83 años**: fragilidad de la red; la religiosidad (católica) como recurso de apoyo.

**Factores de riesgo (para las hipótesis)**
- **FR1 · Predisponentes de delirium**: edad ≥80, deterioro cognitivo previo, multimorbilidad, dependencia funcional, baja escolaridad.
- **FR2 · Precipitantes de delirium**: fármacos psicoactivos (tramadol, pregabalina), infección (ITU recurrente), disglucemia, trastornos hidroelectrolíticos por diurético, dolor, privación de sueño, nicturia.
- **FR3 · Factores de riesgo de demencia (modificables y no modificables)**: edad, sexo femenino, baja escolaridad, DM2, HTA, IC, contaminación del aire intradomiciliaria (humo de leña), aislamiento tras la viudez.
- **FR4 · Antecedentes familiares cardiometabólicos**: hijo con DM, hermanas con HTA (carga vascular familiar).

### Jerarquización propuesta (de mayor a menor riesgo)

g1 B1 → g1 B4 → g1 B3 → g2 B6 → g2 P1 → g2 B8 → g2 S2 → g2 B5 → g3 B2 → g3 P3 → g3 S1 → g3 B7 → g3 P2 → g3 P4 → g4 B9 → g4 B10 → g4 B11 → g4 S3 → g4 S4.
Lógica: el delirium es una urgencia con mortalidad alta y siempre tiene causa; las causas tiempo-dependientes y reversibles (hipoglucemia, toxicidad farmacológica, infección) van arriba; luego el riesgo de daño inmediato (caídas, accidentes domésticos, psicosis); después lo crónico.

### Hipótesis (orden de probabilidad)

- **H1 · Síndrome confusional agudo (delirium) multifactorial**, hiperactivo/mixto — explica B1, P1, P2, P3. Precipitantes candidatos: farmacológico (tramadol + pregabalina), metabólico (hipoglucemia por NPH, hiponatremia por furosemida/tramadol), infeccioso (ITU). Criterios DSM-5-TR / CAM.
- **H2 · Trastorno neurocognitivo mayor (demencia) de base**, probable enfermedad de Alzheimer o mixta (Alzheimer + vascular) — explica B2, S2. A favor: 2 años, memoria episódica, pérdida de AIVD, carga vascular.
- **H3 · Delirium inducido por medicamentos / prescripción potencialmente inapropiada** (sub-hipótesis de H1 con identidad propia por ser reversible) — explica B3, B4.
- **H4 · ITU como foco precipitante** — B6.
- **Diferencial**: demencia con cuerpos de Lewy (alucinaciones visuales bien formadas, fluctuación; pero las alucinaciones son recientes), depresión con quejas cognitivas, hipotiroidismo, déficit de B12 (metformina), hematoma subdural (riesgo de caídas), psicosis de inicio tardío, hipoxemia (humo de leña / IC).

Necesidades de aprendizaje (Caso 6 del sílabo): definición, factores predisponentes y precipitantes, fisiopatología, clasificación y diagnóstico del delirium (CAM); demencias (Alzheimer, vascular, Lewy, Parkinson, frontotemporal); envejecimiento cerebral; evaluación cognitiva del adulto mayor (MMSE/MoCA, actividades instrumentales de Lawton).

## Diagramas mínimos (≥5)

1. `pb`: mapa biopsicosocial de Doña Rosa (cuatro ejes → síndrome confusional sobre deterioro crónico).
2. `pb`: fisiopatología del delirium (insulto → neuroinflamación / desequilibrio ACh-DA → falla de red de atención → signos).
3. `pb`: cascada de la polifarmacia (furosemida + losartán → función renal ↓ → acumulación de pregabalina/metformina; tramadol + furosemida → hiponatremia; NPH → hipoglucemia nocturna → confusión).
4. `jq`: escalera de gravedad / agrupación de problemas en síndromes.
5. `hx`: modelo multifactorial predisponentes × precipitantes (Inouye) → H1 sobre H2.

## Reparto de ejecutores

| Ejecutor | Modelo | Entrega |
|---|---|---|
| Kit | sonnet | `kit/apertura_head.html`, tipo `apertura` en `construir.py`, `kit/validar_apertura.py`, ajuste de `probar_definiciones.js` |
| Términos A | sonnet | `p10_t1`…`p50_t5` (vacunas, losartán, diltiazem, furosemida, paracetamol) |
| Términos B | sonnet | `p60_t6`…`p90_t9` (pregabalina, glucosamina, insulina + metformina, hipotiroidismo subclínico) |
| Razonamiento | sonnet | `p05_c0`, `p91_pb`, `p92_jq`, `p93_hx` |
| Integrador | sonnet | `p01_nav`, `p95_tg`, `p96_js`, numeración Vancouver, construir en verde |
| Pruebas | haiku | navegador (iPad, oscuro, móvil), auditoría, informe de fallas |

Convención para trabajo en paralelo: las citas se escriben `[@clave]` y cada ejecutor deja `_refs_<ejecutor>.tsv` (`clave<TAB>referencia Vancouver`) y `_recall_<ejecutor>.json` (`{"t1":[{"q":…,"a":…,"h":…}]}`) en `apertura/`. El integrador numera por primera aparición, escribe la lista y borra los archivos `_*`.

---

# Widget de enseñanza · Causas metabólicas y por calor del síndrome confusional (caso de Saquisilí) — `causas_metabolicas/`

Caso: `fuentes/casos/caso_saquisili_trastornos_neurocognitivos.md` (medicatura rural en el Centro de Salud de Saquisilí, **sin posibilidad de derivar**; varón que vive solo; «no actúa como él mismo» desde hace dos días, lúcido un minuto y somnoliento o estuporoso al siguiente; inquieto el día previo; horas caminando al calor; cuadro viral hace dos semanas; polaquiuria y nocturia con volumen disminuido; estreñimiento de dos semanas; sed aumentada con ingesta de agua reducida; fatiga de meses).

Sílabo: 2.ª rotación, **Caso 6** (síndrome confusional agudo: factores precipitantes, diagnóstico diferencial, tratamiento, prevención), con **Caso 1** (azotemia prerrenal) y **Caso 3** (delirio como síndrome geriátrico). La etiqueta `puce` vale para contenido nombrado en cualquiera de esos tres casos de la 2.ª rotación (declarado en `vis`, `hb am` «Alcance»). Bibliografía: ediciones vigentes del protocolo § 4 (el sílabo cita Harrison 19.ª y Farreras 17.ª: discrepancia ya declarada en el widget hermano; aquí se repite solo como `hb am` «Precisión sobre el sílabo» en `vis`).

## Por qué un widget nuevo y por qué así

- Ya existe `widgets/trastornos_neurocognitivos/Trastornos_neurocognitivos_widget_v11.html` (multi: delirium, Alzheimer, vascular, Lewy, frontotemporal) con el mismo caso. Su eje es **delirium frente a demencia**; el delirium ocupa una sola pestaña y las causas del caso caben ahí en una tabla de etiología y unas pocas filas de fármacos.
- Lo que falta para **manejar a este paciente en un primer nivel sin derivación** es lo que el sílabo llama «factores precipitantes, diagnóstico diferencial, tratamiento y prevención» del síndrome confusional: cada causa metabólica o ambiental del caso tiene **mecanismo propio y manejo propio** (regla de entidad de la skill), y se discriminan ante **una misma presentación**. Eso es un multi, no un mono: un mono de «delirium» repetiría la pestaña e1 del widget hermano.
- Reconocer el delirium (CAM, 4AT, subtipos, fluctuación), el estudio mínimo común, el manejo común del delirium mientras se corrige la causa (no farmacológico, antipsicótico solo con riesgo, qué no dar) y las banderas de gravedad son **comunes al grupo**: van una vez en `vis` («Común al grupo») y remiten al widget hermano para la profundidad. La prevención común (plan de hidratación del adulto mayor que vive solo, calor, el hijo como vigía, revisión de fármacos) va en «Seguimiento» de e1, y las demás entidades remiten con `span.rem`.
- Se excluyen como entidades: la **infección** (el cuadro viral ya se resolvió; entra como precipitante del estado hiperosmolar y en la búsqueda sistemática de `vis`, y está en el widget hermano) y los **fármacos** (no hay lista de fármacos en el caso; dato faltante en `vis`). La **lesión renal aguda** entra como «Azotemia prerrenal» (Caso 1 del sílabo) porque la oliguria es pista directa del caso y su manejo (volumen, nefrotóxicos, potasio, qué hacer sin diálisis) es propio.

## Router

`Modo: multi · Entidades: e1=Hipernatremia (principal), e2=Azotemia prerrenal, e3=Hipercalcemia, e4=Estado hiperosmolar, e5=Golpe de calor · Amenaza: e5 · Override: no`

- Presentación común: **adulto mayor que vive solo, confuso y fluctuante tras días de calor, con sed, cambios en la diuresis y poca ingesta de agua, en un centro de salud sin derivación**.
- Eje (declarado): de lo más frecuente y lento a lo que mata en horas: hipernatremia → azotemia prerrenal → hipercalcemia → estado hiperosmolar → golpe de calor.
- Principal e1 = deshidratación hipernatrémica: la ESPEN considera a todo adulto mayor en riesgo de deshidratación por baja ingesta [Volkert 2022], y es el denominador de las otras cuatro (todas la producen o la agravan).
- Amenaza e5 = golpe de calor: si no se reconoce, mata o deja secuela neurológica en horas y su tratamiento (enfriar) no espera ningún examen; por eso abre el `hb ro` de `vis` y lleva pasos `Alarma` y `Evita`.
- Textos de botón (exactos): `Panorama` · `Visión de conjunto` · `Hipernatremia` · `Azotemia prerrenal` · `Hipercalcemia` · `Estado hiperosmolar` · `Golpe de calor` · `Errores`.
- Título: «Síndrome confusional: causas metabólicas y calor» · salida `../Sindrome_confusional_causas_widget_v11.html` · `tema` `salud-mental` (mismo acento que el widget hermano del Caso 6).
- Alcance declarado en `vis`: se asume que el centro de salud tiene glucómetro, tira reactiva de orina, termómetro (rectal para temperatura central), pulsioxímetro, ECG, soluciones IV y laboratorio básico (electrolitos, glucosa, urea, creatinina, calcio, albúmina); cuando un examen no exista, la conducta se guía por lo que sí hay, y se dice. No se afirma la dotación real del centro de Saquisilí.

## Ejes de `vis` (literales, van a `nucleo.vis`)

1. `Eje 1 — Temperatura central: muy alta con encefalopatía tras exposición al calor es golpe de calor; se enfría antes de cualquier otro estudio.`
2. `Eje 2 — Glucemia capilar: muy alta con hiperosmolalidad y sin cetosis importante es estado hiperosmolar; normal lo descarta en un minuto.`
3. `Eje 3 — Sodio y diuresis: sodio alto es déficit de agua libre; diuresis escasa con urea desproporcionada a la creatinina es azotemia prerrenal.`
4. `Eje 4 — Semanas de sed, poliuria, estreñimiento y fatiga sin hiperglucemia apuntan a hipercalcemia: calcio corregido y QT corto.`
5. `Eje 5 — Las causas no se excluyen: la hiperglucemia o el calcio alto producen poliuria, hipernatremia y azotemia prerrenal; se buscan todas.`

## Contrato de `vis` por entidad (filas 5, 7, 8 y 9; ≤12 palabras por celda)

| | 5 · Hallazgo que la delata (= celda `k` de su `.qv`) | 7 · Prueba que la confirma (= su paso `1.º` o `Confirma`) | 8 · Primera conducta y quién maneja | 9 · Si no la reconoces |
|---|---|---|---|---|
| e1 | Somnolencia o confusión con sed y poca ingesta de agua | Sodio sérico mayor de 145 mEq/L | Agua libre calculada; bajar el sodio despacio; médico rural | Coma y hemorragia cerebral por retracción del encéfalo |
| e2 | Diuresis escasa con signos de hipovolemia | Creatinina en ascenso (KDIGO) que mejora con volumen | Volumen, suspender nefrotóxicos, diuresis horaria; médico rural | Necrosis tubular, hiperpotasemia y uremia sin diálisis disponible |
| e3 | Semanas de estreñimiento, poliuria, sed y fatiga | Calcio corregido o iónico alto; luego PTH | Solución salina; calcitonina y bisfosfonato si es grave | Arritmia, coma y lesión renal; cáncer oculto sin diagnosticar |
| e4 | Glucemia capilar muy alta sin respiración de Kussmaul | Glucemia y osmolalidad efectiva altas con cetonas escasas | Solución salina primero; potasio antes de la insulina | Coma, trombosis y muerte |
| e5 | Temperatura central muy alta con encefalopatía tras calor | Temperatura rectal de 40 °C o más con disfunción neurológica | Enfriar de inmediato; luego volumen y vigilancia | Falla multiorgánica, coagulación intravascular y muerte en horas |

Las cifras de estas celdas llevan su `[@clave]` en el widget; si un ejecutor no confirma una cifra, la reescribe sin ella y avisa al integrador para alinear `vis`.

## Conteos (manifiesto)

`pg` vis 4, e1 5, e2–e5 3 · `fey` e1 2, e2–e5 1 · `nodos` e1 6, e2 5, e3 6, e4 5, e5 5 · `signos` e1 4, e2 3, e3 4, e4 3, e5 4 · `dc` vis, e1 (dos: `dcE1d` en Diagnóstico y `dcE1t` en Tratamiento), e2, e3, e4, e5. Si un ejecutor necesita otro conteo, lo informa y el integrador ajusta el manifiesto.

## Reparto

| Ejecutor | Modelo | Partes | Simuladores (en `_sim_<X>.js`) |
|---|---|---|---|
| E1 | sonnet | `21_e1` (Hipernatremia, principal, profundidad mono; incluye la prevención común en «Seguimiento») | `dcE1d`, `dcE1t` |
| E2 | sonnet | `22_e2` (Azotemia prerrenal) + `23_e3` (Hipercalcemia) | `dcE2`, `dcE3` |
| E3 | sonnet | `24_e4` (Estado hiperosmolar) + `25_e5` (Golpe de calor, amenaza) | `dcE4`, `dcE5` |
| E4 | sonnet | `05_vis` (incluye «Común al grupo»: reconocer el delirium, estudio mínimo, manejo común del delirium con tabla corta de fármacos comunes) + `80_sin` (solo `hb ro`) | `dcVis` |
| H1 | haiku | control mecánico de partes y comprobación de PMID/DOI/Setid de `_refs_*` | — |
| INT | integrador | `02_pan`, `90_sim` (une `_sim_*.js`), coherencia, conversión de claves, construir, renumerar, navegador, README, cierre del manifiesto | — |

El decisor escribió `01_nav`, el manifiesto provisional, `_refs_catalogo.tsv` (48 referencias comprobadas el 2026-11-13: 34 por PubMed, 5 fichas DailyMed por su API, NICE CG103 y GPC MSP de diabetes 2017 leídas en la web, 7 libros de la tabla del protocolo § 4) y `_sim_00_ayudas.js`. No se cita MSP «Normas y protocolos del adulto mayor» 2010: su único PDF localizado (iess.gob.ec) está bloqueado en la sesión y no se leyó.

## Citas y verificación

- Las partes citan con `[@clave]` (una clave por corchete, precedida de espacio). Claves del catálogo común `causas_metabolicas/_refs_catalogo.tsv`; fuentes nuevas en `_refs_<X>.tsv` del ejecutor, solo con PMID/DOI/Setid devueltos por la herramienta.
- Cada ejecutor verifica al redactar los datos que cambian conducta y anota en `_pend_<X>.tsv` (`dato<TAB>parte<TAB>fuente<TAB>resultado`) lo confirmado, corregido o eliminado. Lo no confirmado no se escribe (cero marcas).
- La conversión a `[n]` se hace una sola vez, al final, con `claves_a_numeros.py` (scratchpad del decisor, copia en el encargo del integrador) y luego `kit/renumerar.py`.

## Relación con el widget hermano

Este widget no repite el contraste con las demencias ni la profundidad del delirium (CAM, subtipos, fisiopatología neurotransmisora, pronóstico): los resume en «Común al grupo» y remite a `Trastornos_neurocognitivos_widget_v11.html`. Si un ejecutor encuentra un dato erróneo en el widget hermano, lo corrige aquí con `hb vi` (error de un widget previo) y lo informa al integrador.
