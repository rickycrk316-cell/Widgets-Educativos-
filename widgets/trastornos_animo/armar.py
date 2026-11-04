#!/usr/bin/env python3
"""Arma p96_js.html (definiciones) y 90_sim.html (enseñanza) desde los fragmentos de los ejecutores."""
import pathlib, re
T = pathlib.Path(__file__).resolve().parent
D, E = T/'definiciones', T/'ensenanza'
TERMS = {'t1':'Trastornos del estado de ánimo','t2':'Angustia','t3':'Opresión precordial','t4':'Palpitaciones',
 't5':'Sudoración y náuseas','t6':'Preinfarto','t7':'Estrés','t8':'Stresstabs','t9':'Xanax (alprazolam)'}
decks = '\n'.join((D/f'_decks_{x}.js').read_text(encoding='utf-8').strip().rstrip(',') + ',' for x in 'EFG').rstrip(',')
terms = ','.join(f"{k}:'{v}'" for k, v in TERMS.items())
(D/'p96_js.html').write_text('<script>\nconst TERMS={'+terms+'};\nconst DECKS={\n'+decks+'\n};\n'+(T/'_motor_def.js').read_text(encoding='utf-8'), encoding='utf-8')
helpers = "function par(t){return '<p>'+t+'</p>';}\nfunction hv(a,v){return a.indexOf(v)>-1;}\nfunction vacio(dc,t){out(dc,par(t));}\n"
sims = '\n'.join((E/f'_sim_{x}.js').read_text(encoding='utf-8').strip() for x in 'ABC')
(E/'90_sim.html').write_text('<script>\n'+helpers+'\n'+sims+'\n</script>\n', encoding='utf-8')
print('armado p96_js y 90_sim')
