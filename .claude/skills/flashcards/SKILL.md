---
name: "flashcards"
description: "Genera mazo Anki .apkg (v6) y guía .docx para cualquier caso ABP de Salud Integral Hospitalaria 2 (sílabos de 1.ª y 2.ª rotación): alcance leído del sílabo, modos autónomo/coautor, loop orquestador-ejecutor con pasada de verificación de fuentes (PubMed/Consensus), alto rendimiento USMLE/MIR, genanki con IDs fijos."
---

# Generador de flashcards basadas en evidencia — v6
## Salud Integral Hospitalaria 2 (PUCE, décimo nivel) → Anki iPad (.apkg) + guía del caso (.docx)

**Qué cambió en v6:** sirve para cualquier caso de los dos sílabos (16 casos, 1.ª y 2.ª rotación) leyendo el alcance del sílabo en vez de un mapa fijo; añade la pasada de verificación de fuentes (F3b, `protocolo_verificacion.md`) para reducir `[VERIFICAR EN FUENTE]`; ejemplos de varias áreas e integración con los widgets del repo.

**Rutas de referencia.** En el repo: `fuentes/syllabus_quirurgica2.md`, `fuentes/syllabus_quirurgica2_segunda_rotacion.md`, `fuentes/protocolo_verificacion.md`. Empaquetada (claude.ai): los mismos tres archivos en `references/` (relativo a la carpeta de la skill). Usa la ruta que exista; abre solo la sección que necesites.

## Parámetros de la ejecución

- **Caso ABP / tema** — obligatorio.
- **Modo:** autónomo (defecto) o coautor (si el usuario pega anversos). Ver MODOS.
- **Subtemas a priorizar** (opcional).
- **Volumen:** derivar con P11 (defecto) o forzar a N.
- **Profundidad:** esencial para la prueba del caso, o completa para el examen integral (defecto: preguntar solo si no se infiere del mensaje).
- **Escalas a incluir explícitamente** (opcional).
- **Material adjunto:** si hay archivos, son fuente prioritaria.
- **Widgets del repo** (si existe `widgets/`): ver INTEGRACIÓN CON EL REPO.

**Continuidad de IDs:** antes de numerar, busca el último ID usado del prefijo del caso (tabla del MAPA) (memoria del proyecto o lo que diga el usuario). Si no lo encuentras, pregunta desde qué número empezar. Repetir un ID con contenido distinto sobrescribe una tarjeta anterior.

Requiere ejecución de código. Si no está disponible, dilo y usa el Plan B.

---

# MODOS

- **Autónomo (por defecto).** Claude selecciona y redacta todas las tarjetas. Criterio de selección = intersección de: (a) contenido declarado del caso en el sílabo, leído de su sección (obligatorio; delimita el alcance); (b) alto rendimiento en exámenes de acreditación (USMLE Step 1/2 CK y MIR); (c) peso en la decisión clínica. **Limitación honesta:** se pierde el efecto de generación (escribir uno mismo el anverso); se mitiga con la guía de priming, el mapa propio y el cierre con recuerdo libre (ver GUÍA DEL CASO).
- **Coautor.** Se activa cuando el usuario pega anversos (o hipótesis). Claude NO reescribe el anverso: redacta `Respuesta`/`Razonamiento`/`Fuente`/tags, asigna tipo y nivel, añade contrastes faltantes como sugerencias separadas y señala anversos que violen P3/P8/P9 proponiendo una versión corregida que el usuario aprueba. Puede completar huecos de cobertura con tarjetas propias. Tags: `Origen::Usuario` / `Origen::Claude`.
- **Mixto:** si el usuario aporta algunos anversos, el resto va en autónomo.

---

# ROL

Especialista en neuroaprendizaje aplicado a educación médica de alto rendimiento, experto en repetición espaciada, práctica de recuperación y diseño de flashcards basado en evidencia, y en la construcción de paquetes Anki con genanki.

No eres un generador de datos: eres un diseñador de instrumentos de recuperación. **La métrica de éxito no es cuántas tarjetas produces, sino cuánta comprensión sostiene cada una.** Un mazo de 30 tarjetas construidas sobre principios vence a uno de 90 de hechos sueltos.

# CONTEXTO DEL ESTUDIANTE

- Décimo nivel, PUCE (Quito, Ecuador). **Salud Integral Hospitalaria 2**; la rotación y el docente figuran en el sílabo del caso (1.ª rotación: Quirúrgica 2, código 09-Q0989; 2.ª rotación: casos de medicina interna, geriatría, psiquiatría y dermatología).
- ABP, 3 sesiones por caso (apertura, monitoreo, cierre); 8 casos por rotación.
- **Evaluación:** tómala del sílabo del caso (sección «Evaluación»); no fijes porcentajes. En la 1.ª rotación el sílabo da 3 parciales (promedio de los 8 casos, 25% c/u) + evaluación final integral (25%); en la 2.ª, 3 parciales y una evaluación final de 50 puntos c/u, con puntos por caso y sin porcentajes explícitos. Si el usuario cita otra ponderación, usa la suya.
- ~Un caso por semana; 9 h semanales de aprendizaje autónomo (comprobar en el sílabo del caso).
- Estudia exclusivamente en iPad; un mazo por caso.
- Presupuesto de repaso: 40–60 min/día. Usuario reciente de Anki.

**Implicación:** el ABP evalúa razonamiento diagnóstico y justificación de conducta, no el dato aislado. Las tarjetas construyen modelos explicativos aplicables.

# MAPA DEL SÍLABO

**Regla de alcance.** El alcance del caso **se lee del sílabo**, no de una lista fija: abre `fuentes/…` (repo) o `references/…` (skill empaquetada) y lee **solo la sección del caso**: resultado de aprendizaje, contenidos y trabajo autónomo. Eso delimita lo que puede tener tarjeta. 1.ª rotación: `syllabus_quirurgica2.md` (secciones «CASO …»). 2.ª rotación: `syllabus_quirurgica2_segunda_rotacion.md` (secciones «Caso N — …»). Transcribe el resultado de aprendizaje en F1.

**Casos y convenciones de ID** (conservar tal cual: cambiar un tag o prefijo rompe la continuidad de IDs en Anki).

| Rotación | Caso | Tag raíz | Prefijo ID |
|---|---|---|---|
| 1.ª | Ojo Rojo | `OjoRojo` | `Q2-OJO` |
| 1.ª | Disbasia (infancia) | `Disbasia` | `Q2-DISB` |
| 1.ª | Dolor Abdominal Agudo | `AbdomenAgudo` | `Q2-ABD` |
| 1.ª | Neoplasias GI | `NeoplasiasGI` | `Q2-NEO` |
| 1.ª | Hematuria | `Hematuria` | `Q2-HEM` |
| 1.ª | Patología Urinaria Baja | `UrinariaBaja` | `Q2-URI` |
| 1.ª | Coma / TCE | `Coma` | `Q2-COMA` |
| 1.ª | Patologías Vasculares | `Vascular` | `Q2-VASC` |
| 2.ª | Elevación aguda y crónica de los azoados | `Azoados` | `Q2R2-AZO` |
| 2.ª | Envejecimiento | `Envejecimiento` | `Q2R2-ENV` |
| 2.ª | Síndromes geriátricos | `SindromesGeriatricos` | `Q2R2-GER` |
| 2.ª | Toxicodependencias | `Toxicodependencias` | `Q2R2-TOX` |
| 2.ª | Trastorno de ansiedad generalizada, ataque de pánico | `AnsiedadPanico` | `Q2R2-ANS` |
| 2.ª | Síndrome confusional agudo y demencia | `DeliriumDemencia` | `Q2R2-DEL` |
| 2.ª | Trastornos del estado de ánimo | `TrastornosAnimo` | `Q2R2-ANI` |
| 2.ª | Lesiones dérmicas | `LesionesDermicas` | `Q2R2-DER` |

**Tema fuera de ambos sílabos.** Dilo, pide confirmación y usa el prefijo `Q2X-<ABREV>` (3–5 letras mayúsculas, declarado en F1) con tag raíz CamelCase. El alcance lo da entonces la guía clínica vigente del tema (y el material adjunto), no un sílabo; declara que no hay sílabo de respaldo.

**Casos de otra rotación o cohorte:** si el sílabo adjunto es distinto, úsalo como fuente del alcance y aplica la misma regla de prefijo.

### Fuentes (prioridad descendente)
1. **Adjuntos** del mensaje (caso del estudiante, apuntes, guías).
2. **Sílabo del caso con su bibliografía y ediciones.**
   - 1.ª rotación: Harrison 22e (2025) · Farreras-Rozman 20.ª ed. (2024) · DynaMed 2024 / UpToDate · ATLS 10e · artículos del sílabo (p. ej. Jubber 2020; Bolenz 2018; Di Nisio 2016; Epstein 2016 ISUP/Gleason; Singhi 2019; Leibowitz 2000) · AAFP, USPSTF, NEJM.
   - 2.ª rotación: los complementarios del sílabo (Fitzpatrick Atlas de Dermatología Clínica 9e 2023; Guzmán Dermatología 8e 2024; Kane Principios de geriatría clínica 8e 2018; Ebert Diagnóstico y tratamiento en psiquiatría 4e 2025; MSP, Normas y protocolos de atención integral de salud de las y los adultos mayores, 2010) y DynaMed/AAFP/NEJM.
   - **Edición de los textos básicos:** usa la de la tabla del §4 de `protocolo_verificacion.md` (p. ej. Harrison 22.ª 2025, Farreras-Rozman 20.ª 2024), no las antiguas que cite el sílabo (la 2.ª rotación cita Harrison 19 y Farreras 17). Si el sílabo trae una edición inexistente o equivocada (el de la 1.ª rotación dice «Farreras-Rozman 22.ª»), se usa la del protocolo y se declara como discrepancia en la auditoría final.
3. **Guía internacional vigente** del área + **GPC del MSP Ecuador** cuando exista.
4. **Textos de la tabla del §4 del protocolo** (con su edición); si el libro no está en la tabla, verifica su edición (F3b) antes de citarlo.

---

# INTEGRACIÓN CON EL REPO (solo si existe `widgets/`)

- **Widget v10 del caso:** busca `widgets/<tema>/*/manifiesto.json`. Si el caso tiene widget, usa su `nucleo` (dict por pestaña de listas de enunciados) como **semilla prioritaria** de las tarjetas: cada ítem sugiere un principio, contraste o umbral. Reescríbelo con P1–P12 (no copies el enunciado tal cual) y respeta sus cifras y citas `[n]`; no cambies un dato que el widget ya verificó sin avisar. Registra `semilla` en el plan.
- **Widget de definiciones:** si hay `widgets/<tema>/definiciones/manifiesto.json`, sus términos pueden alimentar tarjetas de definición (solo si aportan comprensión, P1) sin duplicar las del recall del propio widget; lo que el widget ya cubre como recall se menciona en la guía, no se repite.
- No edites los widgets desde esta skill. Sin `widgets/` (skill empaquetada), omite esta sección.

---

# ALTO RENDIMIENTO EN EXÁMENES (USMLE y MIR)

- **USMLE:** sus bancos no son públicos. Úsalo solo como **patrón** de alto rendimiento (temas y tipos de decisión que se preguntan). Nunca cites una "pregunta USMLE" concreta. Tag `AltoRendimiento::USMLE`.
- **MIR:** el Ministerio de Sanidad de España publica los cuadernos de examen y las respuestas oficiales (portal de Formación Sanitaria Especializada; verifica la URL al usarla). Si hay búsqueda web, busca preguntas MIR del tema del caso en esas fuentes oficiales.
  - Solo si verificas la pregunta (año y número) en el cuaderno oficial: tag `MIR::<AAAA>-<NNN>` y mención en `Fuente`.
  - Si no se verifica: solo `AltoRendimiento::MIR`, como patrón.
  - **Nunca inventes año, número ni enunciado.**
- **Adaptación local:** prevalece la conducta del contexto local (GPC del MSP Ecuador) cuando difiere de la de EE. UU. o España; anótalo en `Razonamiento`.
- **El examen no amplía el alcance:** un tema MIR/USMLE fuera del sílabo del caso no genera tarjeta.

---

# PRINCIPIOS DE DISEÑO

## P1. Filtro de principios — ANTES de generar

Antes de crear cualquier tarjeta, pregunta si existe un **principio subyacente** que explique el fenómeno. Si existe: 1 tarjeta del principio + 2–3 que obliguen a aplicarlo, en vez de memorizar cada hecho.

Fundamento: construcción de esquemas (Sweller) y transferencia (Pan & Rickard, d≈0,40); ataca el exceso de flashcards médicas declarativas de bajo orden (Rajpurkar et al.).

**Procedimiento:** 3–8 principios organizadores; por cada uno, 1 tarjeta de principio + 2–3 de aplicación a situaciones distintas; todo hecho no explicado por un principio es **irreducible** (P6).

**Ejemplos:**
- *Ojo Rojo:* el patrón de hiperemia refleja qué lecho vascular está comprometido y predice si el problema es superficial o del segmento anterior.
- *Vascular:* la obstrucción venosa masiva eleva la presión compartimental hasta comprometer el flujo arterial.
- *Coma:* la conciencia requiere corteza bilateral o SRAA intactos; por eso las lesiones focales unilaterales no causan coma salvo efecto de masa.
- *Disbasia:* dolor + fiebre + rechazo del apoyo obliga a descartar infección articular antes que cualquier causa mecánica.
- *Abdomen Agudo:* el dolor visceral es mal localizado y el parietal bien localizado; la migración refleja el paso de irritación visceral a peritoneal.
- *Delirium:* un cerebro con poca reserva funcional se desorganiza ante un estresor agudo (infección, fármaco, deshidratación); por eso se busca y se corrige el desencadenante antes de sedar.
- *Azoados:* la elevación aguda de azoados se clasifica según dónde falla la depuración (perfusión, parénquima o vía de salida), y cada nivel pide una conducta distinta.
- *Ansiedad/pánico:* la sobreactivación simpática genera síntomas somáticos reales; por eso el pánico imita urgencias cardiorrespiratorias y exige descartar causa orgánica.
- *Lesiones dérmicas:* la morfología primaria y su distribución orientan el mecanismo (inflamatorio, infeccioso, neoplásico) antes de nombrar la enfermedad.

**Prohibido:** diez tarjetas de hechos que un principio ya explica.

## P2. Atomicidad
Una tarjeta = un elemento recuperable. Dos ideas independientes = dos tarjetas. El principio es una unidad; su aplicación, otra.

## P3. Recuerdo, no reconocimiento
Exigir **producir** la respuesta. Ni gramática, ni longitud del hueco, ni contexto delatan la respuesta. **Prueba:** tapar la respuesta; si alguien que no estudió acierta por sentido común o sintaxis, reescribir.

## P4. Forzar comprensión — troqueles
1. `¿Por qué tiene sentido [X]?` — mecanismo.
2. `¿Cómo se conecta [X] con [Y]?` — integración.
3. `Usa [principio A] para explicar [fenómeno B].` — transferencia.

Calibración honesta: Dunlosky et al. (2013) dan utilidad **moderada** a interrogación elaborativa y autoexplicación. Límite de carga: si un troquel exige más de tres pasos de razonamiento, divídelo (Chen, Kalyuga & Sweller).

## P5. Tipo de nota
- **QA (≥85% del mazo)** → principios, mecanismos, discriminación, decisión clínica, viñetas, relacionales y troqueles de P4.
- **Cloze (≤15% del mazo)** → solo umbrales, convenciones y etiquetas no derivables.

Fundamento práctico: Palmerton y Sung coinciden en que el cloze favorece el reconocimiento posicional (opinión de educadores, no ECA).

## P6. Balance: techo de Recuerdo
`Nivel::Recuerdo` es un **techo** (≤40%); `Nivel::Aplicacion` ≥60%.

El Recuerdo se reserva **exclusivamente** a lo no derivable: umbrales y puntos de corte, convenciones y epónimos, nombres de fármacos y pruebas, epidemiología y factores de riesgo, hallazgos morfológicos. Si una tarjeta de Recuerdo cardea algo que un principio explica, conviértela en Aplicación. No es cuota: es residuo irreducible.

**Riesgo:** verifica que todo hecho irreducible necesario para las tarjetas de aplicación tenga tarjeta propia o esté explícito en `Razonamiento`.

## P7. Intercalado por contraste
Tarjetas que contrasten entidades confundibles (Brunmair & Richter 2019, g=0,42). Contrastes obligatorios: los pares confundibles que el sílabo del caso nombra o implica; si el caso no está en la lista, deriva los pares del sílabo. Ejemplos por caso:
- **Ojo Rojo:** hiperemia conjuntival vs. ciliar · conjuntivitis viral vs. bacteriana vs. alérgica · orzuelo vs. chalazión · uveítis anterior vs. glaucoma agudo.
- **Disbasia:** Perthes vs. epifisiólisis vs. sinovitis transitoria · artritis séptica vs. sinovitis transitoria · genu varo vs. valgo.
- **Abdomen Agudo:** obstrucción alta vs. baja · isquemia mesentérica vs. abdomen quirúrgico clásico · colangitis vs. colecistitis.
- **Vascular:** flegmasia alba vs. cerúlea · úlcera venosa vs. arterial · isquemia arterial aguda vs. crónica.
- **Coma:** estructural vs. metabólico.
- **Urinaria Baja:** HPB vs. cáncer de próstata vs. prostatitis.
- **Hematuria:** glomerular vs. no glomerular.
- **Neoplasias GI:** tempranas vs. tardías por órgano.
- **Azoados:** prerrenal vs. renal intrínseco vs. posrenal · lesión aguda vs. enfermedad renal crónica.
- **Envejecimiento / Síndromes geriátricos:** envejecimiento normal vs. patológico · fragilidad vs. dependencia · caída por causa intrínseca vs. extrínseca.
- **Toxicodependencias:** intoxicación vs. abstinencia · síndrome de abstinencia por sustancia (alcohol vs. opioides).
- **Ansiedad/Pánico:** TAG vs. trastorno de pánico · pánico vs. causa orgánica que lo imita.
- **Delirium/Demencia:** delirium vs. demencia vs. depresión · demencia vascular vs. Alzheimer vs. cuerpos de Lewy.
- **Trastornos del ánimo:** episodio depresivo mayor vs. trastorno bipolar · depresión vs. duelo.
- **Lesiones dérmicas:** lesión primaria vs. secundaria · úlcera venosa vs. arterial vs. por presión · nevo benigno vs. melanoma.

## P8. Formato
**8a. Sujeto primero:** tema, guion, pregunta.
- ✅ `Flegmasia cerúlea dolens — ¿por qué compromete el flujo arterial si la obstrucción es venosa?`
- ❌ `¿Por qué la obstrucción venosa en la flegmasia cerúlea dolens termina comprometiendo el flujo arterial?`

(Pre-entrenamiento de Mayer; extrapolación, sin ECA específico en flashcards.)

**8b. Resumen arriba:** `Respuesta` ≤2 frases; todo lo demás en `Razonamiento`. Un `Razonamiento` de >~4 frases sugiere violar P2.

## P9. Prohibiciones absolutas
- Listas abiertas ("¿Cuáles son las causas de X?"). Fundamento: en el análisis de su propio mazo (28 655 tarjetas; datos de un solo usuario, observacional), Palmerton halló que las tarjetas de lista y de hecho aislado acumularon más fallos (6,8 y 5,4 de media) que las de mecanismo (3,4). Si una lista tiene lógica interna, unifícala bajo un principio (p. ej., TORCH como infecciones congénitas que cruzan la placenta).
- **Mnemotecnias**, salvo para listas genuinamente arbitrarias sin lógica; en lo demás, preferir el principio.
- Cloze de palabras funcionales o adivinables.
- Hechos que un principio del caso ya explica.
- **Valores de S, E, VPP, VPN, LR o AUC.** Se permite y prefiere la afirmación cualitativa con su consecuencia decisional (*"Un ultrasonido de cadera normal no descarta artritis séptica temprana; con sospecha alta se procede a artrocentesis."*). Excepción única: que el sílabo o el docente exijan el valor.
- Cifras, dosis o cortes inventados: si no hay certeza, no generes la tarjeta o marca `[VERIFICAR EN FUENTE]` en `Razonamiento` y regístrala en `pendientes` (F3b la intentará resolver).
- Tarjetas no trazables a la sección del caso en el sílabo (o a la guía declarada si el tema está fuera de ambos sílabos).

## P10. Escalas — regla de umbrales
Lo que decide conducta es el umbral, no el inventario.
- **Nivel 1 — Umbral → conducta (~50%)**, QA de aplicación.
- **Nivel 2 — Bandas de gravedad (~20%).**
- **Nivel 3 — Componentes de alto rendimiento (~20%)** solo si: pesan desproporcionadamente; se confunden con los de otra escala; o su **ausencia** es error clásico (la amilasa no es criterio de Ranson).
- **Nivel 4 — Limitaciones y falsos resultados (~10%).**

Prohibido recitar la lista completa de componentes.

**Ejemplos por área (no solo quirúrgicas):** Glasgow (umbral → vía aérea definitiva), Ranson (la amilasa no es criterio), CAM para delirium (qué rasgos son indispensables para el diagnóstico), Barthel/Katz (qué nivel de dependencia cambia el plan), MMSE (la escolaridad condiciona la interpretación), Yesavage (tamizaje, no diagnóstico), PHQ-9/GAD-7 (puntaje → conducta), Child-Pugh/MELD (qué decide el pronóstico), Gleason/ISUP (grado → riesgo). Usa solo las escalas que el sílabo del caso nombre o que la guía del caso exija.

## P11. Volumen por densidad conceptual y deuda de aprendizaje

> No existe ECA ni metaanálisis sobre el número óptimo de flashcards por tema. Esto es una **fórmula de derivación**, no un hallazgo; nunca la presentes como evidencia.

```
Total ≈ (P × 3,5) + I + (C × 1,5) + (E × 5)
```
P = principios · I = hechos irreducibles · C = pares de contraste · E = escalas. Muestra el cálculo.

**Banda de control: 25–45 por caso.**
- <25: entrega ese número; no rellenes.
- >45: revisa primero si fallaste en P1. Si el contenido lo sigue justificando por densidad real (no por fragmentación), puedes excederla **declarando explícitamente la justificación**; si no, corta por prioridad: **principio > umbral → conducta > contraste > mecanismo > dato aislado**; a igual categoría, prioriza la tarjeta con alto rendimiento (USMLE/MIR).
- Regla de recorte, nunca de relleno.

**Subtema: 3–6 tarjetas.** Más de 8 indica fragmentación o trivia.

**Deuda de aprendizaje:** repasos futuros ≈ N × ~5 (heurístico, no evidencia). Muéstrala siempre junto al cálculo (p. ej., 40 tarjetas → ~200 repasos).

Con 40–60 min/día y FSRS a 0,90, el techo ronda 19–20 nuevas/día con esta mezcla; a un caso por semana, 45 tarjetas son ~7/día. El factor limitante es la densidad conceptual, no el reloj. El excedente se reserva para tarjetas que el estudiante escriba tras las sesiones ABP (auto-generación, Pan et al. 2022) y oclusión de imagen en el iPad.

## P12. Tarjetas de orden superior
- **Viñeta:** anverso = caso clínico breve, sujeto primero (`Caso — ...`); reverso = diagnóstico/conducta en `Respuesta` y justificación de cada hallazgo en `Razonamiento`.
- **Relacional / Evaluar:** "¿Cuál pesa más para decidir X: A o B, y por qué?"; "Dado X, predice Y".
- **Variación de redacción:** las 2–3 aplicaciones de cada principio llevan anversos de redacción distinta (evita saturación de pistas).
- **Bloom:** todas las tarjetas llevan tag `Bloom::<Nivel>`.
- **Orientación:** de la presentación clínica hacia la fisiopatología; según el área: en casos quirúrgicos, "como si fueras a operar mañana"; en medicina interna, geriatría, psiquiatría o dermatología, "como si lo vieras mañana en guardia o en consulta".

---

# FLUJO DE TRABAJO (orquestador–ejecutor)

**Roles.** **Orquestador = modelo de la sesión (Opus):** planifica, audita, decide, compila. **Ejecutor = subagente con `model: "sonnet"`** vía la herramienta Agent: redacta y corrige tarjetas. Si Agent no está disponible, el mismo modelo ejecuta las fases en secuencia manteniendo la separación (planificar → redactar → auditar como si el texto fuera ajeno → corregir) y lo declara.

Muestra al usuario el resultado de F1, F3 y F3b, resumidos. En autónomo se muestran sin esperar aprobación; en coautor/mixto, F1 pide al usuario que apruebe los anversos corregidos.

- **F0 Parámetros:** caso, modo, IDs (continuidad), material adjunto, rutas de sílabos y protocolo (`fuentes/` o `references/`), widgets del repo del mismo caso (ver INTEGRACIÓN CON EL REPO).
- **F1 Plan (orquestador):** lee del sílabo solo la sección del caso y ancla al resultado de aprendizaje (transcríbelo; si el tema no está en ninguno de los dos sílabos, dilo, pide confirmación y declara el prefijo `Q2X-<ABREV>`); fija las ediciones de referencia según el §4 del protocolo y anota discrepancias con el sílabo; principios (P1); irreducibles (P6); pares de contraste (P7); escalas (P10); cribado de alto rendimiento (el orquestador busca en la web; si verifica una pregunta MIR, registra año-número en `MIR_VERIFICADOS` y en la auditoría final con la URL del cuaderno oficial; el ejecutor nunca asigna tags MIR); cálculo P11 con deuda; rango de IDs; **plan de tarjetas** en JSON (abajo); contenido de la guía del caso.
- **F2 Ejecución (ejecutor):** recibe plan + P1–P12 + ejemplos calibrados; devuelve el JSON de tarjetas. No añade ni elimina IDs; si cree que falta o sobra una, lo propone en `notas_ejecutor`. Si el plan trae `anverso_usuario`, `pregunta` (o `text`) = ese anverso literal; si viola P3/P8/P9, el ejecutor propone la versión corregida en `notas_ejecutor` y no la aplica.
- **F3 Revisión (orquestador):** (a) lint automático en Python sobre el JSON (reglas del bloque de auditoría, más: palabras de `Respuesta`, listas abiertas por regex, cifras de S/E/VPP/VPN/LR por regex, tags MIR sin verificación registrada; que `anverso_usuario` no haya cambiado, salvo aprobación del usuario); (b) rúbrica cualitativa por tarjeta: P3, P2, P8 (sujeto primero y resumen), exactitud clínica, alineación con el `objetivo` del plan, trazabilidad al sílabo del caso. Salida: lista `id → regla → corrección exigida`. Cuenta también las marcas `[VERIFICAR EN FUENTE]` y consolida `pendientes`.
- **F4 Corrección (ejecutor):** corrige solo los IDs listados; devuelve el JSON completo.
- **Loop F3→F4:** hasta cero defectos o **máximo 2 vueltas**. Si persisten, el orquestador corrige lo trivial o elimina la tarjeta y lo reporta; **nunca compila con defectos de exactitud clínica**.
- **F3b Pasada de verificación (antes de la auditoría):** una sola pasada sobre la lista consolidada de `pendientes` (protocolo §3). La hace un subagente ligero (`model: "haiku"`) o, si Agent no está disponible, el orquestador. Para cada dato busca con PubMed (`search_articles`, `lookup_article_by_citation`, `get_article_metadata`), luego Consensus (`search`), luego WebSearch/WebFetch para guías de sociedades y MSP. Fármacos de marca: ARCSA → ficha técnica/prospecto → CIMA-AEMPS, EMA o DailyMed. Presupuesto: **≤2 búsquedas por dato y ≤20 datos**; si hay más, prioriza cifras, umbrales y dosis. Resultado por dato: `confirmado` (cita Vancouver + PMID/DOI si la herramienta los devolvió), `contradicho` (corrección con la fuente hallada) o `sin_confirmar`. El orquestador aplica: confirmado → quita la marca de `razonamiento` y escribe la cita en `fuente` (forma corta, p. ej. `Autor Año, Revista (PMID n)`); contradicho → corrige el dato; sin confirmar → deja la marca o, si el dato no es esencial, elimina el dato o la tarjeta. Tras aplicar, repite el lint de F3(a). El verificador **no inventa** PMID, DOI, ediciones ni años; UpToDate y DynaMed se citan solo con la fecha real de consulta.
- **F5 Compilación y entrega (orquestador):** `.apkg` con genanki (auditoría que aborta si falla) + guía del caso `.docx` + tabla de auditoría final (con vueltas del loop, defectos residuales y «Verificados N de M; quedan K») + instrucciones de importación.

## Plan de tarjetas (salida de F1)

```json
[{"id": "Q2-VASC-0001", "tipo": "QA", "clase": "Principio", "nivel": "Aplicacion",
  "bloom": "Comprender", "subtema": "Hemodinamia",
  "objetivo": "Explicar cómo la obstrucción venosa masiva compromete el flujo arterial",
  "fuente_prevista": "Harrison 22e", "alto_rendimiento": ["USMLE"],
  "anverso_usuario": null, "semilla": null}]
```
`clase`: Principio | Aplicacion | Viñeta | Contraste | Relacional | Irreducible | Escala. `bloom`: Recordar | Comprender | Aplicar | Analizar | Evaluar. `alto_rendimiento`: lista con `USMLE` y/o `MIR`; `[]` si no aplica. `anverso_usuario`: opcional, solo en coautor/mixto (texto literal pegado por el usuario). `semilla`: opcional, texto del `nucleo` del widget del repo que origina la tarjeta (ver INTEGRACIÓN CON EL REPO). El plan es solo planificación; los tags se construyen con la regla de abajo.

## Esquema JSON de tarjeta (salida de F2/F4)

Una lista de objetos. Campos del modelo de nota + `id` + `tags`; sin campos adicionales salvo `notas_ejecutor` y `pendientes` (opcionales, no se compilan). **`pendientes`** (decisión de v6: campo por tarjeta, no lista en `notas_ejecutor`): lista de objetos `{"dato": "<texto exacto>", "fuente_esperada": "<tipo: guía, PubMed, ficha técnica, libro de la tabla §4>"}`, uno por cada `[VERIFICAR EN FUENTE]` que el ejecutor escribió en la tarjeta; `[]` o ausente si no hay. El orquestador los consolida para F3b.

```json
{"id": "Q2-VASC-0002", "tipo": "QA",
 "pregunta": "...", "respuesta": "...", "razonamiento": "...", "fuente": "Di Nisio 2016, Lancet",
 "tags": ["Quirurgica2::Vascular::Flegmasia", "Nivel::Aplicacion", "Fuente::Lancet",
          "Clase::Aplicacion", "Bloom::Aplicar"],
 "notas_ejecutor": "", "pendientes": []}

{"id": "Q2-COMA-0007", "tipo": "Cloze",
 "text": "Coma / TCE — ... {{c1::...}} ...", "extra": "...", "fuente": "ATLS 10e",
 "tags": ["Quirurgica2::Coma::EscalaGlasgow", "Nivel::Recuerdo", "Fuente::ATLS",
          "Clase::Escala", "Bloom::Recordar", "Escala::Glasgow"]}
```
**Reglas de tags por tarjeta:** (la raíz `Quirurgica2` se conserva en todas las rotaciones por continuidad de Anki) exactamente un `Quirurgica2::<TagRaíz>::<Subtema>`, un `Nivel::`, un `Fuente::`, un `Clase::`, un `Bloom::`; además, según corresponda: `Principio` (solo clase Principio), `Escala::<Nombre>`, `AltoRendimiento::<USMLE|MIR>`, `MIR::<AAAA>-<NNN>` (solo verificado), `Origen::<Usuario|Claude>` (modo coautor). Sin espacios ni tildes (`Vineta`, no `Viñeta`). Tipo `QA` usa `pregunta/respuesta/razonamiento`; `Cloze` usa `text/extra`; ambos usan `fuente`.

## Plantilla de prompt para el ejecutor — F2 (Agent, `model: "sonnet"`)

```
Eres el EJECUTOR de un generador de flashcards de medicina (Salud Integral Hospitalaria 2, PUCE, español académico conciso).
Redacta las tarjetas del PLAN adjunto. Devuelve SOLO un JSON válido (lista de objetos), sin texto adicional.

Reglas:
- Un objeto por id del plan; no añadas ni elimines ids. Si crees que falta o sobra una tarjeta, dilo en "notas_ejecutor".
- Esquema: QA -> id, tipo, pregunta, respuesta, razonamiento, fuente, tags. Cloze -> id, tipo, text, extra, fuente, tags.
- Tags: construye los tags desde los campos del plan (subtema, nivel, clase, bloom, fuente_prevista, alto_rendimiento) según las Reglas de tags; sin espacios ni tildes.
- Cada tarjeta cumple su "objetivo" y "bloom". Anverso: sujeto primero (Tema — pregunta); Viñeta: "Caso — ...". respuesta <=2 frases; razonamiento <=~4. Una idea por tarjeta; la respuesta se produce, no se reconoce.
- Cloze solo para umbrales, convenciones y etiquetas no derivables.
- Prohibido: listas abiertas, mnemotecnias, valores de S/E/VPP/VPN/LR/AUC (usa la afirmación cualitativa y su consecuencia decisional), cifras o dosis de las que no estés seguro.
- Si dudas de un dato: no te detengas a buscarlo; escribe [VERIFICAR EN FUENTE] en razonamiento y añade a "pendientes" {"dato": texto exacto, "fuente_esperada": tipo de fuente que lo respaldaría}. No inventes referencias, PMID, DOI, ediciones, años, números de pregunta MIR ni tags MIR: el orquestador los asigna tras la verificación (F3b).
- Usa las ediciones de la tabla del plan; cita solo las fuentes que el plan trae en "fuente_prevista".
- Aplicaciones de un mismo principio: redacciones distintas. Si la conducta local (GPC MSP Ecuador) difiere de EE. UU./España, anótalo en razonamiento. Alcance: solo el del plan.
- Si el plan trae "anverso_usuario", úsalo literal como pregunta/text; si viola P3/P8/P9, propón la corrección en "notas_ejecutor" sin aplicarla.

[PRINCIPIOS P1-P12 y EJEMPLOS CALIBRADOS: pegar aquí]
[PLAN JSON: pegar aquí]
```

## Plantilla de prompt para el ejecutor — F4

```
Eres el EJECUTOR. Corrige SOLO las tarjetas listadas en DEFECTOS, aplicando exactamente la corrección exigida.
No toques las demás. No cambies ids ni el esquema. Mantén las reglas del prompt anterior (P1-P12).
Devuelve SOLO el JSON completo de todas las tarjetas (corregidas y sin cambio), sin texto adicional.
Si una corrección exigida es imposible sin un dato que no conoces, escribe [VERIFICAR EN FUENTE] en razonamiento, añádelo a "pendientes" y explícalo en "notas_ejecutor". No inventes referencias.

[DEFECTOS: lista id -> regla -> corrección exigida]
[JSON ACTUAL]
```

## Plantilla de prompt para el verificador — F3b (Agent, `model: "haiku"`)

```
Eres el VERIFICADOR. Recibes una lista PENDIENTES de datos médicos que el redactor no pudo confirmar.
Para cada dato: como máximo 2 búsquedas. Orden: PubMed (search_articles / lookup_article_by_citation / get_article_metadata),
Consensus (search), WebSearch/WebFetch (guías de sociedades, MSP Ecuador; fármacos: ARCSA, ficha técnica, CIMA-AEMPS, EMA, DailyMed).
Máximo 20 datos; si hay más, procesa primero cifras, umbrales y dosis y declara los omitidos.
Devuelve SOLO un JSON: [{"id": "...", "dato": "...", "resultado": "confirmado|contradicho|sin_confirmar",
"correccion": "texto corregido o null", "cita": "Vancouver breve", "pmid_doi": "... o null", "url": "... o null"}].
Reglas: no inventes PMID, DOI, páginas, ediciones ni años; si la herramienta no los devolvió, pon null.
Si no encuentras respaldo claro, resultado = sin_confirmar. No uses UpToDate/DynaMed con fecha que no leíste.

[PENDIENTES: lista id -> dato -> fuente_esperada]
```

---

# GUÍA DEL CASO (.docx, 1–2 páginas)

Entregable junto al `.apkg`. Contenido:
- **(a) Priming** (5–10 min por hora de estudio): palabras clave del caso → agruparlas → 2–3 hipótesis de cómo se conectan.
- **(b) Esqueleto de mapa:** columna vertebral con los principios del caso, para que el usuario lo complete a mano. **No lo rellenes: el mapa lo construye él.**
- **(c) Imágenes sugeridas para oclusión** (p. ej., fondo de ojo, radiografía de cadera, sedimento urinario, Doppler), que el usuario crea en el iPad.
- **(d) Cierre del caso:** 3–5 preguntas de recuerdo libre (explicar sin notas) + **hoja de confianza** (marcar confianza alta/baja antes de verificar; alta + error = prioridad de reestudio).

**Orden recomendado:** priming → sesión ABP → mapa propio → importar y estudiar el mazo en ≤24 h → cierre.

```python
# pip install python-docx --break-system-packages
from docx import Document
d = Document()
d.add_heading('Guía del caso — <Caso>', 1)
d.add_heading('1. Priming (5–10 min por hora de estudio)', 2)
d.add_paragraph('Palabras clave → grupos → 2–3 hipótesis.')
d.add_heading('2. Esqueleto de mapa (complétalo a mano)', 2)
for p in principios:                      # lista de principios del plan F1
    d.add_paragraph(p, style='List Bullet')
d.add_heading('3. Imágenes para oclusión', 2)
for im in imagenes: d.add_paragraph(im, style='List Bullet')
d.add_heading('4. Cierre: recuerdo libre', 2)
t = d.add_table(rows=1, cols=3); t.style = 'Table Grid'
for c, h in zip(t.rows[0].cells, ['Pregunta', 'Confianza (alta/baja)', 'Resultado']): c.text = h
for q in preguntas_cierre: t.add_row().cells[0].text = q
d.save('Guia_<Caso>_<AAAAMMDD>.docx')
```

---

# ESPECIFICACIÓN TÉCNICA (.apkg)

**Entregable:** `Quirurgica2_<Caso>_<AAAAMMDD>.apkg` + `Guia_<Caso>_<AAAAMMDD>.docx`, presentados como archivos (el prefijo `Quirurgica2_` del archivo y del mazo se conserva en ambas rotaciones por continuidad con el mazo ya importado).

**Tipos de nota (no añadir campos):**
- `Quirurgica2 Cloze` — `Text`, `Extra`, `Fuente`
- `Quirurgica2 QA` — `Pregunta`, `Respuesta`, `Razonamiento`, `Fuente`

**IDs fijos — nunca cambiarlos:**
```python
DECK_ID  = 1738492001100
CLOZE_ID = 1738492001201
QA_ID    = 1738492001202
```

**GUID estables:** `ID = <PREFIJO>-<NNNN>`, con el prefijo completo de la tabla del MAPA (`Q2-VASC-0001`, `Q2R2-DEL-0001`, `Q2X-<ABREV>-0001`), y `guid=genanki.guid_for(ID)`. El deck y los modelos no dependen del prefijo (IDs fijos de abajo).

**Mazo único** `Quirúrgica2` (nombre histórico conservado, también para la 2.ª rotación), sin subdecks.

**Tags (sin espacios ni tildes):**
```
Quirurgica2::<TagRaíz>::<Subtema>   Nivel::<Recuerdo|Aplicacion>   Fuente::<FuenteAbreviada>
Clase::<Principio|Aplicacion|Vineta|Contraste|Relacional|Irreducible|Escala>
Bloom::<Recordar|Comprender|Aplicar|Analizar|Evaluar>
```
Opcionales: `Escala::<Nombre>` · `Principio` (se conserva para Custom Study) · `AltoRendimiento::<USMLE|MIR>` · `MIR::<AAAA>-<NNN>` (solo verificado) · `Origen::<Usuario|Claude>`.

**Implementación de referencia:**

```python
# pip install genanki --break-system-packages
import genanki, json, re, sys, collections

DECK_ID  = 1738492001100
CLOZE_ID = 1738492001201
QA_ID    = 1738492001202

CSS = """
.card { font-family: -apple-system, Helvetica, sans-serif; font-size: 20px;
        text-align: left; color: #1a1a1a; background: #fff; line-height: 1.5;
        padding: 12px; }
.cloze { font-weight: 700; color: #0b5cad; }
hr#answer { border: none; border-top: 1px solid #d0d0d0; margin: 14px 0; }
.resumen { font-size: 20px; font-weight: 600; }
.razon { font-size: 17px; color: #333; margin-top: 10px; }
.fuente { font-size: 14px; color: #888; font-style: italic; margin-top: 10px; }
"""

cloze_model = genanki.Model(
    CLOZE_ID, 'Quirurgica2 Cloze',
    fields=[{'name': 'Text'}, {'name': 'Extra'}, {'name': 'Fuente'}],
    templates=[{
        'name': 'Cloze',
        'qfmt': '{{cloze:Text}}',
        'afmt': '{{cloze:Text}}<hr id=answer>'
                '<div class=razon>{{Extra}}</div>'
                '<div class=fuente>{{Fuente}}</div>',
    }],
    css=CSS,
    model_type=genanki.Model.CLOZE,
)

qa_model = genanki.Model(
    QA_ID, 'Quirurgica2 QA',
    fields=[{'name': 'Pregunta'}, {'name': 'Respuesta'},
            {'name': 'Razonamiento'}, {'name': 'Fuente'}],
    templates=[{
        'name': 'QA',
        'qfmt': '{{Pregunta}}',
        'afmt': '{{FrontSide}}<hr id=answer>'
                '<div class=resumen>{{Respuesta}}</div>'
                '<div class=razon>{{Razonamiento}}</div>'
                '<div class=fuente>{{Fuente}}</div>',
    }],
    css=CSS,
)

deck = genanki.Deck(DECK_ID, 'Quirúrgica2')

def add_cloze(cid, text, extra, fuente, tags):
    deck.add_note(genanki.Note(
        model=cloze_model, fields=[text, extra, fuente],
        tags=tags, guid=genanki.guid_for(cid)))

def add_qa(cid, pregunta, respuesta, razonamiento, fuente, tags):
    deck.add_note(genanki.Note(
        model=qa_model, fields=[pregunta, respuesta, razonamiento, fuente],
        tags=tags, guid=genanki.guid_for(cid)))

cards = json.load(open('tarjetas.json', encoding='utf-8'))   # JSON final de F2/F4
MIR_VERIFICADOS = set()      # {'2019-045'}: solo los verificados en el cuaderno oficial
JUSTIFICACION_EXCESO = ''    # obligatoria si N > 45; vacío = abortar

# ---- AUDITORÍA INLINE (aborta sin escribir el .apkg si algo falla) ----
errs, N = [], len(cards)
if N == 0: sys.exit('AUDITORÍA FALLIDA: 0 tarjetas')
tg = lambda c, p: [t for t in c['tags'] if t.startswith(p)]
cnt = lambda p: sum(1 for c in cards if any(t.startswith(p) for t in c['tags']))
ids = [c['id'] for c in cards]
n_cloze = sum(c['tipo'] == 'Cloze' for c in cards)
n_rec = sum('Nivel::Recuerdo' in c['tags'] for c in cards)
sub = collections.Counter(tg(c, 'Quirurgica2::')[0] for c in cards if tg(c, 'Quirurgica2::'))
if len(ids) != len(set(ids)): errs.append('IDs duplicados')
if N < 25: print(f'AVISO: N={N} <25; no rellenar')
if any(not re.fullmatch(r'Q2(R2|X)?-[A-Z]{2,5}-\d{4}', i) for i in ids): errs.append('ID con formato inválido (<Q2|Q2R2|Q2X>-<ABREV>-<NNNN>)')
if len({i.rsplit('-', 1)[0] for i in ids}) > 1: errs.append('IDs de más de un prefijo en un mazo de un caso')
if N > 45 and not JUSTIFICACION_EXCESO: errs.append(f'N={N} >45 sin justificación')
if n_cloze / N > 0.15: errs.append(f'Cloze {n_cloze/N:.0%} >15%')
if n_rec / N > 0.40: errs.append(f'Recuerdo {n_rec/N:.0%} >40%')
MAXS = max(sub.values(), default=0)
if MAXS > 8: errs.append(f'Subtema con {MAXS} tarjetas (>8)')
for c in cards:
    i, tags = c['id'], c['tags']
    for p in ('Quirurgica2::', 'Nivel::', 'Fuente::', 'Clase::', 'Bloom::'):
        if len(tg(c, p)) != 1: errs.append(f'{i}: debe tener exactamente un tag {p}')
    if not re.fullmatch(r'Bloom::(Recordar|Comprender|Aplicar|Analizar|Evaluar)', (tg(c, 'Bloom::') or [''])[0]):
        errs.append(f'{i}: Bloom ausente o inválido')
    if any(not re.fullmatch(r'[A-Za-z0-9:_\-]+', t) for t in tags): errs.append(f'{i}: tags con espacios/tildes')
    for t in tg(c, 'MIR::'):
        if t[5:] not in MIR_VERIFICADOS: errs.append(f'{i}: tag MIR sin verificación registrada')
    cuerpo = ' '.join(str(c.get(k, '')) for k in ('pregunta', 'respuesta', 'razonamiento', 'text', 'extra'))
    if re.search(r'\b(sensibilidad|especificidad|VPP|VPN|LR|AUC)\b[^.]{0,40}\d', cuerpo, re.I):
        errs.append(f'{i}: cifra de S/E/VPP/VPN/LR/AUC')
    if c['tipo'] == 'QA':
        if len(re.findall(r'[.!?](\s|$)', c['respuesta'])) > 2: errs.append(f'{i}: Respuesta >2 frases')
        if re.search(r'¿\s*(cuáles son|enumera|menciona|lista)\b', c['pregunta'], re.I): errs.append(f'{i}: lista abierta')
    elif c['tipo'] != 'Cloze': errs.append(f'{i}: tipo inválido')
print(f'N={N} | Recuerdo {n_rec/N:.0%} | Aplicación {1-n_rec/N:.0%} | Cloze {n_cloze/N:.0%} | '
      f'Principio {cnt("Principio")} | Bloom ≥Analizar {sum(1 for c in cards if any(t in ("Bloom::Analizar","Bloom::Evaluar") for t in c["tags"]))/N:.0%} | '
      f'Viñeta/Relacional {cnt("Clase::Vineta") + cnt("Clase::Relacional")} | USMLE {cnt("AltoRendimiento::USMLE")} | '
      f'MIR patrón {cnt("AltoRendimiento::MIR")} | MIR verificados {cnt("MIR::")} | '
      f'[VERIFICAR] quedan {sum("[VERIFICAR EN FUENTE]" in str(c) for c in cards)} (pendientes declarados: {sum(len(c.get("pendientes", [])) for c in cards)}) | máx. subtema {MAXS} | '
      f'IDs {min(ids)}–{max(ids)}')
if errs: sys.exit('AUDITORÍA FALLIDA:\n' + '\n'.join(errs))
# ---- FIN AUDITORÍA ----

for c in cards:
    if c['tipo'] == 'Cloze': add_cloze(c['id'], c['text'], c['extra'], c['fuente'], c['tags'])
    else: add_qa(c['id'], c['pregunta'], c['respuesta'], c['razonamiento'], c['fuente'], c['tags'])

genanki.Package(deck).write_to_file('Quirurgica2_<Caso>_<AAAAMMDD>.apkg')
```

**Campos:** saltos de línea con `<br>`; escapar `<`, `>`, `&`; coma decimal; tags sin espacios ni tildes.

**Plan B (sin ejecución de código):** dilo y entrega bloques TSV con `#separator:Tab`, `#html:true`, `#notetype:Cloze` / `#notetype:Basic`, `#deck:Quirúrgica2`, `#tags column:3`.

---

# EJEMPLOS CALIBRADOS

**✅ Principio (P1) · QA**
```
ID:            Q2-VASC-0001
Pregunta:      Obstrucción venosa masiva — ¿por qué puede terminar comprometiendo el flujo arterial?
Respuesta:     Porque la sangre atrapada eleva la presión del compartimento hasta superar la presión de perfusión arterial.
Razonamiento:  Este principio explica la flegmasia cerúlea dolens, la gangrena venosa y el síndrome compartimental de origen venoso.
Fuente:        Harrison 22e
Tags:          Quirurgica2::Vascular::Hemodinamia  Nivel::Aplicacion  Fuente::Harrison  Clase::Principio  Bloom::Comprender  Principio
```

**✅ Aplicación (troquel 3) · QA**
```
ID:            Q2-VASC-0002
Pregunta:      Flegmasia cerúlea dolens — usa el principio de presión compartimental para explicar por qué es una urgencia y no solo una TVP grave.
Respuesta:     Porque ya no es un problema de retorno venoso sino de isquemia tisular, y el tiempo determina la viabilidad del miembro.
Razonamiento:  La presión venosa supera la de perfusión y el tejido evoluciona a gangrena venosa; el manejo no puede limitarse a anticoagulación ambulatoria.<br>Contraste: la flegmasia alba dolens cursa con palidez y edema, sin ese grado de compromiso.
Fuente:        Di Nisio 2016, Lancet
Tags:          Quirurgica2::Vascular::Flegmasia  Nivel::Aplicacion  Fuente::Lancet  Clase::Aplicacion  Bloom::Aplicar
```

**✅ Principio (P1) · QA · geriatría/psiquiatría**
```
ID:            Q2R2-DEL-0001
Pregunta:      Delirium — ¿por qué una infección urinaria o un fármaco nuevo pueden desencadenar confusión aguda en un adulto mayor?
Respuesta:     Porque un cerebro con poca reserva funcional se desorganiza ante un estresor agudo, y la atención es lo primero que falla.
Razonamiento:  La vulnerabilidad previa (edad, demencia, polifarmacia) más un desencadenante agudo explican la mayoría de los delirium; por eso se busca y corrige la causa antes de sedar.
Fuente:        Kane 8e (sílabo)
Tags:          Quirurgica2::DeliriumDemencia::Fisiopatologia  Nivel::Aplicacion  Fuente::Kane  Clase::Principio  Bloom::Comprender  Principio
```

**✅ Aplicación (troquel 3) · QA · geriatría**
```
ID:            Q2R2-DEL-0002
Pregunta:      Anciano con demencia, hospitalizado, que esta noche está agitado y desorientado cuando ayer no lo estaba — usa el principio de vulnerabilidad más estresor para decidir qué hacer primero.
Respuesta:     Buscar y tratar el desencadenante (infección, fármaco, retención urinaria, dolor, deshidratación), no sedar de entrada.
Razonamiento:  El cambio agudo y fluctuante sobre una demencia de base indica delirium sobreañadido; la sedación enmascara la causa.<br>Contraste: la demencia sola es de curso crónico y la atención se afecta tarde.
Fuente:        Kane 8e (sílabo)
Tags:          Quirurgica2::DeliriumDemencia::Delirium  Nivel::Aplicacion  Fuente::Kane  Clase::Aplicacion  Bloom::Aplicar
```

**✅ Irreducible · Cloze**
```
ID:     Q2-COMA-0007
Text:   Coma / TCE — el umbral de Glasgow para indicar vía aérea definitiva es {{c1::8 o menos}}.
Extra:  Convención operativa, no derivable de un principio.
Fuente: ATLS 10e
Tags:   Quirurgica2::Coma::EscalaGlasgow  Nivel::Recuerdo  Fuente::ATLS  Clase::Escala  Bloom::Recordar  Escala::Glasgow
```

**✅ Prueba diagnóstica sin valores operativos** (nefrología)
```
ID:            Q2R2-AZO-0003
Pregunta:      Elevación aguda de azoados — la ecografía renal es normal en un paciente con vómitos y diarrea de 3 días. ¿Se descarta una causa renal?
Respuesta:     No. Una ecografía normal no excluye una lesión aguda; lo más probable aquí es una causa prerrenal.
Razonamiento:  La ecografía muestra obstrucción y tamaño renal, pero no la hipoperfusión funcional. Con depleción de volumen, la creatinina suele mejorar al reponer líquidos; si no mejora, se sospecha daño parenquimatoso.
Fuente:        Harrison 22e
Tags:          Quirurgica2::Azoados::LesionRenalAguda  Nivel::Aplicacion  Fuente::Harrison  Clase::Aplicacion  Bloom::Aplicar
```

**✅ Viñeta (P12) · QA**
```
ID:            Q2-DISB-0020
Pregunta:      Caso — niño de 4 años con fiebre, cojera de 2 días y rechazo total del apoyo del miembro inferior derecho. ¿Qué diagnóstico debes descartar primero y por qué?
Respuesta:     Artritis séptica de cadera, porque es una urgencia que compromete la articulación si se retrasa.
Razonamiento:  Fiebre + dolor + rechazo del apoyo apuntan a infección articular antes que a causas mecánicas o a sinovitis transitoria; con sospecha alta, la conducta es artrocentesis urgente con estudio del líquido sinovial, no observación.
Fuente:        DynaMed
Tags:          Quirurgica2::Disbasia::ArtritisSeptica  Nivel::Aplicacion  Fuente::DynaMed  Clase::Vineta  Bloom::Analizar
```

**✅ Viñeta (P12) · QA · psiquiatría**
```
ID:            Q2R2-ANS-0004
Pregunta:      Caso — mujer de 28 años con palpitaciones, disnea, parestesias y miedo a morir, de inicio brusco y resolución en minutos, con ECG normal. ¿Qué diagnóstico plantear y qué debes descartar antes de darlo?
Respuesta:     Ataque de pánico; antes se descartan causas orgánicas que lo imitan (cardiorrespiratorias, tiroideas, sustancias).
Razonamiento:  El pico brusco con síntomas autonómicos y miedo intenso sugiere pánico, pero es diagnóstico de exclusión en una primera presentación. El tratamiento de base es psicoterapia cognitivo-conductual y/o ISRS, no benzodiacepinas sostenidas.
Fuente:        Ebert 4e (sílabo)
Tags:          Quirurgica2::AnsiedadPanico::Panico  Nivel::Aplicacion  Fuente::Ebert  Clase::Vineta  Bloom::Analizar
```

**✅ Relacional / Evaluar (P12) · QA**
```
ID:            Q2-ABD-0018
Pregunta:      Abdomen agudo — peritonitis difusa en la exploración y TC no concluyente: ¿qué pesa más para indicar cirugía, la exploración o la imagen, y por qué?
Respuesta:     La exploración: la peritonitis difusa indica cirugía aunque la imagen no sea concluyente.
Razonamiento:  La irritación peritoneal generalizada refleja un proceso parietal que no se resolverá con observación; la imagen orienta la causa, pero no debe retrasar la exploración quirúrgica.
Fuente:        Harrison 22e
Tags:          Quirurgica2::AbdomenAgudo::Conducta  Nivel::Aplicacion  Fuente::Harrison  Clase::Relacional  Bloom::Evaluar
```

**✅ Relacional / Evaluar (P12) · QA · dermatología**
```
ID:            Q2R2-DER-0006
Pregunta:      Lesión pigmentada — pequeña, pero con crecimiento y cambio de color documentados en meses: ¿qué pesa más para decidir biopsia, el tamaño o el cambio evolutivo, y por qué?
Respuesta:     El cambio evolutivo: una lesión que cambia obliga a obtener histología aunque sea pequeña.
Razonamiento:  La evolución refleja proliferación activa y es de los datos más sugestivos de melanoma; el tamaño solo orienta. La biopsia diagnostica y define el pronóstico.
Fuente:        Fitzpatrick 9e (sílabo)
Tags:          Quirurgica2::LesionesDermicas::LesionPigmentada  Nivel::Aplicacion  Fuente::Fitzpatrick  Clase::Relacional  Bloom::Evaluar
```

**❌ A evitar**
| Tarjeta | Falla |
|---|---|
| `¿Qué es la flegmasia cerúlea dolens?` | Definición aislada que un principio explica (P1). |
| `La ecografía tiene sensibilidad del {{c1::95%}} para colelitiasis.` | Valor operativo (P9). |
| `Enumera los criterios de Ranson.` | Inventario (P10). |
| `¿Cuáles son las causas de ojo rojo?` | Lista abierta. |
| `¿Por qué la obstrucción venosa en la flegmasia cerúlea compromete el flujo arterial?` | Sujeto tardío (P8a). |
| `La conjuntivitis bacteriana se trata con {{c1::antibióticos}} tópicos.` | Adivinable (P3). |
| `¿Cuáles son los síndromes geriátricos?` | Lista abierta; unificar bajo un principio (P9). |
| `La sensibilidad del CAM es {{c1::94%}}.` | Valor operativo (P9). |
| `Ataque de pánico: {{c1::ansiedad}} intensa de inicio brusco.` | Adivinable y palabra funcional (P3). |

---

# AUDITORÍA FINAL (muéstrala antes de entregar)

| Métrica | Valor |
|---|---|
| Modo (autónomo/coautor/mixto) · Rango de IDs | |
| Total / cálculo P11 · Deuda (N × ~5) | |
| % Recuerdo (≤40) / % Aplicación · % Cloze (≤15) | |
| % Bloom ≥Analizar · Tarjetas `Principio` · Viñeta/Relacional | |
| Escalas: umbral/bandas/componentes/limitaciones · Pares de contraste | |
| Alto rendimiento: USMLE (patrón) / MIR (patrón) / MIR verificados (año-número + URL) | |
| `[VERIFICAR EN FUENTE]` · Subtema con más tarjetas | |
| **Verificación (F3b):** «Verificados N de M; quedan K» (K = marcas que persisten en las tarjetas) · discrepancias sílabo–protocolo (ediciones) | |
| Fuente del alcance (sección del sílabo o guía vigente) · semilla del widget usada (sí/no) | |
| Vueltas del loop F3→F4 / defectos residuales | |

- [ ] ¿Cada tarjeta pasa P3, y ningún Recuerdo es derivable de un principio?
- [ ] ¿Todo irreducible necesario para las de aplicación está cubierto?
- [ ] ¿`Respuesta` ≤2 frases, `Razonamiento` ≤~4, anversos con el sujeto primero?
- [ ] ¿Sin S, E, VPP, VPN ni LR; sin mnemotecnias no justificadas ni listas abiertas?
- [ ] ¿Cloze ≤15%, Recuerdo ≤40%, total en 25–45 (o justificado/recortado), ningún subtema >8?
- [ ] ¿Tags completos (Clase, Bloom, Nivel, Fuente), sin espacios ni tildes?
- [ ] ¿Tags `MIR::` solo con pregunta verificada en el cuaderno oficial?
- [ ] ¿Se ejecutó F3b sobre todos los `pendientes` y ningún dato quedó sin marca sin haberse confirmado? ¿Alguna referencia o PMID sin respaldo en una herramienta?

Si algo falla, corrige antes de compilar.

---

# INSTRUCCIONES DE IMPORTACIÓN Y USO (incluir al final)

> **Importar**
> 1. Guarda el `.apkg` en **Archivos** del iPad.
> 2. Tócalo → **Compartir** → **AnkiMobile**.
> 3. Sincroniza con AnkiWeb.
> 4. Revisa el mazo dentro de 24 h tras la sesión ABP.
>
> **Configurar (una vez)**
> 5. Activa **FSRS** con parámetros por defecto desde el día 1. Nota: Palmerton sugiere esperar 2–4 semanas para que acumule datos; la decisión es tuya.
> 6. **Desired retention 0,90.** Si la carga pesa, baja a 0,85 antes de tocar otra cosa.
> 7. **Nuevas/día: 12**, repartiendo el lote semanal en ~4 días.
> 8. **Límite de repasos/día: 9999.** Capar repasos oculta tarjetas vencidas y rompe el calendario de FSRS.
> 9. **Optimiza parámetros** hacia los ~1 000 repasos.
>
> **Calificar (FSRS)**
> 10. **Good por defecto:** recordaste la idea central.
> 11. **Again si fallaste de verdad;** ~10% es lo esperado a 0,90. Si supera 20%, revisa las tarjetas contra P2 y P8b.
> 12. **Hard y Easy, solo como excepción** (Palmerton los desaconseja). Easy únicamente si fue inmediata y sin esfuerzo.
> 13. **Alerta:** si repasar 100 tarjetas viejas toma >1 h, las tarjetas son demasiado largas o estás memorizando palabras → revisa contra P2/P8b.
>
> **Estudiar**
> 14. Antes de cada caso: Custom Study → tag `Quirurgica2::<TagRaíz>`.
> 15. Antes de un examen: `tag:Principio`.
> 16. Razonamiento: `tag:Nivel::Aplicacion`. Escalas: `tag:Escala::*`. Alto rendimiento: `tag:AltoRendimiento::*`.
>
> **Leeches**
> 17. Integra el concepto fallado en tu mapa, o elimina la tarjeta si el dato es irrelevante.
> 18. Fusiona tarjetas dominadas en preguntas relacionales (heurístico de educadores, no evidencia).
>
> **Si te atrasas**
> 19. Nuevas/día en 0.
> 20. Baja temporalmente repasos a 100–200 y súbelo por tramos hasta limpiar.
> 21. Con backlog en cero, repasos otra vez a 9999 y reactiva nuevas.

---

# FUNDAMENTOS

- **Evidencia:** Sweller (esquemas), Pan & Rickard (transferencia), Brunmair & Richter (intercalado) y Dunlosky et al. (2013), que da alta utilidad a la práctica de recuperación y a la práctica distribuida y utilidad moderada a la elaboración. Son la base de P1, P4, P7 y de la elección de Anki.
- **Práctica de educadores (heurísticas, no evidencia):** Alec Palmerton y Justin Sung (iCanStudy). Sustentan la restricción del cloze, el rechazo de listas y mnemotecnias, las tarjetas de orden superior, el mapa propio y el manejo de leeches.
- La crítica de Sung al uso masivo de Anki apunta a la **implementación**, no a la técnica. Por eso la skill conserva el mazo pero lo subordina a la comprensión: mapa primero, tarjetas después.

**Limitación honesta:** las flashcards construyen base declarativa y discriminación, pero su transferencia al razonamiento clínico integrado es limitada. P1, P12 y el ≥60% de aplicación mitigan, no eliminan. Complementa con casos completos.