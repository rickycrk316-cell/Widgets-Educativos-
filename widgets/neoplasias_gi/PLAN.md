# Neoplasias gastrointestinales — plan del orquestador

Fuente: `fuentes/Syllabus_primera_rotacion_10mo.md` · caso «Dolor abdominal y pérdida de peso sin causa aparente (neoplasias gastrointestinales)». Objetivo: estudiar para el Examen Integral.

El caso nombra 8 cánceres (boca, esófago, estómago, duodeno, colon, hígado, páncreas, vesícula y vías biliares). La skill v10 admite máximo 5 por widget, así que va en **3 widgets**. El router (§2) lo fija el orquestador; cada ejecutor copia literal su línea como primera línea del manifiesto.

## Widget A · Cáncer del tubo digestivo alto — `alto/` (multi)

- Presentación común: síntomas digestivos altos (disfagia, odinofagia, dispepsia) con pérdida de peso o signos de alarma (anemia, sangrado, vómito persistente, masa).
- `Modo: multi · Entidades: e1=Cáncer gástrico (principal), e2=Cáncer de cavidad oral, e3=Cáncer de esófago, e4=Cáncer de duodeno · Amenaza: e1 · Override: sí`
- Eje declarado: proximal → distal (boca → esófago → duodeno), con el gástrico como principal por su frecuencia en Ecuador.
- Subtipos: esófago escamoso vs adenocarcinoma (en e3); gástrico intestinal vs difuso (Lauren) y precoz vs avanzado (en e1); lesiones premalignas en cada una (leucoplasia/eritroplasia, Barrett, gastritis atrófica/metaplasia intestinal y *H. pylori*, adenoma duodenal y PAF).
- Contenido explícito del sílabo: epidemiología y factores de riesgo, lesiones premalignas, estadiaje (TNM por entidad), manifestaciones tempranas y tardías, tamizaje y búsqueda activa, pruebas diagnósticas, algoritmo ante cribado positivo, referencia oportuna.
- Slug: `Cancer_digestivo_alto_widget_v10.html`

## Widget B · Cáncer hepatobiliopancreático — `hepatobiliopancreatico/` (multi)

- Presentación común: ictericia o dolor epigástrico/hipocondrio derecho con pérdida de peso.
- `Modo: multi · Entidades: e1=Adenocarcinoma de páncreas (principal), e2=Carcinoma hepatocelular, e3=Cáncer de vesícula biliar, e4=Colangiocarcinoma · Amenaza: e1 · Override: sí`
- Eje declarado: parénquima → vía biliar proximal → distal (hígado → vesícula → conductos), con el páncreas como principal.
- Subtipos: colangiocarcinoma intrahepático, perihiliar y distal (en e4); HCC sobre cirrosis vs sin cirrosis (en e2); lesiones premalignas (IPMN y PanIN, cirrosis y hepatitis B/C, vesícula en porcelana y pólipos >10 mm, colangitis esclerosante primaria).
- Incluir vigilancia de HCC en cirróticos (ecografía ± AFP) y signo de Courvoisier-Terrier; CA 19-9 y AFP en su tabla de pruebas con sus límites.
- Slug: `Cancer_hepatobiliopancreatico_widget_v10.html`

## Widget C · Cáncer colorrectal — `colorrectal/` (mono)

- `Modo: mono · Entidades: e1=Cáncer colorrectal · Amenaza: — · Override: sí`
- Pestaña adicional `tam` («Tamizaje y lesiones premalignas»), parte `16x_tam.html`, después de `seg` y con su etapa en `pan`. Cubre secuencia adenoma-carcinoma y vía serrada, pólipos (tipos y riesgo), síndromes hereditarios (Lynch, PAF), estrategias de tamizaje (FIT, colonoscopia, edad de inicio, intervalos) y el algoritmo ante cribado positivo, que el sílabo pide explícitamente.
- Fuentes por defecto: USPSTF 2021 (está en la bibliografía digital del sílabo), US Multi-Society Task Force, ESMO/NCCN para estadiaje y tratamiento.
- Slug: `Cancer_colorrectal_widget_v10.html`

## Reglas de contenido comunes (widget-ensenanza v10)

- Contexto Ecuador (MSP, GPC, INEC, SOLCA si hay datos sostenibles; Quito ~2 850 m), solo con datos leídos.
- Bibliografía por defecto: Harrison 22e, Farreras-Rozman (edición verificable; el sílabo cita «22a. ed. 2024», no verificada) y la guía vigente más específica.
- Kit en `kit/`; partes en `<widget>/`. **No leas ni edites** `kit_head.html`, `kit_script.html` ni `validar.py`.

## Reglas de diseño para ejecutores (kit «Vademécum»)

El orquestador rediseñó el CSS del kit con impeccable y taste-skill (dirección «Vademécum»: monografía impresa con índice de canto). Las clases son las mismas de la v10; lo visual ya está resuelto. Tu parte es que el contenido aproveche ese sistema. El orquestador comprobará cada regla con un script.

1. **Solo clases del contrato v10 (§11).** Nada de `style=`, `<style>`, clases inventadas ni recursos remotos.
2. **Toda tabla lleva `<thead>`** con la fila de cabecera en `<th>`; el cuerpo en `<tbody>`. Va siempre dentro de `div.tw`.
3. **Nada de recuadros anidados.** Ni `.card` dentro de `.card`/`.hb`/`.fey`, ni `.hb` dentro de `.hb`. Una idea por recuadro.
4. **Títulos en tipo oración**, nunca en MAYÚSCULAS ni Título De Cada Palabra. Los `hb-t` que no son literales de la skill: ≤8 palabras.
5. **Párrafos de ≤90 palabras.** Si un párrafo enumera más de 3 elementos, conviértelo en lista o tabla.
6. **Negrita con propósito:** como máximo un `<b>` por párrafo (el término que se define o la regla). En tablas, sin negrita en celdas de cuerpo salvo la primera columna.
7. **Redacción:** voz activa, español de Ecuador, sin signos de exclamación, sin muletillas («cabe destacar», «es importante mencionar», «en el mundo de», «sin lugar a dudas», «crucial», «fundamental» como relleno).
8. **Sin emojis ni pictogramas Unicode.** Solo las flechas que la skill exige (↪ ↓ ← →) y los símbolos de unidades.
9. **Cifras con unidad y fuente** (`[n]`); usa la coma decimal (3,5 mEq/L) y el espacio fino de miles cuando aplique (10 000).
10. **Etapas del Panorama y Feynman** respetan sus conteos de palabras: el kit los compone como entradas de índice y recuadros de lectura; no los alargues para «llenar».
