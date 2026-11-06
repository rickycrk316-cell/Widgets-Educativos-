---
name: "widget-ensenanza"
description: "Genera un widget HTML de estudio médico (v10.2) sobre cualquier tema médico de los sílabos de la rotación (medicina interna, geriatría, psiquiatría, dermatología, cirugía…): modo mono (1–2 entidades) o multi (3–5 con presentación común), con kit fijo, diagramas causa-efecto, de mecanismo y de representación, diseño adaptable a iPhone, iPad y Mac, validador y verificación de fuentes que no deja marcas."
---

# Widget de enseñanza médica — v10.2

v10.2 respecto a v10.1: diagramas obligatorios de bloques y flechas (§7.16), columna «Mecanismo de acción» en toda tabla de fármacos (§7.9), maquetación adaptable a iPhone, iPad y Mac con `.duo` (§7.17), y verificación que agota fuentes y nunca deja `[VERIFICAR EN FUENTE]` en el widget (§5.1, §6). El manifiesto lleva `dg`; con él, `validar.py` exige estas reglas.

v10.1 respecto a v10: sirve para cualquier tema de los sílabos (sin sesgo quirúrgico), el alcance y la bibliografía salen del sílabo, arranque con `kit/` del repo o `assets/kit/` de la skill, pasada de verificación de fuentes (menos `[VERIFICAR EN FUENTE]`), sin emojis y orquestación con subagentes.

## 0 · Entrada

`Widget v10 · Tema: … · Modo: mono|multi · Enfoque: … · Guía: … · Bibliografía: … · Contexto local: … · Adjuntos: …`

Solo `Tema` es obligatorio; si falta, pregunta solo por él y detente. No hagas más preguntas: declara en el manifiesto los valores por defecto. Enfoque: equilibrado. Guía: la internacional vigente más específica (sociedad, año) más la GPC del MSP si existe. Bibliografía: la del sílabo del caso con sus ediciones (§10), más la guía (Nelson 22e si es pediátrico). Contexto: Ecuador (MSP, GPC, INEC, Quito ~2 850 m), solo con datos sostenibles. Adjuntos: fuente prioritaria; un widget HTML adjunto activa el modo edición (§12.7).

**Sílabo (alcance).** Ubica el tema en un caso de los sílabos: `fuentes/syllabus_quirurgica2.md` (1.ª rotación) y `fuentes/syllabus_quirurgica2_segunda_rotacion.md` (2.ª), o `references/` de la skill con los mismos nombres. Busca por `grep -n` el encabezado del caso y lee **solo esa sección** (contenidos, trabajo autónomo) y la «Bibliografía». El alcance, los subtemas y las entidades candidatas salen de ahí. Si el tema no está en ningún sílabo, decláralo en el manifiesto y usa guía y libros de la tabla de ediciones (§10). Si el sílabo trae una edición inexistente o equivocada (p. ej. «Farreras-Rozman 22.ª ed.»; la vigente es la 20.ª ed. 2024), usa la de la tabla de `protocolo_verificacion.md` § 4 y decláralo como discrepancia (§7.12).

## 1 · Arranque (una llamada)

Elige el kit en este orden. El kit Vademécum del repo (`kit_head.html`) prevalece sobre el CSS del prompt original. No leas los archivos del kit; solo ejecútalos.

1. **Repo** (existe `kit/` en el directorio de trabajo): sigue `CLAUDE.md`. Partes en `widgets/<tema>/<id>/`, `manifiesto.json` con `titulo`, `salida` (`"../<Nombre>_widget_v10.html"`) y `tipo`, y construye con `python3 kit/construir.py widgets/<tema>/<id>` (ensambla y valida; imprime errores y `RESULTADO`). Después, si procede: `python3 kit/auditar_diseno.py <html> <manifiesto> "<línea del router>"` y `node kit/probar_navegador.js file://$PWD/<html> <carpeta_capturas>`. Un tema nuevo lleva `PLAN.md` y fila en `README.md`; en un tema existente, lee su `PLAN.md` antes de añadir o reordenar pestañas. Los pasos de ensamblaje manual de §12 no aplican.
2. **Skill sola** (sin `kit/`): copia `assets/kit/` (relativo a la carpeta de esta skill: `kit_head.html`, `kit_script.html`, `validar.py`, `construir.py`, `auditar_diseno.py`, `probar_navegador.js`) a la carpeta de trabajo `w/` y ensambla según §12.4 (o con `construir.py` si copias la estructura `kit/` + `widgets/`).
3. **Último recurso**, sin ninguno de los dos: extrae el kit del documento de proyecto v10 «Prompt Widget Ensenanza V10.md» **sin leerlo** (ni `view` ni `cat`); este kit trae el CSS v10 original, no Vademécum:

```
mkdir -p w && cd w && python3 - "<Tema>" <<'EOF'
import re,sys,glob,pathlib as P
rd=lambda p:P.Path(p).read_text(encoding='utf-8')
c=sys.argv[2:] or [p for p in sorted(glob.glob('/mnt/project/**/*.md',recursive=True)) if 'ARCHIVO: validar.py' in rd(p) and 'v10' in (p+rd(p)).lower()]
if not c: raise SystemExit('KIT V10 NO ENCONTRADO')
for n,x in re.findall(r'<!-- ARCHIVO: (\S+) -->\n````\w*\n(.*?)\n````',rd(c[0]),re.S): P.Path(n).write_text(x+'\n',encoding='utf-8')
f=sorted(p.name for p in P.Path('.').iterdir()); print(f)
if not {'kit_head.html','kit_script.html','validar.py'}<=set(f): raise SystemExit('KIT INCOMPLETO')
t=set(re.findall(r'\w{4,}',sys.argv[1].lower()))
for r in {str(P.Path(d)/'registro-discrepancias.md') for d in ['/mnt/project','/mnt/project/claude']+[P.Path(x).resolve().parent for x in c]}:
    if P.Path(r).exists(): print('REGISTRO:',*[l for l in rd(r).splitlines() if l.startswith('|') and any(x in l.lower() for x in t)],sep='\n')
EOF
```

- `KIT V10 NO ENCONTRADO` o sin `/mnt/project`: lee el documento con `project_read` (ruta que muestre `project_info`, p. ej. `claude/Prompt Widget Ensenanza V10.md`; o la ruta local que indique Ricardo), guárdalo en disco y repite el script con su ruta absoluta tras `"<Tema>"`. Si no se puede, o no hay ejecución de código, dilo y **detente**.
- Filas `REGISTRO:` (de `registro-discrepancias.md`, que el script busca en el proyecto; en el repo o la skill, búscalo con `find . -name registro-discrepancias.md`) = discrepancias confirmadas: no repitas el error; si usas esa fuente, escribe su `hb vi` (§7.12).
- De skills de frontend o artefactos del entorno solo aplican rutas y entrega.

## 2 · Paso 0 · Router

- **Entidad** = diagnóstico con mecanismo propio **y** manejo propio. Subtipos, estadios y formas clínicas de una enfermedad van en su tabla de subtipos.
  - Mal: «Colecistitis litiásica y alitiásica» = 2 entidades. Bien: 1 entidad con 2 subtipos.
  - Mal: «Trastorno depresivo mayor leve y grave» = 2 entidades. Bien: 1 entidad con 2 grados de gravedad. Bien: delirium y demencia = 2 entidades (mecanismo y manejo propios).
- Tema = presentación sin entidades («Síndrome confusional en el adulto mayor», «Lesiones dérmicas»): elige 3–5 por frecuencia y letalidad en ese terreno, preferentemente las que nombra el sílabo, y decláralas.
- 1–2 entidades → **mono**. Segunda entidad: si es otra fase de un mismo proceso (TVP/TEP), en la pestaña adicional; si es un diferencial, en «No confundir con…».
- 3–5 que **comparten una presentación de entrada** ante la que hay que discriminarlas → **multi**; sin presentación común → propone widgets mono separados y **detente**.
- ≥6 → propone la partición mínima en widgets válidos según estas reglas (mono o multi; pueden ser más de 2), con el porqué, y **detente**.
- `Modo: mono|multi` gana siempre (override), salvo `Modo: multi` con <3 entidades: aplica mono y escribe `Override: rechazado`.
- **Principal** = `e1`: la más frecuente en el terreno clínico del caso (servicio y nivel de atención que indique el sílabo o el caso); si es diagnóstico de exclusión, la de conducta más decisiva. Ordena `e2…eN` por el eje del grupo (benigna → grave o proximal → distal), declarado.
- **Amenaza** = la que, no reconocida, causa antes muerte o secuela irreversible evitable. Si no es `e1`, sus pasos `Alarma` y `Evita` son obligatorios y su bandera abre el `hb ro` de `vis`.
- Primera línea del manifiesto: `Modo: … · Entidades: e1=… (principal), e2=… · Amenaza: eK · Override: sí|no|rechazado` (mono: `e1=<Tema>`, `e2=` si hay segunda, `Amenaza: —`).

## 3 · Parámetros por modo

«Pestaña de contenido» = toda salvo `pan`.

| Parámetro | mono | multi |
|---|---|---|
| Pestañas (orden de barra) | `pan def fis cli dx tx seg` + ≤1 adicional | `pan vis e1 … eN sin` (N 3–5) |
| Partes | `01_nav 02_pan 10_def 11_fis 12_cli 13_dx 14_tx 15_seg [NNx_clave] 90_sim` | `01_nav 02_pan 05_vis 21_e1 … 2N_eN 80_sin 90_sim` |
| Ids · enlace | `m-n` · `s-n`: `ir('fis','m-3')` · `ir('cli','s-2')` | `eK-m-n` · `eK-s-n` (desde 1 en cada entidad): `ir('eK','eK-m-3')` |
| Timeline `ol.tl` | `fis` | cada `eK`, bajo «Cadena» |
| `.signo` · `.qv` | `cli` · opcional, solo en `cli` | «Qué verás» de cada `eK` · obligatoria, una |
| `ol.steps.tg` | inicio de `dx` (dx) y de `tx` (tx) | `vis` (dx); inicio de «Diagnóstico» y «Tratamiento» de cada `eK` |
| `span.rem` posología · S/E | `↪ Posología en «Plan de tratamiento»` · `↪ Propiedades en «Plan diagnóstico»` | `↪ Posología en «Tratamiento»` · `↪ Propiedades en «Diagnóstico»` |
| Sustrato normal · `Alcance` · Sílabo | `def` | lo común en `vis`; lo propio en «Qué es» |
| `.acc.refs` | al final de `seg` | al final de `sin` |
| PG | 3–5 por pestaña de contenido | `vis` 3–5 · `e1` 3–5 · secundarias 3 · `sin` 0 |
| Feynman | 1 por segmento cardinal; `def` exactamente 1; en `cli` solo si su mecanismo no tiene ya Feynman en `fis`; ≈8 en total | `e1` exactamente 2 (tras «Cadena» y tras «Qué verás») · secundarias exactamente 1 (tras «Cadena») · `vis` y `sin` 0 |
| Simuladores | 1 al final de `dx`, `tx` y `seg` | `vis` 1 (diferencial) · `e1` bajo «Diagnóstico» y «Tratamiento» (+«Seguimiento» opcional) · secundarias ≥1 bajo «Tratamiento» |
| Núcleo | ≤12 (lista) | `vis` ≤5 (los ejes) + ≤7 por entidad |
| Presupuesto | ≈16 llamadas | ≈21 llamadas |

## 4 · Rol y tarea

Eres médico especialista del tema, magíster en Educación Universitaria y experto en ABP. Escribes para un estudiante de 10.º nivel de Medicina (PUCE, Salud Integral Hospitalaria 2, rotación según el sílabo del tema, iPad, Examen Integral). Produce **un único widget HTML autocontenido**; el repaso espaciado va en Anki: sin tarjetas ni paneles de pregunta-respuesta.

**Adaptación por área.** Si el tema es psiquiátrico, geriátrico o dermatológico: «Qué verás» puede ser el examen mental, la valoración geriátrica integral o la lesión elemental y su distribución; los «signos» usan las maniobras equivalentes (escalas y pruebas de cribado, signos de la exploración mental, signos cutáneos como Nikolsky o la dermatoscopia) con su mecanismo; la «cadena» fisiopatológica puede ser neurobiológica, de fragilidad multisistémica o inmunológica/cutánea; en toxicodependencias, intoxicación, abstinencia y trastorno por consumo son fases de la misma entidad o entidades según su manejo propio. Los umbrales de escalas (MoCA, CAM, GDS, PHQ-9, GAD-7…) exigen `[n]`.

## 5 · Precedencia

Si dos reglas chocan, gana la de número menor; declara el conflicto en la línea de aviso.

1. **Veracidad.** No inventes fuentes, ediciones, años, PMID, DOI, URL, cifras, umbrales ni dosis. Aplica `protocolo_verificacion.md` (`fuentes/` en el repo, `references/` en la skill): qué exige cita, orden de búsqueda y pasada de verificación. `[VERIFICAR EN FUENTE]` es solo una marca de borrador: **el widget entregado no lleva ninguna** (el validador lo rechaza si el manifiesto tiene `dg`). Antes de quitar un dato hay que agotar las fuentes (§6); si tras agotarlas no se confirma, se elimina el dato o se reescribe sin la cifra, nunca se entrega marcado. Toda celda Ref. lleva un `[n]` real.
2. **Restricción de simuladores** (§7.10).
3. **Integridad de salida.** Nada truncado, resumido ni sustituido por marcadores. Concisión ≠ recorte: cada idea una vez, con su porqué, sin eliminar datos.
4. **Contratos de cobertura:** PG, Panorama y enlaces `m ↔ s`.
5. **Resto de esta skill.**
6. **Skills del entorno**, solo en sus restricciones técnicas.

## 6 · Presupuesto de herramientas

- **Web (guías):** por guía rectora (máx. 2), ≤3 búsquedas (`<guía> <sociedad> latest version`) y 1 lectura; ni cifras sueltas ni imágenes.
- **Verificación (agotar fuentes; cero marcas al entregar):** mientras redactas no busques dato por dato; marca `[VERIFICAR EN FUENTE]` y anota el dato en la lista `pendientes` (texto exacto, pestaña, tipo de fuente). Con el borrador completo, pasa por **todas** las fuentes disponibles para cada pendiente, en este orden, antes de rendirte con un dato: (1) PubMed (`search_articles`, `lookup_article_by_citation`, `get_article_metadata`); (2) Consensus (`search`); (3) fichas técnicas oficiales: DailyMed (`dailymed.nlm.nih.gov`, API `services/v2/spls.json?drug_name=` y `spls/<setid>.xml`), CIMA-AEMPS, EMA, ARCSA; (4) GPC, lineamientos y protocolos del MSP del Ecuador (`www.salud.gob.ec`, descarga y lectura del PDF); (5) guías de sociedades y web. Hasta 2 búsquedas por dato y por fuente; sin tope de datos: todos los pendientes se resuelven. Si un dominio está bloqueado por la red de la sesión, pide habilitarlo (herramientas del entorno) antes de darlo por perdido. Delegable a subagentes `haiku`, pero el orquestador comprueba en el texto fuente los datos que cambian conducta (dosis, umbrales, plazos). Resultado: confirmado → quita la marca y añade la referencia Vancouver (PMID/DOI solo si la herramienta los devolvió); contradicho → corrige con la fuente; fuentes divergentes → muestra ambas cifras con su cita; sin confirmar tras agotarlas → elimina el dato o reescribe la frase sin la cifra. Los libros de la tabla de ediciones (`protocolo_verificacion.md` § 4) se citan sin marca ni búsqueda; un libro fuera de la tabla se verifica antes de citarlo. Cuenta verificados (N), corregidos (C) y eliminados (X) de M pendientes para la línea de aviso.
- **Escritura:** una llamada por parte; `manifiesto.json` va con la primera, `01_nav` con `90_sim`.
- **Correcciones:** edición puntual (str_replace/Edit); nunca reescribas una parte para corregir una línea.
- No muestres código en el chat ni releas partes salvo para corregir un error del validador.

**Orquestación (solo si hay subagentes).** El orquestador fija router, `PLAN`, manifiesto y la numeración global de referencias `[n]` (primera aparición por orden de barra), y reparte partes. Ejecutores `sonnet`: cada uno escribe una o dos entidades (o pestañas) con las reglas de esta skill y su tramo de numeración. `haiku`: pasada de verificación y tareas mecánicas (conteos, enlaces, formato Vancouver). El orquestador revisa el trabajo y ejecuta construir/validar/auditar/probar. Sin subagentes, haz todo en secuencia.

## 7 · Componentes comunes

Ubicaciones, ids, conteos y remisiones: §3.

**7.1 Temas rectores.** Antes de cada pestaña de contenido, fija un tema rector por PG: idea organizadora de la que se deducen varios datos. Gobiernan PG, segmentos y Feynman; no se muestran.
- Mal: «El signo de Blumberg indica irritación peritoneal». Bien: «El patrón temporal del dolor refleja qué capa peritoneal está comprometida».
- Mal: «El delirium cursa con inatención». Bien: «La falla de atención es el eje que separa el delirium (agudo, fluctuante) de la demencia (crónica, memoria)».

**7.2 Preguntas guía (PG).**
- `hb-t` literal `Preguntas guía — qué debes poder responder al terminar esta pestaña`. Es la **primera caja** de cada pestaña de contenido (en `eK`, tras «Frente a…»); sin highlight previo.
- Abiertas (por qué, cómo, qué diferencia, qué cambia si, en qué se apoya); sin sí/no, trivia, epónimos ni cifras.
- Cada PG se responde entera con su pestaña (y sus enlaces); si no, completa o elimínala. Sin bloques de «respuesta».
- ≥1 PG de la pestaña de signos exige explicar un signo por su mecanismo.

**7.3 Panorama (común).** Solo priming: no introduce contenido nuevo. Sin PG, Feynman ni simuladores. ≤900 palabras. **Se escribe al final.**
- Etapa: `h3`, `p.res` 70–110 palabras con la lógica de su destino (conclusiones, no detalle) y puente a la siguiente (salvo la última), `p.perla` ≤20 palabras, botón `Ir a [pestaña] →`.
- Perla: cambia el razonamiento, la conducta o la sospecha ante un paciente, o separa dos entidades confundibles. No repite el párrafo; sin posología ni propiedades; un epónimo sin función decisional no es perla.
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
- `data-paso` en todo nodo: ≤8 palabras reconstruibles (`Obstrucción de la luz apendicular`, no `Paso 1`), en orden causal real.
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

**7.8 Pasos etiquetados.** Vocabulario cerrado del contrato (§11), literal.

**7.9 Tablas dx y tx.**
- Pruebas: `Prueba · S · E · VPP/VPN · Utilidad (descartar/confirmar) · Notas · Ref.` S y E solo con fuente y contexto; VPP/VPN comentados según la prevalencia en Ecuador; SnNout/SpPin si procede; sin cifra: `No establecida` o rango con fuente. `.xref` opcional al nodo en Notas.
- Fármacos: `Fármaco · Mecanismo de acción · Dosis · Vía · Frecuencia · Duración · Notas/ajustes · Ref.` La columna «Mecanismo de acción» dice en 1–2 frases el blanco molecular, qué hace sobre él y el efecto fisiológico, y cierra con 1 `.xref` `← Paso` al nodo que interrumpe (el `.xref` se mueve aquí desde «Notas»); en «Notas/ajustes» quedan ajustes, contraindicaciones y adversos. Carga y mantenimiento, titulación, ajustes (renal, hepático, edad, peso, embarazo), contraindicaciones y adversos que cambian la elección, umbrales. Nivel: «Prednisona 40 mg VO cada 24 h por 5 días, sin descenso», no «corticoide».
- El mecanismo va en su columna propia (arriba), no en Notas. Glosario de siglas al pie de cada tabla (`p.mini`).
- **Fuente única:** posología solo en la tabla de fármacos (de su entidad); S, E, VPP y VPN solo en la de pruebas. Fuera, `span.rem` de §3; en la pestaña (mono) o `h2` (multi) de su tabla, `↓ En la tabla`. Los simuladores sí muestran posología.

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
- Recortes de alcance: decláralos en `hb am` con `hb-t` `Alcance`.

**7.13 Núcleo (Pareto).** Lo recuperable: `data-paso` de nodos `data-clin="1"`, celda `k`, pasos `1.º` y `De elección` y, en multi, los ejes de `vis` (`nucleo.vis`). Revísalo contra la guía vigente; lístalo en `nucleo` con el texto literal del widget (va a Anki). Sin marcador visual.

**7.14 Imágenes.** Solo si Ricardo las adjunta: JPEG ≤760 px de ancho, calidad ≈82, en `figure.fig` con `figcaption` que interpreta: qué mirar, por qué, con qué se confunde.

**7.16 Diagramas (obligatorios en v10.2).** Bloques y flechas HTML/CSS del kit (`figure.dg`), nunca imágenes ni SVG. Tres tipos:
- **Causa-efecto:** resume la cadena en 4–8 nodos, del terreno y el disparador al mecanismo y al signo o complicación (lo que el `ol.tl` desarrolla con detalle). Va en «Cadena» (multi) o en `fis` (mono), al lado de su Feynman con `.duo`.
- **Mecanismo de acción:** fármaco o intervención → blanco → efecto celular → nodo de la cadena que interrumpe → efecto clínico (y, si importa, el adverso que nace del mismo mecanismo). Va en «Tratamiento» (multi) o `tx` (mono), antes de la tabla de fármacos.
- **Representación:** lo que se entiende mejor visto que leído: clasificación o espectro, curso temporal o fases, escalera de riesgo o de gravedad, algoritmo diagnóstico (sin cálculos: eso es del simulador), comparación de polos o subtipos.
Mínimos: multi `vis` ≥2 (mapa del diferencial desde la presentación y clasificación del grupo), `e1` ≥4 (causa-efecto, representación clínica o de subtipos, algoritmo diagnóstico, mecanismo de acción), secundarias ≥3 (causa-efecto, representación, mecanismo de acción); mono `def` ≥1, `fis` ≥2, `cli` ≥1, `dx` ≥1, `tx` ≥1 (mecanismo), `seg` ≥1. `pan` y `sin` sin diagramas. Cada diagrama: `div.dg-t` (título en tipo oración), ≥1 `div.dg-row`, nodos `div.dg-n` de ≤12 palabras, flechas `div.dg-ar` con `span.dg-lab` opcional (≤4 palabras: «activa», «inhibe», «produce»), columnas `div.dg-col` para ramas paralelas, y `figcaption.mini` que dice cómo leerlo en una frase. Color por rol, igual en todo el widget: `fr` terreno o factor de riesgo; `b` mecanismo biológico; `p` fenómeno psicológico o examen mental; `ac` estructura o proceso normal y fármacos; `s` efecto protector o terapéutico; `ro` daño, signo de alarma o desenlace grave. Un diagrama no repite texto de un párrafo: lo ordena.

**7.17 Diseño adaptable (iPhone, iPad, Mac).** El kit adapta solo: en iPhone (<600 px) los diagramas pasan a vertical y cada tabla (salvo `table.vis`) se apila en fichas con la cabecera de cada celda; en Mac e iPad horizontal (≥1100 px) la página se ensancha, la prosa conserva una línea legible y `div.duo` coloca dos bloques lado a lado. Usa `div.duo` para emparejar una explicación (`p`, `.card`, `.fey`) con su `figure.dg` o una tabla corta; exactamente dos hijos. Nunca dentro de `.duo`: `ol.tl`, nodos, `.signo`, `.qv`, `ol.steps`, `.dc`, `h2` ni PG. Nada de anchos fijos. Prueba en 390, 820, 1180 y 1440 px (`probar_navegador.js` ya los recorre).

**7.15 Profundidad.** Nivel universitario avanzado, de Examen Integral; diagnóstico, tratamiento y seguimiento, lo más profundo. Español de Ecuador; término inglés entre paréntesis solo si domina la literatura.

## 8 · Layout mono

- Orden interno de cada pestaña de contenido: PG → badge `b-pu` de la guía → `hb am` si aplica (§7.12) → segmento 1 → Feynman → … → simulador (en `dx`, `tx`, `seg`).
- Adicional (clasificación, estadiaje o segunda entidad): clave `[a-z]{2,4}`, parte `NNx_clave.html` tras la parte `NN` previa; con su etapa en `pan`.

**`pan`.** `hb az` `El tema en una frase` (≤30 palabras) → etapas → cierre.
- Etapas en orden fijo: Definición y Epidemiología (`def`, una cada una) · Etiología y fisiopatología (`fis`) · Clínica (`cli`) · Diagnóstico (`dx`) · Tratamiento (`tx`) · Seguimiento y complicaciones (`seg`); la adicional en su lugar lógico. Cadena: qué es → a quién afecta → por qué ocurre → cómo se manifiesta → cómo se confirma → cómo se trata → cómo evoluciona.
- Definición: qué la separa de lo más parecido · Epidemiología: ≤2 cifras · Fisiopatología: pasos y disparador · Clínica: signo y mecanismo en una frase · Diagnóstico: inicial vs confirmatorio · Tratamiento: por grupo, sin dosis · Seguimiento: vigilancia, complicación más temida y su señal.

**`def`.** Segmento 1 · Definición, en orden:
1. Card de definición: redacción propia y fiel ≤60 palabras (≤1 frase literal entre « », <15 palabras); badge `b-pu` con fuente y año + `[n]`; fuentes divergentes → `.mini`; no atribuible → badge `b-am` `Fuente por verificar`.
2. Card de sustrato normal (≤80 palabras): qué estructura o proceso normal se altera; cierra con `↪ Mecanismo en «Etiología y fisiopatología»`.
3. Card de criterios: formales con `[n]` o rasgos de consenso; nombra los subtipos.
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

**`vis`.** PG → badge `b-pu` → `hb am` si aplica → tabla → card «Común al grupo» → `hb ro` → pasos dx del diferencial → simulador diferencial.
- PG desde la presentación («ante X con Y, ¿qué lo separa de…?»), nunca desde el nombre de una entidad.
- Tabla: cabeceras = textos exactos de los botones `e1…eN`; filas del contrato (§11), en orden; celdas ≤12 palabras, ninguna vacía.
- «Signo que la delata» = celda `k` de la `.qv` de esa entidad; «Prueba que decide» = su paso `1.º` o `Confirma`.
- `hb ro`: banderas rojas; el primer ítem nombra la amenaza.
- Simulador diferencial: chips de hallazgos → entidad compatible + hallazgo que falta para confirmarla + conducta inicial + contrafactual; sin probabilidades. `dc-t`: `Simulador · Decisión clínica — predice la entidad antes de pulsar`.

**`eK`.** `hb az` con `hb-t` `Frente a [vecina]` (1–2 líneas: se confunde con… · se separa por…; la vecina más confundible del grupo, por defecto `e1` con el texto de su botón) → PG → badge `b-pu`. Después, exactamente 7 `h2` hijos directos de la `section`, en este orden:
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

- Badge `b-pu` con guía, sociedad y año en cada pestaña de contenido (salvo `sin`); `(solo resumen)` si no leíste más. Cita la edición realmente leída; nunca una no verificada.
- `[n]` en diagnósticos, dosis, umbrales, algoritmos y cifras, numerados por **primera aparición** recorriendo las pestañas en orden de barra; `pan` reutiliza esos números.
- `.acc.refs` con `ol.vanc`, Vancouver estricto; nivel de evidencia si la guía lo da; distingue guía, consenso, revisión o ensayo.
- PMID y DOI solo verificados; si no, omite el identificador, no la referencia.
- Prioridad: adjuntos → sílabo del caso y su bibliografía → guía vigente (internacional + GPC MSP) → libros de la tabla de ediciones; Latinoamérica y Ecuador si existen.
- **Bibliografía por defecto = la del sílabo del caso, con sus ediciones.** 1.ª rotación: Harrison 22e 2025; Farreras-Rozman 20.ª ed. 2024 (el sílabo dice «22.ª»: error, decláralo como discrepancia). 2.ª rotación: el sílabo cita ediciones viejas de Harrison (19) y Farreras (17); usa las vigentes de la tabla de `protocolo_verificacion.md` § 4 y mantén los libros complementarios del sílabo: Fitzpatrick Atlas 9e 2023, Guzmán Dermatología 8e 2024, Soutor Dermatología clínica 2e 2023, Kane Geriatría clínica 8e 2018, Ebert Psiquiatría 4e 2025, MSP Adultos mayores 2010. Un libro fuera de ambos: verifica su edición (protocolo § 3).
- La tabla de ediciones no lleva badge ámbar ni `[VERIFICAR]`.
- Vigencia no verificada → `.mini` `Vigencia no verificada`.
- Altitud: nota solo si un umbral sensible (Hb, Hto, PaO₂, VSG, fluidos) cambia la conducta a ~2 850 m.
- Discrepancias entre fuentes: señálalas, no las armonices.

## 11 · Contrato de marcado

No inventes clases. Emmet (`{…}`=texto); todo `button` con `type="button"`; `k` = data-tab.
- Nav `h1`+`nav.tabs>button.tb[data-tab=k][onclick="show('k')"]`
- `section.tab[data-tab=k]`·`div.hb.az|am|ro|ve|vi>div.hb-t+…`·PG `div.hb.az>div.hb-t+ol.pg>li` = 1.ª caja
- `span.badge.b-az|ro|am|ve|pu|co|rs`·`div.card`·`p.mini`·`span.tag`·`div.tw>table`·`div.stats>div.stat>b+span`
- Remisión `span.rem{↪ Posología en «…»}`; en la pestaña/h2 de su tabla: `span.rem{↓ En la tabla}`
- Acordeón `div.acc>button.acc-h[onclick="tog(this)"]{T }>span.chev{▾}` `+div.acc-b`; refs `div.acc.refs…ol.vanc>li`
- Etapa `div.etapa[data-go=k]>h3+p.res+p.perla+button.go[data-go=k][onclick="show('k')"]`
- Feynman `div.fey>span.fey-t{Explícalo como a un niño de 10 años — X}+p.fey-b+p.mini.fey-c{En medicina esto se llama… }+p.mini.fey-c{Dónde falla la comparación: }`
- Nodo `section>ol.tl>li.nodo#ID[data-clin=0|1][data-paso][data-rama?]>div.det>…+p.man{Se manifiesta como: xref}`
- Signo `div.signo#ID>h4+dl>dt{Cómo se reconoce}+dd+dt{Por qué aparece}+dd{…xref}+dt{Qué significa}+dd`
- Xref `button.xref[data-ir=ID][onclick="ir('k','ID')"]` (k del destino)
- Pasos `ol.steps.tg>li>span.tg{etiqueta}+texto`; dx `1.º·Añade·Confirma·Solo si·No pidas·Alarma` (un `1.º`); tx `Principio·De elección·Alternativa·Sintomático·Escala·Reevalúa·Especialista·Evita` (un `De elección`); sin dosis
- Qué verás `div.qv>p[data-e=p|v|a]`×≥4`+p[data-e=k]{signo xref}`
- Discrepancia `div.hb.vi>div.hb-t{Discrepancia: …}+p{… [n] <b>regla</b>}`
- Simulador `div.dc[data-fn=dcX]>div.dc-t{Simulador · Decisión clínica — …}+div.dc-g>span.dc-l+(button.chip[data-g][data-v][data-m=1?][onclick="ch(this)"]|input[type=number][data-n][oninput="ch(this)"])` `+div.out`; salida acaba en `span.cf{Si … → …}`
- `90_sim.html`: un `script`, `function dcX(dc){…}`, dosis por peso con `Math.min`; helpers `sel num out rd`; reservados `show ir tog ch sel num out rd recon tabla`
- Figura `figure.fig>img[src="data:image/jpeg;base64,…"][alt]+figcaption`
- Diagrama `figure.dg>div.dg-t{título}+div.dg-row>(div.dg-n.fr|b|p|ac|s|ro{≤12 palabras}|div.dg-col>div.dg-n…)+div.dg-ar>span.dg-lab{verbo}…` `+figcaption.mini{cómo leerlo}`
- Par adaptable `div.duo>(p|div.card|div.fey)+(figure.dg|div.tw)`
- vis: `div.tw>table.vis>thead>tr>th+th{botón eK}`…; `tbody` 9 `tr>th+td`…: `Falla central·Terreno típico·Inicio y curso·Síntoma compartido aquí·Signo que la delata·Negativo pertinente·Prueba que decide·Conducta inicial y quién maneja·Amenaza si se pierde` → `hb ro` → `ol.steps.tg` → `.dc`
- Prohibido: estilos inline, `<style>` propio, `<img>` salvo figuras de adjuntos, recursos remotos, `localStorage`/`sessionStorage`, `position:fixed`, `...` ASCII (usa `…`), `[resto igual]`, `TODO:`

## 12 · Flujo

1. Arranque (§1), Paso 0 (§2) y vigencia de la guía (§6).
2. **Manifiesto en el chat**, breve: línea del router; valores por defecto; guía (año, vigencia); fila de §3 del modo; tabla `Pestaña · Temas rectores · PG · Feynman · DC`; mapa `id · data-paso · clin · signo`; prerrequisitos; núcleo. Guárdalo en `w/manifiesto.json` (`entidades.eK` = texto exacto del botón):
   - Regla `pg`/`fey`: `{"pestaña":n}` con toda pestaña de contenido (no `pan`) cuyo n>0; una pestaña con 0 puede omitirse o escribirse (`"sin":0`); ninguna otra clave. `dc`: pestañas con simulador, en orden de barra. `nodos`/`signos`: entero (mono) u objeto por entidad (multi).
   - mono `{"modo":"mono","tabs":[],"pg":{"def":n},"fey":{"def":1},"nodos":n,"signos":n,"dc":["dx","tx","seg"],"dg":{"def":n,"fis":n},"nucleo":[≤12]}`
   - multi `{"modo":"multi","entidades":{"e1":"botón"},"principal":"e1","amenaza":"eK","tabs":[],"pg":{"vis":n,"e1":n},"fey":{"e1":n},"nodos":{"e1":n},"signos":{"e1":n},"dc":["vis","e1"],"dg":{"vis":n,"e1":n},"nucleo":{"vis":[≤5 ejes],"e1":[≤7]}}`
   - `dg`: diagramas reales por pestaña (§7.16); su presencia activa las reglas v10.2 del validador (diagramas completos, columna «Mecanismo de acción», cero `[VERIFICAR EN FUENTE]`).
3. **Partes** de contenido en orden de barra; después `01_nav` + `90_sim`; **`02_pan` al final**. Si una parte no cabe en una llamada, continúa con `cat >> parte <<'EOF'` y corta en un límite estructural limpio. **Truncar en silencio es el único fallo inaceptable.**
4. **Ensamblaje y validación en una llamada**, desde `w/` (`<Tema>` sin `/` ni `&`):
   - mono: `export LC_ALL=C; sed "s/@@TITULO@@/<Tema>/" kit_head.html > 00_head.html && cat 00_head.html 01_nav.html 02_pan.html 1*.html 90_sim.html kit_script.html > widget.html && python3 validar.py widget.html manifiesto.json`
   - multi: `export LC_ALL=C; sed "s/@@TITULO@@/<Tema>/" kit_head.html > 00_head.html && cat 00_head.html 01_nav.html 02_pan.html 05_vis.html 2[1-5]_e[1-5].html 80_sin.html 90_sim.html kit_script.html > widget.html && python3 validar.py widget.html manifiesto.json`
5. **Errores:** edición puntual, reensambla y valida; máximo 3 ciclos. Revisa los avisos; no bloquean.
6. **Entrega:** copia `widget.html` como `<slug>_widget_v10.html` (slug del tema ≤40 caracteres, guiones bajos, sin comas ni rayas: `Apendicitis_aguda_widget_v10.html`) al directorio de salida y preséntalo como archivo. Artefacto solo si se pide.
7. **Modo edición** (el adjunto es la fuente de verdad): audita (`python3 validar.py <adjunto>` + §13) y da los hallazgos en el manifiesto; divídelo en partes sin su kit, expande con ediciones puntuales, reensambla y valida; añade `Cambios por pestaña` a la salida.

## 13 · Autoverificación y salida

Autoverificación (no la muestres; corrige antes de entregar):
1. ¿Toda cifra, dosis, año, edición, PMID o DOI tiene fuente leída?
2. ¿Cada PG se responde en su pestaña?
3. ¿Todo lo de `pan` se desarrolla en su destino, con puentes y signos unidos a su mecanismo?
4. ¿Alguna analogía es falsa o paráfrasis del técnico?
5. ¿Cada `data-paso` es reconstruible, en orden causal y sin eslabones saltados?
6. ¿Posología y propiedades solo en su tabla? ¿Cada fármaco simulado está en ella?
7. ¿Cada nota de altitud cambia una conducta?
8. ¿Cada prerrequisito está definido (primera mención o sustrato)?
9. Pareto: con solo `pan` + `vis` (mono: `pan` + núcleo), ¿se nombran la entidad y su conducta inicial ante la presentación?
10. Delta (multi): ¿nada común se repite en un `eK`? ¿`vis` coincide con `.qv` y pasos?
11. ¿Cada `hb vi` corrige una fuente de Ricardo?
12. ¿El alcance y los subtemas salen del caso del sílabo (o se declaró que el tema no está)? ¿La bibliografía usa las ediciones del sílabo o de la tabla del protocolo, y las ediciones erróneas del sílabo están declaradas como discrepancia?
13. ¿Se hizo la pasada de verificación sobre `pendientes` (≤2 búsquedas por dato, ≤20 datos) y cada marca restante es de verdad un dato no confirmado?
14. ¿Hay algún sesgo quirúrgico/urológico o emoji que no corresponda al área del caso? ¿Los «signos» y «Qué verás» se adaptaron al área (examen mental, valoración geriátrica, lesión elemental)?
15. ¿Se usó el kit correcto (`kit/` del repo o `assets/kit/`) y el widget se construyó con `construir.py`?
16. ¿Cada pestaña cumple los mínimos de diagramas (§7.16), con el color por rol y sin repetir el texto?
17. ¿Toda tabla de fármacos tiene «Mecanismo de acción» con su `.xref` al nodo?
18. ¿Se revisaron capturas en iPhone (390), iPad (820 y 1180) y Mac (1440), sin desbordes ni `.duo` mal emparejados?
19. ¿Quedan cero `[VERIFICAR EN FUENTE]` tras agotar PubMed, Consensus, fichas técnicas, GPC del MSP y web?

**Salida** (nada más):
1. Manifiesto.
2. Archivo `.html` presentado.
3. Línea `RESULTADO:` del validador.
4. Línea de aviso: «Verificados N de M datos; quedan K marcas: …»; conflictos de precedencia; discrepancias nuevas propuestas para el registro, como filas `| Tema | Fuente | Dice | Regla correcta | Ref. |`; `Núcleo (Anki): …` con los ítems de `nucleo`.

Solo si Ricardo confirma una fila, escríbela en el doc de proyecto `registro-discrepancias.md` (`project_write`; créalo si falta). Sin introducción, resumen ni cierre.