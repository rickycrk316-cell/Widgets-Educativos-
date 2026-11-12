---
name: "apertura"
description: "Apertura del ABP en un solo widget HTML: términos desconocidos, problemas biopsicosociales y factores de riesgo con fisiopatología, jerarquización por morbimortalidad e hipótesis diagnósticas, con diagramas y simulador de recall (evoluciona definiciones v6)."
---

# Apertura del caso ABP · Widget interactivo (v1)

Evolución de la skill **definiciones v6** (`.claude/skills/definiciones/SKILL.md`; en el paquete: `references/definiciones_SKILL.md`). Conserva todo su contrato para las pestañas de términos (prerrequisitos morfofuncionales, fuente única, recall, Vancouver, anti-truncamiento) y añade los otros pasos de la sesión de apertura del ABP en el **mismo widget**. Donde esta skill no diga nada, manda definiciones v6.

## Entrada

- **Caso** (texto completo del caso o adjunto) — obligatorio. Si falta, pide el caso y detente.
- **Términos** (uno por línea) — obligatorio.
- **Tema / caso del sílabo** (p. ej. «Caso 6 — Síndrome confusional agudo y demencia», segunda rotación) — fija el alcance de las hipótesis y la bibliografía.
- **Contexto local** (opcional; por defecto Ecuador, MSP).

## TAREA

Ejecutar, sobre un caso real del estudiante, los cuatro pasos de la apertura del ABP en **un único widget HTML autocontenido**:

| Paso | Pestaña(s) | Pregunta que responde |
|---|---|---|
| 0 · Lectura del caso | `c0` Caso | ¿Qué dice el caso? Datos marcados por eje B/P/S/FR |
| 1 · Términos desconocidos | `t1`…`tN` (una por término) | ¿Qué significa cada término y por qué aparece en este caso? |
| 2 · Identificación de problemas | `pb` Problemas | ¿Qué está mal en este paciente, en qué esfera, y por qué mecanismo? |
| 3 · Jerarquización | `jq` Jerarquización | ¿Qué problema puede matarlo o dejarlo dependiente antes? |
| 4 · Hipótesis diagnósticas | `hx` Hipótesis | ¿Qué entidades explican los problemas jerarquizados? |
| Repaso | `tg` Repaso global | Recall mixto de todas las pestañas + Referencias |

El widget **abre** el caso: no lo cierra. Prohibido en todas las pestañas: plan terapéutico, posología recomendada, algoritmos de manejo, pronóstico numérico (eso es del cierre). Sí se permite **nombrar** qué dato faltante confirmaría o descartaría una hipótesis (necesidades de aprendizaje).

## JERARQUÍA DE PRECEDENCIA

1. **Veracidad.** Igual que definiciones v6. Toda cifra con cita `[n]` confirmada; definiciones y bloques con badge púrpura de fuente. Cero marcas: lo que no se confirme tras agotar las fuentes (`fuentes/protocolo_verificacion.md`) se elimina; no existe badge «Fuente por verificar» ni `[VERIFICAR EN FUENTE]`.
2. **Fidelidad al caso.** Ningún problema, dato ni hallazgo se inventa. Lo que el caso no dice (examen físico, laboratorio, fracción de eyección) se declara como **dato faltante**, nunca se supone. Las incongruencias del caso (p. ej. «una semana» frente a «dos semanas») se señalan en `.mini.am`.
3. **Regla de alcance** (abajo).
4. **Fuente única** de prerrequisitos y de fisiopatología: un mecanismo se desarrolla una vez; en el resto, remisión.
5. **Integridad de salida** (anti-truncamiento de v6).
6. Contratos de formato.

## REGLA DE ALCANCE

- **Términos (`t*`):** como v6 (qué es, qué lo distingue, cómo se reconoce). Excepción de apertura: cada término lleva además la card **«Por qué importa en este caso»**, que lo vincula a los problemas (`pid`) que toca. Para un fármaco: clase, mecanismo y el efecto o riesgo que lo hace relevante en este paciente; la dosis solo se cita **como dato del caso**, nunca como recomendación. Para un esquema (p. ej. vacunas), se permite la tabla «recomendado frente a lo que tiene el paciente» porque *es* la definición pedida.
- **Problemas (`pb`):** fisiopatología completa del problema en este paciente (es el núcleo didáctico); sin tratamiento.
- **Jerarquización (`jq`):** criterios explícitos y el orden; sin tratamiento.
- **Hipótesis (`hx`):** argumentos a favor y en contra con datos del caso, diferencial y datos faltantes que la confirmarían; sin tratamiento ni pronóstico numérico.

## PESTAÑA `c0` · CASO

1. `.hb` Idea rectora del caso (≤25 palabras): quién es y qué cambió.
2. `.card.caso` con el caso **transcrito fielmente** por bloques (filiación, hábitos, vacunas, motivo, enfermedad actual, antecedentes). Los datos que generan problemas se marcan con `<mark class="mk-b|mk-p|mk-s|mk-fr">`; la leyenda va arriba en `.ley` con los cuatro chips.
3. `.mini.am` con incongruencias o datos repetidos del caso.
4. Card «Datos que faltan»: lista de lo que la apertura necesita y el caso no da (examen físico, signos vitales, glucemia, sodio, EMO, FEVI…).
5. Sin simulador. Glosario de siglas al pie.

## PESTAÑAS DE TÉRMINO `t1`…`tN`

Orden interno de v6, con una card nueva entre «Ejemplo de anclaje» y «No confundir con»:

`Idea rectora → Prerrequisitos → Definición de referencia → Explicación Feynman → Ejemplo de anclaje (anclado en el paciente) → Por qué importa en este caso (.card.vin, ≤70 palabras, con chips pid) → Mecanismo mínimo (condicional) → No confundir con… → Simulador · Recall → Glosario`

Mazo: 4–6 tarjetas como v6, con ≥1 tarjeta que conecte el término con el caso.

## PESTAÑA `pb` · PROBLEMAS

Clasificación obligatoria en cuatro ejes, cada uno en su contenedor `.pbg` con su color:

| Eje | Código | Qué entra |
|---|---|---|
| Biológicos | `B1…` | Síntomas, síndromes, enfermedades, efectos de fármacos, alteraciones orgánicas |
| Psicológicos | `P1…` | Conducta, afecto, percepción, pensamiento, sueño como vivencia, duelo |
| Sociales | `S1…` | Red de apoyo, cuidador, vivienda, seguridad, escolaridad, economía, funcionalidad social |
| Factores de riesgo | `FR1…` | Predisponentes y precipitantes que sostienen las hipótesis (no son problemas a resolver, son argumentos) |

Cada problema es un acordeón `.acc` (abierto los del eje B, cerrados el resto) cuyo título lleva `<span class="pid">B1</span>` y el nombre del problema. Dentro, siempre:

1. `<p><b>Dato del caso.</b> …</p>` — cita literal o casi literal.
2. `<p><b>Fisiopatología.</b> …</p>` + `ol.tl` de 3–6 nodos (causa → mecanismo → consecuencia clínica en este paciente). En FR, el `.tl` explica **por qué** ese factor predispone o precipita.
3. `<p><b>Por qué importa.</b> …</p>` — consecuencia si no se reconoce, en una o dos frases.
4. Si el mecanismo ya se desarrolló en otro problema o en un prerrequisito: `.rem-line` en lugar de repetirlo.

Diagramas obligatorios en `pb`: (a) **mapa biopsicosocial** del paciente (`.dg` con nodos de los cuatro ejes convergiendo en el problema central) y (b) al menos un **diagrama fisiopatológico** del problema principal. Mazo 4–8 tarjetas.

## PESTAÑA `jq` · JERARQUIZACIÓN

1. `.hb` con el criterio: **mayor riesgo de morbimortalidad para el paciente**, desglosado en: amenaza vital inmediata, reversibilidad/tiempo-dependencia, riesgo de daño o dependencia funcional, impacto en la familia.
2. Tabla de criterios (`Problema · Amenaza vital · Tiempo-dependiente · Reversible · Riesgo de discapacidad`), con valores cualitativos (Alto/Medio/Bajo) en texto.
3. `ol.rank` con **todos** los problemas B, P y S exactamente una vez, del más grave al menos grave. Cada `li` lleva clase de gravedad `g1` (riesgo vital), `g2` (alto), `g3` (moderado), `g4` (bajo), su `pid`, nombre en `<b>`, badge de nivel y una justificación de ≤40 palabras. Los FR no se jerarquizan: se citan como argumento.
4. Diagrama `.dg` «escalera de gravedad» o embudo de agrupación (problemas que se agrupan en un mismo síndrome).
5. Mazo 4–6 tarjetas (por qué X va antes que Y).

## PESTAÑA `hx` · HIPÓTESIS

1. Diagrama integrador `.dg`: **predisponentes + precipitantes → síndrome → hipótesis** (modelo multifactorial).
2. Una `.card.hx` por hipótesis, ordenadas por probabilidad, cada una con: título, badge de probabilidad (Alta/Media/Baja, en texto), línea de problemas que explica (`pid`), tabla `A favor (dato del caso) · En contra o falta`, y `<p><b>Qué la confirmaría.</b>` (dato o criterio, sin plan).
3. Tabla de diagnóstico diferencial: `Hipótesis alternativa · Dato que la acerca · Dato que la aleja`.
4. Card «Necesidades de aprendizaje» con los contenidos del caso del sílabo que la apertura deja abiertos.
5. Mazo 4–8 tarjetas.

## DIAGRAMAS (sin imágenes)

Solo HTML/CSS del kit, para que refluyan en iPad y móvil (nada de `<img>`, `<svg>` con estilos en línea ni colores fijos):

```html
<figure class="dg">
<div class="dg-t">Título del diagrama</div>
<div class="dg-row">
  <div class="dg-col"><div class="dg-n b">Nodo biológico</div><div class="dg-n fr">Factor</div></div>
  <div class="dg-ar"><span class="dg-lab">precipita</span></div>
  <div class="dg-n ro">Problema central</div>
</div>
<figcaption class="mini">Cómo leerlo, en una frase.</figcaption>
</figure>
```

Variantes de nodo: `b` (coral), `p` (violeta), `s` (verde), `fr` (ámbar), `ac` (acento), `ro` (alarma). `.dg-ar` dibuja la flecha (horizontal en pantalla ancha, vertical en móvil); `.dg-lab` es opcional. Mínimo **4 diagramas** en el widget.

## RECALL

Motor único de v6 (`DECKS`, `TERMS`, `RC`, `rc_*`). `DECKS` tiene una clave por pestaña con simulador (`t1…tN`, `pb`, `jq`, `hx`) y `tg` es la unión exacta en ese orden. `TERMS` nombra cada clave.

## CONSTRUCCIÓN

- Tipo `apertura` en `kit/construir.py`: cabecera `kit/apertura_head.html` (def_head + clases de apertura). Diseño v11: los widgets nuevos usarán `kit/v11/apertura_head.html` (restilizada: estilo app, fuente del sistema, acento por tema) cuando exista; hasta entonces, la actual y validador `kit/validar_apertura.py` guiado por el manifiesto.
- Partes: `p01_nav` `p05_c0` `p10_t1`…`p90_t9` `p91_pb` `p92_jq` `p93_hx` `p95_tg` `p96_js`.
- `manifiesto.json`: `titulo`, `salida`, `tipo: "apertura"`, `terminos` (n), `problemas` (`{"B":n,"P":n,"S":n,"FR":n}`), `hipotesis` (n), `diagramas` (mínimo).
- Pruebas: `node kit/probar_definiciones.js <url> <capturas>` (recorre todas las pestañas y mazos).

## AUTOVERIFICACIÓN (añade a la de v6)

- [ ] ¿Cada problema tiene dato del caso, fisiopatología con `.tl` y «por qué importa»?
- [ ] ¿Ningún problema ni dato inventado; los faltantes declarados?
- [ ] ¿Los cuatro ejes tienen al menos un problema?
- [ ] ¿La jerarquía contiene todos los B, P y S una vez, con criterio explícito?
- [ ] ¿Cada hipótesis cita los `pid` que explica y tiene datos a favor y en contra del caso?
- [ ] ¿Cero tratamiento, posología recomendada o pronóstico numérico?
- [ ] ¿≥4 diagramas, legibles en móvil?
- [ ] ¿Validación programática en verde?
