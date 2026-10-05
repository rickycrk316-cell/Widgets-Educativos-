# Graph Report - Widgets-Educativos-  (2026-10-01)

## Corpus Check
- Corpus is ~9,545 words - fits in a single context window. You may not need a graph.

## Summary
- 449 nodes · 755 edges · 15 communities
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 54 edges (avg confidence: 0.76)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Kit v10
- Abdomen agudo vascular (isquemia, aneurisma)
- Dolor abdominal y neoplasias GI
- Saturnismo y porfiria
- Vía biliar: coledocolitiasis y colangitis
- Caso Hematuria y urinaria baja
- Hipopotasemia con íleo
- Apendicitis aguda
- Colelitiasis y colecistitis
- Pancreatitis aguda y escalas
- Caso Disbasia
- Caso Coma / TCE
- Caso Ojo rojo
- Obstrucción intestinal
- Perforación de víscera hueca

## God Nodes (most connected - your core abstractions)
1. `Caso Dolor abdominal agudo` - 30 edges
2. `Pancreatitis aguda` - 26 edges
3. `Caso Disbasia` - 24 edges
4. `Apendicitis aguda` - 24 edges
5. `Colelitiasis y colecistitis aguda` - 24 edges
6. `Caso Patologia urinaria baja` - 23 edges
7. `Salud Integral Hospitalaria 2 Quirurgica 2 (09-Q0989)` - 22 edges
8. `Caso Coma / Traumatismo craneoencefalico` - 22 edges
9. `Caso Patologias vasculares frecuentes` - 22 edges
10. `Caso Ojo rojo` - 21 edges

## Surprising Connections (you probably didn't know these)
- `Lactato mayor de 2 mmol/L (isquemia irreversible)` --references--> `Laboratorio clinico`  [INFERRED]
  widgets/dolor_abdominal/Abdomen_agudo_quirurgico_widget_v10.html → fuentes/Syllabus_primera_rotacion_10mo.md
- `Ecografía de compresión graduada` --references--> `Ecografia abdominal`  [INFERRED]
  widgets/dolor_abdominal/Abdomen_agudo_quirurgico_widget_v10.html → fuentes/Syllabus_primera_rotacion_10mo.md
- `TC con contraste de baja dosis` --references--> `Tomografia computarizada`  [INFERRED]
  widgets/dolor_abdominal/Abdomen_agudo_quirurgico_widget_v10.html → fuentes/Syllabus_primera_rotacion_10mo.md
- `TC con contraste hidrosoluble` --references--> `Tomografia computarizada`  [INFERRED]
  widgets/dolor_abdominal/Abdomen_agudo_quirurgico_widget_v10.html → fuentes/Syllabus_primera_rotacion_10mo.md
- `Prueba que decide: PBG y ALA urinarios en ataque, protegidos de la luz` --references--> `Marcadores bioquimicos`  [INFERRED]
  widgets/dolor_abdominal/Abdomen_agudo_medico_widget_v10.html → fuentes/Syllabus_primera_rotacion_10mo.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Presentacion urologica compartida (hematuria, urinaria baja, TB urinaria)** — fuentes_syllabus_primera_rotacion_10mo_caso_hematuria, fuentes_syllabus_primera_rotacion_10mo_caso_patologia_urinaria_baja, fuentes_syllabus_primera_rotacion_10mo_tuberculosis_urinaria, fuentes_syllabus_primera_rotacion_10mo_traumatismo_uretral [INFERRED 0.75]
- **Dolor abdominal compartido (abdomen agudo, neoplasias, vascular)** — fuentes_syllabus_primera_rotacion_10mo_caso_dolor_abdominal_agudo, fuentes_syllabus_primera_rotacion_10mo_caso_dolor_abdominal_y_perdida_de_peso_neoplasias_gastrointestinales, fuentes_syllabus_primera_rotacion_10mo_caso_patologias_vasculares_frecuentes, fuentes_syllabus_primera_rotacion_10mo_aneurisma_de_aorta_abdominal [INFERRED 0.75]
- **Kit fijo: CSS + JS + validador ensamblan el widget** — fuentes_prompt_widget_ensenanza_v10_kit_head_html_css_y_componentes, fuentes_prompt_widget_ensenanza_v10_kit_script_html_js_del_kit, fuentes_prompt_widget_ensenanza_v10_validar_py_validador_fijo [EXTRACTED 1.00]
- **Las cinco entidades del abdomen agudo quirúrgico** — widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_e1, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_e2, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_e3, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_e4, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_e5 [EXTRACTED 1.00]
- **Guías que sustentan el widget** — widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_ref1, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_ref2, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_ref3, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_ref4, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_ref5 [EXTRACTED 1.00]
- **Simuladores de decisión clínica** — widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_sim_global, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_sim_apendicitis, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_sim_obstruccion, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_sim_perforacion, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_sim_isquemia, widgets_dolor_abdominal_abdomen_agudo_quirurgico_widget_v10_sim_aaa [INFERRED 0.85]
- **Escalas de gravedad del grupo** — widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_tg18_colecistitis_grados, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_tg18_colangitis_grados, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_atlanta, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_ranson_biliar, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_bisap, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_apache2, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_asge_riesgo [INFERRED 0.75]
- **Cadena biliopancreática proximal a distal** — widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_e1, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_e2, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_e3, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_e4 [EXTRACTED 1.00]
- **Conducta que no espera al antibiótico** — widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_amenaza_colangitis, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_drenaje_biliar, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_tg18_colangitis_grados, widgets_dolor_abdominal_dolor_biliopancreatico_widget_v10_cpre_esfinterotomia [INFERRED 0.85]
- **Tres causas médicas de abdomen blando** — widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_e1, widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_e2, widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_e3 [EXTRACTED 1.00]
- **Cadena fisiopatológica de la porfiria aguda intermitente** — widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_e3_deficit_pbg_desaminasa, widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_e3_induccion_alas1, widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_e3_acumulo_ala_pbg, widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_e3_signo_dolor_abdomen_blando [EXTRACTED 1.00]
- **Simuladores de decisión clínica** — widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_sim_dcvis, widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_sim_dce1d, widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_sim_dce1t, widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_sim_dce2, widgets_dolor_abdominal_abdomen_agudo_medico_widget_v10_sim_dce3 [EXTRACTED 1.00]

## Communities (15 total, 0 thin omitted)

### Community 0 - "Kit v10"
Cohesion: 0.06
Nodes (49): Acordeon (.acc), Badges (.badge b-az..b-rs), Cajas highlight (.hb az/am/ro/ve/vi), Cambios respecto a v9 (router mono/multi, tabla en blanco, contrafactual), Chequeo de cadenas prohibidas (localStorage, style inline, etc.), Chequeo de ensamblaje del kit y marcas, Chequeo de Feynman (2 en e1, 1 en secundarias), Chequeo de ids m/s y xref intra-entidad (+41 more)

### Community 1 - "Abdomen agudo vascular (isquemia, aneurisma)"
Cohesion: 0.07
Nodes (51): Abdomen agudo, Aneurisma de aorta abdominal, Angiografia, Ecografia abdominal, Isquemia mesenterica, Abdomen agudo clínico frente a quirúrgico, Angio-TC de aorta toracoabdominal, Choque hemorrágico por pérdida de volumen (+43 more)

### Community 2 - "Dolor abdominal y neoplasias GI"
Cohesion: 0.05
Nodes (47): Bates, Guia de Exploracion Fisica e Historia Clinica (Bickley, 2013), Cancer de boca, Cancer de colon, Cancer de duodeno, Cancer de esofago, Cancer de estomago, Cancer de higado, Caso Dolor abdominal agudo (+39 more)

### Community 3 - "Saturnismo y porfiria"
Cohesion: 0.08
Nodes (40): Laboratorio clinico, Porfiria, Saturnismo, Sindrome de Guillain-Barre, Banderas rojas del grupo (amenaza), Saturnismo, ALA alto con PBG normal (apunta a plomo), Cólico sin peritonismo (+32 more)

### Community 4 - "Vía biliar: coledocolitiasis y colangitis"
Cohesion: 0.08
Nodes (37): Cancer de pancreas, Cancer de vesicula y vias biliares, Colangitis, Coledocolitiasis, Altitud de Quito y cociente PaO2/FiO2, Amenaza: colangitis aguda no reconocida, Bandera roja: ictericia progresiva con colédoco dilatado, Bandera roja: peritonismo difuso (perforación) (+29 more)

### Community 5 - "Caso Hematuria y urinaria baja"
Cohesion: 0.07
Nodes (32): Bolenz et al. The investigation of hematuria (Dtsch Arztebl Int 2018), Bradley et al. Diet, fluid intake, caffeine, alcohol, tobacco and LUTS (J Urol 2017), Cancer de prostata, Cancer del tracto urinario, Caso Hematuria, Caso Patologia urinaria baja, Cistitis, Cistoscopia (+24 more)

### Community 6 - "Hipopotasemia con íleo"
Cohesion: 0.10
Nodes (32): Hipopotasemia con íleo paralítico, Abdomen blando sin peritonismo, Hiperpolarización de la membrana (Na+/K+-ATPasa), Hipomagnesemia: hipopotasemia refractaria, Potasio extracelular bajo, K+ urinario puntual (cociente K/creatinina), KCl IV central (hasta 20 mEq/h con ECG), KCl IV periférico (hasta 10 mEq/h, 40 mEq/L, NaCl 0,9 %) (+24 more)

### Community 7 - "Apendicitis aguda"
Cohesion: 0.15
Nodes (24): Apendicitis aguda, Puntaje AAS (Adult Appendicitis Score), Puntaje AIR (Appendicitis Inflammatory Response), Puntaje de Alvarado (excluye, no confirma), Antibióticos sin cirugía en no complicada sin apendicolito, Apendicectomía laparoscópica en menos de 24 h, Ceftriaxona más metronidazol, Apendicitis complicada (gangrena, perforación, flemón, absceso) (+16 more)

### Community 8 - "Colelitiasis y colecistitis"
Cohesion: 0.13
Nodes (23): Colelitiasis, Ceftriaxona más metronidazol IV, Colecistectomía laparoscópica precoz (grado I, 72 h), Colecistitis alitiásica, Drenaje vesicular si riesgo quirúrgico alto (CCI ≥4 o ASA ≥3), Colelitiasis y colecistitis aguda, Hioscina butilbromuro IV, Ketorolaco IV (+15 more)

### Community 9 - "Pancreatitis aguda y escalas"
Cohesion: 0.16
Nodes (23): Criterios de Ranson modificados, Marcadores bioquimicos, Pancreatitis aguda, Amenaza: pancreatitis con falla orgánica >48 h, APACHE II, Clasificación de Atlanta revisada 2012, BISAP, Colecistectomía en el mismo ingreso (biliar leve) (+15 more)

### Community 10 - "Caso Disbasia"
Cohesion: 0.10
Nodes (21): Alteraciones del pie (plano, cavo, equino, varo, valgo), Anteversion femoral, Artritis septica, Caso Disbasia, Disbasia, Dismetria de miembros inferiores, Displasia del desarrollo de la cadera, Enfermedad de Osgood-Schlatter (+13 more)

### Community 11 - "Caso Coma / TCE"
Cohesion: 0.11
Nodes (20): ATLS Student Course Manual 10th ed. (ACS 2018), Caso Coma / Traumatismo craneoencefalico, Coma, Coma estructural, Coma metabolico, Escala de Glasgow, Estudios toxicologicos, Hiperuricemia (+12 more)

### Community 12 - "Caso Ojo rojo"
Cohesion: 0.12
Nodes (18): Agudeza visual, Ambliopia (ojo vago), Blefaritis, Caso Ojo rojo, Celulitis orbitaria, Conjuntivitis (bacteriana, viral, alergica), Coroidoretinitis, DynaMed 2024: Red eye, conjuntivitis, Blepharitis, Amblyopia, Uveitis (+10 more)

### Community 13 - "Obstrucción intestinal"
Cohesion: 0.20
Nodes (16): Obstruccion intestinal, Obstrucción intestinal, Gas y líquido se acumulan antes del obstáculo, Reposición de cloruro de potasio, Dolor cólico intermitente con borborigmos, Contraste hidrosoluble con radiografía a las 24 h, Operar si peritonismo, estrangulación, isquemia o contraste no avanza, Estrangulación: isquemia, necrosis y perforación (+8 more)

### Community 14 - "Perforación de víscera hueca"
Cohesion: 0.22
Nodes (14): Perforacion de viscera hueca, Tomografia computarizada, Perforación de víscera hueca, Aire libre bajo el diafragma, Contaminación bacteriana causa sepsis, Pared rota: contenido sale al peritoneo, Peritonitis química por ácido y bilis, Reanimar, antibiótico amplio y reparación quirúrgica urgente (+6 more)

## Knowledge Gaps
- **179 isolated node(s):** `Participacion sesion de apertura (1 pt)`, `Participacion sesiones de monitoreo (2 pts)`, `Prueba de monitoreo (1 pt)`, `Prueba de cierre del docente consultor (1 pt)`, `Prueba final del caso clinico (3 pts)` (+174 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 179 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Caso Dolor abdominal agudo` connect `Dolor abdominal y neoplasias GI` to `Abdomen agudo vascular (isquemia, aneurisma)`, `Saturnismo y porfiria`, `Vía biliar: coledocolitiasis y colangitis`, `Hipopotasemia con íleo`, `Apendicitis aguda`, `Colelitiasis y colecistitis`, `Pancreatitis aguda y escalas`, `Caso Coma / TCE`, `Obstrucción intestinal`, `Perforación de víscera hueca`?**
  _High betweenness centrality (0.418) - this node is a cross-community bridge._
- **Why does `Salud Integral Hospitalaria 2 Quirurgica 2 (09-Q0989)` connect `Dolor abdominal y neoplasias GI` to `Kit v10`, `Caso Hematuria y urinaria baja`, `Caso Disbasia`, `Caso Coma / TCE`, `Caso Ojo rojo`?**
  _High betweenness centrality (0.310) - this node is a cross-community bridge._
- **Why does `Abdomen agudo quirúrgico (widget v10)` connect `Abdomen agudo vascular (isquemia, aneurisma)` to `Dolor abdominal y neoplasias GI`, `Vía biliar: coledocolitiasis y colangitis`, `Hipopotasemia con íleo`, `Apendicitis aguda`, `Obstrucción intestinal`, `Perforación de víscera hueca`?**
  _High betweenness centrality (0.245) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Caso Dolor abdominal agudo` (e.g. with `Caso Dolor abdominal y perdida de peso (neoplasias gastrointestinales)` and `Caso Patologias vasculares frecuentes`) actually correct?**
  _`Caso Dolor abdominal agudo` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Participacion sesion de apertura (1 pt)`, `Participacion sesiones de monitoreo (2 pts)`, `Prueba de monitoreo (1 pt)` to the rest of the system?**
  _179 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Kit v10` be split into smaller, more focused modules?**
  _Cohesion score 0.06274509803921569 - nodes in this community are weakly interconnected._
- **Should `Abdomen agudo vascular (isquemia, aneurisma)` be split into smaller, more focused modules?**
  _Cohesion score 0.06588235294117648 - nodes in this community are weakly interconnected._