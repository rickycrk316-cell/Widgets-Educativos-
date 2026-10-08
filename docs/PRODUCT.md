# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS/JS, single self-contained file per widget, assembled from a fixed kit (`kit_head.html` + parts + `kit_script.html`) and checked by `validar.py` (skill `widget-ensenanza` v10). No framework, no build step.

## Users

Ricardo, medical student in 10.º nivel at PUCE (Quito), on the surgical rotation (Quirúrgica 2), and the students of his ABP group. They study each clinical case before and between ABP sessions (apertura, monitoreo, cierre) and for the Examen Integral. Primary device: iPad, often held in portrait; also laptop. Sessions are long reading-and-recall blocks, frequently at night (inferred from the study context, not confirmed).

## Product Purpose

Turn one syllabus case into a single study widget that teaches a clinical presentation end to end (definition, mechanism, signs, diagnosis, treatment, follow-up) and makes the student retrieve it: guiding questions, blank timeline reconstruction, blank comparison table, clinical-decision simulators. Success = the student can name the entity, explain its mechanism and state the initial conduct for the Examen Integral without the widget open. Spaced repetition lives in Anki, not here.

## Positioning

A case widget is built from the course syllabus and current international guidelines with every figure cited (Vancouver) or explicitly flagged `[VERIFICAR EN FUENTE]`, and every sign linked back to the mechanism step that produces it. A generic summary or textbook chapter cannot do the sign ↔ mechanism linkage, the blank-reconstruction modes, or the simulators with counterfactuals.

## Operating Context

ABP methodology (3 sessions per case), syllabus «Salud Integral Hospitalaria 2. Quirúrgica 2» (code 09-Q0989). Widgets are opened offline from the iPad Files app or as a private claude.ai artifact. Reference texts: Harrison 22e, Farreras-Rozman, guideline societies (WSES, TG18, ACG, ESVS…). Context: Ecuador (MSP, INEC), Quito at ~2 850 m.

## Capabilities and Constraints

- Fixed tab structure per mode (mono: `pan def fis cli dx tx seg`; multi: `pan vis e1…eN sin`), fixed class vocabulary, fixed JS (`show`, `ir`, `recon`, `tabla`…). Content parts may not add `<style>`, inline styles, remote resources, `localStorage` or `position:fixed`.
- Must work fully offline: no remote fonts, images or scripts. Any visual change happens only in the kit CSS and must keep every class name and behavior.
- Must read well in light and dark, at iPad portrait (≈768–834 px) and phone width.
- Nothing is saved between sessions (by design of the recall modes).

## Brand Commitments

None beyond the skill's semantic color roles (blue = guide/accent, amber = precision/alcance, red = alarma, green = perla/ok, violet = discrepancia, coral = Feynman, rose = remisión) which carry meaning across all widgets and must stay distinguishable.

## Evidence on Hand

Existing widgets in `widgets/` (14, validated; see README.md). Syllabus in `fuentes/`. No user research, no screenshots of real use. Do not invent usage data.

## Product Principles

1. Truth before polish: an unverified number is flagged, never smoothed over.
2. Retrieval over re-reading: every tab ends in something the student must produce.
3. Mechanism explains signs: every visible finding traces to a step.
4. One idea once: common ground lives in one place and is referenced, never repeated.

## Accessibility & Inclusion

Long reading sessions: body text ≥4.5:1 contrast in both themes, comfortable measure, 44 px touch targets (already required by the kit), respects `prefers-reduced-motion`.
