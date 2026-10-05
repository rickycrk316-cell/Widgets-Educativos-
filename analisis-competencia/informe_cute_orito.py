"""Informe comparativo cute_quito vs oritorepublik.ec (Reels y Carruseles, últimos 7 días).
Los datos de Windsor se guardan en datos_informe.json y de ahí se genera el PDF."""
import json
from pathlib import Path
from datetime import date

D = Path(__file__).parent
rows = json.loads((D / "datos_informe.json").read_text())

def tipo(r):
    if r["media_type"] == "CAROUSEL_ALBUM": return "Carrusel"
    if r["media_type"] in ("VIDEO", "REEL") or r["media_product_type"] == "REELS": return "Reel"
    return None

items = []
for r in rows:
    t = tipo(r)
    if t:
        l, c = r["media_like_count"], r["media_comments_count"]
        items.append(dict(cuenta=r["account_name"], tipo=t, likes=l, com=c, imp=l + c, link=r["media_permalink"], fecha=(r.get("media_timestamp") or "")[:10]))
items.sort(key=lambda x: -x["imp"])

def resumen(cuenta):
    xs = [i for i in items if i["cuenta"] == cuenta]
    out = dict(n=len(xs), imp=sum(i["imp"] for i in xs), likes=sum(i["likes"] for i in xs), com=sum(i["com"] for i in xs))
    out["prom"] = out["imp"] / len(xs) if xs else 0
    for t in ("Reel", "Carrusel"):
        ts = [i for i in xs if i["tipo"] == t]
        out[t] = (len(ts), sum(i["imp"] for i in ts) / len(ts) if ts else 0)
    out["cero_likes"] = sum(1 for i in xs if i["likes"] == 0)
    return out

cuentas = ["oritorepublik.ec", "cute_quito"]
R = {c: resumen(c) for c in cuentas}
win = items[0]
win_c = {c: next(i for i in items if i["cuenta"] == c) for c in cuentas}

def fmt(n): return f"{n:,.0f}".replace(",", ".")
def tabla(xs, mostrar_fecha):
    h = "<tr><th>#</th><th>Cuenta</th><th>Tipo</th>" + ("<th>Fecha</th>" if mostrar_fecha else "") + "<th class=n>Likes</th><th class=n>Coment.</th><th class=n>Impacto</th><th>Link</th></tr>"
    b = ""
    for k, i in enumerate(xs, 1):
        b += f"<tr><td>{k}</td><td>@{i['cuenta']}</td><td>{i['tipo']}</td>" + (f"<td>{i['fecha']}</td>" if mostrar_fecha else "") + f"<td class=n>{fmt(i['likes'])}</td><td class=n>{fmt(i['com'])}</td><td class=n><b>{fmt(i['imp'])}</b></td><td><a href='{i['link']}'>{i['link'].replace('https://www.instagram.com/','')}</a></td></tr>"
    return f"<table>{h}{b}</table>"

o, c = R["oritorepublik.ec"], R["cute_quito"]
mult = o["prom"] / c["prom"] if c["prom"] else 0
html = f"""<!doctype html><html lang=es><meta charset=utf-8><style>
@page{{size:A4;margin:16mm 14mm}}
body{{font:11px/1.45 'Helvetica Neue',Arial,sans-serif;color:#222}}
h1{{font-size:22px;margin:0 0 2px}} h2{{font-size:14px;margin:18px 0 6px;border-bottom:1px solid #ccc;padding-bottom:3px}}
.sub{{color:#666;margin-bottom:10px}}
.win{{background:#f4f1ea;border-left:4px solid #a31a0e;padding:9px 12px;margin:8px 0}}
table{{border-collapse:collapse;width:100%;margin:6px 0;font-size:10px}}
th,td{{padding:3px 5px;border-bottom:1px solid #e3e3e3;text-align:left}} th{{background:#f0f0f0}}
.n{{text-align:right}} a{{color:#1a4fa3;text-decoration:none}}
.note{{color:#555;font-size:10px}} ul{{margin:4px 0 4px 16px;padding:0}}
</style>
<h1>Análisis de competencia en Instagram</h1>
<div class=sub>@oritorepublik.ec y @cute_quito · últimos 7 días · Reels y Carruseles · generado el {date.today():%d/%m/%Y} · fuente: Windsor.ai (instagram_public)<br>Impacto Total = likes + comentarios. Se excluyen las fotos simples.</div>

<h2>Pieza ganadora</h2>
<div class=win><b>{win['tipo']}</b> de <b>@{win['cuenta']}</b> con <b>{fmt(win['imp'])}</b> de Impacto Total ({fmt(win['likes'])} likes + {fmt(win['com'])} comentarios).<br><a href='{win['link']}'>{win['link']}</a></div>
<div class=win><b>Mejor pieza de @cute_quito:</b> {win_c['cute_quito']['tipo']} con <b>{fmt(win_c['cute_quito']['imp'])}</b> de Impacto ({fmt(win_c['cute_quito']['likes'])} likes + {fmt(win_c['cute_quito']['com'])} comentarios) · <a href='{win_c['cute_quito']['link']}'>{win_c['cute_quito']['link']}</a></div>

<h2>Comparación por cuenta</h2>
<table><tr><th>Cuenta</th><th class=n>Publicaciones</th><th class=n>Impacto total</th><th class=n>Impacto promedio</th><th class=n>Reels (n · prom.)</th><th class=n>Carruseles (n · prom.)</th></tr>
<tr><td>@oritorepublik.ec</td><td class=n>{o['n']}</td><td class=n>{fmt(o['imp'])}</td><td class=n>{fmt(o['prom'])}</td><td class=n>{o['Reel'][0]} · {fmt(o['Reel'][1])}</td><td class=n>{o['Carrusel'][0]} · {fmt(o['Carrusel'][1])}</td></tr>
<tr><td>@cute_quito</td><td class=n>{c['n']}</td><td class=n>{fmt(c['imp'])}</td><td class=n>{fmt(c['prom'])}</td><td class=n>{c['Reel'][0]} · {fmt(c['Reel'][1])}</td><td class=n>{c['Carrusel'][0]} · {fmt(c['Carrusel'][1])}</td></tr></table>

<h2>Lo que muestran los datos</h2><ul>
<li>@oritorepublik.ec publicó {o['n']} piezas y sumó {fmt(o['imp'])} de impacto; @cute_quito publicó {c['n']} y sumó {fmt(c['imp'])}. Por pieza, oritorepublik.ec rinde unas {mult:.0f} veces más ({fmt(o['prom'])} contra {fmt(c['prom'])} de promedio).</li>
<li>En @oritorepublik.ec los carruseles rinden más del doble que los reels ({fmt(o['Carrusel'][1])} contra {fmt(o['Reel'][1])} de promedio). Los 3 primeros puestos del ranking general son carruseles suyos.</li>
<li>@cute_quito publica casi todo en reels ({c['Reel'][0]} de {c['n']}), pero su promedio por reel es de {fmt(c['Reel'][1])} y su promedio por carrusel de {fmt(c['Carrusel'][1])}. Con solo {c['Carrusel'][0]} carruseles, la comparación entre formatos en esta cuenta es poco firme.</li>
<li>El impacto de @cute_quito está concentrado: sus 3 mejores piezas (dos reels y un carrusel) suman unos 7 de cada 10 puntos de su impacto total.</li>
</ul>

<h2>Advertencias sobre los datos</h2><ul>
<li><b>@cute_quito:</b> {c['cero_likes']} de sus {c['n']} piezas aparecen con 0 likes, y varias de ellas tienen comentarios (por ejemplo un reel con 23 comentarios y 0 likes). Eso puede ser que la cuenta oculte los likes o que Windsor no los entregue; no tengo cómo saber cuál. Por eso su impacto probablemente está subestimado.</li>
<li><b>@oritorepublik.ec</b> ya no está disponible en tu conector de Windsor (ahora solo están pinkrosetk y cute_quito). Sus datos son los que descargué antes, en la misma ventana de 7 días, y no incluyen fecha de publicación.</li>
<li><b>@pinkrosetk</b> sigue sin datos: Windsor devuelve error de extracción para esa cuenta (<i>retry_later</i>).</li>
<li>Los números son una foto del momento: las piezas más recientes siguen acumulando likes y comentarios.</li></ul>

<h2>Ranking completo (ordenado por Impacto Total)</h2>
{tabla(items, False)}
<div class=note>Tipo: Carrusel = CAROUSEL_ALBUM; Reel = video publicado como REELS.</div>
</html>"""
(D / "Informe_Competencia_cute_orito.html").write_text(html, encoding="utf-8")

print("HTML listo:", len(items), "piezas. PDF: node html_a_pdf.js")
