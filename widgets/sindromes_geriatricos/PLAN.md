# Síndromes geriátricos — plan del orquestador

Fuentes (prioridad): 1) **Caso de Doña Rosa, segunda parte** (abajo); 2) **sílabo de la 2.ª rotación, Caso 3 — Síndromes geriátricos** y Caso 2 (escalas: Barthel, MMSE, Yesavage, MNA, velocidad de la marcha, Tinetti, Up and Go, ECOG), con su bibliografía (Harrison 22e 2025, Farreras-Rozman 20.ª ed. 2024 —el sílabo cita ediciones 19 y 17: discrepancia—, Kane *Principios de geriatría clínica* 8e 2018, MSP *Normas y protocolos de atención integral de salud de las y los adultos mayores* 2010); 3) guías vigentes: ICFSR 2024 (fragilidad), EWGSOP2 2019 (sarcopenia), GLIM 2019/ESPEN geriatría 2022 (desnutrición), AGS Beers 2023 y STOPP/START v3 2023 (polifarmacia), World Guidelines for Falls Prevention 2022 (caídas), ESC 2021/2023 (IC).

Skill: **widget-ensenanza v11**, modo multi → `Sindromes_geriatricos_widget_v11.html`.

## Caso (segunda parte, entregado por Ricardo)

Doña Rosa, 83 años, viuda, vive con su hijo. Antecedentes (primera parte del caso, `widgets/sindrome_confusional/`): IC hipertensiva NYHA II hace 10 años (losartán 25 mg am + 12,5 mg pm, **diltiazem 60 mg bid**, furosemida 40 mg am); lumbociatalgia crónica por espondilolistesis L5-S1 (paracetamol 500 mg tid, tramadol 5 gotas bid, **pregabalina 25 mg am + 50 mg hs**); gonartrosis (glucosamina); DM2 insulinorrequiriente (insulina NPH 12 U hs + metformina 500 mg bid); hipotiroidismo subclínico; IVU recurrente; osteopenia; deterioro cognitivo de 2 años y episodio confusional previo.

**Motivo de consulta:** disnea, decaimiento y falta de apetito.
**Enfermedad actual:** desde hace dos semanas, exacerbación de la disnea que progresó de medianos a pequeños esfuerzos; edema vespertino de miembros inferiores que dificulta la marcha y cede parcialmente con furosemida; toma los medicamentos como se le indicó. Hiporexia, muy decaída, ha dejado de hacer las cosas que antes hacía. Antes de su ingreso hospitalario por COVID-19 era autónoma (preparaba sus alimentos; una empleada se encargaba del orden, la limpieza y la ropa). Ahora necesita ayuda para el traslado cama-silla y para usar el retrete, para ducharse y para ponerse medias y zapatos. Come sola y usa bien los utensilios.

## Router

`Modo: multi · Entidades: e1=Fragilidad (principal), e2=Inmovilidad, e3=Desnutrición, e4=Polifarmacia, e5=Caídas · Amenaza: e4 · Override: no`

- **Presentación común:** adulto mayor con **declive funcional subagudo** (pérdida de actividades básicas de la vida diaria tras una hospitalización), hiporexia y decaimiento.
- **Eje del grupo:** de la reserva perdida (fragilidad) a sus mecanismos de entrada (reposo, nutrición, fármacos) y al desenlace (caída).
- **Amenaza = e4 (polifarmacia e iatrogenia):** no reconocida causa descompensación (diltiazem en IC con FE reducida, edema por pregabalina tratado con más diurético = cascada de prescripción), hipoglucemia y caídas.
- Fuera del grupo (con su widget): delirium y demencia (`trastornos_neurocognitivos`), depresión (`trastornos_animo`): se citan como vecinos en «No confundir con…». Incontinencia y úlceras por presión: dentro de inmovilidad (complicación) o mencionadas en `vis`.

| id | Botón | Parte | Ejecutor | Rango de citas |
|---|---|---|---|---|
| vis | Visión de conjunto | 05_vis | sonnet | 501–599 |
| e1 | Fragilidad | 21_e1 | sonnet | 1–99 |
| e2 | Inmovilidad | 22_e2 | sonnet | 101–199 |
| e3 | Desnutrición | 23_e3 | sonnet | 201–299 |
| e4 | Polifarmacia | 24_e4 | sonnet | 301–399 |
| e5 | Caídas | 25_e5 | sonnet | 401–499 |
| sin | Errores | 80_sin | sonnet (con vis) | — |
| pan | Panorama | 02_pan | al final | reutiliza |

Las referencias se fusionan y renumeran con `kit/renumerar.py` al final.
