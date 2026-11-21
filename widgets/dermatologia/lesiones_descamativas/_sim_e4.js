function dcE4tx(dc){
  var g=sel(dc,'grav'),s=sel(dc,'sit'),b=num(dc,'bsa'),pa=num(dc,'pasi'),dl=num(dc,'dlqi'),pe=num(dc,'peso');
  function e4par(t){return '<p>'+t+'</p>';}
  function e4hv(a,v){return a.indexOf(v)>-1;}
  if(!g.length&&!s.length&&isNaN(b)&&isNaN(pa)&&isNaN(dl)){
    out(dc,e4par('Elige la gravedad (o escribe el BSA), la situación del paciente y, si lo tienes, PASI, DLQI y peso. El simulador propone el escalón de tratamiento con su posología; no calcula probabilidades.'));return;}
  var r=[];
  var zona=e4hv(s,'zona'),art=e4hv(s,'art'),emb=e4hv(s,'emb'),hep=e4hv(s,'hep'),ren=e4hv(s,'ren');
  if(e4hv(s,'alarma')){
    r.push(e4par('<b>Alarma</b>: eritrodermia o pústulas generalizadas con fiebre son una urgencia dermatológica. Deriva sin demora y <b>no uses corticoide sistémico</b>: al retirarlo puede producir un brote pustuloso o eritrodérmico [@bolognia5][@griffiths2021].'));
  }
  var mod=e4hv(g,'mod')||(!isNaN(b)&&b>=5)||zona||art;
  var leve=!mod&&(e4hv(g,'leve')||(!isNaN(b)&&b<5));
  if(leve){
    r.push(e4par('<b>Enfermedad leve'+(!isNaN(b)?' (BSA '+String(b).replace('.',',')+' %)':'')+'</b>: corticoide tópico más calcipotriol, aplicación fina una vez al día sobre la placa, con potencia del corticoide según la zona [@elmets2021]. Escalera de potencias en «Visión».'));
    if(!isNaN(b)&&b>=3) r.push(e4par('BSA entre 3 y 5 %: zona intermedia; si no responde en la reevaluación o aparece una zona especial, escala a fototerapia o sistémico [@elmets2021][@menter2019].'));
  }
  if(mod){
    r.push(e4par('<b>Moderada a grave'+(zona?' o con zona especial':'')+(art?' o con artritis':'')+'</b>: deriva a dermatología (y reumatología si hay artritis) y elige según comorbilidad [@menter2019][@griffiths2021].'));
    if(art) r.push(e4par('Con artritis psoriásica, prefiere un fármaco que trate también la articulación: anti-TNF o anti-IL-17, con cribado previo de TB y hepatitis [@menter2019][@e4_armstrong2020].'));
    var opc=[];
    opc.push('fototerapia NB-UVB, varias sesiones por semana en centro de fototerapia, con dosis según tipo de piel [@elmets2019foto]');
    if(!emb&&!hep&&!ren) opc.push('metotrexato 7,5–25 mg VO una vez por semana con ácido fólico 1–5 mg al día; vigila hemograma y función hepática [@menter2020]');
    if(!ren&&!emb){
      if(!isNaN(pe)&&pe>0){var ini=Math.min(Math.round(2.5*pe),Math.round(5*pe)),tope=Math.round(5*pe);
        opc.push('ciclosporina 2,5 mg/kg/día VO cada 12 h, es decir, '+ini+' mg al día con tope de 5 mg/kg/día ('+tope+' mg al día), a corto plazo [@menter2020]');}
      else opc.push('ciclosporina 2,5 mg/kg/día VO cada 12 h con tope de 5 mg/kg/día, a corto plazo; escribe el peso para calcular los mg [@menter2020]');
    }
    if(!emb&&!hep) opc.push('acitretina VO cada 24 h con dosis según ficha técnica, solo si no puede embarazarse [@menter2020]');
    opc.push('apremilast VO cada 12 h con titulación inicial según ficha técnica; vigila el ánimo [@menter2020]');
    opc.push('biológico (anti-TNF, anti-IL-17 o anti-IL-23) con esquema de la ficha técnica y cribado previo de TB y hepatitis [@menter2019]');
    r.push(e4par('Opciones: '+opc.join('; ')+'.'));
    if(emb) r.push(e4par('Embarazo o posible embarazo: evita metotrexato y acitretina (teratógenos); la fototerapia NB-UVB es una base posible; coordina el biológico con dermatología y obstetricia [@menter2020][@elmets2019foto].'));
    if(hep) r.push(e4par('Hepatopatía o alcohol: evita metotrexato y acitretina [@menter2020].'));
    if(ren) r.push(e4par('Insuficiencia renal o hipertensión: evita ciclosporina [@menter2020].'));
  }
  if(!isNaN(b)||!isNaN(pa)||!isNaN(dl)){
    var m=[];
    if(!isNaN(b)) m.push('BSA '+String(b).replace('.',',')+' %');
    if(!isNaN(pa)) m.push('PASI '+String(pa).replace('.',','));
    if(!isNaN(dl)) m.push('DLQI '+String(dl).replace('.',','));
    r.push(e4par('Registra '+m.join(', ')+' como línea de base para medir la respuesta en la reevaluación [@elmets2021].'));
  }
  r.push(e4par('Evita el corticoide sistémico y los desencadenantes (litio, betabloqueadores, antipalúdicos) [@bolognia5].'));
  r.push('<span class="cf">Si aparecen pústulas generalizadas, eritrodermia o fiebre → alarma y derivación urgente; si el BSA pasa de 3–5 % o hay zona especial o artritis → escala de tópicos a fototerapia, sistémico o biológico [@elmets2021][@menter2019].</span>');
  out(dc,r.join(''));
}
