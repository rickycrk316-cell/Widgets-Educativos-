#!/usr/bin/env python3
"""Ensambla y valida widgets desde sus partes.

Uso:
  python3 kit/construir.py                         # todos los widgets
  python3 kit/construir.py widgets/disbasia/sin_dolor [...]
  python3 kit/construir.py --sin-validar <dir>     # solo ensamblar

Cada carpeta de widget tiene partes numeradas (*.html, se concatenan en orden
alfabético) y un manifiesto.json con, además de los campos del validador:
  "titulo": texto del <title>
  "salida": ruta del HTML final, relativa a la carpeta del widget
  "tipo":   "definiciones", "apertura" o "v11"
v10:         (sin "tipo" o "v10") CONGELADO: el kit v10 se retiró; no se ensambla ni se toca el
             HTML final. Se informa y cuenta como OK. Para reconstruirlo hay que migrarlo a v11.
definiciones: def_head.html (título sustituido) + partes                  → validar_definiciones.py
apertura:     apertura_head.html (título sustituido) + partes             → validar_apertura.py <html> <manifiesto>
v11:          v11/head.html (título; <html data-tema> desde "tema") + partes + v11/script.html → v11/validar.py
"""
import sys, json, pathlib, subprocess, tempfile

KIT = pathlib.Path(__file__).resolve().parent
RAIZ = KIT.parent


def construir(d: pathlib.Path, validar: bool) -> bool:
    m = json.loads((d / 'manifiesto.json').read_text(encoding='utf-8'))
    tipo = m.get('tipo', 'v10')
    if tipo == 'v10':
        print(f'== {d.relative_to(RAIZ) if d.is_relative_to(RAIZ) else d}: congelado (v10), no se reconstruye')
        return True
    cab = {'definiciones': 'def_head.html', 'apertura': 'apertura_head.html', 'v11': 'v11/head.html'}[tipo]
    head = (KIT / cab).read_text(encoding='utf-8')
    if tipo == 'v11':
        head = head.replace('<html lang="es">', f'<html lang="es" data-tema="{m.get("tema", "otro")}">', 1)
    head = head.replace('<title>@@TITULO@@</title>', f'<title>{m["titulo"]}</title>')
    partes = sorted(p for p in d.glob('*.html'))
    html = head + ''.join(p.read_text(encoding='utf-8') for p in partes)
    if tipo == 'v11':
        html += (KIT / 'v11/script.html').read_text(encoding='utf-8')
    out = (d / m['salida']).resolve()
    out.write_text(html, encoding='utf-8')
    try:
        mostrar = out.relative_to(RAIZ)
    except ValueError:
        mostrar = out
    print(f'== {mostrar} ({len(partes)} partes)')
    if not validar:
        return True
    if tipo == 'definiciones':
        cmd = [sys.executable, str(KIT / 'validar_definiciones.py'), str(out), str(d / 'manifiesto.json')]
    elif tipo == 'apertura':
        cmd = [sys.executable, str(KIT / 'validar_apertura.py'), str(out), str(d / 'manifiesto.json')]
    else:
        vcmd = KIT / 'v11/validar.py'
        # validar.py rechaza claves que no conoce: se le pasa el manifiesto sin las de ensamblaje.
        val = {k: v for k, v in m.items() if k not in ('titulo', 'salida', 'tipo')}
        tmp = tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8')
        json.dump(val, tmp, ensure_ascii=False); tmp.close()
        cmd = [sys.executable, str(vcmd), str(out), tmp.name]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if tipo == 'v11':
        pathlib.Path(tmp.name).unlink()
    lineas = (r.stdout + r.stderr).strip().splitlines()
    # Solo errores y la línea de resultado: ahorra contexto al revisar.
    for ln in lineas:
        if ln.startswith(('ERROR', 'ROJO', 'RESULTADO', 'Traceback')) or 'FALLA' in ln:
            print('   ' + ln)
    return r.returncode == 0


def main():
    args = sys.argv[1:]
    validar = '--sin-validar' not in args
    dirs = [pathlib.Path(a) for a in args if not a.startswith('--')]
    if not dirs:
        dirs = sorted(p.parent for p in (RAIZ / 'widgets').glob('*/*/manifiesto.json'))
    ok = all([construir(d.resolve(), validar) for d in dirs])
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
