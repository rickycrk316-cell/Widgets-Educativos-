# Trastornos del estado de ánimo — plan del orquestador

Caso: `fuentes/casos/caso_crisis_angustia_trastornos_animo.md` (consulta externa de primer nivel, **sin posibilidad de derivar**; tercer episodio en un año de palpitaciones, opresión precordial y miedo a perder el control mientras conduce; antes «preinfarto por estrés» tratado con Stresstabs y Xanax por semanas; hoy además sudoración y náuseas).

Sílabo: 2.ª rotación, **Caso 7 — Trastornos del estado de ánimo** (definición y clasificación, fisiopatología, clínica, evaluación diagnóstica, tratamiento, riesgo suicida y su manejo inicial; trabajo autónomo: historia clínica psiquiátrica). El cuadro de presentación pertenece además al **Caso 5 — TAG y ataque de pánico** (trabajo autónomo: serotonina, acetilcolina, GABA, MAO; benzodiacepinas e ISRS). Ambos se cubren.

Bibliografía: la del sílabo de la 2.ª rotación con ediciones vigentes del protocolo § 4 (el sílabo cita Harrison 19.ª y Farreras 17.ª: **discrepancia**; se usan Harrison 22.ª 2025 y Farreras 20.ª 2024) + Ebert 4.ª 2025 (complementaria del sílabo) + DSM-5-TR 2022 + guías: NICE CG113 (ansiedad/pánico), NICE NG222 (depresión), WFSBP 2023, ESC 2023 SCA, AHA/ACC 2021 dolor torácico, OMS mhGAP 2.0 (primer nivel sin especialista).

## Citas (ambos widgets)

Los ejecutores citaron con claves de un catálogo común, que se verificó en PubMed (los 10 artículos de revista, con PMID) y en la web (documentos de organismos). El orquestador las numeró por primera aparición: en enseñanza se cuenta desde `vis` y el Panorama reutiliza los números. Las partes ya llevan `[n]`, así que una cita nueva se numera a mano según el validador.

Lo que no se pudo confirmar: la composición de Stresstabs, que cambia según el país (badge ámbar en t8; DailyMed no es accesible desde la sesión). La duración del ISRS en TAG quedó respaldada por Batelaan 2017 (BMJ, PMID 28903922) y la nota de altitud para la SatO₂ en Quito por Rojas-Camayo 2018 (Thorax, PMID 29054885). También se quitó un tope de 40 mg de diazepam en la sustitución, porque no se encontró en Ashton.

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

Reparto (hecho): ejecutor A → `05_vis` + `21_e1`; B → `22_e2` + `23_e3`; C → `24_e4` + `25_e5` + `80_sin`; D → `02_pan`; el orquestador escribió `01_nav` y unió los simuladores en `90_sim`. El botón de `vis` es «Visión de conjunto».

Título `Crisis de angustia con síntomas somáticos` · salida `Crisis_de_angustia_widget_v10.html`.

## Widget B · Apertura (skill apertura v1) — `apertura/`

Reemplaza al widget de definiciones (el estudiante pidió apertura). Conserva las 9 pestañas de término y su fuente única de prerrequisitos (tabla de abajo), y añade `c0`, `pb`, `jq` y `hx`. Título `Apertura · Trastornos del estado de ánimo` · salida `../Apertura_trastornos_animo.html` · manifiesto `problemas {B:3,P:3,S:3,FR:3}`, `hipotesis 4`, `diagramas 4`.

### Términos (sin cambios en prerrequisitos)

| Pestaña · término | Prerrequisitos canónicos (tipo) | Remisiones | pid que toca (card.vin) |
|---|---|---|---|
| t1 · Trastornos del estado de ánimo | Sistema límbico (B) · Sistemas monoaminérgicos (B) · Afecto, ánimo y emoción (C) | — | P3, H4 |
| t2 · Angustia | Circuito del miedo (C) · Interocepción e ínsula (A) | sistema límbico (t1) | P1, FR3 |
| t3 · Opresión precordial | Precordio y mediastino (A) · Dolor visceral y referido (C) · Aporte y demanda de O₂ (C) | — | B1 |
| t4 · Palpitaciones | Sistema de conducción (B) · SNA (B) | — | B1, B2 |
| t5 · Sudoración y náuseas | Glándula sudorípara ecrina (A) · Reflejo del vómito (C) | SNA (t4) · circuito del miedo (t2) | B1 |
| t6 · Preinfarto | Isquemia y necrosis en el tiempo (C) · Troponinas (A) | circulación coronaria y dolor referido (t3) | P2, S3 |
| t7 · Estrés | Eje HHS (C) · Simpático-adrenomedular (C) | SNA (t4) · circuito del miedo (t2) | FR1, P3 |
| t8 · Stresstabs | Vitaminas B y C como coenzimas (B) | eje HHS (t7) | S3 |
| t9 · Xanax (alprazolam) | Receptor GABA-A (A) · Vida media, CYP3A4 y neuroadaptación (C) | circuito del miedo (t2) · afecto/ánimo (t1) | B3, FR2 |

En apertura cada término lleva la card `.card.vin` «Por qué importa en este caso» (≤70 palabras, chips `span.pid`), su ejemplo de anclaje pasa a estar anclado en el paciente (sin afirmar el diagnóstico) y cada mazo suma 1 tarjeta que conecta el término con el caso (5 → 6).

### Problemas (ids fijos)

| id | Problema | Dato del caso |
|---|---|---|
| B1 | Dolor torácico opresivo agudo con palpitaciones, sudoración y náuseas, no filiado | «opresión en el pecho… se me va a salir el corazón»; hace 40 min; sudoración y náuseas |
| B2 | Episodios paroxísticos recurrentes de activación autonómica | tercer episodio en el último año |
| B3 | Uso de alprazolam por semanas sin diagnóstico ni seguimiento claros | «recibió… Xanax (alprazolam) que consumió por varias semanas» |
| P1 | Miedo intenso a perder el control mental durante la crisis | «sensación de angustia por perder el control mental» |
| P2 | Creencia de enfermedad cardiaca grave («preinfarto») | «le diagnosticaron un preinfarto debido a estrés» (según el paciente) |
| P3 | Estrés referido como causa, con ánimo y ansiedad basal sin explorar | «debido a estrés»; el caso no describe ánimo ni preocupación entre crisis |
| S1 | Crisis mientras conduce: riesgo vial y para su trabajo | «mientras conducía su auto en dirección a su lugar de trabajo» |
| S2 | Atención en primer nivel sin posibilidad de derivar | «no tiene forma de derivar al paciente» |
| S3 | Atención previa fragmentada: rótulo impreciso y tratamientos sin diagnóstico | dos atenciones previas, «preinfarto», Stresstabs y Xanax |
| FR1 | Estrés percibido (predisponente y precipitante) | «debido a estrés» |
| FR2 | Benzodiacepina de vida media corta usada semanas (rebote, abstinencia) | alprazolam por varias semanas |
| FR3 | Situación de la que es difícil escapar (conducir) | episodio al conducir |

Datos que faltan (c0 y hx): edad y sexo; factores de riesgo cardiovascular; signos vitales; ECG y troponina actuales y de los episodios previos; glucemia; TSH; consumo de cafeína, alcohol, tabaco y otras sustancias; dosis, horario y fecha de la última toma de alprazolam; ánimo, preocupación entre crisis, ideación suicida; evitación posterior; antecedentes personales y familiares; ocupación.

### Jerarquía propuesta (`ol.rank`, todos los B, P, S una vez)

g1: B1 (amenaza vital hasta ECG y troponina). g2: B3 (abstinencia con convulsiones si se suspende de golpe; dependencia), S1 (riesgo vial inmediato si la crisis se repite al conducir), B2 (recurrencia que sostiene el diagnóstico y el deterioro). g3: P2 (sostiene la ansiedad anticipatoria y las consultas), P1, S3, S2. g4: P3. Los FR no se jerarquizan.

### Hipótesis (`.card.hx`, por probabilidad)

| id | Hipótesis | Probabilidad | Explica | Qué la confirmaría |
|---|---|---|---|---|
| H1 | Ataques de pánico recurrentes / trastorno de pánico (con posible agorafobia) | Alta | B1, B2, P1, P2, FR3 | ECG y troponina normales; criterios DSM-5-TR (≥4 síntomas con pico en minutos, ≥1 mes de miedo o evitación) |
| H2 | Síndrome coronario agudo | Media (no descartada) | B1 | ECG en ≤10 min y troponina seriada |
| H3 | Ansiedad inducida por benzodiacepinas (rebote o abstinencia) | Media | B2, B3, FR2 | Relación temporal con la última toma y el horario de dosis |
| H4 | Trastorno del ánimo o ansiedad generalizada comórbidos | Baja (por datos faltantes) | P3, FR1 | PHQ-9, GAD-7, pregunta directa por ideación suicida |

Diferencial (tabla fuera de las cards): taquicardia supraventricular, hipertiroidismo, hipoglucemia, feocromocitoma, intoxicación por estimulantes o cafeína, tromboembolia pulmonar.

### Diagramas (`figure.dg`, mínimo 4)

1. `pb` · mapa biopsicosocial: B, P, S y FR convergiendo en «Crisis de angustia con síntomas somáticos recurrente».
2. `pb` · círculo del pánico: sensación corporal → interpretación catastrófica → miedo → descarga simpática → más síntomas.
3. `jq` · escalera de gravedad (g1 → g4).
4. `hx` · predisponentes + precipitantes → síndrome → hipótesis H1–H4.

Reparto (hecho): ejecutor K → `p05_c0` + vin/anclaje/tarjeta de t1–t4; L → lo mismo en t5–t9; M → `p91_pb`; N → `p92_jq` + `p93_hx`. El orquestador armó `p01_nav`, `p95_tg`, `p96_js` y el manifiesto. Las partes ya llevan `[n]` numerados.

## Reglas de diseño para ejecutores (ambos widgets)

Las 10 reglas de `widgets/patologia_urinaria_baja/PLAN.md` § «Reglas de diseño para ejecutores» aplican tal cual (clases solo del kit; tablas con thead/tbody en `div.tw`; sin recuadros anidados; tipo oración; párrafos ≤90 palabras; un `<b>` por párrafo; voz activa, español de Ecuador; sin emojis; coma decimal; conteos de la skill).
