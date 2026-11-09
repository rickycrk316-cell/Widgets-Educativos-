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

function dcE4(dc){
  var sub=sel(dc,'sub'),sx=sel(dc,'sx'),rx=sel(dc,'rx');
  if(!(sub.length||sx.length||rx.length)){
    vacio(dc,'Elige el subtipo, los síntomas que más molestan y el fármaco que recibe ahora. El simulador propone el fármaco con su posología cuando está verificada y lo que se evita.');return;}
  var x=[],pdd=hv(sub,'pdd');
  if(hv(rx,'tip')){
    x.push(par('<b>Antipsicótico típico en curso</b>: sospecha sensibilidad grave si hay rigidez, somnolencia o confusión; en autopsias 13 de 16 pacientes con Lewy reaccionaron mal y 7 de 13 de forma grave [@c_mckeith1992]. Suspéndelo y trata la causa de la agitación; no lo cambies por otro del mismo grupo [@mckeith2017].'));
  }
  if(hv(sx,'cog')||(hv(sx,'vh')&&!hv(sx,'cog'))){
    if(pdd) x.push(par('<b>Cognición</b> (demencia de Parkinson): rivastigmina VO con las comidas, 1,5 mg cada 12 h; sube a 3, 4,5 y 6 mg cada 12 h tras al menos 4 semanas en cada dosis; máximo 12 mg/día. Si interrumpes más de 3 días, reinicia en 1,5 mg [@c_rivastig_label][@c_emre2004]. Alternativa: donepezilo, 5 mg cada noche y 10 mg tras 4 a 6 semanas [@c_aricept].'));
    else x.push(par('<b>Cognición</b> (DLB): inhibidor de colinesterasa de primera línea [@mckeith2017]. Donepezilo VO, 5 mg cada noche y 10 mg tras 4 a 6 semanas (ficha FDA, indicada en Alzheimer; en DLB, 10 mg mejoró el MMSE en 1,4 puntos en un análisis post hoc) [@c_aricept][@c_mori2024b]; o rivastigmina VO, 1,5 mg cada 12 h con las comidas, con ascenso lento [@c_rivastig_label].'));
  }
  if(hv(sx,'vh')) x.push(par('<b>Alucinaciones visuales</b>: el inhibidor de colinesterasa es el primer paso porque puede reducirlas [@mckeith2017]; revisa también dopaminérgicos y anticolinérgicos que las empeoran. Si persisten y son graves, quetiapina a dosis baja con evidencia débil (un ensayo pequeño fue negativo); la clozapina y la pimavanserina no tienen eficacia establecida en DLB [@mckeith2017]. No se fija una dosis en la fuente leída.'));
  if(hv(sx,'agit')) x.push(par('<b>Agitación o psicosis grave</b>: descarta delirium por enfermedad intercurrente y fármacos, aplica medidas no farmacológicas y capacita al cuidador [@mckeith2017]. Evita haloperidol y los antipsicóticos típicos (reacción adversa en 81 % y grave en 54 % de los que reaccionaron) [@c_mckeith1992]; si el riesgo lo exige, quetiapina a dosis baja con vigilancia [@mckeith2017].'));
  if(hv(sx,'park')) x.push(par('<b>Parkinsonismo</b>: levodopa a dosis baja y ascenso lento; responde peor que en el Parkinson y puede aumentar la psicosis. Evalúa caídas, densidad ósea y vitamina D [@mckeith2017]. No se fija una dosis en la fuente leída.'));
  if(hv(sx,'rbd')) x.push(par('<b>Conducta del sueño REM</b>: melatonina, posiblemente más segura; clonazepam nocturno con cautela porque puede empeorar cognición y marcha [@mckeith2017]. No se fija una dosis en la fuente leída.'));
  if(hv(sx,'dep')) x.push(par('<b>Depresión</b>: ISRS, IRSN o mirtazapina según tolerabilidad y respuesta; hay pocos datos específicos en DLB [@mckeith2017].'));
  if(!x.length) x.push(par('Elige al menos un síntoma que moleste para proponer el fármaco.'));
  x.push('<span class="cf">Si el paciente recibe haloperidol y aparece rigidez, somnolencia o confusión graves → sospecha sensibilidad a antipsicóticos de la DLB; suspéndelo y no lo sustituyas por otro típico [@c_mckeith1992][@mckeith2017].</span>');
  out(dc,x.join(''));
}
