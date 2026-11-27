#!/usr/bin/env python3
"""Validador fijo del widget v11 (mono|multi). Uso: python3 validar.py widget.html [manifiesto.json]"""
import sys, re, json, subprocess, tempfile, os, unicodedata
try:
    from bs4 import BeautifulSoup, Tag
except ImportError:
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'beautifulsoup4', '--break-system-packages'])
    from bs4 import BeautifulSoup, Tag
def _hook(tp, v, tb):
    import traceback; ln = traceback.extract_tb(tb)[-1].lineno if tb else '?'
    print(f'ERROR [validador]: excepción interna {tp.__name__}: {v} (línea {ln}); revisa la estructura señalada o reensambla')
    print('RESULTADO: FALLA · errores 1 · avisos 0 · JS ?'); sys.exit(1)
sys.excepthook = _hook
P = sys.argv[1]; H = open(P, encoding='utf-8').read(); S = BeautifulSoup(H, 'html.parser')
E, W = {}, {}
def err(c, m):
    if m not in E.setdefault(c, []): E[c].append(m)
def warn(c, m):
    if m not in W.setdefault(c, []): W[c].append(m)
CIT = re.compile(r'\[\d+(?:\s*[,–-]\s*\d+)*\]')
def txt(el): return re.sub(r'\s+', ' ', el.get_text(' ')).strip()
def words(t): return len(re.findall(r"[\w%/\-]+", CIT.sub(' ', t)))
def kids(el): return [c for c in el.children if isinstance(c, Tag)]
def cls(el): return ' '.join(el.get('class') or [])
def nz(s):
    s = s.replace('º', 'o').replace('°', 'o').casefold()
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    return re.sub(r'[\s.]', '', s)
IDRE = re.compile(r'^(?:(e\d{1,2})-)?([ms])-(\d+)$')
def kind(i):
    m = IDRE.match(i or ''); return m.group(2) if m else None
# --- ensamblaje: separa kit / partes del LLM
A, B = '<!-- /KIT_HEAD -->', '<!-- KIT_SCRIPT -->'
if H.count(A) == 1 and H.count(B) == 1 and H.index(A) < H.index(B): LLM = H[H.index(A) + len(A):H.index(B)]
else: LLM = H; err('ensamblaje', 'marcas del kit ausentes o duplicadas: ensambla con el comando del contrato (kit_head.html primero, kit_script.html al final, sin editarlos)')
L = BeautifulSoup(LLM, 'html.parser')
# --- pestañas y modo
tbs = [b.get('data-tab') for b in S.select('button.tb')]
secl = S.select('section.tab'); keys = [s.get('data-tab') for s in secl]; secs = {s.get('data-tab'): s for s in secl}
name = {b.get('data-tab'): txt(b) for b in S.select('button.tb')}
if len(set(keys)) != len(keys): err('pestañas', f'data-tab repetido en sections: {keys}')
if len(set(tbs)) != len(tbs): err('pestañas', f'data-tab repetido en botones: {tbs}')
if tbs != keys: err('pestañas', f'orden DOM de sections {keys} ≠ orden de botones {tbs}: ordena partes y botones igual')
for b in S.select('button.tb'):
    if (b.get('onclick') or '').strip() != f"show('{b.get('data-tab')}')": err('pestañas', f'botón {b.get("data-tab")}: onclick="show(\'{b.get("data-tab")}\')"')
struct = 'multi' if ('vis' in secs or any(re.fullmatch(r'e\d+', k or '') for k in secs)) else 'mono'
M = None
if len(sys.argv) > 2:
    try: M = json.load(open(sys.argv[2], encoding='utf-8'))
    except Exception as e: err('manifiesto', f'manifiesto.json ilegible: {e}')
MODE = struct
if M is None: warn('manifiesto', 'sin manifiesto: modo detectado por estructura')
elif M.get('modo') is None: warn('manifiesto', f'falta "modo": usa "modo":"{struct}"')
elif M.get('modo') != struct: err('modo', f'manifiesto "modo":"{M.get("modo")}" pero el HTML es {struct} (pestañas {tbs}): corrige uno de los dos')
ENT = [k for k in tbs if re.fullmatch(r'e\d+', k or '')]
N = len(ENT)
BASE = ['pan', 'def', 'fis', 'cli', 'dx', 'tx', 'seg']
if MODE == 'mono':
    for k in BASE:
        if k not in secs: err('pestañas', f'falta <section class="tab" data-tab="{k}">')
    extra = [k for k in tbs if k not in BASE]
    if len(extra) > 1: err('pestañas', f'más de una pestaña adicional: {extra}')
    for x in extra:
        if not re.fullmatch(r'[a-z]{2,4}', x or ''): err('pestañas', f'clave adicional "{x}": 2–4 letras minúsculas')
    if [k for k in tbs if k in BASE] != [k for k in BASE if k in tbs]: err('pestañas', f'orden de barra: {" ".join(BASE)} (+1 adicional en su lugar lógico)')
else:
    exp = ['pan', 'vis'] + [f'e{i}' for i in range(1, N + 1)] + ['sin']
    if N > 15: err('entidades', f'{N} entidades: máximo 15 (multi ampliado); propone dividir el tema')
    if N < 3: err('entidades', f'{N} entidades: multi exige 3–15 (con 1–2 usa mono)')
    if tbs != exp: err('pestañas', f'barra multi debe ser exactamente {" ".join(exp)}; hay {" ".join(map(str, tbs))}')
CONT = [k for k in tbs if k != 'pan' and k in secs]
REFTAB = 'sin' if MODE == 'multi' else 'seg'
# --- JS
scripts = '\n'.join(s.string or '' for s in S.find_all('script'))
llm_js = '\n'.join(s.string or '' for s in L.find_all('script'))
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f: f.write(scripts); jf = f.name
try:
    r = subprocess.run(['node', '--check', jf], capture_output=True, text=True)
    js_ok = 'OK' if not r.returncode else 'ERROR'
    if r.returncode: err('js', 'node --check: ' + r.stderr.strip()[-300:])
except FileNotFoundError:
    js_ok = 'validación manual'; warn('js', 'node no disponible')
os.unlink(jf)
for fn in ['window.show', 'window.ir', 'window.tog', 'window.ch']:
    if fn not in scripts: err('kit', f'kit_script incompleto o editado: falta {fn}; reextrae el kit')
for m in re.finditer(r'(?:function\s+|(?:var|let|const)\s+|window\.)(show|ir|tog|ch|sel|num|out|rd)\b\s*[=(]', llm_js):
    err('simulador', f'90_sim redefine el nombre reservado "{m.group(1)}": renombra tu función')
if len(L.find_all('script')) > 1: warn('simulador', 'más de un <script> en las partes: todo en 90_sim.html')
if re.search(r'\b(VPP|VPN|prevalencia|Bayes|post-?test|pre-?test|Fagan|likelihood)\b', llm_js, re.I): err('simulador', 'simulador con lógica de rendimiento diagnóstico (VPP/VPN/prevalencia/Bayes): elimínala; esas cifras solo se tabulan')
# --- cadenas prohibidas (solo partes del LLM)
for bad in ['localStorage', 'sessionStorage', 'position:fixed', 'position: fixed', '[resto', 'continúa -->', 'TODO:', '<style', '<link', '@import', 'url(', '<iframe', '<object', '<embed', 'src="http', "src='http"]:
    if bad in LLM: err('prohibido', f'cadena prohibida en las partes: «{bad}»')
if re.search(r'<[a-zA-Z][^>]*\sstyle\s*=', LLM): err('prohibido', 'estilo inline (style="…"): usa solo clases del kit')
for bad in ('VERIFICAR EN FUENTE', 'Fuente por verificar'):
    if bad in LLM: err('verificacion', f'{LLM.count(bad)} marca(s) «{bad}»: agota PubMed, Consensus, fichas técnicas y GPC del MSP; si no se confirma, elimina el dato')
if '@@TITULO@@' in H: err('prohibido', 'título sin sustituir: sed "s/@@TITULO@@/<Tema>/"')
LT = BeautifulSoup(LLM, 'html.parser')
for t in LT(['script', 'style']): t.decompose()
m3 = re.search(r'.{0,30}\.\.\..{0,10}', LT.get_text(' '))
if m3: err('prohibido', f'«...» ASCII en el texto («{m3.group(0).strip()}»): usa «…» (U+2026)')
for im in S.find_all('img'):
    fg = im.find_parent('figure'); fc = fg.find('figcaption') if fg else None
    if not (fg and 'fig' in (fg.get('class') or []) and fc and txt(fc) and (im.get('src') or '').startswith('data:image/') and (im.get('alt') or '').strip()):
        err('imagen', '<img> solo así: <figure class="fig"><img src="data:image/jpeg;base64,…" alt="…"><figcaption>interpreta…</figcaption></figure>')
# --- Panorama
pan = secs.get('pan')
if pan:
    et = pan.select('.etapa')
    if MODE == 'mono':
        if len(et) < 7: err('panorama', f'{len(et)} etapas (mínimo 7)')
        gos = None
    else:
        gos = ['vis'] + ENT
        if [e.get('data-go') for e in et] != gos: err('panorama', f'etapas data-go {[e.get("data-go") for e in et]} → deben ser {gos} (eje primero, luego una por entidad)')
    lim = max(900, 115 * (len(ENT) + 1))  # multi ampliado: ~110 palabras por etapa
    if words(txt(pan)) > lim: err('panorama', f'{words(txt(pan))} palabras (>{lim})')
    for i, e in enumerate(et, 1):
        rs, pe = e.select_one('.res'), e.select_one('.perla')
        if not rs or not pe: err('panorama', f'etapa {i}: falta p.res o p.perla'); continue
        n = words(txt(rs))
        if not 70 <= n <= 110: err('panorama', f'etapa {i}: párrafo {n} palabras (70–110)')
        if words(txt(pe)) > 20: err('panorama', f'etapa {i}: perla {words(txt(pe))} palabras (>20)')
        g = e.get('data-go'); bt = e.select_one('button[data-go]')
        if g not in secs or not bt or bt.get('data-go') != g or (bt.get('onclick') or '').strip() != f"show('{g}')": err('panorama', f'etapa {i}: <button type="button" class="go" data-go="{g}" onclick="show(\'{g}\')">')
    for x in pan.select('.pg,.fey,.dc,.nodo,.signo,.qv,ol.tg'): err('panorama', 'elemento prohibido en pan: .' + cls(x))
    if not any(txt(p).startswith('Esto es el mapa, no el territorio') for p in pan.select('p.mini')): warn('panorama', 'falta la línea de cierre literal en p.mini')
# --- segmentos h2 (multi)
H2L = ['Qué es', 'Epidemiología', 'Cadena', 'Qué verás', 'Diagnóstico', 'Tratamiento', 'Seguimiento']
GRP = {}
def top_of(el, sec):
    while el is not None and el.parent is not sec: el = el.parent
    return el
def grp(el):
    s = el.find_parent('section', class_='tab')
    if s is None: return None, None
    t = top_of(el, s); return s.get('data-tab'), GRP.get(id(t))
if MODE == 'multi':
    for k in ENT:
        s = secs.get(k)
        if not s: continue
        for h in s.find_all('h2'):
            if h.parent is not s: err('h2', f'{k}: h2 «{txt(h)}» debe ser hijo directo de la section')
        hs = s.find_all('h2', recursive=False); lab = [txt(h) for h in hs]
        if len(hs) != 7 or any(not nz(a).startswith(nz(b)) for a, b in zip(lab, H2L)):
            err('h2', f'{k}: h2 deben ser 7 y en orden: {" · ".join(H2L)}; hay: {" · ".join(lab)}')
        cur = None; order = []
        for c in kids(s):
            if c.name == 'h2':
                cur = next((b for b in H2L if nz(txt(c)).startswith(nz(b))), txt(c))
            GRP[id(c)] = cur; order.append((c, cur))
        pre = [c for c, g in order if g is None]
        iF = next((i for i, c in enumerate(pre) if 'hb' in (c.get('class') or []) and c.select_one('.hb-t') and txt(c.select_one('.hb-t')).startswith('Frente a')), None)
        iP = next((i for i, c in enumerate(pre) if c.select_one('ol.pg')), None)
        if pre and iF is not None and iF != 0: warn('orden', f'{k}: la primera caja debe ser «Frente a…» (sin highlight previo)')
        if iF is None: err('delta', f'{k}: falta <div class="hb az"><div class="hb-t">Frente a [entidad]</div>… antes de las preguntas guía')
        elif iP is not None and iF > iP: err('delta', f'{k}: «Frente a…» va antes de las preguntas guía')
        elif k != 'e1' and not any(name[j] in txt(pre[iF]) for j in ENT if j != k and j in name): warn('delta', f'{k}: «Frente a…» no nombra a ninguna entidad del grupo')
        if iP is None: err('pg', f'{k}: preguntas guía (hb az + ol.pg) antes del primer h2')
        def first_after(lbl):
            it = [c for c, g in order if g == lbl and c.name != 'h2']
            return it[0] if it else None
        ep = [c for c, g in order if g == 'Epidemiología']
        tb = next((t for c in ep for t in ([c] if c.name == 'table' else c.select('table'))), None)
        EPI = ['Frecuencia', 'Edad', 'Sexo', 'Factores clave']
        if not tb: err('epidemiologia', f'{k}: Epidemiología sin tabla de 4 filas ({" · ".join(EPI)})')
        else:
            rows = tb.select('tbody > tr') or tb.find_all('tr')[1:]
            fc = [txt(r.find(['th', 'td'])) for r in rows if r.find(['th', 'td'])]
            if fc != EPI: err('epidemiologia', f'{k}: primera columna {fc} → exactamente {EPI}')
        for lbl, ctx in (('Diagnóstico', 'dx'), ('Tratamiento', 'tx')):
            fa = first_after(lbl)
            if fa is None or fa.name != 'ol' or not {'steps', 'tg'} <= set(fa.get('class') or []): err('pasos', f'{k}: el primer bloque bajo «{lbl}» debe ser <ol class="steps tg">')
        tls = s.select('ol.tl')
        if not tls: err('timeline', f'{k}: falta ol.tl bajo «Cadena»')
        for o in tls:
            if o.parent is not s or GRP.get(id(o)) != 'Cadena': err('timeline', f'{k}: ol.tl hija directa de la section y bajo h2 «Cadena»')
        qv = s.select('.qv')
        if len(qv) != 1 or GRP.get(id(top_of(qv[0], s))) != 'Qué verás': err('qv', f'{k}: exactamente una .qv bajo «Qué verás» (hay {len(qv)})')
        for sg in s.select('.signo'):
            if GRP.get(id(top_of(sg, s))) != 'Qué verás': err('signos', f'{k}: ficha .signo {sg.get("id")} fuera de «Qué verás»')
        fy = s.select('.fey'); dcs = [grp(d)[1] for d in s.select('.dc')]
        if k == 'e1':
            if len(fy) != 2: err('profundidad', f'e1 (principal): {len(fy)} Feynman (exactamente 2: tras «Cadena» y tras «Qué verás»)')
            for lbl in ('Diagnóstico', 'Tratamiento'):
                if lbl not in dcs: err('profundidad', f'e1 (principal): falta simulador .dc bajo «{lbl}»')
        else:
            if len(fy) not in (1, 2) or grp(fy[0])[1] != 'Cadena': err('profundidad', f'{k} (secundaria): 1–2 Feynman, el primero bajo «Cadena» (hay {len(fy)})')
            if 'Tratamiento' not in dcs: err('profundidad', f'{k} (secundaria): falta simulador .dc bajo «Tratamiento»')
# --- preguntas guía, badge, Feynman
PGR = {}
for k in CONT:
    s = secs[k]; pg = s.select('ol.pg')
    if MODE == 'multi' and k == 'sin':
        if pg: err('pg', 'sin: sin preguntas guía')
        continue
    rng = (3, 5)  # secundarias 3–5 desde el multi ampliado
    if len(pg) != 1: err('pg', f'{k}: {len(pg)} listas ol.pg (debe ser 1)')
    else:
        n = len(pg[0].find_all('li', recursive=False))
        if not rng[0] <= n <= rng[1]: err('pg', f'{k}: {n} preguntas guía ({rng[0]}–{rng[1]})' if rng[0] != rng[1] else f'{k}: {n} preguntas guía (secundaria: exactamente 3)')
    if not s.select('.b-pu'): err('badge', f'{k}: falta <span class="badge b-pu"> de la guía rectora')
for s in S.select('section.tab'):
    k = s.get('data-tab')
    for i, fy in enumerate(s.select('.fey'), 1):
        if fy.find_parent(class_='acc'): err('feynman', f'{k}: Feynman {i} dentro de acordeón')
        b = fy.select_one('.fey-b'); cs = fy.select('.fey-c')
        if not b: err('feynman', f'{k}: Feynman {i} sin p.fey-b'); continue
        if words(txt(b)) > 90: err('feynman', f'{k}: Feynman {i} cuerpo {words(txt(b))} palabras (>90)')
        if re.search(r'\d', txt(b)): warn('feynman', f'{k}: Feynman {i} contiene dígitos (revisar cifras/dosis)')
        if len(cs) != 2 or not txt(cs[0]).startswith('En medicina esto se llama…') or not txt(cs[1]).startswith('Dónde falla la comparación:'):
            err('feynman', f'{k}: Feynman {i}: dos p.mini.fey-c «En medicina esto se llama…» y «Dónde falla la comparación:»')
if MODE == 'multi':
    for k in ('vis', 'sin'):
        if k in secs and secs[k].select('.fey'): err('feynman', f'{k}: sin Feynman')
# --- simuladores
for dc in S.select('.dc'):
    fn = dc.get('data-fn') or ''
    m = re.search(r'function\s+' + re.escape(fn) + r'\s*\([^)]*\)\s*\{', scripts) if fn else None
    if not m: err('simulador', f'.dc sin función definida: {fn or "(sin data-fn)"}')
    else:
        i, d = m.end(), 1
        while i < len(scripts) and d:
            d += {'{': 1, '}': -1}.get(scripts[i], 0); i += 1
        body = scripts[m.end():i]
        if not re.search(r'\bcf\b', body): warn('contrafactual', f'{fn}: la salida no termina en <span class="cf">Si … → …</span>')
        if re.search(r'num\(\s*dc\s*,\s*[\'"](?:peso|kg)[\'"]\s*\)', body) and 'Math.min' not in body: warn('tope', f'{fn}: dosis por peso sin tope: Math.min(dosis, máxima del adulto) y muestra el tope')
    if not dc.select_one('.out'): err('simulador', f'.dc {fn}: falta div.out')
    if not dc.select_one('.dc-t') or not txt(dc.select_one('.dc-t')).startswith('Simulador · Decisión clínica —'): err('simulador', f'.dc {fn}: div.dc-t «Simulador · Decisión clínica — …»')
    for c in dc.select('.chip'):
        if not c.get('data-g') or not c.get('data-v') or 'ch(this)' not in (c.get('onclick') or ''): err('simulador', f'.dc {fn}: chip con data-g, data-v y onclick="ch(this)"')
    for i2 in dc.select('input[type=number]'):
        if not i2.get('data-n') or 'ch(this)' not in (i2.get('oninput') or ''): err('simulador', f'.dc {fn}: input con data-n y oninput="ch(this)"')
DCT = [k for k in CONT if secs[k].select('.dc')]
if MODE == 'mono':
    for k in ('dx', 'tx', 'seg'):
        if k in secs and not secs[k].select('.dc'): err('simulador', f'{k}: falta Simulador · Decisión clínica')
    for k in DCT:
        if k not in ('dx', 'tx', 'seg'): warn('simulador', f'{k}: simulador fuera de pestaña de plan')
else:
    if 'vis' in secs:
        n = len(secs['vis'].select('.dc'))
        if not 1 <= n <= 3: err('simulador', f'vis: {n} simuladores (1–3 diferenciales)')
        elif 'predic' not in txt(secs['vis'].select_one('.dc')).lower(): warn('simulador', 'vis: el rótulo del diferencial debe pedir predecir antes de pulsar')
    if 'sin' in secs and secs['sin'].select('.dc'): err('simulador', 'sin: sin simuladores')
# --- ids y contrato m↔s
ids = [t.get('id') for t in S.find_all(id=True)]
dup = sorted({i for i in ids if ids.count(i) > 1})
if dup: err('ids', f'ids duplicados: {dup}')
where = {}
for s in secl:
    for t in s.find_all(id=True): where[t['id']] = s.get('data-tab')
nodos, signos = S.select('.nodo'), S.select('.signo')
seq = {}
for el, kd, home in [(n, 'm', 'fis') for n in nodos] + [(g, 's', 'cli') for g in signos]:
    i = el.get('id', ''); k = (el.find_parent('section', class_='tab') or {}).get('data-tab')
    m = IDRE.match(i)
    pref = f'{k}-' if MODE == 'multi' else ''
    if MODE == 'mono' and k != home: err('ids', f'{i or kd}: {"nodos" if kd == "m" else "signos"} solo en {home}')
    if MODE == 'multi' and k not in ENT: err('ids', f'{i or kd}: {"nodos" if kd == "m" else "signos"} solo en pestañas eK')
    if not m or m.group(2) != kd: err('ids', f'id inválido «{i}» en {k}: usa «{pref}{kd}-n»'); continue
    if (m.group(1) or '') + ('-' if m.group(1) else '') != pref:
        err('ids', f'id «{i}» en la sección {k}: ' + (f'el prefijo debe ser «{k}-» → «{k}-{kd}-{m.group(3)}»' if MODE == 'multi' else f'mono sin prefijo → «{kd}-{m.group(3)}»'))
    seq.setdefault((k, kd), []).append(int(m.group(3)))
for (k, kd), ns in seq.items():
    if ns != list(range(1, len(ns) + 1)):
        p = f'{k}-' if MODE == 'multi' else ''
        err('ids', f'{k}: numeración {kd} {ns} → {p}{kd}-1…{p}{kd}-{len(ns)} consecutiva en orden DOM')
for k, s in secs.items():
    for o in s.select('ol.tl'):
        if o.parent is not s: err('timeline', f'{k}: cada ol.tl debe ser hija directa de la section')
    if len(s.select('li.nodo')) != len(s.select('ol.tl > li.nodo')) or len(s.select('.nodo')) != len(s.select('li.nodo')): err('timeline', f'{k}: todo .nodo es <li class="nodo"> hijo directo de ol.tl')
if MODE == 'mono' and 'fis' in secs and not secs['fis'].select('ol.tl'): err('timeline', 'fis: falta ol.tl')
for n in nodos:
    i = n.get('id')
    if n.get('data-clin') not in ('0', '1'): err('nodos', f'{i}: data-clin="0|1"')
    if not n.get('data-paso'): err('nodos', f'{i}: data-paso ausente (≤8 palabras, frase del ejercicio Ordenar)')
    if not n.select_one('.det'): err('nodos', f'{i}: falta div.det')
    if n.select('.paso'): err('nodos', f'{i}: no escribas .paso; lo genera el kit')
    if n.select('.nodo'): err('nodos', f'{i}: nodo anidado (timeline plana; usa data-rama)')
for t in nodos + signos:
    if t.find_parent(class_='acc'): err('ids', f'{t.get("id")} dentro de acordeón')
links = {}
for x in S.select('.xref'):
    tgt = x.get('data-ir'); oc = (x.get('onclick') or '').strip()
    if not tgt or tgt not in where: err('enlaces', f'xref a id inexistente: {tgt}'); continue
    ex = f"ir('{where[tgt]}','{tgt}')"
    if oc != ex: err('enlaces', f'xref {tgt}: onclick="{oc}" → onclick="{ex}"')
    src = (x.find_parent('section', class_='tab') or {}).get('data-tab')
    if MODE == 'multi' and src in ENT and where[tgt] in ENT and src != where[tgt]:
        err('enlaces', f'{src}: xref a {tgt} (otra entidad): los enlaces m↔s son intra-entidad; el contraste va en vis')
    own = x.find_parent(class_=['nodo', 'signo'])
    if own is not None and own.get('id'): links.setdefault(own['id'], []).append(tgt)
for n in nodos:
    Ls = [t for t in links.get(n.get('id'), []) if kind(t) == 's']
    if n.get('data-clin') == '1':
        if not Ls: err('enlaces', f'{n.get("id")} (data-clin="1") sin xref a signo en p.man')
        mn = n.select_one('.man')
        if not mn: err('enlaces', f'{n.get("id")} (data-clin="1") sin <p class="man">Se manifiesta como: …</p>')
        elif mn.select('.xref') != [x for x in n.select('.xref') if kind(x.get('data-ir')) == 's']: warn('enlaces', f'{n.get("id")}: xref a signos fuera de p.man')
    if len(Ls) > 3: err('enlaces', f'{n.get("id")}: {len(Ls)} xref a signos (máx 3)')
for g in signos:
    Lm = [t for t in links.get(g.get('id'), []) if kind(t) == 'm']
    if not Lm and 'Mecanismo no establecido' not in txt(g): err('enlaces', f'{g.get("id")}: sin xref a su nodo (o p.mini «Mecanismo no establecido»)')
    if len(Lm) > 2: err('enlaces', f'{g.get("id")}: {len(Lm)} xref a nodos (máx 2)')
    if len(g.select('dt')) < 3: err('signos', f'{g.get("id")}: ficha con menos de 3 dt')
for a, Lx in links.items():
    for b in Lx:
        if kind(a) and kind(b) and kind(a) != kind(b) and a not in links.get(b, []): err('reciprocidad', f'enlace no recíproco {a}→{b}: añade en {b} un xref a {a}')
# --- pasos etiquetados
DX = ['1.º', 'Añade', 'Confirma', 'Solo si', 'No pidas', 'Alarma']
TX = ['Principio', 'De elección', 'Alternativa', 'Sintomático', 'Escala', 'Reevalúa', 'Especialista', 'Evita']
DOSE = re.compile(r'\d+(?:[.,]\d+)?\s*(?:mg|µg|μg|mcg|g|UI|mL|ml)(?:/kg)?(?!\w)(?!/d?L\b)')
TGL = {}
for o in S.select('ol.tg'):
    k, g = grp(o) if MODE == 'multi' else ((o.find_parent('section', class_='tab') or {}).get('data-tab'), None)
    if 'steps' not in (o.get('class') or []): err('pasos', f'{k}: usa <ol class="steps tg">')
    if MODE == 'mono': ctx = {'dx': 'dx', 'tx': 'tx'}.get(k)
    else: ctx = 'dx' if k == 'vis' or g == 'Diagnóstico' else ('tx' if g == 'Tratamiento' else None)
    lab = f'{k}' + (f'/{g}' if g else '')
    if not ctx: err('pasos', f'{lab}: ol.steps.tg solo en ' + ('dx y tx' if MODE == 'mono' else 'vis, «Diagnóstico» y «Tratamiento»')); continue
    V, O = (DX, TX) if ctx == 'dx' else (TX, DX)
    got = []
    for li in o.find_all('li', recursive=False):
        first = next((c for c in li.contents if not (isinstance(c, str) and not c.strip())), None)
        if not (isinstance(first, Tag) and first.name == 'span' and 'tg' in (first.get('class') or [])):
            err('pasos', f'{lab}: cada <li> empieza por <span class="tg">…</span> sin texto previo'); continue
        t = txt(first); got.append(t)
        dp = (li.get('data-paso') or '').strip()
        if not dp: err('pasos', f'{lab}: <li> sin data-paso (frase clave ≤10 palabras para Ordenar)')
        elif words(dp) > 10: err('pasos', f'{lab}: data-paso de {words(dp)} palabras (≤10): «{dp[:40]}»')
        if t in V: pass
        elif t in O: err('pasos', f'{lab}: «{t}» es etiqueta {"tx" if ctx == "dx" else "dx"}; aquí: {" · ".join(V)}')
        elif nz(t) in {nz(v) for v in V}:
            v = next(v for v in V if nz(v) == nz(t)); err('pasos', f'{lab}: etiqueta «{t}» → escribe literal «{v}»' + (' (º es U+00BA)' if v == '1.º' else ''))
        else: err('pasos', f'{lab}: etiqueta «{t}» fuera del vocabulario {ctx}: {" · ".join(V)}')
        dm = DOSE.search(txt(li))
        if dm: err('pasos', f'{lab}: dosis «{dm.group(0)}» en la lista: nombra el fármaco y remite a la tabla (fuente única)')
    key = '1.º' if ctx == 'dx' else 'De elección'
    if got.count(key) != 1: err('pasos', f'{lab}: {got.count(key)} pasos «{key}» (exactamente 1)')
    TGL.setdefault((k, ctx), set()).update(got)
if MODE == 'mono':
    for k in ('dx', 'tx'):
        if k in secs and not secs[k].select('ol.steps.tg'): err('pasos', f'{k}: falta <ol class="steps tg"> al inicio (pasos etiquetados)')
elif 'vis' in secs and len(secs['vis'].select('ol.steps.tg')) != 1: err('pasos', 'vis: exactamente un <ol class="steps tg"> (diferencial, vocabulario dx)')
# --- Qué verás
for q in S.select('.qv'):
    k, g = grp(q) if MODE == 'multi' else ((q.find_parent('section', class_='tab') or {}).get('data-tab'), None)
    if MODE == 'mono' and k != 'cli': err('qv', f'{k}: .qv solo en cli')
    cs = kids(q)
    if any(c.name != 'p' or c.get('data-e') not in ('p', 'v', 'a', 'k') for c in cs): err('qv', f'{k}: .qv solo con <p data-e="p|v|a|k">')
    ek = [c for c in cs if c.get('data-e') == 'k']
    if len(ek) != 1: err('qv', f'{k}: .qv con {len(ek)} celdas data-e="k" (exactamente 1)')
    if len(cs) - len(ek) < 4: err('qv', f'{k}: .qv con {len(cs) - len(ek)} celdas de estado (mínimo 4)')
    for c in cs:
        if re.match(r'(Presente|Variable|Ausente|Signo clave)\b', txt(c), re.I): err('qv', f'{k}: no escribas el estado («{txt(c)[:20]}»): lo pone el CSS')
    if ek and not ek[0].select('.xref'): warn('qv', f'{k}: la celda k suele llevar xref a su ficha .signo')
# --- discrepancia
for h in S.select('.hb.vi'):
    cs = kids(h); t = [c for c in cs if 'hb-t' in (c.get('class') or [])]; p = [c for c in cs if c.name == 'p']
    if len(t) != 1 or len(p) != 1 or len(cs) != 2: err('discrepancia', 'hb vi: exactamente <div class="hb-t">Discrepancia: …</div><p>fuente → error → [n] → <b>regla</b></p>')
    if not CIT.search(txt(h)): err('discrepancia', 'hb vi sin cita [n]')
    if p and words(txt(p[0])) > 110: warn('discrepancia', f'hb vi: {words(txt(p[0]))} palabras (>110)')
    if p and not p[0].select('b,strong'): warn('discrepancia', 'hb vi: la regla correcta va en <b>')
# --- vis y sin (multi)
POS = {id(t): i for i, t in enumerate(S.find_all(True))}
if MODE == 'multi' and 'vis' in secs:
    v = secs['vis']; tv = v.select('table.vis')
    if len(tv) != 1: err('vis', f'vis: {len(tv)} table.vis (exactamente 1)')
    else:
        t = tv[0]
        if 'tw' not in (t.parent.get('class') or []): err('vis', 'table.vis dentro de <div class="tw">')
        tr = t.find_all('tr'); hc = [txt(c) for c in tr[0].find_all(['th', 'td'])] if tr else []
        exh = [name.get(k) for k in ENT]
        if hc[1:] != exh: err('vis', f'vis: cabeceras {hc[1:]} → textos de los botones {exh} (primera celda libre)')
        rows = t.select('tbody > tr') or tr[1:]
        if len(rows) != 9: err('vis', f'vis: {len(rows)} filas (las 9 del contrato, como preguntas)')
        for r in rows:
            cs = r.find_all(['th', 'td'])
            th0 = r.find('th')
            q, qx = (th0.select_one('span.q'), th0.select_one('span.qx')) if th0 and th0.parent is r else (None, None)
            if not q or not qx or not txt(qx): err('vis', f'vis: fila «{txt(cs[0])[:30] if cs else ""}»: th debe llevar span.q (pregunta) y span.qx (qué se busca)')
            elif not txt(q).rstrip().endswith('?'): err('vis', f'vis: pregunta «{txt(q)[:40]}» debe terminar en «?»')
            elif words(txt(qx)) > 15: warn('vis', f'vis: span.qx de {words(txt(qx))} palabras (≤15)')
            if len(cs) != N + 1: err('vis', f'vis: fila «{txt(cs[0]) if cs else ""}» con {len(cs)} celdas (N+1 = {N + 1})')
            for c in cs[1:]:
                if not txt(c): err('vis', f'vis: celda vacía en «{txt(cs[0])[:30]}»')
                elif words(txt(c)) > 12: warn('vis', f'vis: celda de {words(txt(c))} palabras en «{txt(cs[0])[:30]}» (≤12)')
    ro = v.select('.hb.ro')
    if not ro: err('vis', 'vis: falta hb ro (banderas rojas)')
    seqv = [v.select_one(x) for x in ('table.vis', '.hb.ro', 'ol.steps.tg', '.dc')]
    if all(seqv) and [POS[id(x)] for x in seqv] != sorted(POS[id(x)] for x in seqv): warn('vis', 'vis: orden tabla → hb ro → ol.steps.tg → simulador')
    if M and M.get('amenaza') in ENT and M.get('amenaza') != 'e1' and ro:
        am = M['amenaza']; f1 = next((x for x in ro[0].select('li,p') if 'hb-t' not in (x.get('class') or [])), None)
        if not f1 or name.get(am, '§') not in txt(f1): err('amenaza', f'vis: el primer ítem de hb ro debe nombrar la amenaza «{name.get(am)}»')
        if 'Alarma' not in TGL.get((am, 'dx'), set()): err('amenaza', f'{am} (amenaza ≠ e1): paso «Alarma» obligatorio en «Diagnóstico»')
        if 'Evita' not in TGL.get((am, 'tx'), set()): err('amenaza', f'{am} (amenaza ≠ e1): paso «Evita» obligatorio en «Tratamiento»')
if MODE == 'multi' and 'sin' in secs:
    ks = kids(secs['sin']); ok_ro = ok_rf = 0
    for c in ks:
        c_ = set(c.get('class') or [])
        if {'hb', 'ro'} <= c_ and c.select_one('.hb-t') and txt(c.select_one('.hb-t')).startswith('Errores que no se pueden cometer'): ok_ro += 1
        elif {'acc', 'refs'} <= c_: ok_rf += 1
        else: err('sin', f'sin: <{c.name} class="{cls(c)}"> no permitido; solo hb ro «Errores que no se pueden cometer» y .acc.refs (el kit pone los botones)')
    if ok_ro != 1: err('sin', 'sin: exactamente un <div class="hb ro"><div class="hb-t">Errores que no se pueden cometer</div>…')
for rf in S.select('.acc.refs'):
    k = (rf.find_parent('section', class_='tab') or {}).get('data-tab')
    if k != REFTAB: err('refs', f'.acc.refs en {k}: va en {REFTAB}')
if not S.select('.acc.refs'): err('refs', f'falta .acc.refs con ol.vanc en {REFTAB}')
# --- Vancouver
refs = S.select('ol.vanc > li'); seen = []
for k in CONT:
    for m in CIT.finditer(txt(secs[k])):
        for part in re.split(r'\s*,\s*', m.group(0)[1:-1]):
            a = re.split(r'\s*[–-]\s*', part)
            for n in range(int(a[0]), int(a[-1]) + 1):
                if n not in seen: seen.append(n)
bad = next((i for i, n in enumerate(seen) if n != i + 1), None)
if bad is not None: err('vancouver', f'primera cita fuera de orden: [{seen[bad]}] donde tocaba [{bad + 1}]; renumera por primera aparición (barra {" ".join(CONT)}; pan reutiliza)')
if len(refs) != len(seen): err('vancouver', f'lista Vancouver: {len(refs)} ítems vs {len(seen)} citas')
if pan and any(int(x) > len(refs) for x in re.findall(r'\[(\d+)\]', txt(pan))): err('vancouver', 'Panorama cita un número inexistente')
# --- orden de apertura, Feynman en def (mono), remisiones y posología fuera de tabla
if MODE == 'mono' and 'def' in secs and len(secs['def'].select('.fey')) != 1: err('feynman', f'def: {len(secs["def"].select(".fey"))} Feynman (exactamente 1)')
for k in CONT:
    if MODE == 'multi' and k in ENT + ['sin']: continue
    c0 = next(iter(kids(secs[k])), None)
    if c0 is not None and not ({'hb', 'az'} <= set(c0.get('class') or []) and c0.select_one('ol.pg')):
        warn('orden', f'{k}: la primera caja debe ser el hb az de preguntas guía (sin highlight previo)')
for r in S.select('span.rem'):
    k, g = grp(r) if MODE == 'multi' else ((r.find_parent('section', class_='tab') or {}).get('data-tab'), None)
    mt = re.search(r'«([^»]+)»', txt(r))
    if not mt or not k: continue
    tg_ = mt.group(1).strip()
    if tg_ == name.get(k) or (g and tg_ == g): err('remision', f'{k}{"/" + g if g else ""}: «{txt(r)}» apunta a la propia pestaña → <span class="rem">↓ En la tabla</span>')
for k in ['pan'] + CONT:
    if k not in secs: continue
    cp = BeautifulSoup(str(secs[k]), 'html.parser')
    for x in cp.select('.dc,.out,script,code,ol.tg,.acc.refs'): x.decompose()
    for tb in cp.select('table'): tb.decompose()  # umbrales en tablas de criterios no son posología
    dm = DOSE.search(txt(cp))
    if dm: warn('posologia', f'{k}: posología fuera de la tabla de fármacos («{dm.group(0)}»): remite con span.rem')
# --- palabras por pestaña (aviso; umbrales no calibrados)
LIM = {'vis': 1200, 'e1': 2800} if MODE == 'multi' else {}
WC = {k: words(txt(secs[k])) - sum(words(txt(x)) for x in secs[k].select('.acc.refs,.out')) for k in CONT}
for k in CONT:
    lim = LIM.get(k, 1200 if MODE == 'multi' else 2500)
    if WC[k] > lim: warn('palabras', f'{k}: {WC[k]} palabras (>{lim}): lo común va una vez en vis; recorta repeticiones')
    if MODE == 'multi' and k in ENT and k != 'e1' and WC.get('e1') and WC[k] > 0.8 * WC['e1']: warn('palabras', f'{k}: {WC[k]} palabras >80 % de e1 ({WC["e1"]}): la secundaria es delta, no monografía')
# --- clases
_here = os.path.dirname(os.path.abspath(__file__))
_hp = next((q for q in (os.path.join(_here, 'head.html'), os.path.join(_here, '..', 'kit_head.html')) if os.path.exists(q)), None)
css = open(_hp, encoding='utf-8').read() if _hp else ' '.join(s.string or '' for s in S.find_all('style'))
known = set(re.findall(r'\.([a-zA-Z][\w-]*)', css)) | {'rama', 'refs'}
# contrato §10 (por si head.html aún no las trae) y clases generadas por el script
known |= {'nucleo', 'nucleo-t', 'perla', 'perla-t', 'q', 'qx', 'ord', 'ord-bank', 'ord-slots', 'ord-chip', 'ord-slot', 'ord-ok', 'ord-ko', 'ord-btns', 'side', 'bottom', 'perla-filtro'}
for t in L.find_all(class_=True):
    for c in t['class']:
        if c not in known: warn('clases', f'.{c} sin CSS en el kit')
# --- v11: núcleo, perlas, diagramas, tablas
VALEX = {'puce', 'caces', 'usmle1', 'usmle2', 'mir', 'enarm'}
for k in CONT:
    if MODE == 'multi' and k == 'sin': continue
    s = secs[k]; nus = s.select('div.nucleo')
    if len(nus) != 1: err('nucleo', f'{k}: {len(nus)} div.nucleo (exactamente 1, tras las preguntas guía)')
    else:
        nu_ = nus[0]; kk = kids(nu_); ul = [c for c in kk if c.name == 'ul']
        if not (nu_.parent is s or top_of(nu_, s) is not None): pass
        if not kk or kk[0].name != 'div' or 'nucleo-t' not in (kk[0].get('class') or []) or len(ul) != 1 or len(kk) != 2:
            err('nucleo', f'{k}: estructura <div class="nucleo"><div class="nucleo-t">Núcleo</div><ul><li>…</li></ul></div>')
        else:
            lis = ul[0].find_all('li', recursive=False)
            if not 3 <= len(lis) <= 5: err('nucleo', f'{k}: núcleo con {len(lis)} ideas (3–5)')
            for li in lis:
                if words(txt(li)) > 35: warn('nucleo', f'{k}: idea del núcleo de {words(txt(li))} palabras (≤35): «{txt(li)[:30]}…»')
        pgs_ = s.select('ol.pg')
        if pgs_ and POS[id(nu_)] < POS[id(pgs_[0])]: err('nucleo', f'{k}: el núcleo va después de la caja de preguntas guía')
    if not s.select('aside.perla'): warn('perlas', f'{k}: sin ninguna perla de examen (aside.perla)')
for i, a in enumerate(S.select('aside.perla'), 1):
    k = (a.find_parent('section', class_='tab') or {}).get('data-tab')
    codes = (a.get('data-ex') or '').split()
    if not codes: err('perlas', f'{k}: perla {i} sin data-ex'); 
    elif not set(codes) <= VALEX: err('perlas', f'{k}: perla {i}: data-ex {codes} fuera de {sorted(VALEX)}')
    if not a.select_one('div.perla-t'): err('perlas', f'{k}: perla {i} sin div.perla-t')
    if not a.find('p'): err('perlas', f'{k}: perla {i} sin <p> con el dato')
for i, f in enumerate(S.select('figure.dg'), 1):
    if not (f.select_one('.dg-t') and f.select_one('.dg-row') and f.find('figcaption')): err('diagramas', f'figure.dg #{i}: falta dg-t, dg-row o figcaption')
for tb in S.select('table'):
    hs = [txt(h) for h in tb.select('thead th')] or [txt(h) for h in (tb.find('tr') or tb).find_all('th')]
    if hs and hs[0].startswith('Sección del DSM-5-TR'): err('tablas', 'tabla-índice «Sección del DSM-5-TR» prohibida (v11 las quita)')
    if hs and hs[0] == 'Fármaco' and 'Mecanismo de acción' not in hs: err('farmacos', 'tabla de fármacos sin columna «Mecanismo de acción»: ' + ' · '.join(hs))
# --- manifiesto
if MODE == 'mono':
    cnt = {'tabs': tbs, 'pg': {k: len(secs[k].select('ol.pg > li')) for k in CONT if secs[k].select('ol.pg > li')}, 'fey': {k: len(secs[k].select('.fey')) for k in CONT if secs[k].select('.fey')},
           'nodos': len(nodos), 'signos': len(signos), 'dc': DCT}
else:
    cnt = {'entidades': {k: name[k] for k in ENT}, 'tabs': tbs, 'pg': {k: len(secs[k].select('ol.pg > li')) for k in CONT if secs[k].select('ol.pg > li')},
           'fey': {k: len(secs[k].select('.fey')) for k in CONT if secs[k].select('.fey')}, 'nodos': {k: len(secs[k].select('.nodo')) for k in ENT if k in secs},
           'signos': {k: len(secs[k].select('.signo')) for k in ENT if k in secs}, 'dc': DCT}
if M is not None:
    ALL = ['modo', 'entidades', 'principal', 'amenaza', 'tabs', 'pg', 'fey', 'nodos', 'signos', 'dc', 'nucleo', 'dg', 'tema']
    for key in M:
        if key not in ALL and key not in ('titulo', 'salida', 'tipo'): err('manifiesto', f'clave desconocida "{key}" (permitidas: {", ".join(ALL)})')
    req = [x for x in ALL if x not in ('dg', 'tema')] if MODE == 'multi' else ['tabs', 'pg', 'fey', 'nodos', 'signos', 'dc']
    for key in req:
        if key not in M: err('manifiesto', f'falta la clave "{key}"')
    if MODE == 'mono' and 'nucleo' not in M: warn('manifiesto', 'falta "nucleo" (lista ≤12)')
    for key in ('pg', 'fey'):
        if isinstance(M.get(key), dict):
            for k in M[key]:
                if k not in CONT: err('manifiesto', f'{key}: clave "{k}" no es pestaña de contenido ({", ".join(CONT)})')
            if {k: v for k, v in M[key].items() if v != 0} == {k: v for k, v in cnt[key].items() if v}: M[key] = cnt[key]
    # v10.2 (manifiesto con "dg"): diagramas por pestaña, columna de mecanismo de acción y cero marcas de verificación
    TEMAS = ['ginecologia', 'salud-mental', 'digestivo', 'urologia', 'pediatria-ortopedia']
    if M.get('tema') is not None and M['tema'] not in TEMAS: warn('manifiesto', f'"tema":"{M["tema"]}" no tiene acento propio ({", ".join(TEMAS)}): usará azul')
    if M.get('tema') is None: warn('manifiesto', 'falta "tema" (acento del widget)')
    for key, v in cnt.items():
        if key in M and M[key] != v: err('manifiesto', f'{key}: manifiesto {json.dumps(M[key], ensure_ascii=False)} ≠ HTML {json.dumps(v, ensure_ascii=False)}')
    if MODE == 'multi':
        if 'principal' in M and M['principal'] != 'e1': err('manifiesto', f'"principal":"{M["principal"]}" → "principal":"e1" (la principal es e1 por convención)')
        if 'amenaza' in M and M['amenaza'] not in ENT: err('manifiesto', f'"amenaza":"{M["amenaza"]}" no es una entidad ({", ".join(ENT)})')
    nu = M.get('nucleo')
    def hay(el): return txt(el) + ' ' + ' '.join(n.get('data-paso', '') for n in el.select('[data-paso]'))
    if nu is not None:
        if MODE == 'mono':
            if not isinstance(nu, list) or len(nu) > 12 or not all(isinstance(x, str) for x in nu): err('nucleo', 'mono: "nucleo" lista de ≤12 cadenas')
            else:
                for x in nu:
                    if nz(x) not in nz(hay(S)): warn('nucleo', f'«{x}» no aparece en el widget')
        else:
            if not isinstance(nu, dict) or sorted(k for k in nu if k != 'vis') != sorted(ENT): err('nucleo', f'multi: "nucleo" objeto con claves {ENT} (+ "vis" opcional)')
            else:
                for k, lst in nu.items():
                    mx = 5 if k == 'vis' else 7
                    if not isinstance(lst, list) or len(lst) > mx: err('nucleo', f'{k}: núcleo con {len(lst) if isinstance(lst, list) else "?"} ítems (≤{mx})')
                    else:
                        for x in lst:
                            if nz(str(x)) not in nz(hay(secs.get(k, S)) + ' ' + hay(secs.get('vis', S))): warn('nucleo', f'{k}: «{x}» no aparece en {k} ni en vis')
# --- salida (≤25 líneas)
cnt.pop('dg', None)
print(json.dumps(cnt, ensure_ascii=False, separators=(',', ':'))[:400])
ne, nw = sum(map(len, E.values())), sum(map(len, W.values()))
def cut(s, n=400): return s if len(s) <= n else s[:n - 1] + '…'
wl = [cut(f'AVISO [{c}] ×{len(v)}: ' + ' | '.join(v[:3]) + (f' | +{len(v) - 3} más' if len(v) > 3 else ''), 300) for c, v in W.items()]
el = [f'ERROR [{c}]: {m}' for c, v in E.items() for m in v]
if len(el) + len(wl) > 23: el = [cut(f'ERROR [{c}] ×{len(v)}: ' + ' ‖ '.join(v)) for c, v in E.items()]
out = el + wl
if len(out) > 23: out = out[:22] + [f'… {len(out) - 22} líneas más omitidas (corrige y reejecuta)']
for x in out: print(x)
print(f'RESULTADO: {"OK" if not E else "FALLA"} · errores {ne} · avisos {nw} · JS {js_ok} · modo {MODE}')
sys.exit(1 if E else 0)
