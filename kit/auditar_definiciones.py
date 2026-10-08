#!/usr/bin/env python3
"""Auditoría del orquestador para el widget de definiciones (skill definiciones v5.1 + cabecera Vademécum).
Uso: python3 auditar_definiciones.py widget.html N_TERMINOS"""
import sys, re, pathlib
from bs4 import BeautifulSoup

KIT = pathlib.Path(__file__).resolve().parent
H = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
NT = int(sys.argv[2])
F, W = [], []
fail, warn = F.append, W.append

head = (KIT / 'def_head.html').read_text(encoding='utf-8')
MK = '<!-- /DEF_HEAD -->'
if MK not in H:
    fail('cabecera: falta la marca <!-- /DEF_HEAD --> (no se usó def_head.html)')
    hpart, body = '', H
else:
    hpart, body = H.split(MK, 1)
    exp = re.sub(r'<title>@@TITULO@@</title>', re.search(r'<title>.*?</title>', hpart, re.S).group(0), head).split(MK)[0]
    if hpart != exp: fail('cabecera: def_head.html editada')
if body.count('<style') or re.search(r'<[a-zA-Z][^>]*\sstyle\s*=', body): fail('regla 1: estilos propios o inline')

S = BeautifulSoup(body, 'html.parser')
allowed = set(re.findall(r'\.([a-zA-Z][\w-]*)', head)) | {'active', 'op'}
used = {c for t in S.find_all(class_=True) for c in t.get('class')}
js = '\n'.join(s.string or '' for s in S.find_all('script'))
used |= set(re.findall(r"classList\.(?:add|toggle|remove)\('([\w-]+)'", js))
used |= {c for m in re.findall(r'class="([^"]+)"', js) for c in m.split()}
used |= {c for m in re.findall(r"className\s*=\s*'([^']+)'", js) for c in m.split()}
extra = sorted(c for c in used - allowed if not re.search(r"[+'\"$]", c))
if extra: fail(f'regla 1: clases fuera de def_head: {extra}')

tabs = S.select('section.tab')
btns = S.select('nav.tabs button.tb')
if len(tabs) != NT + 1: fail(f'pestañas: {len(tabs)} secciones; se esperaban {NT} términos + Repaso global')
if len(btns) != len(tabs): fail(f'pestañas: {len(btns)} botones ≠ {len(tabs)} secciones')
for t in tabs[:-1]:
    tid = t.get('id')
    if not t.select_one('.hb'): fail(f'{tid}: falta idea rectora (.hb)')
    if not t.select_one('.card.fey'): fail(f'{tid}: falta card Feynman')
    if not t.select_one('.card.ej'): fail(f'{tid}: falta ejemplo de anclaje')
    if not t.select_one('.rc'): fail(f'{tid}: falta simulador de recall')
    if not t.select_one('.acc.no'): warn(f'{tid}: sin acordeón «No confundir con…» marcado .acc.no')
    if not t.select_one('.gloss'): warn(f'{tid}: sin glosario de siglas (.gloss)')
    if not (t.select_one('.pre') or t.select_one('.rem-line')): warn(f'{tid}: sin prerrequisitos ni remisión (¿omisión declarada?)')
    for a in t.select('.pre .acc'):
        if 'op' not in (a.get('class') or []): fail(f'{tid}: acordeón de prerrequisito no nace abierto')
last = tabs[-1] if tabs else None
if last is not None and not last.select_one('ol.vanc'): fail('Repaso global: falta ol.vanc (Vancouver)')

for i, tb in enumerate(S.find_all('table'), 1):
    if not tb.find('thead') or not tb.find('thead').find('th'): fail(f'regla 2: tabla {i} sin thead/th')
    if not tb.find('tbody'): fail(f'regla 2: tabla {i} sin tbody')
    if not (tb.parent and 'tw' in (tb.parent.get('class') or [])): fail(f'regla 2: tabla {i} fuera de .tw')
for c in S.select('.card'):
    if c.find_parent(class_=['card', 'hb', 'pre']): fail('regla 3: .card anidada')

def txt(e): return re.sub(r'\s+', ' ', e.get_text(' ')).strip()
def words(s): return re.findall(r"[\wáéíóúñü%/\-]+", s, re.I)
for e in S.select('h1,h2,h3,.hb-t,.card-t,.pre-t,.rc-t,.acc-h'):
    ws = [w for w in words(txt(e)) if w.isalpha() and len(w) > 3]
    if len(ws) >= 2 and all(w.isupper() for w in ws): fail(f'regla 4: título en MAYÚSCULAS «{txt(e)[:50]}»')
CIT = re.compile(r'\[\d+(?:\s*[,–-]\s*\d+)*\]')
for p in S.find_all('p'):
    if p.find_parent(class_='fey'): continue
    n = len(words(CIT.sub('', txt(p))))
    if n > 90: fail(f'regla 5: párrafo de {n} palabras «{txt(p)[:50]}…»')
    if len(p.find_all(['b', 'strong'])) > 1: warn(f'regla 6: {len(p.find_all(["b","strong"]))} negritas en «{txt(p)[:40]}…»')
visible = txt(S) + ' ' + js
for m in re.finditer(r'.{0,25}[!¡].{0,15}', txt(S)): fail(f'regla 7: exclamación «{m.group(0)}»')
EMO = re.compile('[\U0001F300-\U0001FAFF\U0001F000-\U0001F2FF✀-➿☀-⛿⭐✅❌]')
for m in set(EMO.findall(visible)): fail(f'regla 8: pictograma {m!r} U+{ord(m):04X}')
for bad in ['localStorage', 'sessionStorage', 'position: fixed', 'position:fixed', '[resto', 'continúa -->', 'TODO', 'placeholder', 'TSV', 'Exportar a Anki', '<img', 'src="http']:
    if bad in body: fail(f'skill: cadena prohibida «{bad}»')
if re.search(r'(?<!\.)\.\.\.(?!\.)', txt(S)): fail('skill: «...» ASCII en el texto')
for fn in ['rc_render', 'rc_show', 'rc_grade', 'rc_end', 'rc_reset']:
    n = len(re.findall(r'function\s+' + fn + r'\s*\(', js))
    if n != 1: fail(f'skill: motor de recall: {fn} definida {n} veces (debe ser 1)')
if 'DECKS' not in js: fail('skill: falta const DECKS')

print('\n'.join('FALLA ' + x for x in F)); print('\n'.join('AVISO ' + x for x in W))
print(f'AUDITORÍA DEFINICIONES: {"FALLA" if F else "OK"} · fallas {len(F)} · avisos {len(W)}')
sys.exit(1 if F else 0)
