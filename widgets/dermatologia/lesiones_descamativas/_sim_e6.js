function dcE6tx(dc){
  var e=sel(dc,'ext'),s=sel(dc,'sit');
  function e6vacio(m){out(dc,'<p class="mini">'+m+'</p>');}
  function e6par(t){return '<p>'+t+'</p>';}
  function e6hv(a,v){return a.indexOf(v)>=0;}
  if(!e.length&&!s.length){
    e6vacio('Elige la extensión y la situación del paciente. El simulador propone el tratamiento con su posología; no calcula probabilidades.');return;}
  var KT='ketoconazol 2 % crema tópica 1 vez al día por 14 días, o ketoconazol 2 % champú 1 vez al día por 3 días o 1 vez por semana por 3 semanas [@e6_gupta2015]';
  var TB='terbinafina 1 % crema o solución tópica cada 12 h por 7 días [@e6_gupta2015]';
  var CX='ciclopirox 1 % crema cada 12 h por 14 días [@e6_gupta2015]';
  var SE='sulfuro de selenio 2,5 % en champú (pauta no establecida en la fuente revisada) [@e6_gupta2015]';
  var FL='fluconazol 300 mg VO una vez por semana por 2 semanas (alternativa: 400 mg en dosis única) [@e6_gupta2015]';
  var IT='itraconazol 200 mg VO cada 24 h por 5 a 7 días [@e6_gupta2015]';
  var PR='profilaxis: itraconazol 200 mg VO cada 12 h un día al mes por 6 meses, o sulfuro de selenio [@e6_gupta2015]';
  var r=[];
  var oral=e6hv(e,'ext')||e6hv(s,'recid')||e6hv(s,'fallo');
  if(e6hv(e,'lim')&&!oral){
    r.push(e6par('<b>Pitiriasis versicolor limitada</b>: tópico de primera línea. Elige '+KT+'; o '+TB+'; o '+CX+'; o '+SE+'.'));
  }
  if(oral){
    r.push(e6par('<b>'+(e6hv(e,'ext')?'Extensa':'Recurrente o con fracaso del tópico')+'</b>: antifúngico oral. De elección '+FL+'; alternativa '+IT+'. Se prefiere fluconazol por menos interacciones [@e6_gupta2015].'));
  }
  if(e6hv(s,'recid')) r.push(e6par('Recidivas frecuentes: tras la curación añade '+PR+'; la evidencia es limitada [@e6_gupta2015].'));
  if(e6hv(s,'tbo')) r.push(e6par('<b>Evita la terbinafina oral</b>: no es eficaz en pitiriasis versicolor (no se excreta en el sudor ni alcanza concentración suficiente en el estrato córneo); cámbiala por fluconazol o itraconazol, o por terbinafina tópica [@e6_gupta2015].'));
  if(e6hv(s,'kto')) r.push(e6par('<b>Evita el ketoconazol oral</b>: ya no se indica por hepatotoxicidad (cerca de 1 de cada 500) y las agencias de EE. UU. lo limitaron en 2013 a micosis sistémicas graves; usa fluconazol o itraconazol [@e6_gupta2015].'));
  r.push(e6par('Explica que el color tarda meses en normalizarse y que la recidiva es frecuente en clima cálido; reevalúa con KOH, no con el aspecto [@e6_gupta2015].'));
  r.push('<span class="cf">Si el KOH es negativo y la mancha clara no tiene escama → no es pitiriasis versicolor: piensa en vitíligo o pitiriasis alba y no des antifúngico; si la extensión o las recaídas aumentan → pasa de tópico a fluconazol o itraconazol oral [@e6_gupta2015][@e6_sepaskhah2017].</span>');
  out(dc,r.join(''));
}
