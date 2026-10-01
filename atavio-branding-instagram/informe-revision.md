# Informe de revisión — Brand book Instagram de Atavío (L1 marca, L2 visual)

Archivo editado: `build/brandbook/src.html` (reensamblado con `assemble.py`). Capturas: `review/l2-*.png`, `review/tog-*.png`, `review/l1-*.json`.

| Vuelta | Hallazgo | Severidad | Regla / criterio | Corrección | Estado |
|---|---|---|---|---|---|
| L1-1 | Rótulo «Garantía» del destacado en el mockup del perfil: contraste 2,36:1 (opacity .42 aplicada a toda la figura) | Mayor | Contraste ≥4,5:1 en ambos temas | La atenuación pasa solo al círculo; el texto queda al 100 % (`.hlrow figure[style*=opacity]`); rótulo de 9,5 a 10 px | Corregido |
| L1-1 | Frase de 24 palabras en copy de marca (sección 3, «También nunca…») | Menor | Frases ≤20 palabras | Dividida en dos frases | Corregido |
| L1-1 | Frase de 22 palabras (sección 11, «Lo que nunca se mueve…») | Menor | Frases ≤20 palabras | Dividida en tres frases | Corregido |
| L1-1 | Tabla de contraste (sección 4): muestras «Aa» en #8A8178, #C8A97E y #A31A0E sobre fondos incorrectos, de 15 px | Info | Reglas de color | Son ejemplos de uso prohibido, marcados «No» en la tabla; válido por diseño | No aplica |
| L1-1 | Tablas «No y sí» citan «Dura 10 años», «100% nacional», voseo, «¡ÚLTIMAS UNIDADES!», «premium», «consulta precio por DM», «Un nuevo concepto en moda» | Info | Regex de palabras vetadas | Citas deliberadas en columna «No»; el resto del texto, 0 coincidencias | No aplica |
| L1-1 | Regex automáticas: clientes de la fábrica, Guayaquil, voseo fuera de tabla, exclamaciones, mayúsculas gritadas, emojis (solo 📍 en la bio) | — | R001–R120 (subconjunto automático) | 0 incidencias; «garantía» solo en contextos «pendiente / cuando esté impresa» | OK |
| L1-1 | Cifras contra docs: cuenta (~2.400, 733, 59, 85 %, 22/24, 68 %, 43 %, 41 %), pilares 35/25/25/15, HEX/RGB/CMYK, ratios 12,14 / 9,47 / 6,64 / 6,36 / 3,28 / 1,91 / 1,83, logo 120/72 px y 25/15 mm, bio 147 caracteres, 34 caracteres del nombre, ejemplos de 45 y 86 caracteres | — | Fidelidad de cifras | Coinciden con los docs o se recalcularon bien | OK |
| L1-1 | Contraste, ningún texto en #A31A0E <24 px ni en #C8A97E fuera de las muestras; texto SVG (2X, %) es #2B2B2B sobre hueso en ambos temas | — | Contraste 4,5:1 / 3:1 | Sin cambios | OK |
| L1-1 | Zona segura de reels 15/35/6 % frente a «25 % inferior» del manual (reels) | Info | R: 9:16 sin texto en 15 % sup. / 25 % inf. | Ya está marcada «Por validar» y en Pendientes; es decisión de marca, no se toca | Abierto (decisión de Verónica) |
| L2-1 | Móvil: tablas de ≥3 columnas con `min-width` 560-680 px se cortaban sin pista de scroll; en «No y sí» desaparecía la columna «Sí» | Mayor | Texto cortado / responsive | A ≤640 px las tablas pasan a tarjetas con etiquetas (`data-th` por JS); la columna «No» conserva su etiqueta | Corregido |
| L2-1 | Móvil: barra de horas con «PLANIFI/CAR», «RESP.» vertical y «0,5» cortado | Mayor | Texto cortado | A ≤640 px se ocultan los rótulos (la tabla de abajo los explica); cifras compactas; «0,5» pasa a «0,5 h» | Corregido |
| L2-1 | Móvil: portadas de reel, texto en reel, historias y destacados en 1 columna de 358 px (imágenes 9:16 de ~640 px de alto) | Mayor | Ritmo / espaciado | Rejilla de 2 columnas en móvil | Corregido |
| L2-1 | Móvil: marcos «foto pendiente» de 240 px alineados a la izquierda, con hueco de 118 px | Menor | Alineación | Rejilla 2×2 a ancho completo | Corregido |
| L2-1 | Miniaturas con fondo hueso (catálogo, portadas claras, vista cuadrícula) se funden con la página | Mayor | Jerarquía / bordes | Contorno de 1 px (`--line`) en `.shot-img` | Corregido |
| L2-1 | Escritorio: 6 portadas de destacados rompen en 5 + 1 huérfana | Menor | Alineación | Clase `six`: 6 columnas (3 en tablet y 2 en móvil) | Corregido |
| L2-1 | Etiqueta `.tag` con interlínea 1 y dos líneas apretadas en móvil (portada) | Menor | Espaciado | `line-height:1.35` | Corregido |
| L2-1 | Rótulos `dt` «Lo que nunca se mueve» con 2 líneas apretadas | Menor | Espaciado | `line-height:1.3` | Corregido |
| L2-1 | Barra de horas: último segmento «0,5» sin unidad (inconsistente) | Menor | Consistencia | «0,5 h» | Corregido |
| L2-1 | Regresión propia: `thead` oculto con `clip` generaba scroll horizontal (696 px) y la tabla de pendientes tenía `min-width` en línea | Mayor | scrollWidth ≤ ancho | `thead{display:none}` y `min-width:0!important` | Corregido |
| L2-1 | Conmutadores «Ver zonas seguras / Ver en cuadrícula» | — | Funcionalidad | Probado con click a 1440 y 390 px: cambia `aria-pressed` y `src` (9 variantes de zonas, 5 de cuadrícula), vuelve a «normal», 0 errores | OK |
| L2-1 | Navegación móvil: barra sticky horizontal con ítems de 44 px y ítem activo centrado | — | Móvil | Sin cambios | OK |
| L2-1 | Capturas a 1440 y 390 px, claro y oscuro: `scrollWidth` 1440 y 390, 0 errores de consola, 0 solapamientos | — | Verificación final | — | OK |
| L2-2 | Dos vueltas L2 hechas; no queda nada nuevo | — | — | — | Cerrado |

Contrato Artifact: sin doctype, html, head, body ni iframes; `<title>` al inicio; tokens en `:root` con bloques oscuros; sin descargas ni print. Los dos scripts son inline.

Nota: las capturas usan fuentes locales inyectadas solo en la captura. En algunas de móvil (`l2c-*`, `sheet-*`) Fraunces cae a serif por defecto: es un artefacto de la captura, no del archivo.
