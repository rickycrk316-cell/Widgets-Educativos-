#!/usr/bin/env python3
"""Numera citas [@CLAVE] por primera aparición (orden alfabético de partes = orden de barra)
y sustituye <!--REFS--> por los <li> Vancouver de refs.json.
Uso: python3 citar.py <carpeta_widget> [--prueba]
  --prueba: copia la carpeta a ../_tmp_<id>/ (salida ../_tmp_<id>.html), numera ahí y construye. No toca el original.
  sin --prueba: numera en el sitio (solo el orquestador, al final).
"""
import sys, re, json, shutil, pathlib, subprocess
aquí = pathlib.Path(__file__).resolve().parent
refs = json.loads((aquí/'refs.json').read_text(encoding='utf-8'))
d = pathlib.Path(sys.argv[1]).resolve(); prueba = '--prueba' in sys.argv
if prueba:
    t = d.parent/f'_tmp_{d.name}'
    if t.exists(): shutil.rmtree(t)
    shutil.copytree(d, t); m = json.loads((t/'manifiesto.json').read_text(encoding='utf-8'))
    m['salida'] = f'../_tmp_{d.name}.html'; (t/'manifiesto.json').write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding='utf-8'); d = t
partes = sorted(d.glob('*.html')); orden = []
# Panorama (02_pan) reutiliza números: la primera aparición se cuenta desde vis.
for p in [x for x in partes if not x.name.startswith('02_pan')] + [x for x in partes if x.name.startswith('02_pan')]:
    for k in re.findall(r'\[@([A-Z0-9_]+)\]', p.read_text(encoding='utf-8')):
        if k not in orden: orden.append(k)
mal = [k for k in orden if k not in refs]
if mal: sys.exit(f'ERROR claves desconocidas: {mal}')
num = {k: i+1 for i, k in enumerate(orden)}
lis = '\n'.join(f'<li>{refs[k]}</li>' for k in orden)
nrefs = 0
for p in partes:
    s = p.read_text(encoding='utf-8')
    s2 = re.sub(r'\[@([A-Z0-9_]+)\]', lambda mm: f'[{num[mm.group(1)]}]', s)
    if '<!--REFS-->' in s2: s2 = s2.replace('<!--REFS-->', lis); nrefs += 1
    if s2 != s: p.write_text(s2, encoding='utf-8')
print(f'citas: {len(orden)} referencias; bloque REFS sustituido en {nrefs} parte(s)')
for k in orden: print(f'  [{num[k]}] {k}')
if nrefs != 1: print('AVISO: debe haber exactamente un <!--REFS--> (dentro de ol.vanc)')
if prueba:
    r = aquí.parents[1]/'kit'/'construir.py'
    subprocess.run([sys.executable, str(r), str(d)])
