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
| Q2-OJO | — | OjoRojo | 1762900710001 | — | 0 | — | — |
| Q2-DISB | — | Disbasia | 1762900710002 | — | 0 | — | — |
| Q2-ABD | — | AbdomenAgudo | 1762900710003 | — | 0 | — | — |
| Q2-NEO | — | NeoplasiasGI | 1762900710004 | — | 0 | — | — |
| Q2-HEM | — | Hematuria | 1762900710005 | — | 0 | — | — |
| Q2-URI | — | UrinariaBaja | 1762900710006 | — | 0 | — | — |
| Q2-COMA | — | Coma | 1762900710007 | — | 0 | — | — |
| Q2-VASC | — | Vascular | 1762900710008 | — | 0 | — | — |
| Q2R2-AZO | — | Azoados | 1762900710009 | — | 0 | — | — |
| Q2R2-ENV | — | Envejecimiento | 1762900710010 | — | 0 | — | — |
| Q2R2-GER | — | SindromesGeriatricos | 1762900710011 | — | 0 | — | — |
| Q2R2-TOX | — | Toxicodependencias | 1762900710012 | — | 0 | — | — |
| Q2R2-ANS | — | AnsiedadPanico | 1762900710013 | — | 0 | — | — |
| Q2R2-DEL | — | DeliriumDemencia | 1762900710014 | — | 0 | — | — |
| Q2R2-ANI | — | TrastornosAnimo | 1762900710015 | — | 0 | — | — |
| Q2R2-DER | — | LesionesDermicas | 1762900710016 | — | 0 | — | — |
<!-- registro:fin -->
