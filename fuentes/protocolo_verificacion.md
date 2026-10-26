# Protocolo de verificación de fuentes (compartido por las skills definiciones, widget-ensenanza y flashcards)

Objetivo: que `[VERIFICAR EN FUENTE]` y «Fuente por verificar» queden solo para lo que de verdad no se pudo comprobar en la sesión, no para lo que no se buscó.

## 1 · Qué exige cita

| Dato | Exige | Basta con |
|---|---|---|
| Definición, criterio diagnóstico, clasificación | fuente rectora `[n]` | guía, consenso o manual (DSM, ICS, Roma…) |
| Cifra, umbral, punto de corte, dosis | `[n]` a una fuente leída en la sesión o a la ficha técnica | resumen de PubMed, guía o ficha técnica oficial |
| Anatomía, fisiología, farmacología básica normal | texto de referencia con edición de la tabla del § 4 | conocimiento sólido + libro de la tabla |
| Composición y presentación de un fármaco de marca | ficha técnica o registro sanitario | ARCSA (Ecuador), prospecto del fabricante, CIMA-AEMPS, EMA, DailyMed |

## 2 · Orden de búsqueda (de más a menos prioritario)

1. Adjuntos del mensaje.
2. Sílabo y su bibliografía: `fuentes/syllabus_*.md` en el repo, o `references/syllabus_*.md` dentro de la skill. Si la bibliografía del sílabo trae una edición, usa **esa** (p. ej. Harrison 22e 2025, Farreras-Rozman 22.ª ed. 2024).
3. Guía internacional vigente del área; GPC del MSP del Ecuador cuando exista.
4. Bibliografía de la tabla del § 4.
5. Fármacos de marca: ARCSA → ficha del fabricante → CIMA-AEMPS / EMA / DailyMed.

## 3 · Pasada de verificación (obligatoria antes de marcar)

1. Mientras redactas, no te detengas a buscar cada dato. Marca provisionalmente con `[VERIFICAR EN FUENTE]` y anota el dato en una lista `pendientes` (texto exacto, pestaña o tarjeta, tipo de fuente que lo respaldaría).
2. Al terminar el borrador, una **sola pasada** de verificación sobre `pendientes`. Si hay subagentes, delega la pasada a uno ligero (modelo `haiku`). Si no, hazla tú. Herramientas, en este orden y según estén disponibles:
   - PubMed (`search_articles`, `lookup_article_by_citation`, `get_article_metadata`) para artículos, guías publicadas en revista y consensos. Devuelve PMID y DOI.
   - Consensus (`search`) para preguntas clínicas con evidencia de estudios.
   - WebSearch/WebFetch para guías de sociedades, ARCSA, fichas técnicas y catálogos editoriales.
3. Presupuesto: como máximo 2 búsquedas por dato y 20 datos por ejecución. Si hay más, prioriza cifras, umbrales y dosis.
4. Resultado por dato:
   - **Confirmado** → quita la marca y añade la referencia en Vancouver a la lista, con PMID/DOI si la herramienta los devolvió.
   - **Contradicho** → corrige el dato con la fuente encontrada.
   - **Sin confirmar** → deja la marca. Si el dato no es esencial, mejor elimínalo.
5. En la línea final de aviso, informa: «Verificados N de M datos; quedan K marcas: …».

## 4 · Ediciones de referencia (verificadas el 2026-10-26)

Usa estas ediciones sin badge ámbar. Si necesitas un libro que no está en la tabla, verifica su edición con una búsqueda (§ 3) antes de citarlo.

Citar una edición que existe es veraz aunque haya otra más nueva; prefiere la más reciente de la columna «Edición».

| Libro | Edición · año | Vancouver (inicio) | Confianza |
|---|---|---|---|
| Harrison's Principles of Internal Medicine | 22.ª · 2025 | Loscalzo J, Fauci AS, Kasper DL, Hauser SL, Longo DL, Jameson JL, editors. | alta |
| Farreras-Rozman. Medicina interna | 20.ª · 2024 | Rozman Borstnar C, Cardellach López F, editores. | alta · el sílabo de la 1.ª rotación dice «22.ª»: discrepancia del sílabo |
| Sabiston Textbook of Surgery | 22.ª · 2025 | Townsend CM Jr, Beauchamp RD, Evers BM, Mattox KL, editors. | alta (edición); verificar editores al citar |
| Schwartz's Principles of Surgery | 11.ª · 2019 | Brunicardi FC, editor. | media |
| Guyton and Hall Textbook of Medical Physiology | 14.ª · 2021 (existe 15.ª · 2026, sin confirmar) | Hall JE, Hall ME. | alta para la 14.ª |
| Moore. Clinically oriented anatomy | 9.ª · 2023 | Dalley AF II, Agur AMR. | alta |
| Langman's Medical Embryology | 15.ª · 2024 | Sadler TW. | alta |
| Robbins, Cotran & Kumar Pathologic Basis of Disease | 11.ª · 2025 | Kumar V, Abbas AK, Aster JC, editors. | alta |
| Kandel. Principles of neural science | 6.ª · 2021 | Kandel ER, Koester JD, Mack SH, Siegelbaum SA, editors. | alta |
| Goodman & Gilman's The Pharmacological Basis of Therapeutics | 14.ª · 2023 | Brunton LL, Knollmann BC, editors. | alta |
| Katzung. Basic & Clinical Pharmacology | 16.ª · 2024 | Vanderah TW, editor. | alta |
| Nelson Textbook of Pediatrics | 22.ª · 2025 | Kliegman RM, St Geme JW III, editors. | media (año 2024/2025) |
| Kaplan & Sadock's Synopsis of Psychiatry | 12.ª · 2022 | Boland R, Verduin ML, editors. | media |
| DSM-5-TR | 5.ª ed., texto revisado · 2022 | American Psychiatric Association. | alta |
| Campbell-Walsh-Wein Urology | 13.ª · 2025 | Partin AW, Dmochowski RR, Kavoussi LR, Peters CA, editors. | alta (edición); verificar editores al citar |
| Kanski's Clinical Ophthalmology | 10.ª · 2024 | Salmon JF. | alta |
| Snell's Clinical Neuroanatomy | 9.ª · 2025 | Splittgerber R. | media |
| Ross Histology: A Text and Atlas | 8.ª · 2020 | Pawlina W. | media |
| Fitzpatrick. Atlas de dermatología clínica (sílabo 2.ª rotación) | 9.ª · 2023 | Saavedra AP, Roh EK, Mikailov A, editores. | alta (sílabo) |
| Guzmán. Dermatología. Atlas, diagnóstico y tratamiento (sílabo) | 8.ª · 2024 | Guzmán R, editor. | alta (sílabo) |
| Kane. Principios de geriatría clínica (sílabo) | 8.ª · 2018 | Kane RL, Ouslander JG, Resnick B, Malone ML, editores. | alta (sílabo) |
| Ebert. Diagnóstico y tratamiento en psiquiatría (sílabo) | 4.ª · 2025 | Ebert MH, Martin PR, McVoy M, Ronis RJ, Weissman SH, editores. | alta (sílabo) |

Confianza «media»: cítalo, pero si la edición importa (cifras, criterios) confírmala con una búsqueda. Williams Obstetrics, Bates, Fitzpatrick (tratado) y Netter tienen edición o año contradictorios: verifícalos antes de usarlos.

## 5 · Lo que nunca se hace

- Inventar PMID, DOI, páginas, ediciones o años para «cerrar» una marca.
- Citar UpToDate o DynaMed con una fecha que no leíste; si se citan, la forma es `[Internet]` con `[citado AAAA mmm dd]` de la fecha de consulta real.
- Convertir un dato no confirmado en uno sin marca solo porque «suena bien».
