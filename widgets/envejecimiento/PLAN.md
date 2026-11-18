# Envejecimiento — plan del orquestador

Fuente de alcance: **sílabo de la 2.ª rotación, Caso 2 — Envejecimiento** (`fuentes/syllabus_quirurgica2_segunda_rotacion.md`): situación del adulto mayor en Ecuador, América Latina y el mundo; ley del anciano; abuso y maltrato; fisiología de los procesos de envejecimiento y sus teorías; grandes síndromes geriátricos; escalas (Barthel, MMSE, Yesavage, MNA, velocidad de la marcha, Tinetti, Up and Go, ECOG); trabajo autónomo: indicadores, historia clínica, envejecimiento satisfactorio y activo.

Skill: **widget-ensenanza v11**. Widget único `ensenanza/` → `../Envejecimiento_widget_v11.html`.

## Router

`Modo: mono · Entidades: e1=Envejecimiento (senescencia fisiológica) · Amenaza: — · Override: no`

El envejecimiento no es una enfermedad sino un proceso con mecanismo propio (marcas del envejecimiento) y manejo propio (valoración geriátrica integral y envejecimiento saludable), así que se trata como una sola entidad en modo mono. Los síndromes geriátricos (fragilidad, caídas, delirium, incontinencia, polifarmacia, desnutrición, úlceras por presión) son la evolución desfavorable: van en «Seguimiento». Delirium y demencia tienen widget propio (`trastornos_neurocognitivos`) y aquí solo se remiten.

Adaptación al área (geriatría): «Clínica» = cambios esperables por aparatos y sistemas (los «signos» son hallazgos de la senescencia con su mecanismo); «Plan diagnóstico» = valoración geriátrica integral y escalas; «Plan de tratamiento» = envejecimiento saludable y activo (ejercicio, nutrición, vacunación, deprescripción); la tabla de fármacos son las vacunas y principios de prescripción.

## Pestañas (orden de barra) y partes

| Parte | data-tab | Botón | Contenido |
|---|---|---|---|
| 10_def | def | Definición y epidemiología | envejecimiento, senescencia/senectud/senilidad, homeostenosis, edad biológica vs cronológica, adulto mayor en Ecuador (≥65 años, LOPAM); epidemiología mundial, AL y Ecuador |
| 10x_eco | eco | Ecuador, ley y maltrato | situación del adulto mayor en Ecuador/AL/mundo (indicadores), Ley Orgánica de las Personas Adultas Mayores (2019), abuso y maltrato (tipos, factores, detección, ruta) |
| 11_fis | fis | Teorías y fisiopatología | teorías estocásticas y programadas; 12 marcas; timeline m-1…m-10 |
| 12_cli | cli | Cambios por sistemas | signos s-1…s-9 + tabla de cambios menores por aparato |
| 13_dx | dx | Valoración geriátrica | VGI, escalas con umbrales, distinguir senescencia de enfermedad; simulador |
| 14_tx | tx | Envejecimiento saludable | envejecimiento activo/satisfactorio, ejercicio multicomponente, nutrición, vacunas (tabla), deprescripción; simulador |
| 15_seg | seg | Síndromes geriátricos | fragilidad, sarcopenia, caídas, polifarmacia, desnutrición, incontinencia, úlceras, delirium (remisión); simulador; `.acc.refs` |

## Mapa de nodos (fis) y signos (cli) — fijo

| id | data-paso | clin | Enlaza a |
|---|---|---|---|
| m-1 | Daño molecular acumulado sin reparar | 0 | — |
| m-2 | Acortamiento telomérico limita las divisiones | 0 | — |
| m-3 | Disfunción mitocondrial y estrés oxidativo | 0 | — |
| m-4 | Senescencia celular con secreción proinflamatoria | 0 | — |
| m-5 | Inflamación crónica de bajo grado e inmunosenescencia | 1 | s-8, s-9 |
| m-6 | Agotamiento de células madre y menor regeneración | 1 | s-7 |
| m-7 | Fibrosis y rigidez de los tejidos elásticos | 1 | s-1, s-2 |
| m-8 | Pérdida de unidades funcionales del órgano | 1 | s-3, s-4, s-5 |
| m-9 | Desregulación neuroendocrina y del ritmo circadiano | 1 | s-6 |
| m-10 | Homeostenosis: menor reserva ante el estrés | 1 | s-9 |

| id | Signo (h4) | Aparato | ← Nodo |
|---|---|---|---|
| s-1 | Presión de pulso amplia por rigidez arterial | Cardiovascular | m-7 |
| s-2 | Menor reserva respiratoria y tos débil | Respiratorio | m-7 |
| s-3 | Filtrado glomerular bajo con creatinina normal | Renal | m-8 |
| s-4 | Estreñimiento y saciedad precoz | Digestivo | m-8 |
| s-5 | Presbiacusia | Sentidos | m-8 |
| s-6 | Nocturia | Urinario bajo | m-9 |
| s-7 | Piel delgada y cicatrización lenta | Tegumentario | m-6 |
| s-8 | Infección con presentación atípica | Inmunológico | m-5 |
| s-9 | Sarcopenia y marcha lenta | Musculoesquelético | m-5, m-10 |

Cambios sin ficha propia (tabla de signos menores en cli): hígado y farmacocinética, endocrino-metabólico, cognición normal, visión, hueso.

## Referencias

Banco común 1–31 (`refs_pool.txt` del orquestador). Cada ejecutor usa un tramo propio para referencias nuevas: def 101–120 · eco 121–140 · fis 141–160 · cli 161–180 · dx 181–210 · tx 211–240 · seg 241–270. El orquestador densifica, arma la `ol.vanc` en `15_seg` y ejecuta `kit/renumerar.py`.
