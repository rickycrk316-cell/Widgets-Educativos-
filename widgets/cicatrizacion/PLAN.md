# Cicatrización patológica — plan del orquestador

Pedido del estudiante: widget educativo sobre la **infiltración de triamcinolona en cicatrices queloides**. El tema no figura en los sílabos de `fuentes/`; es estudio complementario de Quirúrgica 2 (cirugía plástica y heridas).

## Router (§2)

La infiltración es un procedimiento, no una entidad: no tiene mecanismo de enfermedad propio. La entidad es el **queloide**; la cicatriz hipertrófica es su diferencial principal (va en «No confundir con…» y en el simulador de `dx`, no como segunda entidad). Una entidad → **mono**. El procedimiento, que es el foco del pedido, ocupa la pestaña adicional.

- `Modo: mono · Entidades: e1=Cicatriz queloide · Amenaza: — · Override: no`
- Pestaña adicional `inf` («Infiltración con triamcinolona»), parte `14x_inf.html`, en su lugar lógico **entre `tx` y `seg`** (barra: `pan def fis cli dx tx inf seg`), con su etapa en `pan` tras Tratamiento.
- Slug: `Queloide_triamcinolona_widget_v10.html` · carpeta `queloide_triamcinolona/`.

## Reparto entre pestañas (qué va dónde)

| Pestaña | Qué cubre | Qué no |
|---|---|---|
| `def` | Definición (sobrepasa los bordes de la herida, no regresa), sustrato normal (fases de cicatrización y remodelado del colágeno), criterios, «No confundir con…» (hipertrófica, dermatofibrosarcoma protuberans, cicatriz madura/ensanchada), epidemiología (fototipos IV–VI, 10–30 años, zonas de tensión) | Dosis, técnica |
| `fis` | Cascada fija (nodos abajo), etiología: genética/étnica, tipo de lesión, tensión mecánica, hormonas (embarazo, pubertad) | Fármacos |
| `cli` | Signos fijos (abajo), localizaciones típicas, síntomas | Conducta |
| `dx` | Diagnóstico clínico; biopsia solo si atípico, recidiva rápida o sospecha de malignidad; escalas (POSAS, Vancouver Scar Scale, JSS); fotografía y medición basales | Tratamiento |
| `tx` | Escalera terapéutica: prevención (silicona, presoterapia), primera línea intralesional (triamcinolona), combinaciones (5-FU, crioterapia), escisión **siempre** con adyuvancia (triamcinolona o radioterapia), láser, alternativas | Técnica fina de inyección (va en `inf`) |
| `inf` | **Prioridad del estudiante: indicaciones, contraindicaciones, técnica, dosificación y frecuencia**, cada uno con su tabla o lista. El procedimiento: mecanismo farmacológico del corticoide sobre el fibroblasto, presentaciones y concentraciones (10–40 mg/mL), dosis máxima por sesión, intervalo, plano correcto (dermis, no subcutáneo), aguja/jeringa, anestesia previa, crioterapia previa, signo de blanqueamiento, cuántas sesiones, criterios de respuesta y de parada, contraindicaciones | Complicaciones en detalle (van en `seg`) |
| `seg` | Ciclo revisar-evaluar-ajustar, recidiva, complicaciones de la infiltración por su mecanismo (atrofia, hipopigmentación, telangiectasias, necrosis, efectos sistémicos: Cushing, alteración menstrual, hiperglucemia), `.acc.refs` | — |

## Nodos de `fis` (fijos: ids `m-1`…`m-8`)

1. `m-1` Lesión que alcanza la dermis reticular (cirugía, quemadura, acné, piercing, vacuna).
2. `m-2` Inflamación crónica persistente en la dermis reticular.
3. `m-3` Fibroblasto hiperactivo: señal TGF-β1/Smad sostenida y menor apoptosis.
4. `m-4` Exceso de colágeno tipo I desorganizado en haces hialinos gruesos.
5. `m-5` Tensión mecánica de la piel amplifica la señal (mecanotransducción).
6. `m-6` Neoangiogénesis y fibras nerviosas nuevas: eritema, prurito y dolor.
7. `m-7` Crecimiento invasivo más allá de los bordes de la herida original.
8. `m-8` Recidiva tras escisión aislada por reactivar la cascada.

`inf` y `tx` enlazan con `.xref` a `m-3` y `m-4` (donde actúa la triamcinolona) y `seg` a `m-8`.

## Signos de `cli` (fijos: ids `s-1`…`s-5`)

1. `s-1` Placa o nódulo firme, brillante, que sobrepasa los bordes de la herida.
2. `s-2` Prolongaciones en «pinza de cangrejo».
3. `s-3` Prurito.
4. `s-4` Dolor o hiperestesia.
5. `s-5` Borde activo eritematoso con telangiectasias.

## Simuladores

- `dx`: queloide frente a cicatriz hipertrófica frente a lesión que exige biopsia.
- `tx`: elegir conducta por escenario (queloide pequeño reciente, queloide grande en lóbulo para escisión, recidiva tras escisión).
- `seg`: atrofia e hipopigmentación tras la tercera sesión → qué ajustar.

## Fuentes

Hoja de datos verificada en PubMed por el ejecutor de investigación (`queloide_triamcinolona/FUENTES.md`), con numeración Vancouver única para todas las partes. Prioridad: recomendaciones internacionales (Gold 2014; Ogawa/JSW 2019 y consenso actualizado), revisiones sistemáticas sobre triamcinolona intralesional y combinaciones, Rook/Bolognia como texto. Cifras sin fuente leída → `[VERIFICAR EN FUENTE]`.

## Reglas de contenido y diseño

Las mismas del plan de `neoplasias_gi/PLAN.md` (§ «Reglas de diseño para ejecutores»): solo clases del contrato v10, tablas con `<thead>`, sin recuadros anidados, tipo oración, párrafos ≤90 palabras, ≤1 `<b>` por párrafo, sin emojis, coma decimal.
