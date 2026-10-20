# Lesiones elementales en dermatología — plan del orquestador

Tema fuera del sílabo, pedido por el estudiante para su rotación clínica hospitalaria. Sin caso problema: widgets genéricos de terminología. Bibliografía rectora pedida por el estudiante: **Bolognia, Dermatology 5e (2024)** y **Fitzpatrick's Dermatology 9e (2019)**; si la edición o el año no se sostienen, badge ámbar «Fuente por verificar» (no inventar edición, página ni ISBN).

Formato: **skill definiciones v5.1** (una pestaña por lesión + repaso global), porque el objetivo es reconocer y nombrar lesiones, no razonar un caso. Son ~36 términos: más de 15 obliga a partir (§Escala), así que van **4 widgets de 9 términos** (régimen normal, tope 5 prerrequisitos). Orden de estudio: A → B → C → D.

Reglas transversales de contenido:
- Cada lesión: definición (tamaño, relieve, contenido, profundidad), sustrato histológico mínimo (epidermis, unión dermoepidérmica, dermis, hipodermis) en prerrequisitos, cómo se explora (inspección, palpación, vitropresión/diascopia, luz tangencial) y 2–3 enfermedades prototipo como ejemplo de anclaje, sin tratamiento.
- **Umbrales de tamaño divergentes:** Bolognia usa 1 cm (mácula/mancha, pápula/placa, vesícula/ampolla); otras fuentes, incluida parte de la tradición Fitzpatrick, usan 0,5 cm. Nota `.mini` con la divergencia y cuál usa cada libro; nunca promediar. Si no hay certeza de la cifra de un libro, `[VERIFICAR EN FUENTE]`.
- Terminología en español de uso clínico en Ecuador, con el término inglés del libro entre paréntesis en la definición (p. ej. mancha (*patch*)).

## Widget A · Lesiones primarias sólidas — `primarias_solidas/`
Términos: 1 Mácula · 2 Mancha (*patch*) · 3 Pápula · 4 Placa · 5 Nódulo · 6 Tumor · 7 Habón (roncha) · 8 Quiste · 9 Comedón.
Archivo `Definiciones_lesiones_primarias_solidas.html` · título `Definiciones · Lesiones primarias sólidas`.

## Widget B · Lesiones de contenido líquido y vasculares — `liquidas_vasculares/`
Términos: 1 Vesícula · 2 Ampolla · 3 Pústula · 4 Absceso · 5 Púrpura (petequia y púrpura palpable) · 6 Equimosis · 7 Telangiectasia · 8 Surco acarino (*burrow*) · 9 Vitropresión (diascopia) y signo de Nikolsky — una pestaña con ambas maniobras de exploración.
Archivo `Definiciones_lesiones_liquidas_vasculares.html` · título `Definiciones · Lesiones líquidas y vasculares`.

## Widget C · Lesiones secundarias — `secundarias/`
Términos: 1 Escama · 2 Costra · 3 Erosión · 4 Úlcera · 5 Fisura · 6 Excoriación · 7 Liquenificación · 8 Atrofia · 9 Cicatriz (hipertrófica, queloide y esclerosis).
Archivo `Definiciones_lesiones_secundarias.html` · título `Definiciones · Lesiones secundarias`.

## Widget D · Descripción morfológica — `descripcion_morfologica/`
Términos: 1 Eritema y eritrodermia · 2 Configuración anular y arciforme · 3 Numular (discoide) · 4 Lesión en diana (iris) · 5 Disposición lineal (Koebner y líneas de Blaschko) · 6 Patrón reticulado · 7 Agrupación herpetiforme · 8 Distribución dermatómica (zosteriforme) · 9 Fotodistribución.
Archivo `Definiciones_descripcion_morfologica.html` · título `Definiciones · Descripción morfológica`. La pestaña 1 incluye cómo redactar una descripción completa (tipo de lesión → color → tamaño → forma/borde → configuración → distribución), como puente al uso en la ronda.

## Diseño
Igual que `widgets/patologia_urinaria_baja/PLAN.md`, Widget B: cabecera `kit/def_head.html` sin tocar, solo su vocabulario de clases, glifos sustituidos por texto («La sabía / A medias / No la sabía», «Fuente por verificar»), reglas de diseño 1–11 de ese PLAN. Modelo de partes: `widgets/patologia_urinaria_baja/definiciones/`.

## Pruebas finales del orquestador
`construir.py` + `auditar_definiciones.py <html> 9` + `probar_definiciones.js`. Sin más revisiones.
