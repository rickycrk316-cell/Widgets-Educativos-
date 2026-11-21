function dcE3tx(dc){
  var t=sel(dc,'tipo'),f=sel(dc,'fase'),z=sel(dc,'zona'),g=sel(dc,'ag'),sc=num(dc,'sc');
  function e3par(x){return '<p>'+x+'</p>';}
  function e3hv(a,v){return a.indexOf(v)>-1;}
  if(!t.length&&!f.length&&!z.length&&!g.length&&isNaN(sc)){
    out(dc,e3par('Elige el tipo, la fase, la zona y la superficie afectada. El simulador propone el tratamiento con su posología; no calcula probabilidades.'));return;}
  var r=[];
  var TRI='triamcinolona 0,1 % crema, una capa sobre la zona afectada, tópica, 2 a 3 veces al día, hasta resolver [@e3_dm_triamcinolona]';
  var CLO='clobetasol 0,05 % crema, capa fina, tópica, 2 veces al día, máximo 2 semanas seguidas y 50 g por semana, sin oclusión y nunca en cara, ingle ni axilas [@e3_dm_clobetasol]';
  var PRE='prednisona VO en dosis única por la mañana, con dosis inicial entre 5 y 60 mg al día según la gravedad (rango de la ficha) y descenso gradual en 2 a 3 semanas [@e3_usatine2010][@e3_dm_prednisona]';
  var cara=e3hv(z,'cara');
  var ext=!isNaN(sc)&&sc>20;
  if(e3hv(t,'irr')){
    r.push(e3par('<b>Irritativa</b>: daño directo sin inmunidad específica. Identifica y evita el irritante, usa barreras en el trabajo y emoliente de forma regular [@e3_bains2019][@e3_patel2022].'));
  }
  if(e3hv(t,'ale')){
    r.push(e3par('<b>Alérgica</b> (tipo IV): el pilar es evitar el alérgeno, que no se pierde por la memoria de los linfocitos T; el corticoide alivia el brote pero no previene la recaída [@e3_usatine2010].'));
  }
  if(e3hv(g,'desc')||(!e3hv(t,'irr')&&e3hv(f,'cro'))){
    r.push(e3par('Agente desconocido o cuadro crónico: si no cede al retirar lo sospechoso, deriva a la prueba del parche con lectura a las 48 h y a las 72–96 h; exige relevancia clínica y no se coloca sobre piel con corticoide [@e3_usatine2010][@e3_fonacierpg2015][@e3_matiz2011].'));
  }
  if(e3hv(f,'agu')){
    r.push(e3par('<b>Aguda vesicular</b>: potencia media o alta en lesión localizada. '+(cara?'En cara o pliegues baja la potencia y evita el clobetasol [@e3_dm_clobetasol]; ↪ escalera de potencias en «Visión». ':'Primera línea: '+TRI+'; alternativa más potente: '+CLO+'. ')+'No rompas las ampollas [@e3_usatine2010].'));
  }
  if(e3hv(f,'cro')){
    r.push(e3par('<b>Crónica liquenificada</b>: la piel gruesa necesita mayor potencia en la placa, con emoliente y evitación sostenida. '+(cara?'En cara o pliegues evita el clobetasol y usa una potencia baja [@e3_dm_clobetasol]; ↪ escalera de potencias en «Visión».':'Opción: '+CLO+'; tras las 2 semanas pasa a '+TRI+' [@bolognia5].')));
  }
  if(!f.length&&!ext&&isNaN(sc)&&(t.length||z.length)){
    r.push(e3par('Elige la fase para fijar la potencia del corticoide tópico; ↪ escalera de potencias en «Visión».'));
  }
  if(!isNaN(sc)){
    if(ext) r.push(e3par('<b>Superficie de '+String(sc).replace('.',',')+' %</b>: supera el 20 %, por lo que suele requerir esteroide sistémico: '+PRE+'. No lo suspendas de golpe porque produce rebote [@e3_usatine2010].'));
    else r.push(e3par('<b>Superficie de '+String(sc).replace('.',',')+' %</b>: no pasa del 20 %, por lo que basta el corticoide tópico más evitación; no necesitas esteroide sistémico [@e3_usatine2010].'));
  }
  r.push('<span class="cf">Si la superficie supera el 20 % o el brote es grave → pasa de corticoide tópico a prednisona oral con descenso en 2 a 3 semanas; si no cede al evitar el agente o este se ignora → deriva a la prueba del parche [@e3_usatine2010].</span>');
  out(dc,r.join(''));
}
