# Plan del orquestador · Biblioteca de elementos de Atavío para Canva (v1.2)

Objetivo: que Ricardo tenga en Canva, listos para arrastrar a un post, todos los elementos visuales del sistema v1.2: logo (sello), motivos del «patrón de molde», iconos, texturas y piezas de apoyo. Fuente de verdad: `v1.2/DECISIONES-V12.md`, `v1.2/CLAUDE.md`, `v1.2/motifs/README.md`, `v1.2/logo/specs.md`.

Rutas: `V=/home/user/Widgets-Educativos-/atavio-branding-instagram/v1.2` · `S=/tmp/claude-0/-home-user-Widgets-Educativos-/a4f9a5b0-9019-55e2-9489-b316b7cde1bb/scratchpad/atavio/elementos` (trabajo) · salida final en `$V/elementos-canva/`.

## Fase 1 · Inventario y curaduría (ejecutor)
Revisar `$V/motifs/`, `$V/motifs/iconos/`, `$V/logo/`, `$V/plantillas-html/feed-assets/` y las 32 plantillas (`$V/plantillas-html/*.html`) para listar TODOS los elementos visuales que aparecen en los posts, incluidos los que hoy solo existen dentro de una plantilla (chip de dato / subtítulo, disco hueso con costura detrás del sello, bloque sólido de titular, numerales grandes, marcador de cinta, etc.).
Curar: quitar duplicados, variantes con logo descartado (`logo-reducida-hueso`, `logo-simbolo-hueso`), el destacado/icono de garantía (pendiente: va aparte en `_pendiente/`), y nada con el anillo viejo.
Entregable: `$S/inventario.json` con, por elemento: id canónico, nombre para Canva (español, buscable), categoría, archivo fuente, variantes (claro = para fondo claro, oscuro = para fondo oscuro), uso y regla en una línea.

## Fase 2 · Producción de archivos (ejecutor)
Categorías y nombres: `01-logo`, `02-costura`, `03-moldes`, `04-etiqueta-y-cinta`, `05-detalles-de-oficio`, `06-texturas`, `07-iconos-destacados`, `08-apoyos` (marquilla, cruz de registro, disco del sello, chip de dato).
Por elemento y variante:
- **PNG transparente** (lado mayor 2400 px; costuras largas: alto mínimo legible, trazo nítido) renderizado con Chromium (`$S/render.js` ya existe: `node render.js jobs.json`, jobs = [{src,out,long}]).
- **SVG «apto Canva»**: sin `<pattern>`, `<mask>`, `<clipPath>`, `<filter>`, `<use>`, `<text>`; las líneas punteadas (`stroke-dasharray`) convertidas en segmentos/rellenos reales (cada puntada como path) para que Canva no las pinte continuas; colores solo de la paleta. Si un elemento no se puede simplificar sin perder fidelidad (tramas de sarga, detalles con recorte), entrega SOLO el PNG y anótalo.
- Nombre de archivo = nombre buscable en Canva, p. ej. `atavio-costura-horizontal-ladrillo.png`, `atavio-molde-delantero-claro.svg`.
Verificación: renderizar cada SVG apto Canva y compararlo con el original (diferencia visual mínima); hoja de contacto por categoría sobre hueso y sobre tinta; mirarlas.
Entregables: `$V/elementos-canva/<categoria>/…`, `$V/elementos-canva/catalogo.pdf` (catálogo A4: miniatura, nombre, uso, regla, fondo correcto), `$V/elementos-canva/LEEME.md`, y `$V/atavio-elementos-canva-v1.2.zip`.

## Fase 3 · Canva (ejecutor, solo si las herramientas mcp__Canva__* están disponibles)
1. Carpeta «Atavío · Elementos v1.2» (create-folder en raíz).
2. Subir los PNG (create-upload-url + `curl -X POST --data-binary`), tandas ≤ 8 URLs; mapa nombre→mediaId en `$S/canva-media.json`. Mover cada imagen a la carpeta (move-item-to-folder).
3. Diseño «Atavío · Biblioteca de elementos v1.2»: una página por categoría (1080×1350, fondo hueso; la de elementos claros sobre tinta), cada elemento insertado con insert_fill, ordenado en rejilla con su nombre como texto debajo. Sirve para copiar y pegar en cualquier post.
4. Verificar con read-design (design_content: cada página referencia los mediaId) y con miniaturas de get-assets; commit; mover a la carpeta.
Límites conocidos: el conector NO puede modificar el Brand Kit (colores, fuentes, logos) ni borrar páginas. Esa parte la hace Ricardo con los archivos (instrucciones en LEEME.md).

## Reglas para el ejecutor
- Si algo no está claro, choca con el manual o una herramienta falla dos veces, DETENTE y devuelve tu informe empezando por `PREGUNTA PARA EL ORQUESTADOR:` con el contexto y 2–3 opciones. El orquestador responde y te reanuda.
- No inventes elementos nuevos ni cambies colores, formas o el logo. Solo exportas, simplificas para compatibilidad y organizas.
- Nada con «—», nada del logo descartado, nada de garantía como publicable.
