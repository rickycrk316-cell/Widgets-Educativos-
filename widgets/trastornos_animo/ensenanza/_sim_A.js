function dcVis(dc){
  var c=sel(dc,'curso'),e=sel(dc,'ecg'),h=sel(dc,'hall'),o=sel(dc,'otros');
  if(!(c.length||e.length||h.length||o.length)){
    vacio(dc,'Elige el curso, el ECG y los hallazgos de la consulta. El simulador propone qué entidad es compatible, qué dato falta para confirmarla y la conducta inicial; no calcula probabilidades.');return;}
  var r=[],n=0;
  var isq=hv(e,'alt')||hv(c,'isq');
  if(isq){n++;
    r.push(par('<b>Síndrome coronario agudo</b>: el dolor persistente o los cambios en el ECG lo hacen la primera hipótesis. Falta la troponina seriada y la monitorización [@ESC_SCA]. Conducta inicial: AAS masticada, ECU 911 y monitorización; no rotules ansiedad.'));
  } else if(hv(e,'no')&&(hv(c,'min')||hv(o,'sudor')||hv(o,'frcv'))){n++;
    r.push(par('Falta el ECG de 12 derivaciones: con opresión torácica, sudoración o factores de riesgo no se etiqueta ansiedad hasta tenerlo [@AHA_DT]. Conducta inicial: ECG en la misma consulta y troponina si está disponible.'));
  }
  if(hv(c,'min')&&hv(e,'norm')){n++;
    r.push(par('<b>Trastorno de pánico</b>: crisis con pico en minutos y ECG normal lo hacen compatible'+(hv(h,'miedo')||hv(h,'evit')?', y el miedo o la evitación lo refuerzan':'')+'. Falta confirmar que las crisis son inesperadas y recurrentes, con miedo persistente a nuevas crisis, y excluir causa orgánica o tóxica [@DSM]. Conducta inicial: psicoeducación, ISRS y TCC; la benzodiacepina no es mantenimiento [@NICE_ANX].'));
  } else if(hv(c,'min')&&!isq&&!hv(e,'no')){n++;
    r.push(par('El pico en minutos sugiere pánico, pero necesita un ECG normal antes de aceptarlo [@AHA_DT].'));
  }
  if(hv(c,'mes')||(hv(h,'preoc')&&!hv(c,'min'))){n++;
    r.push(par('<b>Ansiedad generalizada</b>: preocupación excesiva y difícil de controlar durante meses. Falta el GAD-7 y confirmar la duración de al menos 6 meses con criterios DSM-5-TR [@GAD7][@DSM]. Conducta inicial: ISRS o IRSN y TCC.'));
  }
  if(hv(c,'sem')||hv(h,'anhed')){n++;
    r.push(par('<b>Depresión mayor</b>: ánimo bajo o anhedonia casi todos los días. Falta el PHQ-9 y la pregunta directa por ideación suicida [@PHQ9][@CSSRS]. Conducta inicial: evaluar el riesgo suicida; ISRS y psicoterapia [@NICE_DEP].'));
  }
  if(hv(c,'dosis')||hv(o,'xanax')){n++;
    r.push(par('<b>Consumo de benzodiacepinas</b>: síntomas entre dosis o alprazolam por semanas sugieren tolerancia y rebote. Falta la anamnesis de consumo con criterios DSM-5-TR [@DSM]. Conducta inicial: reducción gradual pactada; nunca suspensión brusca [@ASHTON].'));
  }
  if(hv(o,'ideas')) r.push(par('Ideas de muerte o suicidio: pregunta por plan, intención y medios, acompaña al paciente y retira el acceso a medios letales; el primer nivel maneja el riesgo con mhGAP [@CSSRS][@MHGAP].'));
  if(hv(o,'frcv')&&hv(c,'min')&&!isq) r.push(par('Con factores de riesgo cardiovascular, un cuadro que parece pánico sigue exigiendo ECG y troponina si el dolor dura o se repite [@ESC_SCA].'));
  if(!n) r.push(par('Los hallazgos elegidos no bastan para sostener una entidad. Completa el curso temporal y el ECG antes de decidir.'));
  r.push('<span class="cf">Si el ECG normal pasa a cambios isquémicos o el dolor supera los 20 minutos → la conducta cambia de psicoeducación e ISRS a AAS masticada, ECU 911 y monitorización [@ESC_SCA].</span>');
  out(dc,r.join(''));
}

function dcE1d(dc){
  var s=sel(dc,'sint'),p=sel(dc,'pico'),k=sel(dc,'crisis'),m=sel(dc,'miedo'),e=sel(dc,'ecg'),g=sel(dc,'org');
  if(!(s.length||p.length||k.length||m.length||e.length||g.length)){
    vacio(dc,'Elige los hallazgos de la crisis, el ECG y el estudio orgánico. El simulador indica si cumple ataque de pánico, si cumple trastorno de pánico y qué falta excluir.');return;}
  var r=[];
  if(hv(e,'alt')||hv(p,'pers')){
    r.push(par('La isquemia no está excluida: el ECG alterado o el dolor persistente mandan sobre cualquier criterio psiquiátrico [@ESC_SCA]. Conducta inicial: manejo de síndrome coronario agudo y ECU 911; no diagnostiques pánico.'));
    r.push('<span class="cf">Si el ECG vuelve a ser normal y el dolor cede en minutos → se retoma la evaluación de pánico [@AHA_DT].</span>');
    out(dc,r.join(''));return;
  }
  var ataque=hv(s,'cuatro')&&hv(p,'min');
  if(hv(s,'cuatro')||hv(p,'min')){
    if(ataque) r.push(par('<b>Cumple ataque de pánico</b>: cuatro o más síntomas con pico en minutos [@DSM]. Es un síndrome, no un diagnóstico por sí solo: aparece también en otros trastornos y en causas orgánicas.'));
    else r.push(par('No cumple ataque de pánico: se necesitan cuatro o más síntomas con pico en minutos [@DSM].'));
  } else r.push(par('Falta definir cuántos síntomas hubo y cómo fue el pico para valorar el ataque de pánico.'));
  if(hv(k,'unica')) r.push(par('Un solo ataque no basta para trastorno de pánico: exige ataques inesperados recurrentes [@DSM].'));
  if(hv(k,'esp')) r.push(par('Si las crisis aparecen siempre ante un estímulo definido, piensa en fobia específica o social antes que en pánico [@DSM].'));
  var tp=ataque&&hv(k,'inesp')&&hv(m,'si');
  if(hv(k,'inesp')&&hv(m,'no')) r.push(par('Hay ataques inesperados sin miedo persistente a nuevas crisis ni cambio de conducta durante al menos un mes: aún no cumple trastorno de pánico [@DSM].'));
  if(hv(e,'no')) r.push(par('Falta el ECG de 12 derivaciones: sin él no se diagnostica pánico [@AHA_DT].'));
  if(hv(g,'estim')) r.push(par('La cafeína, los estimulantes o la abstinencia pueden causar el cuadro: se clasifica como inducido por sustancia hasta retirarlos y reevaluar [@DSM].'));
  if(tp&&hv(e,'norm')&&hv(g,'exc')) r.push(par('<b>Cumple trastorno de pánico</b>: ataques inesperados recurrentes, miedo persistente, ECG normal y causa orgánica excluida [@DSM]. Anota si hay agorafobia. Pasa a «Tratamiento».'));
  else if(tp&&hv(e,'norm')) r.push(par('Los criterios clínicos están completos, pero falta excluir causa orgánica: glucemia capilar, TSH y consumo de cafeína, estimulantes, alcohol o benzodiacepinas [@DSM][@HARRISON].'));
  else if(tp) r.push(par('Los criterios clínicos del trastorno de pánico se perfilan, pero faltan el ECG normal y la exclusión de causa orgánica [@DSM].'));
  r.push('<span class="cf">Si el ECG no se hizo o muestra cambios, o aparece dolor persistente → no se diagnostica pánico y se maneja como síndrome coronario agudo [@ESC_SCA].</span>');
  out(dc,r.join(''));
}

function dcE1t(dc){
  var f=sel(dc,'fase'),o=sel(dc,'otros');
  if(!f.length&&!o.length){
    vacio(dc,'Elige la fase del tratamiento y los otros datos para obtener el fármaco, la dosis de inicio y la titulación.');return;}
  var r=[];
  if(hv(o,'ecg')) r.push(par('Antes de explicar «no es un infarto», confirma un ECG normal; sin él, no tranquilices [@AHA_DT].'));
  if(hv(f,'nuevo')){
    var sert='sertralina 25 mg VO cada 24 h durante 1 semana y luego 50 mg cada 24 h, con ajuste según respuesta hasta 200 mg al día [@WFSBP][@NICE_ANX]';
    var esc='escitalopram 5 mg VO cada 24 h durante 1 semana y luego 10 mg cada 24 h, hasta 20 mg al día [@WFSBP]';
    var par10='paroxetina 10 mg VO cada 24 h, con aumento de 10 mg por semana hasta 40 mg al día [@WFSBP]';
    if(hv(o,'qt')) r.push(par('ISRS de inicio: '+sert+'. Evita escitalopram si el intervalo QT está prolongado.'));
    else if(hv(o,'emb')) r.push(par('ISRS de inicio: '+sert+'. Evita paroxetina en el embarazo.'));
    else if(hv(o,'mayor')) r.push(par('ISRS de inicio: '+esc.replace('hasta 20 mg al día','con tope de 10 mg al día en mayores de 65 años')+'; empieza en la mitad de la dosis habitual y vigila el sodio.'));
    else r.push(par('ISRS de inicio: '+sert+'. Alternativas: '+esc+'; o '+par10+'.'));
    r.push(par('Empieza con dosis bajas porque el ISRS puede aumentar la ansiedad al inicio, y avisa que el efecto tarda semanas. Suma TCC con exposición interoceptiva y gradual [@NICE_ANX].'));
  }
  if(hv(f,'falla')) r.push(par('Respuesta insuficiente: revisa adherencia y dosis, sube a la dosis máxima tolerada, cambia a otro ISRS o a un IRSN tras una prueba adecuada y suma TCC si no la recibe [@WFSBP].'));
  if(hv(f,'crisis')) r.push(par('Crisis en consulta: con ECG normal, guía respiración lenta y diafragmática y tranquiliza. Si la crisis es intensa, alprazolam 0,5 mg VO una vez como puente, sin pauta de mantenimiento [@XANAX_FT][@NICE_ANX].'));
  if(hv(f,'xanax')) r.push(par('Alprazolam por semanas: no lo suspendas de golpe. Inicia el ISRS y planifica una reducción gradual pactada (ver «Consumo de benzodiacepinas»); la benzodiacepina no es tratamiento de mantenimiento [@ASHTON][@XANAX_FT].'));
  if(hv(o,'bzd')&&!hv(f,'xanax')) r.push(par('Si se usa alprazolam como puente: 0,5 mg VO cada 8 h, 0,25 mg en adultos mayores o debilitados, durante 2 a 4 semanas como máximo mientras el ISRS hace efecto; advierte somnolencia, caídas, tolerancia y dependencia [@XANAX_FT][@ASHTON].'));
  if(hv(o,'ideas')) r.push(par('Con ideas de muerte o suicidio, vigila de cerca el inicio del ISRS, sobre todo en menores de 25 años, y retira el acceso a medios letales [@NICE_DEP][@MHGAP].'));
  if(hv(o,'polivit')) r.push(par('Evita polivitamínicos como Stresstabs y otros suplementos como tratamiento de la ansiedad: no tienen efecto ansiolítico demostrado y retrasan el diagnóstico [VERIFICAR EN FUENTE].'));
  if(!r.length) r.push(par('Con esos datos no hay una pauta clara: define la fase del tratamiento.'));
  r.push('<span class="cf">Si el paciente ya usa alprazolam por semanas → no se suspende de golpe: se inicia el ISRS y se planea una reducción gradual [@ASHTON].</span>');
  out(dc,r.join(''));
}
