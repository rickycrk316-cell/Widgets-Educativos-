function vis_p(t){return '<p>'+t+'</p>';}
function vis_r(est,falta,cond){return vis_p('<b>Estrategia compatible</b>: '+est)+vis_p('<b>Falta confirmar</b>: '+falta)+vis_p('<b>Conducta inicial</b>: '+cond);}
function vis_has(a,v){return a.indexOf(v)>-1;}
function vis_esp(e,c){
  var m={vaq:'bov',lec:'bov',car:'bov',cerda:'por',yegua:'equ',peqest:'peq',peqfuera:'peq'};
  var s=e[0]||(c.length?m[c[0]]:'');
  return s;
}
function vis_choque(e,c){
  if(!e.length||!c.length)return false;
  var m={vaq:'bov',lec:'bov',car:'bov',cerda:'por',yegua:'equ'};
  var k=c[0];
  if(k==='peqest'||k==='peqfuera')return !(e[0]==='ovi'||e[0]==='cap');
  return m[k]!==e[0];
}
function dcVis(dc){
  var e=sel(dc,'esp'),c=sel(dc,'cat'),o=sel(dc,'obj'),v=sel(dc,'ov');
  if(!(e.length||c.length||o.length||v.length)){
    out(dc,vis_p('Elige la especie o la categoría, el objetivo y el estado del ovario. El simulador propone la estrategia compatible, lo que falta confirmar y la conducta inicial; no calcula probabilidades.'));return;}
  if(vis_has(v,'gest')){
    out(dc,vis_r('ninguna: una hembra gestante no se sincroniza.','la gestación (ecografía o palpación) y la fecha de servicio [@frandson].','no apliques PGF2α, que provoca aborto; espera al parto o al diagnóstico de vacía [@diapos].')+'<span class="cf">Si la ecografía muestra que no hay gestación y sí cuerpo lúteo → la PGF2α vuelve a ser una opción [@diapos].</span>');return;}
  if(vis_choque(e,c)){
    out(dc,vis_p('La especie y la categoría elegidas no coinciden. Corrige una de las dos para obtener una estrategia.'));return;}
  var s=vis_esp(e,c),ob=o[0]||'',cl=vis_has(v,'cl'),sc=vis_has(v,'sincl'),ct=c[0]||'',r='',cf='';
  if(s==='peq'&&(e[0]==='ovi'||e[0]==='cap'))s=e[0];
  if(!s){out(dc,vis_p('Falta la especie o la categoría. Elígela para decidir.'));return;}
  if(ob==='terec'){
    r=vis_r('sincronizar la receptora con la donante para que entren en celo el mismo día [@diapos].','que la receptora cicle, tenga útero sano y no esté gestante; el estado ovárico decide entre PGF2α (con cuerpo lúteo) y progestágeno (sin él) [@diapos].','aplica el protocolo de la especie con el calendario de la donante; la receptora no recibe FSH.');
    cf='Si la receptora no tiene cuerpo lúteo → la PGF2α no sirve y hay que usar un progestágeno [@diapos].';
  } else if(ob==='tedon'){
    if(s==='bov'){
      r=vis_r('poliovulación: FSH en dosis decrecientes cada 12 h durante 4–5 días, con PGF2α en dosis doble hacia el final y IA en celo; alternativa, eCG en dosis única con PGF2α y GnRH [@diapos][@bomapletoft2014].','que la donante cicle (cuerpo lúteo, folículos) y tenga buena condición corporal'+(sc?'; sin cuerpo lúteo la respuesta es impredecible: resuelve el anestro antes':'')+' [@bomapletoft2014].','inicia la FSH entre los días 9 y 12 del ciclo, con la donante bajo supervisión veterinaria [@diapos].');
      cf='Si la donante no tiene cuerpo lúteo al iniciar → la superovulación pierde sincronía y se pospone hasta confirmar el ciclo [@bomapletoft2014].';
    } else {
      r=vis_p('<b>Estrategia compatible</b>: la poliovulación en esta especie no figura en la presentación [@diapos].')+vis_p('<b>Falta confirmar</b>: el protocolo de superovulación de la especie [VERIFICAR EN FUENTE].')+vis_p('<b>Conducta inicial</b>: sincroniza el ciclo de la donante con la estrategia de su especie y consulta al especialista.');
      cf='Si la especie fuera bovina → la superovulación sería FSH decreciente con PGF2α en dosis doble [@diapos].';
    }
  } else if(s==='bov'){
    if(sc){
      r=vis_r('progestágeno (Crestar o CIDR) con eCG al retiro, útil en vaca de carne, Bos indicus y anéstricas [@bo2014][@diapos].','anestro real (ecografía y progesterona sérica), condición corporal y días posparto [@bo2014].','coloca el dispositivo, retira en la fecha y haz IATF o servicio al celo; sin dosis aquí: ver la pestaña «Progestágenos».');
      cf='Si la vaca mejora su condición corporal y aparece cuerpo lúteo → basta PGF2α o GnRH + PGF2α y se ahorra el dispositivo [@diapos].';
    } else if(cl&&ob==='conc'&&ct!=='car'){
      r=vis_r('PGF2α en una o dos dosis separadas 11–14 días, con observación de celo e IA de las positivas, o a tiempo fijo a las 72–96 h [@diapos].','la gestación y el cuerpo lúteo por ecografía o palpación [@frandson].','descarta gestación, inyecta y observa celos 5–7 días; cuadra el calendario de partos con el servicio.');
      cf='Si la ecografía no muestra cuerpo lúteo → la PGF2α no hace efecto y debes pasar a progestágeno o a GnRH + PGF2α [@diapos].';
    } else if(cl&&ct==='car'){
      r=vis_r('Cosynch (GnRH + PGF2α con IATF) o progestágeno con estradiol y eCG si hay anestro posparto [@bo2014][@diapos].','condición corporal, días posparto y cuerpo lúteo [@bo2014].','elige el esquema de unos 10 días con IATF; confirma que haya cuerpo lúteo antes de la PGF2α.');
      cf='Si la vaca es Bos indicus con baja condición corporal → conviene progestágeno con eCG y no solo PGF2α [@bo2014].';
    } else if(cl||ob==='iatf'){
      r=vis_r((ct==='lec'?'Ovsynch (con Presynch si el hato es lechero) ':'GnRH + PGF2α (Ovsynch, Cosynch, Select Synch o Heat Synch) ')+'con IATF [@pursley1995][@moreira2001][@diapos].','el folículo y el cuerpo lúteo por ecografía, y la gestación [@diapos].','respeta las horas exactas entre GnRH, PGF2α, segunda GnRH e IATF; veterinario o técnico entrenado.');
      cf='Si la vaca no tiene folículo respondedor a la primera GnRH → la ovulación a tiempo fijo falla; el Presynch mejora el punto de partida [@moreira2001].';
    } else {
      r=vis_p('<b>Estrategia compatible</b>: aún no se puede decidir; falta el estado ovárico.')+vis_p('<b>Falta confirmar</b>: cuerpo lúteo, folículos y gestación por ecografía o palpación [@frandson].')+vis_p('<b>Conducta inicial</b>: explora el ovario y vuelve a elegir.');
      cf='Si la exploración muestra cuerpo lúteo → PGF2α o GnRH + PGF2α; si no → progestágeno [@diapos].';
    }
  } else if(s==='equ'){
    if(sc){
      r=vis_r('Regumate (altrenogest) durante 15 días y PGF2α al final; celo en 4–6 días [@diapos].','que la yegua esté en época reproductiva y no gestante; ecografía del ovario [@noakes].','administra el progestágeno diario, inyecta PGF2α el último día y sigue el celo con teaser.');
      cf='Si la yegua está en anestro estacional profundo → el progestágeno no basta y hay que esperar la época reproductiva [@noakes].';
    } else if(ob==='iatf'){
      r=vis_r('GnRH + PGF2α en la yegua cíclica [@diapos].','cuerpo lúteo y folículo por ecografía [@diapos].','programa la inseminación según la ovulación seguida por ecografía.');
      cf='Si no hay cuerpo lúteo → la PGF2α no luteoliza y se pasa a progestágeno [@diapos].';
    } else {
      r=vis_r('PGF2α; la yegua entra en celo a los 4–6 días [@diapos].','cuerpo lúteo (diestro) y ausencia de gestación [@frandson].','descarta gestación, inyecta y vigila el celo para el servicio.');
      cf='Si la yegua está gestante → la PGF2α provoca aborto [@frandson].';
    }
  } else if(s==='ovi'||s==='cap'||s==='peq'){
    if(ct==='peqfuera'||sc){
      r=vis_r('progestágeno (CIDR o esponja) con eCG al retiro; celo tras el retiro [@diapos][@abecia2012].','que la hembra no esté gestante y la edad de la estación reproductiva [@abecia2012].','inserta el dispositivo, retíralo en la fecha y aplica eCG al retiro; servicio o IA según el celo.');
      cf='Si la hembra entra en estación con cuerpo lúteo → bastaría PGF2α con observación de celos [@diapos].';
    } else if(s==='ovi'){
      r=vis_r('PGF2α para la luteólisis, observación de celos y, si se quiere IA a tiempo fijo, inducción de la ovulación a las 17–24 h [@diapos].','cuerpo lúteo y estación reproductiva [@abecia2012].','inyecta PGF2α, observa celos y sirve a las positivas.');
      cf='Si la oveja está fuera de estación → no hay cuerpo lúteo y hay que usar progestágeno con eCG [@abecia2012].';
    } else {
      r=vis_r('en la cabra la presentación solo recoge progestágeno (CIDR o esponja) con eCG [@diapos].','la estación y la gestación [@abecia2012].','usa el dispositivo y la eCG al retiro; PGF2α en cabra [VERIFICAR EN FUENTE].');
      cf='Si la cabra tiene cuerpo lúteo en estación → la PGF2α luteoliza, pero su protocolo en cabra [VERIFICAR EN FUENTE].';
    }
  } else if(s==='por'){
    if(ct==='cerda'||ob==='iatf'){
      r=vis_r('GnRH + hCG con IA a tiempo fijo: GnRH 72–74 h tras el destete, hCG 24–26 h después, IA 16–18 h tras la hCG [@diapos].','destete reciente, condición corporal y celo posdestete [@knox2015].','aplica GnRH y hCG a las horas exactas y haz dos IA a tiempo fijo.');
      cf='Si es una cerda primeriza → primero altrenogest 18 días y luego GnRH + hCG [@diapos].';
    } else {
      r=vis_r('Regumate (altrenogest) durante 18 días en primerizas; celo 5–6 días después de retirarlo [@diapos].','que no estén gestantes y que sean primerizas cíclicas [@diapos].','administra el progestágeno diario y sirve en el celo.');
      cf='Si la cerda acaba de destetar → el progestágeno de 3 días o GnRH + hCG a tiempo fijo [@diapos].';
    }
  }
  out(dc,r+'<span class="cf">'+cf+'</span>');
}
