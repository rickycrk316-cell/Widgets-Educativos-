# Ansiedad y pánico — plan del orquestador

Fuentes (prioridad en este orden):
1. **Caso** (texto del estudiante): `fuentes/casos/caso_ansiedad_panico.md`.
2. **Sílabo**, segunda rotación, caso 5 «Trastorno de ansiedad generalizada, ataque de pánico» (`fuentes/syllabus_quirurgica2_segunda_rotacion.md`): trabajo autónomo = concepto de ansiedad; fisiología neuroendocrina (serotonina, acetilcolina, GABA, MAO); benzodiacepinas e ISRS.
3. Guía o texto de referencia vigente: DSM-5-TR 2022 (ataque de pánico), AHA/ACC 2021 (dolor torácico), Cuarta definición universal del infarto 2018, EHRA (palpitaciones), Goodman & Gilman 14.ª ed. 2023, Guyton y Hall 14.ª ed. 2021, Kandel 6.ª ed. 2021, Moore 9.ª ed. 2023.

## Widget · Definiciones (skill definiciones v5.1) — `definiciones/`

- Caso/semana: Ansiedad y pánico (primera sesión). Consulta externa sin posibilidad de derivar.
- Términos, en este orden de pestañas (6 → régimen normal, tope 5 prerrequisitos):
  1. Opresión en el pecho (opresión precordial)
  2. Palpitaciones
  3. Angustia por perder el control mental
  4. Preinfarto — término coloquial, no diagnóstico: `.mini` ámbar con la interpretación (angina inestable / síndrome coronario agudo sin elevación del ST) y la alternativa (uso popular para cualquier dolor torácico «de corazón»)
  5. Stresstabs — producto comercial (multivitamínico del complejo B con vitamina C; composición según presentación): define qué es; badge «Fuente por verificar» para la composición; manejo al paso 7
  6. Xanax (alprazolam) — una pestaña con ambos nombres (marca y principio activo); qué es y su mecanismo; manejo al paso 7
  + pestaña final **Repaso global**.
- Alcance: paso 1 del ABP (qué es, qué lo distingue, cómo se reconoce). No se resuelve el caso: el widget no dice que sea un ataque de pánico ni que se haya descartado un síndrome coronario. Los ejemplos de anclaje pueden usar al paciente del caso.

### Manifiesto de prerrequisitos

| Pestaña / término | Prerrequisitos canónicos (tipo) | Remisiones | Tarjetas |
|---|---|---|---|
| t1 Opresión en el pecho | Inervación sensitiva del corazón y dolor visceral referido (C) · Balance entre aporte y demanda de oxígeno del miocardio (C) | — | 5 |
| t2 Palpitaciones | Sistema de excitación y conducción del corazón (B) · Respuesta simpaticoadrenal de lucha o huida (C) | — | 5 |
| t3 Angustia por perder el control mental | Circuito del miedo: amígdala, corteza prefrontal, hipocampo, hipotálamo, locus coeruleus (B) · Ventilación y CO₂: hiperventilación y alcalosis respiratoria (C) | respuesta simpaticoadrenal (t2) | 6 |
| t4 Preinfarto | Arterias coronarias (A) · Complejo de troponinas del sarcómero cardiaco (A) + mecanismo mínimo (placa inestable → trombo → isquemia) | balance de oxígeno del miocardio (t1) | 6 |
| t5 Stresstabs | Vitaminas hidrosolubles como cofactores del metabolismo (B) | — | 5 |
| t6 Xanax (alprazolam) | Receptor GABA-A y la inhibición sináptica (A) · Vida media de eliminación y estado estacionario (C) | circuito del miedo (t3) | 6 |

Totales: 11 prerrequisitos canónicos · 3 remisiones · 33 tarjetas.

### Referencias (numeración fija por primera aparición)

| [n] | Fuente | Dónde aparece primero |
|---|---|---|
| 1 | Guyton y Hall 2021 | t1 prerrequisitos (también t2, t3, t4, t5) |
| 2 | AHA/ACC 2021, dolor torácico (Gulati) | t1 definición |
| 3 | EHRA, palpitaciones (Raviele 2011) | t2 definición |
| 4 | Kandel 2021 | t3 prerrequisitos |
| 5 | DSM-5-TR 2022 | t3 definición |
| 6 | Moore 2023 | t4 prerrequisitos |
| 7 | Cuarta definición universal del infarto (Thygesen 2018) | t4 definición |
| 8 | Consenso internacional de Takotsubo (Ghadri 2018) | t4 «No confundir con» |
| 9 | Goodman & Gilman 2023 | t6 prerrequisitos y definición |

Stresstabs: definición con «Fuente por verificar» (ficha técnica no consultada).

- Diseño: igual que `patologia_urinaria_baja/PLAN.md` § Widget B (cabecera `kit/def_head.html`, solo sus clases, glifos sin ✅ ⚠️ ❌, remisión con ↪) y sus reglas de diseño 1–10.
- Validación: `python3 kit/construir.py widgets/ansiedad_panico/definiciones` + `auditar_definiciones.py <html> 6` + `probar_definiciones.js`.
- Archivo: `Definiciones_ansiedad_panico.html`.
