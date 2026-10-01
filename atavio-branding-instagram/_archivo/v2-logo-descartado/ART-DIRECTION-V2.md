# Dirección de arte v2 · Atavío Instagram · «El Oficio»

Decisión del orquestador tras la crítica dual (A: review/critica-A/critica-A.md · B: review/critica-B/critica-B.md).
Precedencia: manual de marca > esta dirección > skills (impeccable, taste, soft, redesign, brandkit).

## Veredicto que corregimos
La v1 era «tienda artesanal con buenas fuentes»: serif rojo sobre crema, rectángulo de foto, sello abajo a la derecha. Cualquier panadería de Quito podía usarla. Lo único propio era el texto. La v2 tiene que ser reconocible sin logo ni texto.

## Idea rectora: «el patrón de molde»
Atavío es la tienda de una fábrica. Lo que ocurre en la fábrica antes de coser un pantalón es el **patronaje**: papel de molde marrón, líneas de corte, muescas, flecha de hilo, tallas encajadas. Eso no lo puede usar una tienda que revende. Toda pieza se ve como una hoja de taller bien dibujada, no como una plantilla de redes.

## Cuatro motivos propios (biblioteca fija, vectorial, solo paleta de marca)
1. **Pieza de molde**: contorno de una pieza de pantalón (delantero, bolsillo, pretina, trasero) en trazo fino con **muescas** (triángulos pequeños en el borde), **flecha de hilo** (línea con puntas, texto «HILO»), marca de talla y línea de corte. Variante **gradación**: la misma pieza en tallas 28, 32 y 36, encajadas una dentro de otra (nest). Sobre papel de molde #C8A97E o hueso.
2. **Costura**: el pespunte deja de ser borde de caja. Es UN recorrido continuo por pieza: entra por un borde, rodea o subraya lo importante y sale por otro. En carruseles la misma hebra cruza el borde de lámina y continúa en la siguiente. Guion 3 : espacio 2, trazo 4 a 5 px, un solo grosor por pieza. Una costura por pieza, nunca ocho usos.
3. **Etiqueta colgante**: el precio vive en una etiqueta de cartón (rectángulo con esquina cortada, ojal, hilo corto) en papel de molde o hueso, precio grande en Libre Franklin Medium gris tinta. Reemplaza el «sello de precio» en caja punteada.
4. **Cinta métrica**: regla con marcas cada 1 cm sobre un borde. Hace de indicador de lámina en carruseles (un marcador rojo en la lámina actual), de separador y de «talla 28 a 36». Sustituye el «2 / 7».

Apoyos (no son motivos): **tejido** (sarga de jean en líneas diagonales finas, solo como textura de bloque), **detalle de costura ampliado** (atraque en X, ojal, botón de 4 agujeros, remache) dibujados en línea.

## Fotos
Las fotos reales no existen todavía y no se simulan con personas ni prendas falsas. Reemplazamos los marcos «FOTO PENDIENTE» por **arte de oficio terminado** hecho con los motivos (una pieza de molde, un atraque ampliado, una gradación de tallas). Cada pieza de arte provisional se registra en el manifest como `arte_provisional: true` con el tipo de foto real que la sustituirá y su guía de rodaje (la guía vive en el brand book y en el manifest, no dibujada en la pieza). Cuando haya foto real, ocupa el lugar del arte.

## Reglas de composición
- **Sin antetítulo en mayúsculas sobre cada titular.** El titular lleva el peso. Las series se identifican con una **marquilla** (etiqueta cosida pequeña en una esquina superior) solo en portadas de serie, no en cada pieza.
- **Titular más grande**: feed ≥ 104 px, reels e historias ≥ 118 px, máximo 3 líneas. Cuerpo mínimo 36 px (≈ 13 pt en celular). Pie y notas mínimo 28 px. Fraunces con opsz 144, SOFT 50, tracking -0.01em, `text-wrap: balance`.
- **Logo subordinado**: el símbolo/anillo reducido a 132 px (≥ 120 px del manual) en láminas interiores; logo reducido completo solo en portadas y cierres. Misma esquina (abajo a la derecha en feed). Precio y titular pesan más que el sello.
- **Reels e historias a sangrado completo**: el arte ocupa los 1920 px. El texto vive solo en la franja segura: de y = 288 a y = 1248 (reels), de y = 288 a y = 1440 (historias), 65 px de margen lateral y 120 px libres a la derecha en reels. Nada de beige vacío en el tercio inferior: ahí continúa el arte (pieza de molde, tejido, cinta), sin texto.
- **Zona segura unificada** para portadas de reel: titular dentro de y = 300 a 1240 y dentro del recorte 3:4 (y 240 a 1680). Decisión de Verónica pendiente (ver brand book).
- **Carruseles con ritmo**: la portada y el cierre en ladrillo, las interiores alternan hueso y molde; durar-02 a 05 cada una con su propia composición (atraque ampliado a sangrado; costura con dos hebras; tejido macro; ojal y botón). Un número enorme de Fraunces (≥ 320 px, tono sobre tono) como elemento gráfico, no como etiqueta. La cinta métrica marca el avance.
- **Mapa de color con función fija** (máx. 3 colores por pieza): ladrillo = marca y acción (portadas, costura, titular grande); gris tinta = información y precio; hueso = lienzo por defecto; papel de molde = hoja de patrón, etiqueta de precio, Percha y Archivo; rojo profundo #7C0A02 = solo texto rojo pequeño. Fondo fijo por pilar: Calce = hueso, Oficio = molde, Percha = hueso + etiqueta, Origen = tinta. Un solo rojo por pieza (nada de rojos derivados).
- **Sin cajas decorativas con borde punteado**, sin tarjetas con borde y sombra, sin píldoras, sin hero-metric, sin guiones largos «—» en la copia, sin emoji. Acciones que parecen botones (CTA) se dibujan como etiqueta de texto con flecha, no como botón.
- Márgenes laterales ≥ 120 px (feed); contenido útil dentro del recorte 4:5 → 3:4 (68 px menos de ancho en la cuadrícula).
- Contraste mínimo 4,5:1 (3:1 desde 24 px). Texto nunca en #C8A97E.
- Detalles que premian mirar de cerca (brandkit): cruz de registro en una esquina de piezas de molde, texto minúsculo de taller («CORTE 04 · TALLA 32 · HILO», solo decorativo ≥ 24 px), numeración de molde.

## Brand book v2 (inversionistas + equipo)
Estructura corta, menos de 8 secciones largas, sin numerar 01 a 12: La apuesta (diagnóstico y tesis en una pantalla, tres cifras máximo en frase, no rejilla de 8) · El sistema (logo, color, tipografía, los cuatro motivos) · Aplicaciones (cuadrícula del perfil en 3:4, carruseles, reels, historias, destacados, catálogo) · Cómo se produce (fotos y shot list, voz, semana de 5 horas, plantillas bloqueadas) · Pendientes. Texto cuerpo ≥ 17 px, medida 62 a 72 caracteres, notas ≥ 14 px, targets táctiles ≥ 44 px, sin recortes por overflow, margen lateral ≥ 16 px en móvil y ≥ 6vw en escritorio. Botones «Copiar HEX» solo en la sección de equipo. Incluir tres aplicaciones terminadas: cuadrícula del perfil con 9 piezas, etiqueta colgante de prenda con el sistema, y letrero de caja/probador.

## Entregables v2
`$B/v2/` : motifs/*.svg · plantillas/*.html (+ base.css) · png/ · png/thumb/ · atavio-plantillas-v2.pdf (imágenes) · canva-editable/*.pdf (texto vivo) · brandbook/atavio-instagram.html · manifest.json · DESIGN.md · PRODUCT.md.
