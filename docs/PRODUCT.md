# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS/JS, single self-contained file per widget, assembled from a fixed kit (v11: `kit/v11/`; definitions and openings: `kit/`; v10.2 teaching widgets are frozen, their kit retired) plus parts, and checked by the kit validator (skill `widget-ensenanza` v11). No framework.

## Users

Ricardo, medical student in 10.º nivel at PUCE (Quito), on the surgical rotation (Quirúrgica 2), and the students of his ABP group. They study each clinical case before and between ABP sessions (apertura, monitoreo, cierre) and for the exams below. Primary device: iPad, often held in portrait; also laptop. Sessions are long reading-and-recall blocks, frequently at night (inferred from the study context, not confirmed).

## Product Purpose

Condense many sources into one study widget per topic, under the **20/80 rule**: the 20 % of information that makes the other 80 % understandable goes first (the `Núcleo` of each tab), then the specific data the exams ask for. Nothing is cut: it is reordered (core above, full detail below). Target exams: Examen Integral PUCE, habilitación CACES (Ecuador), USMLE Step 1 and 2 CK, MIR (Spain), ENARM (Mexico), plus the syllabus when the topic is in it (if not, current guidelines and exam outlines). Exam pearls are tagged by exam, with no claims about question frequency. Retrieval is active but light: ordering the steps of a pathophysiologic chain, a diagnostic algorithm or a treatment escalation, and clinical-decision simulators. Multiple-choice practice and spaced repetition live in Anki, not here. Success = the student can name the entity, explain its mechanism and state the initial conduct without the widget open.

## Positioning

A widget is built from current international guidelines, Ecuadorian MSP guidelines and the syllabus, with every figure cited (Vancouver) and **zero verification marks**: what cannot be confirmed after exhausting PubMed, Consensus, drug labels, MSP guidelines and the web is removed (`fuentes/protocolo_verificacion.md`). Every sign is linked to the mechanism step that produces it. A generic summary cannot do the sign-mechanism linkage, the exam-tagged pearls or the simulators with counterfactuals.

## Operating Context

ABP methodology (3 sessions per case), syllabus «Salud Integral Hospitalaria 2. Quirúrgica 2» (code 09-Q0989). Widgets are opened offline from the iPad Files app or as a private claude.ai artifact. Reference texts: Harrison 22e, Farreras-Rozman, guideline societies (WSES, TG18, ACG, ESVS…). Context: Ecuador (MSP, INEC), Quito at ~2 850 m.

## Capabilities and Constraints

- Fixed tab structure per mode (mono: `pan def fis cli dx tx seg`; multi: `pan vis e1…eN sin`), fixed class vocabulary (v11 contract: `docs/DECISIONES_v11.md` §10), fixed JS. Content parts may not add `<style>`, inline styles, remote resources, `localStorage` or `position:fixed`.
- Must work fully offline: no remote fonts, images or scripts. Any visual change happens only in the kit CSS (v11: system font, adaptive navigation, per-theme accent; see `docs/DESIGN.md`).
- Must read well in light and dark on iPhone (<760 px, bottom bar), iPad and Mac (≥760 px, side menu).
- Nothing is saved between sessions (by design of the recall modes).

## Brand Commitments

One accent color per theme (set in the manifest); red = alarm, amber = caution, green = correct. No marketing content and no other brands.

## Evidence on Hand

Existing widgets in `widgets/` (17 frozen v10.2 teaching widgets, not rebuilt until migrated; v11, definitions and opening widgets are live; see README.md). Syllabus in `fuentes/`. No user research, no screenshots of real use. Do not invent usage data.

## Product Principles

1. Truth before polish: an unconfirmed number is removed, never flagged and left in.
2. 20/80 first: core ideas above, full detail below; reorder, never cut.
3. Mechanism explains signs: every visible finding traces to a step.
4. One idea once: common ground lives in one place and is referenced, never repeated.

## Accessibility & Inclusion

Long reading sessions: body text ≥4.5:1 contrast in both themes, comfortable measure, 44 px touch targets (already required by the kit), respects `prefers-reduced-motion`.
