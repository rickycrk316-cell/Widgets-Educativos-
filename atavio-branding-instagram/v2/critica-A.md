# Critica A (revision de diseno) - Atavio, sistema visual de Instagram, brand book y logo propuesta B

Evaluador A. Metodo: inspeccion visual de las imagenes (hojas de contacto en `review/critica-A/cs-*.png`, 10 piezas a tamano real, 6 capturas del brand book desktop, 1 movil, contact sheet del logo). No se ejecuto el detector ni se leyo nada de critica-B.

Precedencia aplicada: el manual de marca manda. Los siguientes puntos son **conflicto skill vs manual**, no defectos: Fraunces y la paleta hueso + ladrillo (taste-skill 4.1/4.2 los vetan por defecto), pespunte en toda pieza, logo en la misma esquina, titular rojo sobre hueso, `Libre Franklin` como sans. Las prohibiciones de craft-floor (kicker, numeros de seccion, hero-metric) NO contradicen el manual: el manual no ordena ni kicker ni numeracion, asi que se tratan como defectos.

---

## 1. Veredicto de especificidad de diseno

**Pregunta: podria otra marca usar esto sin cambios? Respuesta: si, con tres cambios de copia.** Tapando el logo y el texto, el sistema es "tienda artesanal con buenas fuentes": serif calido en rojo sobre fondo crema, rectangulo de foto, circulo de logo abajo a la derecha. Cualquier panaderia, ceramista o tienda de uniformes de Quito encaja. Lo unico que ata el diseno a *una fabrica que cose* es la linea punteada del pespunte, y esa linea se usa como borde de caja, que es exactamente como un cupon "recorte aqui" o un marco de wireframe, no como una costura.

Lo que SI es propio y debe protegerse:
- La copia: "Mismo pantalon. Tres cuerpos.", "Volteala y mira la costura. Asi se sabe.", "Comenta TALLA y te escribimos." Es voz de vendedora, concreta, con prueba. Es lo mas ownable del paquete y esta en el texto, no en la forma.
- El anillo rojo con el nombre dentro (post-mensaje, avatar). Funciona como sello, es reconocible a 190 px.

Lo que falta: una **voz visual** (un gesto de composicion que se reconozca sin logo). Hoy hay tres gestos de plantilla: kicker en mayusculas, titular serif rojo, caja punteada. Ninguno viene del oficio.

---

## 2. Design Health Score (Nielsen, renormalizado)

Superficie: piezas estaticas de comunicacion + documento de marca navegable. Heuristicas 3, 7 y 9 n/a (las piezas no tienen estados ni flujos de error; el brand book solo tiene nav y "copiar HEX").

| # | Heuristica | Score | Hallazgo clave |
|---|---|---|---|
| 1 | Visibilidad del estado | 3 | Contador 2/7 en carruseles y barra de nav con seccion activa en el brand book. Falla: historia-percha y carrusel-durar-07 no dicen cuantas laminas quedan ni que sigue. |
| 2 | Lenguaje de la usuaria | 3 | Copia excelente ("puntadas apretadas", "Pasas, te la pruebas y decides"). Resta: "Foto pendiente" y notas tecnicas ("luz de ventana lateral 90 grados, sin flash") escritas en la pieza son lenguaje de produccion, no de clienta. |
| 3 | Control y libertad | n/a | Pieza estatica. |
| 4 | Consistencia y estandares | 3 | Muy consistente (logo, kicker, pespunte), a costa de monotonia. Falsa affordance: cajas punteadas "Escribenos por WhatsApp" (carrusel-durar-07), "Escribenos para separar tu talla" (carrusel-percha-03) y boton "Separa tu talla" (historia-percha) parecen botones y no hacen nada en imagen. |
| 5 | Prevencion de errores | 2 | Los 32 PNG con marco "FOTO PENDIENTE" se pueden publicar tal cual. No hay marca de agua ni modo "borrador" que lo impida. La zona de reel (35%) contradice el manual (25%) y el propio brand book lo marca "POR VALIDAR". |
| 6 | Reconocimiento antes que recuerdo | 3 | Series reconocibles por kicker (EL CALCE, EL OFICIO...). Destacados con icono + circulo, pero sin rotulo visible dentro del PNG (el rotulo lo pone Instagram a ~10 px). |
| 7 | Flexibilidad y eficiencia | n/a | |
| 8 | Estetica y diseno minimalista | 2 | Todo pesa casi igual: kicker, titular, caja, texto, anillo de 194 px. El logo es el segundo elemento mas pesado de la pieza, por encima del precio. |
| 9 | Recuperacion de errores | n/a | |
| 10 | Ayuda y documentacion | 3 | El brand book es completo (zonas seguras, contraste calculado, "lo unico que cambias / lo que nunca se mueve"). Resta: demasiado largo para su lector principal, 34.316 px de alto en desktop. |
| **Total** | | **19/28 (68%)** | **Aceptable, en el limite de Bueno. Solido y sin errores graves, pero generico.** |

---

## 3. Carga cognitiva

Fallos de la lista (8 items): **3 de 8 = moderada**.
- **Un solo foco: falla.** En post-calce (piezas a 1080 px) compiten kicker, titular de 2 lineas, tres cajas con icono + 4 lineas de texto cada una, 3 rotulos de talla, precio, descripcion, "En los dos locales de Quito" y el anillo. Son 13 elementos. Manual: "un mensaje por pieza".
- **Jerarquia visual: falla en carruseles y reels.** Titular, kicker y anillo tienen peso parecido (durar-02: el "1" rojo gigante, el titular en tinta y el anillo rojo pelean).
- **Memoria de trabajo / opciones: pasa** (max. 3 a 4 bloques).
- **Chunking en brand book: falla.** La seccion 01 (`l2-d-light-01-resumen`) muestra 8 cifras + tesis + 6 vinetas + 4 tarjetas + 2 cajas "North star / Vision 2031" en una pantalla. El inversor no sabe donde empezar.
- Carga extranea mayor: el texto de instruccion de foto ("Cuerpo talla 28, plano entero de frente, mismo pantalon y fondo, luz lateral 90 grados") ocupa mas area visual que cualquier otra copia de la pieza.

---

## 4. Viaje emocional (feed, 4 a 5 piezas seguidas)

1. **Pico de arranque:** post-mensaje (rojo pleno, "Aqui compras directo a quien la fabrica."). Es la mejor pieza del set: una idea, un color, mucho aire, pespunte como unica ornamentacion.
2. **Valle:** post-oficio, post-percha, carrusel-durar-02 a 05. Misma estructura de caja beige con camara. Al scrollear, el ojo aprende "es un formulario" y deja de leer.
3. **Final:** el cierre tiene la accion correcta (una sola: "Escribenos para separar tu talla"), pero es una caja punteada pequena sobre fondo vacio (carrusel-percha-03). La emocion cae justo en el momento de mayor interes (peak-end). El cierre mas fuerte esta en reel-cierre (rojo, "Comenta TALLA"), pero ocupa 35% de vacio debajo.
4. Tono: calido y directo en copia, **frio y de formulario en forma**. La promesa "maestra que te ensena a mirar una costura" no se siente: nada invita a mirar de cerca.

---

## 5. Fortalezas

1. **Disciplina de sistema.** Logo siempre abajo a la derecha, pespunte presente en las 32 piezas, maximo 3 colores, margen constante de 120 px, texto en tinta no en rojo. Esto cumple el manual y da coherencia de cuenta (cuadricula) desde el dia uno.
2. **Copia con prueba y voz de mostrador** (carrusel-durar-02: "Debe haber un refuerzo de puntadas apretadas"). Cumple reglas duras: sin "10 anos", sin "100% nacional", sin marcas cliente, una sola accion por cierre, precio + tela + local en post-calce, post-percha y whatsapp-catalogo.
3. **post-mensaje y avatar** como piezas de marca: el anillo rojo con el nombre y el pespunte exterior (avatar.png) es fuerte, legible y propio. Tambien: el contraste esta calculado y publicado en el brand book (rojo profundo sobre hueso 9,47; gris hilo reconocido como no apto para texto normal).

---

## 6. Problemas prioritarios

### [P1] Los marcos "FOTO PENDIENTE" dominan la pieza y se leen como wireframe (a)
- **Que hace:** en 20 de 32 piezas el elemento mas grande es una caja beige con icono de camara, el rotulo en mayusculas con tracking y 2 a 4 lineas de instrucciones de produccion (post-calce x3, post-oficio, post-percha, post-origen, carrusel-durar-02 a 05, carrusel-percha-02, historia-percha, whatsapp-catalogo, y los 5 reels de portada). En reel-overlay-dato la caja ES la pieza: 1080x1920 de beige con la instruccion en el centro.
- **Por que importa:** al ver la hoja de contacto, la impresion es "plantilla sin terminar". El inversor no puede imaginar el resultado; Ricardo (5 h/semana) no ve un ejemplo de buena foto. El texto de instruccion se lee mas que el titular en whatsapp-catalogo. Ademas, si una foto no llega a tiempo, la pieza sale con la caja (heuristica 5).
- **Arreglo concreto:**
  1. Generar para el brand book y el dossier una **version "con foto"**: foto de stock/propia real (o fotograma ilustrativo marcado "ejemplo") en cada marco para al menos post-calce, post-oficio, post-percha, reel-portada-tres-cuerpos y carrusel-durar-02. Una sola foto buena de costura vale mas que 20 marcos.
  2. En la version de trabajo, bajar el marco a **un icono + dos palabras** ("Foto: costura del bolsillo") a 24 px, sin cuadro de instrucciones; mover las instrucciones de toma a un documento de rodaje o a la nota de la plantilla Canva.
  3. Marcar los PNG de marco vacio con una banda diagonal de "BORRADOR" fuera de zona (solo en exportacion de revision) para que no se publiquen por accidente. Nota: la diagonal esta vetada para el pespunte, no para un sello de borrador; si se prefiere, usar banda horizontal "BORRADOR" arriba.
  4. Marco punteado: pasar a **borde solido fino o sin borde**; el punteado alrededor de un hueco es lo que dice "cupon".
- **Comando:** `/impeccable polish` (estados de placeholder) y `/impeccable shape` para el brief de la version con foto.

### [P1] No hay un motivo propio: el pespunte se usa como borde de caja y a un solo peso, y el sistema es generico (c)
- **Que hace:** la linea punteada aparece como: borde de caja de foto, borde de precio ($28 en post-percha y carrusel-percha-02), borde de CTA (carrusel-durar-07, historia-percha), subrayado ("costura", "TALLA"), franja inferior (carrusel-durar-01 a 07, carrusel-percha-01), borde de fecha (carrusel-percha-01), borde de la pieza entera (reel-overlay-dato, reel-portada-*), halo del avatar y circulo de cada destacado. Son 8 usos al mismo grosor.
- **Por que importa:** al repetirse sin variacion deja de ser costura y pasa a ser textura de borde. Una costura real tiene direccion, curva y tension (sigue un contorno de prenda, hace una esquina, termina en un remate). Aqui es un rectangulo, que es lo menos "costura" posible. Con el resto (serif crema, rojo teja, circulo) resulta una plantilla de Canva de "tienda artesanal". Respuesta a (c): **la marca tiene una buena idea, el pespunte, y la ejecucion es de plantilla; hoy no hay voz visual propia.**
- **Arreglo concreto (conservar el manual, ampliar el recurso):**
  1. Redefinir el pespunte como **linea de costura que recorre la pieza**: entra por un borde, bordea el titular o la foto, hace un giro de 90 grados con radio y sale (siempre horizontal/vertical, nunca diagonal ni ondulada: respeta el manual). Una sola costura por pieza, 3 pt, protagonista.
  2. Quitar el pespunte de CTAs, precios y marcos de foto (5 de los 8 usos). Reservarlo para: separador, subrayado de palabra clave, marco de avatar/destacado, costura-recorrido.
  3. Anadir **un segundo gesto del oficio** dentro del mismo manual: p. ej. el **etiquetado de prenda** (el sello de precio como etiqueta colgante con un ojal y el hilo), o **la marca de patron** (muesca triangular en el borde de la foto, que es lo que un cortador usa para alinear). Una vez definido, aparece en toda pieza como la forma de la foto: eso ya seria una forma que nadie mas tiene.
  4. Anadir un recurso fotografico fijo: **el plano de costura cerrada** como textura de fondo a baja opacidad en portadas (los fondos planos rojo/tinta/molde hoy estan vacios).
- **Comando:** `/impeccable shape` (definir el segundo gesto) luego `/impeccable bolder` (elevar el pespunte a recorrido).

### [P1] Reels e historias: 30% a 35% inferior vacio y composicion apilada (b)
- **Que hace:** reel-portada-tres-cuerpos (y los otros 4 portada): foto 0 a 830, titular 880 a 1130, texto hasta 1235, y de 1235 a 1920 solo hueso liso (35%). En reel-cierre: contenido termina en el anillo (y 1224), el resto es rojo plano. historia-percha: contenido hasta 1400, 520 px de vacio. historia-outlet igual.
- **Por que importa:** la zona inferior esta reservada para la interfaz de Instagram (reel-cierre-zonas lo muestra: "interfaz de Instagram, 35% inferior desde 1248 px"), asi que el vacio es *legitimo* en el reproductor. Pero la **portada** (lo que se ve en la cuadricula 3:4, y = 240 a 1680) deja 445 px de vacio de 1440 = 31% del tile sin nada, ademas de que la foto queda recortada a 590 px. En la cuadricula, cinco portadas parecen "titulo + caja + nada". El manual dice 25%, la plantilla 35%: contradiccion no resuelta.
- **Arreglo concreto:**
  1. Portada de reel = **foto de sangrado completo** (0 a 1920) con el titular sobre bloque solido hueso/tinta en el tercio central (y 640 a 1100), nunca sobre la parte ocupada de la foto (manual). La foto llena la zona inferior; la UI se superpone a la foto, no a beige.
  2. Para historias sin foto (outlet, cierre): subir el bloque tipografico hasta centrarlo opticamente en 15% a 65% y usar la zona inferior para una **textura de tela/costura a baja opacidad** o el pespunte-recorrido, no vacio.
  3. Decidir de una vez 25% vs 35% (el brand book lo declara "por validar") y poner un solo valor en el manual, CLAUDE.md y plantillas.
- **Comando:** `/impeccable layout`.

### [P2] Titular: buena presencia en el lienzo, pequeno en el celular, y compite con kicker y logo (d, e)
- **Que hace:** titular Fraunces a ~92 px de cuerpo (post-calce, post-oficio, reel-portada-*) y ~44 px en pantallas secundarias (carrusel-durar-02 a 05 titulo a ~46 px; historia-percha "Hoy en la percha" ~64 px). El kicker va a ~24 px con tracking.
- **Por que importa:** a 1080 px el titular de post-calce y post-mensaje pega bien. En un celular de 390 pt el lienzo se escala a 0,36: el titular de 92 px queda en ~33 pt (bien), pero el cuerpo de 30 px queda a ~11 pt, el kicker a ~9 pt y la instruccion de foto a ~9 pt, por debajo de lo legible en exteriores. En carruseles 2 a 5 el titulo en tinta de 46 px (~17 pt) tiene menos peso que el numero rojo "1" (155 px) y que el anillo (194 px). Respuesta a (e): **el logo funciona como boton** porque es un circulo con borde grueso y texto adentro, igual a un chip de avatar/boton circular, de 194 px (18% del ancho) en TODAS las piezas, incluso en carruseles de 7 laminas (7 apariciones consecutivas). En post-calce pesa mas que el precio $28. Es una orden del manual (misma esquina), pero no el tamano.
- **Arreglo concreto:** titular minimo 84 px en todo feed/lamina interna; cuerpo minimo 36 px (a 390 pt = 13 pt); eliminar el kicker en piezas de una sola idea (ver abajo); logo: reducir a **132 px (areas de seguridad 2X conservadas)** en laminas 2 a n de carrusel y usar el simbolo + nombre solo en portada y cierre; en historias y reels mantener 160 px. No mover de esquina.
- **Comando:** `/impeccable typeset`.

### [P2] Kicker, numeracion, hero-metric y pildoras: lo que craft-floor prohibe esta por todas partes (g)
- **Que hace:**
  - **Kicker en mayusculas sobre cada titular** en 28 de 32 piezas: "EL CALCE", "EL OFICIO · VOLTEALA", "LA PERCHA · HOY", "COMO SABER SI TE VA A DURAR", "ATAVIO · LA TIENDA DE LA FABRICA", y en reels dos niveles ("EL CALCE · MISMO PANTALON, TRES CUERPOS" repite el titular de abajo, reel-portada-tres-cuerpos). Mayusculas con tracking a ~24 px: ademas el manual (voz) pide "sin MAYUSCULAS gritadas".
  - **Numeros de seccion** 01 a 12 en rojo gigante en cada seccion del brand book (`l2-d-light-01..12`) y en la nav ("00 Portada, 01 Resumen"); contador "2/7" y "1/3" en carruseles. La secuencia de secciones del brand book no necesita numeros; los de carrusel durar si portan informacion (1,2,3,4 son los 4 puntos): esos se conservan.
  - **Hero-metric:** seccion 01 del brand book: ~2.400 / 733 / 23-jul / 59 / 85% / 0 / 22 de 24 / 41% en rejilla de numero grande + etiqueta chica + linea. Es literalmente la plantilla.
  - **Pildoras y tarjetas:** "UNA PANTALLA", "SEIS COLORES. PALETA CERRADA.", "SISTEMA VISUAL DE INSTAGRAM · V1.0 · OCTUBRE 2026" (pildora punteada con version en portada), "NORTH STAR", "VISION 2031", "POR VALIDAR", chips; tarjetas de "1 persona / $150 al mes / Celular / 6 + 4" (4 cards iguales icono-sin-icono + titulo + texto). Version "V1.0" en portada es ademas un tell de taste-skill 9.F.
- **Por que importa:** cada pieza usa la misma muletilla para decir el pilar; el kicker es el recurso que mas convierte el set en plantilla. Para el inversor, la rejilla de 8 cifras parece dashboard de startup, no una tienda de fabrica.
- **Arreglo concreto:**
  1. Feed y carrusel: eliminar el kicker. La serie se reconoce por **color de fondo + forma de la foto + el gesto propio** (P1 anterior), no por una etiqueta. Si se quiere mantener la serie, ponerla en el pie, en minuscula y 28 px, junto al local, una vez.
  2. Brand book: quitar numeros de seccion y pildoras; usar titulos en frase y una nav lateral con nombres. Reducir seccion 01 a **tres cifras** con historia ("85% de los reels pierde su audiencia en 3 segundos" como titular, no como numero de 120 px), las demas en tabla de una linea.
  3. Cuatro "cards" de capacidad: convertir en una frase de dos renglones: "1 persona, 5 horas, $150 al mes, un celular."
- **Comando:** `/impeccable distill`.

### [P2] Monotonia de carruseles y de series (f)
- **Que hace:** carrusel-durar-02, 03, 04, 05 son cuatro copias de una misma estructura: numero grande rojo a la izquierda + titulo en tinta, caja de foto del mismo ancho, parrafo, anillo, franja. carrusel-durar-06 (lista con check) y 07 (cierre) rompen un poco; 01 es portada roja. carrusel-percha-01 a 03: portada molde con caja punteada de fecha, lamina de producto, cierre. Mismo marco de foto en 3 a 4 formatos distintos.
- **Por que importa:** en carrusel el deslizar es la unica accion; sin cambio de ritmo (escala, recorte, color, orientacion de foto) no hay razon de pasar a la lamina 3. Ademas el carrusel del oficio debe ensenar a *mirar*: la foto de la costura deberia crecer, llegar a sangrado completo, mostrar un circulo de zoom. Hoy la imagen mas importante (la costura) esta en una caja de 840x430, igual que la caja de "cierre".
- **Arreglo concreto:** para durar-02 a 05, alternar: lamina 2 foto a sangrado completo con numero sobre bloque; lamina 3 foto recortada en doble pagina (la imagen continua de 3 a 4); lamina 4 foto + inserto circular de detalle; lamina 5 a doble columna. Mantener fija solo la barra de contexto (numero + pie). Un solo color por carrusel; la portada y el cierre en ladrillo.
- **Comando:** `/impeccable layout` y `/impeccable delight` (una transicion de costura continua entre laminas).

### [P3] Jerarquia de color casi plana; ladrillo hace todos los trabajos (i)
- **Que hace:** en post-calce el ladrillo esta en el titular, en 3 marcos de foto, en el anillo y en el pespunte. En carrusel-durar-02, en el "1", los 2 marcos y el anillo. Rojo profundo `#7C0A02` (el "rojo de texto") no se distingue del ladrillo a ojo en ningun PNG; solo aparece en el brand book. Tinta es solo texto y fondo oscuro; molde es fondo secundario y tambien el relleno del marco de foto (post-calce, post-oficio), de carrusel-percha-01 y reel-portada-archivo: **cuatro papeles distintos para el mismo beige**. Hueso, tinta, ladrillo y molde se alternan como fondo sin regla (post-origen tinta, post-mensaje ladrillo, carrusel-percha-01 molde), por lo que el feed rota de color por turnos y no por pilar. reel-portada-voltealo introduce un quinto rojo (el bloque superior `#A93428` aprox. mas claro).
- **Por que importa:** el color es la jerarquia mas barata. Hoy no senala nada: ni precio, ni accion, ni dato. El unico acento verdadero sobre hueso es el rojo del titular, y todo lo demas lo repite.
- **Arreglo concreto:** asignar una funcion unica a cada color: **ladrillo = solo marca** (titular grande y logo, no marco ni linea); **tinta = toda la informacion** (precio incluido, mas grande); **hueso = lienzo**; **molde = solo fichas de tela y fondos de serie "Percha"**; **rojo profundo = unica linea de accion (CTA)**. Fondos por pilar fijo: Calce = hueso, Oficio = hueso con foto sangrada, Percha = molde, Origen = tinta, mensaje = ladrillo. Eliminar el quinto rojo.
- **Comando:** `/impeccable colorize`.

### [P3] Guiones largos y rangos (h)
- **Que hace:** busqueda en `build/brandbook/atavio-instagram.html`: **0** guiones largos (—) en copia. Hay **rangos con raya corta** (–) en cifras ("~$12–15 al mes", "15–30 dias", "76–104", "1,05–1,1") en el brand book. Ninguna pieza PNG tiene raya.
- **Por que importa:** taste-skill 9.G pide guion normal en rangos; la ortografia espanola usa raya o guion segun contexto. No es defecto de marca.
- **Arreglo:** cambiar `–` por `-` en rangos del brand book si se quiere cumplir 9.G al pie; **no se detecta incumplimiento real**. Mantener el uso de "·" bajo control: aparece 3 a 4 veces por pieza ("Textura y costura", "Tallas 28 a 36 · $28 · Quito", kicker + pildora). Reducir a una por linea.
- **Comando:** `/impeccable clarify`.

---

## 7. Personas

**Jordan (primerizo, abre el feed sin contexto).** No entiende que son los marcos beige con camara: lee "FOTO PENDIENTE" como error de la cuenta. En carrusel-durar-02 el "1" rojo y el titulo parecen dos lineas separadas ("1" en una columna, titulo en otra); el circulo "Atavio" parece un boton y lo toca. Abandona en la lamina 3 porque se repite la estructura.

**Casey (movil, una mano, en la calle).** Cuerpo de 30 px a 11 pt y kicker a 9 pt ilegibles con sol. El boton "Separa tu talla" de historia-percha no es tocable (es imagen): lo toca, no pasa nada. El texto de reel-overlay-dato "$28 · talla 28 a 36" esta en bloques tinta bien contrastados, pero a 25% de la altura queda detras de los botones de la interfaz si se desplaza. El destacado-garantia lleva "pendiente: se activa cuando este impresa" a ~20 px al pie: texto interno visible.

**Sam (accesibilidad).** Contraste de pares principales correcto (tinta sobre hueso 12,14; ladrillo sobre hueso 6,64; hueso sobre ladrillo 6,64). Fallos: texto de instruccion en el marco molde (tinta sobre molde `#E3D5BE` aprox. correcto) pero a 22 a 24 px; contador 2/7 en gris hilo (3,28 contra hueso, solo cumple en "texto grande"); en destacados el icono de trazo fino (2 a 3 px sobre 1080) a 64 px de avatar real pasa a trazo de ~0,7 px. No hay texto alternativo definido para las piezas (descripcion de Instagram: pendiente). Pespunte en rojo sobre ladrillo claro (reel-portada-voltealo, borde ladrillo sobre bloque ladrillo) es casi invisible.

**Marlene, 42, vendedora-clienta quiteña que mira Instagram en el celular entre clientes.** Tiene 3 segundos. Lo que entiende de post-calce: "$28" y "Mismo pantalon. Tres cuerpos." (bien). Lo que le estorba: tres cajas con 12 lineas chicas, nada que se parezca a un pantalon o a una mujer. Con fotos reales seria excelente porque el argumento (se ve en cuerpos como el mio) es el correcto. En post-oficio le gusta "Volteala y mira la costura" pero no hay costura que mirar, hay un cuadro. Reel: la portada con 35% de beige vacio la hace pasar. La accion "Comenta TALLA" (reel-cierre) es clara y la haria. Piensa "esto es de una tienda seria" por el anillo, pero no "de la fabrica".

**Inversor que hojea el brand book en 3 minutos.** Abre la portada: logo gigante a 460 px y a la izquierda sin margen (captura desktop `l2-d-light-00-portada`: el logo y el titulo estan pegados al borde izquierdo, sin gutter; en movil `l2-m-light-top` el margen es correcto, asi que parece un defecto de captura o de contenedor desktop a verificar). Pasa a "Resumen para inversores": 8 cifras, 6 vinetas, 4 tarjetas: no encuentra el mensaje. Sigue a color: 6 muestras con 3 botones "Copiar HEX" cada una (herramienta de disenador en un documento para inversor). Plantillas: ve cajas "FOTO PENDIENTE" y piensa "no hay producto visual todavia". Conclusion en 3 minutos: "orden y disciplina, pero nada que me diga que esto lo hizo una agencia".

---

## 8. Observaciones menores

- **Logo (propuesta B, contact sheet).** Fuerte y simple. Problemas: (1) "Reducida 72 px": el nombre mide ~6 px de altura de mayuscula, apenas legible; el "principal 120 px" muestra la bajada "LA TIENDA DE LA FABRICA" a ~2 px: ilegible; el manual fija 120 px de minimo y a ese tamano la bajada no sirve. Sube el minimo de la version con bajada a 200 px o publica solo el simbolo+nombre. (2) El "Simbolo" es un anillo vacio: sin el nombre es un circulo rojo generico (se parece a un indicador de grabacion). CLAUDE.md describe "anillo rojo **abierto**"; los archivos B muestran un anillo **cerrado**. Si "abierto" es una abertura en el trazo, esa abertura (como el ojo de una aguja o un hilo sin cerrar) es el rasgo propio que falta y que haria reconocible el simbolo solo. (3) El avatar de 1080 con halo punteado a 110 y 72 px se vuelve borde sucio.
- **post-oficio:** la linea punteada debajo de "costura" cae a 2 px del ascendente de "Asi se sabe"; casi toca. Subir interlineado o bajar el subrayado 10 px.
- **post-percha, carrusel-percha-02, historia-percha:** el precio $28 en caja punteada sobre fondo igual, a 62 px, es debil; es el dato que cierra la venta. Subir a 96 px en tinta sin caja.
- **destacados:** los 6 iconos son del mismo estilo y escala (bien) pero el taller (maquina) y tallas (cinta) son dibujos genericos; en circulo de pespunte con el icono fino queda "ficha de app", no oficio. Usar un detalle fotografico de cada tema en el circulo.
- **whatsapp-catalogo (800x800):** marco de 340 px para la prenda y la prenda tiene que centrarse; el precio a la derecha ($28) a 40 px esta bien. La caja de foto ocupa el 45% del cuadrado.
- **Brand book:** tres modos (claro/oscuro, desktop/movil) bien resueltos; en `l2-d-light-*` el contenido arranca en x=0 (sin gutter). La seccion 09 tiene 8.594 px de alto: partirla en paginas.
- **Contraste/tamano de texto en cajas de foto:** 22 a 26 px con 3 lineas; si se mantienen, usar maximo 2 lineas.
- **Consistencia de zona segura:** las cuatro plantillas de reel usan 35% inferior, el manual 25%, el dossier "por validar".
- **Coherencia de datos:** "Vision 2031" en brand book coincide con 02-que-es-atavio-extracto; la vision 2035 de CLAUDE.md esta retirada: bien.

---

## 9. Preguntas para considerar

1. Si se quita el logo y el texto de post-calce y post-oficio, que dice que es una **fabrica** y no una tienda? Hoy nada.
2. Que pasa si la **costura** deja de ser un borde y se vuelve un recorrido que une las laminas de un carrusel y las piezas de una cuadricula (una puntada continua que cruza el feed)?
3. Es un anillo **cerrado** el simbolo de una tienda que *abre* una prenda para mostrar como esta hecha? Que dice un anillo con una abertura (hilo, aguja, ojal)?
4. Que pieza del paquete se vendera mas rapido a Veronica y a un inversor: un tablero de 32 plantillas con marcos vacios, o **tres piezas terminadas con foto real** y el resto como sistema?
5. El mejor elemento del sistema es la copia. Que pasaria si cada pieza tuviera **una sola palabra en 160 px** ("Volteala.") y el resto fuera foto?
6. Es necesario un mapa de color por pilar en lugar de un fondo "por turnos"?

---

## 10. Que haria que un inversor diga "esto parece de agencia" (j)

Un inversor lee "agencia" por: (1) **fotografia real y consistente** en cada pieza (hoy cero); (2) **una idea visual repetida con inventiva** (hoy una linea punteada); (3) **jerarquia clara en una pantalla** (un titular, un dato, una accion); (4) **restriccion** (menos etiquetas, menos cajas); (5) **ejemplos aplicados** (una cuadricula de 9 con fotos, una bolsa, un letrero de local, una factura), no solo plantillas; (6) **detalles de oficio** (remate de costura, etiqueta colgante, muesca de patron) ejecutados con precision. El paquete tiene la disciplina (1 y 2 del manual) y la copia; le faltan fotos, un segundo gesto propio y aplicaciones fisicas.

---

## 11. Cambios de mayor impacto para un rediseno (max. 10)

1. **Reemplazar los marcos "FOTO PENDIENTE" por fotos reales o ilustrativas** en al menos 5 piezas insignia y en el brand book (post-calce, post-oficio, reel-portada-tres-cuerpos, carrusel-durar-02, post-percha). El resto de marcos: icono + 2 palabras sin cuadro de instrucciones, y banda "BORRADOR" en exportacion de revision.
2. **Definir una voz visual ownable:** pespunte como recorrido que envuelve la pieza (una costura, nunca ocho) mas un segundo gesto del oficio (etiqueta colgante / muesca de patron / marca de corte) como forma fija de la foto y el sello de precio.
3. **Reels e historias a sangrado completo:** foto de pantalla completa con bloque solido para texto en el tercio central; eliminar el 31% a 35% de vacio de la portada; unificar zona segura (25% o 35%) en manual, plantillas y brand book.
4. **Eliminar kicker, numeros de seccion, pildoras y tarjetas hero-metric** (brand book secciones 01 a 12, plantillas del feed): jerarquia por escala y color, no por etiqueta.
5. **Reducir y subordinar el logo:** de 194 px a 132 px en laminas interiores de carrusel; conservar la esquina; que el precio y el titular pesen mas que el sello.
6. **Escala movil:** cuerpo minimo 36 px, titular minimo 84 px, 2 lineas maximo de instruccion; probar cada pieza a 390 pt de ancho antes de aprobar.
7. **Reescribir el ritmo de los carruseles** (durar-02 a 05): alternar foto a sangrado, doble pagina, inserto circular de detalle, para que deslizar tenga recompensa; una sola paleta por carrusel.
8. **Mapa de color con funcion fija:** ladrillo = marca, tinta = informacion y precio, hueso = lienzo, molde = ficha de tela y serie Percha, rojo profundo = accion; un fondo fijo por pilar; eliminar el quinto rojo de reel-portada-voltealo.
9. **Brand book para inversor:** una pagina de portada con margen, una seccion de resumen de tres cifras, secciones cortas (la 09 de 8.594 px partida), y 3 aplicaciones terminadas (cuadricula de 9, bolsa o etiqueta, letrero del local) en lugar de 12 secciones iguales. Quitar los botones "Copiar HEX" de la version para inversor.
10. **Aclarar el simbolo del logo:** decidir si el anillo es "abierto" (abertura = firma propia) y fijar el minimo legible de cada version (con bajada >= 200 px, reducida >= 96 px) en vez de 120/72.
