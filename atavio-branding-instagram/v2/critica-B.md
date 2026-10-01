# Crítica B: detector + evidencia de navegador (solo evidencia)

Fecha 2026-10-01. Detector: `impeccable detect --json`, una ejecución por objetivo (código de salida 2 = hay hallazgos; sin errores en stderr). Navegador: Playwright/Chromium 1194. JSON crudos y scripts en este directorio: `detect-plantillas.json`, `detect-brandbook.json`, `medicion-brandbook.json`, `medicion-plantillas.json`, `measure-lib.js`, `run-bb.js`, `run-pl.js`.

## 1. Detector

### (a) Plantillas (32 HTML): 48 hallazgos
| Regla | N | Ubicación |
|---|---|---|
| overused-font ("Primary font: fraunces") | 23 | carrusel-durar-01..07, carrusel-percha-01..03, historia-outlet, historia-percha, post-calce, post-mensaje, post-oficio, post-origen, post-percha, reel-cierre, reel-portada-archivo, -desde-1982, -para-el, -tres-cuerpos, -voltealo |
| cream-palette (fondo rgb(243,237,225) = #F3EDE1) | 23 | avatar, carrusel-durar-02..07, carrusel-percha-02..03, destacado-garantia/-locales/-separa/-tallas/-taller/-uniformes, historia-percha, post-calce, post-oficio, post-percha, reel-overlay-dato, reel-portada-para-el, reel-portada-tres-cuerpos, whatsapp-catalogo |
| all-caps-body | 2 | post-mensaje (32 car.), reel-portada-tres-cuerpos (39 car.) |

Las líneas son 0 en todos los hallazgos (el detector trabaja sobre DOM renderizado, no da línea).

### (b) Brand book: 467 hallazgos (todos en atavio-instagram.html)
| Regla | N | Detalle |
|---|---|---|
| low-contrast | 313 | 158x #cfc8bb sobre #fff (1,7:1); 100x #f3ede1 sobre #fff (1,2:1); 40x #000 sobre #2b2b2b; 7x #000 sobre #211f1d; 2x #000/#2b2b2b (3:1); 1x #8a8178/#f3ede1 3,3:1; 1x #c8a97e/#f3ede1 1,9:1; 3x rojo/gris tinta 1,8:1 |
| undersized-ui-text (<11 px) | 117 | 25x cada uno de "Serie · pilar", "Combinación", "Lo único que cambias", "Lo que nunca se mueve" (10 px, sección plantillas); C1..C4 (10 px); "El oficio · Lámina 3" 10 px; "Locales" 10 px; "Separa tu talla"; "Av. República · Av. Isidro Ayora" 9 px |
| cramped-padding | 21 | 15x div.tw (sin inset arriba); 2x div.b-origen; 2x svg; div.safe; div.bad |
| all-caps-body | 9 | uppercase en textos de 31 a 49 caracteres |
| tight-leading | 5 | line-height 1,16 / 1,18 / 1,20 (x3), mínimo exigido 1,3 |
| tiny-text | 2 | 8,5 px (`[logo] p` "UN NUEVO CONCEPTO EN MODA") y 9 px |

### Falsos positivos justificados
- low-contrast (de los 313, 310 son falsos): el detector (jsdom) no resuelve las variables CSS ni el tema oscuro y asume fondo #fff o texto #000. Con getComputedStyle real, a 1440 y 390 en claro quedan 3 fallos y en oscuro 29 nodos en 10 grupos; los 3 fallos coinciden con las 3 filas "No" de la tabla de contraste de la sección 04. Son ejemplos intencionales de pares prohibidos, así que tampoco cuentan como defecto de lectura.
- Fallos de contraste en oscuro en `[elementos]` (span.seal "$28", small "ejemplo", span.ul-stitch, b "Ficha de tela"): ratio 1,16:1 calculado por mi medidor. Falso positivo: el fondo es una capa `linear-gradient` sólida color hueso que no resuelvo. La captura `ev-dark-stitched.png` muestra #2b2b2b sobre hueso legible.
- `[logo] text "2X"` (ratio 1,0 en oscuro): texto SVG; su relleno es el atributo fill, no `color`. Falso positivo.
- cream-palette (23) y overused-font (23): son decisiones documentadas de marca (hueso #F3EDE1 y Fraunces). Los reporto como regla del detector que dispara. No son defectos técnicos.
- Solapamiento sec-num/tag (12 en 1440): los rectángulos de Range del numeral grande exceden su caja de bloque. Las cajas de bloque no se tocan (sec-num bottom 1188 y tag top 1196 en #resumen). Falso positivo.
- "Desbordes" `li`, `a`, `b`, `[plantillas] div.sl/img/track/row/rail` a 390: contenedores con scroll horizontal. `document.scrollWidth = clientWidth = 390`, sin scroll horizontal de página.

## 2. Brand book en navegador (1440 y 390, claro y oscuro; 1183/1126 nodos de texto)

Nota metodológica: el HTML no declara @font-face; inyecté Fraunces y Libre Franklin desde build/fonts (como shoot.js). Sin eso el captura `ev-dark-color.png` muestra los titulares en la serif de reserva.

| Medición | Resultado |
|---|---|
| Contraste real | 0 fallos reales de lectura. Solo las 3 filas "No" de la sección 04 (#8a8178/#f3ede1 3,28; #c8a97e/#f3ede1 1,91; #a31a0e/#2b2b2b 1,83), y falsos positivos arriba |
| Texto < 14 px | 546 nodos a 1440 y 491 a 390. Mínimo 8,5 px. Por tamaño a 1440: 8,5 (1), 9 (4), 10 (112), 10,5 (5), 11 (120), 12 (73), 12,5 (2), 13 (160), 13,5 (69) |
| Medida de línea (140 párrafos) | 1440: 48 con línea más larga >80 car. (máx 114 en `[tipografia] p.small`, 14 px, ancho 680); 28 de 70 párrafos de ≥16 px superan 75 car. (p. ej. `[color] p` 106, `[plantillas] p` 104). 390: máx 64; 68 párrafos con línea más larga <45 car. (`[resumen] blockquote` 31) |
| Overflow de página | Ninguno (scrollWidth = clientWidth en los 4 casos) |
| Recortes por overflow:hidden | `[perfil] div.c` recorte vertical 37 px (6x) y `div.cell` (4x) a ambos anchos; `[logo] div.bad` y 2x `[color] div` recorte horizontal 10 px a 390 |
| Solapamiento de texto real | 0 |
| Targets táctiles <44 px en 390 | 8 de 25: 6x `button.btn` "Copiar HEX" (117x40), `#strip-prev` (118x40), `#strip-next` (121x40) |
| Targets <44 a 1440 (referencia) | 13 enlaces de nav lateral 187x34 más los mismos 8 botones |
| Foco visible | 26 (1440) y 25 (390) enfocables recorridos con Tab; todos con indicador (outline 3 px solid #2b2b2b, :focus-visible). Pendiente: en tema oscuro el color del outline #2b2b2b sobre fondo #211f1d tiene ~1,2:1; lo vi en `a.brand` al leer outlineColor (modo claro); no lo medí en oscuro por separado |
| U+2014 en texto visible | 0 (nodos y pseudo-elementos) |
| border-left/right >1px | 2: `[perfil] div.phone` 2 px a izquierda y derecha, color #2b2b2b (marco de teléfono, no acento de tarjeta) |
| Gradientes en texto | 0 |
| Sombras sin desplazamiento | 0 |
| Tarjetas anidadas | 0 (56 candidatas a 1440, 49 a 390) |
| Familias tipográficas | 2 (Libre Franklin 1065 nodos, Fraunces 118) |
| Tarjetas iguales en fila (3 o más) | 0 por mi criterio (mismo padre, mismo ancho y top). Observación visual: 3 columnas de swatches y 4 tarjetas C1..C4 en `#color` |

## 3. Plantillas (viewport 1080, 32 piezas; canvas 1080x1350, 1080x1920, 1080x1080 y 800x800)
- Tamaño mínimo de texto DOM: 24 px (carrusel-durar-02..05, carrusel-percha-02, historia-percha, post-calce/-oficio/-origen/-percha, reel-overlay-dato, reel-portada-*, whatsapp-catalogo), 26 px (carrusel-durar-01/06/07, carrusel-percha-01/03, historia-outlet, post-mensaje, reel-cierre), 32 px (destacado-garantia). Ningún texto <24 px.
- Contraste: 0 textos bajo 4,5:1 (3:1 si ≥24 px) en las 32 piezas, calculado sobre fondo de color/gradiente resuelto. Texto sobre foto no se puede medir (los marcadores son placeholders).
- Zonas seguras (margen 120 px, declarado en manifest): 0 textos fuera en las piezas de 1080. `whatsapp-catalogo` (800x800) tiene 4 textos a 56 px del borde izquierdo; el margen de 120 px no aplica a ese formato, solo lo consigno.
- Zona segura vertical de historias/reels (1080x1920, 250 px arriba y abajo, criterio externo no declarado en el proyecto): 1 pieza, `destacado-garantia`, texto "pendiente: se activa cuando esté impresa" con 239 px al borde inferior.
- U+2014: 0 en texto DOM de las 32 piezas. Desbordes: 0.

## 4. Pasos fallidos u omitidos
- Detector: no falló; ejecutado una vez por objetivo. Sin números de línea (0).
- Piezas sin nodos de texto DOM (avatar, destacado-locales, -separa, -tallas, -taller, -uniformes): el texto va en SVG/imagen; contraste, tamaño y zonas de su texto NO medidos (omitido; texto SVG excluido por diseño de mi medidor).
- Overlay `detect.js` / live-server: omitido, no se inyectó overlay (cobertura con medición directa de getComputedStyle).
- Contraste de texto sobre fotos/imagen real: no medible (placeholders).
- Foco en tema oscuro: color del outline no medido por separado (ver arriba). Sin pruebas de hover/disabled.
- Los CLI de detector sobre los PNG exportados no se ejecutaron (fuera del alcance).
