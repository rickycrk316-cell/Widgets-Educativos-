# Ansiedad y pánico — plan del orquestador

Fuentes (prioridad en este orden):
1. **Caso** (texto del estudiante): `fuentes/casos/caso_ansiedad_panico.md`.
2. **Sílabo**, segunda rotación, caso 5 «Trastorno de ansiedad generalizada, ataque de pánico» (`fuentes/syllabus_quirurgica2_segunda_rotacion.md`): trabajo autónomo = concepto de ansiedad; fisiología neuroendocrina (serotonina, acetilcolina, GABA, MAO); benzodiacepinas e ISRS.
3. Guía o texto de referencia vigente: DSM-5-TR 2022 (ataque de pánico), AHA/ACC 2021 (dolor torácico), Cuarta definición universal del infarto 2018, EHRA (palpitaciones), Goodman & Gilman 14.ª ed. 2023, Guyton y Hall 14.ª ed. 2021, Kandel 6.ª ed. 2021, Moore 9.ª ed. 2023.

## Widget · Definiciones (skill definiciones v5.1) — `definiciones/`

- Caso/semana: Ansiedad y pánico (primera sesión). Consulta externa sin posibilidad de derivar.
- Términos, en este orden de pestañas (10 → régimen normal, tope 5 prerrequisitos):
  1. Opresión en el pecho (opresión precordial)
  2. Palpitaciones
  3. Angustia por perder el control mental
  4. Preinfarto — término coloquial, no diagnóstico: `.mini` ámbar con la interpretación (angina inestable / síndrome coronario agudo sin elevación del ST) y la alternativa (uso popular para cualquier dolor torácico «de corazón»)
  5. Stresstabs — producto comercial (multivitamínico del complejo B con vitamina C; composición según presentación): define qué es; badge «Fuente por verificar» para la composición; manejo al paso 7
  6. Xanax (alprazolam) — una pestaña con ambos nombres (marca y principio activo); qué es y su mecanismo; manejo al paso 7
  7. Ansiedad
  8. Pánico — la emoción de miedo extremo súbito; «trastorno de pánico» va en «No confundir con»
  9. Ataque de ansiedad — término coloquial (regla de la skill v6)
  10. Ataque de pánico — episodio según DSM-5-TR
  + pestaña final **Repaso global**.
- Alcance: paso 1 del ABP (qué es, qué lo distingue, cómo se reconoce). No se resuelve el caso: el widget no dice que sea un ataque de pánico ni que se haya descartado un síndrome coronario. Los ejemplos de anclaje pueden usar al paciente del caso.

### Manifiesto de prerrequisitos

| Pestaña / término | Prerrequisitos canónicos (tipo) | Remisiones | Tarjetas |
|---|---|---|---|
| t1 Opresión en el pecho | Inervación sensitiva del corazón y dolor visceral referido (C) · Balance entre aporte y demanda de oxígeno del miocardio (C) | — | 5 |
| t2 Palpitaciones | Sistema de excitación y conducción del corazón (B) · Respuesta simpaticoadrenal de lucha o huida (C) | — | 5 |
| t3 Angustia por perder el control mental | Circuito del miedo: amígdala, corteza prefrontal, hipocampo, hipotálamo, locus coeruleus (B) · Ventilación y CO₂: hiperventilación y alcalosis respiratoria (C) | respuesta simpaticoadrenal (t2) | 6 |
| t4 Preinfarto | Arterias coronarias (A) · Complejo de troponinas del sarcómero cardiaco (A) + mecanismo mínimo (placa inestable → trombo → isquemia) | balance de oxígeno del miocardio (t1) | 6 |
| t5 Stresstabs | Vitaminas hidrosolubles como cofactores del metabolismo (B) | — | 5 |
| t6 Xanax (alprazolam) | Receptor GABA-A y la inhibición sináptica (A) · Vida media de eliminación y estado estacionario (C) | circuito del miedo (t3) | 6 |

| t7 Ansiedad | Eje hipotálamo-hipófiso-suprarrenal (C) · Sistema serotoninérgico: núcleos del rafe y proyecciones (B) | circuito del miedo (t3) · lucha o huida (t2) | 5 |
| t8 Pánico | Interocepción y corteza insular (A) | circuito del miedo (t3) | 5 |
| t9 Ataque de ansiedad | — (término coloquial sin base nueva: declarado) | lucha o huida (t2) · eje HHS (t7) | 5 |
| t10 Ataque de pánico | Curso temporal de la descarga de catecolaminas (C) | lucha o huida (t2) · hiperventilación (t3) · interocepción (t8) | 6 |

Totales: 15 prerrequisitos canónicos · 11 remisiones · 54 tarjetas. Ampliación (skill definiciones v6): t7–t10 añadidas tras t6 para no mover prerrequisitos canónicos ni la numeración de referencias; 10 términos → régimen normal (tope 5). Partes `p70_t7`, `p80_t8`, `p90_t9`, `p92_t10` (orden alfabético < `p95`). Fuentes: solo [1] Guyton, [4] Kandel, [5] DSM-5-TR y [9] Goodman & Gilman ya numeradas. «Ataque de ansiedad»: término coloquial (no es categoría del DSM-5-TR) → término cercano + `.mini` ámbar.

### Referencias (numeración fija por primera aparición)

| [n] | Fuente | Dónde aparece primero |
|---|---|---|
| 1 | Guyton y Hall 2021 | t1 prerrequisitos (también t2, t3, t4, t5) |
| 2 | AHA/ACC 2021, dolor torácico (Gulati) | t1 definición |
| 3 | EHRA, palpitaciones (Raviele 2011) | t2 definición |
| 4 | Kandel 2021 | t3 prerrequisitos |
| 5 | DSM-5-TR 2022 | t3 definición |
| 6 | Moore 2023 | t4 prerrequisitos |
| 7 | Cuarta definición universal del infarto (Thygesen 2018) | t4 definición |
| 8 | Consenso internacional de Takotsubo (Ghadri 2018) | t4 «No confundir con» |
| 9 | Goodman & Gilman 2023 | t6 prerrequisitos y definición |

Stresstabs: definición con «Fuente por verificar» (ficha técnica no consultada).

- Diseño: igual que `patologia_urinaria_baja/PLAN.md` § Widget B (cabecera `kit/def_head.html`, solo sus clases, glifos sin ✅ ⚠️ ❌, remisión con ↪) y sus reglas de diseño 1–10.
- Validación: `python3 kit/construir.py widgets/ansiedad_panico/definiciones` + `auditar_definiciones.py <html> 6` + `probar_definiciones.js`.
- Archivo: `Definiciones_ansiedad_panico.html`.

## Widget · Enseñanza (skill widget-ensenanza v10.1, multi) — `ensenanza/`

- Sílabo, 2.ª rotación, caso 5. Resultado: «Maneja de manera integral a los pacientes con ansiedad de acuerdo con evidencia científica». Contenidos: TAG, ataque de pánico, trastornos por estrés, trastornos fóbicos, trastornos somatomorfos. Trabajo autónomo: concepto de ansiedad; serotonina, acetilcolina, GABA, MAO; benzodiacepinas e ISRS. Objetivo general: manejo integral en el nivel de atención, factores de riesgo y repercusiones psicológicas, sociales, personales y familiares (APS, comunicación, ética).
- Presentación común: **síntomas físicos de ansiedad (palpitaciones, opresión torácica, disnea, temblor) y miedo en la consulta de atención primaria**.
- `Modo: multi · Entidades: e1=Trastorno de pánico (principal), e2=Ansiedad generalizada, e3=Trastornos fóbicos, e4=Trauma y estrés, e5=Síntomas somáticos · Amenaza: e4 · Override: no` (e2 = trastorno de ansiedad generalizada; e4 = trastornos relacionados con trauma y factores de estrés; e5 = trastorno de síntomas somáticos y relacionados)
- Eje declarado: **qué dispara la ansiedad** — nada (crisis inesperadas, e1) → el futuro difuso (preocupación, e2) → un objeto o situación concretos (e3; la agorafobia es el subtipo que conecta con conducir) → un evento traumático o estresante (e4) → el propio síntoma corporal (e5).
- Principal: el trastorno de pánico (es el patrón del caso y la consulta más frecuente por síntomas cardiopulmonares en APS). Amenaza: trauma y estrés, por riesgo suicida y cronificación si no se pregunta por el evento; las imitaciones orgánicas (síndrome coronario agudo, arritmia, hipertiroidismo, abstinencia de benzodiacepinas o alcohol, hipoglucemia, feocromocitoma) abren el `hb ro` de `vis` como banderas del grupo.
- Precisión sobre el sílabo (`hb am` en e5): «trastornos somatomorfos» fue reemplazado en el DSM-5 (y DSM-5-TR) por «trastorno de síntomas somáticos y trastornos relacionados».
- Subtipos: e3 = agorafobia, ansiedad social, fobia específica; e4 = trastorno de estrés agudo, TEPT, trastorno de adaptación; e5 = síntomas somáticos, ansiedad por enfermedad, conversión (síntomas neurológicos funcionales).
- «No confundir con…» fuera del grupo: síndrome coronario agudo y arritmias (e1), depresión mayor (e2), TOC (e3), hipertiroidismo (e2), enfermedad orgánica no diagnosticada (e5).
- Simuladores: `dcVis` (diferencial por desencadenante y curso) · `dcE1dx` (ataque de pánico + banderas orgánicas → conducta en consulta sin derivación) · `dcE1tx` (ISRS por perfil; benzodiacepina solo puente) · `dcE2` (GAD-7 → banda → conducta escalonada) · `dcE3` (subtipo → tratamiento) · `dcE4` (tiempo desde el evento → TEA/TEPT/adaptación → conducta y riesgo suicida) · `dcE5` (SSS-8/banderas → manejo en APS).
- Título: `Ansiedad y pánico` · Slug: `Ansiedad_y_panico_widget_v10.html`.

### Referencias: claves simbólicas

Los ejecutores citan con `[@clave]` (varias: `[@a, @b]`); el orquestador renumera por primera aparición en orden de barra y genera `ol.vanc` al final. Clave nueva → el ejecutor la propone en su archivo `refs_<parte>.txt` con la referencia Vancouver completa; la verifica `haiku`.

| Clave | Fuente |
|---|---|
| `dsm` | DSM-5-TR 2022 |
| `nice113` | NICE CG113, TAG y trastorno de pánico en adultos (2011, actualizada 2020) |
| `nice159` | NICE CG159, ansiedad social (2013) |
| `nice116` | NICE NG116, TEPT (2018) |
| `gad7` | Spitzer 2006, GAD-7 |
| `sss8` | Gierk 2014, SSS-8 |
| `pcptsd5` | Prins 2016, PC-PTSD-5 |
| `gulati` | AHA/ACC 2021, dolor torácico |
| `harrison` | Harrison 22e 2025 |
| `goodman` | Goodman & Gilman 14.ª 2023 |
| `kandel` | Kandel 6.ª 2021 |
| `guyton` | Guyton y Hall 14.ª 2021 |
| `ebert` | Ebert, Diagnóstico y tratamiento en psiquiatría 4e 2025 (sílabo) |
| `dm_<fármaco>` | Ficha DailyMed del fármaco (posología); la verifica `haiku` |
