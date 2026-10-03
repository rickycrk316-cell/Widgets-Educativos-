#!/usr/bin/env python3
"""Fase 2 · produce $V/elementos-canva/<cat>/ (SVG apto Canva + PNG) y verifica SVG vs original."""
import os, sys, re, json, shutil, subprocess
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_svg import convert, validate_apto
import elementos_def as D

S = '/tmp/claude-0/-home-user-Widgets-Educativos-/a4f9a5b0-9019-55e2-9489-b316b7cde1bb/scratchpad/atavio/elementos'
OUT = D.V + '/elementos-canva'
W = S + '/work'
BG = {'hueso': '#F3EDE1', 'tinta': '#2B2B2B', 'ladrillo': '#A31A0E', 'molde': '#C8A97E'}


def run_render(jobs, name):
    p = f'{W}/{name}.json'
    json.dump(jobs, open(p, 'w'))
    r = subprocess.run(['node', S + '/render2.js', p], capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(r.stderr)


def set_vb(s, vb):
    x, y, w, h = vb
    head = re.search(r'<svg[^>]*>', s).group(0)
    nh = re.sub(r'viewBox="[^"]*"', f'viewBox="{x:g} {y:g} {w:g} {h:g}"', head)
    nh = re.sub(r'\swidth="[^"]*"', f' width="{w:g}"', nh)
    nh = re.sub(r'\sheight="[^"]*"', f' height="{h:g}"', nh)
    if 'width=' not in nh:
        nh = nh.replace('<svg', f'<svg width="{w:g}" height="{h:g}"', 1)
    return s.replace(head, nh)


def fname(el, v):
    return f'atavio-{el.id}{v.suf}'


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.rmtree(W, ignore_errors=True)
    os.makedirs(W)
    items = []  # (el, var, cat)
    for el in D.ELEMS:
        for v in el.variants:
            items.append((el, v, el.cat))
    # pendiente (garantía)
    pend = D.El('icono-garantia', 'Icono: Garantía (PENDIENTE)', '_pendiente', 'Pendiente: no publicar hasta que la garantía esté redactada e impresa en caja.', '', D.PENDIENTE)
    for v in pend.variants:
        v.crop = ('icono', 'garantia', 'fino')
        items.append((pend, v, '_pendiente'))

    # --- fuentes originales
    for el, v, cat in items:
        if v.text is not None:
            o = v.text
        else:
            o = D.rd(v.src)
            if v.recolor:
                o = D.recolor(o)
        if v.crop and v.crop[0] == 'icono' and v.crop[2] == 'grueso':
            o = o.replace('stroke-width="7"', 'stroke-width="16"')
        v.orig = o

    # --- recortes de iconos (cuadrado centrado en 540,540 que contiene todo el trazo grueso + 24 px)
    probes, keys = [], []
    for el, v, cat in items:
        if v.crop and v.crop[0] == 'icono' and v.crop[2] in ('grueso', 'fino') and v.suf.endswith('claro'):
            if (v.crop[1] not in keys) and (v.crop[2] == 'grueso' or v.crop[1] == 'garantia'):
                keys.append(v.crop[1])
                p = f'{W}/probe-{v.crop[1]}.svg'
                open(p, 'w').write(v.orig.replace('stroke-width="7"', 'stroke-width="16"') if v.crop[1] == 'garantia' else v.orig)
                probes.append({'src': p, 'out': p[:-4] + '.png', 'scale': 1})
    run_render(probes, 'probes')
    crops = {}
    for k in keys:
        a = np.array(Image.open(f'{W}/probe-{k}.png'))[:, :, 3]
        ys, xs = np.where(a > 8)
        half = max(540 - xs.min(), xs.max() + 1 - 540, 540 - ys.min(), ys.max() + 1 - 540) + 24
        half = int(np.ceil(half / 4) * 4)
        crops[k] = (540 - half, 540 - half, 2 * half, 2 * half)
    for el, v, cat in items:
        if v.crop and v.crop[0] == 'icono':
            vb = crops[v.crop[1]]
            v.orig = set_vb(v.orig, vb)
            v.vb = vb

    # --- SVG aptos
    report = []
    for el, v, cat in items:
        v.file = fname(el, v)
        v.svg_ok = False
        v.info = {}
        title = f'Atavío · {el.nombre}' + (f' ({v.etiqueta})' if v.etiqueta and len(el.variants) > 1 else '')
        title = title.replace('—', '·')
        if v.apto:
            s, info = convert(v.orig, title)
            pr = validate_apto(s)
            v.info = info
            v.problems = pr
            if pr:
                print('PROBLEMA', v.file, pr)
                v.apto = False
            else:
                v.svg = s
                v.svg_ok = True
        if not v.svg_ok and not v.apto:
            v.svg = None

    # --- escribir SVG y fuentes de PNG
    pj, vj = [], []
    for el, v, cat in items:
        d = f'{OUT}/{cat}'
        os.makedirs(d, exist_ok=True)
        v.cat = cat
        if v.svg_ok:
            open(f'{d}/{v.file}.svg', 'w', encoding='utf-8').write(v.svg)
        src = f'{W}/{cat}__{v.file}.orig.svg'
        open(src, 'w', encoding='utf-8').write(v.orig)
        job = {'src': src, 'out': f'{d}/{v.file}.png'}
        if v.scale:
            job['scale'] = v.scale
        else:
            job['long'] = v.long
        pj.append(job)
        if v.svg_ok:
            a = f'{W}/{cat}__{v.file}.apto.svg'
            open(a, 'w', encoding='utf-8').write(v.svg)
            bg = BG[v.fondo]
            vj.append({'src': src, 'out': f'{W}/v_{cat}__{v.file}.o.png', 'long': 1800, 'bg': bg})
            vj.append({'src': a, 'out': f'{W}/v_{cat}__{v.file}.a.png', 'long': 1800, 'bg': bg})
    run_render(pj, 'png')
    run_render(vj, 'verify')

    # --- comparación
    worst = []
    for el, v, cat in items:
        if not v.svg_ok:
            continue
        o = np.array(Image.open(f'{W}/v_{cat}__{v.file}.o.png').convert('RGB')).astype(int)
        a = np.array(Image.open(f'{W}/v_{cat}__{v.file}.a.png').convert('RGB')).astype(int)
        bg = np.array([int(BG[v.fondo][i:i + 2], 16) for i in (1, 3, 5)])
        ink = int((np.abs(o - bg).max(axis=2) > 30).sum())
        df = np.abs(o - a).max(axis=2)
        d90 = int((df > 90).sum())
        v.diff = {'ink_px': ink, 'diff90_px': d90, 'diff90_pct_of_ink': round(100 * d90 / max(ink, 1), 3)}
        worst.append((v.diff['diff90_pct_of_ink'], v.file))
    worst.sort(reverse=True)
    print('peores diferencias (% de pixeles de tinta con diff>90):')
    for w in worst[:12]:
        print('  ', w)

    # --- estado
    png_only = [(v.file, v.nota) for el, v, cat in items if not v.svg_ok]
    print('Solo PNG:', len(png_only))
    for p in png_only:
        print('  ', p[0])
    n_svg = sum(1 for el, v, cat in items if v.svg_ok)
    print('SVG:', n_svg, 'PNG:', len(items), 'variantes; elementos:', len(D.ELEMS))
    json.dump({'items': [dict(file=v.file, cat=cat, el=el.id, diff=getattr(v, 'diff', None), info=v.info, svg=v.svg_ok) for el, v, cat in items],
               'crops': crops}, open(S + '/build-report.json', 'w'), indent=1)
    inv = []
    for el in D.ELEMS + [pend]:
        vs = []
        for v in el.variants:
            png = f'{OUT}/{v.cat}/{v.file}.png'
            w, h = Image.open(png).size
            vs.append({'archivo': v.file, 'etiqueta': v.etiqueta, 'fondo_recomendado': v.fondo,
                       'svg': (f'{v.cat}/{v.file}.svg' if v.svg_ok else None), 'png': f'{v.cat}/{v.file}.png', 'png_px': [w, h],
                       'modo': 'svg+png' if v.svg_ok else 'solo png', 'nota': v.nota,
                       'fuente': (os.path.relpath(v.src, D.V) if v.src else 'generado a partir de plantillas (gen_feed.py / vertical.py / HTML)'),
                       'puntadas_convertidas': v.info.get('stitches', 0) if v.info else 0,
                       'verificacion': getattr(v, 'diff', None)})
        inv.append({'id': el.id, 'nombre': el.nombre, 'categoria': el.cat, 'uso': el.uso, 'regla': el.regla, 'variantes': vs})
    json.dump({'version': 'v1.2', 'elementos': inv, 'descartados': D.DESCARTADOS,
               'nota': 'claro = para fondo hueso o molde; oscuro = para fondo tinta o ladrillo; costuras: ladrillo = fondo claro, hueso = fondo oscuro'},
              open(S + '/inventario.json', 'w'), indent=1, ensure_ascii=False)
    return items, pend


if __name__ == '__main__':
    main()
