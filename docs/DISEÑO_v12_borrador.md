# Diseño v12 «Grecia + cuadernos de Leonardo» (borrador para aprobación)

Solo cambia la estética. Contrato de clases, partes, script y validador son los de v11 (`docs/DECISIONES_v11.md` §10).
Activación: `"tipo": "v12"` en `manifiesto.json`. Cabecera: `kit/v12/head.html` (generada); script y validador: los de `kit/v11/`.

## Idea
- **Cromo** (navegación, cabeceras, tarjetas, tablas, simuladores) = mármol y arquitectura: ángulos rectos (radios 3–6 px), filetes de oro, frontón, greca, acanaladuras.
- **Apuntes** (`.nucleo`, `.perla`, `.fey`, `.ord`) = hoja de cuaderno: pergamino con grano, borde de tinta irregular, línea de construcción (círculo y cuadrado), rótulo manuscrito y leyenda en espejo tenue (`aria-hidden` por `content: … / ""`).
- La legibilidad manda: texto en EB Garamond 17,5–19 px, contraste ≥ 4,5:1 medido en todos los pares de tokens; ornamento siempre a baja opacidad y fuera de la columna de texto (la figura del núcleo reserva 70 px a la derecha en escritorio).

## Tokens (mismos nombres que la dirección de arte)
| Token | Claro | Noche |
|---|---|---|
| `--marmol` / `--marmol-2` / `--veta` | #f7f3ea / #efe8d9 / #d9cfbb | #10171d / #1f2b36 / #2c3945 |
| `--pergamino` / `--pergamino-2` (notas) | #ead8b4 / #dcc594 | #2d261a / #3d3322 (vitela a la luz de lámpara) |
| `--tinta` / `--tinta-2` | #2b2118 / #5a4632 | #efe6d0 / #cfc5ac |
| `--sanguina` (acento, rótulos) | #8f3a1e | #e6916f |
| `--egeo` · `--oro` · `--laurel` | #17697a · #b8862b · #55632f | #52b3c4 · #d6a94a · #a7bb6e |
Extras: `--surface` #fbf9f3 (losa), `--ink-3` #69533d (≥ 5,2:1 sobre pergamino), `--nota-borde`, `--nota-sombra`, `--u-*` (ornamentos SVG como data URI; versión clara y nocturna).
Acento por `tema` (pigmentos): ginecología carmín #8f2a4b, salud mental lapislázuli #3b4a8a, digestivo egeo #146577, urología ocre #7f5410, pediatría/ortopedia azul #1f5d8e; otro = sanguina. Cada uno con variante nocturna.

## Tipografías (incrustadas, WOFF2 latino ≈ 118 KB; respaldo serif del sistema)
- Display: Cinzel 600 (h1, h2, rótulos de tabla, dc-t, numerales). Respaldo Trajan/Copperplate/Palatino.
- Texto: EB Garamond 400 / 600 / cursiva 400. Respaldo Iowan Old Style/Palatino/Georgia.
- Rótulo manuscrito: IM Fell English cursiva (solo títulos de hojas: Núcleo, Perla, Ordena, Feynman). Respaldo cursiva serif.
- Fuentes y subconjunto en `kit/v12/fuentes/`; se regeneran con `python3 kit/v12/generar_head.py`.

## Mapa de roles v11 → v12
| v11 | v12 |
|---|---|
| tarjeta blanca redondeada (`.card .nodo .signo .steps li`) | losa de mármol, radio 4 px, filete veta; `.etapa .dc .stat` con cabecera de oro |
| `h1` | frontón + título Cinzel + greca de oro |
| `h2` | Cinzel con doble filete (oro + veta) |
| `nav.side` | columna: acanaladuras en el canto, frontón arriba, índice en cuadrito, activo con barra de oro |
| `nav.bottom` | estilóbato (peldaños), activo con dintel de oro |
| `.nucleo` | hoja principal: pergamino, círculo y cuadrado vitruvianos, números en círculo de tinta, subrayado de pluma |
| `aside.perla` / `p.perla` | nota al margen: pergamino claro, estrella de ocho puntas, filtros `.ex` como sellos rectos |
| `.fey`, `.ord` | hojas de cuaderno (explicación a mano, hoja de ejercicio) |
| `th>span.q+span.qx` | pregunta en 600; subtexto en cursiva |
| `thead th` | Cinzel pequeño, filete de oro |
| `.dg` | papel de proporciones (cuadrícula fina) |
| `.nodo::before` (punto) | rombo; línea de la cascada en oro |
| `.hb am/ro/ve/vi`, `.b-*`, `.dg-n.*` | mismos roles, colores terrosos AA (ámbar, rojo bol, laurel, lapislázuli, cobre, rosa) |
| `.hb.az` (frase del tema) | arquitrabe de oro sobre mármol |
| sol (esquina del título, ≥ 1000 px) | sol dorado a 50 % |

## Reglas de uso
- Un motivo por zona: cabecera = frontón + greca; lateral = acanaladuras; notas = construcción + espejo. No añadir motivos nuevos dentro de párrafos o tablas.
- Rótulos manuscritos solo en hojas de cuaderno y en una línea; nunca cuerpo de texto en Fell.
- Mayúsculas solo en Cinzel (diseño lapidario); resto en minúscula.
- Movimiento: ≤ 200 ms, `prefers-reduced-motion` respetado, sin partículas.
- Todo offline; sin imágenes remotas ni emojis. El peso del HTML crece ≈ 185 KB por las fuentes.
- Modo noche: pizarra egea con tinta pergamino; las notas pasan a vitela oscura con borde de tinta clara.

## Pendiente de decisión del usuario
1. Aprobar o ajustar el rojo sanguina como acento común frente al color por tema.
2. ¿Corona de laurel para la entidad «principal»? (no implementada: el contrato no la marca de forma única).
3. Migrar definiciones y apertura a v12 requiere cabeceras propias (hoy usan las de `kit/`).
