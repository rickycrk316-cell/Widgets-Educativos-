#!/usr/bin/env python3
"""Migra mazos viejos (modelos v6 «Quirurgica2 QA/Cloze») a v7 DENTRO de una colección de Anki
(.colpkg), sin perder el historial de repaso.

Para cada mazo pasado como argumento (mazos/<tema>/tarjetas.json) lee `migracion.json` junto al JSON:
  {"Q2-OJO-0001": <nid viejo | null>, ..., "descartadas": [nid, ...]}

- Nota con nid: se cambia de tipo de nota (v6 → v7, mismas tarjetas y repasos), se reescriben sus
  campos y tags con el contenido v7, su GUID pasa a guid_for(id) (así los .apkg futuros la actualizan)
  y sus tarjetas van al submazo `Quirúrgica2::<caso>`.
- Nota con null: se crea nueva con el modelo v7.
- Descartadas: se suspenden y se mueven a `Quirúrgica2::_Retiradas::<caso>` (no se borran: el
  estudiante decide en Anki si las elimina).
- Los mazos viejos que quedan vacíos se eliminan.

Uso:
  pip install anki genanki
  python3 kit/anki/migrar_coleccion.py <entrada.colpkg> <salida.colpkg> mazos/<tema>/tarjetas.json [...]
La entrada nunca se modifica. Se trabaja en un directorio temporal.
"""
import json
import os
import pathlib
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import modelo as M  # noqa: E402

V6_QA, V6_CLOZE = 1738492001202, 1738492001201
V6_A_V7 = {  # campo v7 -> campo v6 (None = vacío)
    V6_QA: (M.QA_ID, {'Pregunta': 'Pregunta', 'Respuesta': 'Respuesta', 'Razonamiento': 'Razonamiento',
                      'Fuente': 'Fuente'}),
    V6_CLOZE: (M.CLOZE_ID, {'Text': 'Text', 'Extra': 'Extra', 'Fuente': 'Fuente'}),
}


def asegurar_modelos(col):
    """Los modelos v7 deben existir (llegan al importar cualquier .apkg v7). Actualiza plantillas y CSS."""
    for mid, campos, q, a in ((M.QA_ID, M.CAMPOS_QA, M.QFMT_QA, M.AFMT_QA),
                              (M.CLOZE_ID, M.CAMPOS_CLOZE, M.QFMT_CLOZE, M.AFMT_CLOZE)):
        nt = col.models.get(mid)
        if nt is None:
            sys.exit(f'Falta el modelo {mid} en la colección: importa antes un .apkg v7 (p. ej. Toxicodependencias).')
        if [f['name'] for f in nt['flds']] != [n for _, n in campos]:
            sys.exit(f'El modelo {nt["name"]} de la colección tiene otros campos; no se migra.')
        nt['css'] = M.CSS
        nt['tmpls'][0]['qfmt'], nt['tmpls'][0]['afmt'] = q, a
        col.models.update_dict(nt)


def cambiar_tipo(col, nids, v6):
    mid7, mapa = V6_A_V7[v6]
    if not nids:
        return
    info = col.models.change_notetype_info(old_notetype_id=v6, new_notetype_id=mid7)
    req = info.input
    viejos = [f['name'] for f in col.models.get(v6)['flds']]
    nuevos = [f['name'] for f in col.models.get(mid7)['flds']]
    del req.new_fields[:]
    req.new_fields.extend(viejos.index(mapa[n]) if mapa.get(n) in viejos else -1 for n in nuevos)
    req.note_ids[:] = nids
    col.models.change_notetype_of_notes(req)


def migrar(col, json_path):
    import genanki
    base = json_path.parent
    datos = json.loads(json_path.read_text(encoding='utf-8'))
    mig = json.loads((base / 'migracion.json').read_text(encoding='utf-8'))
    meta = datos['meta']
    destino = col.decks.id(f'{M.RAIZ_MAZO}::{meta["caso"]}')
    retiro = col.decks.id(f'{M.RAIZ_MAZO}::_Retiradas::{meta["caso"]}')
    mazos_viejos = set()
    reusar = {c['id']: mig.get(c['id']) for c in datos['tarjetas']}
    # 1. cambio de tipo de nota, agrupado por modelo viejo
    por_modelo = {V6_QA: [], V6_CLOZE: []}
    for c in datos['tarjetas']:
        nid = reusar[c['id']]
        if nid is None:
            continue
        n = col.get_note(nid)
        mazos_viejos |= {col.get_card(cid).did for cid in n.card_ids()}
        if n.mid in por_modelo:
            esperado = V6_QA if c['tipo'] == 'QA' else V6_CLOZE
            if n.mid != esperado:
                sys.exit(f'{c["id"]}: la nota {nid} es de otro tipo ({n.mid}); no se puede reutilizar como {c["tipo"]}')
            por_modelo[n.mid].append(nid)
        elif n.mid not in (M.QA_ID, M.CLOZE_ID):
            sys.exit(f'{c["id"]}: la nota {nid} tiene un modelo desconocido ({n.mid})')
    for v6, nids in por_modelo.items():
        cambiar_tipo(col, nids, v6)
    # 2. contenido v7, GUID, tags y mazo
    nuevas = reusadas = 0
    for c in datos['tarjetas']:
        vals = M.valores_saneados(c)
        nid = reusar[c['id']]
        if nid is None:
            n = col.new_note(col.models.get(M.QA_ID if c['tipo'] == 'QA' else M.CLOZE_ID))
        else:
            n = col.get_note(nid)
        for (_, nombre), v in zip(M.CAMPOS_QA if c['tipo'] == 'QA' else M.CAMPOS_CLOZE, vals):
            n[nombre] = v
        n.tags = list(c['tags'])
        n.guid = genanki.guid_for(c['id'])
        if nid is None:
            col.add_note(n, destino)
            nuevas += 1
        else:
            col.update_note(n)
            col.set_deck(n.card_ids(), destino)
            reusadas += 1
        # tarjetas cloze nuevas que genere el texto quedan en el mazo de destino
        col.set_deck(n.card_ids(), destino)
    # 3. descartadas
    descart = [nid for nid in mig.get('descartadas', []) if col.db.scalar('select 1 from notes where id=?', nid)]
    cids = [cid for nid in descart for cid in col.get_note(nid).card_ids()]
    mazos_viejos |= {col.get_card(cid).did for cid in cids}
    if cids:
        col.set_deck(cids, retiro)
        col.sched.suspend_cards(cids)
    # 4. medios nuevos
    for f in (base / 'media').glob('*') if (base / 'media').is_dir() else []:
        if not col.media.have(f.name):
            col.media.add_file(str(f))
    # 5. mazos viejos vacíos
    borrados = []
    for did in mazos_viejos - {destino, retiro}:
        if not col.decks.card_count(did, include_subdecks=True):
            borrados.append(col.decks.name(did))
            col.decks.remove([did])
    print(f'{meta["caso"]}: {reusadas} reutilizadas (con historial), {nuevas} nuevas, '
          f'{len(descart)} retiradas (suspendidas), mazos viejos eliminados: {borrados or "ninguno"}')


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    entrada, salida = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
    jsons = [pathlib.Path(p).resolve() for p in sys.argv[3:]]
    import anki._backend
    from anki.collection import Collection
    with tempfile.TemporaryDirectory() as tmp:
        colp = os.path.join(tmp, 'collection.anki2')
        anki._backend.RustBackend().import_collection_package(
            col_path=colp, backup_path=str(entrada), media_folder=os.path.join(tmp, 'collection.media'),
            media_db=os.path.join(tmp, 'collection.media.db2'))
        col = Collection(colp)
        repasos = col.db.scalar('select count() from revlog')
        asegurar_modelos(col)
        for j in jsons:
            migrar(col, j)
        assert col.db.scalar('select count() from revlog') == repasos, 'se perdieron repasos'
        print(f'repasos conservados: {repasos}')
        col.export_collection_package(str(salida), include_media=True, legacy=False)
        col.close()
    print(f'listo: {salida}')


if __name__ == '__main__':
    main()
