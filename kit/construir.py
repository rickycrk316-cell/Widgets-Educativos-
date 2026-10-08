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
  "tipo":   "v10" (por defecto) o "definiciones"
v10:          kit_head.html (título sustituido) + partes + kit_script.html → validar.py
definiciones: def_head.html (título sustituido) + partes                  → validar_definiciones.py
"""
import sys, json, pathlib, subprocess, tempfile

KIT = pathlib.Path(__file__).resolve().parent
RAIZ = KIT.parent


def construir(d: pathlib.Path, validar: bool) -> bool:
    m = json.loads((d / 'manifiesto.json').read_text(encoding='utf-8'))
    tipo = m.get('tipo', 'v10')
    head = (KIT / ('def_head.html' if tipo == 'definiciones' else 'kit_head.html')).read_text(encoding='utf-8')
    head = head.replace('<title>@@TITULO@@</title>', f'<title>{m["titulo"]}</title>')
    partes = sorted(p for p in d.glob('*.html'))
    html = head + ''.join(p.read_text(encoding='utf-8') for p in partes)
    if tipo != 'definiciones':
        html += (KIT / 'kit_script.html').read_text(encoding='utf-8')
    out = (d / m['salida']).resolve()
    out.write_text(html, encoding='utf-8')
    print(f'== {out.relative_to(RAIZ)} ({len(partes)} partes)')
    if not validar:
        return True
    if tipo == 'definiciones':
        cmd = [sys.executable, str(KIT / 'validar_definiciones.py'), str(out)]
    else:
        # validar.py rechaza claves que no conoce: se le pasa el manifiesto sin las de ensamblaje.
        val = {k: v for k, v in m.items() if k not in ('titulo', 'salida', 'tipo')}
        tmp = tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8')
        json.dump(val, tmp, ensure_ascii=False); tmp.close()
        cmd = [sys.executable, str(KIT / 'validar.py'), str(out), tmp.name]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if tipo != 'definiciones':
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
