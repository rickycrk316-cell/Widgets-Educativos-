#!/usr/bin/env python3
"""Generador de Lumen (biblioteca de widgets).

Lee biblioteca/estructura.json, los manifiestos de widgets/*/*/manifiesto.json,
las tablas del README.md, los PLAN.md, los sílabos, los casos y los mazos, y escribe
biblioteca/catalogo.js (window.CATALOGO). Con --sitio <dir> arma el sitio publicable.

Solo biblioteca estándar. Uso:
    python3 kit/biblioteca/generar.py
    python3 kit/biblioteca/generar.py --sitio _site
"""
import argparse
import datetime
import html
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ID_RE = re.compile(r"^[a-z0-9-]+$")
ACENTOS = {"ginecologia", "salud-mental", "digestivo", "urologia", "pediatria-ortopedia"}
ESTADOS = {"completo", "parcial", "pendiente"}
ORDEN_TIPO = {"definiciones": 0, "apertura": 1, "ensenanza": 2}


class Fallo(Exception):
    pass


# ---------------------------------------------------------------- Markdown mínimo

def _inline(texto):
    """Inline sobre texto crudo: escapa TODO el HTML y luego aplica el formato permitido."""
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", texto)  # imágenes fuera
    t = html.escape(t, quote=True)
    codigos = []

    def guarda(m):
        codigos.append("<code>%s</code>" % m.group(1))
        return "\x00%d\x00" % (len(codigos) - 1)

    t = re.sub(r"`([^`]+)`", guarda, t)
    t = re.sub(
        r"\[([^\]]+)\]\((https?://[^\s)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        t,
    )
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?![\s*])(.+?)(?<![\s*])\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(?<![\w_])_(?![\s_])(.+?)(?<![\s_])_(?![\w_])", r"<em>\1</em>", t)
    return re.sub(r"\x00(\d+)\x00", lambda m: codigos[int(m.group(1))], t)


def _celdas(linea):
    s = linea.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", s)]


RE_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
RE_HEAD = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
RE_HR = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")
RE_SEP = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")


def _es_inicio_bloque(linea, siguiente):
    return bool(
        RE_HEAD.match(linea)
        or RE_HR.match(linea)
        or RE_ITEM.match(linea)
        or linea.lstrip().startswith(("```", ">"))
        or (linea.lstrip().startswith("|") and siguiente is not None and RE_SEP.match(siguiente))
    )


def _lista(lineas, i):
    """Convierte una lista (con anidación por sangría) empezando en lineas[i]. Devuelve (html, i)."""
    items = []  # (indent, ordenada, [texto])
    n = len(lineas)
    while i < n:
        linea = lineas[i]
        m = RE_ITEM.match(linea)
        if m:
            sangria = len(m.group(1).expandtabs(4))
            items.append([sangria, m.group(2)[0].isdigit(), [m.group(3).strip()]])
            i += 1
            continue
        if not linea.strip():
            j = i + 1
            while j < n and not lineas[j].strip():
                j += 1
            if j < n and (RE_ITEM.match(lineas[j]) or (lineas[j].startswith((" ", "\t")) and items)):
                i = j
                continue
            break
        if linea.startswith((" ", "\t")) and items:
            items[-1][2].append(linea.strip())
            i += 1
            continue
        break

    def construir(pos, nivel_indent):
        partes = []
        ordenada = items[pos][1]
        while pos < len(items) and items[pos][0] >= nivel_indent:
            if items[pos][0] > nivel_indent:
                break
            sangria, _, textos = items[pos]
            pos += 1
            hijos = ""
            if pos < len(items) and items[pos][0] > sangria:
                hijos, pos = construir(pos, items[pos][0])
            partes.append("<li>%s%s</li>" % (_inline(" ".join(textos)), hijos))
        etiqueta = "ol" if ordenada else "ul"
        return "<%s>%s</%s>" % (etiqueta, "".join(partes), etiqueta), pos

    salida = []
    pos = 0
    while pos < len(items):
        bloque, pos = construir(pos, items[pos][0])
        salida.append(bloque)
    return "".join(salida), i


def md_a_html(texto, nivel_min=3, quitar_h1=False):
    """Markdown mínimo a HTML seguro. Los encabezados se reubican para empezar en h<nivel_min>."""
    lineas = texto.replace("\r\n", "\n").split("\n")
    # Primera pasada: bloques con el nivel original de encabezado.
    bloques = []  # ("h", nivel, texto) o ("html", str)
    i, n = 0, len(lineas)
    primera_h1 = True
    while i < n:
        linea = lineas[i]
        sig = lineas[i + 1] if i + 1 < n else None
        if not linea.strip():
            i += 1
            continue
        if re.match(r"^\s*<!--.*-->\s*$", linea):
            i += 1
            continue
        if linea.lstrip().startswith("```"):
            i += 1
            codigo = []
            while i < n and not lineas[i].lstrip().startswith("```"):
                codigo.append(lineas[i])
                i += 1
            i += 1
            bloques.append(("html", "<pre><code>%s</code></pre>" % html.escape("\n".join(codigo))))
            continue
        m = RE_HEAD.match(linea)
        if m:
            nivel = len(m.group(1))
            if quitar_h1 and nivel == 1 and primera_h1:
                primera_h1 = False
            else:
                bloques.append(("h", nivel, m.group(2)))
            i += 1
            continue
        if RE_HR.match(linea):
            bloques.append(("html", "<hr>"))
            i += 1
            continue
        if linea.lstrip().startswith("|") and sig is not None and RE_SEP.match(sig):
            cab = _celdas(linea)
            i += 2
            filas = []
            while i < n and lineas[i].strip().startswith("|"):
                filas.append(_celdas(lineas[i]))
                i += 1
            h = "<table><thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (
                "".join("<th>%s</th>" % _inline(c) for c in cab),
                "".join(
                    "<tr>%s</tr>" % "".join("<td>%s</td>" % _inline(c) for c in fila) for fila in filas
                ),
            )
            bloques.append(("html", '<div class="tabla">%s</div>' % h))
            continue
        if linea.lstrip().startswith(">"):
            citado = []
            while i < n and lineas[i].lstrip().startswith(">"):
                citado.append(re.sub(r"^\s*>\s?", "", lineas[i]))
                i += 1
            interno = md_a_html("\n".join(citado), nivel_min=6)
            bloques.append(("html", "<blockquote>%s</blockquote>" % interno))
            continue
        if RE_ITEM.match(linea):
            h, i = _lista(lineas, i)
            bloques.append(("html", h))
            continue
        parrafo = [linea.strip()]
        i += 1
        while i < n and lineas[i].strip() and not _es_inicio_bloque(lineas[i], lineas[i + 1] if i + 1 < n else None):
            parrafo.append(lineas[i].strip())
            i += 1
        h = _inline(" ".join(parrafo))
        if h.strip():
            bloques.append(("html", "<p>%s</p>" % h))
    niveles = [b[1] for b in bloques if b[0] == "h"]
    base = min(niveles) if niveles else nivel_min
    salida = []
    for b in bloques:
        if b[0] == "h":
            nivel = min(6, b[1] - base + nivel_min)
            salida.append("<h%d>%s</h%d>" % (nivel, _inline(b[2]), nivel))
        else:
            salida.append(b[1])
    return "\n".join(salida)


# ---------------------------------------------------------------- utilidades

def normaliza(texto):
    s = unicodedata.normalize("NFD", texto.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip()


def leer(ruta):
    return Path(ruta).read_text(encoding="utf-8")


def fragmento_silabo(archivo, ancla):
    """Texto Markdown bajo el encabezado cuyo texto es `ancla`, hasta el siguiente de nivel igual o superior."""
    ruta = RAIZ / archivo
    if not ruta.is_file():
        raise Fallo("sílabo inexistente: %s" % archivo)
    lineas = leer(ruta).split("\n")
    objetivo = normaliza(ancla)
    exactos, prefijo = [], []
    for k, linea in enumerate(lineas):
        m = RE_HEAD.match(linea)
        if not m:
            continue
        t = normaliza(m.group(2))
        if t == objetivo:
            exactos.append((k, len(m.group(1))))
        elif t.startswith(objetivo):
            prefijo.append((k, len(m.group(1))))
    hallados = exactos or prefijo
    if len(hallados) != 1:
        raise Fallo("ancla %r en %s: %d coincidencias (se espera 1)" % (ancla, archivo, len(hallados)))
    ini, nivel = hallados[0]
    fin = len(lineas)
    for k in range(ini + 1, len(lineas)):
        m = RE_HEAD.match(lineas[k])
        if m and len(m.group(1)) <= nivel:
            fin = k
            break
    cuerpo = lineas[ini + 1 : fin]
    while cuerpo and (not cuerpo[-1].strip() or RE_HR.match(cuerpo[-1])):
        cuerpo.pop()
    return "\n".join(cuerpo).strip()


def resumen_desde_silabo(md):
    """1-2 frases de «Contenidos» del sílabo, sin añadir nada."""
    lineas = md.split("\n")
    k = next((j for j, l in enumerate(lineas) if re.match(r"^\*\*Contenidos:?\*\*:?\s*$", l.strip())), None)
    if k is None:
        return None
    k += 1
    while k < len(lineas) and not lineas[k].strip():
        k += 1
    bloque = []
    while k < len(lineas) and lineas[k].strip():
        bloque.append(lineas[k].strip())
        k += 1
    if not bloque:
        return None
    if all(RE_ITEM.match(b) for b in bloque):
        items = [RE_ITEM.match(b).group(3).strip().rstrip(".") for b in bloque]
        out = []
        for it in items:
            if out and len("; ".join(out + [it])) > 300:
                break
            out.append(it)
        texto = "; ".join(out) + "."
    else:
        plano = " ".join(bloque)
        frases = re.split(r"(?<=\.)\s+(?=[A-ZÁÉÍÓÚÑ¿¡\"«])", plano)
        out = []
        for f in frases[:2]:
            if out and len(" ".join(out + [f])) > 320:
                break
            out.append(f)
        texto = " ".join(out)
    texto = texto.replace("**", "")
    if len(texto) > 340:
        corte = texto[:340].rsplit(" ", 1)[0].rstrip(",;:")
        texto = corte + "…"
    return texto


def titulo_html(ruta_html):
    """Texto del primer <h2> de un fragmento de término."""
    m = re.search(r"<h2[^>]*>(.*?)</h2>", leer(ruta_html), re.S)
    if not m:
        return None
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()


def nombres_terminos(carpeta):
    pares = []
    for f in carpeta.glob("p*_t*.html"):
        m = re.match(r"^p\d+[a-z]?_t(\d+)\.html$", f.name)
        if m:
            pares.append((int(m.group(1)), f))
    nombres = []
    for _, f in sorted(pares):
        t = titulo_html(f)
        if t:
            nombres.append(t)
    return nombres


# ---------------------------------------------------------------- README

def tabla_readme():
    """Devuelve ({html: (contenido, marcas)}, {carpeta_mazo: (titulo, notas, version)})."""
    lineas = leer(RAIZ / "README.md").split("\n")
    widgets, mazos = {}, {}
    seccion = None
    for l in lineas:
        if l.startswith("## "):
            seccion = l[3:].strip().lower()
            continue
        if not l.startswith("|"):
            continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if seccion == "widgets" and len(c) >= 5:
            m = re.search(r"`([^`]+\.html)`", c[1])
            if m:
                contenido = re.sub(r"\s+", " ", c[3].replace("**", "").replace("`", "")).strip()
                mm = re.search(r"\d+", c[4])
                widgets[m.group(1)] = (contenido, int(mm.group(0)) if mm else 0)
        elif seccion and seccion.startswith("mazos") and len(c) >= 4:
            m = re.search(r"`mazos/([^/`]+)/?`", c[1])
            if m:
                mm = re.search(r"\d+", c[2])
                mazos[m.group(1)] = (c[0], int(mm.group(0)) if mm else None, c[3] or None)
    return widgets, mazos


# ---------------------------------------------------------------- construcción

def cargar_widgets(readme_w, avisos):
    widgets = []
    for f in sorted((RAIZ / "widgets").glob("*/*/manifiesto.json")):
        carpeta = f.parent
        tema_dir = carpeta.parent.name
        m = json.loads(leer(f))
        tipo_m = m.get("tipo")
        if tipo_m in (None, "v10", "v11"):
            tipo, kit = "ensenanza", ("v11" if tipo_m == "v11" else "v10")
        elif tipo_m in ("definiciones", "apertura"):
            tipo, kit = tipo_m, tipo_m
        else:
            raise Fallo("%s: tipo desconocido %r" % (f.relative_to(RAIZ), tipo_m))
        salida = m.get("salida")
        if not salida:
            raise Fallo("%s: falta «salida»" % f.relative_to(RAIZ))
        destino = (carpeta / salida).resolve()
        if not destino.is_file():
            raise Fallo("HTML de salida inexistente: %s (manifiesto %s)" % (salida, f.relative_to(RAIZ)))
        ruta = destino.relative_to(RAIZ).as_posix()
        wid = "%s-%s" % (tema_dir, carpeta.name)
        wid = wid.lower().replace("_", "-")
        # entidades y términos
        ent = m.get("entidades")
        entidades = []
        mapa_ent = {}
        if isinstance(ent, dict):
            for k in sorted(ent, key=lambda x: (len(x), x)):
                v = ent[k]
                if isinstance(v, dict):
                    v = v.get("nombre") or v.get("titulo") or ""
                if v:
                    entidades.append(str(v))
                    mapa_ent[k] = str(v)
        elif isinstance(ent, list):
            entidades = [str(x) for x in ent]
        terminos = []
        if tipo in ("definiciones", "apertura"):
            t = m.get("terminos")
            if isinstance(t, list):
                terminos = [str(x if not isinstance(x, dict) else x.get("nombre", x.get("titulo", ""))) for x in t]
            else:
                terminos = nombres_terminos(carpeta)
                if isinstance(t, int) and t != len(terminos):
                    avisos.append("%s: el manifiesto declara %d términos y se hallaron %d" % (wid, t, len(terminos)))
        contenido, marcas = readme_w.get(Path(ruta).name, (None, None))
        if contenido is None:
            avisos.append("%s: sin fila en la tabla de widgets del README (%s)" % (wid, Path(ruta).name))
            contenido, marcas = "", 0
        acento = m.get("tema") if m.get("tema") in ACENTOS else None
        modo = m.get("modo") if m.get("modo") in ("multi", "mono") else None
        principal = mapa_ent.get(m.get("principal")) if m.get("principal") else None
        amenaza = mapa_ent.get(m.get("amenaza")) if m.get("amenaza") else None
        widgets.append(
            {
                "id": wid,
                "tema": None,
                "titulo": m.get("titulo") or wid,
                "tipo": tipo,
                "kit": kit,
                "modo": modo,
                "ruta": ruta,
                "contenido": contenido,
                "entidades": entidades,
                "terminos": terminos,
                "principal": principal,
                "amenaza": amenaza,
                "marcas": marcas,
                "acento": acento,
                "busqueda": "",
                "_carpeta": tema_dir,
                "_sub": carpeta.name,
            }
        )
    return widgets


def construir(avisos):
    estructura = json.loads(leer(RAIZ / "biblioteca" / "estructura.json"))
    readme_w, readme_m = tabla_readme()
    widgets = cargar_widgets(readme_w, avisos)

    # ids de widgets
    vistos = {}
    for w in widgets:
        if not ID_RE.match(w["id"]):
            raise Fallo("id de widget inválido (^[a-z0-9-]+$): %s" % w["id"])
        if w["id"] in vistos:
            raise Fallo("id de widget duplicado: %s" % w["id"])
        vistos[w["id"]] = w

    carpetas_disco = sorted(p.name for p in (RAIZ / "widgets").iterdir() if p.is_dir())
    asignada = {}
    temas, semestres = [], []
    ids_tema = set()
    nombre = estructura.get("nombre", "Lumen")

    for sem in estructura["semestres"]:
        rots = []
        for rot in sem["rotaciones"]:
            ids = []
            for orden, t in enumerate(rot["temas"], 1):
                tid = t["id"]
                if not ID_RE.match(tid):
                    raise Fallo("id de tema inválido (^[a-z0-9-]+$): %r" % tid)
                if tid in ids_tema:
                    raise Fallo("id de tema duplicado: %s" % tid)
                ids_tema.add(tid)
                for c in t.get("carpetas", []):
                    if c not in carpetas_disco:
                        raise Fallo("el tema %s referencia una carpeta inexistente: widgets/%s" % (tid, c))
                    if c in asignada:
                        raise Fallo("la carpeta widgets/%s está en dos temas: %s y %s" % (c, asignada[c], tid))
                    asignada[c] = tid
                ws = [w for w in widgets if w["_carpeta"] in t.get("carpetas", [])]
                ws.sort(key=lambda w: (t["carpetas"].index(w["_carpeta"]), ORDEN_TIPO[w["tipo"]], w["_sub"]))
                for w in ws:
                    w["tema"] = tid
                # sílabo
                silabo_html, md_sil = None, None
                s = t.get("silabo")
                if s:
                    archivo = s.get("archivo") or rot.get("silabo")
                    if not archivo:
                        raise Fallo("tema %s: silabo sin archivo y la rotación no define uno" % tid)
                    try:
                        md_sil = fragmento_silabo(archivo, s["ancla"])
                    except Fallo as e:
                        raise Fallo("tema %s: %s" % (tid, e))
                    silabo_html = md_a_html(md_sil, 3) or None
                resumen = t.get("resumen")
                if not resumen and md_sil:
                    resumen = resumen_desde_silabo(md_sil)
                if not resumen:
                    avisos.append("tema %s: sin resumen" % tid)
                    resumen = ""
                # PLAN
                planes = []
                for c in t.get("carpetas", []):
                    p = RAIZ / "widgets" / c / "PLAN.md"
                    if p.is_file():
                        planes.append(leer(p))
                plan_html = None
                if len(planes) == 1:
                    plan_html = md_a_html(planes[0], 3, quitar_h1=True) or None
                elif len(planes) > 1:
                    partes = []
                    for md in planes:
                        m = re.search(r"^#\s+(.*)$", md, re.M)
                        partes.append("<h3>%s</h3>\n%s" % (_inline(m.group(1)) if m else "Plan", md_a_html(md, 4, quitar_h1=True)))
                    plan_html = "\n".join(partes)
                # casos
                casos = []
                for nombre_c in t.get("casos", []):
                    p = RAIZ / "fuentes" / "casos" / nombre_c
                    if not p.is_file():
                        raise Fallo("tema %s: caso inexistente fuentes/casos/%s" % (tid, nombre_c))
                    md = leer(p)
                    m = re.search(r"^#\s+(.*)$", md, re.M)
                    casos.append({"titulo": re.sub(r"[`*]", "", m.group(1)).strip() if m else nombre_c, "html": md_a_html(md, 3, quitar_h1=True)})
                # mazos
                mazos = []
                for carpeta_m in t.get("mazos", []):
                    d = RAIZ / "mazos" / carpeta_m
                    if not d.is_dir():
                        raise Fallo("tema %s: carpeta de mazo inexistente mazos/%s" % (tid, carpeta_m))
                    archivos = []
                    for f in sorted(d.glob("*.apkg")):
                        archivos.append({"etiqueta": "Mazo Anki (.apkg)", "ruta": f.relative_to(RAIZ).as_posix()})
                    for f in sorted(d.glob("*.docx")):
                        archivos.append({"etiqueta": "Guía (.docx)", "ruta": f.relative_to(RAIZ).as_posix()})
                    titulo_m, notas, version = readme_m.get(carpeta_m, (carpeta_m, None, None))
                    mazos.append({"titulo": titulo_m, "notas": notas, "version": version, "archivos": archivos})
                # estado
                estado = t.get("estado") or ("completo" if ws else "pendiente")
                if estado not in ESTADOS:
                    raise Fallo("tema %s: estado inválido %r" % (tid, estado))
                temas.append(
                    {
                        "id": tid,
                        "semestre": sem["id"],
                        "rotacion": rot["id"],
                        "orden": orden,
                        "caso": t.get("caso"),
                        "titulo": t["titulo"],
                        "resumen": resumen,
                        "estado": estado,
                        "nota": t.get("nota"),
                        "silaboHtml": silabo_html,
                        "planHtml": plan_html,
                        "casos": casos,
                        "widgets": [w["id"] for w in ws],
                        "mazos": mazos,
                    }
                )
                ids.append(tid)
            rots.append({"id": rot["id"], "etiqueta": rot["etiqueta"], "descripcion": rot.get("descripcion", ""), "temas": ids})
        semestres.append(
            {
                "id": sem["id"],
                "etiqueta": sem["etiqueta"],
                "asignatura": sem.get("asignatura", ""),
                "institucion": sem.get("institucion", ""),
                "rotaciones": rots,
            }
        )

    huerfanas = [c for c in carpetas_disco if c not in asignada]
    if huerfanas:
        raise Fallo(
            "carpetas de widgets/ sin tema en biblioteca/estructura.json: %s. Regístralas en un tema." % ", ".join(huerfanas)
        )

    por_tema = {t["id"]: t for t in temas}
    ordenados = []
    for t in temas:
        for wid in t["widgets"]:
            ordenados.append(vistos[wid])
    for w in ordenados:
        t = por_tema[w["tema"]]
        w["busqueda"] = normaliza(" ".join([w["titulo"], t["titulo"], w["contenido"]] + w["entidades"] + w["terminos"]))
        del w["_carpeta"], w["_sub"]

    # avisos de casos sin referenciar
    usados = {c for t in estructura["semestres"] for r in t["rotaciones"] for tt in r["temas"] for c in tt.get("casos", [])}
    for f in sorted((RAIZ / "fuentes" / "casos").glob("*.md")):
        if f.name not in usados:
            avisos.append("caso sin tema: fuentes/casos/%s" % f.name)

    catalogo = {
        "generado": datetime.date.today().isoformat(),
        "nombre": nombre,
        "semestres": semestres,
        "temas": temas,
        "widgets": ordenados,
    }
    return catalogo


def escribe_catalogo(catalogo):
    cuerpo = json.dumps(catalogo, ensure_ascii=False, indent=1)
    cuerpo = cuerpo.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    destino = RAIZ / "biblioteca" / "catalogo.js"
    destino.write_text("window.CATALOGO = %s;\n" % cuerpo, encoding="utf-8")
    return destino


# ---------------------------------------------------------------- sitio

def arma_sitio(catalogo, destino, avisos):
    destino = Path(destino).resolve()
    if destino == RAIZ or destino in RAIZ.parents or (destino / ".git").exists():
        raise Fallo("directorio de sitio no permitido: %s" % destino)
    if destino.exists():
        if any(destino.iterdir()) and not (destino / ".nojekyll").exists():
            raise Fallo("el directorio %s no está vacío y no parece un sitio generado (falta .nojekyll)" % destino)
        shutil.rmtree(destino)
    destino.mkdir(parents=True)
    copiados = []

    def copia(rel):
        origen = RAIZ / rel
        d = destino / rel
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(origen, d)
        copiados.append(rel)

    if (RAIZ / "index.html").is_file():
        copia("index.html")
    else:
        avisos.append("index.html aún no existe en la raíz: el sitio se arma sin él")
    for f in sorted((RAIZ / "biblioteca").rglob("*")):
        if f.is_file() and f.name != "estructura.json":
            copia(f.relative_to(RAIZ).as_posix())
    for nombre in ("app.css", "app.js"):
        if not (RAIZ / "biblioteca" / nombre).is_file():
            avisos.append("falta biblioteca/%s" % nombre)
    rutas = set()
    for w in catalogo["widgets"]:
        rutas.add(w["ruta"])
    for t in catalogo["temas"]:
        for m in t["mazos"]:
            for a in m["archivos"]:
                rutas.add(a["ruta"])
    for r in sorted(rutas):
        copia(r)
    (destino / ".nojekyll").write_text("", encoding="utf-8")
    copiados.append(".nojekyll")
    return sorted(copiados)


# ---------------------------------------------------------------- principal

def main():
    ap = argparse.ArgumentParser(description="Genera biblioteca/catalogo.js (Lumen) y, opcionalmente, el sitio.")
    ap.add_argument("--sitio", metavar="DIR", help="arma el sitio publicable en DIR")
    args = ap.parse_args()
    avisos = []
    try:
        catalogo = construir(avisos)
        escribe_catalogo(catalogo)
        if args.sitio:
            copiados = arma_sitio(catalogo, args.sitio, avisos)
            print("Sitio en %s: %d archivos" % (args.sitio, len(copiados)))
    except Fallo as e:
        print("ERROR: %s" % e, file=sys.stderr)
        return 1
    for a in avisos:
        print("AVISO: %s" % a, file=sys.stderr)
    pend = sum(1 for t in catalogo["temas"] if t["estado"] == "pendiente")
    print("RESULTADO: %d temas, %d widgets, %d pendientes" % (len(catalogo["temas"]), len(catalogo["widgets"]), pend))
    return 0


if __name__ == "__main__":
    sys.exit(main())
