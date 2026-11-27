# Síndromes geriátricos — plan del orquestador

Fuentes (prioridad): 1) **Caso de Doña Rosa, segunda parte** (abajo); 2) **sílabo de la 2.ª rotación, Caso 3 — Síndromes geriátricos** y Caso 2 (escalas: Barthel, MMSE, Yesavage, MNA, velocidad de la marcha, Tinetti, Up and Go, ECOG), con su bibliografía (Harrison 22e 2025, Farreras-Rozman 20.ª ed. 2024 —el sílabo cita ediciones 19 y 17: discrepancia—, Kane *Principios de geriatría clínica* 8e 2018, MSP *Normas y protocolos de atención integral de salud de las y los adultos mayores* 2010); 3) guías vigentes: ICFSR 2024 (fragilidad), EWGSOP2 2019 (sarcopenia), GLIM 2019/ESPEN geriatría 2022 (desnutrición), AGS Beers 2023 y STOPP/START v3 2023 (polifarmacia), World Guidelines for Falls Prevention 2022 (caídas), ESC 2021/2023 (IC).

Skill: **widget-ensenanza v11**, modo multi → `Sindromes_geriatricos_widget_v11.html`.

## Caso (segunda parte, entregado por Ricardo)

Doña Rosa, 83 años, viuda, vive con su hijo. Antecedentes (primera parte del caso, `widgets/sindrome_confusional/`): IC hipertensiva NYHA II hace 10 años (losartán 25 mg am + 12,5 mg pm, **diltiazem 60 mg bid**, furosemida 40 mg am); lumbociatalgia crónica por espondilolistesis L5-S1 (paracetamol 500 mg tid, tramadol 5 gotas bid, **pregabalina 25 mg am + 50 mg hs**); gonartrosis (glucosamina); DM2 insulinorrequiriente (insulina NPH 12 U hs + metformina 500 mg bid); hipotiroidismo subclínico; IVU recurrente; osteopenia; deterioro cognitivo de 2 años y episodio confusional previo.

**Motivo de consulta:** disnea, decaimiento y falta de apetito.
**Enfermedad actual:** desde hace dos semanas, exacerbación de la disnea que progresó de medianos a pequeños esfuerzos; edema vespertino de miembros inferiores que dificulta la marcha y cede parcialmente con furosemida; toma los medicamentos como se le indicó. Hiporexia, muy decaída, ha dejado de hacer las cosas que antes hacía. Antes de su ingreso hospitalario por COVID-19 era autónoma (preparaba sus alimentos; una empleada se encargaba del orden, la limpieza y la ropa). Ahora necesita ayuda para el traslado cama-silla y para usar el retrete, para ducharse y para ponerse medias y zapatos. Come sola y usa bien los utensilios.

## Router (v3, un solo widget · multi ampliado)

Ricardo pidió el temario del docente en un único widget y cambiar la regla de máximo 5 entidades. El kit admite ahora **multi ampliado** (6–15 entidades; `docs/DECISIONES_v11.md` §4). Se unieron los tres widgets de la v2 en `ensenanza/` → `Sindromes_geriatricos_widget_v11.html`, en el orden del docente:

`Modo: multi ampliado · Entidades: e1=Inmovilidad (principal), e2=Caídas, e3=Incontinencia, e4=Deterioro cognitivo, e5=Fragilidad, e6=Sarcopenia, e7=Polifarmacia (e iatrogenia), e8=Úlceras por presión, e9=Sueño, e10=Malnutrición, e11=Estreñimiento, e12=Aislamiento social, e13=Maltrato · Amenaza: e4 (delirium) · Override: sí`

Generalidades, diagnóstico (valoración geriátrica integral) y tratamiento van en `vis`, que tiene la tabla de 13 columnas y tres simuladores diferenciales (4 I, fragilidad y fármacos, síndromes que no se refieren). Partes `201_e1` … `213_e13`.
