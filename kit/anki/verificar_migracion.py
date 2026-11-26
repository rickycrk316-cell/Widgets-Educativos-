#!/usr/bin/env python3
"""Comprueba los migracion.json contra la colección original antes de migrar (sin modificar nada).

Uso: python3 kit/anki/verificar_migracion.py <entrada.colpkg> mazos/*/tarjetas.json

Errores (impiden migrar o hacen perder historial):
  - nid inexistente, usado dos veces, en dos mazos, o a la vez usado y descartado;
  - tipo distinto (QA↔Cloze);
  - Cloze reutilizada cuyo texto nuevo no conserva todos los huecos que tenían tarjetas
    (esas tarjetas y sus repasos se borrarían);
  - notas viejas del mazo que no están ni usadas ni descartadas;
  - IDs del JSON sin entrada en migracion.json (cuando existe).
Avisos: huecos nuevos en una Cloze reutilizada (tarjetas nuevas, sin pérdida).
"""
import json
import os
import pathlib
import re
import sys
import tempfile

V6 = {1738492001202: 'QA', 1738492001201: 'Cloze', 1762900700101: 'QA', 1762900700102: 'Cloze'}


def main():
    import anki._backend
    from anki.collection import Collection
    entrada, jsons = pathlib.Path(sys.argv[1]).resolve(), [pathlib.Path(p).resolve() for p in sys.argv[2:]]
    E, A = [], []
    with tempfile.TemporaryDirectory() as tmp:
        colp = os.path.join(tmp, 'c.anki2')
        anki._backend.RustBackend().import_collection_package(
            col_path=colp, backup_path=str(entrada), media_folder=os.path.join(tmp, 'm'),
            media_db=os.path.join(tmp, 'm.db'))
        col = Collection(colp)
        dueño = {}
        for j in jsons:
            fm = j.parent / 'migracion.json'
            if not fm.is_file():
                continue
            mazo = j.parent.name
            datos = json.loads(j.read_text(encoding='utf-8'))
            mig = json.loads(fm.read_text(encoding='utf-8'))
            tarj = {c['id']: c for c in datos['tarjetas']}
            desc = {int(n) for n in mig.get('descartadas', [])}
            usados = {k: int(v) for k, v in mig.items() if k != 'descartadas' and v is not None}
            for k in tarj:
                if k not in mig:
                    E.append(f'{mazo}: {k} sin entrada en migracion.json')
            for k in mig:
                if k != 'descartadas' and k not in tarj:
                    E.append(f'{mazo}: {k} está en migracion.json pero no en tarjetas.json')
            dids = set()
            for k, nid in list(usados.items()) + [(None, n) for n in desc]:
                if not col.db.scalar('select 1 from notes where id=?', nid):
                    E.append(f'{mazo}: nid {nid} ({k or "descartada"}) no existe')
                    continue
                if nid in dueño and dueño[nid] != (mazo, k):
                    E.append(f'{mazo}: nid {nid} ya usado en {dueño[nid]}')
                dueño[nid] = (mazo, k)
                n = col.get_note(nid)
                dids |= {col.get_card(c).did for c in n.card_ids()}
                if k is None:
                    continue
                if nid in desc:
                    E.append(f'{mazo}: nid {nid} usado en {k} y también descartado')
                tipo = tarj[k]['tipo']
                if V6.get(n.mid) != tipo:
                    E.append(f'{mazo}: {k} es {tipo} pero la nota {nid} es {V6.get(n.mid, n.mid)}')
                    continue
                if tipo == 'Cloze':
                    viejos = {col.get_card(c).ord + 1 for c in n.card_ids()}
                    nuevos = {int(x) for x in re.findall(r'\{\{c(\d+)::', tarj[k]['text'])}
                    if viejos - nuevos:
                        E.append(f'{mazo}: {k} (nid {nid}) pierde los huecos c{sorted(viejos - nuevos)} '
                                 f'que tienen tarjetas con repasos')
                    if nuevos - viejos:
                        A.append(f'{mazo}: {k} añade huecos c{sorted(nuevos - viejos)} (tarjetas nuevas)')
            # todas las notas viejas de los mazos de origen deben quedar cubiertas
            for did in dids:
                if col.decks.name(did).startswith('Quirúrgica2'):
                    continue
                for nid in col.db.list('select distinct nid from cards where did=?', did):
                    if nid not in desc and nid not in usados.values():
                        E.append(f'{mazo}: nota vieja {nid} del mazo «{col.decks.name(did)}» ni usada ni descartada')
        col.close()
    for a in A:
        print('AVISO', a)
    for e in E:
        print('ERROR', e)
    print(f'RESULTADO: {"OK" if not E else f"{len(E)} errores"}')
    sys.exit(1 if E else 0)


if __name__ == '__main__':
    main()
