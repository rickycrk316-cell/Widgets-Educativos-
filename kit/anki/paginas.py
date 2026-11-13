#!/usr/bin/env python3
"""Escribe páginas HTML que imitan el reviewer de Anki (anverso y reverso, claro y noche) para las
primeras N tarjetas de un tarjetas.json, o las de los IDs dados. Lo llama previsualizar.js; también sirve suelto.

Uso: python3 kit/anki/paginas.py <tarjetas.json> <dir_salida> [N] [--ids ID1,ID2]
Nombre de cada página: <ID>_<anverso|reverso>_<claro|noche>.html (el dispositivo lo fija el viewport);
un cloze genera una tarjeta por hueco: c1 conserva ese nombre, los demás son <ID>_c2_<anverso|…>.html.
"""
import json
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import modelo as M  # noqa: E402

# Reviewer de Anki (ts/reviewer/reviewer.scss, resumido): margen, imágenes y fondo nocturno.
REVIEWER = """
body { margin: 20px; overflow-wrap: break-word; }
body.nightMode { background-color: #2C2C2C; color: #FCFCFC; }
hr { background-color: #8a8a8a; margin: 1em 0; border: none; height: 1px; }
img { max-width: 100%; max-height: 95vh; }
"""


def pagina(cuerpo, noche):
    body = 'card card1' + (' nightMode night_mode' if noche else '')
    return ('<!doctype html><html class="mobile ios"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<style>{REVIEWER}</style><style>{M.CSS}</style></head><body class="{body}">{cuerpo}</body></html>')


def main():
    args = sys.argv[1:]
    ids = None
    if '--ids' in args:
        i = args.index('--ids')
        ids = [x for x in args[i + 1].split(',') if x]
        del args[i:i + 2]
    src, out = pathlib.Path(args[0]).resolve(), pathlib.Path(args[1]).resolve()
    n = int(args[2]) if len(args) > 2 else None
    out.mkdir(parents=True, exist_ok=True)
    todas = json.loads(src.read_text(encoding='utf-8'))['tarjetas']
    if ids:
        por_id = {c['id']: c for c in todas}
        faltan = [x for x in ids if x not in por_id]
        if faltan:
            sys.exit('IDs no encontrados: ' + ', '.join(faltan))
        cards = [por_id[x] for x in ids]
    else:
        cards = todas[:n]
    media = src.parent / 'media'
    if media.is_dir():
        for f in media.iterdir():
            shutil.copy(f, out / f.name)
    for c in cards:
        if c['tipo'] == 'Cloze':
            ordinales = sorted({int(m.group(1)) for m in M.CLOZE_RE.finditer(c['text'])}) or [1]
        else:
            ordinales = [1]
        for o in ordinales:
            frente, reverso = M.render_tarjeta(c, o)
            base = c['id'] if o == 1 else f'{c["id"]}_c{o}'
            for noche in (False, True):
                modo = 'noche' if noche else 'claro'
                (out / f'{base}_anverso_{modo}.html').write_text(pagina(frente, noche), encoding='utf-8')
                (out / f'{base}_reverso_{modo}.html').write_text(pagina(reverso, noche), encoding='utf-8')
    print(len(cards))


if __name__ == '__main__':
    main()
