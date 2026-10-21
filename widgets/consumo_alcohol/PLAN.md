# Plan · Consumo de alcohol (caso de emergencia)

Caso: varón que ingresa a emergencia en estado etílico tras una semana de consumo intenso de aguardiente (zhumir, trópico seco, puntas). Consumo desde los 17 años (cerveza de fin de semana) que progresó desde los 20 (entre semana, más volumen, mezcla de bebidas). Agresividad y maltrato físico y verbal a la pareja en el último año. Hace 6 meses intentó suspender y presentó temblores, mareos e irritabilidad. Deterioro laboral; tristeza, ideas de inutilidad y minusvalía.

## Widget · Definiciones (skill definiciones v5.1) — `definiciones/`

- Caso/semana: Consumo de alcohol, paso 1 del ABP.
- Términos (los dos primeros los pidió el estudiante; 3–6 los añadió el orquestador por ser claves del caso). 6 términos → régimen normal, tope 5 prerrequisitos (usar 1–2 por pestaña):

| Pestaña | Término | Prerrequisitos canónicos | Remisiones |
|---|---|---|---|
| t1 | Estado etílico (intoxicación alcohólica aguda) | Farmacocinética del etanol (tipo C: absorción, distribución en agua corporal, ADH → acetaldehído → ALDH → acetato, CYP2E1, cinética de orden cero); Neurotransmisión GABA-A y glutamato NMDA (tipo B, tabla) | — |
| t2 | Síndrome de abstinencia alcohólica | Neuroadaptación por consumo crónico (tipo C: regulación a la baja de GABA-A, al alza de NMDA, rebote noradrenérgico) | GABA/NMDA («Estado etílico») |
| t3 | Trastorno por consumo de alcohol (incluye tolerancia y dependencia) | Circuito de recompensa mesolímbico y control prefrontal (tipo B, tabla: ATV, núcleo accumbens, corteza prefrontal, amígdala) | neuroadaptación («Síndrome de abstinencia») |
| t4 | Aguardiente y bebida estándar (zhumir, trópico seco, puntas) | Grado alcohólico y cálculo de gramos de etanol (tipo C: % vol × volumen × 0,8 g/mL) | farmacocinética («Estado etílico») |
| t5 | Ideas de inutilidad y minusvalía (síntomas depresivos) | Sistemas monoaminérgicos y regulación del ánimo (tipo B, tabla: serotonina, noradrenalina, dopamina) | recompensa («Trastorno por consumo») |
| t6 | Violencia de pareja | (sin prerrequisito propio: se declara omisión) | corteza prefrontal y control inhibitorio («Trastorno por consumo»); GABA/desinhibición («Estado etílico») |

+ pestaña final **Repaso global**.

- Mecanismo mínimo (`ol.tl` de ≤3 nodos dentro de un `.acc` normal, colapsado, título «Mecanismo mínimo»): t1 y t2.
- Alcance: paso 1. Nada de tratamiento, dosis, CIWA-Ar como algoritmo, epidemiología ni S/E/VPP/VPN. El delirium tremens, la encefalopatía de Wernicke y la intoxicación por metanol se nombran solo en «No confundir con…» o correlatos. Ejemplos de anclaje usan al paciente del caso.
- Marcas: zhumir y trópico seco aparecen solo como las bebidas que refiere el caso; sin descripciones comerciales. Grados alcohólicos concretos de cada bebida → `[VERIFICAR EN FUENTE]`.
- t6 y t5: sin juicio moral; t5 nombra el riesgo suicida solo como «No confundir con» / correlato (ideación suicida es otro término), sin conducta.

## Referencias (Vancouver, numeración fija por primera aparición)

1. Brunton LL, Knollmann BC, editores. Goodman & Gilman's the pharmacological basis of therapeutics. 14th ed. New York: McGraw Hill; 2023.
2. World Health Organization. International classification of diseases for mortality and morbidity statistics, 11th revision (ICD-11). Geneva: World Health Organization; 2019.
3. American Psychiatric Association. Diagnostic and statistical manual of mental disorders. 5th ed, text revision (DSM-5-TR). Washington (DC): American Psychiatric Association Publishing; 2022.
4. Kandel ER, Koester JD, Mack SH, Siegelbaum SA, editores. Principles of neural science. 6th ed. New York: McGraw Hill; 2021.
5. Babor TF, Higgins-Biddle JC, Saunders JB, Monteiro MG. AUDIT: the alcohol use disorders identification test. Guidelines for use in primary care. 2nd ed. Geneva: World Health Organization; 2001.
6. Krug EG, Dahlberg LL, Mercy JA, Zwi AB, Lozano R, editores. World report on violence and health. Geneva: World Health Organization; 2002.

Uso: t1 cita [1] en prerrequisitos y [2][3] en la definición; t2–t3 reutilizan [1]–[3]; t3 introduce [4]; t4 introduce [5] (bebida estándar de 10 g de etanol de la OMS); t5 usa [4] y [3]; t6 introduce [6]. Nadie usa un número fuera de este orden.

## Diseño

Idéntico al widget de definiciones de `patologia_urinaria_baja/PLAN.md` (sección «Widget B» y «Reglas de diseño para ejecutores»): mismo vocabulario de clases, mismos glifos (sin ✅ ⚠️ ❌), mismas reglas 1–10. Archivo: `Definiciones_consumo_alcohol.html`.

## Ampliación 1 · temas del sílabo (monitoreo miércoles, cierre viernes)

Temas pedidos por el docente y dónde se resuelven:

| Tema del sílabo | Dónde |
|---|---|
| Conceptos: alcoholismo, abuso, dependencia, tolerancia, inversión de la tolerancia, craving, trastorno mental | Definiciones t3 (abuso, dependencia, tolerancia) + t7–t10 nuevas; resumen en enseñanza `def` |
| Morbilidad y mortalidad global | enseñanza `def` (Epidemiología) |
| Teorías causales (genética, socioculturales, personalidad, otras) y factores de riesgo | enseñanza `fis` |
| Mecanismo de adicción, dependencia física y psíquica, abstinencia, tolerancia, inversión | enseñanza `fis` (timeline) |
| Cuadro clínico: intoxicación aguda y crónica, abstinencia alcohólica | enseñanza `cli` |
| Clasificación de drogas e intoxicación/abstinencia de otras drogas | enseñanza adicional `dro` |
| Laboratorio: metabolitos en sangre y orina | enseñanza `dx` |
| Tratamiento en el primer nivel: objetivos, metas, farmacológico y no farmacológico | enseñanza `tx` |
| Complicaciones sanitarias y psicosociales, patología dual, criterios de referencia | enseñanza `seg` |

### Definiciones · pestañas nuevas (10 términos, régimen normal)

| Pestaña | Término | Prerrequisito canónico | Remisiones |
|---|---|---|---|
| t7 | Alcoholismo | — (término histórico; se declara omisión) | recompensa («Trastorno por consumo»), neuroadaptación («Síndrome de abstinencia») |
| t8 | Craving (deseo intenso de consumir) | Condicionamiento y memoria asociativa de la recompensa (tipo C) [4] | recompensa y amígdala («Trastorno por consumo») |
| t9 | Inversión de la tolerancia | Sensibilización y reserva funcional hepática (tipo C) [1] | farmacocinética («Estado etílico»), neuroadaptación («Síndrome de abstinencia») |
| t10 | Trastorno mental | — (concepto; se declara omisión) | monoaminas («Ideas de inutilidad») |

Mazo: 5–6 tarjetas por término. Referencias: solo las 6 ya fijadas; alcoholismo cita [2] y [3] (la CIE-11 y el DSM-5-TR no usan «alcoholismo» como diagnóstico); trastorno mental cita [3] (definición de trastorno mental del DSM-5-TR). Repaso global pasa a «diez términos».

### Enseñanza · `ensenanza/` (skill widget-ensenanza v10, modo mono)

- Línea del router: `Modo: mono · Entidades: e1=Trastorno por consumo de alcohol y otras drogas · Amenaza: — · Override: no`. Las intoxicaciones y abstinencias son formas clínicas del mismo proceso (en `cli` y `dro`), no entidades aparte.
- Pestañas: `pan def fis cli dro dx tx seg`; adicional `dro` = «Otras drogas» (parte `12x_dro.html`).
- Caso de anclaje: el paciente del caso de emergencia (en ejemplos y simuladores).
- Guía rectora: OMS mhGAP 2.0 (2016) para el primer nivel; DSM-5-TR (2022) para criterios; ASAM 2020 para abstinencia. Vigencia: mhGAP tiene actualización de recomendaciones 2023 no leída → `.mini` «Vigencia no verificada».
- Citas: los ejecutores citan con claves `[@clave]` del banco de referencias de `ensenanza/REFS.md`; el orquestador numera por primera aparición. No usar fuentes fuera del banco.

### Contraste con el sílabo (segunda rotación, Caso 4 · Toxicodependencias)

El sílabo añade a la lista del docente (trabajo autónomo): historia clínica psiquiátrica y examen de funciones psíquicas → `dx`; normalidad y enfermedad mental → `def` y definiciones t10; neurotransmisión dopamina-GABA-sistema límbico → `fis`; farmacología de benzodiacepinas → `tx`. El docente añade al sílabo: factores de riesgo, personalidad y otras teorías, craving, inversión de la tolerancia (también en el sílabo), patología dual y criterios de referencia. Bibliografía del sílabo (Harrison 19e, Farreras 17e, Ebert 2025) no consultada: se declara en `Alcance`.
