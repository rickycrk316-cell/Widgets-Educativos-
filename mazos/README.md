# Mazos Anki (flashcards v7)

Un mazo por caso en `mazos/<tema>/`: `tarjetas.json` (fuente única), `media/` (SVG/PNG del campo Esquema), `Quirurgica2_<TagRaíz>.apkg` y `Guia_<TagRaíz>.docx`. Se generan con `kit/anki/` (ver `.claude/skills/flashcards/SKILL.md`):

```
python3 kit/anki/compilar_mazo.py mazos/<tema>/tarjetas.json     # lint + .apkg + actualiza este registro
python3 kit/anki/guia_docx.py mazos/<tema>/tarjetas.json
node kit/anki/previsualizar.js mazos/<tema>/tarjetas.json <scratchpad>/capturas
```

## Modelos de nota (IDs fijos: nunca cambiarlos ni editar sus campos)

| Modelo | ID | Campos |
|---|---|---|
| Q2 v7 QA | 1762900700101 | Pregunta, Respuesta, Razonamiento, Mnemotecnia, Esquema, Fuente |
| Q2 v7 Cloze | 1762900700102 | Text, Extra, Mnemotecnia, Esquema, Fuente |

Los modelos v6 (`Quirurgica2 QA` 1738492001202, `Quirurgica2 Cloze` 1738492001201, mazo `Quirúrgica2` 1738492001100) quedan como históricos: no se reutilizan. Un campo nuevo exige un modelo nuevo con ID nuevo, registrado aquí.

## Registro de prefijos y mazos

El compilador lee y actualiza esta tabla (no cambies su formato). Cada caso es el submazo `Quirúrgica2::<Caso>` con su ID fijo. `Último ID` es el mayor ID de nota publicado: los nuevos continúan desde ahí, y un ID publicado nunca se reasigna a otro contenido (se sobrescribiría la tarjeta en Anki). Un tema fuera de los sílabos (`Q2X-<ABREV>`) se añade como fila nueva con el siguiente ID de mazo libre antes de compilar.

<!-- retirados: Q2-TOX -->
Prefijos retirados: `Q2-TOX` (mazo antiguo de toxicodependencias; el caso usa `Q2R2-TOX` desde 0001).

<!-- registro:inicio -->
| Prefijo | Carpeta | Tag raíz | ID de mazo | Último ID | Notas | Versión | Fecha |
|---|---|---|---|---|---|---|---|
| Q2-OJO | ojo_rojo | OjoRojo | 1762900710001 | Q2-OJO-0045 | 45 | 1.0 | 2026-11-26 |
| Q2-DISB | disbasia | Disbasia | 1762900710002 | Q2-DISB-0048 | 48 | 1.0 | 2026-11-26 |
| Q2-ABD | abdomen_agudo | AbdomenAgudo | 1762900710003 | Q2-ABD-0046 | 45 | 1.0 | 2026-11-26 |
| Q2-NEO | neoplasias_gi | NeoplasiasGI | 1762900710004 | Q2-NEO-0028 | 28 | 1.0 | 2026-11-26 |
| Q2-HEM | hematuria | Hematuria | 1762900710005 | Q2-HEM-0034 | 24 | 1.0 | 2026-11-26 |
| Q2-URI | urinaria_baja | UrinariaBaja | 1762900710006 | Q2-URI-0040 | 40 | 1.0 | 2026-11-26 |
| Q2-COMA | coma | Coma | 1762900710007 | Q2-COMA-0031 | 31 | 1.0 | 2026-11-26 |
| Q2-VASC | vascular | Vascular | 1762900710008 | Q2-VASC-0040 | 37 | 1.0 | 2026-11-26 |
| Q2R2-AZO | azoados | Azoados | 1762900710009 | Q2R2-AZO-0031 | 31 | 1.0 | 2026-11-26 |
| Q2R2-ENV | envejecimiento | Envejecimiento | 1762900710010 | Q2R2-ENV-0027 | 25 | 1.0 | 2026-11-26 |
| Q2R2-GER | sindromes_geriatricos | SindromesGeriatricos | 1762900710011 | Q2R2-GER-0031 | 29 | 1.0 | 2026-11-26 |
| Q2R2-TOX | toxicodependencias | Toxicodependencias | 1762900710012 | Q2R2-TOX-0045 | 45 | 1.0 | 2026-11-13 |
| Q2R2-ANS | ansiedad_panico | AnsiedadPanico | 1762900710013 | Q2R2-ANS-0034 | 34 | 1.0 | 2026-11-26 |
| Q2R2-DEL | delirium_demencia | DeliriumDemencia | 1762900710014 | Q2R2-DEL-0036 | 36 | 1.0 | 2026-11-26 |
| Q2R2-ANI | trastornos_animo | TrastornosAnimo | 1762900710015 | Q2R2-ANI-0034 | 34 | 1.0 | 2026-11-26 |
| Q2R2-DER | lesiones_dermicas | LesionesDermicas | 1762900710016 | Q2R2-DER-0036 | 36 | 1.0 | 2026-11-26 |
<!-- registro:fin -->
