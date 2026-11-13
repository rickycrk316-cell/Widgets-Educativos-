---
name: "flashcards"
description: "Genera mazo Anki .apkg (v7) y guía de estudio .docx para cualquier caso ABP de Salud Integral Hospitalaria 2 (sílabos de 1.ª y 2.ª rotación): alcance leído del sílabo, modos autónomo/coautor, orquestador-ejecutores con verificación obligatoria en cascada y cero marcas (lo no confirmado se elimina), diseño visual «Chips clínicos» con color por tipo de dato, campos Mnemotecnia y Esquema, compilador con lint y registro de IDs en mazos/."
---

# Flashcards basadas en evidencia — v7
## Salud Integral Hospitalaria 2 (PUCE, 10.º nivel) → Anki (.apkg) + guía de estudio (.docx)

**Qué cambió en v7.** (1) **Cero marcas**: ningún mazo lleva `[VERIFICAR EN FUENTE]`, «por verificar», «pendiente» ni similar; verificación obligatoria y sin tope de datos; el compilador aborta si encuentra una marca. (2) **Diseño «A · Chips clínicos»**: el color significa tipo de dato, igual en todos los mazos. (3) **Modelos nuevos** `Q2 v7 QA` y `Q2 v7 Cloze` con campos **Mnemotecnia** y **Esquema**. (4) Se **deroga la prohibición de mnemotecnias** (antigua P9). (5) Mazos versionados en `mazos/<tema>/` con registro de IDs. (6) Guía .docx rediseñada (por qué, cuándo y cómo). (7) El código vive en `kit/anki/`, no en este archivo.

**Rutas.** Repo: sílabos y protocolo en `fuentes/` (`syllabus_quirurgica2.md`, `syllabus_quirurgica2_segunda_rotacion.md`, `protocolo_verificacion.md`); herramientas en `kit/anki/`; mazos y registro en `mazos/`. Skill empaquetada: `references/` y `assets/kit/anki/` (registro de partida en `assets/mazos/README.md`; fuera del repo pasa `--registro <carpeta_de_mazos>/README.md` al compilador). Abre solo la sección que necesites.

| Herramienta | Uso |
|---|---|
| `kit/anki/compilar_mazo.py <mazos/tema/tarjetas.json> [--solo-lint] [--demo]` | lint completo; si pasa, genera `.apkg`, lo inspecciona (zip + sqlite) y actualiza `mazos/README.md`. Requiere `pip install genanki` (sin él, `--solo-lint` funciona) |
| `kit/anki/guia_docx.py <tarjetas.json>` | guía `.docx` desde `meta.guia` + tarjetas (python-docx) |
| `node kit/anki/previsualizar.js <tarjetas.json> <scratchpad>/capturas [N]` | anverso/reverso × claro/noche × iPhone 390 px / iPad 820 px; avisa de desbordes e imágenes rotas |
| `kit/anki/estilos.css`, `kit/anki/modelo.py` | CSS del tema A, IDs, campos, plantillas y lista blanca HTML |

Requiere ejecución de código. Si no hay, dilo y entrega el JSON de tarjetas para compilar después (no hay Plan B sin compilador: el lint es parte del contrato).

---

# 0 · Parámetros

- **Caso ABP / tema** (obligatorio). **Modo**: autónomo (defecto), coautor o mixto.
- **Subtemas a priorizar**, **escalas** a incluir, **profundidad** (prueba del caso o examen integral; pregunta solo si no se infiere).
- **Volumen**: derivado con P11 (banda 25–45; techo ~45 salvo que el dueño pida otro).
- **Fechas** (opcionales, para el calendario de la guía): apertura, cierre, examen.
- **Material adjunto**: fuente prioritaria.
- **Continuidad de IDs**: lee `mazos/README.md` (prefijo, ID de mazo, último ID). Los nuevos continúan desde el último; un ID publicado nunca se reasigna a otro contenido (sobrescribiría la tarjeta). Si el prefijo no está, añade la fila antes de compilar.

# 1 · Modos

- **Autónomo.** Claude selecciona y redacta. Criterio = intersección de (a) contenido del caso en el sílabo (delimita el alcance), (b) alto rendimiento USMLE/MIR, (c) peso en la decisión clínica. Se pierde el efecto de generación al no escribir el estudiante el anverso; la guía lo compensa (decir la respuesta antes de voltear, mapa propio, recuerdo libre).
- **Coautor.** El usuario pega anversos: Claude no los reescribe; redacta el resto, asigna tipo y nivel, sugiere contrastes y señala anversos que violen P3/P8 proponiendo una corrección que el usuario aprueba. Tags `Origen::Usuario` / `Origen::Claude`.
- **Mixto.** Lo aportado va en coautor; el resto, autónomo.

# 2 · Contexto y alcance

Estudiante de 10.º nivel, PUCE (Quito). ABP de 3 sesiones por caso (apertura, monitoreo, cierre), ~un caso por semana, 40–60 min/día de repaso, estudia en iPad (y iPhone). La evaluación se toma de la sección «Evaluación» del sílabo del caso; no fijes porcentajes. El ABP evalúa razonamiento y conducta: las tarjetas construyen modelos explicativos, no datos sueltos.

**Regla de alcance.** Lee del sílabo solo la sección del caso (resultado de aprendizaje, contenidos, trabajo autónomo) y transcribe el resultado de aprendizaje en `meta.resultado_aprendizaje`. 1.ª rotación: secciones «CASO …» de `syllabus_quirurgica2.md`; 2.ª: «Caso N — …» de `syllabus_quirurgica2_segunda_rotacion.md`. Tema fuera de ambos sílabos: dilo, pide confirmación, prefijo `Q2X-<ABREV>` y guía clínica vigente como alcance. Un tema MIR/USMLE fuera del caso no genera tarjeta.

| Rotación | Caso | Tag raíz | Prefijo |
|---|---|---|---|
| 1.ª | Ojo Rojo · Disbasia · Dolor Abdominal Agudo · Neoplasias GI | `OjoRojo` · `Disbasia` · `AbdomenAgudo` · `NeoplasiasGI` | `Q2-OJO` · `Q2-DISB` · `Q2-ABD` · `Q2-NEO` |
| 1.ª | Hematuria · Patología Urinaria Baja · Coma/TCE · Patologías Vasculares | `Hematuria` · `UrinariaBaja` · `Coma` · `Vascular` | `Q2-HEM` · `Q2-URI` · `Q2-COMA` · `Q2-VASC` |
| 2.ª | Azoados · Envejecimiento · Síndromes geriátricos · Toxicodependencias | `Azoados` · `Envejecimiento` · `SindromesGeriatricos` · `Toxicodependencias` | `Q2R2-AZO` · `Q2R2-ENV` · `Q2R2-GER` · `Q2R2-TOX` |
| 2.ª | Ansiedad/pánico · Delirium y demencia · Trastornos del ánimo · Lesiones dérmicas | `AnsiedadPanico` · `DeliriumDemencia` · `TrastornosAnimo` · `LesionesDermicas` | `Q2R2-ANS` · `Q2R2-DEL` · `Q2R2-ANI` · `Q2R2-DER` |

El prefijo `Q2-TOX` (mazo antiguo) está retirado: toxicodependencias empieza en `Q2R2-TOX-0001`. El ID de mazo de cada prefijo está en `mazos/README.md`.

**Fuentes (prioridad):** adjuntos → sílabo del caso y su bibliografía → guía internacional vigente y GPC del MSP Ecuador → textos de la tabla §4 del protocolo, con **su** edición (Harrison 22.ª 2025, Farreras-Rozman 20.ª 2024…; si el sílabo cita otra edición, se usa la del protocolo y la discrepancia va a la auditoría).

**Integración con el repo (si existe `widgets/`).** El `nucleo` del `manifiesto.json` del widget del caso es semilla prioritaria (registrar `semilla` en el plan); reescríbelo con P1–P12, respeta sus cifras verificadas. Los términos del widget de definiciones solo dan tarjeta si aportan comprensión. No edites widgets desde esta skill. **Prohibidas** las tarjetas que hablan del estado de un widget, del mazo o de la propia fuente («el widget cita…»): el lint las rechaza.

**Alto rendimiento.** USMLE solo como patrón (`AltoRendimiento::USMLE`), nunca «pregunta USMLE» concreta. MIR: tag `MIR::<AAAA>-<NNN>` solo si el orquestador verificó la pregunta en el cuaderno oficial del Ministerio de Sanidad (registrar en `meta.mir_verificados` con URL en la auditoría); si no, `AltoRendimiento::MIR`. Nunca inventes año, número ni enunciado. La conducta local (GPC MSP) prevalece y se anota en el razonamiento.

---

# 3 · Principios de redacción

**P1. Principio antes que hechos.** 3–8 principios organizadores; por cada uno, 1 tarjeta de principio + 2–3 de aplicación a situaciones distintas (redacciones distintas). Lo no explicado por un principio es irreducible (P6). Base: construcción de esquemas y transferencia (Pan & Rickard 2018, d≈0,40). Ejemplos: *Vascular* — la obstrucción venosa masiva eleva la presión compartimental hasta comprometer el flujo arterial. *Coma* — la conciencia requiere corteza bilateral o SRAA intactos. *Delirium* — un cerebro con poca reserva se desorganiza ante un estresor agudo: se busca el desencadenante antes de sedar. *Azoados* — se clasifica por dónde falla la depuración (perfusión, parénquima, vía de salida).

**P2. Atomicidad.** Una tarjeta = un elemento recuperable (mínima información, Wozniak).

**P3. Recuerdo, no reconocimiento.** Ni gramática, ni longitud del hueco, ni contexto delatan la respuesta. Prueba: tapa la respuesta; si alguien que no estudió acierta por sintaxis, reescribe.

**P4. Troqueles de comprensión.** «¿Por qué tiene sentido X?» · «¿Cómo se conecta X con Y?» · «Usa el principio A para explicar B». Máximo tres pasos de razonamiento por tarjeta. (Dunlosky 2013: utilidad moderada para la interrogación elaborativa.)

**P5. Tipo de nota.** QA ≥85 % (principios, mecanismos, discriminación, decisión, viñetas). Cloze ≤15 %, solo para umbrales, convenciones y etiquetas no derivables.

**P6. Techo de Recuerdo.** `Nivel::Recuerdo` ≤40 % y solo para lo no derivable (cortes, convenciones, epónimos, nombres de fármacos y pruebas, epidemiología, morfología). Todo irreducible que necesiten las de aplicación tiene tarjeta o está en el razonamiento.

**P7. Intercalado por contraste.** Pares confundibles que el sílabo nombra o implica (Brunmair & Richter 2019, g=0,42). Ejemplos: hiperemia conjuntival vs. ciliar · artritis séptica vs. sinovitis transitoria · prerrenal vs. renal vs. posrenal · intoxicación vs. abstinencia · TAG vs. pánico · delirium vs. demencia vs. depresión · depresión vs. duelo · úlcera venosa vs. arterial vs. por presión · nevo vs. melanoma. Los contrastes de 3+ rasgos piden **Esquema** (tabla).

**P8. Formato.** (a) Sujeto primero: el anverso empieza por `<span class="tema">Sujeto</span>` y sigue la pregunta. (b) `Respuesta` ≤2 frases; el resto en `Razonamiento` (≤~4 frases; más sugiere violar P2).

**P9. Prohibiciones.** Listas abiertas («¿Cuáles son…?»): unifícalas bajo un principio o un esquema. Cloze de palabras funcionales o adivinables. Hechos que un principio ya explica. **Valores de S, E, VPP, VPN, LR o AUC** (usa la afirmación cualitativa con su consecuencia; excepción: que el sílabo o el docente exijan el valor). Cifras, dosis o cortes no verificados (§5). Tarjetas no trazables al caso. Metatexto sobre widgets, mazo o fuentes. *(Las mnemotecnias ya no están prohibidas: ver §6.)*

**P10. Escalas: umbral, no inventario.** Umbral → conducta (~50 %), bandas de gravedad (~20 %), componentes de alto rendimiento (~20 %, solo si pesan, se confunden o su ausencia es error clásico: la amilasa no es criterio de Ranson), limitaciones (~10 %). Prohibido recitar todos los componentes. Solo escalas que el sílabo nombre o la guía del caso exija (Glasgow, CAM, Barthel/Katz, MMSE, Yesavage, PHQ-9/GAD-7, Child-Pugh/MELD, Gleason/ISUP…).

**P11. Volumen.** Fórmula de derivación (no evidencia): `Total ≈ P×3,5 + I + C×1,5 + E×5` (principios, irreducibles, contrastes, escalas); muéstrala con la deuda (≈ N × 5 repasos, heurístico). Banda 25–45: por debajo no se rellena; por encima, revisa P1 y recorta por prioridad **principio > umbral→conducta > contraste > mecanismo > dato aislado** (a igualdad, alto rendimiento); exceder exige `meta.justificacion_exceso`. Subtema 3–6 tarjetas (>8 = fragmentación; el lint lo rechaza).

**P12. Orden superior.** Viñeta (`Caso — …`: diagnóstico/conducta en la respuesta, justificación de cada hallazgo en el razonamiento), relacional («¿qué pesa más para decidir X, A o B, y por qué?»), predicción («dado X, predice Y»). Tag `Bloom::` en todas. Orientación: «como si lo vieras mañana en guardia o en quirófano».

---

# 4 · Flujo orquestador → ejecutores

**Roles.** Orquestador = modelo de la sesión: planifica, audita, decide, compila. Ejecutores = subagentes (herramienta Agent) **capaces** (`sonnet` o superior; **nunca `haiku`**, tampoco para verificar). Sin Agent, el mismo modelo hace las fases en secuencia, auditando como si el texto fuera ajeno, y lo declara. En autónomo se muestran F1, F3 y F4 resumidos sin esperar aprobación; en coautor/mixto, F1 espera la aprobación de los anversos corregidos.

1. **F1 Plan (orquestador).** Sílabo del caso → resultado de aprendizaje; ediciones (§4 del protocolo) y discrepancias; principios (P1), irreducibles (P6), contrastes (P7), escalas (P10); cribado de alto rendimiento (MIR verificado por el orquestador); cálculo P11 con deuda; rango de IDs desde el registro; qué tarjetas llevan mnemotecnia establecida o esquema; `meta.guia` (principios, palabras clave, imágenes para oclusión, preguntas de cierre, relación subtema→sílabo, fechas, referencias). Plan por tarjeta:
   ```json
   {"id": "Q2R2-TOX-0001", "tipo": "QA", "clase": "Principio", "nivel": "Aplicacion", "bloom": "Comprender",
    "subtema": "Abstinencia", "objetivo": "Explicar el rebote de la abstinencia alcohólica",
    "fuente_prevista": "Goodman & Gilman 14.ª ed.", "alto_rendimiento": ["USMLE"],
    "mnemotecnia": null, "esquema": "tabla intoxicación vs. abstinencia", "anverso_usuario": null, "semilla": null}
   ```
2. **F2 Redacción (ejecutor).** Recibe plan + §3 + §6 + ejemplos (§7) y devuelve el JSON de tarjetas (§5, esquema). No añade ni quita IDs (propuestas en `notas_ejecutor`). **Ante un dato dudoso no escribe marcas en la tarjeta**: lo añade a `pendientes` (`{"dato": texto exacto, "campo": "razonamiento", "fuente_esperada": "guía | PubMed | ficha técnica | libro §4"}`) y redacta el resto. No inventa referencias, PMID, DOI, ediciones, años ni tags MIR.
3. **F3 Lint + rúbrica (orquestador).** `python3 kit/anki/compilar_mazo.py <json> --solo-lint` (esquema, IDs, tags, lista blanca HTML, límite de marcas, cloze, cuotas…); con `pendientes` aún abiertos, el lint falla solo por eso y por lo demás debe estar limpio. Rúbrica por tarjeta: P3, P2, P8, exactitud clínica, alineación con `objetivo`, trazabilidad al sílabo, uso correcto de las clases de color (§6), calidad de mnemotecnia/esquema. Salida: `id → regla → corrección exigida`.
4. **F3c Corrección (ejecutor).** Corrige solo los IDs listados y devuelve el JSON completo. Bucle F3→F3c hasta cero defectos o 2 vueltas; si persisten, el orquestador corrige lo trivial o elimina la tarjeta. Nunca se compila con defectos de exactitud.
5. **F4 Verificación obligatoria en cascada (ejecutor capaz, sin tope de datos).** Sobre **todos** los `pendientes` y además sobre toda cifra, dosis, umbral, criterio y cita de `Fuente` del mazo. Cascada por dato, hasta 2 búsquedas por fuente: **PubMed** (`search_articles`, `lookup_article_by_citation`, `get_article_metadata`) → **Consensus** (`search`) → **fichas técnicas** (DailyMed, CIMA-AEMPS, EMA, ARCSA) → **GPC/lineamientos MSP Ecuador** (salud.gob.ec) → **web/guías de sociedades**. Si un dominio está bloqueado por la red, pide habilitarlo antes de darlo por perdido. Resultado por dato:
   - **confirmado** → cita en `Fuente` (forma corta `Autor Año, Revista (PMID n)`) y en `meta.guia.referencias` (Vancouver completa);
   - **contradicho** → se corrige con la fuente hallada;
   - **divergente** → ambas cifras, cada una con su cita;
   - **sin confirmar** → se elimina el dato o la tarjeta, o se reformula cualitativamente. Nunca queda marca.
   El verificador devuelve `[{"id", "dato", "resultado", "correccion", "cita", "pmid_doi", "url"}]`; no inventa PMID/DOI/ediciones; UpToDate/DynaMed solo con `[citado AAAA mmm dd]` real. El orquestador aplica, vacía `pendientes` y rellena `meta.verificacion = {"total": M, "verificados": N, "eliminados": [{"id", "dato", "motivo"}]}`.
6. **F5 Re-lint y rúbrica** de las tarjetas tocadas por F4 (un dato corregido puede romper P3 o el límite de 2 frases). El lint completo debe dar `RESULTADO: lint OK`.
7. **F6 Compilación.** `python3 kit/anki/compilar_mazo.py mazos/<tema>/tarjetas.json` → `.apkg` + inspección + registro actualizado. Aborta ante cualquier marca, `pendientes` no vacío o error.
8. **F7 Previsualización.** `node kit/anki/previsualizar.js mazos/<tema>/tarjetas.json <scratchpad>/capturas_<tema> 8`; mira tú las capturas (al menos una QA con esquema y un cloze, en iPhone noche) y corrige desbordes o tablas ilegibles. Las capturas no se versionan.
9. **F8 Guía.** `python3 kit/anki/guia_docx.py mazos/<tema>/tarjetas.json`. Revisa que `meta.guia` tenga principios, palabras clave, preguntas de cierre, subtemas y referencias verificadas.
10. **F9 Auditoría y entrega** (§9). Commit de `tarjetas.json`, `media/`, `.apkg`, `.docx` y `mazos/README.md` juntos.

---

# 5 · Esquema del JSON (`mazos/<tema>/tarjetas.json`)

```json
{"meta": {"caso": "Toxicodependencias", "rotacion": "2.ª", "tag_raiz": "Toxicodependencias", "prefijo": "Q2R2-TOX",
          "version": "1.0", "fecha": "AAAA-MM-DD", "resultado_aprendizaje": "…", "fuente_alcance": "Sílabo 2.ª rotación, Caso …",
          "justificacion_exceso": "", "mir_verificados": [],
          "verificacion": {"total": 0, "verificados": 0, "eliminados": []},
          "guia": {"principios": [], "palabras_clave": [], "imagenes_oclusion": [], "preguntas_cierre": [],
                   "subtemas": {"Abstinencia": "relación con el sílabo"}, "fechas": {"apertura": null, "cierre": null, "examen": null},
                   "referencias": ["Vancouver completa…"]}},
 "tarjetas": [
  {"id": "Q2R2-TOX-0001", "tipo": "QA", "pregunta": "…", "respuesta": "…", "razonamiento": "…",
   "mnemotecnia": "", "esquema": "", "fuente": "…", "tags": ["…"], "pendientes": [], "notas_ejecutor": ""},
  {"id": "Q2R2-TOX-0004", "tipo": "Cloze", "text": "…{{c1::…}}…", "extra": "…",
   "mnemotecnia": "", "esquema": "", "fuente": "…", "tags": ["…"], "pendientes": []}]}
```

- Media (SVG/PNG del esquema) en `mazos/<tema>/media/`, nombre `<prefijo-en-minúsculas>-<nnnn>-<tema>.svg` (sin espacios, no empieza por `_`).
- **Tags** (sin espacios ni tildes): exactamente uno de `Quirurgica2::<TagRaíz>::<Subtema>`, `Nivel::<Recuerdo|Aplicacion>`, `Fuente::<Abrev>`, `Clase::<Principio|Aplicacion|Vineta|Contraste|Relacional|Irreducible|Escala>`, `Bloom::<Recordar|Comprender|Aplicar|Analizar|Evaluar>`; opcionales `Principio` (solo clase Principio), `Escala::<Nombre>`, `AltoRendimiento::<USMLE|MIR>`, `MIR::<AAAA>-<NNN>` (verificado), `Origen::<Usuario|Claude>`. La raíz `Quirurgica2` se conserva en ambas rotaciones.
- **El compilador valida**: esquema y claves; formato y unicidad de IDs (GUID = `guid_for(id)`), prefijo contra el registro (y retirados); tags; lista blanca HTML; ≤4 marcas semánticas por campo (Esquema exento); `.tema` único al inicio del anverso; **cero marcas** de verificación en campos, tags y `meta` (salvo `meta.verificacion`); metatexto; `pendientes` vacío; cloze bien formado (c1… contiguos, sin anidar, span dentro del hueco); `Fuente` no vacía; Respuesta ≤2 frases; listas abiertas; cifras de S/E/VPP/VPN/LR/AUC; mnemotecnia expandida; tablas ≤4 columnas y ≤9 filas con cabecera; media existente; cuotas (Cloze ≤15 %, Recuerdo ≤40 %, subtema ≤8, N>45 con justificación). `--demo` (con `meta.demo: true`, fuera de `mazos/`) convierte las cuotas en avisos y no toca el registro.

---

# 6 · Diseño visual («A · Chips clínicos»)

Fondo gris muy claro (casi negro en noche), acento índigo, respuesta en recuadro con borde izquierdo índigo, razonamiento debajo, bloques **Mnemotecnia** (borde rosa) y **Esquema** (tabla o diagrama) solo si el campo tiene contenido, y `Fuente` al pie. Tipografía del sistema. Contraste WCAG AA comprobado en claro y noche (texto/fondo ≥5,6:1 en todas las píldoras).

**El color significa tipo de dato, igual en todos los mazos:**

| Clase | Tipo de dato | Cuándo usarla | Ejemplo |
|---|---|---|---|
| `.fx` (violeta) | fármaco | nombre de fármaco o grupo | `<span class="fx">tiamina</span>` |
| `.num` (azul, cifras tabulares) | cifra, dosis, umbral | el número que decide conducta | `<span class="num">≥ 2 de 11</span>` |
| `.al` (rojo) | signo de alarma | lo que no se puede pasar por alto | `<span class="al">convulsión</span>` |
| `.dx` (verde) | diagnóstico / entidad | la entidad que es la respuesta o el contraste | `<span class="dx">delirium</span>` |
| `.mec` (ámbar) | mecanismo | el eslabón fisiopatológico clave | `<span class="mec">rebote GABA/NMDA</span>` |
| `.mne` (rosa, cursiva) | mnemotecnia | solo dentro del campo Mnemotecnia | `<span class="mne">CAGE</span>` |
| `.vs` (índigo) | contraste | rótulo «Contraste» / «vs.» en el razonamiento | `<span class="vs">Contraste</span>` |
| `.tema` (versalitas índigo) | sujeto | una vez, al inicio del anverso | `<span class="tema">Abstinencia alcohólica</span>` |

Reglas: marca solo lo que el estudiante debe recuperar (≤4 marcas por campo; lo ideal 1–3); no marques palabras sueltas sin valor; el anverso casi nunca lleva marcas aparte de `.tema` (delatarían la respuesta, P3). En cloze la marca va **dentro** del hueco: `{{c1::<span class="num">12 meses</span>}}`. Etiquetas permitidas: `span` (con una clase de la tabla), `b`, `strong`, `i`, `em`, `br`, `sub`, `sup`; en Mnemotecnia además `ul/li`; en Esquema además `table/caption/thead/tbody/tr/th/td` (`colspan`, `rowspan`, `scope`), `ul/ol/li` e `img` (`src`, `alt`). Nada de `style=`, clases inventadas, scripts ni enlaces; el texto se escapa (`<`, `>`, `&` literales son seguros).

**Mnemotecnia** (campo opcional). Solo si existe una **establecida y popular** (inglés o español; se prioriza la más usada: CAGE, MUDPILES, etc.); no inventes acrónimos forzados; si no hay una buena, el campo queda vacío. Siempre **expandida**: una `<span class="mne">` con la mnemotecnia, idioma entre paréntesis si es inglesa, y `<ul><li><b>L</b> significado</li>…</ul>` (≥2 ítems). La mnemotecnia sirve para listas genuinamente arbitrarias; no sustituye al principio (si hay principio, la tarjeta pregunta el principio).

**Esquema** (campo opcional). Cuando el tema lo pide: contrastes de 3+ rasgos, clasificaciones, cronologías, algoritmos cortos. Tabla HTML de ≤4 columnas y ≤9 filas, celdas breves (2–5 palabras), primera columna `<th>` con el rasgo. O diagrama SVG en `media/` con fondo transparente, colores de la paleta clara y texto ≥12 px en un viewBox de ~360 px de ancho (en noche Anki lo verá invertido con `invert(1) hue-rotate(180deg)`, igual que hace con los dibujos). El esquema complementa: la respuesta debe poder producirse sin mirarlo.

---

# 7 · Ejemplos calibrados (formato JSON real; datos verificados)

**✅ Principio · QA**
```json
{"id": "Q2R2-TOX-0001", "tipo": "QA",
 "pregunta": "<span class=\"tema\">Abstinencia alcohólica</span>¿Por qué un depresor, al suspenderse, deja temblor, taquicardia y convulsiones?",
 "respuesta": "Porque el consumo crónico <span class=\"mec\">regula a la baja GABA-A y al alza NMDA</span>; sin etanol queda un cerebro hiperexcitable.",
 "razonamiento": "El rebote noradrenérgico da temblor, sudoración y taquicardia; el extremo es <span class=\"al\">convulsión</span> y <span class=\"al\">delirium tremens</span>.<br><span class=\"vs\">Contraste</span> la intoxicación deprime el SNC; la abstinencia da los signos opuestos.",
 "fuente": "Goodman &amp; Gilman 14.ª ed. 2023",
 "tags": ["Quirurgica2::Toxicodependencias::Abstinencia", "Nivel::Aplicacion", "Fuente::GoodmanGilman", "Clase::Principio", "Bloom::Comprender", "Principio"]}
```

**✅ Irreducible con mnemotecnia establecida · QA**
```json
{"pregunta": "<span class=\"tema\">Tamizaje de alcohol</span>¿Qué cuestionario de cuatro preguntas usas en consulta y qué explora cada una?",
 "respuesta": "El <span class=\"dx\">CAGE</span>: explora intentos de reducir, molestia por la crítica, culpa y consumo matutino.",
 "razonamiento": "Es un tamizaje: un resultado positivo orienta a evaluar el consumo, no establece el diagnóstico.",
 "mnemotecnia": "<span class=\"mne\">CAGE</span> (inglés)<ul><li><b>C</b> Cut down: ¿has sentido que debes reducir?</li><li><b>A</b> Annoyed: ¿te molesta que critiquen tu consumo?</li><li><b>G</b> Guilty: ¿te has sentido culpable?</li><li><b>E</b> Eye-opener: ¿bebes al despertar?</li></ul>",
 "fuente": "Ewing 1984, JAMA (PMID 6471323)"}
```

**✅ Contraste con esquema · QA**
```json
{"pregunta": "<span class=\"tema\">Confusión en el adulto mayor</span>¿Qué dato de la historia separa mejor el delirium de la demencia?",
 "respuesta": "El curso: el <span class=\"dx\">delirium</span> es de inicio agudo y fluctuante, con la <span class=\"mec\">atención</span> afectada primero.",
 "razonamiento": "La demencia avanza en meses o años con la atención conservada hasta fases tardías. Un cambio agudo sobre una demencia de base es delirium sobreañadido: busca el desencadenante.",
 "esquema": "<table><thead><tr><th>Rasgo</th><th>Delirium</th><th>Demencia</th></tr></thead><tbody><tr><th>Inicio</th><td><span class=\"al\">Agudo</span></td><td>Insidioso</td></tr><tr><th>Curso</th><td>Fluctuante</td><td>Progresivo</td></tr><tr><th>Atención</th><td>Alterada desde el inicio</td><td>Conservada al inicio</td></tr></tbody></table>",
 "fuente": "Inouye 2014, Lancet (PMID 23992774)"}
```

**✅ Convención no derivable · Cloze**
```json
{"tipo": "Cloze",
 "text": "<span class=\"tema\">Trastorno por consumo de sustancias · DSM-5-TR</span>Se diagnostica con {{c1::<span class=\"num\">≥ 2 de 11</span>}} criterios en un periodo de {{c2::<span class=\"num\">12 meses</span>}}.",
 "extra": "Tolerancia y abstinencia no cuentan si aparecen bajo tratamiento médico supervisado.",
 "fuente": "APA, DSM-5-TR 2022"}
```

**✅ Cloze con diagrama** — `"esquema": "<img src=\"q2r2-tox-0004-wernicke.svg\" alt=\"Déficit de tiamina y tríada de Wernicke\">"`, con `text` = «…déficit de {{c1::<span class=\"fx\">tiamina</span>}}, que se repone {{c2::antes de la glucosa}}…» (Sechi 2007, Lancet Neurol, PMID 17434099).

**✅ Relacional (P12), sin cifras** — `<span class="tema">Abdomen agudo</span>Peritonitis difusa en la exploración y TC no concluyente: ¿qué pesa más para indicar cirugía y por qué?` → «La exploración: la peritonitis difusa indica cirugía aunque la imagen no sea concluyente.»

**❌ A evitar**

| Tarjeta | Falla |
|---|---|
| `¿Qué es la flegmasia cerúlea dolens?` | definición aislada que un principio explica (P1) |
| `La sensibilidad del CAM es {{c1::…}}` | valor operativo (P9) |
| `¿Cuáles son las causas de ojo rojo?` | lista abierta (P9) |
| `<span class="num">{{c1::12 meses}}</span>` | marca fuera del hueco (§6) |
| `<span class="fx">GABA</span>, <span class="mec">NMDA</span>, … (6 marcas)` | saturación (≤4) |
| `Mnemotecnia: «TIAMINA» = …` inventada | mnemotecnia forzada (§6) |
| `El widget de alcohol cita 12 meses…` | metatexto (prohibido) |
| cualquier `[VERIFICAR EN FUENTE]` o «pendiente» | cero marcas: el compilador aborta |

---

# 8 · Personalización de Anki (lo verificado)

- El reviewer **no invierte colores** en modo noche: añade `nightMode` y `night_mode` a `<body class="card …">`. Por eso todo color sale de variables en `.card` redefinidas en `.card.nightMode, .card.night_mode`; un `style=` en línea quedaría ilegible de noche (y el lint lo rechaza).
- Las clases de plataforma (`ipad`, `iphone`, `mobile`, `win`, `mac`) van en `<html>`, no en `.card`: el CSS usa `@media (max-width: 480px)` para el iPhone.
- Cloze: Anki genera `<span class="cloze">` (hueco activo) y `.cloze-inactive` (los demás huecos, visibles). La marca semántica va dentro del hueco para que el estilo sobreviva; el hueco activo se subraya en índigo.
- `<hr id=answer>` es el ancla a la que Anki desplaza al voltear: no la quites.
- Imágenes en media: el reviewer limita `img` a `max-width: 100%`. Prueba el primer SVG de cada mazo en el iPad; si un dispositivo no lo muestra, exporta el diagrama a PNG con el mismo nombre base. Los archivos que usa la plantilla (no los campos) deben empezar por `_`; los de campos, no.
- genanki: `Model(id, nombre, fields, templates, css, model_type=CLOZE)`, `Note(guid=guid_for(id))`, `Package.media_files`; tags sin espacios. **Cambiar campos o plantillas de un modelo ya importado impide actualizar** las notas: para cambios estructurales, modelo nuevo con ID nuevo (registrado en `mazos/README.md`). Retocar solo el CSS no cambia el esquema del modelo; si una reimportación no lo aplica, pégalo en Tipos de nota → Tarjetas → Estilo.
- No se puede: fuentes remotas, JavaScript fiable entre plataformas, ni depender de clases de plataforma en `.card`.

---

# 9 · Auditoría final (muéstrala antes de entregar)

| Métrica | Valor |
|---|---|
| Modo · rango de IDs · ID de mazo · versión | |
| Total / cálculo P11 · deuda (N × ~5) | |
| % Recuerdo (≤40) / % Aplicación · % Cloze (≤15) · máx. subtema (≤8) | |
| Principio · Viñeta/Relacional · % Bloom ≥Analizar · escalas por nivel · pares de contraste | |
| Mnemotecnias (cuáles) · esquemas (tablas / SVG) | |
| Alto rendimiento: USMLE / MIR patrón / MIR verificados (año-número + URL) | |
| **Verificación:** «Verificados N de M; eliminados K: …» (de `meta.verificacion`) · marcas restantes: 0 | |
| Discrepancias sílabo–protocolo (ediciones) · fuente del alcance · semilla del widget (sí/no) | |
| Vueltas F3→F3c · defectos residuales · lint/compilación (`RESULTADO`) · capturas revisadas | |

- [ ] ¿Cada tarjeta pasa P3 y ningún Recuerdo es derivable de un principio?
- [ ] ¿Sujeto primero, Respuesta ≤2 frases, Razonamiento ≤~4?
- [ ] ¿Colores usados según su tipo de dato, ≤4 por campo, sin delatar la respuesta en el anverso?
- [ ] ¿Mnemotecnias establecidas y expandidas; esquemas legibles en iPhone noche?
- [ ] ¿Cero marcas, `pendientes` vacíos, todas las cifras con cita confirmada?
- [ ] ¿`mazos/README.md` actualizado y commit de JSON + media + .apkg + .docx juntos?

**Entrega:** `mazos/<tema>/Quirurgica2_<TagRaíz>.apkg` + `Guia_<TagRaíz>.docx` como archivos, la auditoría y la línea de verificación. La guía ya incluye importación, configuración (FSRS, retención 0,90, nuevas/día, repasos 9999, sanguijuelas), código de colores, cómo responder y calificar, calendario respecto a la tutoría y al examen, mapa del mazo y referencias de aprendizaje verificadas.

**Fundamentos.** Recuperación y práctica distribuida: utilidad alta (Dunlosky 2013); elaboración e intercalado: moderada; palabra clave mnemotécnica: baja en general, útil para listas arbitrarias. Palmerton y Sung (educadores) son heurística, no evidencia. Límite honesto: las tarjetas construyen base declarativa y discriminación; la transferencia al razonamiento clínico integrado es limitada y se complementa con casos completos.
