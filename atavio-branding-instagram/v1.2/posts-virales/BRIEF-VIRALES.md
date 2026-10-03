# Brief del orquestador · 5 posts con potencial viral · Atavío v1.2

## Por qué estos cinco (lógica de viralidad)
En Instagram 2026 lo que multiplica el alcance son los **envíos por DM** y los **guardados**, no los «me gusta». Cada post está diseñado alrededor de un disparador concreto, sin romper ninguna regla de marca (Franqueza: nada que no podamos sostener).

| # | Post | Formato | Disparador | Pilar / fondo |
|---|---|---|---|---|
| 1 | «¿Cuál de estas dos costuras dura más?» | Post único 4:5 | Comentarios (juego A o B) + respuesta en el pie de foto | Oficio / molde |
| 2 | «Por qué se rompe la entrepierna (y cómo evitarlo antes de comprar)» | Carrusel 6 láminas | Envío por DM: «mándaselo a quien siempre le pasa» | Oficio / molde + hueso |
| 3 | «Lava tu jean así y no se destiñe» | Carrusel 5 láminas | Guardado: guía práctica | Calce / hueso |
| 4 | «Diccionario de taller» | Carrusel 6 láminas | Guardado + identidad: aprendes a hablar como costurera | Oficio / molde + hueso |
| 5 | «El camino corto» (de la fábrica a tu clóset) | Post único 4:5 | Envío + conversación: transparencia del precio sin intermediarios | Origen / tinta |

## Contenido exacto (no inventar más que esto)
**1 · ¿Cuál dura más?** Titular: «¿Cuál de estas dos costuras dura más?». Dos detalles ampliados lado a lado, rotulados A y B: A = costura sencilla con puntadas largas y separadas; B = costura doble con atraque en X en el extremo (usar motivos de detalle de `elementos-canva/05-detalles-de-oficio` y de costura). Línea inferior: «Respóndenos en los comentarios. La respuesta está en el pie de foto.» Pie de foto (caption) con la respuesta: B, porque la doble costura reparte la tensión y el atraque refuerza el punto donde más se jala.
**2 · Entrepierna** (6): 01 portada «Por qué se rompe la entrepierna» · 02 «Es el punto donde se cruzan cuatro costuras y donde más se jala.» · 03 «Mira si hay costura doble en el tiro.» · 04 «Busca un atraque o refuerzo donde se unen las piernas.» · 05 «Tela con cuerpo: tócala, que no se sienta delgada.» · 06 cierre «Mándaselo a quien siempre le pasa.» + «Ven a tocarla. Av. República · Av. Isidro Ayora».
**3 · Lavar el jean** (5): 01 portada «Lava tu jean así y no se destiñe» · 02 «Al revés, siempre.» · 03 «Agua fría y poco detergente.» · 04 «Sin secadora. A la sombra.» · 05 «La primera vez, lávalo solo.» + «Guárdalo para tu próxima lavada.» (consejos de cuidado genéricos y correctos; no prometer duración).
**4 · Diccionario de taller** (6): 01 portada «Diccionario de taller: 5 palabras para comprar mejor» · 02 Atraque: «Puntadas apretadas que refuerzan donde más se jala.» · 03 Pespunte: «La costura que se ve por fuera. Pareja es buena señal.» · 04 Pretina: «La banda de la cintura. Debe ir firme y sin ondas.» · 05 Tiro: «La medida de la cintura a la entrepierna. Define cómo te queda.» · 06 Bota recta: «Pierna del mismo ancho de la rodilla al tobillo.» + «Guárdalo y úsalo en el probador.» (puedes usar 5 entradas + portada = 6 láminas; cada lámina con el motivo correspondiente).
**5 · El camino corto**: titular «Aquí compras directo a quien la fabrica.» Diagrama de dos rutas en cinta métrica o costura: ruta larga «Fábrica → importador → distribuidor → tienda → tú» (gris hilo, más larga) frente a ruta corta «Fábrica → Atavío → tú» (ladrillo/hueso, corta). Sin cifras ni porcentajes (no tenemos datos). Línea: «Diseñado, cortado y terminado en Quito, desde 1982.»

Captions: escribe un pie de foto por post (máx. 125 caracteres antes del «más», 1 acción, 3-5 hashtags locales: #QuitoEcuador #HechoEnQuito #PantalónDeMujer etc.), en `captions.md`.

## Sistema (no negociable, fuente: v1.2/CLAUDE.md, DECISIONES-V12.md, DESIGN.md v2)
- Lienzo 1080×1350. Fraunces SemiBold titulares ≥ 104 px (portadas hasta 140), Libre Franklin cuerpo ≥ 36 px, notas ≥ 28 px. Fuentes locales: `atavio/build/fonts/`. Tokens: `atavio/v2/plantillas/tokens.css`.
- Colores: ladrillo #A31A0E, profundo #7C0A02, hueso #F3EDE1, molde #C8A97E, tinta #2B2B2B, hilo #8A8178. Rojo sello #DA3732 solo el logo. Máx. 4 tintas por pieza, un solo rojo de paleta. Texto nunca en molde.
- Logo: el sello de `v1.2/logo/` (reducido 150 px en interiores, principal 200 px en portadas y cierres), abajo a la derecha, área libre 12 %. Sobre molde, sello sobre disco hueso con costura ladrillo (`elementos-canva/08-apoyos/sello-*-sobre-disco`). Sobre ladrillo, invertido.
- Motivos: SOLO de `v1.2/elementos-canva/` y `v1.2/motifs/` (costura continua, molde, etiqueta, cinta métrica, detalles de oficio, sarga). Una costura por pieza; en carruseles la hebra cruza el borde entre láminas y empata.
- Márgenes laterales ≥ 120 px, contenido clave dentro del recorte 3:4. Un mensaje por lámina. Sin antetítulo en mayúsculas sobre cada titular (máx. uno por carrusel, en la portada, como marquilla de serie). Sin «—», sin «cosemos» en presente, sin exclamaciones, sin emoji, sin «premium/exclusivo/lujo/10 años/100 % nacional», sin precios inventados (estos posts no son de producto: no llevan precio).
- Craft (impeccable craft-floor + taste-skill): jerarquía por escala y color, sin tarjetas con borde y sombra, sin píldoras, sin tarjetas iguales en fila, contraste ≥ 4,5:1 (3:1 desde 24 px), detalle que premia mirar de cerca. Cada post debe ser reconocible como Atavío sin el logo.
- Indicador de lámina en carruseles: cinta métrica con marcador (como `carrusel-durar-*`). Portadas que se lean en la cuadrícula 3:4 y en miniatura de celular.

Referencias de implementación: generador del carrusel durar en `atavio/v2/_pieces/gen_feed.py` y `export_feed.js` (reutiliza su estructura y helpers).
