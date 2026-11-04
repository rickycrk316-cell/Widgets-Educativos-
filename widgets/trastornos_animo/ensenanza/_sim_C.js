function dcE4(dc){
  var d=num(dc,'dosis'),ri=sel(dc,'ritmo'),o=sel(dc,'otros');
  if(isNaN(d)&&!ri.length&&!o.length){
    vacio(dc,'Escribe la dosis diaria de alprazolam y elige la evolución y los otros datos para obtener la pauta de reducción.');return;}
  var f=function(x){return String(x).replace('.',',');};
  var r=[];
  if(hv(o,'conv')) r.push(par('Convulsión o confusión: es abstinencia grave. Reinstala la benzodiacepina, estabiliza y activa ECU 911; no sigas reduciendo [@ASHTON][@MHGAP].'));
  if(hv(o,'isq')) r.push(par('Opresión torácica actual: haz ECG de 12 derivaciones antes de atribuirla a rebote o abstinencia; si hay cambios isquémicos, sigue el manejo de «Síndrome coronario agudo» [@AHA_DT].'));
  if(hv(o,'alc')) r.push(par('Alcohol u opioides: suman depresión respiratoria con la benzodiacepina; suspéndelos o trátalos antes de iniciar la reducción [@FDA_BZD].'));
  if(!isNaN(d)){
    if(d<=0){
      r.push(par('Escribe una dosis diaria mayor de 0 mg.'));
    } else {
      if(d>10) r.push(par('La dosis supera los 10 mg al día que admite la ficha en pánico; confirma la dosis real [@XANAX_FT].'));
      var eq=d*20;
      var sub=Math.min(eq,40);
      var lo=Math.max(0.5,rd(sub*0.10*2,0)/2),hi=Math.max(0.5,rd(sub*0.25*2,0)/2);
      r.push(par('Equivalencia: alprazolam '+f(d)+' mg al día ≈ diazepam '+f(rd(eq,1))+' mg al día (0,5 mg de alprazolam ≈ 10 mg de diazepam) [@ASHTON].'));
      if(eq>sub) r.push(par('El equivalente supera el tope inicial de 40 mg al día [VERIFICAR EN FUENTE]: sustituye hasta '+f(sub)+' mg de diazepam, mantén el alprazolam restante y completa el cambio en pasos [@ASHTON].'));
      else r.push(par('Sustituye por diazepam '+f(rd(sub,1))+' mg al día VO, repartido en 2–3 tomas o por la noche, y retira el alprazolam [@ASHTON].'));
      if(hv(ri,'sint')) r.push(par('Con síntomas de abstinencia en el paso, mantén la dosis actual o retrocede un paso, y alarga el intervalo a 2 semanas o más; baja el 10 % en el paso siguiente [@ASHTON].'));
      else r.push(par('Reducción: baja entre '+f(lo)+' y '+f(hi)+' mg de diazepam al día (10 a 25 % de la dosis) cada 1–2 semanas, según tolere [@ASHTON][@FDA_BZD].'));
      r.push(par('Trata a la vez el trastorno de base con sertralina 25 mg VO cada 24 h durante una semana y luego 50 mg, más TCC [@NICE_ANX][@WFSBP].'));
    }
  } else {
    r.push(par('Escribe la dosis diaria de alprazolam para calcular la equivalencia en diazepam y el primer paso de reducción.'));
  }
  r.push('<span class="cf">Si aparecen convulsión, confusión o síntomas intensos de abstinencia en un paso → reinstala la dosis previa, enlentece la reducción y activa ECU 911 si hay compromiso vital [@ASHTON][@MHGAP].</span>');
  out(dc,r.join(''));
}

function dcE5(dc){
  var e=sel(dc,'ecg'),o=sel(dc,'otros');
  if(!e.length&&!o.length){
    vacio(dc,'Elige el hallazgo del ECG y los otros datos para obtener la conducta inicial con su posología.');return;}
  var r=[];
  var stel=hv(e,'stel'),sest=hv(e,'sest'),norm=hv(e,'norm');
  var isq=stel||sest||hv(o,'tro');
  if(stel) r.push(par('SCACEST: emergencia con reperfusión inmediata. Activa ECU 911 para traslado a un centro con ICP, con monitorización y desfibrilador [@ESC_SCA].'));
  else if(sest||hv(o,'tro')) r.push(par('Compatible con IAMSEST o angina inestable: activa ECU 911 para traslado a un centro con ICP; no esperes más resultados [@ESC_SCA].'));
  else if(norm&&hv(o,'dolor')) r.push(par('ECG sin cambios con dolor en curso: no descartes isquemia. Repite el ECG, mide troponina si hay, usa HEART como apoyo y trata como SCA hasta descartarlo [@ESC_SCA][@HEART].'));
  else if(norm) r.push(par('ECG inicial sin cambios: no descarta el síndrome. Repite el ECG, toma troponina si hay y observa; considera otras causas solo después [@ESC_SCA][@AHA_DT].'));
  else r.push(par('Con dolor torácico y sin ECG, hazlo en los primeros 10 min antes de cualquier otra decisión [@ESC_SCA].'));
  if(isq||hv(o,'dolor')){
    if(hv(o,'aas')) r.push(par('Alergia a AAS: no lo des. El segundo antiagregante lo decide el centro con ICP [@ESC_SCA].'));
    else r.push(par('Ácido acetilsalicílico 150–300 mg VO masticada, dosis única [@ESC_SCA].'));
    if(hv(o,'pas')||hv(o,'pde5')){
      r.push(par('No des nitroglicerina: '+(hv(o,'pas')?'la presión sistólica es menor de 90 mmHg':'hay un inhibidor de PDE5 reciente')+' [@ESC_SCA]. Acuesta al paciente y vigila.'));
    } else {
      r.push(par('Si persiste el dolor: nitroglicerina 0,4 mg sublingual cada 5 min, hasta 3 dosis, mientras la presión sistólica se mantenga adecuada [@ESC_SCA].'));
    }
    if(hv(o,'sat')) r.push(par('SatO₂ menor de 90 %: oxígeno inhalado, titulado hasta una SatO₂ de 90 % o más; en Quito compara con el valor basal local [VERIFICAR EN FUENTE] [@ESC_SCA].'));
    else r.push(par('Sin hipoxemia, no des oxígeno de rutina [@ESC_SCA].'));
    r.push(par('Evita las benzodiacepinas para calmar la angustia mientras no se descarte isquemia [@AHA_DT].'));
  }
  r.push('<span class="cf">Si el ECG sigue sin cambios, la troponina seriada es negativa y el dolor cede → considera crisis de angustia y pasa a «Trastorno de pánico»; si el dolor persiste o la troponina sube → trata como SCASEST y mantén el traslado [@ESC_SCA].</span>');
  out(dc,r.join(''));
}
