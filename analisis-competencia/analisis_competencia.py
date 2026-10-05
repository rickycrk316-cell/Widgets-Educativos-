"""Análisis de competencia en Instagram (datos públicos vía Windsor.ai).

Descarga las publicaciones de los últimos 7 días, conserva solo Reels y
Carruseles, calcula el Impacto Total (likes + comentarios) y escribe
Analisis_Competencia.md ordenado de mayor a menor impacto.

Uso:
    export WINDSOR_API_KEY=...        # no guardes la clave en el repositorio
    python3 analisis_competencia.py
"""
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

BASE_URL = "https://connectors.windsor.ai/instagram_public"
FIELDS = [
    "account_name", "media_permalink", "media_product_type", "media_type",
    "media_like_count", "media_comments_count", "likes_per_post", "comments_per_post",
]
ACCOUNTS = ["oritorepublik.ec", "pinkrosetk"]  # cuentas conectadas en Windsor
OUT = Path(__file__).with_name("Analisis_Competencia.md")
TIMEOUT = 300


def fetch(api_key, account=None):
    params = {"date_preset": "last_7d", "fields": ",".join(FIELDS), "api_key": api_key}
    if account:
        params["select_accounts"] = f"instagram_public__{account}"
    url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT) as r:
            payload = json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            raise RuntimeError(f"HTTP {e.code}: {body[:200]}") from None
    # Windsor devuelve {"data": [...]} o, en algunos casos, la lista directa.
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("data"), list):
        return payload["data"]
    raise RuntimeError(payload.get("error", str(payload)[:200]) if isinstance(payload, dict) else str(payload)[:200])


def download(api_key):
    """Intenta todas las cuentas juntas; si falla, cuenta por cuenta."""
    errors = {}
    try:
        return fetch(api_key), errors
    except Exception as e:  # una cuenta caída tumba la descarga conjunta
        print(f"Descarga conjunta falló: {e}. Pruebo cuenta por cuenta.", file=sys.stderr)
    rows = []
    for acc in ACCOUNTS:
        for intento in range(2):
            try:
                rows += fetch(api_key, acc)
                errors.pop(acc, None)
                break
            except Exception as e:
                errors[acc] = str(e)
                time.sleep(5)
    return rows, errors


def num(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return 0


def tipo(row):
    mt = (row.get("media_type") or "").upper()
    pt = (row.get("media_product_type") or "").upper()
    if mt == "CAROUSEL_ALBUM":
        return "Carrusel"
    if mt in ("VIDEO", "REEL") or pt == "REELS":
        return "Reel"
    return None  # IMAGE simple u otro: se ignora


def procesar(rows):
    vistos = {}
    for row in rows:
        t = tipo(row)
        link = row.get("media_permalink")
        if not t or not link:
            continue
        likes = num(row.get("media_like_count", row.get("likes_per_post")))
        coment = num(row.get("media_comments_count", row.get("comments_per_post")))
        item = {
            "cuenta": row.get("account_name") or "",
            "link": link, "tipo": t, "likes": likes, "comentarios": coment,
            "impacto": likes + coment,
        }
        # Windsor puede repetir una publicación por día; nos quedamos con el valor más alto.
        if link not in vistos or item["impacto"] > vistos[link]["impacto"]:
            vistos[link] = item
    return sorted(vistos.values(), key=lambda x: x["impacto"], reverse=True)


def escribir(items, errores):
    L = [f"# Análisis de competencia en Instagram", "",
         f"Periodo: últimos 7 días · generado el {date.today():%d/%m/%Y} · fuente: Windsor.ai (instagram_public)",
         "Solo Reels y Carruseles. Impacto Total = likes + comentarios.", ""]
    if errores:
        L += ["> Cuentas sin datos por error de la API: "
              + "; ".join(f"**{a}** ({e[:120]})" for a, e in errores.items()), ""]
    if not items:
        L += ["No hay Reels ni Carruseles en el periodo para las cuentas disponibles."]
    else:
        g = items[0]
        L += ["## Pieza ganadora", "",
              f"**{g['tipo']}** de @{g['cuenta']} con **{g['impacto']:,}** de Impacto Total "
              f"({g['likes']:,} likes + {g['comentarios']:,} comentarios).", "",
              f"Link: {g['link']}", "",
              "## Ranking", "",
              "| # | Cuenta | Tipo | Likes | Comentarios | Impacto Total | Link |",
              "|---:|---|---|---:|---:|---:|---|"]
        for i, it in enumerate(items, 1):
            L.append(f"| {i} | @{it['cuenta']} | {it['tipo']} | {it['likes']:,} | {it['comentarios']:,} "
                     f"| **{it['impacto']:,}** | [ver]({it['link']}) |")
        reels = [x for x in items if x["tipo"] == "Reel"]
        carr = [x for x in items if x["tipo"] == "Carrusel"]
        prom = lambda xs: sum(x["impacto"] for x in xs) / len(xs) if xs else 0
        L += ["", "## Reels vs. Carruseles", "",
              "| Tipo | Publicaciones | Impacto promedio |", "|---|---:|---:|",
              f"| Reel | {len(reels)} | {prom(reels):,.0f} |",
              f"| Carrusel | {len(carr)} | {prom(carr):,.0f} |"]
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")


def main():
    api_key = os.environ.get("WINDSOR_API_KEY")
    if not api_key:
        sys.exit("Falta la variable de entorno WINDSOR_API_KEY.")
    rows, errores = download(api_key)
    items = procesar(rows)
    escribir(items, errores)
    print(f"{len(rows)} filas descargadas, {len(items)} Reels/Carruseles. Archivo: {OUT}")
    if errores:
        print(f"Cuentas con error: {', '.join(errores)}", file=sys.stderr)


if __name__ == "__main__":
    main()
