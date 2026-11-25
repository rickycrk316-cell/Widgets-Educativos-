# Elevación aguda de azoados — plan del orquestador

Fuente de alcance: sílabo de la 2.ª rotación, **Caso 1 — Elevación aguda y crónica de los azoados** (`fuentes/syllabus_quirurgica2_segunda_rotacion.md`): azotemia prerrenal, azotemia renal, necrosis tubular aguda, nefritis intersticial; prerrequisitos de fisiología renal y farmacología de IECA, calcioantagonistas y diuréticos.

Pedido del estudiante: widget de **lesión renal aguda (LRA)** que incluya nefritis intersticial y necrosis tubular aguda; tratamiento farmacológico centrado en el **mecanismo de acción** y no farmacológico centrado en la **alimentación**.

## Widget · Lesión renal aguda (widget-ensenanza v11, multi) — `lra/`

- Presentación común: **elevación aguda de azoados (creatinina y urea) o caída de la diuresis** (criterios KDIGO).
- `Modo: multi · Entidades: e1=Necrosis tubular aguda (principal), e2=Azotemia prerrenal, e3=Nefritis intersticial aguda, e4=LRA posrenal · Amenaza: e1 · Override: no`
- Principal = NTA: causa más frecuente de LRA establecida en el hospital (Liaño 1996) y la de conducta más decisiva (hiperpotasemia, sobrecarga, diálisis). Amenaza = NTA (oligúrica: hiperpotasemia y edema pulmonar).
- Eje del grupo (e2…e4): recorrido del flujo — antes del riñón (prerrenal) → intersticio renal (NIA) → después del riñón (posrenal).
- Lo común (criterios y estadios KDIGO, abordaje de complicaciones —hiperpotasemia, acidosis, sobrecarga—, ajuste de fármacos, **base de la alimentación en LRA**) va en `vis`; cada entidad desarrolla lo propio, incluida su alimentación específica.
- Alcance: la azotemia crónica (DM, HTA, glomerulonefritis) queda fuera (otro widget del caso); la glomerulonefritis rápidamente progresiva se nombra como vecina fuera del grupo.
- Guía rectora: KDIGO AKI 2012 (el borrador KDIGO AKI/AKD 2026 pasó revisión pública y no está publicado); nutrición: ESPEN 2021.
- Título: `Lesión renal aguda` · Salida: `Lesion_renal_aguda_widget_v11.html` · Acento `urologia`.
