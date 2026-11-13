"""Validador del widget de definiciones (skill definiciones v5.1). Uso: python3 validar_definiciones.py widget.html [manifiesto.json]
El manifiesto (opcional) aporta terminos, prerrequisitos, remisiones y tarjetas; sin él rigen los valores del widget de patología urinaria baja."""
import re, sys, subprocess, json, os
from html.parser import HTMLParser
import tempfile
kit=os.path.dirname(os.path.abspath(__file__)); here=tempfile.mkdtemp()
P=sys.argv[1]; H=open(P,encoding='utf-8').read()
res=[]
def chk(name,ok,det=''):
    res.append((name,ok,det)); print(('VERDE ' if ok else 'ROJO  ')+name+(' | '+det if det else ''))
# partes
m=re.search(r'<script>(.*?)</script>',H,re.S); js=m.group(1)
body_nojs=H.replace(m.group(0),'')
open('/tmp/_w.js','w').write(js) if False else None
tmp=os.path.join(here,'_w.js'); open(tmp,'w',encoding='utf-8').write(js)
r=subprocess.run(['node','--check',tmp],capture_output=True,text=True)
chk('node --check',r.returncode==0,r.stderr[:200])
# evaluar DECKS
ev=r"""
const vm=require('vm');const fs=require('fs');
const code=fs.readFileSync(process.argv[2],'utf8');
const sb={document:{getElementById:()=>null,querySelectorAll:()=>[]},console};
vm.createContext(sb);vm.runInContext(code+';this.__o={DECKS,TERMS,RC}',sb);
console.log(JSON.stringify({DECKS:sb.__o.DECKS,TERMS:sb.__o.TERMS}));
"""
evf=os.path.join(here,'_ev.js'); open(evf,'w').write(ev)
r=subprocess.run(['node',evf,tmp],capture_output=True,text=True)
D=json.loads(r.stdout)['DECKS']; TERMS=json.loads(r.stdout)['TERMS']
os.remove(evf); os.remove(tmp)
# estructura
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack=[]; s.tabs={}; s.cur=None; s.text=[]; s.cls=set(); s.errs=[]; s.opened={}; s.paras=[]; s.pbuf=None
        s.inpre=False; s.prestack=0; s.cnt={}
    def handle_starttag(self,t,a):
        a=dict(a)
        for c in (a.get('class') or '').split(): self.cls.add(c)
        if t in('div','section','table','nav','ol','ul','button','p','span','thead','tbody'): self.stack.append(t)
        if t=='section': self.cur=a.get('id'); self.tabs[self.cur]={'pre_acc':0,'rem':0,'html':''}
        c=a.get('class') or ''
        if self.cur:
            if 'pre' in c.split(): self.inpre=True; self.prestack=len(self.stack)
            if t=='div' and 'acc' in c.split() and self.inpre: self.tabs[self.cur]['pre_acc']+=1
            if 'rem-line' in c.split(): self.tabs[self.cur]['rem']+=1
    def handle_endtag(self,t):
        if t in('div','section','table','nav','ol','ul','button','p','span','thead','tbody'):
            if not self.stack or self.stack[-1]!=t: self.errs.append('desbalance '+t+' tras '+str(self.stack[-3:]))
            else: self.stack.pop()
        if self.inpre and t=='div' and len(self.stack)<self.prestack: self.inpre=False
        if t=='section': self.cur=None
    def handle_data(self,d): self.text.append(d)
p=P(); p.feed(body_nojs)
chk('balance div/section/table/nav/ol/ul/button/p/span',not p.errs and not p.stack,'; '.join(p.errs[:3])+str(p.stack))
for t in ('div','section','table'):
    chk('conteo <%s>'%t,len(re.findall('<'+t+r'[\s>]',body_nojs))==len(re.findall('</'+t+'>',body_nojs)))
MAN=json.load(open(sys.argv[2],encoding='utf-8')) if len(sys.argv)>2 else {}
NT=MAN.get('terminos',9)
ids=['t%d'%i for i in range(1,NT+1)]+['tg']
chk('%d pestañas (%d + Repaso global)'%(NT+1,NT),list(p.tabs)==ids,str(list(p.tabs)))
btn=re.findall(r"onclick=\"show\('(\w+)',this\)\"",body_nojs)
chk('show(id) -> pestaña existente y 1:1',btn==ids,str(btn))
chk('barra: %d botones tb'%(NT+1),len(re.findall(r'class="tb( active)?"',body_nojs))==NT+1)
exp_can=MAN.get('prerrequisitos',[3,2,2,1,2,1,2,2,2]); exp_rem=MAN.get('remisiones',[0,1,1,2,1,1,1,1,1]); exp_card=MAN.get('tarjetas',[6,5,5,5,6,5,5,5,6])
chk('prerrequisitos canónicos vs manifiesto',[p.tabs[i]['pre_acc'] for i in ids[:NT]]==exp_can,str([p.tabs[i]['pre_acc'] for i in ids[:NT]]))
chk('remisiones vs manifiesto',[p.tabs[i]['rem'] for i in ids[:NT]]==exp_rem,str([p.tabs[i]['rem'] for i in ids[:NT]]))
chk('tope prerrequisitos <=5',max(exp_can)<=5 and all(p.tabs[i]['pre_acc']<=5 for i in ids[:NT]))
chk('DECKS claves = pestañas con simulador',sorted(D)==sorted(ids[:NT]+['tg']) and all(('id="rc-%s"'%k) in body_nojs for k in D),str(sorted(D)))
chk('tarjetas por mazo vs manifiesto',[len(D[i]) for i in ids[:NT]]==exp_card,str([len(D[i]) for i in ids[:NT]]))
chk('4-6 tarjetas por término',all(4<=len(D[i])<=6 for i in ids[:NT]))
un=[(c['q'],c['a'],c['h']) for i in ids[:NT] for c in D[i]]
g=[(c['q'],c['a'],c['h']) for c in D['tg']]
chk('mazo global = unión exacta',un==g and len(g)==sum(exp_card),str(len(g)))
chk('toda tarjeta con pista',all(c['h'] for i in ids[:NT] for c in D[i]))
chk('un solo motor rc_* (1 definición c/u)',all(len(re.findall(r'function '+f+r'\(',js))==1 for f in('rc_render','rc_show','rc_grade','rc_end','rc_reset')) and not re.search(r'function rc_\w+_t\d',js))
# citas
txt=re.sub(r'\s+',' ',''.join(p.text))
vi=body_nojs.index('class="vanc"')
pre=body_nojs[:vi]
pre=re.sub(r'<[^>]+>',' ',pre)
cites=re.findall(r'\[(\d+)\]',pre)
seen=[]
for c in cites:
    if int(c) not in seen: seen.append(int(c))
nli=len(re.findall(r'<li>',body_nojs[vi:body_nojs.index('</ol>',vi)]))
chk('citas [n] en orden de primera aparición',seen==list(range(1,len(seen)+1)),str(seen))
chk('lista Vancouver = nº de citas distintas',nli==len(seen),'%d li / %d citas'%(nli,len(seen)))
# cadenas prohibidas
bad=['localStorage','sessionStorage','position: fixed','position:fixed','...','[resto','continúa -->','TODO','placeholder','TSV','Exportar a Anki','<img','src="http','class="fig"','style=','⚠','✅','❌','!important']
hits=[b for b in bad if b in H.replace('!important','' if False else '!important')]
hits=[b for b in bad if b in H and not (b=='!important')]
chk('cadenas prohibidas',not hits,str(hits))
chk('un solo <style> (cabecera intacta)',H.count('<style')==1)
head=open(os.path.join(kit,'def_head.html'),encoding='utf-8').read().replace('<title>@@TITULO@@</title>',re.search(r'<title>.*?</title>',H,re.S).group(0))
chk('cabecera = def_head.html con título sustituido',H.startswith(head))
chk('sin emojis/pictogramas',not re.search('[\U0001F000-\U0001FFFF☀-➿⬀-⯿️]',H))
# vocabulario
voc=set('tabs tb tab wrap hb hb-t pre pre-t acc op rem-line chip-rs card card-t fey ej badge b-pu b-am b-ro b-ve b-az b-co b-rs acc-h chev acc-b no tw tl rc rc-t rc-count rc-card rc-q rc-a rc-hint rc-btns go gr ok mid ko ghost rc-end rep mini am gloss vanc active res'.split())
used=set(p.cls)|set(c for s in re.findall(r'class="([^"+]+)"',js) for c in s.split())|{'ok','rep'}
chk('solo vocabulario de clases del PLAN',used<=voc,str(sorted(used-voc)))
# tablas
tabs=re.findall(r'<table>.*?</table>',body_nojs,re.S)
chk('tablas con thead(th)+tbody dentro de div.tw',all('<thead><tr><th' in t and '<tbody>' in t for t in tabs) and body_nojs.count('<div class="tw"><table>')==len(tabs),str(len(tabs)))
# palabras
def wc(s): return len(re.findall(r'\S+',re.sub(r'<[^>]+>','',s)))
bad=[]
for pm in re.finditer(r'<p(?: class="[^"]*")?>(.*?)</p>',body_nojs,re.S):
    if wc(pm.group(1))>90: bad.append(wc(pm.group(1)))
chk('párrafos <=90 palabras',not bad,str(bad))
badb=[wc(x) for x in re.findall(r'<p(?: class="[^"]*")?>(.*?)</p>',body_nojs,re.S) if len(re.findall('<b>',x))>1]
chk('<=1 <b> por párrafo',not badb)
sec=[]
for i in ids[:NT]:
    h=re.search(r'id="%s">(.*)'%i,body_nojs,re.S)
sections=re.findall(r'<section class="tab[^"]*" id="(\w+)">(.*?)</section>',body_nojs,re.S)
fl=[]
for sid,sh in sections:
    if sid=='tg': continue
    hb=re.search(r'<div class="hb"><div class="hb-t">(.*?)</div><p>(.*?)</p>',sh,re.S)
    if wc(hb.group(2))>25: fl.append((sid,'hb',wc(hb.group(2))))
    d=re.search(r'Definición de referencia</div>\s*<p>(.*?)</p>',sh,re.S)
    if wc(d.group(1))>60: fl.append((sid,'def',wc(d.group(1))))
    f=re.search(r'card fey">.*?<p>(.*?)</p>',sh,re.S)
    if wc(f.group(1))>80: fl.append((sid,'fey',wc(f.group(1))))
    # siglas
    gl=re.search(r'<p class="gloss">(.*?)</p>',sh,re.S).group(1)
    core=sh.replace(re.search(r'<p class="gloss">.*?</p>',sh,re.S).group(0),'')
    core=re.sub(r'<[^>]+>',' ',core).replace('[VERIFICAR EN FUENTE]',' ')
    toks=set(re.findall(r'(?<![A-Za-zÁ-ú])[A-Z][A-Z0-9]{1,}(?![A-Za-zÁ-ú])',core))-{'IV'} 
    miss=[t for t in toks if t not in gl and not (t=='Roma')]
    if miss: fl.append((sid,'siglas sin glosario',miss))
    if len(re.findall(r'class="hb"',sh))!=1: fl.append((sid,'hb'))
    if '>Prerrequisitos — lo que debes tener claro antes de leer la definición<' not in sh: fl.append((sid,'pre-t'))
    if 'class="acc no"' not in sh or 'class="rc"' not in sh or 'card ej' not in sh: fl.append((sid,'estructura'))
chk('límites de palabras (hb 25, def 60, Feynman 80) y glosarios',not fl,str(fl))
chk('sin <b> en celdas que no sean 1.ª columna',not re.search(r'</td><td>[^<]*<b>',body_nojs))
chk('sin cards anidadas',not re.search(r'class="card[^"]*">(?:(?!</div>).)*class="(card|hb)[" ]',body_nojs,re.S))
chk('sin exclamaciones ni muletillas',not re.search(r'[¡!]|cabe destacar|es importante mencionar|sin lugar a dudas|vale la pena',re.sub(r'<[^>]+>|<!--.*?-->|<!DOCTYPE[^>]*>','',re.sub(r'<(script|style).*?</\1>','',H,flags=re.S),flags=re.S)))
chk('cierre </div></body></html>',H.rstrip().endswith('</div></body></html>'))
chk('Repaso global con Referencias y ol.vanc',"<span>Referencias</span>" in H and 'class="vanc"' in H)
print('\nRESULTADO:', 'VERDE' if all(r[1] for r in res) else 'ROJO'); sys.exit(0 if all(r[1] for r in res) else 1)
