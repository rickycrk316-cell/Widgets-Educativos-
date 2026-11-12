# Sincronización del celo y poliovulación — plan del orquestador (prueba veterinaria)

Widget de prueba de la skill `widget-ensenanza` v10.1 fuera de medicina humana: MVET3230 Tecnología y Reproducción Animal (UDLA, período 202710), Unidad 5 «Sincronización del estro» (5.1–5.4) y 8.4 «Producción y transferencia de embriones» (superovulación). Rama aparte: no toca los widgets de Quirúrgica 2.

Fuentes (prioridad): 1) presentación de clase «Sincronización de celos y poliovulación» (protocolos, días, horas, dosis de FSH); 2) sílabo MVET3230 y su bibliografía (Frandson 9.ª ed. 2025; Carrasco y Breen 2023); 3) revisiones de referencia (Pursley 1995, Moreira 2001, Wiltbank y Pursley 2014, Bó y Baruselli 2014, Bó y Mapletoft 2014, Adams 2008, Abecia 2012, Knox 2015) y fichas técnicas para dosis.

## Router

`Modo: multi · Entidades: e1=PGF2α (principal), e2=GnRH + PGF2α, e3=Progestágenos, e4=Poliovulación · Amenaza: e1 · Override: sí (adaptación veterinaria)`

- No hay enfermedades: las «entidades» son **estrategias hormonales** con mecanismo propio (qué evento del ciclo controlan) y manejo propio (protocolo). Las especies (bovino, equino, ovino, caprino, porcino) son filas dentro de cada estrategia, no entidades: así quedan 4 entidades con una presentación común («hay que llevar un grupo de hembras a celo u ovulación en una ventana corta»).
- Principal = PGF2α: la herramienta más usada y la base de todas las demás. Amenaza = PGF2α: aplicada a una hembra gestante provoca aborto (pérdida irreversible evitable con un diagnóstico de gestación previo).
- Eje del grupo: de controlar un evento (luteólisis) → dos eventos (onda folicular + luteólisis + ovulación) → sustituir el CL (progestágeno) → multiplicar la ovulación (poliovulación).
- Etiquetas fijas del validador reinterpretadas (declarado en `vis` con `hb am` «Alcance»): «Qué verás» = respuesta observable; «Diagnóstico» = selección y verificación de hembras; «Tratamiento» = protocolos y dosis; «Epidemiología» = uso y categorías de hembra.
- Petición de la alumna: aprende con esquemas → cada pestaña lleva ≥4 SVG en línea (líneas de tiempo de protocolos, ovario, curvas hormonales, flujos) con un color fijo por hormona.

## Migración a v11

- Kit `kit/v11/` traído de las ramas v11 (`claude/youthful-noether-fsuqnj`, idéntico a `claude/happy-mendel-ylorra`); manifiesto con `"tipo": "v11"` y `"tema": "veterinaria"` (sin acento propio: azul).
- Ajuste mínimo del kit para veterinaria: etiqueta de perla `udla` (UDLA, sílabo MVET3230) añadida a `kit/v11/script.html` y `kit/v11/validar.py`, porque las etiquetas de examen v11 (PUCE, CACES, USMLE, MIR, ENARM) son de medicina humana.
- Filas de `vis` como preguntas adaptadas a estrategias hormonales; núcleo por pestaña; perlas `udla`; `data-paso` en los pasos para «Ordenar»; columna «Mecanismo de acción» en las tablas de fármacos; cero `[VERIFICAR EN FUENTE]` (lo no confirmado se eliminó).
- Se mantienen los esquemas SVG (la alumna aprende visualmente), sin `url(` (las flechas son triángulos dibujados).
