#!/usr/bin/env python3
"""Auditoría del orquestador: ¿el widget respeta el kit Vademécum y las reglas de diseño del PLAN?
Uso: python3 auditar_diseno.py widget.html manifiesto.json "Modo: … (línea del router esperada)" [modo_entidades_json]
Sale con código 1 si hay fallas (FALLA); los AVISO no bloquean."""
import sys, re, json, pathlib, unicodedata
from bs4 import BeautifulSoup, Tag

KIT = pathlib.Path(__file__).resolve().parent
html_path, man_path, router = sys.argv[1], sys.argv[2], sys.argv[3]
H = pathlib.Path(html_path).read_text(encoding='utf-8')
F, W = [], []
fail = F.append
warn = W.append

A, B = '<!-- /KIT_HEAD -->', '<!-- KIT_SCRIPT -->'
head, rest = H.split(A, 1)
llm, script = rest.split(B, 1)
kh = (KIT / 'kit_head.html').read_text(encoding='utf-8')
kh_expected = re.sub(r'<title>@@TITULO@@</title>', re.search(r'<title>.*?</title>', head, re.S).group(0), kh).split(A)[0]
if head != kh_expected:
    fail('kit: el kit_head del widget no es el kit Vademécum (fue editado o es el kit antiguo)')
if B + script != (KIT / 'kit_script.html').read_text(encoding='utf-8'):
    fail('kit: kit_script editado')

# 1 · solo clases del contrato
css_js = kh + (KIT / 'kit_script.html').read_text(encoding='utf-8')
allowed = set(re.findall(r'\.([a-zA-Z][\w-]*)', css_js)) | set(re.findall(r"className\s*=\s*'([^']+)'", css_js))
allowed = {c for x in allowed for c in x.split()}
allowed |= {'det', 'refs', 'tg', 'steps', 'pg', 'vanc', 'vis', 'rec-go'}
S = BeautifulSoup(llm, 'html.parser')
used = {c for t in S.find_all(class_=True) for c in t.get('class')}
extra = sorted(used - allowed)
if extra: fail(f'regla 1: clases fuera del kit: {extra}')
if re.search(r'<[a-zA-Z][^>]*\sstyle\s*=', llm) or '<style' in llm: fail('regla 1: estilos inline o <style> en las partes')

# 2 · tablas con thead/th/tbody dentro de .tw
for i, t in enumerate(S.find_all('table'), 1):
    sec = (t.find_parent('section') or {}).get('data-tab', '?')
    if not t.find('thead') or not t.find('thead').find('th'): fail(f'regla 2: tabla {i} ({sec}) sin <thead> con <th>')
    if not t.find('tbody'): fail(f'regla 2: tabla {i} ({sec}) sin <tbody>')
    if not (t.parent and 'tw' in (t.parent.get('class') or [])): fail(f'regla 2: tabla {i} ({sec}) fuera de div.tw')

# 3 · recuadros anidados
for c in S.select('.card'):
    p = c.find_parent(class_=['card', 'hb', 'fey'])
    if p: fail(f'regla 3: .card anidada dentro de .{" .".join(p.get("class"))} ({(c.find_parent("section") or {}).get("data-tab")})')
for h in S.select('.hb'):
    if h.find_parent(class_='hb'): fail('regla 3: .hb dentro de .hb')

def words(s): return re.findall(r"[\wáéíóúñü%/\-]+", s, re.I)
def txt(e): return re.sub(r'\s+', ' ', e.get_text(' ')).strip()

# 4 · títulos en tipo oración; hb-t ≤8 palabras salvo literales de la skill
LIT = ('Preguntas guía', 'Frente a', 'Errores que no se pueden cometer', 'Precisión sobre el sílabo', 'Discrepancia', 'El grupo en una frase', 'El tema en una frase', 'Alcance', 'Antes de cerrar')
for e in S.select('h1,h2,h3,h4,.hb-t,.dc-t,.fey-t'):
    t = txt(e); ws = [w for w in words(t) if w.isalpha() and len(w) > 3]
    if len(ws) >= 2 and all(w.isupper() for w in ws): fail(f'regla 4: título en MAYÚSCULAS: «{t[:60]}»')
    small = [w for w in ws[1:] if w[0].islower()]
    if len(ws) >= 4 and not small: warn(f'regla 4: posible Título De Cada Palabra: «{t[:60]}»')
for e in S.select('.hb-t'):
    t = txt(e)
    if not t.startswith(LIT) and len(words(t)) > 8: fail(f'regla 4: hb-t de {len(words(t))} palabras (>8): «{t[:70]}»')

# 5 · párrafos ≤90 palabras
CIT = re.compile(r'\[\d+(?:\s*[,–-]\s*\d+)*\]')
for p in S.find_all('p'):
    if set(p.get('class') or []) & {'res', 'fey-b'}: continue  # conteos propios de la skill (regla 10)
    n = len(words(CIT.sub('', txt(p))))
    if n > 90: fail(f'regla 5: párrafo de {n} palabras en {(p.find_parent("section") or {}).get("data-tab")}: «{txt(p)[:60]}…»')

# 6 · negrita con propósito
for p in S.find_all('p'):
    if len(p.find_all(['b', 'strong'])) > 1: warn(f'regla 6: {len(p.find_all(["b","strong"]))} negritas en un párrafo: «{txt(p)[:50]}…»')
for tb in S.find_all('tbody'):
    for tr in tb.find_all('tr'):
        for td in tr.find_all(['td', 'th'])[1:]:
            if td.find(['b', 'strong']): warn(f'regla 6: negrita en celda de cuerpo: «{txt(td)[:40]}»'); break

# 7 · redacción
body = txt(S)
for m in re.finditer(r'.{0,30}[!¡].{0,20}', body): fail(f'regla 7: signo de exclamación: «{m.group(0)}»')
for w in ['cabe destacar', 'es importante mencionar', 'en el mundo de', 'sin lugar a dudas', 'vale la pena', 'en resumen,', 'cabe mencionar']:
    if w in body.lower(): fail(f'regla 7: muletilla «{w}»')

# 8 · emojis / pictogramas
EMO = re.compile('[\U0001F300-\U0001FAFF\U0001F000-\U0001F2FF✀-➿☀-⛿⭐✅❌]')
for m in EMO.finditer(body):
    if m.group(0) != '⚠': fail(f'regla 8: pictograma {m.group(0)!r} (U+{ord(m.group(0)):04X})')

# 9 · coma decimal
for m in re.finditer(r'(?<![\w.\[/-])(\d+)\.(\d+)(?!\.\d)(?![\w/])', body):
    a, b2 = m.group(1), m.group(2)
    if len(a) <= 3 and len(b2) <= 2 and not (len(a) == 4): warn(f'regla 9: posible punto decimal «{m.group(0)}»')

# router
M = json.loads(pathlib.Path(man_path).read_text(encoding='utf-8'))
txtman = json.dumps(M, ensure_ascii=False)
exp_mode = re.search(r'Modo:\s*(\w+)', router).group(1)
if M.get('modo') != exp_mode: fail(f'router: modo {M.get("modo")} ≠ {exp_mode}')
ents = re.findall(r'e\d=([^·,(]+?)(?:\s*\(principal\))?(?=,\s*e\d=|\s*·)', router)
if exp_mode == 'multi':
    got = [M.get('entidades', {}).get(f'e{i}') for i in range(1, len(ents) + 1)]
    for i, (a, b2) in enumerate(zip(ents, got), 1):
        if (b2 or '').strip() != a.strip(): fail(f'router: e{i} «{b2}» ≠ plan «{a.strip()}»')
    am = re.search(r'Amenaza:\s*(e\d)', router)
    if am and M.get('amenaza') != am.group(1): fail(f'router: amenaza {M.get("amenaza")} ≠ {am.group(1)}')

print('\n'.join('FALLA ' + x for x in F)); print('\n'.join('AVISO ' + x for x in W))
print(f'AUDITORÍA: {"FALLA" if F else "OK"} · fallas {len(F)} · avisos {len(W)}')
sys.exit(1 if F else 0)
