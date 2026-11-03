# Ginecología · Ciclo ovárico, cuerpo albo y terapia hormonal de la menopausia — plan del orquestador

Fuente del pedido: Ricardo (estudio personal). **El tema no figura en ninguno de los dos sílabos** (`fuentes/syllabus_quirurgica2*.md`); el caso más cercano es «Envejecimiento» (2.ª rotación: fisiología del envejecimiento, evaluación integral de la mujer adulta mayor). Alcance y bibliografía salen de la guía vigente y de los libros de la tabla de ediciones del protocolo (Guyton 14e, Ross 8e, Harrison 22e, Goodman & Gilman 14e), más lo verificado en PubMed, Consensus y NIH (NIA, NCBI Bookshelf, ClinicalTrials.gov).

## Router

`Modo: mono · Entidades: e1=Menopausia y terapia hormonal · Amenaza: — · Override: no`

- Una sola entidad con mecanismo y manejo propios: la deficiencia estrogénica de la menopausia y su tratamiento hormonal.
- El ciclo ovárico normal (folículo → cuerpo lúteo → **cuerpo albo**) es el sustrato: va en la pestaña adicional `cic` («Ciclo ovárico y cuerpo albo», parte `10x_cic.html`, entre `def` y `fis`).
- Puente conceptual que vertebra el widget: el cuerpo albo es la cicatriz sin función endocrina del cuerpo lúteo. Tras la menopausia ya no se forman cuerpos lúteos: no hay progesterona endógena. Por eso, en la mujer con útero, el estrógeno de la terapia hormonal se acompaña siempre de un progestágeno (el que «reemplaza» al cuerpo lúteo) para proteger el endometrio; sin útero, estrógeno solo.

## Pestañas (orden de barra)

`pan def cic fis cli dx tx seg`

| Pestaña | Parte | Simulador | Feynman |
|---|---|---|---|
| def | 10_def | — | 1 |
| cic | 10x_cic | fase del ciclo por día y duración → estructura dominante y perfil hormonal | 1 |
| fis | 11_fis | — | 2 |
| cli | 12_cli | — | 1 |
| dx | 13_dx | estadio STRAW+10 y cuándo pedir FSH | 1 |
| tx | 14_tx | esquema de terapia hormonal según útero, edad/tiempo desde la menopausia, contraindicaciones y síntoma | 1 |
| seg | 15_seg | vigilancia y conducta ante sangrado o duración de la terapia | 1 |

## Mapa de nodos (`fis`) y signos (`cli`)

| id | data-paso | clin | signo |
|---|---|---|---|
| m-1 | Atresia agota la reserva folicular | 0 | — |
| m-2 | Inhibina B cae y la FSH sube | 1 | s-1 |
| m-3 | Ciclos anovulatorios sin cuerpo lúteo | 1 | s-1 |
| m-4 | Estradiol cae de forma definitiva | 1 | s-1 |
| m-5 | Neuronas KNDy estrechan la zona termoneutral | 1 | s-2, s-3 |
| m-6 | Epitelio urogenital pierde trofismo | 1 | s-4 |
| m-7 | Resorción ósea supera a la formación | 1 | s-5 |
| m-8 | Endotelio y lípidos pierden protección estrogénica | 0 | — |

Signos: s-1 Cambio del patrón menstrual · s-2 Bochorno y sudoración nocturna · s-3 Insomnio y cambios del ánimo · s-4 Síndrome genitourinario de la menopausia · s-5 Pérdida de talla o fractura por fragilidad.

## Orquestación

Orquestador: router, PLAN, manifiesto, numeración de referencias, `01_nav`, ensamblaje de `90_sim`, construir/validar/auditar/probar. Ejecutores `sonnet`: investigación (PubMed, Consensus, NIH), redacción por pares de pestañas y Panorama. `haiku`: pasada de verificación de `pendientes`, renumeración Vancouver y conteos.

Slug: `Ciclo_ovarico_menopausia_TH_widget_v10.html` · título `Ciclo ovárico, cuerpo albo y terapia hormonal`.
