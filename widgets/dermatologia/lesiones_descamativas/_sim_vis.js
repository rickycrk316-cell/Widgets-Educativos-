function vsHas(a,v){return a.indexOf(v)>-1;}
function vsP(t){return '<p>'+t+'</p>';}
function dcVis(dc){
  var ed=sel(dc,'ed'),zo=sel(dc,'zona'),es=sel(dc,'esc'),pr=sel(dc,'pru'),sg=sel(dc,'sg'),al=sel(dc,'al');
  if(!(ed.length||zo.length||es.length||pr.length||sg.length||al.length)){
    out(dc,vsP('Elige la edad, la zona, la escama, el prurito y los hallazgos que tengas. El simulador propone la entidad compatible, el hallazgo que falta para confirmarla y la conducta inicial; no calcula probabilidades.'));return;}
  var E=[
    {k:'e1',n:'Dermatitis atópica',f:'prurito con distribución según la edad y curso crónico, que cumpla los criterios del Reino Unido [@e1_williams1994]',c:'emoliente diario y corticoide tópico por potencia y zona, baja en cara y pliegues [@sidbury2023]',h:0},
    {k:'e2',n:'Dermatitis seborreica',f:'simetría en zonas seborreicas y ausencia de pérdida de pelo; KOH si hay duda con tiña [@e2_clark2015]',c:'antifúngico tópico de base y corticoide de baja potencia por pocas semanas [@e2_clark2015]',h:0},
    {k:'e3',n:'Dermatitis de contacto',f:'la exposición y la mejoría al evitar el agente; parche si es crónica o el alérgeno se ignora [@e3_usatine2010][@e3_fonacierpg2015]',c:'evitar el agente y corticoide tópico según la zona [@e3_usatine2010]',h:0},
    {k:'e4',n:'Psoriasis',f:'Auspitz tras retirar la escama y revisión de uñas y superficie afectada [@bolognia5][@griffiths2021]',c:'corticoide más calcipotriol tópicos si es leve, derivación si es moderada o grave, y nunca corticoide sistémico [@elmets2021][@menter2019]',h:0},
    {k:'e5',n:'Pitiriasis rosada',f:'medallón previo y KOH negativo; VDRL o RPR si hay palmas o plantas [@e5_villalon2018][@e5_leung2021]',c:'tranquilizar y aliviar el prurito; cede en 6 a 8 semanas [@e5_villalon2018]',h:0},
    {k:'e6',n:'Pitiriasis versicolor',f:'KOH del raspado con levaduras e hifas cortas [@e6_gupta2015]',c:'antifúngico tópico; oral si es extensa o recurrente; la terbinafina oral no sirve [@e6_gupta2015]',h:0}
  ];
  function add(a,l,ks){if(vsHas(a,l))for(var i=0;i<ks.length;i++)E[ks[i]].h++;}
  add(ed,'lact',[0,1]);add(ed,'adol',[3,4,5]);add(ed,'adul',[1,2,3]);
  add(zo,'flex',[0]);add(zo,'seb',[1]);add(zo,'geo',[2]);add(zo,'ext',[3]);add(zo,'tron',[4,5]);
  add(es,'gras',[1]);add(es,'plat',[3]);add(es,'fina',[5]);add(es,'col',[4]);
  add(pr,'int',[0,2]);add(pr,'leve',[1,3,5]);
  add(sg,'atop',[0]);add(sg,'med',[4]);add(sg,'aus',[3]);add(sg,'pits',[3]);add(sg,'una',[5]);add(sg,'evita',[2]);add(sg,'kohp',[5]);
  var x=[];
  if(vsHas(al,'erit')) x.push(vsP('<b>Alarma, psoriasis eritrodérmica o pustulosa generalizada</b>: es la amenaza del grupo y pasa por delante de cualquier otro diagnóstico. Falta confirmar el antecedente de psoriasis y descartar causas de eritrodermia. Conducta inicial: deriva sin demora y no des corticoide sistémico [@bolognia5][@griffiths2021].'));
  if(vsHas(al,'herp')) x.push(vsP('<b>Alarma, eccema herpético</b> sobre una dermatitis atópica. Falta confirmar el antecedente de eccema y la fiebre. Conducta inicial: urgencia con antiviral intravenoso; no lo rotules como sobreinfección bacteriana [@e1_traidl2021][@e1_chan2022].'));
  if(vsHas(al,'palm')) x.push(vsP('<b>Palmas o plantas</b>: piensa en sífilis secundaria antes de aceptar una pitiriasis rosada. Falta el VDRL o RPR. Conducta inicial: pídelo y busca factor de riesgo y lesiones mucosas [@e5_villalon2018][@e5_scarvaglieri2025].'));
  if(vsHas(al,'vih')) x.push(vsP('<b>Forma extensa o súbita</b> de dermatitis seborreica: marcador cutáneo de inmunosupresión. Falta la prueba de VIH. Conducta inicial: pídela con consejería [@e2_dalloglio2022].'));
  var mx=0,i;
  for(i=0;i<E.length;i++) if(E[i].h>mx) mx=E[i].h;
  var top=[];
  if(mx>0) for(i=0;i<E.length;i++) if(E[i].h===mx) top.push(E[i]);
  if(vsHas(sg,'kohn')) x.push(vsP('KOH negativo: descarta pitiriasis versicolor y tiña; quedan los eccemas, la psoriasis y la pitiriasis rosada [@ely2014][@e6_gupta2015].'));
  if(vsHas(sg,'kohn')) top=top.filter(function(e){return e.k!=='e6';});
  if(!top.length){
    x.push(vsP('Los datos elegidos no bastan para sostener una entidad. Describe la lesión, la escama y la distribución, y haz un KOH si la escama es dudosa [@ely2014].'));
  } else {
    for(i=0;i<top.length&&i<3;i++){
      var e=top[i];
      x.push(vsP('<b>'+e.n+'</b> es la compatible'+(top.length>1?' (empata con otras: busca el dato que las separe)':'')+'. Falta confirmar: '+e.f+'. Conducta inicial: '+e.c+'. Detalle en su pestaña.'));
    }
  }
  x.push('<span class="cf">Si aparece Auspitz tras retirar la escama → de eccema a psoriasis; si el KOH muestra levaduras e hifas → pitiriasis versicolor y antifúngico en lugar de corticoide [@bolognia5][@e6_gupta2015].</span>');
  out(dc,x.join(''));
}
