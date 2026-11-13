#!/usr/bin/env python3
"""Escribe páginas HTML que imitan el reviewer de Anki (anverso y reverso, claro y noche) para las
primeras N tarjetas de un tarjetas.json. Lo llama previsualizar.js; también sirve suelto.

Uso: python3 kit/anki/paginas.py <tarjetas.json> <dir_salida> [N]
Nombre de cada página: <ID>_<anverso|reverso>_<claro|noche>.html (el dispositivo lo fija el viewport).
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
    src, out = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
    n = int(sys.argv[3]) if len(sys.argv) > 3 else None
    out.mkdir(parents=True, exist_ok=True)
    cards = json.loads(src.read_text(encoding='utf-8'))['tarjetas'][:n]
    media = src.parent / 'media'
    if media.is_dir():
        for f in media.iterdir():
            shutil.copy(f, out / f.name)
    for c in cards:
        frente, reverso = M.render_tarjeta(c)
        for noche in (False, True):
            modo = 'noche' if noche else 'claro'
            (out / f'{c["id"]}_anverso_{modo}.html').write_text(pagina(frente, noche), encoding='utf-8')
            (out / f'{c["id"]}_reverso_{modo}.html').write_text(pagina(reverso, noche), encoding='utf-8')
    print(len(cards))


if __name__ == '__main__':
    main()
