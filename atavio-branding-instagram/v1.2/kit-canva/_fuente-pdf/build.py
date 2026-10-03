# Genera «Atavío · Brand Guidelines para Canva» (PDF A4) pensado para el Brand Kit Builder de Canva.
# Texto real, fuentes estáticas con nombre, HEX escritos, secciones con títulos bilingües.
import re, pathlib, subprocess, json

V = pathlib.Path("/home/user/Widgets-Educativos-/atavio-branding-instagram/v1.2")
OUT = pathlib.Path(__file__).parent
F = V / "kit-canva" / "fuentes"
LOGO = V / "logo"
MOT = V / "motifs"


def svg(path, style=""):
    s = pathlib.Path(path).read_text()
    s = re.sub(r"<\?xml.*?\?>", "", s)
    s = re.sub(r"<title>.*?</title>", "", s, flags=re.S)
    s = re.sub(r"\swidth=\"[^\"]*\"", "", s, count=1)
    s = re.sub(r"\sheight=\"[^\"]*\"", "", s, count=1)
    return s.replace("<svg ", '<svg style="%s" ' % style, 1)


COLORS = [
    ("Rojo ladrillo", "Brick Red", "#A31A0E", "163 · 26 · 14", "Color principal de marca. Superficies, acentos, costura, titulares grandes.", "#F3EDE1"),
    ("Rojo profundo", "Deep Red", "#7C0A02", "124 · 10 · 2", "Rojo cuando tiene que ser texto: titulares pequeños, facturas, uniformes.", "#F3EDE1"),
    ("Hueso", "Bone", "#F3EDE1", "243 · 237 · 225", "Fondo por defecto. Sustituye al blanco puro.", "#2B2B2B"),
    ("Papel de molde", "Pattern Paper", "#C8A97E", "200 · 169 · 126", "Fondos secundarios, hoja de patrón, etiqueta de precio. Nunca para texto.", "#2B2B2B"),
    ("Gris tinta", "Ink Gray", "#2B2B2B", "43 · 43 · 43", "Todo el texto y el precio. Sustituye al negro puro.", "#F3EDE1"),
    ("Gris hilo", "Thread Gray", "#8A8178", "138 · 129 · 120", "Líneas y texto secundario grande (24 px o más).", "#F3EDE1"),
]


def css():
    faces = "".join(
        '@font-face{font-family:"%s";src:url("file://%s") format("truetype");font-weight:%d;font-style:normal}' % (fam, F / fn, w)
        for fam, fn, w in [("Fraunces", "Fraunces-Regular.ttf", 400), ("Fraunces", "Fraunces-SemiBold.ttf", 600),
                           ("Libre Franklin", "LibreFranklin-Regular.ttf", 400), ("Libre Franklin", "LibreFranklin-Medium.ttf", 500),
                           ("Libre Franklin", "LibreFranklin-SemiBold.ttf", 600)])
    return faces + """
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#F3EDE1;color:#2B2B2B;font-family:"Libre Franklin",sans-serif;font-size:10.5pt;line-height:1.5}
.page{width:210mm;height:297mm;padding:22mm 20mm 20mm;position:relative;overflow:hidden;page-break-after:always;background:#F3EDE1}
.page:last-child{page-break-after:auto}
h1,h2,h3{font-family:"Fraunces",serif;font-weight:600;color:#2B2B2B;line-height:1.1;text-wrap:balance}
h1{font-size:40pt;margin-bottom:5mm}
h2{font-size:24pt;margin-bottom:2mm}
h2 .en{display:block;font-family:"Libre Franklin",sans-serif;font-weight:500;font-size:10pt;color:#8A8178;margin-top:1.5mm;letter-spacing:.02em}
h3{font-size:13pt;margin:6mm 0 2mm}
p{max-width:150mm;margin-bottom:2.6mm}
.lead{font-size:12.5pt;line-height:1.45;max-width:155mm}
.small{font-size:8.5pt;line-height:1.4;color:#2B2B2B}
.stitch{height:4px;margin:5mm 0 6mm;background:repeating-linear-gradient(90deg,#A31A0E 0 3.2mm,transparent 3.2mm 5.3mm);width:100%}
.foot{position:absolute;left:20mm;right:20mm;bottom:10mm;display:flex;justify-content:space-between;font-size:8pt;color:#8A8178;border-top:.3mm solid #C8A97E;padding-top:2.5mm}
table{width:100%;border-collapse:collapse;font-size:9.5pt}
th{text-align:left;font-weight:600;font-size:8.5pt;color:#8A8178;padding:2mm 2mm 2mm 0;border-bottom:.4mm solid #2B2B2B}
td{padding:2.4mm 2mm 2.4mm 0;border-bottom:.25mm solid #C8A97E;vertical-align:top}
.sw{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm}
.sw .chip{height:30mm;padding:3mm;display:flex;align-items:flex-end;font-weight:600;font-size:11pt}
.sw .meta{font-size:8.8pt;line-height:1.4;margin-top:2mm}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:8mm}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm}
.box{background:#EAE2D2;padding:4mm}
.lg{display:flex;align-items:center;justify-content:center;height:44mm}
.cap{font-size:8.8pt;line-height:1.35;margin-top:2mm}
.spec{border-top:.3mm solid #C8A97E;padding:4mm 0}
.spec .k{font-size:8.5pt;color:#8A8178;font-weight:500}
ul{padding-left:4.5mm;max-width:155mm}
li{margin-bottom:1.6mm}
.no{color:#7C0A02;font-weight:600}
b,strong{font-weight:600}
.compact{font-size:9.8pt}
.compact td{padding:1.7mm 2mm 1.7mm 0}
.compact h3{margin:4.5mm 0 1.5mm}
.compact .lead{font-size:11.5pt}
.compact li{margin-bottom:1mm}
"""


def foot(n, sec):
    return '<div class="foot"><span>Atavío · Brand Guidelines · v1.2 · Octubre 2026</span><span>%s · %d</span></div>' % (sec, n)


pages = []

# 1 Portada
pages.append(f'''<section class="page" style="display:flex;flex-direction:column">
{svg(LOGO/"atavio-sello-principal.svg","width:92mm;height:92mm;margin:6mm 0 14mm -2mm")}
<h1>Atavío<br>Brand Guidelines</h1>
<p class="lead">Guía de marca para el kit de Canva. Logo, colores, tipografía, voz de marca, recursos gráficos y reglas de Instagram, en una sola fuente.</p>
<div class="stitch"></div>
<table style="max-width:150mm"><tr><td style="width:40mm"><b>Marca</b></td><td>Atavío, la tienda de la fábrica</td></tr>
<tr><td><b>Empresa</b></td><td>Siray SAS · Almacenes Atavío · Quito, Ecuador</td></tr>
<tr><td><b>Versión</b></td><td>1.2 · 1 de octubre de 2026</td></tr>
<tr><td><b>Idioma</b></td><td>Español de Ecuador</td></tr>
<tr><td><b>Instagram</b></td><td>@atavio.ecuador</td></tr></table>
<div style="flex:1"></div>
{foot(1,"Portada")}</section>''')

# 2 Marca
pages.append(f'''<section class="page"><h2>Sobre la marca<span class="en">About the brand · Brand overview</span></h2>
<div class="stitch"></div>
<p class="lead"><b>Atavío es la tienda de la fábrica.</b> No es una marca de ropa: es la tienda de Siray SAS, una fábrica de confección quiteña que opera desde 1982. Aquí compras directo a quien la fabrica.</p>
<h3>Posicionamiento</h3>
<p>Para las familias quiteñas que quieren ropa que les dure y les quede bien sin pagar de más, Atavío es la tienda de una fábrica ecuatoriana con oficio desde 1982. La ropa cuesta menos porque no pasa por intermediarios, y está mejor hecha porque la diseña, corta y revisa la misma gente que te la vende.</p>
<h3>Público</h3>
<p>Mujer quiteña de 30 a 55 años (rango real de 25 a 80) que compra para sí y para su familia, a menudo acompañada. Hombre de 30 o más que compra pantalón clásico. Lo que cierra la venta es tocar la tela y verse en el espejo.</p>
<h3>Valores</h3>
<table><tr><th style="width:30mm">Valor</th><th>Qué significa</th><th>Qué nos obliga a hacer</th></tr>
<tr><td><b>Oficio</b></td><td>Hacemos ropa desde 1982. Sabemos por qué una prenda dura.</td><td>Explicar lo técnico en vez de adornarlo. Mostrar el taller.</td></tr>
<tr><td><b>Dignidad</b></td><td>Todos merecen vestir bien y ser bien atendidos.</td><td>Tallas completas al mismo precio. Buen trato sin importar cuánto gaste.</td></tr>
<tr><td><b>Franqueza</b></td><td>Decimos lo que sí podemos y lo que no.</td><td>Demostrar en vez de prometer.</td></tr></table>
<h3>Personalidad</h3>
<p>Arquetipo: el Creador, con el Sabio como secundario. Atavío es la maestra que te enseña a mirar una costura por dentro y luego te deja decidir. Con oficio, directa, cálida y ecuatoriana, sin caricatura. Accesible, nunca aspiracional.</p>
<h3>Locales</h3>
<p>Dos locales, ambos en Quito: Av. República (cerca del CC El Jardín) y Av. Isidro Ayora (Carcelén).</p>
{foot(2,"Sobre la marca")}</section>''')

# 3 Logo
logos = [("atavio-sello-principal.svg", "#F3EDE1", "<b>Principal.</b> Círculo rojo #DA3732, nombre en blanco y bajada «La tienda de la fábrica». Mínimo 172 px o 45 mm."),
         ("atavio-sello-reducido.svg", "#F3EDE1", "<b>Reducido.</b> Sin bajada. Redes, esquina de piezas, etiquetas. Mínimo 64 px."),
         ("atavio-sello-invertido.svg", "#A31A0E", "<b>Invertido.</b> Círculo hueso, letras rojas. Solo sobre fondo rojo ladrillo."),
         ("atavio-sello-una-tinta-tinta.svg", "#F3EDE1", "<b>Una tinta, gris tinta.</b> Impresión a un color, bordado, grabado."),
         ("atavio-sello-una-tinta-hueso.svg", "#2B2B2B", "<b>Una tinta, hueso.</b> El mismo uso sobre fondos oscuros."),
         ("atavio-wordmark.svg", "#F3EDE1", "<b>Wordmark.</b> Solo el nombre, para usos lineales.")]
cells = "".join(f'<div><div class="lg" style="background:{bg}">{svg(LOGO/f, "height:34mm;width:auto;max-width:48mm")}</div><div class="cap">{c}</div></div>' for f, bg, c in logos)
pages.append(f'''<section class="page"><h2>Logo<span class="en">Logo · Brand mark · El sello</span></h2>
<div class="stitch"></div>
<p>El logo de Atavío es un sello: un círculo rojo relleno #DA3732 con el nombre «Atavío» en blanco, en letras finas dibujadas a medida, y la bajada «LA TIENDA DE LA FÁBRICA». Es el mismo sello que la marca usa en su fachada y en su perfil de Instagram.</p>
<div class="grid3" style="margin-top:5mm">{cells}</div>
<h3>Reglas</h3>
<ul><li>Siempre círculo relleno. Área libre alrededor: 12 % del diámetro por cada lado.</li>
<li>Por fondo: sobre hueso o gris tinta, el sello rojo. Sobre rojo ladrillo, el invertido. Sobre papel de molde, el sello rojo sobre un disco hueso.</li>
<li>Avatar de Instagram: sello reducido a sangre, sin bajada.</li>
<li><span class="no">Nunca</span> abrirlo como anillo, cambiar el rojo, poner letras de otro color, usar la bajada antigua «Un nuevo concepto en moda», deformarlo, rotarlo, ni añadir sombra, degradado o contorno.</li></ul>
{foot(3,"Logo")}</section>''')

# 4 Colores
sw = "".join(f'<div><div class="chip" style="background:{h};color:{fg};{ "outline:.3mm solid #C8A97E;outline-offset:-.3mm;" if h=="#F3EDE1" else ""}">{h}</div><div class="meta"><b>{es}</b> · {en}<br>HEX {h} · RGB {rgb}<br>{use}</div></div>' for es, en, h, rgb, use, fg in COLORS)
pages.append(f'''<section class="page"><h2>Colores de marca<span class="en">Brand colors · Color palette</span></h2>
<div class="stitch"></div>
<p>Paleta principal de Atavío: seis colores. Hueso es el fondo por defecto, gris tinta es el color de todo el texto y rojo ladrillo es el color de marca.</p>
<div class="sw" style="margin-top:4mm">{sw}</div>
<h3>Color del logo (no forma parte de la paleta de uso)</h3>
<div style="display:flex;gap:5mm;align-items:center"><div style="width:30mm;height:16mm;background:#DA3732;display:flex;align-items:flex-end;padding:2mm;color:#FFFFFF;font-weight:600">#DA3732</div>
<p class="small" style="margin:0"><b>Rojo sello</b> · Logo Red · HEX #DA3732 · RGB 218 · 55 · 50. Exclusivo del logo. No se usa en texto, fondos, acentos ni gráficos.</p></div>
<h3>Reglas de color</h3>
<ul><li>Máximo 4 tintas de la paleta por pieza, contando el fondo. El logo, las fotos y el hilo gris de los gráficos no cuentan.</li>
<li>Un solo rojo de paleta por pieza: ladrillo o profundo.</li>
<li>Texto en gris tinta. Rojo solo en titulares grandes. Nunca texto en papel de molde.</li>
<li>Sobre fondo gris tinta: texto hueso, y el rojo solo en elementos grandes.</li></ul>
{foot(4,"Colores")}</section>''')

# 5 Tipografía
pages.append(f'''<section class="page"><h2>Tipografía<span class="en">Typography · Brand fonts</span></h2>
<div class="stitch"></div>
<p>Dos familias tipográficas, gratuitas, con licencia SIL Open Font License. Las dos están en Google Fonts.</p>
<div class="spec"><div class="k">Título · Heading · Fraunces SemiBold</div><div style="font-family:Fraunces;font-weight:600;font-size:34pt;line-height:1.05">Voltéala y mira la costura.</div></div>
<div class="spec"><div class="k">Subtítulo · Subheading · Fraunces Regular</div><div style="font-family:Fraunces;font-weight:400;font-size:20pt;line-height:1.2">Diseñado, cortado y terminado en Quito.</div></div>
<div class="spec"><div class="k">Cuerpo · Body text · Libre Franklin Regular</div><div style="font-size:12pt;line-height:1.5;max-width:150mm">Este pantalón lo cortamos y lo revisamos aquí, en Quito. Voltéalo al revés y mira el bolsillo: ese atraque es el que aguanta el uso diario.</div></div>
<div class="spec"><div class="k">Precio y datos · Price · Libre Franklin Medium</div><div style="font-weight:500;font-size:26pt;line-height:1">$28 <span style="font-size:12pt">· tallas 28 a 36 · ejemplo</span></div></div>
<div class="spec"><div class="k">Etiquetas y botones · Labels · Libre Franklin SemiBold</div><div style="font-weight:600;font-size:12pt">Escríbenos para separar tu talla <svg viewBox="0 0 16 10" style="width:1em;height:.62em;vertical-align:.05em" aria-hidden="true"><path d="M1 5H14M10 1L14.5 5L10 9" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div>
<table style="margin-top:3mm"><tr><th>Rol</th><th>Fuente</th><th>Lienzo 1080 px</th><th>Impreso</th></tr>
<tr><td>Título</td><td>Fraunces SemiBold</td><td>104 a 120 px (reels 118 a 132)</td><td>26 a 48 pt</td></tr>
<tr><td>Subtítulo</td><td>Fraunces Regular o SemiBold</td><td>56 a 64 px</td><td>15 a 20 pt</td></tr>
<tr><td>Cuerpo</td><td>Libre Franklin Regular</td><td>36 px mínimo</td><td>10 a 12 pt</td></tr>
<tr><td>Precio</td><td>Libre Franklin Medium</td><td>48 a 96 px</td><td>según pieza</td></tr>
<tr><td>Notas</td><td>Libre Franklin Regular</td><td>28 px mínimo</td><td>8 a 9 pt</td></tr></table>
<p class="small" style="margin-top:3mm">Nunca más de dos familias. Nunca Fraunces en textos largos. Nunca letras decorativas Unicode. El nombre del logo es un dibujo, no una fuente.</p>
{foot(5,"Tipografía")}</section>''')

# 6 Voz
pages.append(f'''<section class="page compact"><h2>Voz de marca<span class="en">Brand voice · Tone of voice</span></h2>
<div class="stitch"></div>
<p class="lead">Atavío habla como una vendedora del local que sabe de costura: con oficio, directa y cálida. Explica en vez de prometer, dice el precio sin disculparse y deja que la clienta decida. Da argumentos, no halagos.</p>
<table><tr><th style="width:30mm">Rasgo</th><th>Así suena</th><th>Hasta dónde</th></tr>
<tr><td><b>Con oficio</b></td><td>«Esa tela la escogimos para que aguante el uso diario, no para la foto.»</td><td>Explica, no presume. Sin volverse técnico ni aburrido.</td></tr>
<tr><td><b>Directa</b></td><td>«Pruébatela. Si no te arma bien, no te la lleves.»</td><td>Directo no es seco.</td></tr>
<tr><td><b>Cálida</b></td><td>«Nos vemos el sábado, le guardo la talla.»</td><td>Sin fingir una confianza que no existe.</td></tr></table>
<h3>Cómo escribimos</h3>
<ul><li>Frases cortas, de 8 a 15 palabras.</li>
<li><b>Tú</b> en redes, carteles y etiquetas. <b>Usted</b> en la atención uno a uno (WhatsApp, mensajes, local). Nunca voseo («pasá», «mirá»).</li>
<li>Sin exclamaciones, sin MAYÚSCULAS para gritar, máximo un emoji por publicación.</li>
<li>Números con cifras: «desde 1982», «$25», «3 meses».</li>
<li>Una sola acción por pieza: «Escríbenos para separar tu talla».</li></ul>
<h3>Palabras que no usamos · y qué decimos en su lugar</h3>
<table><tr><th>No</th><th>Sí</th></tr>
<tr><td>«Dura 10 años»</td><td>Mostrar la prenda con años, en foto, con autorización</td></tr>
<tr><td>«100 % nacional»</td><td>«Diseñado, cortado y terminado en Quito»</td></tr>
<tr><td>«Cosemos» en presente</td><td>«Diseñamos, cortamos y terminamos en Quito»</td></tr>
<tr><td>«Exclusivo», «premium», «lujo»</td><td>«Bien hecho», «de oficio», «que sirve»</td></tr>
<tr><td>«¡Últimas unidades!»</td><td>Solo si es verdad, y dicho normal</td></tr>
<tr><td>«Un nuevo concepto en moda»</td><td>«La tienda de la fábrica»</td></tr></table>
<h3>Mensajes clave</h3>
<p>Aquí compras directo a quien la fabrica. · Tócala. Pruébatela. Si no te arma bien, no te la lleves. · Voltéala y mira la costura. Así se sabe. · Diseñado, cortado y terminado en Quito, desde 1982. · Te separamos tu talla. Pasas, te la pruebas y decides.</p>
{foot(6,"Voz de marca")}</section>''')

# 7 Recursos gráficos
mot = [("costura-horizontal-1080.svg", "Costura (pespunte)", "Una línea punteada continua que imita la costura de máquina. Una sola hebra por pieza, rojo ladrillo sobre claro, hueso sobre oscuro. Nunca en diagonal ni como borde de caja."),
       ("molde-delantero.svg", "Pieza de molde", "Contorno de una pieza de patronaje de pantalón, con muescas y flecha de hilo. Sobre papel de molde o hueso."),
       ("etiqueta-colgante.svg", "Etiqueta colgante", "Etiqueta de cartón con ojal. El precio vive solo aquí, en Libre Franklin Medium gris tinta."),
       ("cinta-metrica-horizontal.svg", "Cinta métrica", "Regla con marcas cada centímetro. Indica el avance en los carruseles.")]
mc = "".join(f'<div class="box" style="display:flex;gap:5mm;align-items:center"><div style="width:52mm;flex:none;display:flex;justify-content:center">{svg(MOT/f, "max-height:32mm;max-width:52mm;width:auto;height:auto")}</div><div><b>{t}</b><div class="cap">{d}</div></div></div>' for f, t, d in mot if (MOT/f).exists())
pages.append(f'''<section class="page"><h2>Recursos gráficos<span class="en">Graphics · Brand elements · Patterns</span></h2>
<div class="stitch"></div>
<p>El sistema visual se llama «patrón de molde». Usa lo que pasa en la fábrica antes de coser: papel de molde, líneas de corte, costura, etiqueta y cinta métrica.</p>
<div style="display:grid;gap:4mm;margin-top:4mm">{mc}</div>
<h3>Reglas de composición</h3>
<ul><li>Un mensaje por pieza. Márgenes laterales de 120 px como mínimo en el lienzo de 1080.</li>
<li>Logo siempre en la misma esquina de cada formato (abajo a la derecha en el feed).</li>
<li>Nunca texto sobre la parte ocupada de una foto: bloque de color sólido detrás.</li>
<li>Sin sombras, degradados, cajas decorativas, píldoras ni emoji en las piezas.</li></ul>
{foot(7,"Recursos gráficos")}</section>''')

# 8 Fotografía
pages.append(f'''<section class="page"><h2>Fotografía<span class="en">Photography · Image style</span></h2>
<div class="stitch"></div>
<p class="lead">Todo con celular y luz de ventana. La foto muestra la prenda como es: la tela del color que es, la costura visible, la prenda en cuerpos reales.</p>
<table><tr><th style="width:42mm">Tipo de foto</th><th>Qué muestra</th><th>Por qué</th></tr>
<tr><td><b>Textura y costura</b></td><td>Primer plano de la tela, el pespunte, el botón, el atraque</td><td>Lo que cierra la venta es tocar la tela</td></tr>
<tr><td><b>Calce en cuerpos distintos</b></td><td>La misma prenda en dos o tres personas de contextura diferente</td><td>Las clientas compran cuando «arma bien»</td></tr>
<tr><td><b>Taller y manos</b></td><td>Máquinas, mesa de corte, manos trabajando</td><td>Creíble e imposible de copiar</td></tr>
<tr><td><b>Prenda con años</b></td><td>Pantalones y chaquetas con años de uso, con autorización de su dueño</td><td>Prueba durabilidad sin prometer</td></tr></table>
<h3>Cómo se hace</h3>
<ul><li>Luz de ventana lateral a 90 grados. Apagar las luces del techo. Nunca sol directo ni flash.</li>
<li>Fondo hueso, gris claro o madera, ordenado.</li>
<li>Planchar la prenda y cortar hilos sueltos antes de disparar.</li>
<li>Edición mínima: exposición y balance de blancos. Sin filtros de color.</li>
<li>Toda persona en cuadro firma una autorización escrita de uso de imagen.</li>
<li><span class="no">Nunca</span> fotografiar prendas o etiquetas de marcas clientes de la fábrica.</li></ul>
{foot(8,"Fotografía")}</section>''')

# 9 Instagram y plantillas
pages.append(f'''<section class="page"><h2>Instagram y plantillas<span class="en">Social media · Templates · Formats</span></h2>
<div class="stitch"></div>
<table><tr><th>Pieza</th><th>Tamaño</th><th>Regla</th></tr>
<tr><td>Post de feed y carrusel</td><td>1080 × 1350 px (4:5)</td><td>Lo importante dentro del recorte 3:4 de la cuadrícula</td></tr>
<tr><td>Reel</td><td>1080 × 1920 px (9:16)</td><td>Sin texto en el 15 % superior ni en el 35 % inferior; 65 px laterales</td></tr>
<tr><td>Historia</td><td>1080 × 1920 px (9:16)</td><td>Sin texto en el 15 % superior ni en el 25 % inferior</td></tr>
<tr><td>Portada de destacado</td><td>1080 × 1920 px</td><td>Icono centrado dentro del círculo visible</td></tr>
<tr><td>Foto de perfil</td><td>1080 × 1080 px</td><td>Sello reducido a sangre</td></tr>
<tr><td>Catálogo de WhatsApp</td><td>800 × 800 px</td><td>Fondo hueso, prenda centrada, precio abajo</td></tr></table>
<h3>Pilares de contenido</h3>
<table><tr><th>Pilar</th><th>Peso</th><th>Fondo</th><th>Series</th></tr>
<tr><td><b>El calce</b></td><td>35 %</td><td>Hueso</td><td>Mismo pantalón, tres cuerpos · Para él</td></tr>
<tr><td><b>El oficio</b></td><td>25 %</td><td>Papel de molde</td><td>Voltéala · Cómo saber si… te va a durar</td></tr>
<tr><td><b>La percha</b></td><td>25 %</td><td>Hueso con etiqueta</td><td>Hoy en la percha · La percha de la semana</td></tr>
<tr><td><b>El origen</b></td><td>15 %</td><td>Gris tinta</td><td>Desde 1982 · El Archivo Atavío</td></tr></table>
<h3>Toda pieza de producto lleva</h3>
<p>Precio, tela y local. Una sola acción. Solo prendas con tres tallas o más en stock. Hashtags: de 3 a 5, locales y específicos.</p>
<h3>Bio del perfil</h3>
<p style="font-weight:500">La tienda de la fábrica · Quito desde 1982<br>Diseñado, cortado y terminado en Quito<br><svg viewBox="0 0 12 16" style="width:.75em;height:1em;vertical-align:-.12em" aria-hidden="true"><path d="M6 15C6 15 1 9.5 1 6A5 5 0 0 1 11 6C11 9.5 6 15 6 15Z" fill="#DA3732"/><circle cx="6" cy="6" r="1.9" fill="#F3EDE1"/></svg> Av. República · Av. Isidro Ayora<br>Separa tu talla por WhatsApp <svg viewBox="0 0 10 16" style="width:.62em;height:1em;vertical-align:-.12em" aria-hidden="true"><path d="M5 1V14M1 10L5 14.5L9 10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></p><p class="small">En Instagram el pin es el emoji de ubicación y la flecha es el símbolo de flecha hacia abajo. La bio mide 147 caracteres.</p>
{foot(9,"Instagram")}</section>''')

# 10 Resumen para el kit
summary = "".join(f"<tr><td>{es}</td><td>{h}</td><td>{use}</td></tr>" for es, en, h, rgb, use, fg in COLORS)
pages.append(f'''<section class="page"><h2>Resumen del kit<span class="en">Brand Kit summary</span></h2>
<div class="stitch"></div>
<h3>Paleta «Atavío»</h3>
<table><tr><th>Nombre</th><th>HEX</th><th>Uso</th></tr>{summary}</table>
<p class="small" style="margin-top:2mm">Paleta aparte «Solo logo»: Rojo sello #DA3732.</p>
<h3>Fuentes</h3>
<table><tr><th>Rol</th><th>Fuente</th></tr>
<tr><td>Título · Heading</td><td>Fraunces SemiBold</td></tr>
<tr><td>Subtítulo · Subheading</td><td>Fraunces Regular</td></tr>
<tr><td>Cuerpo · Body</td><td>Libre Franklin Regular</td></tr>
<tr><td>Precio y datos</td><td>Libre Franklin Medium</td></tr>
<tr><td>Etiquetas</td><td>Libre Franklin SemiBold</td></tr></table>
<h3>Voz de marca en una línea</h3>
<p>Con oficio, directa y cálida: explica en vez de prometer, en frases cortas, de tú en lo público y de usted en la atención uno a uno.</p>
<h3>Antes de publicar</h3>
<ul><li>Logo con su área libre y sobre su tamaño mínimo.</li><li>Texto en gris tinta; máximo 4 tintas; un solo rojo.</li><li>Sin palabras vetadas; sin «cosemos» en presente; durabilidad solo en pantalón, jean, gabardina y chaqueta.</li><li>Sin marcas clientes de la fábrica; solo los dos locales de Quito.</li></ul>
{foot(10,"Resumen")}</section>''')

html = '<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Atavío · Brand Guidelines v1.2</title><style>' + css() + "</style></head><body>" + "".join(pages) + "</body></html>"
(OUT / "brand-guidelines.html").write_text(html)
print("html ok", len(pages), "páginas")
