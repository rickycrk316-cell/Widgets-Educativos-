function dcE2(dc){
  var s=sel(dc,'sit'),o=sel(dc,'otros');
  if(!s.length){
    vacio(dc,'Elige la situación del tratamiento y los otros datos para obtener el fármaco, la dosis y la conducta.');return;}
  var r=[];
  if(hv(s,'inicio')){
    if(hv(o,'hta')) r.push(par('Inicio con hipertensión no controlada: prefiere un ISRS, como escitalopram 10 mg VO cada 24 h (máximo 20 mg) o sertralina 50 mg VO cada 24 h (inicia con 25 mg la primera semana, hasta 200 mg), y evita venlafaxina XR porque sube la presión arterial; añade terapia cognitivo-conductual [@NICE_ANX][@WFSBP].'));
    else r.push(par('Inicio: escitalopram 10 mg VO cada 24 h (máximo 20 mg) o sertralina 50 mg VO cada 24 h (inicia con 25 mg la primera semana, hasta 200 mg), más terapia cognitivo-conductual. Alternativa IRSN: venlafaxina XR 75 mg VO cada 24 h con alimentos (hasta 225 mg) o duloxetina 60 mg VO cada 24 h (inicia con 30 mg la primera semana, máximo 120 mg) [@NICE_ANX][@WFSBP].'));
    r.push(par('El efecto tarda 4 a 6 semanas: avísalo al paciente y revisa a las 2 semanas la tolerancia y la ideación suicida [@NICE_ANX].'));
  }
  if(hv(s,'nores')) r.push(par('Sin respuesta tras 4 a 6 semanas: confirma adherencia y dosis, sube la dosis del ISRS hasta el máximo tolerado, cambia a otro ISRS, a un IRSN o a pregabalina 75 mg VO cada 12 h con ajuste renal [VERIFICAR EN FUENTE], y refuerza la terapia cognitivo-conductual [@NICE_ANX][@WFSBP].'));
  if(hv(s,'intol')) r.push(par('No tolera el ISRS: si fue activación o náusea, reinicia con la mitad de la dosis y titula despacio, por ejemplo sertralina 25 mg VO cada 24 h; si persiste, cambia a pregabalina 75 mg VO cada 12 h o a duloxetina 60 mg VO cada 24 h [@WFSBP] [VERIFICAR EN FUENTE].'));
  if(hv(o,'hep')) r.push(par('Hepatopatía: evita duloxetina y usa dosis menores de ISRS con titulación lenta [@NICE_ANX].'));
  if(hv(o,'mayor')) r.push(par('65 años o más: empieza con la mitad de la dosis, vigila hiponatremia y caídas, y limita escitalopram a 10 mg [VERIFICAR EN FUENTE].'));
  if(hv(o,'bzd')) r.push(par('Usa benzodiacepina desde hace semanas: no la suspendas de golpe; mantenla mientras el ISRS empieza a actuar y redúcela de forma gradual y pactada para evitar rebote y abstinencia [@NICE_ANX][@FDA_BZD][@ASHTON].'));
  if(hv(o,'ide')) r.push(par('Ideación suicida: el ISRS puede activar en las primeras semanas; da pocas dosis por receta, revisa cada semana y estratifica el riesgo (ver «Visión de conjunto») [@MHGAP].'));
  r.push('<span class="cf">Si aparecen ideación suicida o una depresión mayor asociada → deja de ser solo ansiedad y se trata primero el riesgo y el episodio depresivo [@MHGAP][@NICE_ANX].</span>');
  out(dc,r.join(''));
}

function dcE3r(dc){
  var i=sel(dc,'ide'),f=sel(dc,'fac');
  if(!i.length){
    vacio(dc,'Elige el nivel de ideación y los factores presentes para obtener el nivel de riesgo y la conducta en primer nivel sin derivación.');return;}
  var base={ninguna:0,pasiva:1,activa:2,plan:3},b=0,k;
  for(k in base){if(hv(i,k)) b=base[k];}
  var n=f.length,lvl=b;
  if(b>=1&&n>=1) lvl++;
  if(b>=1&&n>=3) lvl++;
  if(lvl>3) lvl=3;
  var nom=['bajo','bajo con vigilancia','moderado','alto'],r=[];
  r.push(par('Nivel de riesgo: <b>'+nom[lvl]+'</b>. Los factores presentes ('+n+') suben el nivel; el simulador no calcula probabilidades [@CSSRS][@MHGAP].'));
  if(lvl===0){
    r.push(par('Sin ideación: explica que puede consultar si cambia, trata el episodio depresivo y vuelve a preguntar en cada cita [@MHGAP].'));
    if(n) r.push(par('Con antecedentes o factores de riesgo, sigue preguntando de forma directa y verifica que haya apoyo y plan de contacto [@MHGAP].'));
  }
  if(lvl===1){
    r.push(par('Conducta: plan de seguridad escrito (señales de alarma, estrategias de afrontamiento, personas y números de contacto), psicoeducación a la familia y seguimiento cercano en 1 semana [@MHGAP].'));
  }
  if(lvl===2){
    r.push(par('Conducta: plan de seguridad escrito, restricción de medios con ayuda de un familiar (retirar fármacos, plaguicidas y armas), acompañamiento por una persona de confianza y seguimiento cercano en pocos días [@MHGAP].'));
  }
  if(lvl===3){
    r.push(par('Riesgo inminente: no dejes solo al paciente en ningún momento, retira los medios del entorno, mantén observación continua en el centro y activa ECU 911 para el traslado; mientras llega, conversa, escucha y no lo dejes marchar [@MHGAP].'));
    r.push(par('Después de la crisis: plan de seguridad escrito, familia comprometida y seguimiento diario o muy cercano hasta que baje el riesgo [@MHGAP].'));
  }
  if(hv(f,'agrav')) r.push(par('Psicosis, alcohol o desesperanza grave: trátalo como factor que sube el riesgo; si es psicosis, pide interconsulta o teleconsulta con psiquiatría [@MHGAP].'));
  if(hv(f,'medios')) r.push(par('El acceso a medios letales es el factor más modificable: retíralos o restríngelos de inmediato con la familia [@MHGAP].'));
  r.push('<span class="cf">Si el paciente pasa de pensamientos sin plan a plan o intención, o aparece acceso a medios → la conducta cambia de plan de seguridad y seguimiento a no dejarlo solo y activar ECU 911 [@MHGAP][@CSSRS].</span>');
  out(dc,r.join(''));
}

function dcE3(dc){
  var g=sel(dc,'grav'),e=sel(dc,'etapa'),o=sel(dc,'otros');
  if(!e.length){
    vacio(dc,'Elige la etapa del tratamiento (y la gravedad si estás iniciando) para obtener la conducta y la posología.');return;}
  var r=[];
  if(hv(e,'inicio')){
    if(!g.length) r.push(par('Elige la gravedad (PHQ-9 por bandas) para decidir entre psicoterapia sola o combinada con fármaco [@PHQ9][@NICE_DEP].'));
    else if(hv(g,'leve')) r.push(par('Depresión leve: empieza con psicoterapia (activación conductual o terapia cognitivo-conductual) y revisa en 2 semanas; añade un ISRS si no mejora o el paciente lo prefiere [@NICE_DEP].'));
    else{
      r.push(par('Depresión '+(hv(g,'grave')?'grave':'moderada')+': ISRS más psicoterapia. Sertralina 50 mg VO cada 24 h (inicia con 25 mg si hay ansiedad marcada, hasta 200 mg), o escitalopram 10 mg VO cada 24 h (máximo 20 mg), o fluoxetina 20 mg VO cada 24 h por la mañana (hasta 60 mg) [@NICE_DEP].'));
      if(hv(g,'grave')) r.push(par('Grave: revisa cada semana el riesgo suicida y la tolerancia durante el primer mes [@NICE_DEP][@MHGAP].'));
    }
  }
  if(hv(e,'nores')) r.push(par('Sin respuesta tras 4 a 6 semanas: confirma adherencia, sube la dosis hasta el máximo tolerado, cambia a otro ISRS o a venlafaxina XR 75 mg VO cada 24 h con alimentos (hasta 225 mg), o añade psicoterapia [@NICE_DEP].'));
  if(hv(e,'remis')) r.push(par('En remisión: mantén el mismo fármaco y la misma dosis al menos 6 meses y retira de forma gradual para evitar discontinuación y recaída [@NICE_DEP].'));
  if(hv(o,'bip')) r.push(par('Antecedente de manía o hipomanía: no inicies un antidepresivo solo, porque puede inducir viraje; requiere estrategia con estabilizador, idealmente con psiquiatría [@DSM][@NICE_DEP].'));
  if(hv(o,'joven')) r.push(par('Menor de 25 años: vigila activación e ideación en las primeras semanas con revisión durante la primera semana [VERIFICAR EN FUENTE].'));
  if(hv(o,'mayor')) r.push(par('65 años o más: inicia con la mitad de la dosis, vigila hiponatremia y caídas, y limita escitalopram a 10 mg [VERIFICAR EN FUENTE].'));
  if(hv(o,'psic')) r.push(par('Síntomas psicóticos: la depresión con psicosis no se maneja con ISRS solo; pide interconsulta o teleconsulta con psiquiatría y, si no es posible, sigue mhGAP en el centro [@MHGAP].'));
  if(hv(o,'sui')) r.push(par('Ideación suicida: estratifica el riesgo en esa consulta (ver «Diagnóstico») y no entregues fármacos en cantidad letal [@MHGAP].'));
  r.push('<span class="cf">Si el paciente tiene antecedente de manía o aparece ideación con plan → la conducta pasa de iniciar o ajustar el antidepresivo a descartar bipolaridad o asegurar la vida primero [@DSM][@MHGAP].</span>');
  out(dc,r.join(''));
}
