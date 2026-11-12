#!/usr/bin/env python3
"""Empaqueta las skills del repo (.claude/skills/<nombre>/) como .skill instalables en claude.ai.

Uso:
  python3 kit/empaquetar_skills.py                  # definiciones, apertura, widget-ensenanza, flashcards
  python3 kit/empaquetar_skills.py definiciones     # solo una (el impeccable es de terceros: no se empaqueta)

Cada .skill (zip con la carpeta <nombre>/) lleva SKILL.md más:
  references/  sílabos y protocolo de verificación (copias de fuentes/)
  assets/kit/  kit y validadores que la skill usa fuera del repo
Salida: dist/<nombre>.skill. En el repo la skill lee fuentes/ y kit/ directamente.
"""
import sys, re, zipfile, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
REFS = ['fuentes/syllabus_quirurgica2.md', 'fuentes/syllabus_quirurgica2_segunda_rotacion.md', 'fuentes/protocolo_verificacion.md']
KIT = {
    'definiciones': ['def_head.html', 'validar_definiciones.py', 'auditar_definiciones.py', 'construir.py', 'probar_definiciones.js'],
    'apertura': ['apertura_head.html', 'validar_apertura.py', 'auditar_definiciones.py', 'construir.py', 'probar_definiciones.js'],
    'widget-ensenanza': ['v11/head.html', 'v11/script.html', 'v11/validar.py', 'v11/probar.js', 'construir.py', 'renumerar.py'],
    'flashcards': [],
}
# Referencias propias de cada skill, además de REFS (se copian a references/)
REFS_EXTRA = {
    'apertura': ['fuentes/skill_apertura_v1.md', 'fuentes/skill_definiciones_v5.1.md', 'docs/DESIGN.md'],
    'widget-ensenanza': ['docs/DECISIONES_v11.md', 'docs/DESIGN.md'],
}
EXTRA = {
    'definiciones': {'widgets/ansiedad_panico/definiciones/p96_js.html': 'assets/kit/p96_js_ejemplo.html'},
}


def validar(skill: pathlib.Path) -> str:
    s = (skill / 'SKILL.md').read_text(encoding='utf-8')
    m = re.match(r'---\n(.*?)\n---\n', s, re.S)
    if not m: return 'SKILL.md sin frontmatter'
    fm = dict(re.findall(r'^(\w+):\s*"?(.*?)"?\s*$', m.group(1), re.M))
    if fm.get('name') != skill.name: return f'name «{fm.get("name")}» ≠ carpeta «{skill.name}»'
    if not 0 < len(fm.get('description', '')) <= 1024: return 'description vacía o >1024 caracteres'
    return ''


def empaquetar(nombre: str) -> bool:
    skill = RAIZ / '.claude/skills' / nombre
    err = validar(skill)
    if err:
        print(f'ERROR {nombre}: {err}'); return False
    out = RAIZ / 'dist' / f'{nombre}.skill'
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(skill.rglob('*')):
            if f.is_file() and '__pycache__' not in f.parts:
                z.write(f, f'{nombre}/{f.relative_to(skill)}')
        for r in REFS + REFS_EXTRA.get(nombre, []):
            z.write(RAIZ / r, f'{nombre}/references/{pathlib.Path(r).name}')
        for k in KIT[nombre]:
            z.write(RAIZ / 'kit' / k, f'{nombre}/assets/kit/{k}')  # conserva v11/ para que construir.py funcione
        for src, dst in EXTRA.get(nombre, {}).items():
            z.write(RAIZ / src, f'{nombre}/{dst}')
        n = len(z.namelist())
    print(f'== {out.relative_to(RAIZ)} ({n} archivos, {out.stat().st_size // 1024} KB)')
    return True


if __name__ == '__main__':
    nombres = sys.argv[1:] or list(KIT)
    sys.exit(0 if all([empaquetar(n) for n in nombres]) else 1)
