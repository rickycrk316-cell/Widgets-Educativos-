#!/usr/bin/env python3
"""Genera kit/v12/head.html a partir de head.src.html + fuentes/*.woff2 (base64) + ornamentos SVG (data URI).

Uso: python3 kit/v12/generar_head.py
head.html se versiona ya generado (construir.py solo lo lee); edita head.src.html y vuelve a generar.
"""
import base64, pathlib, re, urllib.parse

AQUI = pathlib.Path(__file__).resolve().parent

# --- tipografías incrustadas (subconjunto latino, WOFF2) -------------------------------------------------
FUENTES = [
    ('Cinzel', 'normal', '400 700', 'cinzel-600.woff2'),
    ('EB Garamond', 'normal', '400 500', 'garamond-400.woff2'),
    ('EB Garamond', 'normal', '600 700', 'garamond-600.woff2'),
    ('EB Garamond', 'italic', '400 600', 'garamond-400i.woff2'),
    ('IM Fell English', 'italic', '400', 'fell-italic.woff2'),
]


def fontface():
    out = []
    for fam, estilo, peso, f in FUENTES:
        b = base64.b64encode((AQUI / 'fuentes' / f).read_bytes()).decode()
        out.append(f'@font-face{{font-family:"{fam}";font-style:{estilo};font-weight:{peso};font-display:swap;'
                   f'src:url(data:font/woff2;base64,{b}) format("woff2")}}')
    return '\n'.join(out)


# --- ornamentos: (claro, oscuro) = colores de trazo ----------------------------------------------------
TINTA = ('#5a4632', '#d9c79c')      # pluma / líneas de construcción
ORO = ('#b8862b', '#d6a94a')
SANG = ('#8f3a1e', '#e6916f')
VETA = ('#c9bda3', '#3a4856')


def svg(cuerpo, w, h, extra=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" {extra}>'
            f'{cuerpo}</svg>')


def uri(s):
    return 'url("data:image/svg+xml,' + urllib.parse.quote(s, safe="/:=' ,.-()") + '")'


def ornamentos(m):  # m = 0 claro, 1 oscuro
    t, o, s, v = TINTA[m], ORO[m], SANG[m], VETA[m]
    d = {}
    # greca (meandro): tira de 12 px de alto
    d['greca'] = svg(f'<path d="M0 11.2H28M2 11.2V1.2H14V8.2H6V4.6H10M16 11.2V1.2H28V8.2H20V4.6H24" fill="none" stroke="{o}" stroke-width="1.3" stroke-linejoin="miter"/>', 28, 12)
    # frontón: triángulo + arquitrabe, se estira al ancho
    d['fronton'] = svg(f'<polyline points="0,15 50,1.5 100,15" fill="none" stroke="{o}" stroke-width="1.3" vector-effect="non-scaling-stroke"/>'
                       f'<line x1="0" y1="15.4" x2="100" y2="15.4" stroke="{o}" stroke-width="1.3" vector-effect="non-scaling-stroke"/>',
                       100, 16, 'preserveAspectRatio="none"')
    # acanaladuras de columna (tira vertical)
    d['flautas'] = svg(f'<rect x="1" y="0" width="1.5" height="8" fill="{v}"/><rect x="4.5" y="0" width="1" height="8" fill="{v}"/><rect x="7.5" y="0" width="1.5" height="8" fill="{v}"/>', 10, 8)
    # sol dorado: disco + rayos
    rayos = ''.join(f'<line x1="50" y1="6" x2="50" y2="{14 if i % 2 else 20}" transform="rotate({i * 15} 50 50)"/>' for i in range(24))
    d['sol'] = svg(f'<g fill="none" stroke="{o}" stroke-width="1.4"><circle cx="50" cy="50" r="19"/><circle cx="50" cy="50" r="14" stroke-width=".7"/>{rayos}</g>', 100, 100)
    # hombre de Vitruvio simplificado: cuadrado, círculo, ejes, diagonales, marcas de proporción
    ticks = ''.join(f'<line x1="{x}" y1="9" x2="{x}" y2="12"/><line x1="{x}" y1="88" x2="{x}" y2="91"/>' for x in range(10, 91, 10))
    d['vitruvio'] = svg(f'<g fill="none" stroke="{t}" stroke-width=".7"><rect x="12" y="12" width="76" height="76"/><circle cx="50" cy="56" r="38"/>'
                        f'<circle cx="50" cy="56" r="38" stroke-width=".4" stroke-dasharray="1.5 2.5" transform="translate(0 -6)"/>'
                        f'<line x1="50" y1="4" x2="50" y2="96"/><line x1="4" y1="50" x2="96" y2="50"/>'
                        f'<line x1="12" y1="12" x2="88" y2="88" stroke-width=".4"/><line x1="88" y1="12" x2="12" y2="88" stroke-width=".4"/>{ticks}</g>', 100, 100)
    # estrella de ocho puntas para perlas
    d['estrella'] = svg(f'<path d="M8 0L9.6 6.4L16 8L9.6 9.6L8 16L6.4 9.6L0 8L6.4 6.4Z" fill="{s}"/>', 16, 16)
    # cuadrícula de proporción para diagramas
    d['cuadricula'] = svg(f'<path d="M0 .5H24M.5 0V24" stroke="{v}" stroke-width=".6" fill="none" opacity=".55"/>', 24, 24)
    # grano de pergamino (ruido) y mármol (vetas)
    if m == 0:
        d['grano'] = ('<svg xmlns="http://www.w3.org/2000/svg" width="220" height="220"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="7" stitchTiles="stitch"/>'
                      '<feColorMatrix values="0 0 0 0 .40  0 0 0 0 .28  0 0 0 0 .12  0 0 0 .75 -.28"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>')
        d['vena'] = ('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200"><filter id="v"><feTurbulence type="fractalNoise" baseFrequency=".0025 .011" numOctaves="2" seed="11" stitchTiles="stitch"/>'
                     '<feColorMatrix values="0 0 0 0 .62  0 0 0 0 .55  0 0 0 0 .42  0 0 0 .40 -.17"/></filter><rect width="100%" height="100%" filter="url(#v)"/></svg>')
    else:
        d['grano'] = ('<svg xmlns="http://www.w3.org/2000/svg" width="220" height="220"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="7" stitchTiles="stitch"/>'
                      '<feColorMatrix values="0 0 0 0 .85  0 0 0 0 .75  0 0 0 0 .55  0 0 0 .45 -.18"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>')
        d['vena'] = ('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1200"><filter id="v"><feTurbulence type="fractalNoise" baseFrequency=".0025 .011" numOctaves="2" seed="11" stitchTiles="stitch"/>'
                     '<feColorMatrix values="0 0 0 0 .35  0 0 0 0 .45  0 0 0 0 .55  0 0 0 .22 -.09"/></filter><rect width="100%" height="100%" filter="url(#v)"/></svg>')
    return d


NOMBRES = ['greca', 'fronton', 'flautas', 'sol', 'vitruvio', 'estrella', 'cuadricula', 'grano', 'vena']


def urls(m):
    o = ornamentos(m)
    return ''.join(f'--u-{n}:{uri(o[n])};' for n in NOMBRES)


# --- tema oscuro (noche egea: tinta sobre pizarra) ------------------------------------------------------
OSCURO_BASE = ('--bg:#10171d;--surface:#18222b;--surface-2:#1f2b36;--ink:#efe6d0;--ink-2:#cfc5ac;--ink-3:#a69d88;--line:#2c3945;--line-2:#43535f;'
               '--marmol:#10171d;--marmol-2:#1f2b36;--veta:#2c3945;--oro:#d6a94a;--egeo:#52b3c4;--laurel:#a7bb6e;--sanguina:#e6916f;--tinta:#efe6d0;--tinta-2:#cfc5ac;'
               '--am:#e8c27a;--am-f:#2e2412;--ro:#ff9d93;--ro-f:#361a18;--ve:#b5cf84;--ve-f:#1e2a15;--pu:#aab8e8;--pu-f:#1e2440;--co:#efae8c;--co-f:#33211a;--rs:#eea0bd;--rs-f:#33192a;'
               '--accent:#e6916f;--accent-ink:#f0a98c;--accent-field:#2b2320;--on-accent:#1a0f0a;'
               '--nota:#2d261a;--nota-2:#3d3322;--nota-l:#322a1c;--nota-borde:#cdb67f;--nota-lin:rgba(217,199,156,.7);--nota-sombra:rgba(0,0,0,.45);--nota-ink:#f1e7cf;'
               '--sh:0 0 0 1px rgba(255,255,255,.02);--sh-up:0 8px 22px rgba(0,0,0,.5);color-scheme:dark;')

TEMAS = {  # tema: (claro: acento, ink, campo) · (oscuro: acento, ink, campo, sobre-acento)
    'pediatria-ortopedia': (('#1f5d8e', '#1f5d8e', '#dde9f1'), ('#7bbbe8', '#a3d0f0', '#14293a', '#06192a')),
    'ginecologia': (('#8f2a4b', '#8f2a4b', '#f4e1e6'), ('#ee8aa8', '#f4a9c0', '#331a25', '#3a0a1f')),
    'salud-mental': (('#3b4a8a', '#3b4a8a', '#e3e6f1'), ('#9fb0f0', '#bcc8f6', '#1d2340', '#101640')),
    'digestivo': (('#146577', '#146577', '#dcebed'), ('#5fc4d4', '#8ad8e4', '#12292e', '#04202a')),
    'urologia': (('#7f5410', '#7f5410', '#f1e5c9'), ('#e3b25a', '#eecb85', '#2e2410', '#2b1a02')),
}


def temas_claro():
    return '\n'.join(f':root[data-tema="{k}"]{{--accent:{a};--accent-ink:{i};--accent-field:{f};--on-accent:#fbf6ea}}' for k, ((a, i, f), _) in TEMAS.items())


def temas_oscuro(sel):
    return '\n'.join(f'{sel}[data-tema="{k}"]{{--accent:{a};--accent-ink:{i};--accent-field:{f};--on-accent:{oa}}}' for k, (_, (a, i, f, oa)) in TEMAS.items())


def main():
    src = (AQUI / 'head.src.html').read_text(encoding='utf-8')
    oscuro = OSCURO_BASE + urls(1)
    rep = {
        '@@FONTS@@': fontface(),
        '@@URL_L@@': urls(0),
        '@@TEMAS_L@@': temas_claro(),
        '@@TEMAS_D1@@': temas_oscuro(':root:not([data-theme="light"])'),
        '@@TEMAS_D2@@': temas_oscuro(':root[data-theme="dark"]'),
        '@@DARK@@': oscuro,
    }
    for k, v in rep.items():
        src = src.replace(k, v)
    assert '@@' not in src.replace('@@TITULO@@', ''), 'marcador sin sustituir'
    (AQUI / 'head.html').write_text(src, encoding='utf-8')
    print(f'head.html: {len(src.encode()) / 1024:.1f} KB')


if __name__ == '__main__':
    main()
