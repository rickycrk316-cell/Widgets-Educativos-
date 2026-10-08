# Patología urinaria baja — plan del orquestador

Fuentes (prioridad en este orden):
1. **Caso de Carlos** (adjunto del estudiante): `fuentes/casos/caso_carlos_patologia_urinaria_baja.md` (transcripción fiel de `caso_carlos_p1.jpg` y `caso_carlos_p2.jpg`).
2. **Sílabo**, caso «PATOLOGÍA URINARIA BAJA»: `fuentes/Syllabus_primera_rotacion_10mo.md`, con su bibliografía complementaria (DynaMed 2024 de HPB, prostatitis aguda/crónica, cáncer de próstata; Epstein 2016 ISUP/Gleason; Bradley 2017 dieta y STUI; Harrison «síndrome de dolor vesical»).
3. Guía internacional vigente más específica (p. ej. EAU 2024–2025 STUI masculinos no neurogénicos, AUA 2023 HPB, EAU/AUA cáncer de próstata, EAU infecciones urológicas, CDC 2021 ITS para uretritis).

Decisiones confirmadas por el estudiante: amenaza = cáncer de próstata; el caso es el **ancla** (fuente prioritaria) de los dos widgets, que siguen siendo de estudio general; diseño **Vademécum** en ambos.

## Pistas del caso que los widgets deben usar (sin resolver el caso por el estudiante)

| Pista | Por qué importa | Dónde usarla |
|---|---|---|
| Varón de 64 años, STUI desde los 58: polaquiuria 10/día, nicturia 5/noche, vaciado incompleto, goteo posmiccional, «moja los zapatos» | Patrón de llenado + vaciado + posmiccional de crecimiento prostático | `vis` (presentación común), e1 |
| Tacto rectal: próstata aumentada, **blanda, contornos regulares** | Separa HPB de cáncer (duro, nodular) y de prostatitis aguda (dolorosa, caliente) | `vis` («Signo que la delata», «Negativo pertinente»), e1, e3 |
| Hermano con cáncer de próstata | Antecedente familiar de primer grado: cambia la decisión compartida sobre PSA | e3 (amenaza) y simulador |
| Niega disuria, fiebre y mal olor | Negativos pertinentes frente a cistitis, prostatitis aguda y uretritis | `vis`, e2, e4, e5 |
| **Clortalidona** 25 mg QD | Diurético: poliuria; si se toma tarde, nicturia; la nicturia puede ser poliuria nocturna y no solo próstata | e1 (Diagnóstico: diario miccional; Tratamiento: horario del diurético) |
| **Sertal compuesto** ocasional (propinox, antiespasmódico antimuscarínico, + clonixinato de lisina) | Los antimuscarínicos pueden precipitar retención urinaria en el crecimiento prostático | e1 (`Evita`), hb ro de `vis` si corresponde |
| Dolor a la palpación del **escroto izquierdo** | Hallazgo que no explica la HPB: epididimitis u orquiepididimitis (prostatitis, uretritis), varicocele, hernia | e2/e5 («Qué verás» o seguimiento) y `vis` como hallazgo a explicar |
| **StO₂ 89 %** en Quito (~2 850 m) y tabaquismo ≈29 paquetes-año (1 cajetilla/día de los 15 a los 44) | Por debajo de lo esperado aun en altura: repetir y estudiar; el tabaco es además factor de riesgo de cáncer vesical (hematuria) | Nota de altitud solo si cambia una conducta; `vis` como hallazgo fuera del eje |
| Colon irritable, colecistectomía, herpes zóster | Contexto; no explican los STUI | Solo si aportan (no forzar) |

## Widget A · Patología urinaria baja (widget-ensenanza v10, multi) — `ensenanza/`

- Presentación común: **síntomas del tracto urinario inferior (STUI) en el varón adulto**.
- `Modo: multi · Entidades: e1=Hiperplasia prostática benigna (principal), e2=Prostatitis, e3=Cáncer de próstata, e4=Cistitis, e5=Uretritis · Amenaza: e3 · Override: sí`
- Eje declarado: glándula prostática (proliferativa benigna → inflamatoria → neoplásica… ordenado como e2 inflamatoria, e3 neoplásica) y luego vía urinaria baja de proximal a distal (vejiga → uretra).
- Subtipos: prostatitis bacteriana aguda, bacteriana crónica y síndrome de dolor pélvico crónico (en e2); cistitis no complicada vs complicada (en el varón siempre complicada) y síndrome de dolor vesical (en e4); uretritis gonocócica vs no gonocócica (en e5); Gleason/ISUP (en e3).
- «No confundir con…» (vecinas fuera del grupo, sílabo): **tuberculosis renal y vesical** y **trauma/estenosis uretral**; también vejiga hiperactiva y poliuria nocturna.
- Simuladores esperados: e1 dx = **I-PSS** (escala → banda → conducta, permitido por §7.10) + tamaño/síntomas → tratamiento; e3 = decisión compartida de PSA según edad y antecedente familiar (sin probabilidades: §7.10); `vis` = diferencial desde los hallazgos de Carlos.
- Título: `Patología urinaria baja` · Slug: `Patologia_urinaria_baja_widget_v10.html`.
- Kit: Vademécum (`kit/kit_head.html`). No lo leas ni lo edites.

## Widget B · Definiciones (skill definiciones v5.1) — `definiciones/`

- Caso/semana: Patología urinaria baja (primera sesión, precaso de Carlos).
- Términos, en este orden de pestañas (9 → régimen normal, tope 5 prerrequisitos):
  1. Patología urinaria baja
  2. Frecuencia miccional
  3. Insomnio (de inicio y de mantenimiento) — una pestaña con ambos tipos
  4. Tenesmo vesical
  5. Incontinencia urinaria
  6. Clortalidona — el estudiante escribió «Clortaridona»: aplica la regla de término mal escrito (`.mini` ámbar con la interpretación)
  7. Sertal — en el caso es «Sertal compuesto»: define el producto y sus componentes (propinox y clonixinato de lisina), qué son, no cómo se usan; `.mini` ámbar con la interpretación
  8. Colon irritable
  9. Próstata aumentada de tamaño
  + pestaña final **Repaso global**.
- Alcance: paso 1 del ABP (qué es, qué lo distingue, cómo se reconoce). Clortalidona y Sertal: qué son y su mecanismo; su manejo va al paso 7 (decláralo en `.mini`). Los ejemplos de anclaje pueden usar a Carlos.
- Diseño: usa **exactamente** `kit/def_head.html` como cabecera (sustituye `@@TITULO@@` por `Definiciones · Patología urinaria baja`) y **solo sus clases**. Escribe las partes del cuerpo y el motor JS al final; nada de `<style>` propio ni `style=`.
  - Vocabulario: `nav.tabs>button.tb` (activa `.active`) · `section.tab` (activa `.active`) · `.hb>.hb-t` (idea rectora) · `.pre>.pre-t` + `.acc.op` (prerrequisitos, abiertos) · `.rem-line` con `.chip-rs` (remisiones) · `.card` (`.card-t`), `.card.fey` (Feynman), `.card.ej` (ejemplo de anclaje) · `.badge.b-pu|b-am|b-ro|b-ve|b-az|b-co|b-rs` · `.acc` (`.acc-h` + `.chev` + `.acc-b`; `.acc.no` para «No confundir con…») · `.tw>table` con `thead`/`tbody` · `ol.tl>li` (mini-timeline) · `.rc` (`.rc-t`, `.rc-count`, `.rc-card`, `.rc-q`, `.rc-a`, `.rc-hint`, `.rc-btns`, `button.go`, `button.gr.ok|mid|ko`, `button.ghost`, `.rc-end.ok|rep`) · `.mini`, `.mini.am` · `.gloss` · `ol.vanc`.
  - Glifos: los botones de calificación dicen «La sabía / A medias / No la sabía» con su color (`.gr.ok/.mid/.ko`) y el badge dice «Fuente por verificar» (`.b-am`), **sin** ✅ ⚠️ ❌: la regla de diseño 8 prevalece sobre esos glifos (decisión del orquestador; decláralo en el manifiesto).
- Archivo: `Definiciones_patologia_urinaria_baja.html`.

## Reglas de diseño para ejecutores (ambos widgets)

1. Solo clases del kit/cabecera. Nada de `style=`, `<style>` propio, clases inventadas ni recursos remotos.
2. Toda tabla con `<thead>` (fila de cabecera en `<th>`) y `<tbody>`, dentro de `div.tw`.
3. Nada de recuadros anidados (`.card` dentro de `.card`/`.hb`/`.fey`/`.pre`; `.hb` dentro de `.hb`). En definiciones, los acordeones de prerrequisito sí van dentro de `.pre`.
4. Títulos en tipo oración, nunca en MAYÚSCULAS ni Título De Cada Palabra; `hb-t` no literales ≤8 palabras.
5. Párrafos de ≤90 palabras (salvo `p.res` y Feynman, con sus conteos de skill); enumeraciones de más de 3 elementos → lista o tabla.
6. Como máximo un `<b>` por párrafo; sin negrita en celdas de cuerpo salvo la primera columna.
7. Voz activa, español de Ecuador, sin exclamaciones ni muletillas («cabe destacar», «es importante mencionar», «sin lugar a dudas», «vale la pena»).
8. Sin emojis ni pictogramas Unicode (solo ↪ ↓ ← → ▾ y símbolos de unidades).
9. Coma decimal y espacio fino de miles; cifras con unidad y `[n]`.
10. Respeta los conteos de palabras de cada skill; no alargues para llenar.

## Pruebas finales del orquestador

- Enseñanza: `validar.py` + `kit/auditar_diseno.py` (router, kit intacto, reglas 1–9) + `probar_navegador.js` + detector impeccable + revisión de diseño independiente.
- Definiciones: validación propia de la skill (el ejecutor) + `auditar_definiciones.py` (contrato de la skill, cabecera intacta, reglas 1–9) + `probar_definiciones.js` (pestañas, desborde, motor de recall por pestaña y repaso global) + detector impeccable.
