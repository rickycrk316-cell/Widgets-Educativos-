---
name: Atavío · El Oficio v2
description: Sistema visual de la tienda de la fábrica. Cada pieza se ve como una hoja de patronaje bien dibujada, sobre lienzo 1080.
colors:
  ladrillo: "#A31A0E"
  profundo: "#7C0A02"
  hueso: "#F3EDE1"
  molde: "#C8A97E"
  tinta: "#2B2B2B"
  hilo: "#8A8178"
typography:
  titular-feed:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "104px"
    fontWeight: 600
    lineHeight: 1.04
    letterSpacing: "-0.01em"
    fontVariation: "'opsz' 144, 'SOFT' 50"
  titular-reel:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "118px"
    fontWeight: 600
    lineHeight: 1.04
    letterSpacing: "-0.01em"
    fontVariation: "'opsz' 144, 'SOFT' 50"
  numero-grafico:
    fontFamily: "Fraunces, Georgia, serif"
    fontSize: "320px"
    fontWeight: 600
    lineHeight: 0.9
  cuerpo:
    fontFamily: "Libre Franklin, Arial, sans-serif"
    fontSize: "36px"
    fontWeight: 400
    lineHeight: 1.4
  precio:
    fontFamily: "Libre Franklin, Arial, sans-serif"
    fontSize: "140px"
    fontWeight: 500
    lineHeight: 1
  nota:
    fontFamily: "Libre Franklin, Arial, sans-serif"
    fontSize: "28px"
    fontWeight: 400
    lineHeight: 1.35
  rotulo-taller:
    fontFamily: "Libre Franklin, Arial, sans-serif"
    fontSize: "24px"
    fontWeight: 600
    letterSpacing: "0.12em"
rounded:
  none: "0px"
  tag: "8px"
spacing:
  margen-feed: "120px"
  margen-reel: "65px"
  hebra-guion: "9px"
  hebra-espacio: "6px"
---

# Design System: Atavío · El Oficio v2

## Overview

**Creative North Star: "El patrón de molde"**

Atavío es la tienda de una fábrica, y lo que sucede en la fábrica antes de coser un pantalón es el patronaje: papel de molde, líneas de corte, muescas, flecha de hilo, tallas encajadas. Toda pieza se dibuja como una hoja de taller, con la precisión de quien sabe cortar, y se lee de un vistazo como una vendedora honesta. Se debe reconocer sin logo ni texto.

El sistema es plano, de línea y de papel. No hay sombras, degradados ni tarjetas. La profundidad viene del cambio de superficie (hueso, molde, tinta, ladrillo) y de un trazo de 4 a 5 px constante. La densidad es baja: un mensaje, un motivo, un precio.

Se rechaza explícitamente: serif rojo sobre crema con caja de foto (panadería), cajas con borde punteado, píldoras, antetítulos en mayúsculas sobre cada titular, hero-metric, rojos derivados, guiones largos en la copia y emoji.

**Key Characteristics:**
- Cuatro motivos propios: pieza de molde, costura, etiqueta colgante, cinta métrica.
- Máximo 3 colores por pieza contando el fondo; un solo rojo.
- Titular enorme (≥ 104 px) y precio sobre etiqueta, sello subordinado.
- Arte de oficio terminado en lugar de marcos de foto vacíos.

## Colors

Paleta cerrada de seis tintas del manual de marca; cada una con una sola función.

### Primary
- **Rojo ladrillo** (#A31A0E): marca y acción. Portadas y cierres, costura, titular grande, marcador de cinta. Nunca texto pequeño.

### Secondary
- **Rojo profundo** (#7C0A02): solo texto rojo pequeño o titulares rojos de uniformes y facturas; sombra tono sobre tono del ladrillo en tejido.

### Neutral
- **Hueso** (#F3EDE1): lienzo por defecto. Sustituye al blanco puro.
- **Papel de molde** (#C8A97E): hoja de patrón, etiqueta de precio, pilares Percha y Archivo, fondo de Oficio. Nunca texto (1,91:1 sobre hueso).
- **Gris tinta** (#2B2B2B): todo el texto, información y precio. Fondo del pilar Origen.
- **Gris hilo** (#8A8178): líneas de apoyo, rótulos de taller decorativos ≥ 24 px, texto secundario grande (≥ 24 px; 3,28:1 sobre hueso).

### Named Rules
**La regla de la función fija.** Ladrillo = marca y acción; tinta = información y precio; hueso = lienzo; molde = hoja de patrón y etiqueta; profundo = texto rojo pequeño; hilo = línea y secundario.
**La regla de un rojo.** Nunca un quinto rojo ni mezclas. Sin opacidades ni degradados que generen tonos nuevos.
**Fondo por pilar.** Calce = hueso; Oficio = molde; Percha = hueso + etiqueta; Origen = tinta. Portada y cierre de carrusel en ladrillo.

### Contraste (mínimo 4,5:1; 3:1 desde 24 px a lienzo 1080)
| Combinación | Ratio | Uso |
|---|---|---|
| tinta sobre hueso / hueso sobre tinta | 12,14 | texto en general |
| profundo sobre hueso | 9,47 | texto rojo pequeño |
| ladrillo sobre hueso / hueso sobre ladrillo | 6,64 | titular grande, texto hueso en portadas |
| molde sobre tinta | 6,36 | elementos y líneas sobre fondo oscuro (texto solo si es grande) |
| hilo sobre hueso | 3,28 | solo ≥ 24 px y decorativo |
| ladrillo sobre tinta | 1,83 | prohibido para texto; solo elementos grandes |
| molde sobre hueso | 1,91 | prohibido para texto |

## Typography

**Display Font:** Fraunces SemiBold, opsz 144, SOFT 50, tracking -0,01 em, `text-wrap: balance`.
**Body Font:** Libre Franklin (Regular cuerpo, Medium precio, SemiBold rótulos).

**Character:** serif cálida y grande que habla como una maestra, y una grotesca sólida que informa como una etiqueta de taller. Dos familias, nunca más.

### Hierarchy (lienzo 1080)
- **Titular feed** (SemiBold, ≥ 104 px, 1,04): máximo 3 líneas.
- **Titular reel e historia** (SemiBold, ≥ 118 px, 1,04): máximo 3 líneas.
- **Número gráfico** (SemiBold, ≥ 320 px): tono sobre tono (profundo sobre ladrillo, molde sobre hueso), elemento gráfico, no etiqueta.
- **Cuerpo** (Regular, ≥ 36 px, 1,4): 1 a 2 frases de 8 a 15 palabras.
- **Precio** (Medium, 120 a 180 px, tinta): sobre etiqueta colgante, nunca en rojo ni tachado.
- **Nota y pie** (Regular, ≥ 28 px, hilo o tinta).
- **Rótulo de taller** (SemiBold, ≥ 24 px, mayúsculas, tracking 0,12 em): solo decorativo («CORTE 04 · TALLA 32 · HILO»).

### Named Rules
**Sin antetítulo.** El titular lleva el peso; las series se identifican con la marquilla, solo en portadas de serie.
**Nada de Fraunces en párrafos.** Ni Unicode decorativo ni mayúsculas gritadas en la copia.

## Layout

Lienzo base 1080 de ancho. Feed 1080x1350 (4:5), margen lateral ≥ 120 px y contenido útil dentro del recorte 3:4 de la cuadrícula del perfil (68 px menos de ancho). Reels e historias 1080x1920 a sangrado completo: el arte ocupa los 1920 px; texto solo en la franja segura, de y = 288 a 1248 (reels) y de y = 288 a 1440 (historias), 65 px laterales y 120 px libres a la derecha en reels. Portadas de reel: titular entre y = 300 y 1240 y dentro del recorte 3:4 (y 240 a 1680); decisión de Verónica pendiente. Nada de beige vacío en el tercio inferior: ahí continúa el arte (molde, tejido, cinta) sin texto.

Logo subordinado: símbolo de 132 px en láminas interiores (mínimo del manual 120), siempre en la misma esquina (abajo a la derecha en feed); logo completo solo en portadas y cierres. Un mensaje por pieza.

Carruseles con ritmo: portada y cierre en ladrillo; interiores alternan hueso y molde; cada lámina con su composición propia; la cinta métrica marca el avance (un marcador ladrillo en la lámina actual) y sustituye el «2 / 7».

## Elevation & Depth

Plano por defecto. Sin sombras, sin bordes con tarjeta. La jerarquía se logra con escala, cambio de superficie y un trazo de línea. La única «elevación» es la hoja de molde sobre un fondo de otra tinta.

## Shapes

Esquinas limpias, contornos de molde con unión en inglete (4 a 5 px), esquinas de iconos de 2 px, etiqueta colgante con una esquina cortada y 8 px en el resto. Sin píldoras ni círculos decorativos. Muescas (V hacia adentro, 0,95 cm a escala de patrón) como forma recurrente.

## Components

### Motivo 1 · Pieza de molde
Contorno de pieza de pantalón de mujer, bota recta, con línea de corte (4 a 5 px) y línea de costura punteada, muescas, flecha de hilo con «HILO», marca de talla en Fraunces, cruz de registro en una esquina y rótulo de taller. Sobre molde u hueso (papel #C8A97E), o en línea hueso sobre tinta. Variante gradación: 28 punteado, 32 guiones, 36 continuo, encajadas con diferencias reales. **Regla:** una pieza por lámina como protagonista; escalado uniforme y recortes a sangrado permitidos; el arte provisional lleva `arte_provisional: true` en el manifest.

### Motivo 2 · Costura
Un recorrido continuo por pieza: entra por un borde, rodea o subraya lo importante y sale por otro. Guion 9 / espacio 6 (3:2) a 1080, un solo grosor de 4,5 px por pieza, puntas redondeadas; ladrillo sobre claro, hueso sobre oscuro. En carruseles la misma hebra cruza el borde y continúa (x = 1080 cae en un espacio; mismo y). **Regla:** una costura por pieza, nunca ocho usos; nunca como borde de caja, de precio, de CTA ni de marco de foto. Horizontal/vertical salvo la curva en S y el anillo definidos en la biblioteca.

### Motivo 3 · Etiqueta colgante
Cartón de molde (o hueso sobre fondo oscuro) con una esquina cortada, ojal y cordón. Contiene el precio en Libre Franklin Medium tinta y el nombre de la prenda; sustituye al sello de precio en caja punteada. Zona libre de precio: x 130 a 510, y 480 a 720 en el viewBox 640x980. **Regla:** el precio vive solo en la etiqueta; una etiqueta por pieza; el CTA se dibuja como etiqueta de texto con flecha, no como botón.

### Motivo 4 · Cinta métrica
Regla con marcas cada cm y numeración cada 5, pegada a un borde. Indicador de lámina (marcador ladrillo), separador y «talla 28 a 36». **Regla:** 0 a 45 cm en horizontal (1080), 0 a 80 cm en vertical (1920); un marcador por cinta.

### Apoyos (no son motivos)
Tejido sarga: solo textura de bloque, tono sobre tono (molde sobre hueso, profundo sobre ladrillo). Detalles ampliados (atraque en X, ojal, botón de 4 agujeros, remache, costura ampliada): arte a sangrado para láminas de oficio, con hebra y puntadas visibles. Marquilla de serie: etiqueta cosida en la esquina superior solo en portadas de serie. Cruz de registro y rótulos de taller: detalle que premia mirar de cerca.

### Iconos de destacados
Línea de 7 px, esquina de 2 px: locales, separa tu talla, tallas y telas, el taller, uniformes, garantía (guardado hasta que la garantía esté redactada).

## Do's and Don'ts

### Do:
- **Do** dibujar cada pieza como hoja de taller: una pieza o detalle protagonista y un precio sobre etiqueta.
- **Do** usar texto en gris tinta; sobre fondo oscuro, texto en hueso y rojo solo en elementos grandes.
- **Do** mantener máximo 3 colores y un solo rojo (#A31A0E; #7C0A02 solo para texto rojo pequeño).
- **Do** probar cada pieza a 390 pt de ancho; cuerpo ≥ 36 px, notas ≥ 28 px, titular ≥ 104 px (≥ 118 en reels).
- **Do** registrar el arte provisional con el tipo de foto real que lo reemplazará.
- **Do** mantener el texto dentro de las zonas seguras y la composición a sangrado completo en 9:16.

### Don't:
- **Don't** usar cajas decorativas con borde punteado, tarjetas con borde y sombra, píldoras ni hero-metric.
- **Don't** poner antetítulo en mayúsculas sobre cada titular.
- **Don't** escribir texto en #C8A97E ni rojo ladrillo sobre tinta.
- **Don't** simular fotos con personas o prendas falsas, ni mostrar marcas cliente.
- **Don't** usar guiones largos, emoji, signos de exclamación ni palabras vetadas en la copia.
- **Don't** usar la costura diagonal o en bordes de caja; no más de un grosor de costura por pieza.
- **Don't** mostrar el icono de garantía ni «3 meses» hasta que la garantía esté redactada e impresa en caja.
- **Don't** usar degradados, sombras, opacidades que inventen tonos ni un quinto rojo.
