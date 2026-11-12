---
name: "widget-ensenanza"
description: "Genera un widget HTML de estudio médico (v11) sobre cualquier tema: modo mono (1–2 entidades) o multi (3–5 con presentación común). Regla 20/80 con núcleo por pestaña, perlas por examen (PUCE, CACES, USMLE, MIR, ENARM), ejercicio de ordenar pasos, diseño tipo app, kit v11 y cero marcas de verificación."
---

# Widget de enseñanza médica — v11

v11 respecto a v10.2: propósito 20/80 con `div.nucleo` por pestaña y perlas etiquetadas por examen, visión de conjunto con filas-pregunta, ejercicio «Ordenar» (sustituye los modos en blanco), diagramas solo donde aclaran, diseño tipo app con acento por tema y kit propio en `kit/v11/`. Fuente de las decisiones: `docs/DECISIONES_v11.md`.

## 0 · Propósito y entrada

**Propósito.** El widget condensa muchas fuentes. Primero rige la **regla 20/80**: el 20 % de la información que hace entender el otro 80 %. Sobre esa base va lo específico que se toma en exámenes: **Examen Integral PUCE, habilitación CACES (Ecuador), USMLE Step 1 y Step 2 CK, MIR (España) y ENARM (México)**, más los requisitos del sílabo cuando el tema está en él. **No se recorta: se reordena** (núcleo arriba, detalle completo debajo). Sin preguntas de práctica de opción múltiple: eso va en Anki.

**Entrada.** `Widget v11 · Tema: … · Modo: mono|multi · Enfoque: … · Guía: … · Bibliografía: … · Contexto local: … · Adjuntos: …`

Solo `Tema` es obligatorio; si falta, pregunta solo por él y detente. Valores por defecto, declarados en el manifiesto: enfoque equilibrado; guía = la internacional vigente más específica (sociedad, año) más la GPC del MSP si existe; contexto Ecuador (MSP, GPC, INEC, Quito ~2 850 m) solo con datos sostenibles; adjuntos = fuente prioritaria (un widget HTML adjunto activa el modo edición, §12.7).

**Sílabo (alcance).** Ubica el tema en un caso de `fuentes/syllabus_quirurgica2.md` (1.ª rotación) o `fuentes/syllabus_quirurgica2_segunda_rotacion.md` (2.ª). Busca con `grep -n` el encabezado del caso y lee **solo esa sección** y la «Bibliografía»; de ahí salen alcance, subtemas y entidades candidatas. **Si el tema no está en el sílabo: «sin sílabo»**, declarado en el manifiesto; el alcance sale de las guías vigentes y de los temarios de los exámenes objetivo, y la bibliografía de la tabla de ediciones (§10). Si el sílabo trae una edición inexistente o equivocada (p. ej. «Farreras-Rozman 22.ª ed.»; la vigente es la 20.ª ed. 2024), usa la de `fuentes/protocolo_verificacion.md` § 4 y decláralo como discrepancia (§7.12).

## 1 · Arranque (una llamada)

Solo existe la ruta del repo (`kit/` en el directorio de trabajo); si falta, dilo y detente. No leas los archivos del kit; solo ejecútalos. Sigue `CLAUDE.md`.

- Partes en `widgets/<tema>/<id>/` y `manifiesto.json` con `titulo`, `salida` (`"../<Nombre>_widget_v11.html"`), `tipo: "v11"` y `tema` (acento, §7.17).
- Construir (ensambla y valida; imprime errores y `RESULTADO`): `python3 kit/construir.py widgets/<tema>/<id>`.
- Probar: `node kit/v11/probar.js file://$PWD/<html> <carpeta_capturas_en_scratchpad>`; revisa capturas en 390, 820, 1180 y 1440 px.
- Referencias: `python3 kit/renumerar.py` renumera Vancouver por primera aparición (§10).
- Kit en `kit/v11/` (`head.html`, `script.html`, `validar.py`, `probar.js`). Los widgets sin `"tipo": "v11"` usan el kit v10.2 (legado) y no se tocan.
- Un tema nuevo lleva `PLAN.md` y fila en `README.md`; en un tema existente, lee su `PLAN.md` antes de añadir o reordenar pestañas.
- De skills de frontend o artefactos del entorno solo aplican rutas y entrega.

## 2 · Paso 0 · Router

- **Entidad** = diagnóstico con mecanismo propio **y** manejo propio. Subtipos, estadios y formas clínicas de una enfermedad van en su tabla de subtipos.
  - Mal: «Colecistitis litiásica y alitiásica» = 2 entidades. Bien: 1 entidad con 2 subtipos.
  - Mal: «Trastorno depresivo mayor leve y grave» = 2 entidades. Bien: 1 entidad con 2 grados de gravedad. Bien: delirium y demencia = 2 entidades (mecanismo y manejo propios).
- Tema = presentación sin entidades («Síndrome confusional en el adulto mayor», «Lesiones dérmicas»): elige 3–5 por frecuencia y letalidad en ese terreno, preferentemente las del sílabo, y decláralas.
- 1–2 entidades → **mono**. Segunda entidad: si es otra fase de un mismo proceso (TVP/TEP), en la pestaña adicional; si es un diferencial, en «No confundir con…».
- 3–5 que **comparten una presentación de entrada** ante la que hay que discriminarlas → **multi**; sin presentación común → propone widgets mono separados y **detente**.
- ≥6 → propone la partición mínima en widgets válidos (mono o multi; pueden ser más de 2), con el porqué, y **detente**.
- `Modo: mono|multi` gana siempre (override), salvo `Modo: multi` con <3 entidades: aplica mono y escribe `Override: rechazado`.
- **Principal** = `e1`: la más frecuente en el terreno clínico del caso; si es diagnóstico de exclusión, la de conducta más decisiva. Ordena `e2…eN` por el eje del grupo (benigna → grave o proximal → distal), declarado.
- **Amenaza** = la que, no reconocida, causa antes muerte o secuela irreversible evitable. Si no es `e1`, sus pasos `Alarma` y `Evita` son obligatorios y su bandera abre el `hb ro` de `vis`.
- Primera línea del manifiesto: `Modo: … · Entidades: e1=… (principal), e2=… · Amenaza: eK · Override: sí|no|rechazado` (mono: `e1=<Tema>`, `e2=` si hay segunda, `Amenaza: —`).

## 3 · Parámetros por modo

«Pestaña de contenido» = toda salvo `pan`.

| Parámetro | mono | multi |
|---|---|---|
| Pestañas (orden de barra) | `pan def fis cli dx tx seg` + ≤1 adicional | `pan vis e1 … eN sin` (N 3–5) |
| Partes | `01_nav 02_pan 10_def 11_fis 12_cli 13_dx 14_tx 15_seg [16x_clave] 90_sim` | `01_nav 02_pan 05_vis 21_e1 … 2N_eN 80_sin 90_sim` |
| Ids · enlace | `m-n` · `s-n`: `ir('fis','m-3')` · `ir('cli','s-2')` | `eK-m-n` · `eK-s-n` (desde 1 en cada entidad): `ir('eK','eK-m-3')` |
| Timeline `ol.tl` | `fis` | cada `eK`, bajo «Cadena» |
| `.signo` · `.qv` | `cli` · opcional, solo en `cli` | «Qué verás» de cada `eK` · obligatoria, una |
| `ol.steps.tg` | inicio de `dx` y de `tx` | `vis` (dx); inicio de «Diagnóstico» y «Tratamiento» de cada `eK` |
| `span.rem` posología · S/E | `↪ Posología en «Plan de tratamiento»` · `↪ Propiedades en «Plan diagnóstico»` | `↪ Posología en «Tratamiento»` · `↪ Propiedades en «Diagnóstico»` |
| Sustrato normal · `Alcance` · Sílabo | `def` | lo común en `vis`; lo propio en «Qué es» |
| `.acc.refs` | al final de `seg` | al final de `sin` |
| PG | 3–5 por pestaña de contenido | `vis` 3–5 · `e1` 3–5 · secundarias 3 · `sin` 0 |
| `div.nucleo` | 1 por pestaña de contenido (3–5 `li`) | 1 en `vis`, 1 en cada `eK` (3–5 `li`); `sin` 0 |
| Feynman | 1 por segmento cardinal; `def` exactamente 1; en `cli` solo si su mecanismo no tiene ya Feynman en `fis`; ≈8 en total | `e1` exactamente 2 (tras «Cadena» y tras «Qué verás») · secundarias exactamente 1 (tras «Cadena») · `vis` y `sin` 0 |
| Simuladores | 1 al final de `dx`, `tx` y `seg` | `vis` 1 (diferencial) · `e1` bajo «Diagnóstico» y «Tratamiento» (+«Seguimiento» opcional) · secundarias ≥1 bajo «Tratamiento» |
| Ordenar | `ol.tl` de `fis`, `ol.steps.tg` de `dx` y de `tx` | `ol.tl`, dx y tx de cada `eK` (+ dx de `vis`) |
| Núcleo Anki (`nucleo` del manifiesto) | ≤12 (lista) | `vis` ≤5 (los ejes) + ≤7 por entidad |
| Presupuesto | ≈16 llamadas | ≈21 llamadas |

## 4 · Rol y tarea

Eres médico especialista del tema, magíster en Educación Universitaria y experto en ABP. Escribes para un estudiante de 10.º nivel de Medicina (PUCE, Salud Integral Hospitalaria 2, iPad, Examen Integral) que también se prepara para CACES, USMLE, MIR y ENARM. Produce **un único widget HTML autocontenido**, sin recursos externos, que funcione sin internet. El repaso espaciado va en Anki: sin tarjetas ni preguntas de práctica.

**Adaptación por área.** Si el tema es psiquiátrico, geriátrico o dermatológico: «Qué verás» puede ser el examen mental, la valoración geriátrica integral o la lesión elemental y su distribución; los «signos» usan las maniobras equivalentes (escalas y pruebas de cribado, signos de la exploración mental, signos cutáneos como Nikolsky o la dermatoscopia) con su mecanismo; la «cadena» puede ser neurobiológica, de fragilidad multisistémica o inmunológica/cutánea; en toxicodependencias, intoxicación, abstinencia y trastorno por consumo son fases de la misma entidad o entidades según su manejo propio. Los umbrales de escalas (MoCA, CAM, GDS, PHQ-9, GAD-7…) exigen `[n]`.

## 5 · Precedencia

Si dos reglas chocan, gana la de número menor; declara el conflicto en la línea de aviso.

1. **Veracidad.** No inventes fuentes, ediciones, años, PMID, DOI, URL, cifras, umbrales ni dosis. Aplica `fuentes/protocolo_verificacion.md`. **El widget entregado no lleva ninguna marca `[VERIFICAR EN FUENTE]` ni badge «Fuente por verificar»**: antes de quitar un dato se agotan las fuentes (§6); si tras agotarlas no se confirma, se elimina el dato o se reescribe sin la cifra. Toda celda Ref. lleva un `[n]` real.
2. **Restricción de simuladores** (§7.10).
3. **Integridad de salida.** Nada truncado, resumido ni sustituido por marcadores. Concisión ≠ recorte: cada idea una vez, con su porqué, sin eliminar datos.
4. **Contratos de cobertura:** PG, Panorama y enlaces `m ↔ s`.
5. **Resto de esta skill.**
6. **Skills del entorno**, solo en sus restricciones técnicas.

## 6 · Presupuesto de herramientas

- **Web (guías):** por guía rectora (máx. 2), ≤3 búsquedas (`<guía> <sociedad> latest version`) y 1 lectura; ni cifras sueltas ni imágenes.
- **Verificación (agotar fuentes; cero marcas al entregar):** mientras redactas no busques dato por dato; anota en la lista `pendientes` el dato (texto exacto, pestaña, tipo de fuente) y no lo dejes en el widget como marca. Con el borrador completo, pasa por **todas** las fuentes para cada pendiente, en este orden: (1) PubMed (`search_articles`, `lookup_article_by_citation`, `get_article_metadata`); (2) Consensus (`search`); (3) fichas técnicas oficiales: DailyMed (`dailymed.nlm.nih.gov`), CIMA-AEMPS, EMA, ARCSA; (4) GPC, lineamientos y protocolos del MSP (`www.salud.gob.ec`, descarga y lectura del PDF); (5) guías de sociedades y web. Hasta 2 búsquedas por dato y fuente; sin tope de datos. Si un dominio está bloqueado por la red de la sesión, pide habilitarlo antes de darlo por perdido. Delegable a subagentes `haiku`, pero el orquestador comprueba en el texto fuente los datos que cambian conducta (dosis, umbrales, plazos). Resultado: confirmado → añade la referencia Vancouver (PMID/DOI solo si la herramienta los devolvió); contradicho → corrige con la fuente; fuentes divergentes → muestra ambas cifras con su cita; sin confirmar tras agotarlas → elimina el dato o reescribe sin la cifra. Los libros de la tabla de ediciones se citan sin búsqueda; uno fuera de la tabla se verifica antes de citarlo. Cuenta verificados (N), corregidos (C) y eliminados (X) de M pendientes para la línea de aviso. Rige igual para definiciones y apertura.
- **Escritura:** una llamada por parte; `manifiesto.json` va con la primera, `01_nav` con `90_sim`.
- **Correcciones:** edición puntual (Edit); nunca reescribas una parte para corregir una línea.
- No muestres código en el chat ni releas partes salvo para corregir un error del validador.

**Orquestación (solo si hay subagentes).** El orquestador fija router, `PLAN`, manifiesto y la numeración global de referencias `[n]` (primera aparición por orden de barra), y reparte partes. Ejecutores `sonnet`: cada uno escribe una o dos entidades (o pestañas) con las reglas de esta skill y su tramo de numeración. `haiku`: pasada de verificación y tareas mecánicas (conteos, enlaces, formato Vancouver). El orquestador revisa el trabajo y ejecuta construir/probar. Sin subagentes, haz todo en secuencia.

## 7 · Componentes comunes

Ubicaciones, ids, conteos y remisiones: §3.

**7.1 Temas rectores.** Antes de cada pestaña de contenido, fija un tema rector por PG: idea organizadora de la que se deducen varios datos. Gobiernan PG, núcleo, segmentos y Feynman; no se muestran.
- Mal: «El signo de Blumberg indica irritación peritoneal». Bien: «El patrón temporal del dolor refleja qué capa peritoneal está comprometida».
- Mal: «El delirium cursa con inatención». Bien: «La falla de atención es el eje que separa el delirium (agudo, fluctuante) de la demencia (crónica, memoria)».

**7.2 Orden fijo de cada pestaña de contenido.** (1) Preguntas guía → (2) Núcleo → (3) Detalle completo, ordenado por relevancia → (4) perlas de examen junto al tema que tocan.

**7.2a Preguntas guía (PG).**
- `hb-t` literal `Preguntas guía — qué debes poder responder al terminar esta pestaña`. Es la **primera caja** de cada pestaña de contenido (en `eK`, tras «Frente a…»); sin highlight previo.
- Abiertas (por qué, cómo, qué diferencia, qué cambia si, en qué se apoya); sin sí/no, trivia, epónimos ni cifras.
- Cada PG se responde entera con su pestaña (y sus enlaces); si no, completa o elimínala. Sin bloques de «respuesta».
- ≥1 PG de la pestaña de signos exige explicar un signo por su mecanismo.

**7.2b Núcleo (`div.nucleo`, el 20 %).** Inmediatamente tras las PG: `div.nucleo>div.nucleo-t{Núcleo}+ul>li` con 3–5 `li` de ≤35 palabras que explican el resto de la pestaña: el mecanismo central, el dato que lo delata, la conducta decisiva. Cada idea con su `[n]` si lleva dato. Todo lo que dice el núcleo se desarrolla en el detalle; el detalle no se recorta por existir el núcleo. No lo confundas con la lista `nucleo` del manifiesto (§7.13, para Anki).

**7.2c Perlas de examen (`aside.perla`).** `aside.perla[data-ex="…"]>div.perla-t{Perla de examen}+p{dato con [n]}`, colocada junto al tema que toca, nunca agrupada al final; ni en `pan` ni en `sin`. Solo datos que cambian razonamiento, conducta o sospecha, o que se piden de forma típica; no se afirma frecuencia de preguntas. `data-ex` lleva una o varias etiquetas de `puce caces usmle1 usmle2 mir enarm`, con **criterio fijo por tipo de dato**:
- mecanismo, fisiología, farmacología básica, anatomía → `usmle1`;
- conducta clínica, diagnóstico y tratamiento según guías internacionales → `usmle2 mir enarm`;
- dato de una GPC, lineamiento o norma del MSP del Ecuador → `caces`;
- contenido nombrado en el sílabo del caso → `puce` (solo si el tema está en el sílabo; sin sílabo, nunca `puce`).
Un dato puede llevar varias etiquetas si cumple varios criterios. El kit las muestra como chips y ofrece un filtro global por examen.

**7.3 Panorama (común).** Solo priming: no introduce contenido nuevo. Sin PG, núcleo, perlas de examen, Feynman ni simuladores. ≤900 palabras. **Se escribe al final.**
- Etapa: `h3`, `p.res` 70–110 palabras con la lógica de su destino (conclusiones, no detalle) y puente a la siguiente (salvo la última), `p.perla` ≤20 palabras, botón `Ir a [pestaña] →`.
- Perla del Panorama: cambia el razonamiento, la conducta o la sospecha, o separa dos entidades confundibles. No repite el párrafo; sin posología ni propiedades; un epónimo sin función decisional no es perla.
- Cierre literal en `p.mini`: `Esto es el mapa, no el territorio: cada párrafo y cada perla se justifican en su pestaña.`
- Contrato inverso: lo que no se desarrolle en su destino, escríbelo allí o elimínalo.

**7.4 Feynman.**
- Va tras su segmento cardinal (el que desarrolla un tema rector) y su `ol.tl`, fuera de acordeón.
- Cuerpo ≤90 palabras, lenguaje cotidiano, ≤1 analogía honesta; si no existe, en llano.
- `En medicina esto se llama…` (U+2026): términos y sigla. `Dónde falla la comparación:` el límite de la analogía.
- Prohibido en el cuerpo: dosis, cifras, umbrales, siglas, guías, escalas; analogía que contradiga el mecanismo; tono infantil, emojis, paráfrasis del técnico, relleno.

**7.5 Timeline y profundidad por nodo.**
- Cadena causa-efecto: cada nodo nombra quién ejecuta el paso y su efecto; si es blanco farmacológico o dato diagnóstico, dilo y remite.
- Cada `ol.tl` hija directa de la `section`; timeline plana; ramas con `data-rama="Rama A"`, sin nodos anidados.
- `data-paso` en todo nodo: frase clave de ≤8 palabras reconstruible (`Obstrucción de la luz apendicular`, no `Paso 1`), en orden causal real. Alimenta el ejercicio «Ordenar» (§7.15): el `.det` del nodo es la explicación que se despliega al revisar.
- `data-clin="1"`: `p.man` con 1–3 `.xref` a signos; `data-clin="0"`: paso intermedio.
- Toda molécula, receptor o estructura del `.det` dice en una frase qué es, qué hace y dónde. Sin eslabones saltados; estructura que explica ≠ estructura que se ve; nombra los dos golpes (terreno + desencadenante) si existen. Solo moléculas del camino causal; listas, en acordeón.
  - Mal: «La CCK contrae la vesícula». Bien: «La colecistocinina (CCK, hormona de las células I duodenales) activa receptores CCK1 del músculo liso vesicular y lo contrae».
  - Mal: «La insuficiencia renal sube la creatinina». Bien: «La caída del filtrado glomerular (FG, volumen de plasma depurado por minuto en los glomérulos) reduce la excreción de creatinina, que se acumula en plasma».

**7.6 Enlaces nodo ↔ signo** (precedencia 4).
- Nodos en orden de timeline y signos en orden de aparición, numerados desde 1 sin saltos.
- ≤3 enlaces por nodo y ≤2 por signo, recíprocos. Todo nodo `data-clin="1"` enlaza a un signo; todo signo enlaza a su nodo o lleva `.mini` `Mecanismo no establecido`.
- Nodos y signos nunca dentro de acordeón.

**7.7 Signos y «Qué verás».**
- Clínica por mecanismo o rama, no por aparato; signos menores en tabla `Signo · Mecanismo · Nodo`.
- `.signo`: `Por qué aparece` en 1–2 frases con `.xref` `← Mecanismo`; `Qué significa` sin propiedades.
- `.qv`: `p|v|a` = presente, variable, ausente; `k` = signo clave. No escribas el estado.

**7.8 Pasos etiquetados.** Vocabulario cerrado del contrato (§11), literal. **Cada `li` de `ol.steps.tg` lleva `data-paso`** (≤10 palabras, frase clave reconstruible, sin la etiqueta); el texto del `li` es la explicación que se despliega al revisar el ejercicio «Ordenar».

**7.9 Tablas dx y tx.**
- Pruebas: `Prueba · S · E · VPP/VPN · Utilidad (descartar/confirmar) · Notas · Ref.` S y E solo con fuente y contexto; VPP/VPN comentados según la prevalencia en Ecuador; SnNout/SpPin si procede; sin cifra: `No establecida` o rango con fuente. `.xref` opcional al nodo en Notas.
- Fármacos: `Fármaco · Mecanismo de acción · Dosis · Vía · Frecuencia · Duración · Notas/ajustes · Ref.` La columna «Mecanismo de acción» dice en 1–2 frases el blanco molecular, qué hace sobre él y el efecto fisiológico, y cierra con 1 `.xref` `← Paso` al nodo que interrumpe; en «Notas/ajustes» quedan ajustes (renal, hepático, edad, peso, embarazo), contraindicaciones y adversos que cambian la elección. Incluye carga y mantenimiento, titulación y umbrales. Nivel: «Prednisona 40 mg VO cada 24 h por 5 días, sin descenso», no «corticoide».
- Glosario de siglas al pie de cada tabla (`p.mini`).
- **Fuente única:** posología solo en la tabla de fármacos (de su entidad); S, E, VPP y VPN solo en la de pruebas. Fuera, `span.rem` de §3; en la pestaña (mono) o `h2` (multi) de su tabla, `↓ En la tabla`. Los simuladores sí muestran posología.
- **Prohibidas las tablas-índice** que solo dicen dónde está cada cosa (p. ej. «Esquema DSM-5-TR» o cuadros de criterios que enumeran apartados sin contenido). Los criterios se escriben con su contenido en la card de criterios.

**7.10 Simulador · Decisión clínica.**
- Salida: clasificación, diagnóstico integrado o conducta con posología completa; cada umbral o recomendación con `[n]`. Selección vacía (también al cargar) → mensaje guía.
- `sel(dc,'g')` → `data-v` activos; `num(dc,'n')` → número o `NaN`.
- Dosis por peso: `rd()` y tope `Math.min` con la dosis máxima del adulto o la de la guía; la salida muestra el tope. Todo fármaco del simulador figura en la tabla de fármacos de su pestaña.
- Tipos: dx (inicial vs confirmatorio; doble eje; escala → banda → conducta; ambulatorio/hospital/quirófano; referencia) · tx (posología por grupo, gravedad, biomarcador, peso o SC; escalonamiento) · seguimiento (vigilancia por riesgo; escalada; fracaso).
- Contrafactual `span.cf`: el hallazgo cuyo cambio cambia la conducta (en multi, el que lleva a la entidad vecina).
- **Restricción (precedencia 2):** prohibido calcular VPP, VPN, LR, probabilidad pre/post-test, Bayes o Fagan, o tomar la prevalencia como entrada; esas cifras solo se tabulan.

**7.11 Prerrequisitos.** Inventaría en el manifiesto los términos que el tema da por sabidos. Define cada uno en su primera mención (una frase) o en la card de sustrato normal con la remisión `por eso en…`.

**7.12 Discrepancias, sílabo y alcance.**
- `hb vi` solo para errores de fuentes de Ricardo (sílabo, texto base, adjunto, widget previo): ≤110 palabras, fuente → por qué está mal → `[n]` → **regla correcta** en `<b>`, lista para Anki. En la pestaña del dato; nunca en `pan` ni `sin`.
- Sílabo impreciso: `hb am` con `hb-t` `Precisión sobre el sílabo`. Si nombra una entidad genérica: clasificación completa + la forma que encaja + la más frecuente como contraste.
- Recortes de alcance: decláralos en `hb am` con `hb-t` `Alcance`. Sin sílabo: `hb am` con `hb-t` `Sin sílabo` indicando las guías y temarios usados.

**7.13 Núcleo para Anki (`nucleo` del manifiesto).** Lo recuperable: `data-paso` de nodos `data-clin="1"`, celda `k`, pasos `1.º` y `De elección` y, en multi, los ejes de `vis` (`nucleo.vis`). Revísalo contra la guía vigente; lístalo con el texto literal del widget (va a Anki). Sin marcador visual propio.

**7.14 Imágenes.** Solo si Ricardo las adjunta: JPEG ≤760 px de ancho, calidad ≈82, en `figure.fig` con `figcaption` que interpreta: qué mirar, por qué, con qué se confunde.

**7.15 Recuerdo activo: ordenar pasos.** Sustituye a los modos «Timeline en blanco» y «Tabla en blanco» (no los escribas). El script del kit añade un botón «Ordenar» a cada bloque elegible: cadena fisiopatológica (`ol.tl`, usa el `data-paso` de cada nodo), algoritmo diagnóstico y escalonamiento del tratamiento (`ol.steps.tg`, usa el `data-paso` de cada `li`). Al activarlo aparece una caja con las frases desordenadas y una fila de huecos numerados; se arrastra (iPad, Mac) o se toca la frase y luego el hueco (iPhone). «Revisar» recoloca los pasos en su orden, marca aciertos y errores y despliega la explicación de cada paso; «Reiniciar» baraja de nuevo. No se guarda nada. Las partes **no** escriben las clases `.ord*`; solo aportan `data-paso` claros, distintos entre sí y en orden causal o de algoritmo reales, con explicación completa en el nodo o `li`.

**7.16 Diagramas (solo donde aclaran).** Bloques y flechas HTML/CSS del kit (`figure.dg`), nunca imágenes ni SVG. **Sin mínimos por pestaña**: pon un diagrama cuando ordena mejor que el texto y omítelo si el párrafo ya basta. Tipos útiles:
- **Causa-efecto:** resume la cadena en 4–8 nodos, del terreno y el disparador al mecanismo y al signo o complicación. Junto a la «Cadena» (multi) o en `fis` (mono).
- **Mecanismo de acción:** fármaco o intervención → blanco → efecto celular → nodo que interrumpe → efecto clínico (y el adverso del mismo mecanismo si importa). Antes de la tabla de fármacos.
- **Representación:** clasificación o espectro, curso temporal o fases, escalera de riesgo o gravedad, algoritmo diagnóstico (sin cálculos), comparación de polos o subtipos.
`pan` y `sin` sin diagramas. Cada diagrama: `div.dg-t` (título en tipo oración), ≥1 `div.dg-row`, nodos `div.dg-n` de ≤12 palabras, flechas `div.dg-ar` con `span.dg-lab` opcional (≤4 palabras: «activa», «inhibe», «produce»), columnas `div.dg-col` para ramas paralelas, y `figcaption.mini` que dice cómo leerlo en una frase. Color por rol, igual en todo el widget: `fr` terreno o factor de riesgo; `b` mecanismo biológico; `p` fenómeno psicológico o examen mental; `ac` estructura o proceso normal y fármacos; `s` efecto protector o terapéutico; `ro` daño, signo de alarma o desenlace grave. Un diagrama no repite texto de un párrafo: lo ordena. Se empareja con su explicación mediante `div.duo`.

**7.17 Diseño (lo hace el kit; las partes no llevan estilos).**
- **Estilo app de estudio:** tarjetas con esquinas suaves, mucho aire, tipografía grande, jerarquía por tamaño y peso; fuente del sistema (`-apple-system, system-ui`), sin recursos externos.
- **Paleta neutra con un acento por tema**, declarado en `manifiesto.tema`: `ginecologia` frambuesa, `salud-mental` índigo, `digestivo` verde azulado, `urologia` ámbar oscuro, `pediatria-ortopedia` azul; otro → azul. Modo oscuro automático. Rojo, ámbar y verde solo para alarma, precaución y correcto: no los uses como decoración.
- **Navegación adaptable generada por el script** a partir de tu `nav.tabs>button.tb` (texto corto, ≤2 palabras): iPhone (<760 px) barra inferior; iPad y Mac (≥760 px) menú lateral con los `h2` de la pestaña activa para saltar. Por eso los `h2` deben ser títulos de sección claros. Filtro de perlas por examen en la barra o el menú.
- **Animaciones sutiles** (cambio de pestaña, elevación de tarjetas, aparición de pasos al revisar «Ordenar»); respetan `prefers-reduced-motion`. Sin barra de progreso.
- **Tablas:** fichas apiladas en iPhone (salvo `table.vis`); en iPad/Mac, tablas limpias con cabecera fija dentro del contenedor.
- **`div.duo`:** empareja una explicación (`p`, `.card`, `.fey`) con su `figure.dg` o una tabla corta; exactamente dos hijos; dos columnas en Mac e iPad horizontal. Nunca dentro de `.duo`: `ol.tl`, nodos, `.signo`, `.qv`, `ol.steps`, `.dc`, `h2` ni PG. Nada de anchos fijos.
- **Revisión visual** con capturas en 390, 820, 1180 y 1440 px (`kit/v11/probar.js`), sin desbordes.

**7.18 Profundidad.** Nivel universitario avanzado, de examen; diagnóstico, tratamiento y seguimiento, lo más profundo. Español de Ecuador; término inglés entre paréntesis solo si domina la literatura.

## 8 · Layout mono

- Orden interno de cada pestaña de contenido: PG → **núcleo** → badge `b-pu` de la guía → `hb am` si aplica (§7.12) → segmento 1 → Feynman → … → simulador (en `dx`, `tx`, `seg`). Las perlas de examen van junto al tema.
- Adicional (clasificación, estadiaje o segunda entidad): clave `[a-z]{2,4}`, parte `16x_clave.html` tras `15_seg`; con su etapa en `pan`.

**`pan`.** `hb az` `El tema en una frase` (≤30 palabras) → etapas → cierre.
- Etapas en orden fijo: Definición y Epidemiología (`def`, una cada una) · Etiología y fisiopatología (`fis`) · Clínica (`cli`) · Diagnóstico (`dx`) · Tratamiento (`tx`) · Seguimiento y complicaciones (`seg`); la adicional en su lugar lógico. Cadena: qué es → a quién afecta → por qué ocurre → cómo se manifiesta → cómo se confirma → cómo se trata → cómo evoluciona.
- Definición: qué la separa de lo más parecido · Epidemiología: ≤2 cifras · Fisiopatología: pasos y disparador · Clínica: signo y mecanismo en una frase · Diagnóstico: inicial vs confirmatorio · Tratamiento: por grupo, sin dosis · Seguimiento: vigilancia, complicación más temida y su señal.

**`def`.** Segmento 1 · Definición, en orden:
1. Card de definición: redacción propia y fiel ≤60 palabras (≤1 frase literal entre « », <15 palabras); badge `b-pu` con fuente y año + `[n]`; fuentes divergentes → `.mini`; si no se puede atribuir a una fuente verificada, reescríbela con una que sí.
2. Card de sustrato normal (≤80 palabras): qué estructura o proceso normal se altera; cierra con `↪ Mecanismo en «Etiología y fisiopatología»`.
3. Card de criterios: formales con `[n]` o rasgos de consenso, con su contenido (sin tabla-índice); nombra los subtipos.
4. Tabla `Entidad vecina · Qué comparte · Criterio que las separa` («No confundir con…»), 2–3 filas, fuera de acordeón.
5. Card de ejemplo de anclaje: viñeta de 2–3 líneas, sin conducta.
6. Feynman (el único de `def`).

Segmento 1 sin tratamiento, pronóstico ni plan diagnóstico. Segmento 2 · Epidemiología: `div.stats` solo con `[n]`; factores de riesgo epidemiológicos (mecanismos en `fis`); Ecuador y Latinoamérica si existen, si no `.mini` sin estimaciones.

**`fis`.** Tabla de etiología `Causa / grupo · Cómo entra en la cascada · Nodo · Ref.`, agrupada por punto de entrada, con `.xref` a su nodo en cada fila → timeline(s). Cada rama suele ser un segmento cardinal.

**`cli`.** `.qv` opcional tras el badge; segmento final opcional de formas clínicas con su mecanismo y enlace.

**`dx` · `tx` · `seg`.** `dx` y `tx`: pasos → su tabla → simulador. `seg`: ciclo revisar-evaluar-ajustar, índices pronósticos, comorbilidades y cada complicación por su mecanismo con `.xref` al nodo si existe → simulador → `.acc.refs`.

## 9 · Layout multi

**Delta.** Lo común a ≥2 entidades (presentación, criterios de disfunción orgánica, nota de altitud, analgesia común…) se escribe una vez, en `vis`, en una `div.card` que empieza por `<b>Común al grupo</b>`; cada `eK` remite con `span.rem` (`↪ … en «[botón de vis]»`) y desarrolla solo lo propio, respondiendo a cada fila de `vis`. Secundarias ≤1 200 palabras; subtipos ≤3 filas.

**`pan`.** `hb az` `El grupo en una frase` (≤30 palabras) → etapa eje (`data-go="vis"`: la presentación que las une y los 2–3 ejes que las separan; puente a `e1`) → una etapa por entidad (`data-go="eK"`, en orden: dónde cae en el eje → mecanismo en una frase → signo que la delata → conducta decisiva; puente a la siguiente) → cierre. N+1 etapas, todas de 70–110 palabras.

**`vis`.** PG → **núcleo** → badge `b-pu` → `hb am` si aplica → tabla → card «Común al grupo» → `hb ro` → pasos dx del diferencial → simulador diferencial.
- PG desde la presentación («ante X con Y, ¿qué lo separa de…?»), nunca desde el nombre de una entidad.
- **Tabla con filas como preguntas.** Cabeceras de columna = textos exactos de los botones `e1…eN`. Cada fila: `tr>th>(span.q{pregunta}+span.qx{qué se busca, ≤15 palabras})+td…`; celdas ≤12 palabras, ninguna vacía. Las 9 filas, en este orden y con esta redacción (lenguaje fácil, sin jerga en la pregunta):
  1. `¿Cuál es el mecanismo principal que explica la enfermedad?` · qx: «El paso que falla y explica casi todo lo demás.» (antes «Falla central»)
  2. `¿En qué persona o población es más frecuente?` · qx: «Edad, sexo, antecedente o contexto donde más aparece.» (antes «Terreno típico»)
  3. `¿Cómo empieza y cómo evoluciona?` · qx: «Rapidez de inicio y curso: agudo, subagudo, crónico o recurrente.» (antes «Inicio y curso»)
  4. `¿Qué síntoma comparte con las demás?` · qx: «La queja de entrada común y cómo se presenta en esta entidad.» (antes «Síntoma compartido aquí»)
  5. `¿Qué hallazgo la delata?` · qx: «El signo o dato clave que la separa de las otras.» (antes «Signo que la delata»; celda `k` de su `.qv`)
  6. `¿Qué dato negativo la descarta?` · qx: «Lo que debería faltar; si está presente, piensa en otra.» (antes «Negativo pertinente»)
  7. `¿Qué prueba la confirma?` · qx: «La prueba que decide el diagnóstico, no la de tamizaje.» (antes «Prueba que decide»; su paso `1.º` o `Confirma`)
  8. `¿Qué haces primero y quién la maneja?` · qx: «Primera conducta y nivel o especialista que se hace cargo.» (antes «Conducta inicial y quién maneja»)
  9. `¿Qué pasa si no la reconoces?` · qx: «La complicación o desenlace grave que se evita al sospecharla.» (antes «Amenaza si se pierde»)
- `hb ro`: banderas rojas; el primer ítem nombra la amenaza.
- Simulador diferencial: chips de hallazgos → entidad compatible + hallazgo que falta para confirmarla + conducta inicial + contrafactual; sin probabilidades. `dc-t`: `Simulador · Decisión clínica — predice la entidad antes de pulsar`.

**`eK`.** `hb az` con `hb-t` `Frente a [vecina]` (1–2 líneas: se confunde con… · se separa por…; la vecina más confundible del grupo, por defecto `e1` con el texto de su botón) → PG → **núcleo** → badge `b-pu`. Después, exactamente 7 `h2` hijos directos de la `section`, en este orden:
1. `Qué es`: oneliner + criterios + subtipos (por qué existen + tabla equivalente) + «No confundir con…» solo con vecina fuera del grupo.
2. `Epidemiología`: tabla de 4 filas, primera columna exacta `Frecuencia` · `Edad` · `Sexo` · `Factores clave`, con `[n]`.
3. `Cadena`: tabla de etiología (opcional) → `ol.tl` → Feynman.
4. `Qué verás`: `.qv` → fichas `.signo` de los signos clave → tabla de signos menores (opcional) → Feynman (`e1`).
5. `Diagnóstico`: pasos dx → tabla de pruebas → simulador (`e1`).
6. `Tratamiento`: pasos tx → tabla de fármacos → simulador.
7. `Seguimiento`: complicaciones por mecanismo con `.xref` al nodo; simulador opcional en `e1`.

`e1` a profundidad mono; secundarias con los conteos de §3. `.xref` solo dentro de la entidad: el contraste vive en `vis`.

**`sin`.** Solo `div.hb.ro` con `hb-t` `Errores que no se pueden cometer` (del grupo) y `.acc.refs`. Nada más.

## 10 · Fuentes y Vancouver

- **Hipervínculos (v11):** cada `li` de `ol.vanc` lleva, cuando existan, `doi:…`, `PMID: n`, `Setid <id>` (DailyMed) o `Disponible en: <URL>`; el script del kit los convierte en enlaces a la página de la fuente (doi.org, PubMed, DailyMed, URL). Sin identificador (libros), enlace a búsqueda en Google Académico. No escribas `<a>` en las partes.

- Badge `b-pu` con guía, sociedad y año en cada pestaña de contenido (salvo `sin`); `(solo resumen)` si no leíste más. Cita la edición realmente leída; nunca una no verificada.
- `[n]` en diagnósticos, dosis, umbrales, algoritmos y cifras, numerados por **primera aparición** recorriendo las pestañas en orden de barra; `pan` reutiliza esos números. Tras editar referencias, ejecuta `kit/renumerar.py` para renumerar.
- `.acc.refs` con `ol.vanc`, Vancouver estricto; nivel de evidencia si la guía lo da; distingue guía, consenso, revisión o ensayo.
- PMID y DOI solo verificados; si no, omite el identificador, no la referencia.
- Prioridad: adjuntos → sílabo del caso y su bibliografía (si hay) → guía vigente (internacional + GPC MSP) → libros de la tabla de ediciones; Latinoamérica y Ecuador si existen.
- **Bibliografía por defecto = la del sílabo del caso, con sus ediciones.** 1.ª rotación: Harrison 22e 2025; Farreras-Rozman 20.ª ed. 2024 (el sílabo dice «22.ª»: error, decláralo). 2.ª rotación: el sílabo cita ediciones viejas de Harrison (19) y Farreras (17); usa las vigentes de `protocolo_verificacion.md` § 4 y mantén los complementarios del sílabo: Fitzpatrick Atlas 9e 2023, Guzmán Dermatología 8e 2024, Soutor Dermatología clínica 2e 2023, Kane Geriatría clínica 8e 2018, Ebert Psiquiatría 4e 2025, MSP Adultos mayores 2010. Sin sílabo: guías vigentes y libros de la tabla. Un libro fuera de ambos: verifica su edición (protocolo § 3).
- Sin badge ámbar ni marca de verificación en la tabla de ediciones. Vigencia no verificada → `.mini` `Vigencia no verificada` (solo si de verdad no se pudo comprobar la versión de la guía).
- Altitud: nota solo si un umbral sensible (Hb, Hto, PaO₂, VSG, fluidos) cambia la conducta a ~2 850 m.
- Discrepancias entre fuentes: señálalas, no las armonices.

## 11 · Contrato de marcado

No inventes clases. Emmet (`{…}`=texto); todo `button` con `type="button"`; `k` = data-tab.
- Nav `h1`+`nav.tabs>button.tb[data-tab=k][onclick="show('k')"]` (el script construye `nav.side`, `nav.bottom` y `.perla-filtro`; no los escribas)
- `section.tab[data-tab=k]`·`div.hb.az|am|ro|ve|vi>div.hb-t+…`·PG `div.hb.az>div.hb-t+ol.pg>li` = 1.ª caja
- Núcleo `div.nucleo>div.nucleo-t{Núcleo}+ul>li`×3–5, justo tras las PG
- Perla de examen `aside.perla[data-ex="puce caces usmle1 usmle2 mir enarm"(una o varias)]>div.perla-t{Perla de examen}+p`
- `span.badge.b-az|ro|am|ve|pu|co|rs`·`div.card`·`p.mini`·`span.tag`·`div.tw>table`·`div.stats>div.stat>b+span`
- Remisión `span.rem{↪ Posología en «…»}`; en la pestaña/h2 de su tabla: `span.rem{↓ En la tabla}`
- Acordeón `div.acc>button.acc-h[onclick="tog(this)"]{T }>span.chev{▾}` `+div.acc-b`; refs `div.acc.refs…ol.vanc>li`
- Etapa `div.etapa[data-go=k]>h3+p.res+p.perla+button.go[data-go=k][onclick="show('k')"]`
- Feynman `div.fey>span.fey-t{Explícalo como a un niño de 10 años — X}+p.fey-b+p.mini.fey-c{En medicina esto se llama… }+p.mini.fey-c{Dónde falla la comparación: }`
- Nodo `section>ol.tl>li.nodo#ID[data-clin=0|1][data-paso][data-rama?]>div.det>…+p.man{Se manifiesta como: xref}`
- Signo `div.signo#ID>h4+dl>dt{Cómo se reconoce}+dd+dt{Por qué aparece}+dd{…xref}+dt{Qué significa}+dd`
- Xref `button.xref[data-ir=ID][onclick="ir('k','ID')"]` (k del destino)
- Pasos `ol.steps.tg>li[data-paso]>span.tg{etiqueta}+texto`; dx `1.º·Añade·Confirma·Solo si·No pidas·Alarma` (un `1.º`); tx `Principio·De elección·Alternativa·Sintomático·Escala·Reevalúa·Especialista·Evita` (un `De elección`); sin dosis
- Qué verás `div.qv>p[data-e=p|v|a]`×≥4`+p[data-e=k]{signo xref}`
- Discrepancia `div.hb.vi>div.hb-t{Discrepancia: …}+p{… [n] <b>regla</b>}`
- Simulador `div.dc[data-fn=dcX]>div.dc-t{Simulador · Decisión clínica — …}+div.dc-g>span.dc-l+(button.chip[data-g][data-v][data-m=1?][onclick="ch(this)"]|input[type=number][data-n][oninput="ch(this)"])` `+div.out`; salida acaba en `span.cf{Si … → …}`
- `90_sim.html`: un `script`, `function dcX(dc){…}`, dosis por peso con `Math.min`; helpers `sel num out rd`; reservados `show ir tog ch sel num out rd recon tabla`
- Figura `figure.fig>img[src="data:image/jpeg;base64,…"][alt]+figcaption`
- Diagrama `figure.dg>div.dg-t{título}+div.dg-row>(div.dg-n.fr|b|p|ac|s|ro{≤12 palabras}|div.dg-col>div.dg-n…)+div.dg-ar>span.dg-lab{verbo}…` `+figcaption.mini{cómo leerlo}`
- Par adaptable `div.duo>(p|div.card|div.fey)+(figure.dg|div.tw)`
- vis: `div.tw>table.vis>thead>tr>th+th{botón eK}`…; `tbody` 9 `tr>th>(span.q{pregunta}+span.qx{mini explicación})+td`… con las preguntas de §9 → `hb ro` → `ol.steps.tg` → `.dc`
- Generadas por el script (no las escribas): `.ord`, `.ord-bank`, `.ord-slots`, `.ord-chip`, `.ord-slot`, `.ord-ok`, `.ord-ko`, `.ord-btns`, `nav.side`, `nav.bottom`, `.perla-filtro`; `html[data-tema]` lo pone `construir.py` desde `manifiesto.tema`
- Prohibido: estilos inline, `<style>` propio, `<img>` salvo figuras de adjuntos, recursos remotos, `localStorage`/`sessionStorage`, `position:fixed`, `...` ASCII (usa `…`), `[resto igual]`, `TODO:`, `[VERIFICAR EN FUENTE]`

## 12 · Flujo

1. Arranque (§1), Paso 0 (§2) y vigencia de la guía (§6).
2. **Manifiesto en el chat**, breve: línea del router; valores por defecto (incluido «sin sílabo» si aplica); guía (año, vigencia); fila de §3 del modo; tabla `Pestaña · Temas rectores · PG · Feynman · DC`; mapa `id · data-paso · clin · signo`; prerrequisitos; núcleo Anki. Guárdalo en `widgets/<tema>/<id>/manifiesto.json` (`entidades.eK` = texto exacto del botón):
   - Comunes: `"titulo"`, `"salida"`, `"tipo":"v11"`, `"tema"` (acento, §7.17).
   - Regla `pg`/`fey`: `{"pestaña":n}` con toda pestaña de contenido (no `pan`) cuyo n>0; una pestaña con 0 puede omitirse o escribirse (`"sin":0`); ninguna otra clave. `dc`: pestañas con simulador, en orden de barra. `nodos`/`signos`: entero (mono) u objeto por entidad (multi). `dg` (opcional): diagramas reales por pestaña, si los hay; no hay mínimos.
   - mono `{"modo":"mono","tabs":[],"pg":{"def":n},"fey":{"def":1},"nodos":n,"signos":n,"dc":["dx","tx","seg"],"nucleo":[≤12]}`
   - multi `{"modo":"multi","entidades":{"e1":"botón"},"principal":"e1","amenaza":"eK","tabs":[],"pg":{"vis":n,"e1":n},"fey":{"e1":n},"nodos":{"e1":n},"signos":{"e1":n},"dc":["vis","e1"],"nucleo":{"vis":[≤5 ejes],"e1":[≤7]}}`
3. **Partes** de contenido en orden de barra; después `01_nav` + `90_sim`; **`02_pan` al final**. Si una parte no cabe en una llamada, continúa con `cat >> parte <<'EOF'` y corta en un límite estructural limpio. **Truncar en silencio es el único fallo inaceptable.**
4. **Construir:** `python3 kit/construir.py widgets/<tema>/<id>` (ensambla con `kit/v11/` y valida). Corrige con edición puntual y repite; máximo 3 ciclos. Revisa los avisos; no bloquean.
5. **Probar:** `node kit/v11/probar.js file://$PWD/<html> <carpeta_capturas>`; revisa 390, 820, 1180 y 1440 px, el ejercicio «Ordenar», el filtro de perlas y los `.duo`.
6. **Entrega:** HTML final en la ruta de `salida` (`<slug>_widget_v11.html`: slug ≤40 caracteres, guiones bajos, sin comas ni rayas), junto con partes y fila en `README.md`. Artefacto solo si se pide.
7. **Modo edición** (el adjunto es la fuente de verdad): audita contra §14 y da los hallazgos en el manifiesto; si es v10.x, conviértelo a v11 en partes (núcleo, perlas, `data-paso` en pasos, filas-pregunta, sin modos en blanco ni tablas-índice) y añade `Cambios por pestaña` a la salida.

## 13 · Reglas de las demás skills

Las skills de definiciones y apertura adoptan el diseño v11 y la regla de cero marcas para widgets futuros; los ya hechos no se tocan.

## 14 · Autoverificación y salida

Autoverificación (no la muestres; corrige antes de entregar):
1. ¿Toda cifra, dosis, año, edición, PMID o DOI tiene fuente leída?
2. ¿Cada PG se responde en su pestaña?
3. ¿Cada pestaña sigue PG → núcleo (3–5 ideas, ≤35 palabras, con `[n]`) → detalle, y nada del detalle se recortó?
4. ¿Todo lo de `pan` se desarrolla en su destino, con puentes y signos unidos a su mecanismo?
5. ¿Alguna analogía es falsa o paráfrasis del técnico?
6. ¿Cada `data-paso` (nodos y `li` de `ol.steps.tg`) es reconstruible, distinto, en orden causal y con su explicación completa?
7. ¿Posología y propiedades solo en su tabla? ¿Cada fármaco simulado está en ella? ¿Toda tabla de fármacos tiene «Mecanismo de acción» con su `.xref`?
8. ¿Cada perla de examen lleva `data-ex` según el criterio fijo, está junto a su tema y lleva `[n]`?
9. ¿Cada nota de altitud cambia una conducta?
10. ¿Cada prerrequisito está definido (primera mención o sustrato)?
11. Pareto: con solo `pan` + `vis` (mono: `pan` + núcleos), ¿se nombran la entidad y su conducta inicial ante la presentación?
12. Delta (multi): ¿nada común se repite en un `eK`? ¿`vis` usa las 9 preguntas con `span.q`+`span.qx` y coincide con `.qv` y pasos?
13. ¿Cada `hb vi` corrige una fuente de Ricardo?
14. ¿El alcance sale del caso del sílabo, o se declaró «sin sílabo» con guías y temarios? ¿Las ediciones erróneas del sílabo están declaradas como discrepancia?
15. ¿Quedan cero `[VERIFICAR EN FUENTE]`, y cero «Fuente por verificar» tras agotar PubMed, Consensus, fichas técnicas, GPC del MSP y web?
16. ¿Hay sesgo quirúrgico/urológico o emoji que no corresponda al área? ¿Los «signos» y «Qué verás» se adaptaron al área?
17. ¿Sin tablas-índice, sin modos en blanco, sin preguntas de práctica? ¿Diagramas solo donde aclaran, con color por rol y sin repetir el texto?
18. ¿El manifiesto lleva `"tipo":"v11"` y `tema`, y se construyó con `kit/construir.py`? ¿Referencias renumeradas con `kit/renumerar.py`?
19. ¿Se revisaron capturas en 390, 820, 1180 y 1440 px, sin desbordes ni `.duo` mal emparejados?

**Salida** (nada más):
1. Manifiesto.
2. Ruta del `.html` generado.
3. Línea `RESULTADO:` del validador.
4. Línea de aviso: «Verificados N de M datos; corregidos C; eliminados X»; conflictos de precedencia; discrepancias nuevas propuestas para el registro, como filas `| Tema | Fuente | Dice | Regla correcta | Ref. |`; `Núcleo (Anki): …` con los ítems de `nucleo`.

Solo si Ricardo confirma una fila, escríbela en `registro-discrepancias.md` (créalo si falta). Sin introducción, resumen ni cierre.
