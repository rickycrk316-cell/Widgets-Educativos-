function e2par(t){return '<p>'+t+'</p>';}
function e2hv(a,v){return a.indexOf(v)>-1;}
function dcE2tx(dc){
  var ed=sel(dc,'edad'),z=sel(dc,'zona'),s=sel(dc,'sit');
  if(!(ed.length||z.length||s.length)){
    out(dc,e2par('Elige la edad, la zona y la situación. El simulador propone el tratamiento con su posología según la tabla de fármacos; no calcula probabilidades.'));return;}
  var KC='ketoconazol 2 % champú 2 veces por semana por 4 semanas [@e2_dalloglio2022]';
  var KCR='ketoconazol 2 % crema 2 veces al día por 4 semanas [@e2_dalloglio2022]';
  var CC='ciclopirox 1 % champú 3 veces por semana por 4 semanas [@e2_dalloglio2022]';
  var CCR='ciclopirox 1 % crema 2 veces al día por 4 semanas [@e2_dalloglio2022]';
  var SE='sulfuro de selenio 2,5 % champú 2 veces por semana por 2 semanas y luego 1 vez por semana por 2 semanas [@e2_borda2015]';
  var HC='hidrocortisona 1 % crema 1 vez al día hasta 4 semanas [@e2_dalloglio2022]';
  var TC='tacrolimus 0,1 % ungüento o pimecrolimus 1 % crema 1 o 2 veces al día por 4 a 8 semanas, fuera de indicación [@e2_dalloglio2022]';
  var x=[];
  var lact=e2hv(ed,'lact'),cuero=e2hv(z,'cuero'),cara=e2hv(z,'cara'),pl=e2hv(z,'pliegues');
  var infl=e2hv(s,'infl'),ext=e2hv(s,'ext'),rec=e2hv(s,'recae');
  if(lact){
    x.push(e2par('<b>Lactante</b>: la evidencia de fármacos tópicos es escasa y hay riesgo de absorción. Usa champú emoliente y aceites vegetales con retiro mecánico suave de las escamas [@e2_dalloglio2022].'));
    if(infl&&(cara||pl||!z.length)) x.push(e2par('Con inflamación marcada, la hidrocortisona 1 % crema tiene evidencia escasa y no hay pauta establecida en las fuentes: úsala solo pocos días y con indicación de pediatría o dermatología [@e2_dalloglio2022].'));
    if(pl) x.push(e2par('En pliegues la lesión es húmeda y brillante: mantén la zona limpia y seca y evita oclusión [@e2_borda2015].'));
  } else {
    if(cuero) x.push(e2par('<b>Cuero cabelludo</b>: primera línea '+KC+'. Alternativas: '+CC+', o '+SE+' [@e2_dalloglio2022].'));
    if(cara||pl) x.push(e2par('<b>'+(cara&&pl?'Cara y pliegues':cara?'Cara':'Pliegues')+'</b>: primera línea '+KCR+'. Alternativa: '+CCR+'.'));
    if(!z.length&&ed.length) x.push(e2par('Elige la zona: cuero cabelludo, cara o pliegues cambian la presentación del fármaco.'));
    if(infl&&(cara||pl||!z.length)) x.push(e2par('<b>Inflamación marcada</b>: añade '+HC+', o '+TC+'. No prolongues el corticoide en cara ni pliegues por atrofia y telangiectasias [@e2_dalloglio2022].'));
    if(infl&&cuero&&!cara&&!pl) x.push(e2par('<b>Inflamación marcada en cuero cabelludo</b>: puedes asociar un corticoide tópico por pocas semanas junto al antifúngico; no lo prolongues [@e2_clark2015][@e2_dalloglio2022]. ↪ Escalera de potencias en «Visión».'));
  }
  if(rec) x.push(e2par('<b>Recaída tras remisión</b>: retoma el antifúngico y mantén ketoconazol 2 % champú 1 vez por semana (por 6 meses redujo las recaídas) [@e2_dalloglio2022].'));
  if(ext) x.push(e2par('<b>Extensa, súbita o refractaria</b>: pide prueba de VIH y busca otras causas de inmunosupresión; deriva a dermatología, que valora antifúngico oral o UVB [@e2_dalloglio2022][@e2_borda2019].'));
  x.push('<span class="cf">Si aparecen parches con pérdida de pelo y puntos negros en un niño → cambia a tiña capitis: KOH y cultivo del pelo y antifúngico sistémico, no champú [@e2_borda2015].</span>');
  out(dc,x.join(''));
}
