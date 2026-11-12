#!/usr/bin/env python3
"""Validador del widget de apertura (skill apertura v1), guiado por el manifiesto.
Uso: python3 validar_apertura.py widget.html manifiesto.json
Manifiesto: terminos (n), problemas {"B":n,"P":n,"S":n,"FR":n}, hipotesis (n), diagramas (mínimo)."""
import re, sys, subprocess, json, os, tempfile
from bs4 import BeautifulSoup

kit = os.path.dirname(os.path.abspath(__file__))
H = open(sys.argv[1], encoding='utf-8').read()
M = json.load(open(sys.argv[2], encoding='utf-8'))
NT = int(M['terminos'])
PROB = {k: int(M['problemas'].get(k, 0)) for k in ('B', 'P', 'S', 'FR')}
NH = int(M['hipotesis'])
ND = max(4, int(M['diagramas']))  # suelo del contrato: 4 diagramas
res = []


def chk(name, ok, det=''):
    res.append(ok)
    print(('VERDE ' if ok else 'ROJO  ') + name + (' | ' + det if det else ''))


def wc(s):
    return len(re.findall(r'\S+', s))


def txt(e):
    return re.sub(r'\s+', ' ', e.get_text(' ')).strip()


# ---------- JS ----------
m = re.search(r'<script>(.*?)</script>', H, re.S)
chk('hay un <script>', bool(m) and H.count('<script') == 1)
if not m:
    print('\nRESULTADO: ROJO'); sys.exit(1)
js = m.group(1)
body = H.replace(m.group(0), '')
work = tempfile.mkdtemp()
tmp = os.path.join(work, '_w.js'); open(tmp, 'w', encoding='utf-8').write(js)
r = subprocess.run(['node', '--check', tmp], capture_output=True, text=True)
chk('node --check', r.returncode == 0, r.stderr[:200])
ev = r"""
const vm=require('vm');const fs=require('fs');
const code=fs.readFileSync(process.argv[2],'utf8');
const sb={document:{getElementById:()=>null,querySelectorAll:()=>[]},console};
vm.createContext(sb);vm.runInContext(code+';this.__o={DECKS,TERMS,RC}',sb);
console.log(JSON.stringify({DECKS:sb.__o.DECKS,TERMS:sb.__o.TERMS}));
"""
evf = os.path.join(work, '_ev.js'); open(evf, 'w').write(ev)
r = subprocess.run(['node', evf, tmp], capture_output=True, text=True)
try:
    o = json.loads(r.stdout); D = o['DECKS']; TERMS = o['TERMS']
    chk('DECKS y TERMS se evalúan', True)
except Exception:
    chk('DECKS y TERMS se evalúan', False, r.stderr[:200])
    print('\nRESULTADO: ROJO'); sys.exit(1)

# ---------- cero marcas (estricto) ----------
PROHIB = ('VERIFICAR EN FUENTE', 'Fuente por verificar')
hall = [x for x in PROHIB if re.search(re.escape(x), H, re.I)]
chk('cero marcas: sin «[VERIFICAR EN FUENTE]» ni «Fuente por verificar»', not hall, str(hall))

# ---------- estructura (balance) ----------
from html.parser import HTMLParser
TAGS = ('div', 'section', 'table', 'nav', 'ol', 'ul', 'li', 'button', 'p', 'span', 'thead', 'tbody', 'figure', 'figcaption', 'mark')


class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack = []; s.errs = []

    def handle_starttag(s, t, a):
        if t in TAGS: s.stack.append(t)

    def handle_endtag(s, t):
        if t in TAGS:
            if not s.stack or s.stack[-1] != t: s.errs.append('desbalance ' + t + ' tras ' + str(s.stack[-3:]))
            else: s.stack.pop()


p = P(); p.feed(body)
chk('balance de etiquetas de bloque', not p.errs and not p.stack, '; '.join(p.errs[:3]) + str(p.stack))

S = BeautifulSoup(body, 'html.parser')
tabs = S.select('section.tab')
ids = [t.get('id') for t in tabs]
T = ['t%d' % i for i in range(1, NT + 1)]
exp = ['c0'] + T + ['pb', 'jq', 'hx', 'tg']
chk('pestañas en orden c0, t1..tN, pb, jq, hx, tg', ids == exp, str(ids))
btn = re.findall(r"onclick=\"show\('(\w+)',this\)\"", body)
chk('botones show(id) 1:1 con las pestañas', btn == exp, str(btn))
chk('barra: un botón tb por pestaña', len(S.select('nav.tabs button.tb')) == len(exp))
act = [t.get('id') for t in tabs if 'active' in (t.get('class') or [])]
bact = [i for i, b in enumerate(S.select('nav.tabs button.tb')) if 'active' in (b.get('class') or [])]
chk('solo c0 activa (sección y botón)', act == ['c0'] and bact == [0], str(act) + str(bact))
chk('cada pestaña empieza con <h2>', all((t.find(True) is not None and t.find(True).name == 'h2') for t in tabs))
chk('tipo del manifiesto = apertura', M.get('tipo') == 'apertura')
SEC = dict(zip(ids, tabs))
c0 = SEC.get('c0')

# ---------- c0 ----------
if c0 is not None:
    chk('c0: sin simulador', not c0.select('.rc') and 'id="rc-c0' not in body)
    chk('c0: card.caso', bool(c0.select_one('.card.caso')))
    chk('c0: .ley con los cuatro chips', bool(c0.select_one('.ley')) and all(c0.select_one('.ley .chip-' + x) for x in ('b', 'p', 's', 'fr')))
    chk('c0: marcas mk-b, mk-p, mk-s, mk-fr', all(c0.select_one('mark.mk-' + x) for x in ('b', 'p', 's', 'fr')))
    chk('c0: idea rectora y glosario', bool(c0.select_one('.hb')) and bool(c0.select_one('.gloss')))
    chk('c0: mark solo con clase mk-*', all(any(c.startswith('mk-') for c in (mk.get('class') or [])) for mk in S.find_all('mark')))

# ---------- términos ----------
fl = []
for tid in T:
    t = SEC.get(tid)
    if t is None: continue
    if not t.select_one('.hb'): fl.append((tid, 'hb'))
    pre = t.select_one('.pre'); rem = t.select('.rem-line')
    if not (pre or rem): fl.append((tid, 'sin pre ni rem-line'))
    if pre and not pre.select_one('.pre-t'): fl.append((tid, 'pre-t'))
    npre = len(t.select('.pre .acc'))
    if npre > 5: fl.append((tid, 'prerrequisitos>5', npre))
    if any('op' not in (a.get('class') or []) for a in t.select('.pre .acc')): fl.append((tid, 'prerrequisito cerrado'))
    defc = [c for c in t.select('.card') if (c.select_one('.card-t') and 'Definición de referencia' in txt(c.select_one('.card-t')))]
    if not defc: fl.append((tid, 'card definición'))
    if not t.select_one('.card.fey'): fl.append((tid, 'fey'))
    if not t.select_one('.card.ej'): fl.append((tid, 'ej'))
    if not t.select_one('.card.vin'): fl.append((tid, 'card.vin'))
    elif not t.select_one('.card.vin .pid'): fl.append((tid, 'vin sin pid'))
    if not t.select_one('.acc.no'): fl.append((tid, 'acc.no'))
    if not t.select_one('.rc'): fl.append((tid, 'rc'))
    if not t.select_one('.gloss'): fl.append((tid, 'gloss'))
    sh = str(t)
    ie, iv, ino = sh.find('card ej'), sh.find('card vin'), sh.find('acc no')
    if not (0 <= ie < iv < ino): fl.append((tid, 'orden ej → vin → no confundir'))
chk('estructura de cada pestaña de término', not fl, str(fl))

# simuladores y mazos
rc_ids = [t.get('id') for t in tabs if t.select_one('.rc')]
want_rc = T + ['pb', 'jq', 'hx', 'tg']
chk('simulador solo en t*, pb, jq, hx, tg', rc_ids == want_rc, str(rc_ids))
rcbad = [k for k in want_rc if not all(('id="%s"' % x) in body for x in ('rc-' + k, 'rc-%s-n' % k, 'rc-%s-c' % k, 'rc-%s-b' % k, 'rc-%s-e' % k))]
chk('cada rc con sus ids -n -c -b -e', not rcbad, str(rcbad))
chk('DECKS claves = pestañas con simulador', sorted(D) == sorted(want_rc), str(sorted(D)))
chk('TERMS nombra cada pestaña (no tg)', sorted(TERMS) == sorted(want_rc[:-1]), str(sorted(TERMS)))
okd = all(k in D for k in want_rc)
if okd:
    chk('4-6 tarjetas por término', all(4 <= len(D[k]) <= 6 for k in T), str([len(D[k]) for k in T]))
    chk('pb y hx 4-8 tarjetas', all(4 <= len(D[k]) <= 8 for k in ('pb', 'hx')), str((len(D['pb']), len(D['hx']))))
    chk('jq 4-6 tarjetas', 4 <= len(D['jq']) <= 6, str(len(D['jq'])))
    orden = T + ['pb', 'jq', 'hx']
    un = [(c['q'], c['a'], c['h'], k) for k in orden for c in D[k]]
    g = [(c['q'], c['a'], c['h'], c.get('t')) for c in D['tg']]
    chk('mazo global = unión exacta en orden (campo t correcto)', un == g, '%d frente a %d' % (len(un), len(g)))
    chk('toda tarjeta con q, a y pista', all(c.get('q') and c.get('a') and c.get('h') for k in orden for c in D[k]))
chk('un solo motor rc_* (1 definición c/u)', all(len(re.findall(r'function ' + f + r'\(', js)) == 1 for f in ('rc_render', 'rc_show', 'rc_grade', 'rc_end', 'rc_reset')) and not re.search(r'function rc_\w+_t\d', js))

# ---------- pb ----------
pids_def = {}  # id -> eje
pb = SEC.get('pb')
if pb is not None:
    axes = {}
    fl = []
    for g in pb.select('.pbg'):
        cl = [c for c in g.get('class') if c in ('b', 'p', 's', 'fr')]
        if len(cl) != 1: fl.append('pbg sin un modificador de eje'); continue
        axes.setdefault(cl[0].upper(), []).append(g)
        if not g.select_one('.pbg-t'): fl.append('pbg sin .pbg-t (%s)' % cl[0])
    for ax, n in PROB.items():
        if n > 0 and len(axes.get(ax, [])) != 1: fl.append('eje %s: %d contenedores .pbg' % (ax, len(axes.get(ax, []))))
    chk('pb: un .pbg por eje (con título)', not fl, str(fl))
    fl = []; allp = []
    for ax, n in PROB.items():
        if n == 0 or ax not in axes: continue
        accs = [a for a in axes[ax][0].select('.acc') if a.select_one('.acc-h .pid')]
        got = [txt(a.select_one('.acc-h .pid')) for a in accs]
        allp += got
        chk('pb %s: %d problemas con ids %s1..%s%d' % (ax, n, ax, ax, n), got == ['%s%d' % (ax, i) for i in range(1, n + 1)], str(got))
        for a in accs:
            pid = txt(a.select_one('.acc-h .pid')); pids_def[pid] = ax
            b = a.select_one('.acc-b'); bt = txt(b) if b else ''
            for need in ('Dato del caso', 'Fisiopatología', 'Por qué importa'):
                if need not in bt: fl.append((pid, need))
            if b is not None and not (b.select_one('ol.tl') or b.select_one('.rem-line')): fl.append((pid, 'sin ol.tl ni rem-line'))
            op = 'op' in (a.get('class') or [])
            if (ax == 'B') != op: fl.append((pid, 'apertura del acordeón (B abierto, resto cerrado)'))
        extra = [a for a in axes[ax][0].select('.acc') if not a.select_one('.acc-h .pid')]
        if extra: fl.append((ax, 'acordeón sin pid en su cabecera'))
    chk('pb: cada problema con Dato del caso, Fisiopatología, ol.tl/rem-line y Por qué importa', not fl, str(fl[:6]))
    chk('pb: ids únicos', len(allp) == len(set(allp)))
    chk('pb: ≥1 diagrama', bool(pb.select('figure.dg')))

# ---------- jq ----------
jq = SEC.get('jq')
if jq is not None:
    rk = jq.select('ol.rank')
    chk('jq: un ol.rank', len(rk) == 1)
    if rk:
        lis = rk[0].find_all('li', recursive=False)
        fl = []; seen = []
        for li in lis:
            gc = [c for c in (li.get('class') or []) if c in ('g1', 'g2', 'g3', 'g4')]
            if len(gc) != 1: fl.append('li sin clase g1-g4')
            pd = li.select_one('.pid')
            if not pd: fl.append('li sin pid'); continue
            seen.append(txt(pd))
        need = [i for i, ax in pids_def.items() if ax in ('B', 'P', 'S')]
        chk('jq: cada li con clase g1-g4 y pid', not fl, str(fl[:3]))
        chk('jq: rank contiene cada B/P/S una vez y ningún FR', sorted(seen) == sorted(need) and len(seen) == len(set(seen)),
            'faltan %s; sobran %s; repetidos %s' % (sorted(set(need) - set(seen)), sorted(set(seen) - set(need)), sorted({x for x in seen if seen.count(x) > 1})))
    chk('jq: tabla de criterios', bool(jq.select_one('table')))
    chk('jq: ≥1 diagrama', bool(jq.select('figure.dg')))

# ---------- hx ----------
hx = SEC.get('hx')
if hx is not None:
    cards = hx.select('.card.hx')
    chk('hx: nº de .card.hx = manifiesto', len(cards) == NH, '%d de %d' % (len(cards), NH))
    fl = []; hids = []
    for c in cards:
        ps = [txt(x) for x in c.select('.pid')]
        prob = [x for x in ps if not x.startswith('H')]
        hids += [x for x in ps if re.fullmatch(r'H\d+', x)]
        if not prob: fl.append('hipótesis sin pid de problema')
        for x in prob:
            if x not in pids_def: fl.append('pid inexistente ' + x)
        if not c.select_one('table'): fl.append('sin tabla')
        if 'Qué la confirmaría' not in txt(c): fl.append('sin «Qué la confirmaría»')
    chk('hx: cada hipótesis cita pid existentes, tiene tabla y «Qué la confirmaría»', not fl, str(fl[:4]))
    chk('hx: ids H únicos', len(hids) == len(set(hids)))
    chk('hx: tabla diferencial fuera de las cards', any(not t.find_parent(class_='hx') for t in hx.select('table')))
    chk('hx: card «Necesidades de aprendizaje»', 'Necesidades de aprendizaje' in txt(hx))
    chk('hx: ≥1 diagrama', bool(hx.select('figure.dg')))

# pids usados en todo el widget deben existir
bad = set()
for t in tabs:
    for x in t.select('.pid'):
        v = txt(x)
        if re.fullmatch(r'H\d+', v): continue
        if v not in pids_def: bad.add(v)
chk('todo pid usado existe en Problemas', not bad, str(sorted(bad)))

# ---------- diagramas ----------
figs = S.select('figure.dg')
chk('diagramas ≥ max(4, manifiesto) (%d)' % ND, len(figs) >= ND, str(len(figs)))
fl = []
for i, f in enumerate(figs, 1):
    if not f.select_one('.dg-t'): fl.append((i, 'dg-t'))
    if f.find('figcaption') is None: fl.append((i, 'figcaption'))
    if not f.select_one('.dg-row'): fl.append((i, 'dg-row'))
    if f.find('img') or f.find('svg'): fl.append((i, 'img/svg'))
    for n in f.select('.dg-n'):
        if wc(txt(n)) > 12: fl.append((i, 'nodo>12 palabras', txt(n)[:30]))
    for a in f.select('.dg-ar'):
        if not a.find_parent(class_='dg-row'): fl.append((i, 'dg-ar fuera de dg-row'))
chk('cada figure.dg con dg-t, dg-row, figcaption y nodos ≤12 palabras', not fl, str(fl[:4]))
chk('figure.dg solo con clase dg', all('dg' in (f.get('class') or []) for f in S.find_all('figure')))

# ---------- citas ----------
vi = body.find('class="vanc"')
chk('hay ol.vanc', vi > 0)
if vi > 0:
    pre = re.sub(r'<[^>]+>', ' ', body[:vi])
    seen = []
    for g in re.findall(r'\[(\d+(?:\s*[,–-]\s*\d+)*)\]', pre):
        for part in re.split(r'\s*,\s*', g):
            if re.search(r'[–-]', part):
                a, b2 = [int(x) for x in re.split(r'\s*[–-]\s*', part)]
                nums = range(a, b2 + 1)
            else:
                nums = [int(part)]
            for n in nums:
                if n not in seen: seen.append(n)
    nli = len(S.select('ol.vanc > li'))
    chk('citas [n] en orden de primera aparición', seen == list(range(1, len(seen) + 1)), str(seen))
    chk('lista Vancouver = nº de citas distintas', nli == len(seen), '%d li / %d citas' % (nli, len(seen)))
chk('no quedan citas [@clave]', '[@' not in H)

# ---------- cadenas prohibidas, cabecera ----------
bad = ['localStorage', 'sessionStorage', 'position: fixed', 'position:fixed', '...', '[resto', 'continúa -->', 'TODO', 'placeholder', 'TSV', 'Exportar a Anki', '<img', '<svg', 'src="http', 'class="fig"', 'style=', '⚠', '✅', '❌']
hits = [b for b in bad if b in H]
chk('cadenas prohibidas', not hits, str(hits))
chk('un solo <style> (cabecera intacta)', H.count('<style') == 1)
head = open(os.path.join(kit, 'apertura_head.html'), encoding='utf-8').read()
tm = re.search(r'<title>.*?</title>', H, re.S)
head = head.replace('<title>@@TITULO@@</title>', tm.group(0) if tm else '')
chk('cabecera = apertura_head.html con título sustituido', H.startswith(head))
chk('sin emojis/pictogramas', not re.search('[\U0001F000-\U0001FFFF☀-➿⬀-⯿️]', H))

# ---------- vocabulario ----------
headcss = re.search(r'<style>(.*?)</style>', head, re.S).group(1)
voc = set(re.findall(r'\.([a-zA-Z][\w-]*)', headcss)) | {'active', 'op'}
used = {c for t in S.find_all(class_=True) for c in t.get('class')}
used |= {c for s in re.findall(r'class="([^"+]+)"', js) for c in s.split()} | {'ok', 'rep'}
chk('solo vocabulario de clases de apertura_head', used <= voc, str(sorted(used - voc)))

# ---------- tablas, cards, párrafos ----------
fl = []
for i, tb in enumerate(S.find_all('table'), 1):
    if not tb.find('thead') or not tb.find('thead').find('th') or not tb.find('tbody'): fl.append((i, 'thead/tbody'))
    if not (tb.parent and 'tw' in (tb.parent.get('class') or [])): fl.append((i, 'fuera de .tw'))
chk('tablas con thead(th)+tbody dentro de div.tw', not fl, str(fl))
fl = []
for tb in S.find_all('table'):
    for tr in tb.find_all('tr'):
        for k, td in enumerate(tr.find_all(['td', 'th'])):
            if k > 0 and td.name == 'td' and td.find(['b', 'strong']): fl.append(txt(td)[:25])
chk('<b> solo en la 1.ª columna de las tablas', not fl, str(fl[:3]))
chk('sin cards anidadas', not any(c.find_parent(class_=['card', 'hb', 'pre']) for c in S.select('.card')))
big = [wc(txt(x)) for x in S.find_all('p') if wc(txt(x)) > 90]
chk('párrafos <=90 palabras', not big, str(big))
chk('<=1 <b> por párrafo', not [1 for x in S.find_all('p') if len(x.find_all(['b', 'strong'])) > 1])

# ---------- límites por pestaña y siglas ----------
fl = []
ROM = {'II', 'III', 'IV'}
for t in tabs:
    sid = t.get('id')
    if sid == 'tg': continue
    hbs = t.select('.hb')
    if len(hbs) > 1: fl.append((sid, 'más de una .hb'))
    for hb in hbs:
        pp = hb.find('p'); n = wc(txt(pp)) if pp else 0
        lim = 25 if (sid == 'c0' or sid in T) else 40
        if n > lim: fl.append((sid, 'hb', n))
    if sid in T:
        for c in t.select('.card'):
            ct = c.select_one('.card-t'); tt = txt(ct) if ct else ''
            pp = c.find('p')
            if 'Definición de referencia' in tt and pp and wc(txt(pp)) > 60: fl.append((sid, 'def', wc(txt(pp))))
            if 'fey' in c.get('class') and pp and wc(txt(pp)) > 80: fl.append((sid, 'fey', wc(txt(pp))))
            if 'vin' in c.get('class'):
                cc = BeautifulSoup(str(c), 'html.parser')
                for x in cc.select('.card-t,.pid'): x.decompose()
                if wc(txt(cc)) > 70: fl.append((sid, 'vin', wc(txt(cc))))
    gls = t.select('.gloss')
    if len(gls) != 1: fl.append((sid, 'glosario', len(gls))); continue
    gl = txt(gls[0])
    cc = BeautifulSoup(str(t), 'html.parser')
    for x in cc.select('.gloss,.pid'): x.decompose()
    core = txt(cc)
    toks = set(re.findall(r'(?<![A-Za-zÁ-ú])[A-Z][A-Z0-9]{1,}(?![A-Za-zÁ-ú0-9])', core)) - ROM
    toks = {x for x in toks if not re.fullmatch(r'(B|P|S|FR|H)\d+', x)}
    miss = sorted(x for x in toks if x not in gl)
    if miss: fl.append((sid, 'siglas sin glosario', miss))
chk('límites (hb, def 60, Feynman 80, vin 70) y glosarios por pestaña', not fl, str(fl))
heads = []
for e in S.select('h1,h2,h3,.hb-t,.card-t,.pre-t,.rc-t,.acc-h,.pbg-t,.dg-t'):
    ws = [w for w in re.findall(r"[A-Za-zÁ-úñ]+", txt(e)) if len(w) > 3]
    if len(ws) >= 2 and all(w.isupper() for w in ws): heads.append(txt(e)[:40])
chk('sin títulos en MAYÚSCULAS', not heads, str(heads))

# ---------- estilo ----------
vis = txt(BeautifulSoup(body, 'html.parser').find('body') or S)
vis = re.sub(r'<style.*?</style>', '', vis)
chk('sin exclamaciones ni muletillas', not re.search(r'[¡!]|cabe destacar|es importante mencionar|sin lugar a dudas|vale la pena', vis))
chk('cierre </div></body></html>', H.rstrip().endswith('</div></body></html>'))
chk('Repaso global con Referencias y ol.vanc', '<span>Referencias</span>' in H and bool(S.select_one('ol.vanc')))

print('\nRESULTADO:', 'VERDE' if all(res) else 'ROJO')
sys.exit(0 if all(res) else 1)
