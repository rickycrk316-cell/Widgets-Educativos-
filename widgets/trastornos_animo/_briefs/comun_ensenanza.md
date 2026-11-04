# Brief común · ejecutores del widget de enseñanza (sonnet)

Eres ejecutor del orquestador. Repo: /home/user/Widgets-Educativos- . Escribe SOLO tus archivos; no construyas, no hagas commit, no toques archivos de otros ejecutores ni el kit.

Lee, en este orden:
1. /root/.claude/skills/synced/a37b13fa-e893-4f31-8d1d-52bb3c262b77_a0e17d79-16f8-47b7-b024-0cd3aa89414b/widget-ensenanza/SKILL.md (reglas completas; §7, §9, §10, §11 son tu contrato de marcado y contenido).
2. widgets/trastornos_animo/PLAN.md (router, ejes, contrato de vis por entidad, conteos, citas, pistas del caso). Los conteos de PG, Feynman, nodos y signos de tu entidad son OBLIGATORIOS y exactos.
3. widgets/patologia_urinaria_baja/PLAN.md, solo la sección «Reglas de diseño para ejecutores».
4. Como plantilla de estructura (no de contenido): widgets/patologia_urinaria_baja/ensenanza/21_e1.html (entidad principal), 22_e2.html (secundaria), 05_vis.html, 80_sin.html y 90_sim.html (estilo de funciones dc). Imita exactamente su marcado (clases, ids, botones con type="button", estructura de h2, .qv, .signo, ol.tl, .dc). docs/DESIGN.md si dudas de una clase. NO leas kit/*.html ni kit/validar.py.
5. El caso: fuentes/casos/caso_crisis_angustia_trastornos_animo.md. Úsalo como ancla en ejemplos y simuladores sin afirmar el diagnóstico del paciente.

Reglas clave:
- Citas: SOLO claves [@CLAVE] de widgets/trastornos_animo/refs.json (p. ej. [@DSM], [@NICE_ANX]). Nunca números. Si necesitas una fuente que no está, no la inventes: marca el dato con [VERIFICAR EN FUENTE] y anótalo en pendientes. Toda celda Ref. lleva al menos una clave real.
- Ids de tu entidad eK: nodos eK-m-1…, signos eK-s-1…; xref: onclick="ir('eK','eK-m-3')" data-ir="eK-m-3".
- Simuladores: el HTML del .dc va en tu parte, con data-fn="<nombre del PLAN>". El JS de sus funciones va en widgets/trastornos_animo/ensenanza/_sim_<TU_LETRA>.js (solo funciones function dcX(dc){…}, sin <script>). Usa solo los helpers par(t), hv(a,v), vacio(dc,t), sel(dc,'g'), num(dc,'n'), out(dc,html), rd(x). Toda dosis del simulador debe figurar en la tabla de fármacos de su entidad. Sin probabilidades/VPP/LR. Salida acaba en <span class="cf">Si … → …</span>. Selección vacía → mensaje guía.
- Psiquiatría (SKILL §4): «Qué verás» = examen mental y exploración dirigida; los signos usan escalas o signos de la exploración mental con su mecanismo; la cadena es neurobiológica (o fisiopatológica coronaria en e5).
- Contexto Ecuador: primer nivel MSP, sin derivación posible (mhGAP), ECU 911; nota de altitud (Quito ~2 850 m) solo si cambia una conducta (p. ej. umbral de SatO₂ para oxígeno en e5).
- Sin web: no busques; la pasada de verificación la hace después un subagente. Dosis estándar de ficha técnica bien establecidas se citan a la clave correspondiente (XANAX_FT, NICE_ANX, NICE_DEP, WFSBP, ESC_SCA, ASHTON).
- Nada de '...' ASCII (usa …), emojis, style=, <style>, TODO, localStorage.

Entrega:
- Tus partes .html (escritas completas, sin truncar; si una parte es larga, escríbela en varias llamadas con append, cortando en límites estructurales).
- widgets/trastornos_animo/_pendientes_<TU_LETRA>.md: lista de datos marcados o dudosos (texto exacto · parte · tipo de fuente que lo respaldaría), máximo 8, priorizando cifras, umbrales y dosis.
- Respuesta final (breve, ≤25 líneas): archivos escritos; por entidad, los ítems de núcleo (≤7, texto LITERAL del widget: data-paso de nodos clin=1, celda k, pasos 1.º y De elección); conteos reales (PG, Feynman, nodos, signos, simuladores); claves de refs usadas.
