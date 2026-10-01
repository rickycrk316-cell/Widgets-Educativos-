# Biblioteca de motivos · Atavío v2

Generada por `v2/_build/*.py` (Python + fontTools + shapely). Todo es vector, sin `<text>` (glifos de Fraunces SemiBold opsz 144 y Libre Franklin SemiBold convertidos a trazados). Solo seis colores: #A31A0E, #7C0A02, #F3EDE1, #C8A97E, #2B2B2B, #8A8178. Sin opacidades ni degradados. Fondo transparente: el SVG no trae lienzo.

## Variantes
- `nombre.svg` = `nombre-claro.svg`: para fondo hueso o molde (líneas tinta, hebra ladrillo, hoja de molde en #C8A97E).
- `nombre-oscuro.svg`: para fondo tinta o ladrillo (líneas hueso, hebra hueso o molde, piezas solo en línea). Etiqueta colgante: `etiqueta-colgante-oscura.svg` (= `-oscuro`).
- Sin variante (un solo color de marca): `marcador*.svg`, `tejido-sarga-ladrillo.svg` (profundo sobre ladrillo).

## Trazo
Contornos de molde 4 a 5 px; hilo y líneas de apoyo 3 a 3,5 px; pespunte 4,5 px con puntas redondeadas y dasharray `4.5 10.5`: se ve como guion 9 / espacio 6 (periodo 15 px). Iconos 7 px, unión redonda, esquina 2 px. Para mostrar iconos a 110 px en destacados, subir `stroke-width` del grupo `<g>` a 12 a 14.

## Costura: continuidad entre láminas
`costura-horizontal-1080` y `-2160` empiezan en x = 5,25 con la última puntada terminando en 1074,75 / 2154,75. El borde x = 1080 cae en el centro de un espacio, por lo que la lámina 2 (mismo archivo, misma y) continúa la hebra sin salto. Usar siempre el mismo y de lámina a lámina. `costura-vertical-1920` igual para reels (periodo 15 px, empieza en y = 5,25). Curva S, esquina L y anillo entran y salen por los bordes del viewBox (1080x1350, 1080x1350, 1080x1080); el anillo (centro 540,540, radio 190) lleva un punto `id="punto"` que se puede borrar. Subrayado 1080x80, con remate (puntada atrás) en ambos extremos, se estira en horizontal solo con `preserveAspectRatio="none"` si se acepta alterar la puntada: mejor recortarlo.

## Coordenadas útiles
- **Etiqueta colgante** (viewBox 640x980). Cartón x 80 a 560, y 200 a 940, esquina cortada arriba a la izquierda. Ojal centro (345,262). Zona libre de nombre: x 130 a 510, y 330 a 440. **Zona libre de precio: x 130 a 510, y 480 a 720** (línea base fija en y = 740, x 130 a 510). Precio en Libre Franklin Medium gris tinta, hasta ~170 px de alto de cifra.
- **Marquilla de serie** (viewBox 640x310). **Zona de texto: x 190 a 536, y 100 a 212** (dentro de la puntada). Texto hueso sobre ladrillo (claro) o tinta sobre hueso (oscuro). Rótulo en Libre Franklin SemiBold mayúsculas ≥ 36 px.
- **Cinta métrica horizontal** (1080x136): 0 cm en x = 18, 23,2 px por cm, 45 cm. **Vertical** (136x1920): 0 cm en y = 32, 80 cm. Numeración cada 5. Marcas del borde al interior de la lámina.
- **Marcador** (72x176): punta en (36,170), línea de referencia x = 36. Sobre cinta horizontal: `translate(18 + cm*23.2 - 36, -170)`. `marcador-vertical` (176x72): punta en (6,36); `translate(136 - 6, 32 + cm*23.2 - 36)`.
- **Moldes**: viewBox propio por pieza (delantero ~760x1960, trasero ~780x2020, bolsillo 1128x~1330, pretina 2056x~700, gradación 1080x1920). Escala del dibujo: delantero y trasero 16 px/cm, gradación 14,2 px/cm; las cotas son de pantalón de mujer talla 32, bota recta. Gradación: 28 punteado, 32 guiones (ladrillo), 36 continuo; diferencias de cintura (+2,5 cm por cuarto de pieza por talla), rise (+1,3 cm), largo (+1,8 cm), bajo y rodilla (+0,8 cm por lado).
- **Detalles** (viewBox 1000x1000): atraque en X, ojal, botón de 4 agujeros, remache, costura ampliada con escala de 1 cm. Se pueden recortar a sangrado; los marcos de tela son parte del dibujo.
- **Iconos** (iconos/, viewBox 1080x1080): locales, separa-tu-talla, tallas-y-telas, el-taller, uniformes, garantia (no usar hasta que la garantía esté redactada).

## Reglas de uso resumidas
Una costura por pieza. Moldes: no escalar de forma no uniforme; el número de talla y «CORTE 04 · TALLA 32 · HILO» son decoración (≥ 24 px a 1080). Hoja de contactos: `hoja-de-motivos.png`.
