# Graph Report - Widgets-Educativos-  (2026-10-01)

## Corpus Check
- Corpus is ~9,545 words - fits in a single context window. You may not need a graph.

## Summary
- 209 nodes · 281 edges · 9 communities
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 17 edges (avg confidence: 0.76)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Caso Hematuria y urinaria baja
- Kit v10: componentes
- Dolor abdominal y neoplasias GI
- Caso Disbasia
- Kit v10: validador
- Caso Coma / TCE
- Caso Ojo rojo
- Caso Patología vascular
- Curso, evaluación y bibliografía

## God Nodes (most connected - your core abstractions)
1. `Caso Dolor abdominal agudo` - 26 edges
2. `Caso Disbasia` - 24 edges
3. `Caso Patologia urinaria baja` - 23 edges
4. `Salud Integral Hospitalaria 2 Quirurgica 2 (09-Q0989)` - 22 edges
5. `Caso Ojo rojo` - 21 edges
6. `Caso Coma / Traumatismo craneoencefalico` - 21 edges
7. `Caso Patologias vasculares frecuentes` - 21 edges
8. `Caso Hematuria` - 20 edges
9. `Caso Dolor abdominal y perdida de peso (neoplasias gastrointestinales)` - 19 edges
10. `kit_head.html (CSS y componentes)` - 17 edges

## Surprising Connections (you probably didn't know these)
- `Skill widget-ensenanza v10` --conceptually_related_to--> `Salud Integral Hospitalaria 2 Quirurgica 2 (09-Q0989)`  [INFERRED]
  fuentes/Prompt Widget Ensenanza V10.md → fuentes/Syllabus_primera_rotacion_10mo.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Presentacion urologica compartida (hematuria, urinaria baja, TB urinaria)** — fuentes_syllabus_primera_rotacion_10mo_caso_hematuria, fuentes_syllabus_primera_rotacion_10mo_caso_patologia_urinaria_baja, fuentes_syllabus_primera_rotacion_10mo_tuberculosis_urinaria, fuentes_syllabus_primera_rotacion_10mo_traumatismo_uretral [INFERRED 0.75]
- **Dolor abdominal compartido (abdomen agudo, neoplasias, vascular)** — fuentes_syllabus_primera_rotacion_10mo_caso_dolor_abdominal_agudo, fuentes_syllabus_primera_rotacion_10mo_caso_dolor_abdominal_y_perdida_de_peso_neoplasias_gastrointestinales, fuentes_syllabus_primera_rotacion_10mo_caso_patologias_vasculares_frecuentes, fuentes_syllabus_primera_rotacion_10mo_aneurisma_de_aorta_abdominal [INFERRED 0.75]
- **Kit fijo: CSS + JS + validador ensamblan el widget** — fuentes_prompt_widget_ensenanza_v10_kit_head_html_css_y_componentes, fuentes_prompt_widget_ensenanza_v10_kit_script_html_js_del_kit, fuentes_prompt_widget_ensenanza_v10_validar_py_validador_fijo [EXTRACTED 1.00]

## Communities (9 total, 0 thin omitted)

### Community 0 - "Caso Hematuria y urinaria baja"
Cohesion: 0.07
Nodes (33): Bolenz et al. The investigation of hematuria (Dtsch Arztebl Int 2018), Bradley et al. Diet, fluid intake, caffeine, alcohol, tobacco and LUTS (J Urol 2017), Cancer de prostata, Cancer del tracto urinario, Caso Hematuria, Caso Patologia urinaria baja, Cistitis, Cistoscopia (+25 more)

### Community 1 - "Kit v10: componentes"
Cohesion: 0.10
Nodes (30): Acordeon (.acc), Badges (.badge b-az..b-rs), Cajas highlight (.hb az/am/ro/ve/vi), Chequeo de simuladores .dc (contrafactual, sin Bayes/VPP), Etapa del panorama (.etapa, .res, .perla, .go), Feynman (.fey), Ficha Que veras (.qv, .signo), kit_head.html (CSS y componentes) (+22 more)

### Community 2 - "Dolor abdominal y neoplasias GI"
Cohesion: 0.07
Nodes (32): Abdomen agudo, Apendicitis aguda, Cancer de boca, Cancer de colon, Cancer de duodeno, Cancer de esofago, Cancer de estomago, Cancer de higado (+24 more)

### Community 3 - "Caso Disbasia"
Cohesion: 0.09
Nodes (22): Alteraciones del pie (plano, cavo, equino, varo, valgo), Anteversion femoral, Artritis septica, Caso Disbasia, Disbasia, Dismetria de miembros inferiores, Displasia del desarrollo de la cadera, Enfermedad de Osgood-Schlatter (+14 more)

### Community 4 - "Kit v10: validador"
Cohesion: 0.14
Nodes (19): Cambios respecto a v9 (router mono/multi, tabla en blanco, contrafactual), Chequeo de cadenas prohibidas (localStorage, style inline, etc.), Chequeo de ensamblaje del kit y marcas, Chequeo de Feynman (2 en e1, 1 en secundarias), Chequeo de ids m/s y xref intra-entidad, Chequeo de JS (node --check), Chequeo de manifiesto (modo), Chequeo de pestañas y orden de botones (+11 more)

### Community 5 - "Caso Coma / TCE"
Cohesion: 0.11
Nodes (19): ATLS Student Course Manual 10th ed. (ACS 2018), Caso Coma / Traumatismo craneoencefalico, Coma, Coma estructural, Coma metabolico, Escala de Glasgow, Estudios toxicologicos, Hiperuricemia (+11 more)

### Community 6 - "Caso Ojo rojo"
Cohesion: 0.12
Nodes (18): Agudeza visual, Ambliopia (ojo vago), Blefaritis, Caso Ojo rojo, Celulitis orbitaria, Conjuntivitis (bacteriana, viral, alergica), Coroidoretinitis, DynaMed 2024: Red eye, conjuntivitis, Blepharitis, Amblyopia, Uveitis (+10 more)

### Community 7 - "Caso Patología vascular"
Cohesion: 0.12
Nodes (17): Aneurisma de aorta abdominal, Angiografia, Caso Patologias vasculares frecuentes, Di Nisio, van Es, Buller. Deep vein thrombosis and pulmonary embolism (Lancet 2016), Doppler vascular, DynaMed 2024: Peripheral artery disease, Deep vein thrombosis, Venous insufficiency, Lower extremity ulcer, Enfermedad arterial periferica, Flegmasia alba dolens (+9 more)

### Community 8 - "Curso, evaluación y bibliografía"
Cohesion: 0.12
Nodes (17): Bates, Guia de Exploracion Fisica e Historia Clinica (Bickley, 2013), ClinicalKey, DynaMed, AAFP, NEJM (recursos digitales), Correquisitos (Quirurgica 1, Medicina de Laboratorio, Destrezas clinicas quirurgicas 2), Docente Ivan Dueñas Espin, Esquema de evaluacion ABP por caso, Evaluacion de grado: 3 parciales (promedio de 8 casos ABP) y examen final, 25% c/u, Farreras-Rozman. Medicina interna 22a ed. (2024), Harrison. Principios de Medicina Interna, 22e (Longo, 2025) (+9 more)

## Knowledge Gaps
- **143 isolated node(s):** `Participacion sesion de apertura (1 pt)`, `Participacion sesiones de monitoreo (2 pts)`, `Prueba de monitoreo (1 pt)`, `Prueba de cierre del docente consultor (1 pt)`, `Prueba final del caso clinico (3 pts)` (+138 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 143 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Salud Integral Hospitalaria 2 Quirurgica 2 (09-Q0989)` connect `Curso, evaluación y bibliografía` to `Caso Hematuria y urinaria baja`, `Dolor abdominal y neoplasias GI`, `Caso Disbasia`, `Kit v10: validador`, `Caso Coma / TCE`, `Caso Ojo rojo`, `Caso Patología vascular`?**
  _High betweenness centrality (0.525) - this node is a cross-community bridge._
- **Why does `Skill widget-ensenanza v10` connect `Kit v10: validador` to `Curso, evaluación y bibliografía`?**
  _High betweenness centrality (0.367) - this node is a cross-community bridge._
- **Why does `Prompt Widget Ensenanza v10 (kit fijo)` connect `Kit v10: validador` to `Kit v10: componentes`?**
  _High betweenness centrality (0.317) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Caso Dolor abdominal agudo` (e.g. with `Caso Dolor abdominal y perdida de peso (neoplasias gastrointestinales)` and `Caso Patologias vasculares frecuentes`) actually correct?**
  _`Caso Dolor abdominal agudo` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Participacion sesion de apertura (1 pt)`, `Participacion sesiones de monitoreo (2 pts)`, `Prueba de monitoreo (1 pt)` to the rest of the system?**
  _143 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Caso Hematuria y urinaria baja` be split into smaller, more focused modules?**
  _Cohesion score 0.07196969696969698 - nodes in this community are weakly interconnected._
- **Should `Kit v10: componentes` be split into smaller, more focused modules?**
  _Cohesion score 0.09879032258064516 - nodes in this community are weakly interconnected._