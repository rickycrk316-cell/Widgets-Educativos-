# Propuesta B — especificaciones del logo

Fuente: Manual v1.1, cap. 04. Texto convertido a trazados (sin `<text>`). Construido con `build/build.py`.

## Unidad X
- Diámetro exterior del anillo = 1000 unidades. **X = 60** (6 % del diámetro) = grosor del trazo. Radio de la línea central = 470.
- **Área de seguridad = 2X = 120 unidades** por los cuatro lados. Todos los SVG (salvo el avatar) usan `viewBox="-120 -120 1240 1240"`: el viewBox ya incluye la zona libre; el anillo ocupa 0–1000.
- Nada (texto, foto, borde, otro logo) entra en esa zona.

## Tipografía y color
- Nombre: Fraunces SemiBold (wght 600, opsz 144, SOFT 50, WONK 0), ancho 610 u. (principal) / 660 u. (reducida), con kerning de la fuente.
- Bajada «LA TIENDA DE LA FÁBRICA»: Libre Franklin SemiBold, mayúsculas, tracking ≈ 0,24 em, ancho 540 u.
- Pespunte corto (guion 3 / espacio 2, 6 u. de trazo) entre nombre y bajada, solo en principal y una tinta. Anillo interior de pespunte descartado en el logo (ensucia a 72–120 px); solo se usa como marco exterior en el avatar.
- Anillo `#A31A0E`. Nombre: claro `#2B2B2B` (12,14:1; regla del manual: texto en gris tinta, no en rojo); oscuro `#F3EDE1`. Una tinta: todo `#2B2B2B` o todo `#F3EDE1`.

## Tamaños mínimos
| Soporte | Versión | Mínimo |
|---|---|---|
| Pantalla | Principal | 120 px de ancho (incluye el área 2X) |
| Pantalla | Reducida | 72 px de ancho |
| Impresión | Principal | 25 mm |
| Impresión | Reducida | 15 mm |

A 120 px la bajada mide ≈ 4 px de alto de mayúscula: es el límite; por debajo usar reducida o símbolo.

## Archivos
atavio-principal-claro/oscuro, atavio-reducida-claro/oscuro, atavio-simbolo (solo anillo), atavio-una-tinta-tinta/hueso (versión principal en un color), avatar-instagram (1080×1080, fondo hueso, anillo + nombre, marco de pespunte rojo ladrillo a r=487, anillo X=64; legible a 110 px en recorte circular). PNG de 1024 px de ancho junto a cada SVG. Fondo transparente salvo el avatar.
