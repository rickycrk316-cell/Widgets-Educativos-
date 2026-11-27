# Síndromes geriátricos — plan del orquestador

Fuentes (prioridad): 1) **Caso de Doña Rosa, segunda parte** (abajo); 2) **sílabo de la 2.ª rotación, Caso 3 — Síndromes geriátricos** y Caso 2 (escalas: Barthel, MMSE, Yesavage, MNA, velocidad de la marcha, Tinetti, Up and Go, ECOG), con su bibliografía (Harrison 22e 2025, Farreras-Rozman 20.ª ed. 2024 —el sílabo cita ediciones 19 y 17: discrepancia—, Kane *Principios de geriatría clínica* 8e 2018, MSP *Normas y protocolos de atención integral de salud de las y los adultos mayores* 2010); 3) guías vigentes: ICFSR 2024 (fragilidad), EWGSOP2 2019 (sarcopenia), GLIM 2019/ESPEN geriatría 2022 (desnutrición), AGS Beers 2023 y STOPP/START v3 2023 (polifarmacia), World Guidelines for Falls Prevention 2022 (caídas), ESC 2021/2023 (IC).

Skill: **widget-ensenanza v11**, modo multi → `Sindromes_geriatricos_widget_v11.html`.

## Caso (segunda parte, entregado por Ricardo)

Doña Rosa, 83 años, viuda, vive con su hijo. Antecedentes (primera parte del caso, `widgets/sindrome_confusional/`): IC hipertensiva NYHA II hace 10 años (losartán 25 mg am + 12,5 mg pm, **diltiazem 60 mg bid**, furosemida 40 mg am); lumbociatalgia crónica por espondilolistesis L5-S1 (paracetamol 500 mg tid, tramadol 5 gotas bid, **pregabalina 25 mg am + 50 mg hs**); gonartrosis (glucosamina); DM2 insulinorrequiriente (insulina NPH 12 U hs + metformina 500 mg bid); hipotiroidismo subclínico; IVU recurrente; osteopenia; deterioro cognitivo de 2 años y episodio confusional previo.

**Motivo de consulta:** disnea, decaimiento y falta de apetito.
**Enfermedad actual:** desde hace dos semanas, exacerbación de la disnea que progresó de medianos a pequeños esfuerzos; edema vespertino de miembros inferiores que dificulta la marcha y cede parcialmente con furosemida; toma los medicamentos como se le indicó. Hiporexia, muy decaída, ha dejado de hacer las cosas que antes hacía. Antes de su ingreso hospitalario por COVID-19 era autónoma (preparaba sus alimentos; una empleada se encargaba del orden, la limpieza y la ropa). Ahora necesita ayuda para el traslado cama-silla y para usar el retrete, para ducharse y para ponerse medias y zapatos. Come sola y usa bien los utensilios.

## Router (v2, temario del docente para la clase)

Temario: generalidades, diagnóstico y tratamiento; las 4 I (inmovilidad, inestabilidad y caídas, incontinencia, deterioro cognitivo); además fragilidad, sarcopenia, polifarmacia, iatrogenia, úlceras por presión, alteraciones del sueño, malnutrición, estreñimiento, aislamiento social, abuso y maltrato. Son 14 entidades: la skill admite 3–5 por widget multi, así que se parten en 3 widgets con un índice común en el artefacto. Generalidades (definición de síndrome geriátrico, valoración geriátrica integral = diagnóstico, principios de tratamiento interdisciplinario) van en `vis` de W1; `vis` de W2 y W3 remiten a W1 para lo común.

| Widget | Carpeta | Salida | Entidades (principal · amenaza) |
|---|---|---|---|
| W1 Las 4 I | `cuatro_i/` | `Sindromes_geriatricos_4I_widget_v11.html` | e1 Inmovilidad (principal) · e2 Caídas · e3 Incontinencia · e4 Deterioro cognitivo (amenaza: delirium) · e5 Úlceras por presión |
| W2 Fragilidad | `fragilidad_nutricion/` | `Fragilidad_sarcopenia_polifarmacia_widget_v11.html` | e1 Fragilidad (principal) · e2 Sarcopenia · e3 Malnutrición · e4 Polifarmacia e iatrogenia (amenaza) |
| W3 Otros | `otros/` | `Sueno_estrenimiento_aislamiento_maltrato_widget_v11.html` | e1 Alteraciones del sueño (principal) · e2 Estreñimiento · e3 Aislamiento social · e4 Abuso y maltrato (amenaza) |

Partes reutilizadas del widget v1 (`ensenanza/`, retirado): Inmovilidad, Caídas, Fragilidad, Desnutrición, Polifarmacia, con citas renumeradas a su rango. Rangos de citas por widget: e1 1–99, e2 101–199, e3 201–299, e4 301–399, e5 401–499, vis 501–599.
