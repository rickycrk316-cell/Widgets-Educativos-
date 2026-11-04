# Trastornos del estado de ánimo — plan del orquestador

Caso: `fuentes/casos/caso_crisis_angustia_trastornos_animo.md` (consulta externa de primer nivel, **sin posibilidad de derivar**; tercer episodio en un año de palpitaciones, opresión precordial y miedo a perder el control mientras conduce; antes «preinfarto por estrés» tratado con Stresstabs y Xanax por semanas; hoy además sudoración y náuseas).

Sílabo: 2.ª rotación, **Caso 7 — Trastornos del estado de ánimo** (definición y clasificación, fisiopatología, clínica, evaluación diagnóstica, tratamiento, riesgo suicida y su manejo inicial; trabajo autónomo: historia clínica psiquiátrica). El cuadro de presentación pertenece además al **Caso 5 — TAG y ataque de pánico** (trabajo autónomo: serotonina, acetilcolina, GABA, MAO; benzodiacepinas e ISRS). Ambos se cubren.

Bibliografía: la del sílabo de la 2.ª rotación con ediciones vigentes del protocolo § 4 (el sílabo cita Harrison 19.ª y Farreras 17.ª: **discrepancia**; se usan Harrison 22.ª 2025 y Farreras 20.ª 2024) + Ebert 4.ª 2025 (complementaria del sílabo) + DSM-5-TR 2022 + guías: NICE CG113 (ansiedad/pánico), NICE NG222 (depresión), WFSBP 2023, ESC 2023 SCA, AHA/ACC 2021 dolor torácico, OMS mhGAP 2.0 (primer nivel sin especialista).

## Citas (ambos widgets)

Las partes citan con claves `[@CLAVE]` de `refs.json` (nunca números). El orquestador numera al final con `python3 widgets/trastornos_animo/citar.py <carpeta>`, que también sustituye `<!--REFS-->` (dentro de `ol.vanc`) por la lista Vancouver. Clave nueva: añádela a `refs.json` solo con datos que hayas leído; si no, `[VERIFICAR EN FUENTE]` (enseñanza) o badge ámbar (definiciones) y anótala en `pendientes`.

## Pistas del caso (sin resolver el caso)

| Pista | Por qué importa | Dónde |
|---|---|---|
| Inicio brusco al conducir, pico en minutos, miedo a perder el control, tercer episodio | Patrón de crisis de angustia recurrente; conducir = situación de la que es difícil escapar (agorafobia) | vis, e1 |
| Opresión precordial + sudoración + náuseas | Igual de compatibles con SCA: obligan a ECG antes de etiquetar ansiedad | vis (hb ro), e5 |
| «Preinfarto por estrés» sin datos objetivos | Término popular; error de rotulación que perpetúa la crisis y la consulta repetida | e1, e5, def t6 |
| Xanax por semanas | Riesgo de tolerancia, rebote interdosis y abstinencia; BZD no es tratamiento de mantenimiento del pánico | e4, e1 tx |
| Stresstabs | Polivitamínico sin efecto ansiolítico demostrado; tratamiento sin diagnóstico | def t8, e1 (Evita) |
| Sin derivación | Manejo integral en primer nivel (mhGAP) y estabilización del SCA mientras se activa ECU 911 | e1 tx, e3 riesgo suicida, e5 |

## Widget A · Enseñanza (widget-ensenanza v10.1, multi) — `ensenanza/`

Router: `Modo: multi · Entidades: e1=Trastorno de pánico (principal), e2=Ansiedad generalizada, e3=Depresión mayor, e4=Consumo de benzodiacepinas, e5=Síndrome coronario agudo · Amenaza: e5 · Override: no`

- Presentación común: **crisis de angustia con síntomas somáticos (opresión torácica, palpitaciones, sudoración) en consulta externa de primer nivel**.
- Eje (declarado): origen de la crisis, de ansiedad primaria → afectivo → inducido por sustancia → orgánico amenazante (e1 → e5).
- Textos de botón (exactos): `Trastorno de pánico` · `Ansiedad generalizada` · `Depresión mayor` · `Consumo de benzodiacepinas` · `Síndrome coronario agudo`.
- Subtipos: e1 con/sin agorafobia y crisis esperadas/inesperadas; e2 —; e3 gravedad (leve/moderada/grave), con características ansiosas, distimia como vecina; e4 intoxicación · tolerancia/dependencia · abstinencia · trastorno por consumo (fases de una entidad); e5 SCACEST · SCASEST (IAMSEST/angina inestable).
- Vecinas fuera del grupo («No confundir con…»): hipertiroidismo, feocromocitoma, arritmias (TSV), hipoglucemia, intoxicación por estimulantes, trastorno bipolar, TEP, disección aórtica.

Ejes de `vis` (literales, van a `nucleo.vis`):
1. `Eje 1 — Curso temporal: crisis con pico en minutos, preocupación de meses, ánimo bajo de semanas, síntomas entre dosis o dolor isquémico persistente.`
2. `Eje 2 — ECG de 12 derivaciones antes de etiquetar ansiedad: el pánico se diagnostica tras excluir la isquemia.`
3. `Eje 3 — En toda ansiedad recurrente se criba el ánimo y se pregunta directamente por ideación suicida.`

Contrato de `vis` por entidad (celdas `Signo que la delata` = `k` de la `.qv` de esa entidad; `Prueba que decide` = su paso `1.º` o `Confirma`):

| | Signo que la delata (k) | 1.º dx | Conducta inicial |
|---|---|---|---|
| e1 | Crisis inesperadas recurrentes con pico en minutos y miedo persistente a nuevas crisis | ECG de 12 derivaciones normal + criterios DSM-5-TR en la entrevista | Psicoeducación, ISRS y TCC; BZD no como mantenimiento |
| e2 | Preocupación excesiva, difícil de controlar, la mayoría de días ≥6 meses | GAD-7 + criterios DSM-5-TR | ISRS/IRSN y TCC |
| e3 | Ánimo deprimido o anhedonia casi todos los días ≥2 semanas | PHQ-9 + pregunta directa por ideación suicida | Evaluar riesgo suicida; ISRS y psicoterapia |
| e4 | Ansiedad de rebote entre dosis y escalada de alprazolam | Anamnesis de consumo con criterios DSM-5-TR | Reducción gradual pactada; nunca suspensión brusca |
| e5 | Opresión retroesternal >20 min con diaforesis, sobre todo con factores de riesgo | ECG de 12 derivaciones en ≤10 min + troponina | AAS masticada, ECU 911 y monitorización |

Conteos (manifiesto): `pg` vis 4, e1 4, e2–e5 3 · `fey` e1 2, e2–e5 1 · `nodos` e1 6, e2 5, e3 5, e4 5, e5 5 · `signos` e1 4, e2 3, e3 3, e4 3, e5 3 · `dc` vis, e1, e2, e3, e4, e5. Simuladores: `dcVis` (diferencial), `dcE1d` y `dcE1t` (e1 dx y tx), `dcE2` (tx), `dcE3r` (riesgo suicida → conducta en primer nivel, en «Diagnóstico») y `dcE3` (tx), `dcE4` (pauta de reducción por dosis), `dcE5` (conducta inicial en primer nivel sin derivación). Helpers comunes en `90_sim`: `par(t)`, `hv(a,v)`, `vacio(dc,t)` + los del kit (`sel num out rd`).

Reparto: ejecutor A → `05_vis` + `21_e1`; B → `22_e2` + `23_e3`; C → `24_e4` + `25_e5` + `80_sin` (con `<!--REFS-->`); D (al final) → `02_pan`. El JS de cada simulador va en `ensenanza/_sim_<X>.js` (no `.html`); el orquestador arma `90_sim.html` y `01_nav.html`.

Título `Crisis de angustia con síntomas somáticos` · salida `Crisis_de_angustia_widget_v10.html`.

## Widget B · Definiciones (skill definiciones v6) — `definiciones/`

Caso/semana: Trastornos del estado de ánimo (precaso del paciente con crisis al conducir). Términos derivados del texto del caso por el orquestador (el estudiante no entregó lista). 9 términos → régimen normal (tope 5 prerrequisitos). 5 tarjetas por término (45 en total).

| Pestaña · término | Prerrequisitos canónicos (tipo) | Remisiones | Tarjetas |
|---|---|---|---|
| t1 · Trastornos del estado de ánimo | Sistema límbico (B) · Sistemas monoaminérgicos: serotonina, noradrenalina, dopamina y MAO (B) · Afecto, ánimo y emoción como funciones psíquicas (C) | — | 5 |
| t2 · Angustia (miedo a perder el control) | Circuito del miedo: tálamo → amígdala → hipotálamo y tronco (C) · Interocepción y corteza insular (A) | sistema límbico (t1) | 5 |
| t3 · Opresión precordial | Precordio y contenido mediastínico (A) · Dolor visceral y dolor referido (C) · Aporte y demanda de oxígeno del miocardio, circulación coronaria (C) | — | 5 |
| t4 · Palpitaciones | Sistema de conducción cardiaco (B) · Sistema nervioso autónomo: divisiones, transmisores y receptores (B) | — | 5 |
| t5 · Sudoración y náuseas | Glándula sudorípara ecrina e inervación simpática colinérgica (A) · Reflejo del vómito: área postrema, núcleo del tracto solitario, aferencias vagales (C) | SNA (t4) · circuito del miedo (t2) | 5 |
| t6 · Preinfarto (término popular) | Isquemia y necrosis miocárdica en el tiempo (C) · Troponinas cardiacas en el sarcómero (A) | circulación coronaria (t3) · dolor referido (t3) | 5 |
| t7 · Estrés | Eje hipotálamo-hipófiso-suprarrenal (C) · Sistema simpático-adrenomedular (C) | SNA (t4) · circuito del miedo (t2) | 5 |
| t8 · Stresstabs | Vitaminas hidrosolubles del complejo B y C como coenzimas (B) | eje HHS (t7) | 5 |
| t9 · Xanax (alprazolam) | Receptor GABA-A (A) · Vida media, metabolismo por CYP3A4 y neuroadaptación (C) | circuito del miedo (t2) · afecto/ánimo (t1) | 5 |

- «Preinfarto»: término coloquial → define el más cercano (síndrome coronario agudo sin elevación del ST / angina inestable) con `.mini.am` (interpretación y alternativa popular). No es entidad diagnóstica.
- «Angustia»: en la tradición hispana = ansiedad con vivencia corporal; DSM-5-TR «ataque de pánico». `.mini.am` con la interpretación.
- Stresstabs y Xanax: marca + principio activo en la misma pestaña; qué es y mecanismo; manejo → paso 7 (`.mini`). Composición de Stresstabs: verificar en ficha del fabricante/registro (pendiente para haiku).
- Reparto: ejecutor E → t1–t3; F → t4–t6; G → t7–t9. Cada uno escribe sus `pNN_tK.html` y `definiciones/_decks_tK.js` (solo el objeto del mazo). El orquestador arma `p01_nav`, `p95_tg` (con `<!--REFS-->`) y `p96_js` (motor copiado del widget de definiciones existente).

Título `Definiciones · Trastornos del estado de ánimo` · salida `../Definiciones_trastornos_animo.html`.

## Reglas de diseño para ejecutores (ambos widgets)

Las 10 reglas de `widgets/patologia_urinaria_baja/PLAN.md` § «Reglas de diseño para ejecutores» aplican tal cual (clases solo del kit; tablas con thead/tbody en `div.tw`; sin recuadros anidados; tipo oración; párrafos ≤90 palabras; un `<b>` por párrafo; voz activa, español de Ecuador; sin emojis; coma decimal; conteos de la skill).
