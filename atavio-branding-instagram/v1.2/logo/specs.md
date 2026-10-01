# Sello ATAVÍO — especificaciones

Reconstrucción vectorial del logo del perfil de Instagram. Origen: captura 780×793 (círculo medido por ajuste: centro 390,7/394,7 px, radio 387,3 px). Todas las medidas en unidades del viewBox 1000×1000 (círculo = 1000 de diámetro, r = 500).

## Medidas (sello principal)
| Elemento | Valor |
|---|---|
| Círculo | diámetro 1000 (llena el viewBox) |
| Ancho del nombre «Atavío» | 714 (71,4 % del diámetro) |
| Altura de la A (mayúscula) | 208 · altura de la «t» 192 · altura de x 150 |
| Grosor de trazo del nombre | 10,5 (monolínea; la i tiene 8,3) |
| Base del nombre | y = 560 (la tilde sube hasta y = 352) |
| Bajada: altura de mayúscula | 35,1 · base y = 636 · centrada (x ≈ 501) |
| Separación base nombre → altura de mayúscula bajada | 41 |
| Bajada original (solo prueba) | ancho 706; la nueva «LA TIENDA DE LA FÁBRICA» mantiene tamaño, tracking (-0,017 em) y base |
| Reducido | mismo nombre, desplazado +29 hacia abajo hasta el centro óptico (media de los centros de la caja de mayúscula y de la caja de x) |

**X = altura de mayúscula de la bajada = 35,1.** Se descarta la «t» (192) porque 2X = 384 daría un margen del 38 % del diámetro, desproporcionado. **Área de seguridad: 2X = 70 unidades (7 % del diámetro) alrededor del círculo.**

## Tamaños mínimos
- Sello principal: la bajada alcanza 6 px de mayúscula con diámetro 6/0,0351 = **172 px** en pantalla; impresión: **45 mm** (mayúscula 1,6 mm).
- Reducido: **48 px** en pantalla / **12 mm** en impresión. A 48 px el trazo mide 0,5 px (se lee, pero tenue); desde 64 px es cómodo. Bajo ese tamaño usar solo el círculo o el avatar.
- Wordmark solo: ancho mínimo 90 px / 25 mm.
- Avatar de Instagram: probado a 110 px y 48 px (ver contact-sheet.png).

## Colores y contraste (WCAG)
| Par | Ratio | Nota |
|---|---|---|
| Blanco #FFFFFF sobre #DA3732 | 4,59:1 | letras del sello |
| #DA3732 sobre hueso #F3EDE1 | 3,94:1 | ≥ 3:1, por tanto la invertida usa letras #DA3732 (no hace falta ladrillo) |
| #DA3732 sobre tinta #2B2B2B | 3,08:1 | el borde se distingue (≥ 3:1) |
| #DA3732 sobre molde #C8A97E | 2,06:1 | < 3:1: el borde se distingue sobre todo por el tono; usar con área de seguridad completa y no en tamaños pequeños. Alternativa: sello una-tinta |
| #DA3732 sobre ladrillo #A31A0E | 1,69:1 | no usar: por eso existe la invertida |
| Hueso #F3EDE1 sobre ladrillo #A31A0E | 6,64:1 | círculo de la invertida |
| Hueso sobre tinta / tinta sobre hueso | 12,14:1 | versiones una tinta |

Colores: rojo del sello #DA3732 (exclusivo del logo), blanco #FFFFFF (excepción documentada a «hueso en vez de blanco»: el sello se reproduce tal cual), hueso #F3EDE1, tinta #2B2B2B, ladrillo #A31A0E, molde #C8A97E. La invertida (círculo hueso) se ve sin borde sobre fondo hueso: solo para fondos rojos u oscuros.

## Tipografías
- **Nombre «Atavío»**: ninguna fuente libre alcanza IoU 0,85 (mejores: Didact Gothic 0,40; Raleway ExtraLight 0,38; Quicksand Light 0,37). Se redibujó como geometría monolínea ajustada a la captura (IoU suave 0,885 frente a la captura): A con vértice plano, t sin gancho, «a» de un piso, v, í, o con elipses de exponente 2,16. No es una fuente; es dibujo propio, sin licencia de terceros.
- **Bajada**: Open Sans variable (wght 500, wdth 95), **SIL OFL 1.1**. IoU suave 0,757 (alternativas: Noto Sans 0,736, Cabin 600 ≈ 0,68, Hind SemiBold ≈ 0,66). El original parece Myriad (propietaria); Open Sans es la mejor equivalente libre. Texto convertido a trazados (sin `<text>`).

## Usos incorrectos
No cambiar el rojo, ni usarlo en otros elementos; no poner el sello rojo sobre ladrillo; no estirar ni condensar; no añadir sombras, contornos ni degradados; no devolver la bajada «UN NUEVO CONCEPTO EN MODA»; no rotar; no usar el reducido por debajo de 48 px ni el principal por debajo de 172 px; no invadir el área de seguridad; no recrear con una fuente.

## Archivos
Los SVG usan subtrazos superpuestos con relleno nonzero (unir con Pathfinder si se envía a bordado o grabado). PNG de 1024 px con fondo transparente en png/. `_prueba-identidad.svg` y `comparacion.png` son solo verificación.
