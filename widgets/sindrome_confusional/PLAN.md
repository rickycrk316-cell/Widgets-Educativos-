# Síndrome confusional — plan del orquestador

Fuentes (prioridad): 1) **Caso de Doña Rosa** (`fuentes/casos/caso_dona_rosa_sindrome_confusional.md`); 2) **sílabo de la segunda rotación, Caso 6 — Síndrome confusional agudo y demencia** (`fuentes/syllabus_quirurgica2_segunda_rotacion.md`), con su bibliografía (Harrison, Farreras, Kane *Principios de geriatría clínica* 8e, Ebert *Psiquiatría* 4e, MSP 2010 adulto mayor); 3) guía vigente más específica (DSM-5-TR, Inouye *Lancet* 2014, AGS Beers 2023, STOPP/START v3, Comisión *Lancet* de demencia 2024, ADA Standards 2025 adultos mayores, ACIP/CDC esquema de adultos vigente, MSP Ecuador).

Skill: **apertura v1** (`fuentes/skill_apertura_v1.md`), un único widget `apertura/` → `Apertura_sindrome_confusional.html`.

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

Convención para trabajo en paralelo: las citas se escriben `[@clave]` y cada ejecutor deja `_refs_<ejecutor>.tsv` (`clave<TAB>referencia Vancouver`) y `_mazos_<ejecutor>.json` (`{"t1":[{"q":…,"a":…,"h":…}]}`) en `apertura/`. El integrador numera por primera aparición, escribe la lista y borra los archivos `_*`.
