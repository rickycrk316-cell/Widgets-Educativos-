function dcVis(dc){
  var c=sel(dc,'curso'),a=sel(dc,'aten'),d=sel(dc,'dom'),s=sel(dc,'sig');
  if(!(c.length||a.length||d.length||s.length)){
    vacio(dc,'Elige el tiempo y curso, la atención, el dominio que cayó primero y los signos acompañantes. El simulador propone la entidad compatible, el hallazgo que falta y la conducta inicial; no calcula probabilidades.');return;}
  var x=[],n=0;
  var cron=hv(c,'cron')||hv(c,'esc');
  var inat=hv(a,'alt');
  var delir=hv(c,'agudo')||(inat&&!cron);
  var lewy=cron&&((inat&&(hv(d,'vis')||hv(s,'park')))||(hv(d,'vis')&&hv(s,'park')));
  var vasc=!delir&&!lewy&&(hv(c,'esc')||((hv(s,'foc')||hv(s,'vas'))&&(hv(d,'eje')||!d.length)));
  var ft=!delir&&!lewy&&!vasc&&(hv(d,'con')||hv(s,'des')||hv(s,'afa'));
  var ea=!delir&&!lewy&&!vasc&&!ft&&(hv(d,'mem')||(cron&&!d.length));
  if(delir){n++;
    x.push(par('<b>Delirium</b>: el inicio en horas o días con inatención y conciencia que fluctúa define el cuadro, y se busca primero aunque haya una demencia de fondo [@dsm5tr][@nice_ng97]. Falta confirmarlo con el CAM o el 4AT en la cabecera y identificar la causa'+(hv(s,'pre')?' (el precipitante elegido orienta dónde buscar)':'')+' [@inouye1990]. Conducta inicial: buscar y corregir la causa, medidas no farmacológicas y antipsicótico solo si hay riesgo; si no distingues delirium de demencia, trata primero el delirium [@nice_ng97]. Detalle en «Delirium».'));
    if(cron||hv(d,'mem')) x.push(par('Si además hay un declive de meses, piensa en <b>delirium sobre demencia</b>: la demencia aumenta el riesgo de delirium y no se rotula hasta que el delirium se resuelva [@nice_ng97].'));
  }
  if(lewy){n++;
    x.push(par('<b>Demencia con cuerpos de Lewy</b>: la fluctuación cognitiva con alucinaciones visuales o parkinsonismo en un declive crónico es su perfil [@mckeith2017]. Descarta primero un delirium, que imita la fluctuación [@nice_ng97]. Falta confirmar con los criterios de McKeith 2017; si hay duda, NICE propone SPECT con 123I-FP-CIT [@mckeith2017][@nice_ng97]. Conducta inicial: inhibidor de colinesterasa (donepezilo o rivastigmina) y evitar los antipsicóticos, que pueden causar reacciones graves [@nice_ng97].'));
  }
  if(vasc){n++;
    x.push(par('<b>Neurocognitivo vascular</b>: el declive escalonado, ejecutivo, con signos focales y factores vasculares apunta a una causa cerebrovascular [@sachdev2014]. Falta la RM con una lesión vascular que explique el déficit; la carga de lesiones sola no basta para el diagnóstico [@nice_ng97]. Conducta inicial: control estricto de los factores de riesgo vascular y prevención secundaria; los inhibidores de colinesterasa solo si se sospecha Alzheimer, Lewy o demencia de Parkinson asociados [@nice_ng97].'));
  }
  if(ft){n++;
    x.push(par('<b>Degeneración frontotemporal</b>: el cambio temprano de conducta o de lenguaje con memoria relativamente conservada separa este grupo del Alzheimer [@rascovsky2011][@gornotempini2011]. Falta confirmar con los criterios de Rascovsky (conducta) o Gorno-Tempini (lenguaje) y la neuroimagen con atrofia frontotemporal; FDG-PET o SPECT de perfusión si hay duda [@nice_ng97]. Conducta inicial: no ofrezcas inhibidores de colinesterasa ni memantina [@nice_ng97]; el manejo de la conducta se detalla en «Frontotemporal».'));
  }
  if(ea){n++;
    x.push(par('<b>Enfermedad de Alzheimer</b>: el olvido progresivo de lo reciente con fallo para aprender información nueva, de inicio insidioso y con atención conservada, es su perfil [@mckhann2011]. Falta medir la cognición con MoCA o MMSE, la función diaria, las causas reversibles y la neuroimagen estructural [@nice_ng97]. Conducta inicial: inhibidor de colinesterasa si hay demencia leve a moderada, intervención no farmacológica y apoyo al cuidador [@nice_ng97]. Detalle en «Enfermedad de Alzheimer».'));
  }
  if(hv(s,'rap')) x.push(par('<b>Declive en semanas a pocos meses</b>: sospecha enfermedad de Creutzfeldt-Jakob u otra causa de demencia rápidamente progresiva y refiere a neurología con acceso a estudio de líquido cefalorraquídeo [@nice_ng97].'));
  if(!n&&!hv(s,'rap')) x.push(par('Los datos elegidos no bastan para sostener una entidad. Define el tiempo de instalación, la atención y el dominio que cayó primero.'));
  if(cron&&!delir) x.push(par('En todo declive crónico descarta antes las causas reversibles: B12, TSH, depresión y fármacos anticolinérgicos [@b_knopman2001][@nice_ng97].'));
  x.push('<span class="cf">Si el inicio fuera de horas a días con inatención → delirium, aunque el dominio inicial parezca de Alzheimer; si aparecen signos focales con declive escalonado → vascular; si hay alucinaciones visuales con parkinsonismo y fluctuación → cuerpos de Lewy [@nice_ng97][@mckeith2017].</span>');
  out(dc,x.join(''));
}

function dcE2(dc){
  var m=num(dc,'mmse'),mo=num(dc,'moca'),f=sel(dc,'fun'),s=sel(dc,'sit');
  if(isNaN(m)&&isNaN(mo)&&!f.length&&!s.length){
    vacio(dc,'Escribe el puntaje del MMSE (y el del MoCA si lo tienes), elige si conserva su independencia y marca la situación. El simulador propone el estadio, la conducta y el fármaco con su posología; no calcula probabilidades.');return;}
  var x=[];
  var ya=hv(s,'iche'),into=hv(s,'into')||hv(s,'brad'),brad=hv(s,'brad'),ren=hv(s,'renal'),cond=hv(s,'cond');
  var DON='donepezilo 5 mg VO una vez al día por la noche; tras 4 a 6 semanas, 10 mg (máximo en la fase leve a moderada) [@b_don]';
  var RIV='rivastigmina 1,5 mg VO cada 12 h con las comidas; sube a 3, 4,5 y 6 mg cada 12 h, con al menos 2 semanas en cada paso (máximo 12 mg al día) [@b_riv]';
  var GAL='galantamina 4 mg VO cada 12 h con comida; 8 mg cada 12 h tras al menos 4 semanas, y 12 mg cada 12 h tras otras 4 semanas si lo tolera [@b_gal]';
  var MEM='memantina 5 mg VO una vez al día; sube 5 mg cada semana hasta 10 mg cada 12 h (20 mg al día)'+(ren?'; con depuración de creatinina de 5 a 29 mL/min, la dosis objetivo es 5 mg cada 12 h':'')+' [@b_mem]';
  var bad=false;
  if(!isNaN(mo)){
    if(mo<0||mo>30){x.push(par('El MoCA va de 0 a 30 puntos: revisa el puntaje [@b_moca2005].'));bad=true;}
    else x.push(par('MoCA de '+mo+' puntos: '+(mo<23?'bajo el corte original de 26 y también bajo 23, el corte que mejora la exactitud':(mo<26?'bajo el corte original de 26 pero no bajo 23, zona donde aumentan los falsos positivos':'sin alteración con el corte original de 26'))+' [@b_moca2005][@b_carson2018]. El MoCA tamiza; no tiene bandas de gravedad verificadas aquí, así que estadifica con el MMSE y la función diaria.'));
  }
  if(!isNaN(m)){
    if(m<0||m>30){x.push(par('El MMSE va de 0 a 30 puntos: revisa el puntaje [@b_perneczky2006].'));bad=true;}
    else {
      var est,ing=hv(f,'ind');
      if(m>=26){
        x.push(par('<b>MMSE de '+m+' puntos</b>: '+(m===30?'sin deterioro':'rango dudoso (26 a 29)')+' [@b_perneczky2006]. El MMSE detecta poco el deterioro leve, así que un valor alto no descarta un trastorno neurocognitivo leve [@b_moca2005]. Conducta inicial: valora la función con un informante, completa con MoCA y reevalúa; sin demencia no hay indicación de inhibidor de colinesterasa [@nice_ng97].'));
      } else {
        est=m>=21?'leve':(m>=11?'moderada':'grave');
        x.push(par('<b>MMSE de '+m+' puntos: demencia '+est+' por Alzheimer</b> si hay declive que compromete la independencia (21 a 25 leve, 11 a 20 moderada, 0 a 10 grave) [@b_perneczky2006][@dsm5tr].'));
        if(ing&&m<=20) x.push(par('Dato incongruente: un MMSE de 20 o menos con independencia conservada exige confirmar la función con un informante; la escala por sí sola no estadifica [@nice_ng97].'));
        else if(ing) x.push(par('Con independencia conservada se trata de un <b>trastorno neurocognitivo leve</b> y no de demencia [@dsm5tr]. Las recomendaciones de tratamiento de NICE se refieren a la demencia; aquí el manejo es no farmacológico, control de factores de riesgo y reevaluación periódica [@nice_ng97]. Los anticuerpos antiamiloide son los únicos con indicación de etiqueta en la fase de deterioro leve, con amiloide confirmado y vigilancia de ARIA, y quedan fuera del primer nivel [@b_lec][@b_kis].'));
        else if(est==='leve'){
          if(into) x.push(par('Demencia leve con '+(brad?'bradicardia, bloqueo o síncope':'intolerancia o contraindicación a los inhibidores de colinesterasa')+': NICE no recomienda memantina en la fase leve; mantén las medidas no farmacológicas'+(brad?', obtén un ECG y consulta al especialista antes de cualquier colinesterásico, porque estos fármacos tienen efecto vagotónico y pueden causar bloqueo o síncope [@b_don]':'')+' [@nice_ng97].'));
          else if(ya) x.push(par('Demencia leve que ya toma un inhibidor de colinesterasa: continúa el mismo; no lo suspendas por la gravedad sola [@nice_ng97]. Añadir memantina se reserva para la fase moderada o grave [@nice_ng97].'));
          else x.push(par('Demencia leve: inhibidor de colinesterasa. NICE empieza por el de menor costo, salvo razón para otro. Opciones: '+DON+'; o '+RIV+'; o '+GAL+' [@nice_ng97].'));
        } else if(est==='moderada'){
          if(ya) x.push(par('Demencia moderada que ya toma un inhibidor de colinesterasa: continúa y considera añadir memantina: '+MEM+' [@nice_ng97].'));
          else if(into) x.push(par('Demencia moderada con '+(brad?'bradicardia, bloqueo o síncope':'intolerancia o contraindicación a los inhibidores de colinesterasa')+': memantina en monoterapia: '+MEM+' [@nice_ng97].'+(brad?' Obtén un ECG antes de cualquier colinesterásico [@b_don].':'')));
          else x.push(par('Demencia moderada: inhibidor de colinesterasa de primera línea. Opciones: '+DON+'; o '+RIV+'; o '+GAL+' [@nice_ng97]. Si no lo tolera, pasa a memantina.'));
        } else {
          if(ya) x.push(par('Demencia grave que ya toma un inhibidor de colinesterasa: ofrece memantina añadida y no suspendas el inhibidor por la gravedad sola: '+MEM+' [@nice_ng97].'));
          else x.push(par('Demencia grave: memantina en monoterapia: '+MEM+' [@nice_ng97].'));
        }
        if(ren&&est!=='grave'&&!ing) x.push(par('Con depuración de creatinina de 5 a 29 mL/min, la galantamina no debe pasar de 16 mg al día [@b_gal] y la memantina se limita a 5 mg cada 12 h [@b_mem].'));
      }
    }
  }
  if(!bad&&isNaN(m)&&isNaN(mo)) x.push(par('Con la función y la situación elegidas falta un puntaje: mide el MMSE para estadificar [@b_perneczky2006].'));
  if(cond) x.push(par('<b>Agitación o psicosis</b>: primero busca dolor, delirium y causas del entorno y ofrece intervenciones psicosociales; el antipsicótico solo si hay riesgo de daño o angustia grave, a la dosis mínima eficaz, por el menor tiempo y con reevaluación al menos cada 6 semanas [@nice_ng97]. Los antipsicóticos aumentan el riesgo de muerte en ancianos con psicosis por demencia [@b_risp].'));
  x.push(par('En todos los casos: apoyo al cuidador, actividades, revisión de fármacos anticolinérgicos y planificación anticipada [@nice_ng97].'));
  x.push('<span class="cf">Si el MMSE baja de 21 a 20 puntos o menos (leve → moderada) → se considera la memantina junto al inhibidor; si aparece bradicardia, bloqueo o síncope → se evita el colinesterásico y, en la fase moderada o grave, se pasa a memantina [@nice_ng97][@b_don].</span>');
  out(dc,x.join(''));
}
