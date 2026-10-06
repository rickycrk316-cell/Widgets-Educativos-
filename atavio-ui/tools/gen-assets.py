"""Convierte los SVG oficiales de v1.2 en src/assets/*.ts (cadena con el interior del SVG + viewBox).
Fuente de verdad: ../atavio-branding-instagram/v1.2/{logo,motifs}. Ejecutar: npm run gen:assets"""
import re, json
from pathlib import Path
V = Path(__file__).resolve().parents[2] / "atavio-branding-instagram" / "v1.2"
OUT = Path(__file__).resolve().parents[1] / "src" / "assets"
OUT.mkdir(parents=True, exist_ok=True)

def parse(p):
    s = p.read_text(encoding="utf-8")
    vb = re.search(r'viewBox="([^"]+)"', s).group(1)
    inner = re.sub(r'^\s*<svg[^>]*>', '', s.strip(), count=1)
    inner = re.sub(r'</svg>\s*$', '', inner)
    inner = re.sub(r'<title>.*?</title>', '', inner, flags=re.S)
    return {"viewBox": vb, "inner": inner.strip()}

def write(name, mapping):
    body = "// Generado por tools/gen-assets.py. No editar a mano.\n"
    body += "export interface SvgAsset { viewBox: string; inner: string }\n"
    body += f"export const {name}: Record<string, SvgAsset> = " + json.dumps(mapping, ensure_ascii=False, indent=1) + ";\n"
    (OUT / f"{name}.ts").write_text(body, encoding="utf-8")
    print(name, {k: len(v["inner"]) for k, v in mapping.items()})

L = V / "logo"
write("sellos", {
    "principal": parse(L / "atavio-sello-principal.svg"),
    "reducido": parse(L / "atavio-sello-reducido.svg"),
    "invertido": parse(L / "atavio-sello-invertido.svg"),
    "invertido-reducido": parse(L / "atavio-sello-invertido-reducido.svg"),
    "tinta": parse(L / "atavio-sello-una-tinta-tinta.svg"),
    "tinta-reducido": parse(L / "atavio-sello-una-tinta-tinta-reducido.svg"),
    "hueso": parse(L / "atavio-sello-una-tinta-hueso.svg"),
    "hueso-reducido": parse(L / "atavio-sello-una-tinta-hueso-reducido.svg"),
})
M = V / "motifs"
write("motivos", {
    "etiqueta-claro": parse(M / "etiqueta-colgante.svg"),
    "etiqueta-oscuro": parse(M / "etiqueta-colgante-oscuro.svg"),
    "marquilla-claro": parse(M / "marquilla-serie.svg"),
    "marquilla-oscuro": parse(M / "marquilla-serie-oscuro.svg"),
    "atraque-claro": parse(M / "detalle-atraque-x.svg"),
    "atraque-oscuro": parse(M / "detalle-atraque-x-oscuro.svg"),
    "cinta-claro": parse(M / "cinta-metrica-horizontal.svg"),
    "cinta-oscuro": parse(M / "cinta-metrica-horizontal-oscuro.svg"),
    "marcador": parse(M / "marcador.svg"),
})
