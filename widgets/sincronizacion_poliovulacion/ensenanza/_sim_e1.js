function e1_hv(a,v){return a.indexOf(v)>=0;}
function e1_p(x){return '<p>'+x+'</p>';}

function dcE1d(dc){
  var e=sel(dc,'e'),d=sel(dc,'d');
  if(!e.length){out(dc,e1_p('Elige el estado ovárico de la hembra para decidir si es candidata a PGF2α.'));return;}
  var r=[];
  if(e1_hv(e,'gest')){
    r.push(e1_p('<b>No es candidata: hembra gestante.</b> La PGF2α destruye el cuerpo lúteo que mantiene la gestación y provoca aborto [@diapos][@frandson]. Confirma antes de inyectar: palpación rectal o ecografía y, si hay duda, progesterona sérica [@noakes].'));
    r.push('<span class="cf">Si no puedes descartar la gestación (sin registro de servicio ni ecografía) → no inyectes PGF2α; confirma primero con ecografía [@noakes].</span>');
  } else if(e1_hv(e,'cl')){
    r.push(e1_p('<b>Candidata.</b> Cuerpo lúteo maduro (aprox. día 5–17 del ciclo bovino) y no gestante: la PGF2α provoca luteólisis y el celo llega en pocos días [@diapos][@frandson].'));
    if(e1_hv(d,'celo')) r.push(e1_p('El registro de celos anteriores ayuda a ubicar la hembra en el ciclo; aun así confirma el CL por ecografía o palpación [@diapos].'));
    if(e1_hv(d,'p4')) r.push(e1_p('Progesterona sérica alta apoya CL funcional; no distingue por sí sola ciclando de gestante: descarta la gestación [@noakes].'));
    r.push('<span class="cf">Si el CL se ve pero la hembra pudo ser servida en el último ciclo → verifica gestación antes de inyectar; si es negativa → PGF2α y celo en pocos días [@diapos].</span>');
  } else if(e1_hv(e,'clj')){
    r.push(e1_p('<b>No candidata todavía: CL joven (primeros días tras la ovulación).</b> El CL es refractario a la PGF2α los primeros días y no regresa; la inyección no sincroniza nada [@frandson][@wiltbank2014]. Espera unos días y repite la evaluación.'));
    r.push(e1_p('Por eso los protocolos de 2 dosis separan las inyecciones 11–14 días: tras la primera, todas las hembras ciclando tienen un CL maduro a la segunda [@diapos].'));
    r.push('<span class="cf">Si la hembra tiene CL joven → no inyectes; si usas el esquema de 2 dosis, la 2.ª cae cuando el CL ya es sensible [@diapos].</span>');
  } else {
    r.push(e1_p('<b>No candidata: anestro (sin CL).</b> Sin cuerpo lúteo no hay receptor de PGF2α ni luteólisis que provocar; la hormona no inicia la ciclicidad [@diapos]. Corrige la causa (condición corporal, posparto, lactación) o usa un progestágeno o GnRH [@bo2014].'));
    r.push('<span class="cf">Si la ecografía no muestra CL ni folículo en crecimiento → no uses PGF2α; si aparece un CL → es candidata [@bo2014].</span>');
  }
  out(dc,r.join(''));
}

function dcE1t(dc){
  var s=sel(dc,'s'),c=sel(dc,'c');
  if(!s.length){out(dc,e1_p('Elige la especie para obtener el protocolo con PGF2α y su dosis.'));return;}
  var r=[],iatf=e1_hv(c,'iatf'),gest=e1_hv(c,'gest');
  if(gest){
    r.push(e1_p('<b>Alto: posible gestación.</b> No uses PGF2α hasta confirmar que la hembra está vacía: causa aborto [@diapos]. Con el protocolo de 2 dosis, las hembras gestantes del grupo abortan en la segunda inyección.'));
  }
  if(e1_hv(s,'bov')){
    if(iatf){
      r.push(e1_p('<b>Bovino, 2 dosis + IATF:</b> cloprostenol 500 µg IM (o dinoprost 25 mg IM) en el día 0 y otra dosis igual 11–14 días después; IATF a 72 y 96 h o una sola a 72–80 h tras la segunda [@diapos][@cimavet].'));
    } else if(e1_hv(c,'det')){
      r.push(e1_p('<b>Bovino, 1 dosis con detección de CL:</b> cloprostenol 500 µg IM (o dinoprost 25 mg IM) a las hembras con CL; observa celo 5–7 días e insemina a celo detectado [@diapos][@cimavet].'));
    } else {
      r.push(e1_p('<b>Bovino, 1 dosis + observación + 2.ª dosis:</b> una dosis (cloprostenol 500 µg IM), observa celos 5 días e insemina las positivas; a las no vistas, 2.ª dosis a los 11–14 días y observa 5–7 días [@diapos][@cimavet].'));
    }
  } else if(e1_hv(s,'equ')){
    r.push(e1_p('<b>Yegua:</b> con CL en diestro, dinoprost 5 mg IM (o cloprostenol 250 µg IM [VERIFICAR EN FUENTE]); el celo y el servicio se programan según el esquema de la presentación (servicio 4–6 días) [@diapos][@cimavet].'));
  } else if(e1_hv(s,'ovi')){
    r.push(e1_p('<b>Oveja, 2 dosis:</b> cloprostenol 125 µg IM [VERIFICAR EN FUENTE] en dos tomas separadas por 10–14 días; el celo aparece a los 2–3 días y el servicio se programa en 4–6 días [@diapos][@cimavet] [VERIFICAR EN FUENTE el punto de partida del intervalo de servicio].'));
  } else {
    r.push(e1_p('<b>Cabra, 2 dosis:</b> cloprostenol 125 µg IM [VERIFICAR EN FUENTE] en dos tomas separadas por 11 días; celo a unas 50 h y servicio a 36–40 h [@diapos][@cimavet] [VERIFICAR EN FUENTE el punto de partida del servicio].'));
  }
  if(!gest) r.push(e1_p('Antes de inyectar, confirma que la hembra no está gestante; manipula el producto con guantes: la PGF2α es peligrosa para mujeres embarazadas y asmáticas [VERIFICAR EN FUENTE].'));
  r.push('<span class="cf">Si la hembra no muestra celo 5–7 días tras la dosis → revisa por ecografía si había CL maduro; si no lo había, no era candidata y no se repite la misma dosis [@diapos].</span>');
  out(dc,r.join(''));
}
