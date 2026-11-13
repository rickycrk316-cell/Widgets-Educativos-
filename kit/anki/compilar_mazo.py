#!/usr/bin/env python3
"""Valida (lint) y compila un mazo Anki v7 desde mazos/<tema>/tarjetas.json.

Uso:
  python3 kit/anki/compilar_mazo.py mazos/<tema>/tarjetas.json            # lint + .apkg + registro
  python3 kit/anki/compilar_mazo.py mazos/<tema>/tarjetas.json --solo-lint
  python3 kit/anki/compilar_mazo.py <scratchpad>/demo/tarjetas.json --demo   # sin cuotas ni registro

Requiere genanki para compilar (no para --solo-lint):  pip install genanki
Aborta (código 1, sin escribir nada) si hay cualquier error: marcas de verificación, `pendientes`
no vacío, HTML fuera de la lista blanca, cloze mal formado, IDs repetidos o fuera del registro, etc.
"""
import argparse
import collections
import json
import pathlib
import re
import sqlite3
import sys
import tempfile
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import modelo as M  # noqa: E402

RAIZ_REPO = pathlib.Path(__file__).resolve().parents[2]
REGISTRO = RAIZ_REPO / 'mazos' / 'README.md'

# Marcas prohibidas (decisión del dueño: cero marcas en campos, tags y metadatos de la guía).
# TODO/FIXME/XXX/VERIFICAR solo en mayúsculas («todo», «sobre todo» son español normal); «pendiente(s)» suelto
# es uso clínico legítimo: solo abortan sus formas de marca (y el campo `pendientes` no vacío, más abajo).
MARCAS = re.compile(r'\b(?:TODO|FIXME|XXX)\b|VERIFICAR|'
                    r'(?i:verificar\s+en\s+fuente|por\s+verificar|fuente\s+pendiente|'
                    r'pendientes?\s+de\s+verifica(?:r|ci[oó]n)|sin\s+confirmar|no\s+confirmad[oa]|'
                    r'\[\s*\?\s*\]|\?\?|\[\s*cita\s*\]|\[\s*ref\s*\]|\[\s*n\s*\])')
# Tarjetas que hablan de un widget, del mazo o de la propia fuente: prohibidas.
METATEXTO = re.compile(r'\bwidgets?\b|\best[ea]s?\s+(mazo|tarjeta)s?\b|\bla\s+fuente\s+(cita|dice|indica|menciona)\b|'
                       r'\bel\s+s[ií]labo\s+(dice|pide|cita)\b|\bseg[uú]n\s+(el|la)\s+(widget|tarjeta)\b', re.I)
LISTA_ABIERTA = re.compile(r'¿\s*(cu[aá]les\s+son|enumera|menciona|lista)\b', re.I)
OPERATIVOS = re.compile(r'\b(sensibilidad|especificidad|VPP|VPN|LR|AUC)\b[^.]{0,40}\d', re.I)
ID_RE = re.compile(r'(Q2|Q2R2|Q2X)-[A-Z]{2,5}-\d{4}')
TAG_RE = re.compile(r'[A-Za-z0-9:_\-]+')
NIVELES = {'Recuerdo', 'Aplicacion'}
CLASES = {'Principio', 'Aplicacion', 'Vineta', 'Contraste', 'Relacional', 'Irreducible', 'Escala'}
BLOOM = {'Recordar', 'Comprender', 'Aplicar', 'Analizar', 'Evaluar'}
META_OBLIG = ('caso', 'tag_raiz', 'prefijo', 'version', 'fecha', 'resultado_aprendizaje', 'fuente_alcance', 'verificacion')
CLAVES = {'QA': {'id', 'tipo', 'pregunta', 'respuesta', 'razonamiento', 'mnemotecnia', 'esquema', 'fuente', 'tags',
                 'pendientes', 'notas_ejecutor'},
          'Cloze': {'id', 'tipo', 'text', 'extra', 'mnemotecnia', 'esquema', 'fuente', 'tags', 'pendientes',
                    'notas_ejecutor'}}
OBLIG = {'QA': ('pregunta', 'respuesta', 'fuente'), 'Cloze': ('text', 'fuente')}


def texto_plano(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h or '')).strip()


# ---------------- Registro de IDs (mazos/README.md) ----------------
def leer_registro():
    if not REGISTRO.is_file():
        return None, [], {}
    txt = REGISTRO.read_text(encoding='utf-8')
    ret = re.search(r'<!--\s*retirados:\s*(.*?)\s*-->', txt)
    retirados = [x.strip() for x in ret.group(1).split(',')] if ret else []
    bloque = re.search(r'<!-- registro:inicio -->(.*?)<!-- registro:fin -->', txt, re.S)
    filas = {}
    if bloque:
        for ln in bloque.group(1).strip().splitlines()[2:]:
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            if len(c) == 8:
                filas[c[0]] = dict(zip(('prefijo', 'carpeta', 'tag_raiz', 'deck_id', 'ultimo', 'notas', 'version', 'fecha'), c))
    return txt, retirados, filas


def escribir_registro(txt, filas):
    cab = ('| Prefijo | Carpeta | Tag raíz | ID de mazo | Último ID | Notas | Versión | Fecha |\n'
           '|---|---|---|---|---|---|---|---|\n')
    cuerpo = ''.join(f'| {f["prefijo"]} | {f["carpeta"]} | {f["tag_raiz"]} | {f["deck_id"]} | {f["ultimo"]} | '
                     f'{f["notas"]} | {f["version"]} | {f["fecha"]} |\n' for f in filas.values())
    nuevo = re.sub(r'<!-- registro:inicio -->.*?<!-- registro:fin -->',
                   lambda _: '<!-- registro:inicio -->\n' + cab + cuerpo + '<!-- registro:fin -->', txt, flags=re.S)
    REGISTRO.write_text(nuevo, encoding='utf-8')


# ---------------- Lint ----------------
def lint(datos, base, demo):
    E, A = [], []          # errores, avisos
    meta = datos.get('meta') if isinstance(datos, dict) else None
    cards = datos.get('tarjetas') if isinstance(datos, dict) else None
    if not isinstance(meta, dict) or not isinstance(cards, list) or not cards:
        return ['el JSON debe ser {"meta": {...}, "tarjetas": [...]} con al menos una tarjeta'], A, {}
    for k in META_OBLIG:
        if not meta.get(k):
            E.append(f'meta.{k} vacío o ausente')
    if demo and not meta.get('demo'):
        E.append('--demo exige meta.demo = true')
    if not demo and meta.get('demo'):
        E.append('meta.demo = true: compílalo con --demo (y fuera de mazos/)')
    pref, raiz = meta.get('prefijo', ''), meta.get('tag_raiz', '')

    # Cero marcas también en los metadatos que van a la guía (salvo el informe de eliminados).
    def scan_meta(obj, ruta):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if ruta == 'meta' and k == 'verificacion':
                    continue
                scan_meta(v, f'{ruta}.{k}')
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                scan_meta(v, f'{ruta}[{i}]')
        elif isinstance(obj, str) and MARCAS.search(obj):
            E.append(f'{ruta}: marca de verificación «{MARCAS.search(obj).group(0)}» (cero marcas)')
    scan_meta(meta, 'meta')
    ver = meta.get('verificacion') or {}
    if not demo and not (isinstance(ver, dict) and isinstance(ver.get('total'), int) and isinstance(ver.get('verificados'), int)
                         and isinstance(ver.get('eliminados'), list)):
        E.append('meta.verificacion debe ser {"total": M, "verificados": N, "eliminados": [...]} (pasada de verificación)')

    ids, sub, info = [], collections.Counter(), {'imgs': set()}
    mir_ok = set(meta.get('mir_verificados') or [])
    for n, c in enumerate(cards):
        i = c.get('id', f'#{n}')
        t = c.get('tipo')
        if t not in CLAVES:
            E.append(f'{i}: tipo debe ser QA o Cloze')
            continue
        extra = set(c) - CLAVES[t]
        if extra:
            E.append(f'{i}: claves no permitidas para {t}: {", ".join(sorted(extra))}')
        for k in OBLIG[t]:
            if not texto_plano(c.get(k, '')) and not (k == 'text' and c.get(k)):
                E.append(f'{i}: campo {k} vacío')
        if not ID_RE.fullmatch(str(i)):
            E.append(f'{i}: ID inválido (<Q2|Q2R2|Q2X>-<ABREV>-<NNNN>)')
        elif i.rsplit('-', 1)[0] != pref:
            E.append(f'{i}: prefijo distinto de meta.prefijo ({pref})')
        ids.append(i)
        if c.get('pendientes'):
            E.append(f'{i}: `pendientes` no vacío — termina la verificación antes de compilar')

        # Campos: lista blanca, marcas semánticas, cero marcas, metatexto
        for k, _ in M.campos(c):
            v = c.get(k, '') or ''
            if not isinstance(v, str):
                E.append(f'{i}.{k}: debe ser texto')
                continue
            _, inf = M.sanear(k, v)
            E += [f'{i}.{k}: {e}' for e in inf['errores']]
            if k != 'esquema' and inf['marcas'] > M.LIMITE_MARCAS:
                E.append(f'{i}.{k}: {inf["marcas"]} marcas semánticas (máx. {M.LIMITE_MARCAS}: no saturar)')
            if inf['temas'] and k not in ('pregunta', 'text'):
                E.append(f'{i}.{k}: .tema solo va en el anverso (pregunta/text)')
            if MARCAS.search(v):
                E.append(f'{i}.{k}: marca de verificación «{MARCAS.search(v).group(0)}» (cero marcas)')
            if METATEXTO.search(texto_plano(v)):
                E.append(f'{i}.{k}: habla del widget/mazo/fuente («{METATEXTO.search(texto_plano(v)).group(0)}»): prohibido')
            if k != 'text' and re.search(r'\{\{c\d+::', v):
                E.append(f'{i}.{k}: sintaxis cloze fuera de Text')
            for src in inf['imgs']:
                info['imgs'].add(src)
                if not (base / 'media' / src).is_file():
                    E.append(f'{i}.{k}: media/{src} no existe junto al JSON')
        frente = c.get('pregunta' if t == 'QA' else 'text', '') or ''
        if not re.match(r'\s*<span class="tema">[^<]+</span>', frente):
            E.append(f'{i}: el anverso debe empezar por <span class="tema">Sujeto</span> (sujeto primero)')
        elif M.sanear('pregunta', frente)[1]['temas'] != 1:
            E.append(f'{i}: exactamente un .tema por anverso')
        cuerpo = ' '.join(texto_plano(c.get(k, '')) for k in ('pregunta', 'respuesta', 'razonamiento', 'text', 'extra'))
        if OPERATIVOS.search(cuerpo):
            E.append(f'{i}: cifra de S/E/VPP/VPN/LR/AUC (usa la afirmación cualitativa)')
        if t == 'QA':
            if len(re.findall(r'[.!?](\s|$)', texto_plano(c.get('respuesta', '')))) > 2:
                E.append(f'{i}: Respuesta >2 frases')
            if LISTA_ABIERTA.search(texto_plano(c.get('pregunta', ''))):
                E.append(f'{i}: lista abierta')
        else:
            E += [f'{i}: {e}' for e in lint_cloze(c.get('text', ''))]
        if c.get('mnemotecnia'):
            m = c['mnemotecnia']
            if m.count('<span class="mne">') != 1:
                E.append(f'{i}.mnemotecnia: lleva exactamente una <span class="mne"> con la mnemotecnia')
            if len(re.findall(r'<li>', m)) < 2 or '<ul>' not in m:
                E.append(f'{i}.mnemotecnia: expándela en <ul><li><b>L</b> significado</li>…</ul> (≥2 ítems)')
        if c.get('esquema'):
            E += [f'{i}.esquema: {e}' for e in lint_esquema(c['esquema'])]

        # Tags
        tags = c.get('tags') or []
        if not isinstance(tags, list) or not tags:
            E.append(f'{i}: tags ausentes')
            continue
        tg = lambda p: [x for x in tags if x.startswith(p)]  # noqa: E731
        for x in tags:
            if not isinstance(x, str) or not TAG_RE.fullmatch(x):
                E.append(f'{i}: tag inválido «{x}» (sin espacios ni tildes)')
            elif MARCAS.search(x):
                E.append(f'{i}: tag con marca de verificación «{x}»')
        for p in ('Quirurgica2::', 'Nivel::', 'Fuente::', 'Clase::', 'Bloom::'):
            if len(tg(p)) != 1:
                E.append(f'{i}: debe tener exactamente un tag {p}')
        q2 = tg('Quirurgica2::')
        if q2:
            partes = q2[0].split('::')
            if len(partes) != 3 or partes[1] != raiz:
                E.append(f'{i}: tag de tema debe ser Quirurgica2::{raiz}::<Subtema>')
            else:
                sub[partes[2]] += 1
        for p, ok in (('Nivel::', NIVELES), ('Clase::', CLASES), ('Bloom::', BLOOM)):
            if tg(p) and tg(p)[0][len(p):] not in ok:
                E.append(f'{i}: {tg(p)[0]} inválido')
        if 'Principio' in tags and 'Clase::Principio' not in tags:
            E.append(f'{i}: tag Principio solo con Clase::Principio')
        for x in tg('MIR::'):
            if x[5:] not in mir_ok:
                E.append(f'{i}: {x} sin verificación registrada en meta.mir_verificados')

    dup = [x for x, k in collections.Counter(ids).items() if k > 1]
    if dup:
        E.append('IDs (y por tanto GUID) duplicados: ' + ', '.join(dup))

    # Cuotas del mazo
    N = len(cards)
    n_cloze = sum(c.get('tipo') == 'Cloze' for c in cards)
    n_rec = sum('Nivel::Recuerdo' in (c.get('tags') or []) for c in cards)
    cuotas = []
    if N > 45 and not meta.get('justificacion_exceso'):
        cuotas.append(f'N={N} >45 sin meta.justificacion_exceso')
    if n_cloze / N > 0.15:
        cuotas.append(f'Cloze {n_cloze / N:.0%} >15%')
    if n_rec / N > 0.40:
        cuotas.append(f'Recuerdo {n_rec / N:.0%} >40%')
    if sub and max(sub.values()) > 8:
        cuotas.append(f'subtema con {max(sub.values())} tarjetas (>8)')
    if N < 25:
        A.append(f'N={N} <25: no rellenar')
    if demo:
        A += [f'(demo) {x}' for x in cuotas]
    else:
        E += cuotas
    info.update(N=N, n_cloze=n_cloze, n_rec=n_rec, sub=sub, ids=sorted(ids))
    return E, A, info


def lint_cloze(t):
    E = []
    if t.count('{{') != t.count('}}'):
        E.append('cloze: llaves {{ }} desbalanceadas')
    cl = list(M.CLOZE_RE.finditer(t))
    if not cl:
        return E + ['cloze: Text sin ningún {{c1::…}}']
    nums = sorted({int(m.group(1)) for m in cl})
    if nums != list(range(1, len(nums) + 1)):
        E.append(f'cloze: numeración {nums} (debe empezar en c1 y ser contigua)')
    for m in cl:
        cuerpo = m.group(2)
        if not texto_plano(cuerpo):
            E.append('cloze: hueco vacío')
        if '{{' in cuerpo:
            E.append('cloze: cloze anidado')
        abre, cierra = len(re.findall(r'<span\b', cuerpo)), cuerpo.count('</span>')
        if abre != cierra:
            E.append('cloze: <span> cruza el límite del hueco (la marca semántica va DENTRO del cloze)')
    if re.search(r'<span class="(?:' + '|'.join(M.SEMANTICAS) + r')">[^<]*\{\{c\d+::', t):
        E.append('cloze: marca semántica envolviendo el cloze; ponla dentro: {{c1::<span class="num">…</span>}}')
    return E


def lint_esquema(h):
    E = []
    for tabla in re.findall(r'<table>(.*?)</table>', h, re.S):
        filas = re.findall(r'<tr>(.*?)</tr>', tabla, re.S)
        cols = max((sum(int(x or 1) for x in re.findall(r'<t[hd](?:\s+[^>]*?colspan="(\d+)")?[^>]*>', f)) for f in filas), default=0)
        if cols > 4:
            E.append(f'tabla de {cols} columnas (máx. 4: debe leerse en iPhone)')
        if len(filas) > 9:
            E.append(f'tabla de {len(filas)} filas (máx. 9 incluida la cabecera)')
        if '<th' not in tabla:
            E.append('tabla sin cabecera <th>')
    if '<table' in h and not re.search(r'<table>', h):
        E.append('<table> no lleva atributos (el estilo viene de la plantilla)')
    return E


# ---------------- Compilación ----------------
def importar_genanki():
    try:
        import genanki
        return genanki
    except ImportError:
        sys.exit('Falta genanki. Instálalo con:  pip install genanki   (o --solo-lint para validar sin compilar)')


def compilar(datos, base, deck_id, salida):
    genanki = importar_genanki()
    meta = datos['meta']
    qa = genanki.Model(M.QA_ID, M.QA_NOMBRE, fields=[{'name': n} for _, n in M.CAMPOS_QA],
                       templates=[{'name': 'QA', 'qfmt': M.QFMT_QA, 'afmt': M.AFMT_QA}], css=M.CSS)
    cl = genanki.Model(M.CLOZE_ID, M.CLOZE_NOMBRE, fields=[{'name': n} for _, n in M.CAMPOS_CLOZE],
                       templates=[{'name': 'Cloze', 'qfmt': M.QFMT_CLOZE, 'afmt': M.AFMT_CLOZE}], css=M.CSS,
                       model_type=genanki.Model.CLOZE)
    nombre = f'{M.RAIZ_MAZO}::{meta["caso"]}' + (' (demo)' if meta.get('demo') else '')
    deck = genanki.Deck(deck_id, nombre)
    media = set()
    for c in datos['tarjetas']:
        vals = M.valores_saneados(c)
        for k, _ in M.campos(c):
            media |= set(M.sanear(k, c.get(k, ''))[1]['imgs'])
        deck.add_note(genanki.Note(model=qa if c['tipo'] == 'QA' else cl, fields=vals, tags=c['tags'],
                                   guid=genanki.guid_for(c['id']), sort_field=c['id']))
    pkg = genanki.Package(deck)
    pkg.media_files = [str(base / 'media' / m) for m in sorted(media)]
    pkg.write_to_file(str(salida))
    return nombre, sorted(media)


def inspeccionar(apkg):
    """Abre el .apkg (zip + sqlite) y devuelve modelos, campos, tamaño del CSS, nº de notas y media."""
    with zipfile.ZipFile(apkg) as z, tempfile.TemporaryDirectory() as td:
        nombres = z.namelist()
        db = next(n for n in ('collection.anki21', 'collection.anki2') if n in nombres)
        z.extract(db, td)
        media = json.loads(z.read('media').decode('utf-8')) if 'media' in nombres else {}
        con = sqlite3.connect(pathlib.Path(td) / db)
        models = json.loads(con.execute('select models from col').fetchone()[0])
        decks = json.loads(con.execute('select decks from col').fetchone()[0])
        n_notas = con.execute('select count(*) from notes').fetchone()[0]
        n_cards = con.execute('select count(*) from cards').fetchone()[0]
        con.close()
    mods = {int(k): (v['name'], [f['name'] for f in v['flds']], len(v['css']), v['type']) for k, v in models.items()}
    return mods, {int(k): v['name'] for k, v in decks.items()}, n_notas, n_cards, list(media.values())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('json')
    ap.add_argument('--solo-lint', action='store_true')
    ap.add_argument('--demo', action='store_true', help='cuotas del mazo como avisos; no usa ni toca el registro')
    ap.add_argument('--registro', help='registro de IDs (defecto: mazos/README.md del repo; fuera del repo, '
                                       'la copia de la carpeta de mazos del estudiante)')
    a = ap.parse_args()
    global REGISTRO
    if a.registro:
        REGISTRO = pathlib.Path(a.registro).resolve()
    ruta = pathlib.Path(a.json).resolve()
    base = ruta.parent
    try:
        datos = json.loads(ruta.read_text(encoding='utf-8'))
    except Exception as e:  # noqa: BLE001
        sys.exit(f'JSON ilegible: {e}')
    E, A, info = lint(datos, base, a.demo)

    # Registro
    meta = datos.get('meta', {}) if isinstance(datos, dict) else {}
    pref = meta.get('prefijo', '')
    dentro_mazos = REGISTRO.parent in ruta.parents
    txt, retirados, filas = leer_registro()
    deck_id = M.DECK_ID_DEMO
    if a.demo:
        if dentro_mazos:
            E.append('--demo no se usa dentro de mazos/: la demo va al scratchpad')
    else:
        if not dentro_mazos:
            E.append(f'un mazo real vive en {REGISTRO.parent}/<tema>/tarjetas.json')
        if txt is None:
            E.append(f'falta el registro de IDs {REGISTRO} (usa --registro fuera del repo)')
        elif pref in retirados:
            E.append(f'prefijo {pref} retirado en el registro: no se reutiliza')
        elif pref not in filas:
            E.append(f'prefijo {pref} no está en el registro mazos/README.md: añádelo con su ID de mazo antes de compilar')
        else:
            f = filas[pref]
            if f['tag_raiz'] != meta.get('tag_raiz'):
                E.append(f'tag raíz {meta.get("tag_raiz")} ≠ registro ({f["tag_raiz"]})')
            if f['carpeta'] not in ('—', '', base.name):
                E.append(f'el prefijo {pref} ya pertenece a la carpeta mazos/{f["carpeta"]}')
            if not f['deck_id'].isdigit():
                E.append(f'ID de mazo de {pref} sin asignar en el registro')
            else:
                deck_id = int(f['deck_id'])
            ult = f['ultimo']
            if ID_RE.fullmatch(ult) and info.get('ids'):
                nuevos = [x for x in info['ids'] if x > ult]
                esperados = [f'{pref}-{int(ult[-4:]) + k + 1:04d}' for k in range(len(nuevos))]
                if nuevos != esperados:
                    A.append(f'IDs nuevos {nuevos[:3]}… no continúan desde {ult} (huecos): revisa la numeración')

    if 'N' in info:
        print(f'N={info["N"]} | Cloze {info["n_cloze"] / info["N"]:.0%} | Recuerdo {info["n_rec"] / info["N"]:.0%} | '
              f'máx. subtema {max(info["sub"].values(), default=0)} | IDs {info["ids"][0]}–{info["ids"][-1]} | '
              f'media {len(info["imgs"])}')
    for x in A:
        print('AVISO:', x)
    if E:
        print('\n'.join('ERROR: ' + x for x in E))
        sys.exit(f'RESULTADO: LINT FALLIDO ({len(E)} errores) — no se escribe nada')
    print('RESULTADO: lint OK')
    if a.solo_lint:
        return

    salida = base / (f'Quirurgica2_{meta["tag_raiz"]}' + ('_demo' if a.demo else '') + '.apkg')
    nombre, media = compilar(datos, base, deck_id, salida)
    mods, decks, nn, nc, med = inspeccionar(salida)
    print(f'apkg: {salida}')
    print(f'  mazo {deck_id} «{nombre}» | notas {nn} | tarjetas {nc} | media {med}')
    for mid, (nm, fl, css, tp) in sorted(mods.items()):
        print(f'  modelo {mid} «{nm}» ({"cloze" if tp == 1 else "estándar"}) campos={fl} css={css} B')
    if nn != info['N'] or sorted(med) != media or {M.QA_ID, M.CLOZE_ID} - set(mods):
        sys.exit('RESULTADO: INSPECCIÓN DEL APKG FALLIDA')
    if not a.demo:
        f = filas[pref]
        previo = [f['ultimo']] if ID_RE.fullmatch(f['ultimo']) else []
        f.update(carpeta=base.name, ultimo=max(previo + info['ids']), notas=str(nn),
                 version=str(meta['version']), fecha=str(meta['fecha']))
        escribir_registro(txt, filas)
        print(f'registro actualizado: {pref} último ID {f["ultimo"]}, versión {meta["version"]}')
    print('RESULTADO: OK')


if __name__ == '__main__':
    main()
