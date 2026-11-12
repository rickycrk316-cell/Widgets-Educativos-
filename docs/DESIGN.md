---
name: Widgets de estudio · v11
description: Sistema visual v11 de los widgets de Quirúrgica 2: estilo app de estudio moderna, fuente del sistema, acento por tema y navegación adaptable.
colors:
  bg: "#FFFFFF"
  bg-2: "#F5F5F7"
  ink: "#1D1D1F"
  ink-2: "#4A4A50"
  ink-3: "#6E6E73"
  line: "#E3E3E8"
  accent-default: "#2F5BD3"
  alarm: "#C0362C"
  caution: "#8A5A00"
  ok: "#2E7D32"
  night-bg: "#000000"
  night-bg-2: "#1C1C1E"
  night-ink: "#F5F5F7"
typography:
  family: "-apple-system, system-ui, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
rounded:
  card: "12px–16px"
---

# Design System: Widgets de estudio · v11

Fuente de verdad: `docs/DECISIONES_v11.md` (§8 diseño, §10 contrato de clases). Este documento resume el sistema; el CSS vive solo en `kit/v11/`.

## Overview

Estilo **app de estudio moderna**: tarjetas con esquinas suaves (12–16 px), mucho aire, tipografía grande y clara, jerarquía por tamaño y peso, sin filetes de periódico. Un sistema, bordes iguales, micro-interacciones discretas; sin fotos ni efectos de sitio web. Funciona sin internet y sin recursos externos.

## Colors

- Fondo blanco o gris muy claro; en modo oscuro automático, negro o gris muy oscuro. Texto casi negro.
- **Un acento por tema**, declarado en el manifiesto (`"tema"`) y aplicado por `construir.py` en `html[data-tema]`: `ginecologia` frambuesa, `salud-mental` índigo, `digestivo` verde azulado, `urologia` ámbar oscuro, `pediatria-ortopedia` azul; cualquier otro, azul.
- Rojo = alarma, ámbar = precaución, verde = correcto. Nunca para decorar. Los roles de la v10 (violeta discrepancia, coral Feynman, rosa remisión) solo se conservan donde el componente ya los usa.

## Typography

Fuente del sistema (San Francisco en Apple): `-apple-system, system-ui, …`. Títulos y cuerpo grandes y claros; la jerarquía la dan tamaño y peso, no el serif ni las versalitas. Cifras tabulares en tablas y pasos.

## Navegación adaptable

Las partes escriben `nav.tabs>button.tb` (`01_nav`); el script genera el resto.
- **iPhone (<760 px):** barra inferior fija (`nav.bottom`) con icono de texto corto + nombre de cada pestaña; desplazamiento horizontal si no caben.
- **iPad y Mac (≥760 px):** menú lateral fijo (`nav.side`) con las pestañas y, bajo la activa, sus `h2` para saltar dentro de la pestaña.
- Filtro de perlas por examen (`.perla-filtro`) accesible desde la barra o el menú: Todos · PUCE · CACES · USMLE 1 · USMLE 2 · MIR · ENARM.
- Sin barra de progreso.

## Animaciones

Transición suave al cambiar de pestaña; tarjetas que se elevan 2 px al pasar el puntero o tocar; aparición escalonada de los pasos al revisar el ejercicio de ordenar. Todo se desactiva con `prefers-reduced-motion`.

## Tablas

Fichas apiladas en iPhone; en iPad y Mac, tablas limpias con cabecera fija dentro del contenedor. Controles táctiles de 44 px.

## Components

Clases que las partes pueden escribir (el resto las genera el script):

| Componente | Clases |
|---|---|
| Núcleo (el 20 %) | `div.nucleo>div.nucleo-t+ul>li` (3–5 `li`, ≤35 palabras) |
| Perla de examen | `aside.perla[data-ex]>div.perla-t+p`; `data-ex` ∈ `puce caces usmle1 usmle2 mir enarm` |
| Visión de conjunto | `table.vis`, `th>span.q+span.qx` (pregunta + qué se busca) |
| Ordenar pasos | `li[data-paso]` en `ol.tl` y `ol.steps.tg`; generadas: `.ord .ord-bank .ord-slots .ord-chip .ord-slot .ord-ok .ord-ko .ord-btns` |
| Diagramas | `figure.dg` (`dg-t`, `dg-row`, `dg-col`, `dg-n.fr|b|p|ac|s|ro`, `dg-ar>span.dg-lab`, `figcaption`); `div.duo` empareja texto y diagrama |
| Vigentes de v10 | `.card`, preguntas guía, `ol.tl` (cascada), signos y «Qué verás», tablas de fármacos con «Mecanismo de acción», Feynman, simuladores de decisión, `.xref`, `span.tg` |

Se quitan «Timeline en blanco», «Tabla en blanco» y las tablas-índice (p. ej. esquema DSM-5-TR).

## Do's and Don'ts

Do: probar cada cambio en iPhone, iPad vertical y Mac, en claro y oscuro; mantener 44 px en controles táctiles; usar el acento solo para interacción y énfasis.
Don't: fuentes web o recursos remotos; `position:fixed` en las partes (solo el kit lo usa para la navegación); sombras decorativas; colores de alarma fuera de su significado.

## Legado v10.2 (Vademécum)

Los widgets anteriores siguen con `kit/kit_head.html`, `kit/def_head.html` y `kit/apertura_head.html`: monografía de vademécum, papel blanco frío, tinta azul única (`#2342A6`), serif en títulos, filetes en vez de sombras, columna de 880 px, radio de 3 px, pestañas como índice de canto. No se tocan; se reconstruyen con `python3 kit/construir.py`.
