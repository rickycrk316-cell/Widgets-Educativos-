# Biblioteca de elementos de Atavío para Canva · v1.2

Fuente de verdad: DECISIONES-V12.md, CLAUDE.md, motifs/README.md y logo/specs.md. Los archivos son exportaciones de los motivos y de las plantillas HTML con las mismas medidas y colores. No se ha cambiado ningún color, forma ni el logo.

## Qué hay
49 elementos, 103 variantes en 8 carpetas. Cada variante tiene PNG transparente (lado mayor 2400 px; costuras largas a 2x o 3x para que la puntada se vea nítida) y, salvo las texturas, SVG apto Canva.

| Carpeta | Contenido |
|---|---|
| 01-logo | Sello principal y reducido (rojo, invertido, una tinta tinta, una tinta hueso), wordmark (rojo, tinta, hueso), avatar |
| 02-costura | Horizontal 1080 y 2160, vertical 1920, subrayado, curva en S, esquina en L, anillo, cierre con remate |
| 03-moldes | Delantero, trasero, bolsillo, pretina, gradación 28·32·36, prenda pantalón (con pespunte y simple) |
| 04-etiqueta-y-cinta | Etiqueta colgante, cinta métrica horizontal (con y sin numeración) y vertical, marcadores |
| 05-detalles-de-oficio | Atraque en X, botón de 4 agujeros, costura ampliada, ojal, remache |
| 06-texturas | Sarga (claro, oscuro, ladrillo) a 1080 × 1920 y muestra de tejido con orilla dentada |
| 07-iconos-destacados | Locales, Separa tu talla, Tallas y telas, El taller, Uniformes (trazo fino y grueso) |
| 08-apoyos | Marquilla de serie, cruz de registro, disco del sello (con y sin sello), disco de destacado, chip de dato, bloque de titular, filete, flecha de la hebra |

El icono de Garantía queda en `_pendiente/` y fuera del ZIP.

## Nombres y variantes
- `claro` = para fondo hueso o molde. `oscuro` = para fondo tinta o ladrillo.
- Costuras: `-ladrillo` sobre fondo claro, `-hueso` sobre fondo oscuro.
- Sellos: sin sufijo = rojo (hueso o tinta); `-invertido` solo sobre ladrillo y rojos; `-una-tinta-tinta` / `-una-tinta-hueso` para impresión barata, bordado y grabado.
- Iconos: sin sufijo = trazo 7 px; `-trazo-grueso` = trazo 16 px, el de los destacados de las plantillas.
- Sobre papel de molde el sello va dentro del disco hueso: usa `atavio-sello-principal-sobre-disco` o `atavio-sello-reducido-sobre-disco`.

## Cómo subirlo a Canva
1. Crea la carpeta «Atavío · Elementos v1.2».
2. Sube los SVG de cada carpeta (Subir archivos). Las texturas y los marcados «solo PNG» suben como PNG.
3. Si un SVG se ve distinto en Canva, sube el PNG del mismo nombre.
4. Brand Kit (lo haces tú, el conector no puede): colores en `kit-canva/COLORES.md` (paleta «Atavío · uso» con los seis primeros y «Solo logo» con #DA3732), fuentes en `kit-canva/fuentes/` (Fraunces SemiBold, Libre Franklin Regular, Medium y SemiBold) y logos desde `01-logo`.

## SVG apto Canva y solo PNG
Los SVG no tienen `<pattern>`, `<mask>`, `<clipPath>`, `<filter>`, `<use>` ni `<text>`. Las líneas punteadas se convirtieron en puntadas reales rellenas (cada puntada es un subtrazado) y el recorte de los detalles se resolvió con geometría. Solo hay colores de la paleta (más #DA3732 y blanco del sello). Las puntadas curvas pueden quedar a menos de 1 px de la posición original.

Solo PNG, 5 archivos: `textura-sarga-claro`, `-oscuro`, `-ladrillo`, `textura-sarga-bloque-claro` y `-oscuro`. La trama de sarga es un `<pattern>` de miles de trazos diagonales con guiones; vectorizarla pesa más de 1 MB y Canva no la reproduce igual.

## Textos que NO están en los archivos (se hacen en Canva)
Fuentes: Fraunces SemiBold (titulares y numerales) y Libre Franklin (todo lo demás). Máximo 2 familias. Tamaños para lienzo 1080.
- Titular: Fraunces 600, interlineado 1,03 (feed) o 1,02 (reel e historia), interletraje -0,01 em. Feed 104 a 112 px, reel e historia 118 a 124 px. Color ladrillo sobre hueso o molde, hueso sobre ladrillo o tinta.
- Numeral grande (carruseles «Cómo saber si…»): Fraunces 600, 560 px, interlineado 0,8, interletraje -0,02 em, tono sobre tono: papel de molde #C8A97E sobre hueso, hueso #F3EDE1 sobre molde. Va a un lado del detalle, sin tapar el titular.
- Cuerpo: Libre Franklin 400 a 36 px, interlineado 1,38 (Medium para énfasis). Nota 28 px.
- Rótulo de taller: Libre Franklin 600, 28 px, mayúsculas, interletraje 0,12 em, tinta (hilo sobre hueso en láminas interiores).
- Etiqueta colgante (viewBox 640 × 980): nombre Libre Franklin 600, 58 px, en x 130 a 510, desde y 325; precio Libre Franklin 500, interletraje -0,02 em, cifras tabulares, hasta 200 px, zona y 480 a 738; detalle 400, 40 px, desde y 775. Todo gris tinta. El precio vive solo en la etiqueta.
- Chip de dato (830 × 210): precio 500 a 112 px, talla 600 a 44 px, tela 400 a 32 px debajo. Gris tinta.
- Subtítulo de reel: bloque tinta con texto hueso Libre Franklin 600, 46 px, interlineado 1,28, relleno 18 / 32 / 22 px, ancho 640 (caja de texto con fondo).
- Marquilla de serie: texto Libre Franklin 600, 32 px a 640 de ancho de marquilla, dentro de la puntada (x 190 a 536, y 100 a 212): hueso sobre ladrillo, tinta sobre hueso.
- Flecha de texto «→» en Libre Franklin cuando no va sobre ladrillo.

## Medidas de colocación (de las plantillas)
- Marcador sobre cinta horizontal: punta en x = 18 + cm × 23,2 (centro del marcador sobre esa x), borde superior en el borde del lienzo. En carrusel de 7 láminas las posiciones de la plantilla van de x = 134 a 946.
- Marcador vertical: punta en y = 32 + cm × 23,2.
- Costura: usa siempre el mismo alto de lámina a lámina; la de 1080 empalma sin salto.
- Sello sobre molde: disco hueso 1,25 × diámetro del sello (250 px para 200, 187,5 para 150), centrado, con costura ladrillo fina.
- Destacados (1080 × 1920): textura de sarga claro de fondo, `disco-destacado` centrado en (540, 960), icono de trazo grueso centrado. Ancho aproximado del icono en el lienzo: ver tabla.

| Icono | Factor sobre el lienzo original de 1080 | Ancho del archivo recortado en la historia |
|---|---|---|
| locales | 1.12 | 726 px |
| separa-tu-talla | 1.0 | 744 px |
| tallas-y-telas | 0.84 | 618 px |
| el-taller | 0.8 | 685 px |
| uniformes | 0.84 | 618 px |

Los iconos están recortados en un cuadrado centrado en el mismo punto que el original: al centrarlos en el disco quedan donde estaban en la plantilla.

## Ajustes técnicos respecto a las plantillas
- Sarga sobre ladrillo: tinta al 38 % sobre ladrillo, como en las plantillas v1.2 (un solo rojo de paleta). El motivo original usaba rojo profundo.
- Detalles en fondo claro: la hebra va en ladrillo (antes profundo), igual que `feed-assets`.
- Costuras circulares de los discos: el periodo se ajustó una fracción de px para cerrar en puntada entera, sin muñón.
- Cierre con remate: sin la puntada recortada que dejaba la plantilla; la barra de remate está en la misma posición.
- Texturas a 1080 × 1920 (cubren feed y reel); la trama conserva el periodo de 20 px.

## Reglas que siguen vigentes
Una costura continua por pieza. Máximo 4 tintas de paleta contando el fondo; un solo rojo de paleta; #DA3732 solo en el sello. Sello en la versión de su fondo, con 12 % de aire. Sin sombras, degradados ni cajas decorativas. Nada de logo descartado ni de garantía publicable.

## Archivos
`catalogo.pdf` (miniatura, nombre, uso, regla y fondo por elemento) · `_pendiente/` · el ZIP `atavio-elementos-canva-v1.2.zip` está en la carpeta superior.
