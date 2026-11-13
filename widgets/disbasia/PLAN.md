# Disbasia en la infancia — plan del orquestador

Fuente: `fuentes/syllabus_quirurgica2.md`, caso «DISBASIA» (Quirúrgica 2, PUCE). Sin caso problema adjunto: widgets genéricos del sílabo. Tema pediátrico: bibliografía por defecto **Nelson 22e** + Harrison/Farreras si aplica + la guía vigente más específica de cada entidad.

El caso nombra ~20 entidades. La skill v10 admite máximo 5 por widget: **4 widgets multi**, confirmados por el estudiante. El router lo fija el orquestador; cada ejecutor copia literal su línea como primera línea del manifiesto.

Contenido transversal del sílabo que **debe aparecer en el `vis` de cada widget** (como «Común al grupo» o en el diferencial, según corresponda): historia clínica dirigida del niño con disbasia (anamnesis, antecedentes, evolución temporal, caracterización del dolor), evaluación semiológica de la marcha (tipos de marcha: antálgica, de Trendelenburg, en estepaje, equina, atáxica…), signos de alarma y criterios de referencia al especialista, interpretación de pruebas (radiografía, ecografía de cadera, RM, estudios neurológicos).

## Widget A · Cojera dolorosa con fiebre o signos sistémicos — `dolorosa_sistemica/`

- Presentación común: niño que cojea o rechaza apoyar, con dolor, con o sin fiebre.
- `Modo: multi · Entidades: e1=Sinovitis transitoria de cadera (principal), e2=Artritis séptica, e3=Osteomielitis, e4=Neoplasia ósea maligna · Amenaza: e2 · Override: sí`
- Eje: inflamatoria benigna autolimitada → infección articular → infección ósea → tumor (benigno → grave, con la amenaza en e2 por la destrucción articular en horas).
- Subtipos: osteomielitis aguda hematógena, subaguda y crónica (e3); osteosarcoma y sarcoma de Ewing (e4; la leucemia como «No confundir con…» fuera del grupo).
- Criterios de Kocher (y modificaciones) como simulador de diferencial sinovitis vs artritis séptica: escala → banda → conducta, sin probabilidades (§7.10).
- Slug: `Cojera_dolorosa_sistemica_widget_v10.html` · título `Cojera dolorosa con fiebre`.

## Widget B · Cojera dolorosa mecánica según la edad — `dolorosa_mecanica/`

- Presentación común: dolor de cadera o rodilla de curso subagudo con cojera, sin fiebre, cuya causa depende de la edad (el dolor de cadera puede referirse a la rodilla).
- `Modo: multi · Entidades: e1=Enfermedad de Legg-Calvé-Perthes (principal), e2=Epifisiólisis de la cabeza femoral, e3=Enfermedad de Osgood-Schlatter · Amenaza: e2 · Override: sí`
- Eje: por edad (Perthes 4–8 años → epifisiólisis en la adolescencia temprana y obesidad → Osgood-Schlatter en adolescente deportista) y de cadera a rodilla.
- Subtipos: epifisiólisis estable vs inestable (Loder) (e2); estadios/clasificación de Perthes (Waldenström, Herring) (e1).
- Slug: `Cojera_dolorosa_mecanica_widget_v10.html` · título `Cojera dolorosa mecánica`.

## Widget C · Marcha alterada sin dolor — `sin_dolor/`

- Presentación común: alteración de la marcha sin dolor articular (asimetría, marcha de pato, caídas, debilidad).
- `Modo: multi · Entidades: e1=Displasia del desarrollo de la cadera (principal), e2=Dismetría de miembros inferiores, e3=Enfermedad neuromuscular, e4=Síndrome de Guillain-Barré · Amenaza: e4 · Override: sí`
- Eje: estructural de cadera → estructural de longitud → neuromuscular crónica → neurológica aguda (el sílabo trae Guillain-Barré como diferencial neurológico relevante).
- Subtipos: Ortolani/Barlow y Graf (e1); dismetría real vs aparente (e2); distrofia muscular de Duchenne como forma prototípica, con parálisis cerebral y atrofia muscular espinal como subtipos/vecinas (e3; «Precisión sobre el sílabo»: el sílabo dice «patología neuromuscular» genérica); variantes de Guillain-Barré (e4).
- Slug: `Marcha_sin_dolor_widget_v10.html` · título `Marcha alterada sin dolor`.

## Widget D · Alteraciones de la forma de piernas y pies — `forma_piernas_pies/`

- Presentación común: los padres consultan por la forma de las piernas o los pies, o por cómo camina el niño (rodillas juntas o separadas, «camina con los pies hacia dentro», pie plano).
- `Modo: multi · Entidades: e1=Genu varo y genu valgo (principal), e2=Anteversión femoral, e3=Pie plano, e4=Pie cavo, e5=Pie equinovaro · Amenaza: e5 · Override: sí`
- Eje: de proximal a distal (rodilla → fémur → pie) y de variante fisiológica a deformidad estructural.
- Subtipos: fisiológico vs patológico (Blount, raquitismo) en e1; perfil rotacional (anteversión femoral, torsión tibial, metatarso aducto) en e2; pie plano flexible vs rígido (coalición tarsal) en e3; pie cavo neurológico vs idiopático en e4; pie equinovaro congénito (pie zambo) en e5, con **pie varo y pie valgo** (talo valgo, astrágalo vertical) tratados como subtipos o vecinas, declarado en «Precisión sobre el sílabo».
- Amenaza e5: el pie zambo no tratado en la ventana del método de Ponseti deja secuela; el pie cavo exige descartar causa neurológica (alarma).
- Slug: `Forma_piernas_pies_widget_v10.html` · título `Forma de piernas y pies`.

## Reglas de diseño para ejecutores (kit «Vademécum»)

1. Solo clases del contrato v10 (§11). Nada de `style=`, `<style>`, clases inventadas ni recursos remotos.
2. Toda tabla con `<thead>` (fila de cabecera en `<th>`) y `<tbody>`, dentro de `div.tw`.
3. Nada de recuadros anidados (`.card` dentro de `.card`/`.hb`/`.fey`; `.hb` dentro de `.hb`).
4. Títulos en tipo oración; `hb-t` no literales ≤8 palabras.
5. Párrafos de ≤90 palabras (salvo `p.res` y Feynman); enumeraciones de más de 3 elementos → lista o tabla.
6. Como máximo un `<b>` por párrafo; sin negrita en celdas de cuerpo salvo la primera columna.
7. Voz activa, español de Ecuador, sin exclamaciones ni muletillas.
8. Sin emojis ni pictogramas Unicode (solo ↪ ↓ ← → y símbolos de unidades).
9. Coma decimal y espacio fino de miles; cifras con unidad y `[n]`.
10. Respeta los conteos de palabras de la skill; no alargues para llenar.
11. En el núcleo (Anki), cada ítem que venga de un paso `No pidas`/`Evita` conserva esa etiqueta al inicio.
12. Dosis pediátricas por peso siempre con `Math.min` al tope adulto y el tope visible (§7.10).

## Pruebas finales del orquestador

`validar.py` + `auditar_diseno.py` (router, kit intacto, reglas) + `probar_navegador.js` (herramientas v10 retiradas; widget congelado) + revisión con `.claude/skills/impeccable` adaptada + revisión clínica del orquestador.
