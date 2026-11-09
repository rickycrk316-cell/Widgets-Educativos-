function dcE3(dc){
  var ev=sel(dc,'ev'),st=sel(dc,'sit'),pas=num(dc,'pas'),pad=num(dc,'pad'),ldl=num(dc,'ldl'),a1c=num(dc,'a1c');
  if(!(ev.length||st.length)&&isNaN(pas)&&isNaN(pad)&&isNaN(ldl)&&isNaN(a1c)){
    vacio(dc,'Elige el evento cerebrovascular previo y la situación, y escribe presión, LDL y HbA1c si los tienes. El simulador propone las medidas de prevención secundaria con su posología; no calcula probabilidades.');return;}
  var x=[],icas=hv(st,'icas'),hr=hv(st,'hemrisk');
  if(hv(ev,'isq')){
    if(icas){
      x.push(par('<b>Antiagregación</b>: aspirina 325 mg VO cada 24 h a largo plazo'+(hr?'. Con riesgo alto de transformación hemorrágica no se añade clopidogrel; sigue en monoterapia':'; añade clopidogrel 75 mg VO cada 24 h hasta 90 días')+' [@c_turan2022]. Pasado ese plazo no mantengas ambos [@c_dawson2022].'));
    } else {
      x.push(par('<b>Antiagregación</b>: un solo antiagregante a largo plazo, por ejemplo clopidogrel 75 mg VO cada 24 h sin dosis de carga [@c_plavix], o aspirina de liberación prolongada 162,5 mg VO cada 24 h según la ficha FDA [@c_durlaza]. Evita la doble antiagregación después de los primeros 90 días [@c_dawson2022].'));
    }
  } else if(hv(ev,'hem')){
    x.push(par('<b>Hemorragia intracerebral previa</b>: las fuentes leídas no fijan un esquema antiagregante; la decisión pesa el riesgo de resangrado y la hace neurología. Si usas atorvastatina 80 mg, sopesa riesgo y beneficio: en SPARCL el ictus hemorrágico fue más frecuente (2,3 % frente a 1,4 %) [@c_lipitor].'));
  } else if(hv(ev,'nin')){
    x.push(par('<b>Sin evento clínico</b>: las fuentes leídas no fijan el uso de antiagregante en lesión silente; el eje es controlar presión, lípidos y glucemia y vigilar la aparición de eventos [@c_dawson2022][@sachdev2014].'));
  }
  if(!isNaN(pas)||!isNaN(pad)){
    var meta=icas?'menor de 140/90 mmHg':'menor de 130/80 mmHg';
    var alta=icas?(pas>=140||pad>=90):(pas>=130||pad>=80);
    if(alta) x.push(par('<b>Presión</b> de '+(isNaN(pas)?'?':pas)+'/'+(isNaN(pad)?'?':pad)+' mmHg: sobre la meta ('+meta+'). Inicia o intensifica antihipertensivos; la guía apoya la combinación de fármacos y la medición fuera de consulta, pero no fija una dosis única [@c_dawson2022]'+(icas?'; en estenosis intracraneal sintomática la meta es menos estricta [@c_turan2022]':'')+'.'));
    else x.push(par('<b>Presión</b> de '+(isNaN(pas)?'?':pas)+'/'+(isNaN(pad)?'?':pad)+' mmHg: dentro de la meta ('+meta+'). Mantén el esquema y controla fuera de consulta [@c_dawson2022].'));
  }
  if(!isNaN(ldl)){
    if(ldl>=70) x.push(par('<b>LDL</b> de '+ldl+' mg/dL: sobre la meta de 70 mg/dL [@c_dawson2022]. Atorvastatina 80 mg VO cada 24 h (rango de la ficha 10 a 80 mg) [@c_lipitor]; si no llega a la meta con estatina, considera ezetimiba o un inhibidor de PCSK9 [@c_dawson2022].'));
    else x.push(par('<b>LDL</b> de '+ldl+' mg/dL: en meta (menor de 70 mg/dL). Mantén la estatina [@c_dawson2022].'));
  } else if(hv(ev,'isq')){
    x.push(par('<b>Estatina</b>: mide el LDL; indica atorvastatina 80 mg VO cada 24 h, la dosis del ensayo SPARCL tras ictus o AIT, hasta LDL menor de 70 mg/dL [@c_lipitor][@c_dawson2022].'));
  }
  if(hv(st,'dm')||!isNaN(a1c)){
    if(!isNaN(a1c)&&a1c>=7) x.push(par('<b>HbA1c</b> de '+String(a1c).replace('.',',')+' %: sobre la meta de menos de 7 % que apoya la mayoría del grupo ESO; ajusta el tratamiento antidiabético [@c_dawson2022].'));
    else if(!isNaN(a1c)) x.push(par('<b>HbA1c</b> de '+String(a1c).replace('.',',')+' %: en la meta de menos de 7 % [@c_dawson2022].'));
    else x.push(par('<b>Diabetes</b>: falta la HbA1c; la meta que apoya el grupo ESO es menor de 7 % [@c_dawson2022].'));
  }
  if(hv(st,'cog')){
    x.push(par('<b>Demencia establecida</b>: un inhibidor de colinesterasa da un beneficio modesto con más abandonos por efectos digestivos [@c_birks2013riv]. Rivastigmina VO con las comidas: 1,5 mg cada 12 h, sube a 3, 4,5 y 6 mg cada 12 h tras al menos 2 semanas en cada dosis, máximo 12 mg/día; vigila el peso (ficha FDA, indicada en Alzheimer) [@c_rivastig_label].'));
  }
  if(!x.length) x.push(par('Los datos elegidos no bastan para proponer medidas; añade el evento previo o las cifras de presión, LDL y HbA1c.'));
  x.push('<span class="cf">Si hay estenosis intracraneal sintomática grave con bajo riesgo de transformación hemorrágica → se añade clopidogrel 75 mg/día a la aspirina hasta 90 días; si no, la doble antiagregación no pasa de 90 días [@c_turan2022][@c_dawson2022].</span>');
  out(dc,x.join(''));
}
