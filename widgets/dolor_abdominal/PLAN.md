# Dolor abdominal agudo — plan de orquestación (widget-ensenanza v10)

Fuente: `fuentes/Syllabus_primera_rotacion_10mo.md` · caso «Dolor abdominal agudo» (Quirúrgica 2, PUCE, 10.º nivel).

El caso nombra ~12 entidades. La skill v10 admite máximo 5 por widget, así que se parte en **3 widgets multi**. El router (§2) lo fija el orquestador para que los tres sean coherentes entre sí; cada ejecutor lo copia literal en su manifiesto.

## Widget A · Abdomen agudo quirúrgico — `quirurgico/`

- Presentación común: dolor abdominal agudo con sospecha de causa quirúrgica (peritonismo, obstrucción o dolor desproporcionado).
- `Modo: multi · Entidades: e1=Apendicitis aguda (principal), e2=Obstrucción intestinal, e3=Perforación de víscera hueca, e4=Isquemia mesentérica aguda, e5=Aneurisma de aorta abdominal roto · Amenaza: e5 · Override: sí`
- Eje declarado: de inflamatoria localizada → mecánica → perforativa → vascular (benigna → grave).
- Subtipos: obstrucción alta/baja y por bridas, hernia o tumor (en e2); perforación gástrica/duodenal e intestinal (en e3); isquemia embólica, trombótica, venosa y no oclusiva (en e4).
- `vis` además: definición de abdomen agudo y diferencia clínico vs quirúrgico (común al grupo), signos peritoneales y criterios de gravedad, remisión a los widgets B y C.
- Slug de entrega: `Abdomen_agudo_quirurgico_widget_v10.html`

## Widget B · Dolor biliopancreático — `biliopancreatico/`

- Presentación común: dolor en hipocondrio derecho o epigastrio de origen biliar o pancreático.
- `Modo: multi · Entidades: e1=Colelitiasis y colecistitis aguda (principal), e2=Coledocolitiasis, e3=Colangitis aguda, e4=Pancreatitis aguda · Amenaza: e3 · Override: sí`
- e1 cubre colelitiasis asintomática → cólico biliar → colecistitis aguda como espectro de un mismo proceso (subtipos/estadios en su tabla).
- Eje declarado: proximal → distal en la vía biliopancreática y de menor a mayor gravedad sistémica.
- e4: incluir criterios de Ranson modificados (sílabo) y compararlos con otras escalas (BISAP, Atlanta revisada, APACHE II) en la tabla de pruebas o pronóstico.
- Slug de entrega: `Dolor_biliopancreatico_widget_v10.html`

## Widget C · Abdomen agudo médico — `medico/`

- Presentación común: dolor abdominal intenso sin causa quirúrgica demostrable (abdomen «blando» o desproporcionado a la exploración), con riesgo de laparotomía innecesaria.
- `Modo: multi · Entidades: e1=Hipopotasemia con íleo paralítico (principal), e2=Saturnismo, e3=Porfiria aguda intermitente · Amenaza: e3 · Override: sí`
- El sílabo dice «hipocalemia»: el término correcto en español es hipopotasemia (hipocalemia se acepta como sinónimo). Si se considera impreciso, `hb am` «Precisión sobre el sílabo».
- El sílabo lista la pancreatitis como etiología médica: se desarrolla en el widget B; aquí solo se remite en `vis`.
- Eje declarado: metabólica frecuente → tóxica → genética rara con riesgo neurológico.
- Slug de entrega: `Abdomen_agudo_medico_widget_v10.html`

## Reglas comunes a los tres ejecutores

- Contexto: Ecuador (MSP, GPC, INEC; Quito ~2 850 m), solo con datos sostenibles.
- Bibliografía por defecto: Harrison 22e, Farreras-Rozman (última edición verificable; el sílabo cita «22a. ed. 2024»: verificar y, si es error, registrarlo como discrepancia propuesta, no como `hb vi` en `pan`/`sin`), y la guía internacional vigente más específica de cada entidad.
- Kit ya extraído en `<widget>/w/` (`kit_head.html`, `kit_script.html`, `validar.py`): no leer ni editar el documento del kit.
- Entrega en `widgets/dolor_abdominal/<slug>` + `manifiesto.json` dentro de `w/`.
