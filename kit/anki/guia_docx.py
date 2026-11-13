#!/usr/bin/env python3
"""Genera la guía de estudio .docx de un mazo v7 desde su tarjetas.json (meta.guia + tarjetas).

Uso: python3 kit/anki/guia_docx.py mazos/<tema>/tarjetas.json [--salida ruta.docx]
Requiere python-docx (pip install python-docx).

La guía explica POR QUÉ funciona cada principio (con cita verificada), CUÁNDO estudiar (calendario
respecto a la tutoría ABP y al examen) y CÓMO usar el mazo (importar, configurar FSRS, leer el código
de colores, responder y calificar, sanguijuelas, mnemotecnia y esquema), más el mapa del mazo.
Las referencias de aprendizaje de REF_APRENDIZAJE se verificaron el 2026-11-12 (PubMed: PMID/DOI;
web: Clark & Paivio, Ye 2022, Wozniak, manual de Anki). Si añades una, verifícala antes.
"""
import argparse
import collections
import datetime as dt
import json
import math
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import modelo as M  # noqa: E402
from compilar_mazo import MARCAS  # noqa: E402

try:
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt, RGBColor
except ImportError:
    sys.exit('Falta python-docx. Instálalo con:  pip install python-docx')

REF_APRENDIZAJE = [
    'Roediger HL, Karpicke JD. Test-enhanced learning: taking memory tests improves long-term retention. Psychol Sci. 2006;17(3):249-55. doi:10.1111/j.1467-9280.2006.01693.x. PMID: 16507066.',
    'Larsen DP, Butler AC, Roediger HL. Test-enhanced learning in medical education. Med Educ. 2008;42(10):959-66. doi:10.1111/j.1365-2923.2008.03124.x. PMID: 18823514.',
    'Cepeda NJ, Pashler H, Vul E, Wixted JT, Rohrer D. Distributed practice in verbal recall tasks: a review and quantitative synthesis. Psychol Bull. 2006;132(3):354-80. doi:10.1037/0033-2909.132.3.354. PMID: 16719566.',
    'Dunlosky J, Rawson KA, Marsh EJ, Nathan MJ, Willingham DT. Improving students\' learning with effective learning techniques: promising directions from cognitive and educational psychology. Psychol Sci Public Interest. 2013;14(1):4-58. doi:10.1177/1529100612453266. PMID: 26173288.',
    'Ye J, Su J, Cao Y. A stochastic shortest path algorithm for optimizing spaced repetition scheduling. En: Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining. Nueva York: ACM; 2022. p. 4381-90. doi:10.1145/3534678.3539081.',
    'Brunmair M, Richter T. Similarity matters: a meta-analysis of interleaved learning and its moderators. Psychol Bull. 2019;145(11):1029-52. doi:10.1037/bul0000209. PMID: 31556629.',
    'Clark JM, Paivio A. Dual coding theory and education. Educ Psychol Rev. 1991;3:149-210. doi:10.1007/BF01320076.',
    'Soderstrom NC, Bjork RA. Learning versus performance: an integrative review. Perspect Psychol Sci. 2015;10(2):176-99. doi:10.1177/1745691615569000. PMID: 25910388.',
    'Wozniak P. Effective learning: twenty rules of formulating knowledge [Internet]. SuperMemo; 1999 [citado 2026 nov 12]. Disponible en: https://www.supermemo.com/en/archives1990-2015/articles/20rules',
    'Bertsch S, Pesta BJ, Wiscott R, McDaniel MA. The generation effect: a meta-analytic review. Mem Cognit. 2007;35(2):201-10. doi:10.3758/bf03193441. PMID: 17645161.',
    'Diekelmann S, Born J. The memory function of sleep. Nat Rev Neurosci. 2010;11(2):114-26. doi:10.1038/nrn2762. PMID: 20046194.',
    'Butterfield B, Metcalfe J. Errors committed with high confidence are hypercorrected. J Exp Psychol Learn Mem Cogn. 2001;27(6):1491-4. doi:10.1037//0278-7393.27.6.1491. PMID: 11713883.',
    'Pan SC, Rickard TC. Transfer of test-enhanced learning: meta-analytic review and synthesis. Psychol Bull. 2018;144(7):710-56. doi:10.1037/bul0000151. PMID: 29733621.',
    'Anki Manual [Internet]. Ankitects; [citado 2026 nov 12]. Secciones Deck Options (FSRS, Desired Retention), Studying y Leeches. Disponible en: https://docs.ankiweb.net',
]
# (principio, qué haces en este mazo, por qué fija la memoria con [A n])
PRINCIPIOS = [
    ('Recuerdo activo (efecto test)', 'Dices la respuesta antes de voltear la tarjeta.',
     'Recuperar un dato de memoria lo fortalece más que releerlo: a la semana, quien se evaluó recordó más que quien reestudió, aunque este se sentía más seguro [A1]. En educación médica el efecto se mantiene y crece con la retroalimentación [A2].'),
    ('Repetición espaciada', 'Repasas cada día lo que Anki programa, sin acumular.',
     'Repartir los repasos en el tiempo retiene más que concentrarlos, y el intervalo óptimo crece cuanto más lejos está el examen [A3]. La práctica distribuida y la de recuperación son las dos técnicas de mayor utilidad en la revisión de Dunlosky [A4].'),
    ('FSRS (planificador de Anki)', 'Activas FSRS con retención deseada 0,90.',
     'FSRS estima para cada tarjeta cuándo tu probabilidad de recordarla bajará a la retención deseada y la programa en ese momento; procede de la línea de modelos de memoria de Ye y cols. [A5]. El 90 % por defecto equilibra retención y carga; por encima la carga sube muy rápido [A14].'),
    ('Intercalado por contraste', 'Las tarjetas de contraste mezclan entidades confundibles.',
     'Mezclar categorías parecidas obliga a buscar el rasgo que las separa; el efecto es moderado (g = 0,42) y mayor cuando las categorías se parecen entre sí [A6].'),
    ('Elaboración', 'El razonamiento del reverso explica el porqué.',
     'Preguntarte por qué algo es cierto lo engancha a lo que ya sabes; la evidencia le da utilidad moderada [A4].'),
    ('Codificación dual', 'El color marca el tipo de dato y el esquema da una imagen.',
     'Lo guardado a la vez como palabras y como imagen tiene dos vías de recuperación [A7].'),
    ('Dificultades deseables', 'Aceptas que cueste: recordar, espaciar y mezclar.',
     'Lo que se siente fácil al estudiar (releer, mirar la respuesta) puede no dejar aprendizaje duradero, y lo que cuesta un poco sí [A8].'),
    ('Mínima información', 'Una idea por tarjeta y respuesta corta.',
     'Las tarjetas simples se recuerdan mejor y se califican con honestidad [A9].'),
    ('Generación', 'Escribes o dices tu respuesta completa antes de ver la del mazo.',
     'Producir la información la fija mejor que solo leerla (efecto medio ≈ 0,40 DE) [A10].'),
    ('Sueño', 'Estudias de día y duermes; no cambias sueño por tarjetas.',
     'El sueño consolida lo aprendido durante el día [A11].'),
    ('Calibración', 'Antes de voltear decides si estás seguro; en el cierre usas la hoja de confianza.',
     'Los errores cometidos con mucha confianza son los que más se corrigen tras ver la respuesta [A12]: la sorpresa se convierte en aprendizaje.'),
    ('Transferencia', 'Las tarjetas de aplicación y las viñetas piden decidir, no recitar.',
     'La práctica de recuperación se transfiere a preguntas de aplicación y a problemas de diagnóstico médico [A13].'),
]
LEYENDA = [  # clase, nombre, ejemplo
    ('fx', 'Fármaco', 'benzodiacepina'), ('num', 'Cifra, dosis o umbral', '≥ 2 de 11'),
    ('al', 'Signo de alarma', 'convulsión'), ('dx', 'Diagnóstico o entidad', 'delirium'),
    ('mec', 'Mecanismo', 'rebote GABA/NMDA'), ('mne', 'Mnemotecnia', 'CAGE'),
    ('vs', 'Contraste (A frente a B)', 'Contraste'), ('tema', 'Sujeto de la tarjeta', 'ABSTINENCIA'),
]
INDIGO = RGBColor(0x4F, 0x46, 0xC8)
GRIS = RGBColor(0x5F, 0x5F, 0x6C)


def var_css(nombre):
    m = re.search(r'--' + re.escape(nombre) + r':\s*#([0-9A-Fa-f]{6})', M.CSS)
    return m.group(1) if m else '16161D'


def sombrear(celda, hexcolor):
    tcPr = celda._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hexcolor)
    tcPr.append(shd)


def tabla(doc, cabecera, filas, anchos=None):
    t = doc.add_table(rows=1, cols=len(cabecera))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for c, h in zip(t.rows[0].cells, cabecera):
        c.text = ''
        r = c.paragraphs[0].add_run(h)
        r.bold = True
        r.font.size = Pt(9.5)
        sombrear(c, 'EEEEF5')
    for f in filas:
        cells = t.add_row().cells
        for c, v in zip(cells, f):
            c.text = ''
            r = c.paragraphs[0].add_run(str(v))
            r.font.size = Pt(9.5)
    if anchos:
        anchar(t, anchos)
    doc.add_paragraph()
    return t


def anchar(t, anchos):
    t.autofit = False
    for col, w in zip(t.columns, anchos):
        col.width = Cm(w)
    if True:
        for fila in t.rows:
            for c, w in zip(fila.cells, anchos):
                c.width = Cm(w)


def viñetas(doc, items, estilo='List Bullet'):
    for x in items:
        doc.add_paragraph(x, style=estilo)


def plano(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h or '')).strip()


def fecha(s):
    try:
        return dt.date.fromisoformat(s) if s else None
    except ValueError:
        sys.exit(f'fecha inválida: {s} (usa AAAA-MM-DD)')


def calendario(N, fechas):
    """Filas (cuándo, qué, por qué) respecto a la tutoría ABP y al examen."""
    ap, ci, ex = (fecha(fechas.get(k)) for k in ('apertura', 'cierre', 'examen'))
    dias_reparto = 4
    nuevas = max(1, math.ceil(N / dias_reparto))
    f = lambda d, k=0: (d + dt.timedelta(days=k)).strftime('%a %d %b') if d else None  # noqa: E731
    filas = [
        (f(ap, -1) or 'Día −1', 'Priming de 10 min: lee las palabras clave, agrúpalas y escribe 2–3 hipótesis.',
         'Activa conocimiento previo antes de la tutoría.'),
        (f(ap) or 'Día 0 (apertura)', 'Tras la sesión ABP: dibuja tu mapa propio. Importa el mazo y estudia el primer lote (≤ 24 h).',
         'Recuerdo activo y generación sobre lo recién discutido.'),
        ((f(ap, 1) + ' – ' + f(ap, dias_reparto - 1)) if ap else f'Días 1–{dias_reparto - 1}',
         f'Nuevas/día ≈ {nuevas} (el mazo completo en {dias_reparto} días) + todos los repasos que toque.',
         'Espaciado: cada tarjeta vuelve antes de olvidarse.'),
        (f(ci) or 'Cierre ABP', 'Antes del cierre: recuerdo libre sin notas y hoja de confianza; reestudia lo de «alta confianza + error».',
         'Calibración e hipercorrección.'),
        ('Cada día', 'Repasos completos (40–60 min de presupuesto total). Nunca topes los repasos para «ponerte al día».',
         'FSRS solo funciona si ves las tarjetas el día que vencen.'),
    ]
    if ex:
        filas.append((f(ex, -7) + ' – ' + f(ex, -1), 'Semana del examen: sin nuevas de este caso; Estudio personalizado con tag:Principio y tag:Nivel::Aplicacion; mezcla casos.',
                      'Intercalado y transferencia; el sueño de esos días consolida.'))
        filas.append((f(ex), 'Examen. La noche anterior, duerme: no hagas maratón de tarjetas.', 'Sueño y consolidación.'))
    else:
        filas.append(('Semana previa al examen', 'Sin nuevas; Estudio personalizado con tag:Principio y tag:Nivel::Aplicacion; mezcla casos; duerme.',
                      'Intercalado, transferencia y sueño.'))
    return filas, nuevas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('json')
    ap.add_argument('--salida')
    a = ap.parse_args()
    ruta = pathlib.Path(a.json).resolve()
    datos = json.loads(ruta.read_text(encoding='utf-8'))
    meta, cards = datos['meta'], datos['tarjetas']
    g = meta.get('guia') or {}
    sospechoso = MARCAS.search(json.dumps(g, ensure_ascii=False))
    if sospechoso:
        sys.exit(f'meta.guia contiene una marca de verificación («{sospechoso.group(0)}»): cero marcas')
    N = len(cards)
    raiz = meta['tag_raiz']
    salida = pathlib.Path(a.salida) if a.salida else ruta.parent / (f'Guia_{raiz}' + ('_demo' if meta.get('demo') else '') + '.docx')

    doc = Document()
    sec = doc.sections[0]
    sec.left_margin = sec.right_margin = Cm(2)
    sec.top_margin = sec.bottom_margin = Cm(1.8)
    st = doc.styles['Normal']
    st.font.name = 'Calibri'
    st.font.size = Pt(10.5)
    for nivel, tam in ((1, 16), (2, 13), (3, 11)):
        h = doc.styles[f'Heading {nivel}']
        h.font.color.rgb = INDIGO
        h.font.size = Pt(tam)
    pie = sec.footer.paragraphs[0]
    pie.text = f'Guía de estudio · {meta["caso"]} · mazo v{meta["version"]} · {meta["fecha"]}'
    pie.runs[0].font.size = Pt(8)
    pie.runs[0].font.color.rgb = GRIS

    t = doc.add_paragraph()
    r = t.add_run(f'Guía de estudio · {meta["caso"]}')
    r.bold, r.font.size, r.font.color.rgb = True, Pt(22), INDIGO
    p = doc.add_paragraph()
    r = p.add_run(f'Salud Integral Hospitalaria 2 · {meta.get("rotacion", "")} rotación · mazo Anki v{meta["version"]} · '
                  f'{N} notas · {meta["fecha"]}')
    r.font.color.rgb = GRIS
    if meta.get('demo'):
        doc.add_paragraph('DEMO de herramientas: este documento no es material de estudio.').runs[0].bold = True
    doc.add_paragraph(f'Resultado de aprendizaje: {meta["resultado_aprendizaje"]}')

    doc.add_heading('En un minuto', 1)
    filas_cal, nuevas = calendario(N, g.get('fechas') or {})
    viñetas(doc, [
        'Antes de voltear: di la respuesta en voz alta (o escríbela) y decide si estás seguro.',
        'Califica con honestidad: «Otra vez» si fallaste la idea central; «Bien» en casi todo lo demás.',
        f'Haz ~{nuevas} nuevas al día tras la apertura y TODOS los repasos de cada día.',
        'El color dice qué tipo de dato es (leyenda abajo); el esquema y la mnemotecnia se miran después de responder.',
        'Duerme: el sueño consolida lo que estudiaste.',
    ])

    doc.add_heading('1. Por qué funciona', 1)
    doc.add_paragraph('Cada principio de este mazo tiene respaldo experimental. La columna derecha dice por qué fija la memoria; '
                      'las citas [A n] están al final.')
    tabla(doc, ['Principio', 'Qué haces', 'Por qué funciona'], PRINCIPIOS, anchos=[3.4, 4.4, 9.2])
    doc.add_paragraph('Límite honesto: las tarjetas construyen base y discriminación, pero no sustituyen resolver casos completos. '
                      'Las mnemotecnias de palabra clave tienen utilidad baja en general [A4]; por eso aquí solo se usan las '
                      'establecidas, para listas arbitrarias, y siempre expandidas.')

    doc.add_heading('2. Cuándo estudiar', 1)
    tabla(doc, ['Cuándo', 'Qué', 'Por qué'], filas_cal, anchos=[3.4, 8.6, 5.0])
    doc.add_paragraph(f'Carga esperada: {N} tarjetas nuevas generan del orden de {N * 5} repasos en las próximas semanas '
                      '(estimación práctica, no un dato experimental).')

    doc.add_heading('3. Cómo usar el mazo', 1)
    doc.add_heading('Importar', 2)
    viñetas(doc, [
        'iPad / iPhone (AnkiMobile): guarda el .apkg en Archivos, tócalo y elige Compartir → AnkiMobile. Sincroniza con AnkiWeb.',
        'Mac / PC (Anki de escritorio): Archivo → Importar y elige el .apkg; luego Sincronizar.',
        f'El mazo aparece como «{M.RAIZ_MAZO}::{meta["caso"]}». Reimportar una versión nueva actualiza las notas existentes '
        '(mismo ID) sin perder tu historial.',
    ])
    doc.add_heading('Configurar una vez (opciones del mazo)', 2)
    viñetas(doc, [
        'FSRS: activado. Retención deseada: 0,90 (si la carga pesa, baja a 0,85 antes de tocar otra cosa).',
        f'Nuevas/día: {nuevas} durante los días de reparto; luego 0 hasta el siguiente caso.',
        'Máximo de repasos/día: 9999. Topar repasos oculta tarjetas vencidas y desordena el calendario.',
        'Sanguijuelas: Anki marca y suspende una tarjeta tras 8 fallos (valor por defecto) [A14].',
        'Optimiza los parámetros de FSRS cuando acumules unos cientos de repasos.',
    ])
    doc.add_heading('Leer el código de colores', 2)
    doc.add_paragraph('El color significa siempre el mismo tipo de dato, en todos los mazos. Úsalo para reconocer qué te pide la tarjeta, '
                      'no para memorizar el color.')
    tl = doc.add_table(rows=1, cols=3)
    tl.style = 'Table Grid'
    for c, h in zip(tl.rows[0].cells, ['Así se ve', 'Tipo de dato', 'Clase']):
        c.text = ''
        c.paragraphs[0].add_run(h).bold = True
        sombrear(c, 'EEEEF5')
    for cls, nom, ej in LEYENDA:
        cells = tl.add_row().cells
        cells[0].text = ''
        run = cells[0].paragraphs[0].add_run(ej.upper() if cls == 'tema' else ej)
        run.bold = True
        if cls in ('vs', 'tema'):
            run.font.color.rgb = INDIGO
        else:
            run.font.color.rgb = RGBColor.from_string(var_css(cls))
            sombrear(cells[0], var_css(cls + '-b'))
        if cls == 'mne':
            run.italic = True
        cells[1].text = nom
        cells[2].text = f'.{cls}'
    anchar(tl, (4.5, 8.5, 3.0))
    doc.add_paragraph()
    doc.add_paragraph('La respuesta va en un recuadro con borde índigo; debajo, el razonamiento (por qué), y si existen, '
                      'los bloques Mnemotecnia (borde rosa) y Esquema (tabla o diagrama). En modo noche los colores se adaptan solos.')
    doc.add_heading('Responder y calificar', 2)
    viñetas(doc, [
        'Lee el sujeto (arriba, en mayúsculas) y la pregunta. Di la respuesta completa en voz alta antes de voltear: '
        'generar es lo que fija la memoria [A1][A10].',
        'Otra vez: no recordaste la idea central o te equivocaste en lo esencial (sé estricto: si en la guardia sería un error, es Otra vez).',
        'Difícil: correcta, pero con dudas o tardaste mucho. Úsalo poco.',
        'Bien: correcta con algo de esfuerzo. Debe ser tu botón más usado.',
        'Fácil: correcta e inmediata, sin esfuerzo. Excepcional.',
        'Si fallas con mucha seguridad, detente 10 segundos en el razonamiento: es el error que más vas a aprender [A12].',
    ])
    doc.add_heading('Mnemotecnia y esquema', 2)
    viñetas(doc, [
        'Mnemotecnia: primero intenta recordar sin ella; si fallas, repasa qué significa cada letra y vuelve a decir la respuesta.',
        'Esquema: después de responder, recórrelo con la vista y explícalo en una frase. Si es una tabla de contraste, '
        'tapa una columna y reconstrúyela.',
        'En el iPhone, si una tabla no cabe, deslízala hacia el lado.',
    ])
    doc.add_heading('Sanguijuelas y atrasos', 2)
    viñetas(doc, [
        'Sanguijuela (tarjeta suspendida por fallos repetidos): no la reactives sin más. Lee el razonamiento, ubícala en tu mapa '
        'y, si sigue fallando, reescríbela con tus palabras o elimínala si el dato es irrelevante.',
        'Si te atrasas: nuevas/día en 0, despeja los repasos por tramos y, con el atraso en cero, reactiva las nuevas.',
        f'Estudio personalizado útil: tag:Quirurgica2::{raiz} (todo el caso), tag:Principio (antes del examen), '
        'tag:Nivel::Aplicacion (razonamiento), tag:Clase::Contraste (diferenciales).',
    ])

    doc.add_heading('4. Mapa del mazo', 1)
    sub = collections.OrderedDict()
    for c in cards:
        s = next((x.split('::')[2] for x in c['tags'] if x.startswith('Quirurgica2::') and x.count('::') == 2), '—')
        d = sub.setdefault(s, collections.Counter())
        d['n'] += 1
        d[c['tipo']] += 1
        d['apl'] += 'Nivel::Aplicacion' in c['tags']
        d['mne'] += bool(c.get('mnemotecnia'))
        d['esq'] += bool(c.get('esquema'))
    rel = g.get('subtemas') or {}
    tabla(doc, ['Subtema', 'Tarjetas', 'QA / Cloze', 'Aplicación', 'Extras', 'Relación con el sílabo'],
          [(s, d['n'], f'{d["QA"]} / {d["Cloze"]}', f'{d["apl"]}', f'{d["mne"]} mnemo · {d["esq"]} esquema', rel.get(s, ''))
           for s, d in sub.items()], anchos=[3.0, 1.6, 1.9, 1.8, 3.0, 5.7])
    doc.add_paragraph(f'Total: {N} notas · alcance: {meta["fuente_alcance"]}.')
    if g.get('principios'):
        doc.add_heading('Esqueleto de tu mapa (complétalo a mano)', 2)
        doc.add_paragraph('Estas son las ideas organizadoras del caso. Dibuja tú las conexiones, ejemplos y excepciones: el mapa lo construyes tú.')
        viñetas(doc, g['principios'], 'List Number')

    doc.add_heading('5. Antes y después de la tutoría', 1)
    if g.get('palabras_clave'):
        doc.add_heading('Priming (5–10 min)', 2)
        doc.add_paragraph('Palabras clave: ' + ' · '.join(g['palabras_clave']) + '. Agrúpalas y escribe 2–3 hipótesis de cómo se conectan.')
    if g.get('imagenes_oclusion'):
        doc.add_heading('Imágenes para oclusión (créalas tú en el iPad)', 2)
        viñetas(doc, g['imagenes_oclusion'])
    if g.get('preguntas_cierre'):
        doc.add_heading('Cierre: recuerdo libre y hoja de confianza', 2)
        doc.add_paragraph('Responde sin notas. Marca tu confianza ANTES de comprobar. Alta confianza + error = prioridad de reestudio.')
        tabla(doc, ['Pregunta', 'Confianza (alta/baja)', 'Resultado'], [(q, '', '') for q in g['preguntas_cierre']],
              anchos=[10.0, 3.5, 3.5])

    doc.add_heading('Referencias', 1)
    doc.add_heading('Aprendizaje', 2)
    for k, ref in enumerate(REF_APRENDIZAJE, 1):
        doc.add_paragraph(f'[A{k}] {ref}').runs[0].font.size = Pt(9)
    if g.get('referencias'):
        doc.add_heading('Contenido del caso', 2)
        for k, ref in enumerate(g['referencias'], 1):
            doc.add_paragraph(f'{k}. {ref}').runs[0].font.size = Pt(9)
    for par in doc.paragraphs:
        par.paragraph_format.space_after = Pt(3)
    doc.save(salida)
    print(f'guía: {salida}')


if __name__ == '__main__':
    main()
