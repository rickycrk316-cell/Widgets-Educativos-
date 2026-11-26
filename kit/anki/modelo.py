"""Modelos de nota v7 (tema A · Chips clínicos): IDs fijos, campos, plantillas, CSS y saneado HTML.

Lo comparten compilar_mazo.py (genera el .apkg), paginas.py (previsualización) y guia_docx.py.
NUNCA cambies los IDs ni el orden/nombre de los campos de un modelo ya importado: Anki no podría
actualizar las notas. Si hace falta otro campo, crea un modelo NUEVO con ID nuevo y regístralo en
mazos/README.md.
"""
import html
import pathlib
import re
from html.parser import HTMLParser

DIR = pathlib.Path(__file__).resolve().parent
CSS = (DIR / 'estilos.css').read_text(encoding='utf-8')

# ---- IDs fijos (registrados en mazos/README.md) ----
QA_ID = 1762900700101
CLOZE_ID = 1762900700102
QA_NOMBRE = 'Q2 v7 QA'
CLOZE_NOMBRE = 'Q2 v7 Cloze'
DECK_ID_DEMO = 1762900799999          # solo para --demo; nunca se registra
DECK_ID_BASE = 1762900710000          # IDs de mazo por prefijo: base + n (los asigna el registro)
RAIZ_MAZO = 'Quirúrgica2'             # mazo padre histórico; cada caso es un submazo


def nombre_mazo(meta):
    """Quirúrgica2::Rotación <n>::<caso>; meta.rotacion es «1.ª» o «2.ª» (también admite 1 o 2)."""
    n = str(meta['rotacion']).strip()[:1]
    if n not in '12' or not n:
        raise ValueError(f'meta.rotacion debe ser «1.ª» o «2.ª», no {meta["rotacion"]!r}')
    return f'{RAIZ_MAZO}::Rotación {n}::{meta["caso"]}'

# Campos: (clave en el JSON, nombre del campo en Anki). El orden es el del modelo.
CAMPOS_QA = [('pregunta', 'Pregunta'), ('respuesta', 'Respuesta'), ('razonamiento', 'Razonamiento'),
             ('mnemotecnia', 'Mnemotecnia'), ('esquema', 'Esquema'), ('fuente', 'Fuente')]
CAMPOS_CLOZE = [('text', 'Text'), ('extra', 'Extra'), ('mnemotecnia', 'Mnemotecnia'),
                ('esquema', 'Esquema'), ('fuente', 'Fuente')]

_BLOQUES = ('{{#Mnemotecnia}}<div class="bloque mnemo"><div class="rot">Mnemotecnia</div>{{Mnemotecnia}}</div>{{/Mnemotecnia}}'
            '{{#Esquema}}<div class="bloque esquema"><div class="rot">Esquema</div><div class="esq" lang="es">{{Esquema}}</div></div>{{/Esquema}}'
            '{{#Fuente}}<div class="fuente">{{Fuente}}</div>{{/Fuente}}')
QFMT_QA = '<div class="q">{{Pregunta}}</div>'
AFMT_QA = ('{{FrontSide}}<hr id=answer><div class="resp">{{Respuesta}}</div>'
           '{{#Razonamiento}}<div class="razon">{{Razonamiento}}</div>{{/Razonamiento}}' + _BLOQUES)
QFMT_CLOZE = '<div class="q">{{cloze:Text}}</div>'
AFMT_CLOZE = ('<div class="q">{{cloze:Text}}</div><hr id=answer>'
              '{{#Extra}}<div class="razon">{{Extra}}</div>{{/Extra}}' + _BLOQUES)

# ---- Lista blanca HTML ----
SEMANTICAS = ('fx', 'num', 'al', 'dx', 'mec', 'mne', 'vs')     # cuentan para el límite por campo
CLASES_SPAN = SEMANTICAS + ('tema',)
LIMITE_MARCAS = 4
INLINE = {'span', 'b', 'strong', 'i', 'em', 'br', 'sub', 'sup'}
TABLA = {'table', 'caption', 'thead', 'tbody', 'tr', 'th', 'td'}
LISTA = {'ul', 'ol', 'li'}
PERMITIDAS = {   # etiquetas por campo
    'pregunta': INLINE, 'respuesta': INLINE, 'razonamiento': INLINE, 'text': INLINE, 'extra': INLINE,
    'fuente': INLINE - {'span'}, 'mnemotecnia': INLINE | LISTA, 'esquema': INLINE | TABLA | LISTA | {'img'},
}
ATRIBUTOS = {'span': {'class'}, 'th': {'colspan', 'rowspan', 'scope'}, 'td': {'colspan', 'rowspan'},
             'img': {'src', 'alt'}}
VACIAS = {'br', 'img'}


class _Saneador(HTMLParser):
    """Reconstruye el HTML con solo las etiquetas de la lista blanca; todo texto se escapa."""

    def __init__(self, campo):
        super().__init__(convert_charrefs=True)
        self.campo, self.out, self.errores, self.pila = campo, [], [], []
        self.marcas, self.temas, self.imgs, self.spans_abiertos = 0, 0, [], 0

    def handle_starttag(self, tag, attrs):
        perm = PERMITIDAS[self.campo]
        if tag not in perm:
            self.errores.append(f'etiqueta <{tag}> no permitida en {self.campo}')
            return
        a = dict(attrs)
        for k in a:
            if k not in ATRIBUTOS.get(tag, set()):
                self.errores.append(f'atributo {k}= no permitido en <{tag}> ({self.campo})'
                                    + (' — nada de estilos en línea: usa clases' if k == 'style' else ''))
        partes = [tag]
        if tag == 'span':
            cls = (a.get('class') or '').split()
            if len(cls) != 1 or cls[0] not in CLASES_SPAN:
                self.errores.append(f'<span class="{a.get("class")}">: clase no permitida (usa una de {", ".join(CLASES_SPAN)})')
            else:
                if cls[0] in SEMANTICAS:
                    self.marcas += 1
                    if self.spans_abiertos:
                        self.errores.append(f'marca semántica .{cls[0]} anidada dentro de otra ({self.campo})')
                else:
                    self.temas += 1
                partes.append(f'class="{cls[0]}"')
            self.spans_abiertos += 1
        for k in ('colspan', 'rowspan'):
            if k in a and k in ATRIBUTOS.get(tag, ()):
                if not str(a[k]).isdigit():
                    self.errores.append(f'{k} no numérico')
                else:
                    partes.append(f'{k}="{a[k]}"')
        if tag == 'th' and 'scope' in a:
            if a['scope'] in ('row', 'col'):
                partes.append(f'scope="{a["scope"]}"')
        if tag == 'img':
            src = a.get('src') or ''
            if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*\.(svg|png|jpg|jpeg|webp)', src):
                self.errores.append(f'img src="{src}": nombre de archivo de media inválido (sin rutas ni espacios, no empieza por _)')
            self.imgs.append(src)
            partes.append(f'src="{html.escape(src)}"')
            partes.append(f'alt="{html.escape(a.get("alt") or "")}"')
            if not a.get('alt'):
                self.errores.append(f'img src="{src}" sin alt')
        self.out.append('<' + ' '.join(partes) + '>')
        if tag not in VACIAS:
            self.pila.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VACIAS and self.pila and self.pila[-1] == tag:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VACIAS:
            return
        if tag not in PERMITIDAS[self.campo]:
            return
        if not self.pila or self.pila[-1] != tag:
            self.errores.append(f'</{tag}> sin abrir o mal anidada ({self.campo})')
            return
        self.pila.pop()
        if tag == 'span':
            self.spans_abiertos -= 1
        self.out.append(f'</{tag}>')

    def handle_data(self, data):
        self.out.append(html.escape(data, quote=False))

    def handle_comment(self, data):
        self.errores.append(f'comentario HTML no permitido ({self.campo})')


def sanear(campo, valor):
    """Devuelve (html_saneado, info). info: errores, marcas semánticas, nº de .tema, imágenes."""
    p = _Saneador(campo)
    p.feed(valor or '')
    p.close()
    if p.pila:
        p.errores.append(f'etiquetas sin cerrar en {campo}: {", ".join(p.pila)}')
    return ''.join(p.out), {'errores': p.errores, 'marcas': p.marcas, 'temas': p.temas, 'imgs': p.imgs}


def campos(tarjeta):
    return CAMPOS_QA if tarjeta['tipo'] == 'QA' else CAMPOS_CLOZE


def valores_saneados(tarjeta):
    """Lista de valores de campo en el orden del modelo, ya saneados."""
    return [sanear(k, tarjeta.get(k, ''))[0] for k, _ in campos(tarjeta)]


# ---- Render de previsualización (imita al reviewer de Anki para nuestras plantillas) ----
CLOZE_RE = re.compile(r'\{\{c(\d+)::(.*?)(?:::(.*?))?\}\}', re.S)


def render_cloze(texto, ordinal, reverso):
    """Imita rslib/src/cloze.rs: activo -> span.cloze ([...] en el anverso), resto -> span.cloze-inactive."""
    def rep(m):
        n, cuerpo, pista = int(m.group(1)), m.group(2), m.group(3)
        if n == ordinal:
            if reverso:
                return f'<span class="cloze" data-ordinal="{n}">{cuerpo}</span>'
            return f'<span class="cloze" data-ordinal="{n}">[{html.escape(pista) if pista else "..."}]</span>'
        return f'<span class="cloze-inactive" data-ordinal="{n}">{cuerpo}</span>'
    return CLOZE_RE.sub(rep, texto)


def render_plantilla(plantilla, valores, frontside='', ordinal=1, reverso=False):
    def seccion(m):
        return m.group(2) if valores.get(m.group(1), '').strip() else ''
    out = re.sub(r'\{\{#(\w+)\}\}(.*?)\{\{/\1\}\}', seccion, plantilla, flags=re.S)
    out = out.replace('{{FrontSide}}', frontside)
    out = re.sub(r'\{\{cloze:(\w+)\}\}', lambda m: render_cloze(valores.get(m.group(1), ''), ordinal, reverso), out)
    return re.sub(r'\{\{(\w+)\}\}', lambda m: valores.get(m.group(1), ''), out)


def render_tarjeta(tarjeta, ordinal=1):
    """(anverso_html, reverso_html) tal como los vería el reviewer, para la previsualización."""
    vals = {nombre: v for (_, nombre), v in zip(campos(tarjeta), valores_saneados(tarjeta))}
    if tarjeta['tipo'] == 'QA':
        frente = render_plantilla(QFMT_QA, vals)
        return frente, render_plantilla(AFMT_QA, vals, frontside=frente)
    return (render_plantilla(QFMT_CLOZE, vals, ordinal=ordinal, reverso=False),
            render_plantilla(AFMT_CLOZE, vals, ordinal=ordinal, reverso=True))
