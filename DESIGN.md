---
name: Widgets de estudio · Vademécum
description: Kit visual de los widgets v10 de Quirúrgica 2, compuesto como una monografía de vademécum con índice de canto.
colors:
  paper: "#FBFBFC"
  paper-2: "#F1F2F5"
  ink: "#16181D"
  ink-2: "#3A3D46"
  ink-3: "#686C78"
  rule: "#D7D9E0"
  accent: "#2342A6"
  accent-ink: "#1B358A"
  accent-field: "#EAEEFA"
  amber: "#7A4A06"
  amber-field: "#FBF1DF"
  alarm: "#9E1F1F"
  alarm-field: "#FBE9E7"
  green: "#2F5E12"
  green-field: "#EBF3E1"
  violet: "#4C3FA8"
  violet-field: "#EEECFB"
  coral: "#8E3517"
  coral-field: "#FAEDE6"
  rose: "#8A2C52"
  rose-field: "#FAEAF1"
  night-paper: "#121317"
  night-paper-2: "#1C1E24"
  night-ink: "#E7E8EC"
  night-accent: "#8EA4FF"
typography:
  title:
    fontFamily: "ui-serif, New York, Iowan Old Style, Charter, Georgia, serif"
    fontSize: "26px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.012em"
  section:
    fontFamily: "ui-serif, New York, Iowan Old Style, Charter, Georgia, serif"
    fontSize: "19px"
    fontWeight: 600
    lineHeight: 1.3
  box-title:
    fontFamily: "ui-serif, New York, Iowan Old Style, Charter, Georgia, serif"
    fontSize: "16px"
    fontWeight: 600
    lineHeight: 1.35
  body:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "13.5px"
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: "0.04em"
  tag:
    fontFamily: "ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "11px"
    fontWeight: 700
    lineHeight: 1.4
rounded:
  sm: "2px"
  md: "3px"
spacing:
  gutter: "16px"
  box: "12px 14px"
  section-top: "40px"
components:
  tab:
    backgroundColor: "{colors.paper-2}"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.md}"
    padding: "9px 15px 8px"
    height: "44px"
  tab-active:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.paper}"
  button-go:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.paper}"
    rounded: "{rounded.md}"
    padding: "8px 16px"
    height: "44px"
  chip:
    backgroundColor: "{colors.paper-2}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    height: "44px"
  chip-on:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.paper}"
  box-guide:
    backgroundColor: "{colors.accent-field}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.box}"
---

# Design System: Widgets de estudio · Vademécum

## Overview

Cada widget se lee como una monografía de vademécum: papel blanco frío, tinta negra azulada y una sola tinta de imprenta azul para guía y navegación. La jerarquía la llevan filetes, serif en los títulos y versalitas en las etiquetas, no tarjetas con sombra. La barra de pestañas es un índice de canto: pestañas planas y la activa en tinta azul, unida al papel por el filete grueso inferior. De noche el papel pasa a grafito y la tinta se aclara; ningún componente cambia de forma.

El kit es offline por contrato: solo fuentes del sistema (New York en iPad), sin recursos remotos. Las clases y el JS son los de la skill `widget-ensenanza` v10; este sistema vive solo en `fuentes/kit_v10_vademecum/kit_head.html`.

## Colors

### Primary
- **Tinta azul vademécum** (`accent` #2342A6, noche #8EA4FF): pestaña activa, botones «Ir a», chips activos, línea de la cascada, contrafactual. Su campo (`accent-field`) solo rellena «Preguntas guía», la presentación clave de «Qué verás» y los enlaces.

### Neutral
- **Papel** (`paper`, `paper-2`) y **tinta** (`ink`, `ink-2`, `ink-3`), todos con sesgo azul. Filete fino `rule`; filete grueso = `ink`.

### Roles clínicos (tintas planas, no acentos)
Ámbar = precisión/alcance; rojo = alarma; verde = perla/confirmación; violeta = discrepancia y línea de guía rectora (exigencia de la skill); coral = Feynman; rosa = remisión. Cada rol tiene tinta y campo, en claro y oscuro, siempre con filete completo de 1 px.

### Named Rules
- **Una tinta de imprenta.** El azul es el único color de interacción; los roles clínicos nunca se usan para decorar.
- **Campo con filete.** Todo campo de color lleva su filete completo del mismo rol; nunca un borde lateral grueso.

## Typography

Serif del sistema para títulos (h1 26–28 px sobre filete de 2 px; h2 19 px con filete superior; títulos de recuadro y de simulador 16 px), sans del sistema para el cuerpo (15–15,5 px / 1,65), versalitas a 13,5 px para cabeceras de tabla, etiquetas de signo y de simulador, y monoespaciada solo en las etiquetas cerradas de pasos (`span.tg`). Cifras tabulares en tablas, pasos y estadísticas. Feynman en serif 16 px para que se lea como prosa.

### Named Rules
- **Sin mayúsculas sostenidas.** Los títulos van en tipo oración; las versalitas solo en etiquetas cortas.

## Layout

Columna única de 880 px máximo con gutter de 16 px (24 px desde 700 px). Secciones separadas por filete y 40 px arriba / 14 px abajo. El Panorama es un índice numerado (01, 02…) por contador CSS. Las tablas desbordan dentro de su contenedor; la tabla comparativa fija su primera columna.

## Elevation & Depth

Plana. No hay sombras de elevación; la profundidad la dan el filete y el campo. Única excepción funcional: el anillo de papel alrededor del nodo cuadrado de la cascada.

## Shapes

Radio de 3 px en recuadros y botones, 2 px en insignias y etiquetas. Nodos de la cascada cuadrados (1 px).

## Components

### Navigation
Índice de canto: pestañas de 44 px, planas, con borde superior y laterales; la activa en azul sólido. Degradado de 56 px hacia el papel en los bordes cuando hay más pestañas; desplazamiento con imantado y margen de 56 px.

### Buttons
«Ir a» azul sólido; enlaces cruzados (`.xref`) con campo azul y filete, partibles en línea.

### Cards / Containers
`.card` en `paper-2` con filete fino. «Preguntas guía» con campo azul; «Frente a» y «El grupo en una frase» solo con filetes azules arriba y abajo. Nada de recuadros anidados.

### Signature Component: la cascada
`ol.tl` con línea azul de 2 px y nodos cuadrados; cada nodo es una ficha `paper-2`. En modo reconstrucción solo se ve el número y «?».

## Do's and Don'ts

### Do:
- Usar el filete para separar y el campo solo cuando el recuadro es un rol.
- Mantener 44 px en todo control táctil.
- Probar cada cambio en iPad vertical, móvil y modo oscuro.

### Don't:
- Añadir sombras, degradados decorativos o tarjetas apiladas.
- Introducir fuentes web o recursos remotos.
- Usar el color de un rol clínico fuera de su significado.
