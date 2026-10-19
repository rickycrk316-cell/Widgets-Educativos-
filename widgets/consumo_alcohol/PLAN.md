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
