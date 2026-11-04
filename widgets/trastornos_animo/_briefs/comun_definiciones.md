# Brief común · ejecutores del widget de definiciones (sonnet)

Eres ejecutor del orquestador. Repo: /home/user/Widgets-Educativos- . Escribe SOLO tus archivos; no construyas, no hagas commit, no toques archivos de otros.

Lee, en este orden:
1. /root/.claude/skills/synced/a37b13fa-e893-4f31-8d1d-52bb3c262b77_a0e17d79-16f8-47b7-b024-0cd3aa89414b/definiciones/SKILL.md (contrato completo: orden interno de pestaña, plantillas A/B/C de prerrequisitos, regla de alcance, tarjetas, clases del kit, glifos).
2. widgets/trastornos_animo/PLAN.md: sección «Widget B · Definiciones» (tabla de prerrequisitos canónicos y remisiones = fuente única OBLIGATORIA; no desarrolles un prerrequisito asignado a otra pestaña: usa la remisión «↪ Prerrequisito ya desarrollado en «[término]»: [prerrequisito].» + ≤20 palabras) y «Citas».
3. Plantilla de estructura (no de contenido): widgets/patologia_urinaria_baja/definiciones/p10_t1.html (pestaña con prerrequisitos y remisión) y p70_t7.html (fármaco de marca), y las primeras 60 líneas de p96_js.html (formato de mazo {q,a,h}). docs/DESIGN.md si dudas de una clase. NO leas kit/*.html.
4. El caso: fuentes/casos/caso_crisis_angustia_trastornos_animo.md. Paso 1 del ABP: no resuelvas el caso ni afirmes el diagnóstico del paciente; sin tratamiento, dosis, epidemiología, S/E.

Reglas clave:
- Cada pestaña: <section class="tab" id="tK"> (solo t1 lleva además class active), h2 con el término, y el orden interno de la skill hasta el simulador <div class="rc" id="rc-tK">…</div> (copia el marcado vacío del rc de la plantilla, cambiando la clave y el título «Simulador · Recall de [término]») y el glosario .gloss/.mini al pie.
- Citas: SOLO claves [@CLAVE] de widgets/trastornos_animo/refs.json (nunca números), dentro de badges b-pu y texto. Libros de la tabla (Guyton, Kandel, Moore, G&G, Snell, DSM, Kaplan, Ebert, Harrison) se citan sin ámbar. Si algo no es atribuible, badge ámbar «Fuente por verificar» y anótalo en pendientes. No inventes fuentes.
- Mazos: 5 tarjetas por término (1–2 de prerrequisito estructura→función o función→signo; ≥1 de discriminación; resto definición y reconocimiento). Escribe widgets/trastornos_animo/definiciones/_decks_<TU_LETRA>.js con líneas del tipo:
  t1:[ {q:'…',a:'…',h:'…'}, … ],
  (comillas simples escapadas con \' si hace falta; una clave por término; sin const ni ;). Las tarjetas no llevan citas.
- Sin '...' ASCII (usa …), emojis, ✅⚠️❌, ↩, style=, <style>, clases inventadas, TODO.
- Sin web: la verificación la hace después otro subagente.

Entrega:
- Tus pNN_tK.html completos (sin truncar; usa varias llamadas si hace falta) y tu _decks_<TU_LETRA>.js.
- widgets/trastornos_animo/_pendientes_<TU_LETRA>.md (≤6 datos dudosos: texto · pestaña · fuente que lo respaldaría).
- Respuesta final breve (≤15 líneas): archivos, nº de prerrequisitos canónicos, remisiones y tarjetas por pestaña, claves de refs usadas.
