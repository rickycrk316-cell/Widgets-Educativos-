# Widget de enseñanza médica — v10 · Kit (documento de proyecto)

Este documento contiene **solo el kit fijo** de la skill `widget-ensenanza` v10. Las reglas viven en la skill. Claude lo extrae por script **sin leerlo**; no lo edites a mano.

## Uso

En un chat de este proyecto, con ejecución de código activa:

> Widget v10 · Tema: … · Modo: mono|multi (opcional) · Enfoque: … · Guía: … · Bibliografía: … · Contexto local: … · Adjuntos: …

Solo **Tema** es obligatorio. La skill decide el modo: **mono** (1–2 entidades, estructura por etapas de la v9) o **multi** (3–5 entidades con una presentación común: Panorama · De un vistazo · una pestaña por entidad · Síntesis).

## Cambios respecto a v9

| # | Cambio |
|---|---|
| 1 | Router mono/multi con override `Modo:`; tope de 5 entidades. |
| 2 | Modo multi: `pan · vis · e1…eN · sin`; tabla de 9 filas fijas con «tabla en blanco»; delta «Frente a…»; profundidad escalonada (e1 completa). |
| 3 | Pasos etiquetados de vocabulario cerrado en diagnóstico y tratamiento; ficha «Qué verás»; caja de discrepancia violeta; contrafactual en todo simulador. |
| 4 | Profundidad por nodo, prerrequisitos en primera mención, sílabo crítico, concisión ≠ recorte, fármaco por el nodo, recortes declarados. |
| 5 | Núcleo recuperable (20/80) listado en el manifiesto para Anki. Registro de discrepancias opcional (`registro-discrepancias.md`). |
| 6 | Kit: timeline en blanco por sección, `ir()` robusto, fixes de v9; validador con ids por entidad y reciprocidad corregida. |

---

# KIT (no leer · se extrae por script)

## kit_head.html

<!-- ARCHIVO: kit_head.html -->
````html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>@@TITULO@@</title>
<style>
:root{--surface-0:#FFFFFF;--surface-1:#F6F6F4;--border:rgba(0,0,0,.14);--border-accent:#378ADD;--bg-accent:#E6F1FB;--text-primary:#1A1A1A;--text-secondary:#444441;--text-muted:#73726C;--text-accent:#185FA5;--radius:8px;--font-sans:-apple-system,system-ui,"Segoe UI",Helvetica,Arial,sans-serif;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--surface-0:#1E1E1C;--surface-1:#2A2A28;--border:rgba(255,255,255,.16);--border-accent:#85B7EB;--bg-accent:#042C53;--text-primary:#EDEDEA;--text-secondary:#C8C7C2;--text-muted:#9C9A92;--text-accent:#B5D4F4}}
:root[data-theme="dark"]{--surface-0:#1E1E1C;--surface-1:#2A2A28;--border:rgba(255,255,255,.16);--border-accent:#85B7EB;--bg-accent:#042C53;--text-primary:#EDEDEA;--text-secondary:#C8C7C2;--text-muted:#9C9A92;--text-accent:#B5D4F4}
html{color-scheme:light dark}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;background:var(--surface-0);color:var(--text-primary);font:14px/1.75 var(--font-sans);-webkit-text-size-adjust:100%}
.wrap{max-width:920px;margin:0 auto;padding:12px 14px 40px;background:transparent}
h1{font-size:20px;line-height:1.3;margin:6px 0 10px}
h2{font-size:17px;line-height:1.35;margin:22px 0 8px}
h3{font-size:15px;line-height:1.4;margin:16px 0 6px}
p{margin:0 0 10px}
button{font:inherit;color:inherit;cursor:pointer}
button:focus-visible,a:focus-visible,input:focus-visible,textarea:focus-visible{outline:2px solid var(--border-accent);outline-offset:2px}
.tabs{display:flex;gap:6px;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;padding:6px 0 8px;border-bottom:.5px solid var(--border);margin-bottom:12px;position:-webkit-sticky;position:sticky;top:0;z-index:5;background:var(--surface-0)}
.tabs-w{position:-webkit-sticky;position:sticky;top:0;z-index:5;background:var(--surface-0)}
.tabs-w::before,.tabs-w::after{content:"";position:absolute;top:0;bottom:9px;width:36px;pointer-events:none;opacity:0;transition:opacity .2s;z-index:1}
.tabs-w::before{left:0;background:linear-gradient(to left,rgba(128,128,128,0),var(--surface-0))}
.tabs-w::after{right:0;background:linear-gradient(to right,rgba(128,128,128,0),var(--surface-0))}
.tabs-w.ov-l::before,.tabs-w.ov-r::after{opacity:1}
.nodo,.signo,.qv,.dc,h2{scroll-margin-top:72px}
.tabs::-webkit-scrollbar{display:none}
.tb{flex:0 0 auto;min-height:44px;padding:8px 14px;border:.5px solid var(--border);border-radius:var(--radius);background:var(--surface-1);font-size:13px;white-space:nowrap}
.tb.on{background:var(--bg-accent);color:var(--text-accent);border-color:var(--border-accent);font-weight:600}
.tab{display:none}
.tab.on{display:block}
.card{background:var(--surface-1);border:.5px solid var(--border);border-radius:12px;padding:12px 14px;margin:10px 0;font-size:13px;line-height:1.5}
.card p{margin:0 0 8px}
.mini{font-size:12px;color:var(--text-muted);line-height:1.5;margin:6px 0}
.hb{border-radius:12px;padding:12px 14px;margin:10px 0;border:.5px solid transparent}
.hb.az{background:var(--bg-accent);color:var(--text-primary);border-color:var(--border-accent)}
.hb.am{background:#FAEEDA;color:#854F0B;border-color:#854F0B}
.hb.ro{background:#FCEBEB;color:#A32D2D;border-color:#A32D2D}
.hb.ve{background:#EAF3DE;color:#3B6D11;border-color:#3B6D11}
.hb.am .mini,.hb.ro .mini,.hb.ve .mini{color:inherit;opacity:.85}
.hb-t{font-weight:600;margin-bottom:4px}
.pg{margin:0;padding-left:22px}
.pg li{margin:4px 0}
.hb.az:has(.pg){margin-bottom:20px}
.badge{display:inline-block;font-size:11px;line-height:1.4;padding:2px 8px;border-radius:999px;margin:0 4px 4px 0;font-weight:600;vertical-align:middle}
.b-az{background:var(--bg-accent);color:var(--text-accent)}
.b-ro{background:#FCEBEB;color:#A32D2D}
.b-am{background:#FAEEDA;color:#854F0B}
.b-ve{background:#EAF3DE;color:#3B6D11}
.b-pu{background:#EEEDFE;color:#534AB7}
.b-co{background:#FAECE7;color:#993C1D}
.b-rs{background:#FBEAF0;color:#993556}
.rem{display:inline-block;font-size:12px;background:#FBEAF0;color:#993556;border-radius:var(--radius);padding:2px 8px;margin:4px 0}
.fey{background:var(--surface-1);border:.5px solid #993C1D;border-radius:12px;padding:12px 14px;margin:14px 0 22px}
.fey-t{display:inline-block;font-size:11px;font-weight:600;background:#FAECE7;color:#993C1D;border-radius:999px;padding:2px 8px;margin-bottom:6px}
.fey-b{margin:0 0 8px}
.fey-c{margin:2px 0}
.etapa{background:var(--surface-1);border:.5px solid var(--border);border-radius:12px;padding:12px 14px;margin:12px 0}
.etapa h3{margin-top:0}
.res{margin:0 0 10px}
.perla{border-top:.5px solid var(--border);padding-top:8px;margin:0 0 8px;font-weight:600}
.perla::before{content:"Perla";display:inline-block;font-size:11px;background:#EAF3DE;color:#3B6D11;border-radius:999px;padding:2px 8px;margin-right:8px;vertical-align:middle}
.go{min-height:44px;padding:8px 14px;border:.5px solid var(--border-accent);border-radius:var(--radius);background:var(--bg-accent);color:var(--text-accent);font-size:13px}
.tw{overflow-x:auto;margin:8px 0;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;font-size:13px;line-height:1.5}
th,td{border:.5px solid var(--border);padding:6px 8px;text-align:left;vertical-align:top}
th{background:var(--surface-1);font-weight:600}
.stats{display:grid;grid-template-columns:1fr;gap:8px;margin:10px 0}
@media (min-width:600px){.stats{grid-template-columns:repeat(3,1fr)}}
.stat{background:var(--surface-1);border:.5px solid var(--border);border-radius:12px;padding:10px 12px}
.stat b{display:block;font-size:20px;line-height:1.3;color:var(--text-accent)}
.stat span{font-size:12px;color:var(--text-secondary);line-height:1.4;display:block}
.steps{list-style:none;counter-reset:st;padding:0;margin:8px 0}
.steps>li{counter-increment:st;position:relative;padding:4px 0 8px 38px}
.steps>li::before{content:counter(st);position:absolute;left:0;top:2px;width:26px;height:26px;border-radius:50%;background:var(--bg-accent);color:var(--text-accent);font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center}
.tl{list-style:none;margin:12px 0;padding:0 0 0 18px;border-left:2px solid var(--border-accent)}
.nodo{position:relative;margin:0 0 14px;padding:10px 12px;background:var(--surface-1);border:.5px solid var(--border);border-radius:12px;font-size:13px;line-height:1.5}
.nodo::before{content:"";position:absolute;left:-25px;top:14px;width:10px;height:10px;border-radius:50%;background:var(--border-accent)}
.paso{display:block;font-size:14px;margin-bottom:4px}
.pn{color:var(--text-accent);margin-right:4px}
.man{margin:8px 0 0;font-size:12px;color:var(--text-secondary)}
.signo{background:var(--surface-1);border:.5px solid var(--border);border-radius:12px;padding:12px 14px;margin:10px 0;font-size:13px;line-height:1.5}
.signo h4{margin:0 0 6px;font-size:14px}
.signo dl{margin:0}
.signo dt{font-weight:600;font-size:12px;color:var(--text-secondary);margin-top:6px}
.signo dd{margin:0}
.xref{display:inline-flex;align-items:center;min-height:44px;padding:4px 10px;margin:3px 6px 3px 0;border:0;border-radius:var(--radius);background:var(--bg-accent);color:var(--text-accent);font-size:12px;text-align:left}
p .xref,td .xref,li .xref,dd .xref{display:inline;position:relative;min-height:0;padding:1px 6px;margin:0 2px;line-height:inherit;border-radius:6px;white-space:nowrap}
p .xref::after,td .xref::after,li .xref::after,dd .xref::after{content:"";position:absolute;left:-4px;right:-4px;top:-12px;bottom:-12px}
.hl{outline:.5px solid var(--border-accent);background:var(--bg-accent)!important;transition:background .3s}
.acc{border:.5px solid var(--border);border-radius:12px;margin:10px 0;overflow:hidden}
.acc-h{display:flex;justify-content:space-between;align-items:center;width:100%;min-height:44px;padding:8px 14px;border:0;background:var(--surface-1);font-weight:600;font-size:13px;text-align:left}
.chev{transition:transform .2s}
.acc.op .chev{transform:rotate(180deg)}
.acc-b{display:none;padding:10px 14px;font-size:13px;line-height:1.5}
.acc.op .acc-b{display:block}
.vanc{font-size:12px;line-height:1.5;padding-left:22px}
.vanc li{margin:4px 0;word-break:break-word}
.dc{border:1px solid var(--border-accent);border-radius:12px;padding:12px 14px;margin:18px 0;background:var(--surface-0)}
.dc-t{font-weight:600;color:var(--text-accent);margin-bottom:8px}
.dc-g{margin:8px 0}
.dc-l{font-size:12px;color:var(--text-secondary);margin-bottom:4px;display:block}
.chip{min-height:44px;padding:6px 12px;margin:3px 6px 3px 0;border:.5px solid var(--border);border-radius:var(--radius);background:var(--surface-1);font-size:13px}
.chip.on{background:var(--bg-accent);color:var(--text-accent);border-color:var(--border-accent);font-weight:600}
.dc input[type=number]{min-height:44px;width:120px;padding:6px 10px;border:.5px solid var(--border);border-radius:var(--radius);background:var(--surface-1);color:var(--text-primary);font-size:14px}
.out{margin-top:10px;padding:10px 12px;border-radius:var(--radius);background:var(--surface-1);border:.5px solid var(--border);font-size:13px;line-height:1.55;min-height:44px}
.tag{display:inline-block;font-size:11px;padding:2px 8px;border-radius:999px;background:var(--bg-accent);color:var(--text-accent);margin:4px 4px 0 0}
.rec-bar{border:1px dashed var(--border-accent);border-radius:12px;padding:12px 14px;margin:12px 0;font-size:13px;line-height:1.5}
.rec-bar textarea{width:100%;min-height:110px;margin-top:8px;padding:8px 10px;border:.5px solid var(--border);border-radius:var(--radius);background:var(--surface-1);color:var(--text-primary);font:13px/1.5 var(--font-sans);resize:vertical}
.chip:disabled{cursor:default;opacity:.85}
.rec-btns{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
.rec-ctl{display:none;gap:6px;margin-top:6px}
.recon .rec-ctl{display:flex}
.recon>*:not(.rec-bar):not(.tl){display:none}
.recon .nodo:not(.rev) .pt{display:none}
.recon .nodo:not(.rev) .pn::after{content:" ?"}
.recon .nodo:not(.rev) .det{display:none}
.recon .nodo.pis:not(.rev) .det{display:block}
.recon .nodo.pis:not(.rev) .det>*:not(.man){display:none}
.recon .nodo:not(.pis):not(.rev) .man{display:none}
.recon .nodo.rev{border-color:var(--border-accent)}
.rec-go{margin:18px 0}
.steps.tg>li{padding-left:38px}
span.tg{display:inline-block;font:600 11px/1.4 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;padding:2px 7px;margin:0 6px 2px 0;border-radius:6px;background:var(--surface-1);border:.5px solid var(--border);color:var(--text-secondary);white-space:nowrap;vertical-align:1px}
span.tg[data-t="clave"]{background:var(--bg-accent);color:var(--text-accent);border-color:var(--border-accent)}
span.tg[data-t="ok"]{background:#EAF3DE;color:#3B6D11;border-color:#3B6D11}
span.tg[data-t="cond"]{background:#FAEEDA;color:#854F0B;border-color:#854F0B}
span.tg[data-t="no"]{background:#FBEAF0;color:#993556;border-color:#993556}
span.tg[data-t="alarma"]{background:#FCEBEB;color:#A32D2D;border-color:#A32D2D}
.qv{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px;margin:10px 0}
.qv p{margin:0;padding:8px 10px;border-radius:10px;border:.5px solid var(--border);background:var(--surface-1);font-size:13px;line-height:1.45}
.qv p::before{display:block;font-size:10px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;margin-bottom:2px;color:var(--text-muted)}
.qv p[data-e="p"]{background:var(--bg-accent);border-color:var(--border-accent)}
.qv p[data-e="p"]::before{content:"Presente";color:var(--text-accent)}
.qv p[data-e="v"]::before{content:"Variable"}
.qv p[data-e="a"]{border:1px dashed var(--border);color:var(--text-muted);background:transparent}
.qv p[data-e="a"]::before{content:"Ausente"}
.qv p[data-e="k"]{grid-column:1/-1;border:1.5px solid var(--border-accent);background:var(--bg-accent)}
.qv p[data-e="k"]::before{content:"Signo clave";color:var(--text-accent)}
.hb.vi{background:#EEEDFE;color:#534AB7;border-color:#534AB7}
.hb.vi .mini{color:inherit;opacity:.85}
table.vis{min-width:620px}
table.vis td{min-width:140px}
table.vis tr>:first-child{position:-webkit-sticky;position:sticky;left:0;z-index:1;background:var(--surface-1);min-width:118px;max-width:150px;font-weight:600}
.vb-bar{border:1px dashed var(--border-accent);border-radius:12px;padding:12px 14px;margin:12px 0;font-size:13px;line-height:1.5}
.tbl>*:not(.vb-bar):not(.vis-w){display:none}
.tbl td.tap{cursor:pointer}
.tbl td.tap:not(.rev){color:transparent;background:repeating-linear-gradient(135deg,var(--surface-1),var(--surface-1) 8px,var(--bg-accent) 8px,var(--bg-accent) 16px)}
.tbl td.tap:not(.rev) *{visibility:hidden}
.tbl td.tap.rev{box-shadow:inset 0 0 0 1px var(--border-accent)}
.cf{display:block;margin-top:8px;padding-top:6px;border-top:.5px dashed var(--border-accent);font-style:italic;color:var(--text-secondary)}
.cf::before{content:"Contrafactual · ";font-style:normal;font-weight:600;color:var(--text-accent)}
.fig{margin:12px 0}
.fig img{display:block;max-width:100%;height:auto;border-radius:var(--radius);border:.5px solid var(--border)}
.fig figcaption{font-size:12px;color:var(--text-muted);line-height:1.5;margin-top:6px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
</style>
</head>
<body>
<div class="wrap">
<!-- /KIT_HEAD -->
````

## kit_script.html

<!-- ARCHIVO: kit_script.html -->
````html
<!-- KIT_SCRIPT -->
</div>
<script>
(function(){
'use strict';
var $=function(s,r){return(r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
function secK(k){return $('section.tab[data-tab="'+k+'"]')}
function secOf(el){return el&&el.closest?el.closest('section.tab'):null}
function nameOf(k){var b=$('button.tb[data-tab="'+k+'"]');return b?b.textContent.replace(/\s+/g,' ').replace(/^\s+|\s+$/g,''):k}
function btn(t,f,c){var b=document.createElement('button');b.type='button';b.className=c||'chip';b.textContent=t;b.addEventListener('click',f);return b}
function recon(s,on){if(!s)return;s.classList.toggle('recon',!!on);$$('.nodo',s).forEach(function(n){n.classList.remove('rev');n.classList.remove('pis')});var st=$('.rec-state',s);if(st)st.textContent=on?'Modo reconstrucción activo':'Modo lectura';var a=$('.rec-bar [data-act="rec"]',s);if(a){a.disabled=!!on;a.classList.toggle('on',!!on);a.textContent=on?'Reconstrucción activa':'Activar reconstrucción'}}
window.recon=function(k,on){recon(secK(k),on)};
function navOv(){var n=$('nav.tabs');if(!n)return;var sl=n.scrollLeft,mx=n.scrollWidth-n.clientWidth,w=n.parentNode;[n,w].forEach(function(e){if(e===n||e.classList.contains('tabs-w')){e.classList.toggle('ov-l',sl>2);e.classList.toggle('ov-r',sl<mx-2)}})}
function tabla(on){var t=$('table.vis'),s=secOf(t);if(!s)return;s.classList.toggle('tbl',!!on);$$('td.tap',t).forEach(function(c){c.classList.remove('rev')});var st=$('.vb-state',s);if(st)st.textContent=on?'Tabla tapada: toca cada celda para revelarla':'Modo lectura'}
window.tabla=tabla;
window.show=function(k){var ns=secK(k);if(!ns)return;$$('section.tab.on').forEach(function(s){if(s!==ns){if(s.classList.contains('recon'))recon(s,false);if(s.classList.contains('tbl'))tabla(false)}});$$('.tb,.tab').forEach(function(e){e.classList.toggle('on',e.getAttribute('data-tab')===k)});window.scrollTo(0,0);var b=$('.tb.on');if(b&&b.scrollIntoView){try{b.scrollIntoView({inline:'nearest',block:'nearest'})}catch(e){}}navOv()};
window.ir=function(k,id){var el=document.getElementById(id),s=secOf(el);if(!s)return;var nodo=el.classList.contains('nodo');if(s.classList.contains('recon')&&!nodo)recon(s,false);if(s.classList.contains('tbl')&&!el.closest('.vis-w'))tabla(false);show(s.getAttribute('data-tab'));if(nodo&&s.classList.contains('recon'))el.classList.add('rev');var a=el.closest('.acc');if(a)a.classList.add('op');el.scrollIntoView({block:'start'});el.classList.add('hl');setTimeout(function(){el.classList.remove('hl')},1500)};
window.tog=function(b){var a=b.closest('.acc');if(a)a.classList.toggle('op')};
window.sel=function(dc,g){return $$('.chip.on[data-g="'+g+'"]',dc).map(function(c){return c.getAttribute('data-v')})};
window.num=function(dc,n){var i=$('input[data-n="'+n+'"]',dc);if(!i||i.value==='')return NaN;return parseFloat(String(i.value).replace(',','.'))};
window.out=function(dc,h){var o=$('.out',dc);if(o)o.innerHTML=h};
window.rd=function(x,d){var p=Math.pow(10,d||0);return Math.round(x*p)/p};
function outErr(dc,e){var o=$('.out',dc);if(o)o.textContent='Error de cálculo: '+(e&&e.message?e.message:String(e))}
function runDc(dc){var fn=window[dc.getAttribute('data-fn')];if(typeof fn==='function'){try{fn(dc)}catch(e){outErr(dc,e)}}}
window.ch=function(el){var dc=el.closest('.dc');if(!dc)return;if(el.classList.contains('chip')){var g=el.getAttribute('data-g');if(el.getAttribute('data-m')==='1'){el.classList.toggle('on')}else{var was=el.classList.contains('on');$$('.chip[data-g="'+g+'"]',dc).forEach(function(c){c.classList.remove('on')});if(!was)el.classList.add('on')}}runDc(dc)};
function initNodos(f){var k=f.getAttribute('data-tab');$$('.nodo',f).forEach(function(n,i){var p=document.createElement('b');p.className='paso';var pn=document.createElement('span');pn.className='pn';pn.textContent=(i+1)+' ·';var pt=document.createElement('span');pt.className='pt';pt.textContent=n.getAttribute('data-paso')||'';p.appendChild(pn);p.appendChild(pt);var ra=n.getAttribute('data-rama');if(ra){var b=document.createElement('span');b.className='badge b-az rama';b.textContent=ra;p.appendChild(document.createTextNode(' '));p.appendChild(b)}n.insertBefore(p,n.firstChild);var c=document.createElement('div');c.className='rec-ctl';if($('.man',n))c.appendChild(btn('Pista',function(){n.classList.toggle('pis')}));c.appendChild(btn('Revelar',function(){n.classList.toggle('rev')}));n.appendChild(c)});
var tl=$('ol.tl',f);if(!tl)return;var bar=document.createElement('div');bar.className='rec-bar';bar.id='rec-bar-'+k;var t=document.createElement('div');t.innerHTML='<b>Timeline en blanco</b> · <span class="rec-state">Modo lectura</span><p class="mini">Reconstruye la cascada sin mirar: escribe cada paso en orden, luego usa Pista (signos que produce) y Revelar nodo por nodo. Nada se guarda.</p>';bar.appendChild(t);var ta=document.createElement('textarea');ta.setAttribute('aria-label','Escribe aquí la cascada en orden');var bs=document.createElement('div');bs.className='rec-btns';var ab=btn('Activar reconstrucción',function(){recon(f,true);ta.focus()});ab.setAttribute('data-act','rec');bs.appendChild(ab);bs.appendChild(btn('Revelar todo',function(){$$('.nodo',f).forEach(function(n){n.classList.add('rev')})}));bs.appendChild(btn('Salir',function(){recon(f,false)}));bar.appendChild(bs);bar.appendChild(ta);tl.parentNode.insertBefore(bar,tl)}
var TGT={'1.º':'clave','De elección':'clave','Confirma':'ok','Solo si':'cond','Escala':'cond','Reevalúa':'cond','No pidas':'no','Evita':'no','Alarma':'alarma'};
function initTg(){$$('ol.tg span.tg').forEach(function(s){var v=TGT[s.textContent.replace(/^\s+|\s+$/g,'')];if(v)s.setAttribute('data-t',v)})}
function initTabla(){var t=$('table.vis'),s=secOf(t);if(!s)return;var w=t.parentNode;if(!w.classList.contains('tw')){w=document.createElement('div');w.className='tw';t.parentNode.insertBefore(w,t);w.appendChild(t)}w.classList.add('vis-w');var rows=$$('tbody tr',t);if(!rows.length)rows=$$('tr',t).slice(1);rows.forEach(function(r){Array.prototype.slice.call(r.children,1).forEach(function(c){c.classList.add('tap');c.addEventListener('click',function(){if(s.classList.contains('tbl'))c.classList.add('rev')})})});
var bar=document.createElement('div');bar.className='vb-bar';bar.id='vb-bar';var h=document.createElement('div');h.innerHTML='<b>Tabla en blanco</b> · <span class="vb-state">Modo lectura</span><p class="mini">Tapa todas las celdas de las entidades (quedan visibles las cabeceras y los ejes). Di cada celda antes de tocarla; un toque la revela. Nada se guarda.</p>';bar.appendChild(h);var bs=document.createElement('div');bs.className='rec-btns';bs.appendChild(btn('Tapar la tabla',function(){tabla(true)}));bs.appendChild(btn('Revelar todo',function(){$$('td.tap',t).forEach(function(c){c.classList.add('rev')})}));bs.appendChild(btn('Salir',function(){tabla(false)}));bar.appendChild(bs);w.parentNode.insertBefore(bar,w)}
function initRecGo(){var TL=$$('section.tab').filter(function(s){return!!$('ol.tl',s)}),sin=secK('sin'),dst=sin||secK('seg');if(!dst)return;var ord=sin?TL.filter(function(s,i){return i%2===0}).concat(TL.filter(function(s,i){return i%2===1})):TL;var vt=$('table.vis');if(!ord.length&&!(sin&&vt))return;
var w=document.createElement('div');w.className='hb az rec-go';w.innerHTML='<div class="hb-t">Antes de cerrar: recupera sin mirar</div><p class="mini">Cada botón te lleva a la función en blanco correspondiente. Intenta la respuesta completa antes de revelar.</p>';var bs=document.createElement('div');bs.className='rec-btns';w.appendChild(bs);
if(sin&&vt){var vs=secOf(vt),vk=vs.getAttribute('data-tab'),b0=btn('Tabla en blanco — '+nameOf(vk),function(){show(vk);tabla(true);var b=document.getElementById('vb-bar');if(b)b.scrollIntoView({block:'start'})},'go');b0.setAttribute('data-rec',vk);bs.appendChild(b0)}
ord.forEach(function(s){var k=s.getAttribute('data-tab'),b=btn('Reconstruir la cascada — '+nameOf(k),function(){show(k);recon(s,true);var r=document.getElementById('rec-bar-'+k);if(r)r.scrollIntoView({block:'start'})},'go');b.setAttribute('data-rec',k);bs.appendChild(b)});
var rf=$('.acc.refs',dst);if(rf)dst.insertBefore(w,rf);else dst.appendChild(w)}
function init(){var f=$('.tb'),ph=[function(){var n=$('nav.tabs');if(n){var w=document.createElement('div');w.className='tabs-w';n.parentNode.insertBefore(w,n);w.appendChild(n);n.addEventListener('scroll',navOv);window.addEventListener('resize',navOv)}},function(){$$('section.tab').forEach(function(s){if($('ol.tl',s))initNodos(s)})},initTg,initTabla,initRecGo,function(){$$('.dc').forEach(runDc)},function(){show(secK('pan')?'pan':(f?f.getAttribute('data-tab'):''))}];ph.forEach(function(p){try{p()}catch(e){if(window.console)console.error('kit v10:',e)}})}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
</body>
</html>
````

## validar.py

<!-- ARCHIVO: validar.py -->
````python
#!/usr/bin/env python3
"""Validador fijo del widget v10 (mono|multi). Uso: python3 validar.py widget.html [manifiesto.json]"""
import sys, re, json, subprocess, tempfile, os, unicodedata
try:
    from bs4 import BeautifulSoup, Tag
except ImportError:
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'beautifulsoup4', '--break-system-packages'])
    from bs4 import BeautifulSoup, Tag
def _hook(tp, v, tb):
    import traceback; ln = traceback.extract_tb(tb)[-1].lineno if tb else '?'
    print(f'ERROR [validador]: excepción interna {tp.__name__}: {v} (línea {ln}); revisa la estructura señalada o reensambla')
    print('RESULTADO: FALLA · errores 1 · avisos 0 · JS ?'); sys.exit(1)
sys.excepthook = _hook
P = sys.argv[1]; H = open(P, encoding='utf-8').read(); S = BeautifulSoup(H, 'html.parser')
E, W = {}, {}
def err(c, m): E.setdefault(c, []).append(m)
def warn(c, m):
    if m not in W.setdefault(c, []): W[c].append(m)
CIT = re.compile(r'\[\d+(?:\s*[,–-]\s*\d+)*\]')
def txt(el): return re.sub(r'\s+', ' ', el.get_text(' ')).strip()
def words(t): return len(re.findall(r"[\w%/\-]+", CIT.sub(' ', t)))
def kids(el): return [c for c in el.children if isinstance(c, Tag)]
def cls(el): return ' '.join(el.get('class') or [])
def nz(s):
    s = s.replace('º', 'o').replace('°', 'o').casefold()
    s = ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))
    return re.sub(r'[\s.]', '', s)
IDRE = re.compile(r'^(?:(e[1-5])-)?([ms])-(\d+)$')
def kind(i):
    m = IDRE.match(i or ''); return m.group(2) if m else None
# --- ensamblaje: separa kit / partes del LLM
A, B = '<!-- /KIT_HEAD -->', '<!-- KIT_SCRIPT -->'
if H.count(A) == 1 and H.count(B) == 1 and H.index(A) < H.index(B): LLM = H[H.index(A) + len(A):H.index(B)]
else: LLM = H; err('ensamblaje', 'marcas del kit ausentes o duplicadas: ensambla con el comando del contrato (kit_head.html primero, kit_script.html al final, sin editarlos)')
L = BeautifulSoup(LLM, 'html.parser')
# --- pestañas y modo
tbs = [b.get('data-tab') for b in S.select('button.tb')]
secl = S.select('section.tab'); keys = [s.get('data-tab') for s in secl]; secs = {s.get('data-tab'): s for s in secl}
name = {b.get('data-tab'): txt(b) for b in S.select('button.tb')}
if len(set(keys)) != len(keys): err('pestañas', f'data-tab repetido en sections: {keys}')
if len(set(tbs)) != len(tbs): err('pestañas', f'data-tab repetido en botones: {tbs}')
if tbs != keys: err('pestañas', f'orden DOM de sections {keys} ≠ orden de botones {tbs}: ordena partes y botones igual')
for b in S.select('button.tb'):
    if (b.get('onclick') or '').strip() != f"show('{b.get('data-tab')}')": err('pestañas', f'botón {b.get("data-tab")}: onclick="show(\'{b.get("data-tab")}\')"')
struct = 'multi' if ('vis' in secs or any(re.fullmatch(r'e\d+', k or '') for k in secs)) else 'mono'
M = None
if len(sys.argv) > 2:
    try: M = json.load(open(sys.argv[2], encoding='utf-8'))
    except Exception as e: err('manifiesto', f'manifiesto.json ilegible: {e}')
MODE = struct
if M is None: warn('manifiesto', 'sin manifiesto: modo detectado por estructura')
elif M.get('modo') is None: warn('manifiesto', f'falta "modo": usa "modo":"{struct}"')
elif M.get('modo') != struct: err('modo', f'manifiesto "modo":"{M.get("modo")}" pero el HTML es {struct} (pestañas {tbs}): corrige uno de los dos')
ENT = [k for k in tbs if re.fullmatch(r'e\d+', k or '')]
N = len(ENT)
BASE = ['pan', 'def', 'fis', 'cli', 'dx', 'tx', 'seg']
if MODE == 'mono':
    for k in BASE:
        if k not in secs: err('pestañas', f'falta <section class="tab" data-tab="{k}">')
    extra = [k for k in tbs if k not in BASE]
    if len(extra) > 1: err('pestañas', f'más de una pestaña adicional: {extra}')
    for x in extra:
        if not re.fullmatch(r'[a-z]{2,4}', x or ''): err('pestañas', f'clave adicional "{x}": 2–4 letras minúsculas')
    if [k for k in tbs if k in BASE] != [k for k in BASE if k in tbs]: err('pestañas', f'orden de barra: {" ".join(BASE)} (+1 adicional en su lugar lógico)')
else:
    exp = ['pan', 'vis'] + [f'e{i}' for i in range(1, N + 1)] + ['sin']
    if N > 5: err('entidades', f'{N} entidades: máximo 5; propone dividir el tema en dos widgets')
    if N < 3: err('entidades', f'{N} entidades: multi exige 3–5 (con 1–2 usa mono)')
    if tbs != exp: err('pestañas', f'barra multi debe ser exactamente {" ".join(exp)}; hay {" ".join(map(str, tbs))}')
CONT = [k for k in tbs if k != 'pan' and k in secs]
REFTAB = 'sin' if MODE == 'multi' else 'seg'
# --- JS
scripts = '\n'.join(s.string or '' for s in S.find_all('script'))
llm_js = '\n'.join(s.string or '' for s in L.find_all('script'))
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f: f.write(scripts); jf = f.name
try:
    r = subprocess.run(['node', '--check', jf], capture_output=True, text=True)
    js_ok = 'OK' if not r.returncode else 'ERROR'
    if r.returncode: err('js', 'node --check: ' + r.stderr.strip()[-300:])
except FileNotFoundError:
    js_ok = 'validación manual'; warn('js', 'node no disponible')
os.unlink(jf)
for fn in ['window.show', 'window.ir', 'window.tog', 'window.ch', 'window.recon', 'window.tabla', 'initNodos', 'initRecGo']:
    if fn not in scripts: err('kit', f'kit_script incompleto o editado: falta {fn}; reextrae el kit')
for m in re.finditer(r'(?:function\s+|(?:var|let|const)\s+|window\.)(show|ir|tog|ch|sel|num|out|rd|recon|tabla)\b\s*[=(]', llm_js):
    err('simulador', f'90_sim redefine el nombre reservado "{m.group(1)}": renombra tu función')
if len(L.find_all('script')) > 1: warn('simulador', 'más de un <script> en las partes: todo en 90_sim.html')
if re.search(r'\b(VPP|VPN|prevalencia|Bayes|post-?test|pre-?test|Fagan|likelihood)\b', llm_js, re.I): err('simulador', 'simulador con lógica de rendimiento diagnóstico (VPP/VPN/prevalencia/Bayes): elimínala; esas cifras solo se tabulan')
# --- cadenas prohibidas (solo partes del LLM)
for bad in ['localStorage', 'sessionStorage', 'position:fixed', 'position: fixed', '[resto', 'continúa -->', 'TODO:', '<style', '<link', '@import', 'url(', '<iframe', '<object', '<embed', 'src="http', "src='http"]:
    if bad in LLM: err('prohibido', f'cadena prohibida en las partes: «{bad}»')
if re.search(r'<[a-zA-Z][^>]*\sstyle\s*=', LLM): err('prohibido', 'estilo inline (style="…"): usa solo clases del kit')
if '@@TITULO@@' in H: err('prohibido', 'título sin sustituir: sed "s/@@TITULO@@/<Tema>/"')
LT = BeautifulSoup(LLM, 'html.parser')
for t in LT(['script', 'style']): t.decompose()
m3 = re.search(r'.{0,30}\.\.\..{0,10}', LT.get_text(' '))
if m3: err('prohibido', f'«...» ASCII en el texto («{m3.group(0).strip()}»): usa «…» (U+2026)')
for im in S.find_all('img'):
    fg = im.find_parent('figure'); fc = fg.find('figcaption') if fg else None
    if not (fg and 'fig' in (fg.get('class') or []) and fc and txt(fc) and (im.get('src') or '').startswith('data:image/') and (im.get('alt') or '').strip()):
        err('imagen', '<img> solo así: <figure class="fig"><img src="data:image/jpeg;base64,…" alt="…"><figcaption>interpreta…</figcaption></figure>')
# --- Panorama
pan = secs.get('pan')
if pan:
    et = pan.select('.etapa')
    if MODE == 'mono':
        if len(et) < 7: err('panorama', f'{len(et)} etapas (mínimo 7)')
        gos = None
    else:
        gos = ['vis'] + ENT
        if [e.get('data-go') for e in et] != gos: err('panorama', f'etapas data-go {[e.get("data-go") for e in et]} → deben ser {gos} (eje primero, luego una por entidad)')
    if words(txt(pan)) > 900: err('panorama', f'{words(txt(pan))} palabras (>900)')
    for i, e in enumerate(et, 1):
        rs, pe = e.select_one('.res'), e.select_one('.perla')
        if not rs or not pe: err('panorama', f'etapa {i}: falta p.res o p.perla'); continue
        n = words(txt(rs))
        if not 70 <= n <= 110: err('panorama', f'etapa {i}: párrafo {n} palabras (70–110)')
        if words(txt(pe)) > 20: err('panorama', f'etapa {i}: perla {words(txt(pe))} palabras (>20)')
        g = e.get('data-go'); bt = e.select_one('button[data-go]')
        if g not in secs or not bt or bt.get('data-go') != g or (bt.get('onclick') or '').strip() != f"show('{g}')": err('panorama', f'etapa {i}: <button type="button" class="go" data-go="{g}" onclick="show(\'{g}\')">')
    for x in pan.select('.pg,.fey,.dc,.nodo,.signo,.qv,ol.tg'): err('panorama', 'elemento prohibido en pan: .' + cls(x))
    if not any(txt(p).startswith('Esto es el mapa, no el territorio') for p in pan.select('p.mini')): warn('panorama', 'falta la línea de cierre literal en p.mini')
# --- segmentos h2 (multi)
H2L = ['Qué es', 'Epidemiología', 'Cadena', 'Qué verás', 'Diagnóstico', 'Tratamiento', 'Seguimiento']
GRP = {}
def top_of(el, sec):
    while el is not None and el.parent is not sec: el = el.parent
    return el
def grp(el):
    s = el.find_parent('section', class_='tab')
    if s is None: return None, None
    t = top_of(el, s); return s.get('data-tab'), GRP.get(id(t))
if MODE == 'multi':
    for k in ENT:
        s = secs.get(k)
        if not s: continue
        for h in s.find_all('h2'):
            if h.parent is not s: err('h2', f'{k}: h2 «{txt(h)}» debe ser hijo directo de la section')
        hs = s.find_all('h2', recursive=False); lab = [txt(h) for h in hs]
        if len(hs) != 7 or any(not nz(a).startswith(nz(b)) for a, b in zip(lab, H2L)):
            err('h2', f'{k}: h2 deben ser 7 y en orden: {" · ".join(H2L)}; hay: {" · ".join(lab)}')
        cur = None; order = []
        for c in kids(s):
            if c.name == 'h2':
                cur = next((b for b in H2L if nz(txt(c)).startswith(nz(b))), txt(c))
            GRP[id(c)] = cur; order.append((c, cur))
        pre = [c for c, g in order if g is None]
        iF = next((i for i, c in enumerate(pre) if 'hb' in (c.get('class') or []) and c.select_one('.hb-t') and txt(c.select_one('.hb-t')).startswith('Frente a')), None)
        iP = next((i for i, c in enumerate(pre) if c.select_one('ol.pg')), None)
        if pre and iF is not None and iF != 0: warn('orden', f'{k}: la primera caja debe ser «Frente a…» (sin highlight previo)')
        if iF is None: err('delta', f'{k}: falta <div class="hb az"><div class="hb-t">Frente a [entidad]</div>… antes de las preguntas guía')
        elif iP is not None and iF > iP: err('delta', f'{k}: «Frente a…» va antes de las preguntas guía')
        elif k != 'e1' and not any(name[j] in txt(pre[iF]) for j in ENT if j != k and j in name): warn('delta', f'{k}: «Frente a…» no nombra a ninguna entidad del grupo')
        if iP is None: err('pg', f'{k}: preguntas guía (hb az + ol.pg) antes del primer h2')
        def first_after(lbl):
            it = [c for c, g in order if g == lbl and c.name != 'h2']
            return it[0] if it else None
        ep = [c for c, g in order if g == 'Epidemiología']
        tb = next((t for c in ep for t in ([c] if c.name == 'table' else c.select('table'))), None)
        EPI = ['Frecuencia', 'Edad', 'Sexo', 'Factores clave']
        if not tb: err('epidemiologia', f'{k}: Epidemiología sin tabla de 4 filas ({" · ".join(EPI)})')
        else:
            rows = tb.select('tbody > tr') or tb.find_all('tr')[1:]
            fc = [txt(r.find(['th', 'td'])) for r in rows if r.find(['th', 'td'])]
            if fc != EPI: err('epidemiologia', f'{k}: primera columna {fc} → exactamente {EPI}')
        for lbl, ctx in (('Diagnóstico', 'dx'), ('Tratamiento', 'tx')):
            fa = first_after(lbl)
            if fa is None or fa.name != 'ol' or not {'steps', 'tg'} <= set(fa.get('class') or []): err('pasos', f'{k}: el primer bloque bajo «{lbl}» debe ser <ol class="steps tg">')
        tls = s.select('ol.tl')
        if not tls: err('timeline', f'{k}: falta ol.tl bajo «Cadena»')
        for o in tls:
            if o.parent is not s or GRP.get(id(o)) != 'Cadena': err('timeline', f'{k}: ol.tl hija directa de la section y bajo h2 «Cadena»')
        qv = s.select('.qv')
        if len(qv) != 1 or GRP.get(id(top_of(qv[0], s))) != 'Qué verás': err('qv', f'{k}: exactamente una .qv bajo «Qué verás» (hay {len(qv)})')
        for sg in s.select('.signo'):
            if GRP.get(id(top_of(sg, s))) != 'Qué verás': err('signos', f'{k}: ficha .signo {sg.get("id")} fuera de «Qué verás»')
        fy = s.select('.fey'); dcs = [grp(d)[1] for d in s.select('.dc')]
        if k == 'e1':
            if len(fy) != 2: err('profundidad', f'e1 (principal): {len(fy)} Feynman (exactamente 2: tras «Cadena» y tras «Qué verás»)')
            for lbl in ('Diagnóstico', 'Tratamiento'):
                if lbl not in dcs: err('profundidad', f'e1 (principal): falta simulador .dc bajo «{lbl}»')
        else:
            if len(fy) != 1 or grp(fy[0])[1] != 'Cadena': err('profundidad', f'{k} (secundaria): exactamente 1 Feynman y bajo «Cadena» (hay {len(fy)})')
            if 'Tratamiento' not in dcs: err('profundidad', f'{k} (secundaria): falta simulador .dc bajo «Tratamiento»')
# --- preguntas guía, badge, Feynman
PGR = {}
for k in CONT:
    s = secs[k]; pg = s.select('ol.pg')
    if MODE == 'multi' and k == 'sin':
        if pg: err('pg', 'sin: sin preguntas guía')
        continue
    rng = (3, 3) if (MODE == 'multi' and k in ENT and k != 'e1') else (3, 5)
    if len(pg) != 1: err('pg', f'{k}: {len(pg)} listas ol.pg (debe ser 1)')
    else:
        n = len(pg[0].find_all('li', recursive=False))
        if not rng[0] <= n <= rng[1]: err('pg', f'{k}: {n} preguntas guía ({rng[0]}–{rng[1]})' if rng[0] != rng[1] else f'{k}: {n} preguntas guía (secundaria: exactamente 3)')
    if not s.select('.b-pu'): err('badge', f'{k}: falta <span class="badge b-pu"> de la guía rectora')
for s in S.select('section.tab'):
    k = s.get('data-tab')
    for i, fy in enumerate(s.select('.fey'), 1):
        if fy.find_parent(class_='acc'): err('feynman', f'{k}: Feynman {i} dentro de acordeón')
        b = fy.select_one('.fey-b'); cs = fy.select('.fey-c')
        if not b: err('feynman', f'{k}: Feynman {i} sin p.fey-b'); continue
        if words(txt(b)) > 90: err('feynman', f'{k}: Feynman {i} cuerpo {words(txt(b))} palabras (>90)')
        if re.search(r'\d', txt(b)): warn('feynman', f'{k}: Feynman {i} contiene dígitos (revisar cifras/dosis)')
        if len(cs) != 2 or not txt(cs[0]).startswith('En medicina esto se llama…') or not txt(cs[1]).startswith('Dónde falla la comparación:'):
            err('feynman', f'{k}: Feynman {i}: dos p.mini.fey-c «En medicina esto se llama…» y «Dónde falla la comparación:»')
if MODE == 'multi':
    for k in ('vis', 'sin'):
        if k in secs and secs[k].select('.fey'): err('feynman', f'{k}: sin Feynman')
# --- simuladores
for dc in S.select('.dc'):
    fn = dc.get('data-fn') or ''
    m = re.search(r'function\s+' + re.escape(fn) + r'\s*\([^)]*\)\s*\{', scripts) if fn else None
    if not m: err('simulador', f'.dc sin función definida: {fn or "(sin data-fn)"}')
    else:
        i, d = m.end(), 1
        while i < len(scripts) and d:
            d += {'{': 1, '}': -1}.get(scripts[i], 0); i += 1
        body = scripts[m.end():i]
        if not re.search(r'\bcf\b', body): warn('contrafactual', f'{fn}: la salida no termina en <span class="cf">Si … → …</span>')
        if re.search(r'num\(\s*dc\s*,\s*[\'"](?:peso|kg)[\'"]\s*\)', body) and 'Math.min' not in body: warn('tope', f'{fn}: dosis por peso sin tope: Math.min(dosis, máxima del adulto) y muestra el tope')
    if not dc.select_one('.out'): err('simulador', f'.dc {fn}: falta div.out')
    if not dc.select_one('.dc-t') or not txt(dc.select_one('.dc-t')).startswith('Simulador · Decisión clínica —'): err('simulador', f'.dc {fn}: div.dc-t «Simulador · Decisión clínica — …»')
    for c in dc.select('.chip'):
        if not c.get('data-g') or not c.get('data-v') or 'ch(this)' not in (c.get('onclick') or ''): err('simulador', f'.dc {fn}: chip con data-g, data-v y onclick="ch(this)"')
    for i2 in dc.select('input[type=number]'):
        if not i2.get('data-n') or 'ch(this)' not in (i2.get('oninput') or ''): err('simulador', f'.dc {fn}: input con data-n y oninput="ch(this)"')
DCT = [k for k in CONT if secs[k].select('.dc')]
if MODE == 'mono':
    for k in ('dx', 'tx', 'seg'):
        if k in secs and not secs[k].select('.dc'): err('simulador', f'{k}: falta Simulador · Decisión clínica')
    for k in DCT:
        if k not in ('dx', 'tx', 'seg'): warn('simulador', f'{k}: simulador fuera de pestaña de plan')
else:
    if 'vis' in secs:
        n = len(secs['vis'].select('.dc'))
        if n != 1: err('simulador', f'vis: {n} simuladores (exactamente 1, diferencial)')
        elif 'predic' not in txt(secs['vis'].select_one('.dc')).lower(): warn('simulador', 'vis: el rótulo del diferencial debe pedir predecir antes de pulsar')
    if 'sin' in secs and secs['sin'].select('.dc'): err('simulador', 'sin: sin simuladores')
# --- ids y contrato m↔s
ids = [t.get('id') for t in S.find_all(id=True)]
dup = sorted({i for i in ids if ids.count(i) > 1})
if dup: err('ids', f'ids duplicados: {dup}')
where = {}
for s in secl:
    for t in s.find_all(id=True): where[t['id']] = s.get('data-tab')
nodos, signos = S.select('.nodo'), S.select('.signo')
seq = {}
for el, kd, home in [(n, 'm', 'fis') for n in nodos] + [(g, 's', 'cli') for g in signos]:
    i = el.get('id', ''); k = (el.find_parent('section', class_='tab') or {}).get('data-tab')
    m = IDRE.match(i)
    pref = f'{k}-' if MODE == 'multi' else ''
    if MODE == 'mono' and k != home: err('ids', f'{i or kd}: {"nodos" if kd == "m" else "signos"} solo en {home}')
    if MODE == 'multi' and k not in ENT: err('ids', f'{i or kd}: {"nodos" if kd == "m" else "signos"} solo en pestañas eK')
    if not m or m.group(2) != kd: err('ids', f'id inválido «{i}» en {k}: usa «{pref}{kd}-n»'); continue
    if (m.group(1) or '') + ('-' if m.group(1) else '') != pref:
        err('ids', f'id «{i}» en la sección {k}: ' + (f'el prefijo debe ser «{k}-» → «{k}-{kd}-{m.group(3)}»' if MODE == 'multi' else f'mono sin prefijo → «{kd}-{m.group(3)}»'))
    seq.setdefault((k, kd), []).append(int(m.group(3)))
for (k, kd), ns in seq.items():
    if ns != list(range(1, len(ns) + 1)):
        p = f'{k}-' if MODE == 'multi' else ''
        err('ids', f'{k}: numeración {kd} {ns} → {p}{kd}-1…{p}{kd}-{len(ns)} consecutiva en orden DOM')
for k, s in secs.items():
    for o in s.select('ol.tl'):
        if o.parent is not s: err('timeline', f'{k}: cada ol.tl debe ser hija directa de la section')
    if len(s.select('li.nodo')) != len(s.select('ol.tl > li.nodo')) or len(s.select('.nodo')) != len(s.select('li.nodo')): err('timeline', f'{k}: todo .nodo es <li class="nodo"> hijo directo de ol.tl')
if MODE == 'mono' and 'fis' in secs and not secs['fis'].select('ol.tl'): err('timeline', 'fis: falta ol.tl')
for n in nodos:
    i = n.get('id')
    if n.get('data-clin') not in ('0', '1'): err('nodos', f'{i}: data-clin="0|1"')
    if not n.get('data-paso'): err('nodos', f'{i}: data-paso ausente (≤8 palabras, lo usa la timeline en blanco)')
    if not n.select_one('.det'): err('nodos', f'{i}: falta div.det')
    if n.select('.paso'): err('nodos', f'{i}: no escribas .paso; lo genera el kit')
    if n.select('.nodo'): err('nodos', f'{i}: nodo anidado (timeline plana; usa data-rama)')
for t in nodos + signos:
    if t.find_parent(class_='acc'): err('ids', f'{t.get("id")} dentro de acordeón')
links = {}
for x in S.select('.xref'):
    tgt = x.get('data-ir'); oc = (x.get('onclick') or '').strip()
    if not tgt or tgt not in where: err('enlaces', f'xref a id inexistente: {tgt}'); continue
    ex = f"ir('{where[tgt]}','{tgt}')"
    if oc != ex: err('enlaces', f'xref {tgt}: onclick="{oc}" → onclick="{ex}"')
    src = (x.find_parent('section', class_='tab') or {}).get('data-tab')
    if MODE == 'multi' and src in ENT and where[tgt] in ENT and src != where[tgt]:
        err('enlaces', f'{src}: xref a {tgt} (otra entidad): los enlaces m↔s son intra-entidad; el contraste va en vis')
    own = x.find_parent(class_=['nodo', 'signo'])
    if own is not None and own.get('id'): links.setdefault(own['id'], []).append(tgt)
for n in nodos:
    Ls = [t for t in links.get(n.get('id'), []) if kind(t) == 's']
    if n.get('data-clin') == '1':
        if not Ls: err('enlaces', f'{n.get("id")} (data-clin="1") sin xref a signo en p.man')
        mn = n.select_one('.man')
        if not mn: err('enlaces', f'{n.get("id")} (data-clin="1") sin <p class="man">Se manifiesta como: …</p>')
        elif mn.select('.xref') != [x for x in n.select('.xref') if kind(x.get('data-ir')) == 's']: warn('enlaces', f'{n.get("id")}: xref a signos fuera de p.man')
    if len(Ls) > 3: err('enlaces', f'{n.get("id")}: {len(Ls)} xref a signos (máx 3)')
for g in signos:
    Lm = [t for t in links.get(g.get('id'), []) if kind(t) == 'm']
    if not Lm and 'Mecanismo no establecido' not in txt(g): err('enlaces', f'{g.get("id")}: sin xref a su nodo (o p.mini «Mecanismo no establecido»)')
    if len(Lm) > 2: err('enlaces', f'{g.get("id")}: {len(Lm)} xref a nodos (máx 2)')
    if len(g.select('dt')) < 3: err('signos', f'{g.get("id")}: ficha con menos de 3 dt')
for a, Lx in links.items():
    for b in Lx:
        if kind(a) and kind(b) and kind(a) != kind(b) and a not in links.get(b, []): err('reciprocidad', f'enlace no recíproco {a}→{b}: añade en {b} un xref a {a}')
# --- pasos etiquetados
DX = ['1.º', 'Añade', 'Confirma', 'Solo si', 'No pidas', 'Alarma']
TX = ['Principio', 'De elección', 'Alternativa', 'Sintomático', 'Escala', 'Reevalúa', 'Especialista', 'Evita']
DOSE = re.compile(r'\d+(?:[.,]\d+)?\s*(?:mg|µg|μg|mcg|g|UI|mL|ml)(?:/kg)?(?!\w)(?!/d?L\b)')
TGL = {}
for o in S.select('ol.tg'):
    k, g = grp(o) if MODE == 'multi' else ((o.find_parent('section', class_='tab') or {}).get('data-tab'), None)
    if 'steps' not in (o.get('class') or []): err('pasos', f'{k}: usa <ol class="steps tg">')
    if MODE == 'mono': ctx = {'dx': 'dx', 'tx': 'tx'}.get(k)
    else: ctx = 'dx' if k == 'vis' or g == 'Diagnóstico' else ('tx' if g == 'Tratamiento' else None)
    lab = f'{k}' + (f'/{g}' if g else '')
    if not ctx: err('pasos', f'{lab}: ol.steps.tg solo en ' + ('dx y tx' if MODE == 'mono' else 'vis, «Diagnóstico» y «Tratamiento»')); continue
    V, O = (DX, TX) if ctx == 'dx' else (TX, DX)
    got = []
    for li in o.find_all('li', recursive=False):
        first = next((c for c in li.contents if not (isinstance(c, str) and not c.strip())), None)
        if not (isinstance(first, Tag) and first.name == 'span' and 'tg' in (first.get('class') or [])):
            err('pasos', f'{lab}: cada <li> empieza por <span class="tg">…</span> sin texto previo'); continue
        t = txt(first); got.append(t)
        if t in V: pass
        elif t in O: err('pasos', f'{lab}: «{t}» es etiqueta {"tx" if ctx == "dx" else "dx"}; aquí: {" · ".join(V)}')
        elif nz(t) in {nz(v) for v in V}:
            v = next(v for v in V if nz(v) == nz(t)); err('pasos', f'{lab}: etiqueta «{t}» → escribe literal «{v}»' + (' (º es U+00BA)' if v == '1.º' else ''))
        else: err('pasos', f'{lab}: etiqueta «{t}» fuera del vocabulario {ctx}: {" · ".join(V)}')
        dm = DOSE.search(txt(li))
        if dm: err('pasos', f'{lab}: dosis «{dm.group(0)}» en la lista: nombra el fármaco y remite a la tabla (fuente única)')
    key = '1.º' if ctx == 'dx' else 'De elección'
    if got.count(key) != 1: err('pasos', f'{lab}: {got.count(key)} pasos «{key}» (exactamente 1)')
    TGL.setdefault((k, ctx), set()).update(got)
if MODE == 'mono':
    for k in ('dx', 'tx'):
        if k in secs and not secs[k].select('ol.steps.tg'): err('pasos', f'{k}: falta <ol class="steps tg"> al inicio (pasos etiquetados)')
elif 'vis' in secs and len(secs['vis'].select('ol.steps.tg')) != 1: err('pasos', 'vis: exactamente un <ol class="steps tg"> (diferencial, vocabulario dx)')
# --- Qué verás
for q in S.select('.qv'):
    k, g = grp(q) if MODE == 'multi' else ((q.find_parent('section', class_='tab') or {}).get('data-tab'), None)
    if MODE == 'mono' and k != 'cli': err('qv', f'{k}: .qv solo en cli')
    cs = kids(q)
    if any(c.name != 'p' or c.get('data-e') not in ('p', 'v', 'a', 'k') for c in cs): err('qv', f'{k}: .qv solo con <p data-e="p|v|a|k">')
    ek = [c for c in cs if c.get('data-e') == 'k']
    if len(ek) != 1: err('qv', f'{k}: .qv con {len(ek)} celdas data-e="k" (exactamente 1)')
    if len(cs) - len(ek) < 4: err('qv', f'{k}: .qv con {len(cs) - len(ek)} celdas de estado (mínimo 4)')
    for c in cs:
        if re.match(r'(Presente|Variable|Ausente|Signo clave)\b', txt(c), re.I): err('qv', f'{k}: no escribas el estado («{txt(c)[:20]}»): lo pone el CSS')
    if ek and not ek[0].select('.xref'): warn('qv', f'{k}: la celda k suele llevar xref a su ficha .signo')
# --- discrepancia
for h in S.select('.hb.vi'):
    cs = kids(h); t = [c for c in cs if 'hb-t' in (c.get('class') or [])]; p = [c for c in cs if c.name == 'p']
    if len(t) != 1 or len(p) != 1 or len(cs) != 2: err('discrepancia', 'hb vi: exactamente <div class="hb-t">Discrepancia: …</div><p>fuente → error → [n] → <b>regla</b></p>')
    if not CIT.search(txt(h)): err('discrepancia', 'hb vi sin cita [n]')
    if p and words(txt(p[0])) > 110: warn('discrepancia', f'hb vi: {words(txt(p[0]))} palabras (>110)')
    if p and not p[0].select('b,strong'): warn('discrepancia', 'hb vi: la regla correcta va en <b>')
# --- vis y sin (multi)
POS = {id(t): i for i, t in enumerate(S.find_all(True))}
VIS9 = ['Falla central', 'Terreno típico', 'Inicio y curso', 'Síntoma compartido aquí', 'Signo que la delata', 'Negativo pertinente', 'Prueba que decide', 'Conducta inicial y quién maneja', 'Amenaza si se pierde']
if MODE == 'multi' and 'vis' in secs:
    v = secs['vis']; tv = v.select('table.vis')
    if len(tv) != 1: err('vis', f'vis: {len(tv)} table.vis (exactamente 1)')
    else:
        t = tv[0]
        if 'tw' not in (t.parent.get('class') or []): err('vis', 'table.vis dentro de <div class="tw">')
        tr = t.find_all('tr'); hc = [txt(c) for c in tr[0].find_all(['th', 'td'])] if tr else []
        exh = [name.get(k) for k in ENT]
        if hc[1:] != exh: err('vis', f'vis: cabeceras {hc[1:]} → textos de los botones {exh} (primera celda libre)')
        rows = t.select('tbody > tr') or tr[1:]
        lab = [txt(r.find(['th', 'td'])) for r in rows]
        if lab != VIS9: err('vis', f'vis: filas {lab} → exactamente, en orden: {" · ".join(VIS9)}')
        for r in rows:
            cs = r.find_all(['th', 'td'])
            if len(cs) != N + 1: err('vis', f'vis: fila «{txt(cs[0]) if cs else ""}» con {len(cs)} celdas (N+1 = {N + 1})')
            for c in cs[1:]:
                if not txt(c): err('vis', f'vis: celda vacía en «{txt(cs[0])}»')
                elif words(txt(c)) > 12: warn('vis', f'vis: celda de {words(txt(c))} palabras en «{txt(cs[0])}» (≤12)')
    ro = v.select('.hb.ro')
    if not ro: err('vis', 'vis: falta hb ro (banderas rojas)')
    seqv = [v.select_one(x) for x in ('table.vis', '.hb.ro', 'ol.steps.tg', '.dc')]
    if all(seqv) and [POS[id(x)] for x in seqv] != sorted(POS[id(x)] for x in seqv): warn('vis', 'vis: orden tabla → hb ro → ol.steps.tg → simulador')
    if M and M.get('amenaza') in ENT and M.get('amenaza') != 'e1' and ro:
        am = M['amenaza']; f1 = next((x for x in ro[0].select('li,p') if 'hb-t' not in (x.get('class') or [])), None)
        if not f1 or name.get(am, '§') not in txt(f1): err('amenaza', f'vis: el primer ítem de hb ro debe nombrar la amenaza «{name.get(am)}»')
        if 'Alarma' not in TGL.get((am, 'dx'), set()): err('amenaza', f'{am} (amenaza ≠ e1): paso «Alarma» obligatorio en «Diagnóstico»')
        if 'Evita' not in TGL.get((am, 'tx'), set()): err('amenaza', f'{am} (amenaza ≠ e1): paso «Evita» obligatorio en «Tratamiento»')
if MODE == 'multi' and 'sin' in secs:
    ks = kids(secs['sin']); ok_ro = ok_rf = 0
    for c in ks:
        c_ = set(c.get('class') or [])
        if {'hb', 'ro'} <= c_ and c.select_one('.hb-t') and txt(c.select_one('.hb-t')).startswith('Errores que no se pueden cometer'): ok_ro += 1
        elif {'acc', 'refs'} <= c_: ok_rf += 1
        else: err('sin', f'sin: <{c.name} class="{cls(c)}"> no permitido; solo hb ro «Errores que no se pueden cometer» y .acc.refs (el kit pone los botones)')
    if ok_ro != 1: err('sin', 'sin: exactamente un <div class="hb ro"><div class="hb-t">Errores que no se pueden cometer</div>…')
for rf in S.select('.acc.refs'):
    k = (rf.find_parent('section', class_='tab') or {}).get('data-tab')
    if k != REFTAB: err('refs', f'.acc.refs en {k}: va en {REFTAB}')
if not S.select('.acc.refs'): err('refs', f'falta .acc.refs con ol.vanc en {REFTAB}')
# --- Vancouver
refs = S.select('ol.vanc > li'); seen = []
for k in CONT:
    for m in CIT.finditer(txt(secs[k])):
        for part in re.split(r'\s*,\s*', m.group(0)[1:-1]):
            a = re.split(r'\s*[–-]\s*', part)
            for n in range(int(a[0]), int(a[-1]) + 1):
                if n not in seen: seen.append(n)
bad = next((i for i, n in enumerate(seen) if n != i + 1), None)
if bad is not None: err('vancouver', f'primera cita fuera de orden: [{seen[bad]}] donde tocaba [{bad + 1}]; renumera por primera aparición (barra {" ".join(CONT)}; pan reutiliza)')
if len(refs) != len(seen): err('vancouver', f'lista Vancouver: {len(refs)} ítems vs {len(seen)} citas')
if pan and any(int(x) > len(refs) for x in re.findall(r'\[(\d+)\]', txt(pan))): err('vancouver', 'Panorama cita un número inexistente')
# --- orden de apertura, Feynman en def (mono), remisiones y posología fuera de tabla
if MODE == 'mono' and 'def' in secs and len(secs['def'].select('.fey')) != 1: err('feynman', f'def: {len(secs["def"].select(".fey"))} Feynman (exactamente 1)')
for k in CONT:
    if MODE == 'multi' and k in ENT + ['sin']: continue
    c0 = next(iter(kids(secs[k])), None)
    if c0 is not None and not ({'hb', 'az'} <= set(c0.get('class') or []) and c0.select_one('ol.pg')):
        warn('orden', f'{k}: la primera caja debe ser el hb az de preguntas guía (sin highlight previo)')
for r in S.select('span.rem'):
    k, g = grp(r) if MODE == 'multi' else ((r.find_parent('section', class_='tab') or {}).get('data-tab'), None)
    mt = re.search(r'«([^»]+)»', txt(r))
    if not mt or not k: continue
    tg_ = mt.group(1).strip()
    if tg_ == name.get(k) or (g and tg_ == g): err('remision', f'{k}{"/" + g if g else ""}: «{txt(r)}» apunta a la propia pestaña → <span class="rem">↓ En la tabla</span>')
for k in ['pan'] + CONT:
    if k not in secs: continue
    cp = BeautifulSoup(str(secs[k]), 'html.parser')
    for x in cp.select('.dc,.out,script,code,ol.tg,.acc.refs'): x.decompose()
    for tb in cp.select('table'): tb.decompose()  # umbrales en tablas de criterios no son posología
    dm = DOSE.search(txt(cp))
    if dm: warn('posologia', f'{k}: posología fuera de la tabla de fármacos («{dm.group(0)}»): remite con span.rem')
# --- palabras por pestaña (aviso; umbrales no calibrados)
LIM = {'vis': 1200, 'e1': 2800} if MODE == 'multi' else {}
WC = {k: words(txt(secs[k])) - sum(words(txt(x)) for x in secs[k].select('.acc.refs,.out')) for k in CONT}
for k in CONT:
    lim = LIM.get(k, 1200 if MODE == 'multi' else 2500)
    if WC[k] > lim: warn('palabras', f'{k}: {WC[k]} palabras (>{lim}): lo común va una vez en vis; recorta repeticiones')
    if MODE == 'multi' and k in ENT and k != 'e1' and WC.get('e1') and WC[k] > 0.8 * WC['e1']: warn('palabras', f'{k}: {WC[k]} palabras >80 % de e1 ({WC["e1"]}): la secundaria es delta, no monografía')
# --- clases
css = ' '.join(s.string or '' for s in S.find_all('style'))
known = set(re.findall(r'\.([a-zA-Z][\w-]*)', css)) | {'rama', 'refs'}
for t in L.find_all(class_=True):
    for c in t['class']:
        if c not in known: warn('clases', f'.{c} sin CSS en el kit')
# --- manifiesto
if MODE == 'mono':
    cnt = {'tabs': tbs, 'pg': {k: len(secs[k].select('ol.pg > li')) for k in CONT if secs[k].select('ol.pg > li')}, 'fey': {k: len(secs[k].select('.fey')) for k in CONT if secs[k].select('.fey')},
           'nodos': len(nodos), 'signos': len(signos), 'dc': DCT}
else:
    cnt = {'entidades': {k: name[k] for k in ENT}, 'tabs': tbs, 'pg': {k: len(secs[k].select('ol.pg > li')) for k in CONT if secs[k].select('ol.pg > li')},
           'fey': {k: len(secs[k].select('.fey')) for k in CONT if secs[k].select('.fey')}, 'nodos': {k: len(secs[k].select('.nodo')) for k in ENT if k in secs},
           'signos': {k: len(secs[k].select('.signo')) for k in ENT if k in secs}, 'dc': DCT}
if M is not None:
    ALL = ['modo', 'entidades', 'principal', 'amenaza', 'tabs', 'pg', 'fey', 'nodos', 'signos', 'dc', 'nucleo']
    for key in M:
        if key not in ALL: err('manifiesto', f'clave desconocida "{key}" (permitidas: {", ".join(ALL)})')
    req = ALL if MODE == 'multi' else ['tabs', 'pg', 'fey', 'nodos', 'signos', 'dc']
    for key in req:
        if key not in M: err('manifiesto', f'falta la clave "{key}"')
    if MODE == 'mono' and 'nucleo' not in M: warn('manifiesto', 'falta "nucleo" (lista ≤12)')
    for key in ('pg', 'fey'):
        if isinstance(M.get(key), dict):
            for k in M[key]:
                if k not in CONT: err('manifiesto', f'{key}: clave "{k}" no es pestaña de contenido ({", ".join(CONT)})')
            if {k: v for k, v in M[key].items() if v != 0} == {k: v for k, v in cnt[key].items() if v}: M[key] = cnt[key]
    for key, v in cnt.items():
        if key in M and M[key] != v: err('manifiesto', f'{key}: manifiesto {json.dumps(M[key], ensure_ascii=False)} ≠ HTML {json.dumps(v, ensure_ascii=False)}')
    if MODE == 'multi':
        if 'principal' in M and M['principal'] != 'e1': err('manifiesto', f'"principal":"{M["principal"]}" → "principal":"e1" (la principal es e1 por convención)')
        if 'amenaza' in M and M['amenaza'] not in ENT: err('manifiesto', f'"amenaza":"{M["amenaza"]}" no es una entidad ({", ".join(ENT)})')
    nu = M.get('nucleo')
    def hay(el): return txt(el) + ' ' + ' '.join(n.get('data-paso', '') for n in el.select('[data-paso]'))
    if nu is not None:
        if MODE == 'mono':
            if not isinstance(nu, list) or len(nu) > 12 or not all(isinstance(x, str) for x in nu): err('nucleo', 'mono: "nucleo" lista de ≤12 cadenas')
            else:
                for x in nu:
                    if nz(x) not in nz(hay(S)): warn('nucleo', f'«{x}» no aparece en el widget')
        else:
            if not isinstance(nu, dict) or sorted(k for k in nu if k != 'vis') != sorted(ENT): err('nucleo', f'multi: "nucleo" objeto con claves {ENT} (+ "vis" opcional)')
            else:
                for k, lst in nu.items():
                    mx = 5 if k == 'vis' else 7
                    if not isinstance(lst, list) or len(lst) > mx: err('nucleo', f'{k}: núcleo con {len(lst) if isinstance(lst, list) else "?"} ítems (≤{mx})')
                    else:
                        for x in lst:
                            if nz(str(x)) not in nz(hay(secs.get(k, S)) + ' ' + hay(secs.get('vis', S))): warn('nucleo', f'{k}: «{x}» no aparece en {k} ni en vis')
# --- salida (≤25 líneas)
print(json.dumps(cnt, ensure_ascii=False, separators=(',', ':'))[:400])
ne, nw = sum(map(len, E.values())), sum(map(len, W.values()))
def cut(s, n=400): return s if len(s) <= n else s[:n - 1] + '…'
wl = [cut(f'AVISO [{c}] ×{len(v)}: ' + ' | '.join(v[:3]) + (f' | +{len(v) - 3} más' if len(v) > 3 else ''), 300) for c, v in W.items()]
el = [f'ERROR [{c}]: {m}' for c, v in E.items() for m in v]
if len(el) + len(wl) > 23: el = [cut(f'ERROR [{c}] ×{len(v)}: ' + ' ‖ '.join(v)) for c, v in E.items()]
out = el + wl
if len(out) > 23: out = out[:22] + [f'… {len(out) - 22} líneas más omitidas (corrige y reejecuta)']
for x in out: print(x)
print(f'RESULTADO: {"OK" if not E else "FALLA"} · errores {ne} · avisos {nw} · JS {js_ok} · modo {MODE}')
sys.exit(1 if E else 0)
````
