function dcE5(dc){
  var s=sel(dc,'sint'),t=sel(dc,'sit');
  if(!s.length&&!t.length){
    vacio(dc,'Elige el síntoma conductual predominante y la situación del paciente. El simulador propone el fármaco con su posología y lo que se evita; no calcula probabilidades.');return;}
  var may=hv(t,'may60'),hna=hv(t,'hipona'),ice=hv(t,'ichE');
  var CIT='citalopram 20 mg VO cada 24 h; en mayores de 60 años el máximo es 20 mg al día [@d_dm_citalopram]';
  var SER='sertralina VO cada 24 h: inicio 25 a 50 mg al día, con aumentos de 25 a 50 mg por semana; en frontotemporal se reportó 50 a 100 mg al día [@d_dm_sertralina][@d_young2018]';
  var TRA='trazodona VO en dosis divididas: la ficha sugiere 150 mg al día con aumentos de 50 mg al día cada 3 a 4 días, hasta 400 mg al día como máximo ambulatorio; los ensayos en demencia usaron 50 a 300 mg al día [@d_dm_trazodona][@d_cochrane2004]';
  var r=[];
  if(hv(s,'desinh')){
    r.push(par('<b>Desinhibición, compulsiones o hiperoralidad</b>: un ISRS es la primera opción. '+(may?CIT:CIT+'; alternativa: '+SER)+(may?'; alternativa: '+SER:'')+' [@d_wittebrood2024].'));
    if(hna) r.push(par('Con hiponatremia o diurético, vigila el sodio: los ISRS pueden bajarlo, sobre todo en el adulto mayor [@d_dm_sertralina]; mide el sodio antes y a las semanas del inicio.'));
  }
  if(hv(s,'inq')){
    r.push(par('<b>Inquietud motora o irritabilidad</b>: trazodona. '+TRA+'. En el ensayo cruzado mejoró irritabilidad, agitación y conducta alimentaria [@d_lebert2004].'));
  }
  if(hv(s,'agr')){
    r.push(par('<b>Agresión con riesgo para el paciente o el cuidador</b>: primero medidas no farmacológicas y seguridad; si persiste el peligro, quetiapina con psiquiatría. No hay dosis establecida para frontotemporal en las fuentes leídas, así que la fija el especialista a la dosis mínima [@d_wittebrood2024].'));
    r.push(par('Cautela con cualquier antipsicótico: advertencia de caja negra en demencia y riesgo de efectos extrapiramidales [@d_wittebrood2024][@d_young2018].'));
  }
  if(hv(s,'apat')){
    r.push(par('<b>Apatía</b>: no hay fármaco con eficacia probada que se pueda recomendar con dosis en este grupo; usa medidas no farmacológicas y apoyo al cuidador, y evita la bupropiona, que el consenso desaconsejó en la mayoría de los síntomas [@d_wittebrood2024].'));
  }
  if(ice) r.push(par('<b>Ya toma un inhibidor de colinesterasa</b>: reevalúa suspenderlo; no mejora la cognición en frontotemporal y puede empeorar los síntomas neuropsiquiátricos [@d_wittebrood2024][@d_young2018].'));
  if(!s.length) r.push(par('Elige también el síntoma predominante para proponer el fármaco; evita siempre los inhibidores de colinesterasa y la memantina [@d_young2018].'));
  else r.push(par('Evita los inhibidores de colinesterasa y la memantina [@d_young2018]. Reevalúa con el cuidador la respuesta a las semanas [@d_jicha2011].'));
  r.push('<span class="cf">Si el paciente tenía memoria alterada y alucinaciones visuales con fluctuación (cuerpos de Lewy) o un Alzheimer → el inhibidor de colinesterasa pasa a ser útil, y el antipsicótico típico se evita [@mckeith2017].</span>');
  out(dc,r.join(''));
}
