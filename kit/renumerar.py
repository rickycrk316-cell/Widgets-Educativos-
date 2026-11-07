#!/usr/bin/env python3
"""Renumera las citas Vancouver [n] de un widget por orden de primera aparición.

Uso: python3 kit/renumerar.py widgets/<tema>/<id>

- Recorre las partes *.html en orden alfabético (el Panorama 02_pan, si existe, se cuenta al final:
  reutiliza números) y numera cada referencia por su primera cita.
- Reordena los <li> de la única ol.vanc del widget y quita los que nadie cita (los informa).
- Para añadir una referencia nueva: agrégala como último <li> de ol.vanc, cítala con el número que le
  toca (total + 1) y ejecuta este script.
"""
import re, sys, pathlib

d = pathlib.Path(sys.argv[1])
partes = sorted(d.glob('*.html'))
orden_lectura = [p for p in partes if not p.name.startswith('02_pan')] + [p for p in partes if p.name.startswith('02_pan')]
txt = {p: p.read_text(encoding='utf-8') for p in partes}
OL = re.compile(r'(<ol class="vanc">)(.*?)(</ol>)', re.S)
CITA = re.compile(r'(?<=[\s\]>(\'"])\[(\d+)\]')

con_ol = [p for p in partes if OL.search(txt[p])]
if len(con_ol) != 1:
    sys.exit(f'ERROR: debe haber exactamente una ol.vanc en las partes (hay {len(con_ol)})')
pol = con_ol[0]
m = OL.search(txt[pol])
items = re.findall(r'<li>.*?</li>', m.group(2), re.S)

vistos = []
for p in orden_lectura:
    s = txt[p]
    if p == pol:
        s = s[:m.start()] + s[m.end():]
    for n in CITA.findall(s):
        n = int(n)
        if n not in vistos:
            vistos.append(n)

fuera = [n for n in vistos if n < 1 or n > len(items)]
if fuera:
    sys.exit(f'ERROR: citas sin referencia en ol.vanc: {fuera} (la lista tiene {len(items)} ítems)')
mapa = {old: i + 1 for i, old in enumerate(vistos)}
huerfanas = [i + 1 for i in range(len(items)) if (i + 1) not in mapa]

for p in partes:
    s = txt[p]
    if p == pol:
        cab = CITA.sub(lambda x: f'[{mapa[int(x.group(1))]}]', s[:m.start()])
        cola = CITA.sub(lambda x: f'[{mapa[int(x.group(1))]}]', s[m.end():])
        nuevos = [items[old - 1] for old in vistos]
        s = cab + m.group(1) + '\n' + '\n'.join(nuevos) + '\n' + m.group(3) + cola
    else:
        s = CITA.sub(lambda x: f'[{mapa[int(x.group(1))]}]', s)
    if s != txt[p]:
        p.write_text(s, encoding='utf-8')

cambios = {o: n for o, n in mapa.items() if o != n}
print(f'renumerado: {len(vistos)} referencias citadas; {len(cambios)} cambiaron de número')
if huerfanas:
    print(f'AVISO: se quitaron {len(huerfanas)} referencias que nadie cita (números antiguos {huerfanas})')
