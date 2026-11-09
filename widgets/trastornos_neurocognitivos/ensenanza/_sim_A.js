function dcE1d(dc){
  var cu=sel(dc,'curso'),at=sel(dc,'atn'),cam=sel(dc,'cam'),mo=sel(dc,'mot'),de=sel(dc,'dem'),pi=sel(dc,'pista');
  if(!(cu.length||at.length||cam.length||mo.length||de.length||pi.length)){
    vacio(dc,'Elige el inicio y curso, la atención, los rasgos adicionales de la CAM, el patrón psicomotor, la demencia previa y las pistas del caso. El simulador dice si cumple el algoritmo de la CAM, el subtipo y qué causa buscar primero con los recursos del centro de salud; no calcula probabilidades.');return;}
  var x=[];
  var c1=hv(cu,'agudo'),c2=hv(at,'alt'),c34=hv(cam,'pens')||hv(cam,'conc');
  var cumple=false;
  if(!cu.length||!at.length){
    x.push(par('Faltan los dos rasgos que abren el algoritmo de la CAM: el inicio y curso, y la atención. Sin ellos no puedes aplicar el criterio [@inouye1990].'));
  } else if(c1&&c2&&c34){
    cumple=true;
    x.push(par('<b>Cumple el algoritmo de la CAM: delirium</b>. Hay inicio agudo con curso fluctuante, inatención y, además, '+(hv(cam,'pens')&&hv(cam,'conc')?'pensamiento desorganizado y conciencia alterada':(hv(cam,'pens')?'pensamiento desorganizado':'conciencia alterada'))+' [@inouye1990][@wilson2020].'));
  } else if(c1&&c2){
    x.push(par('Hay inicio agudo e inatención, pero falta pensamiento desorganizado o conciencia alterada: la CAM exige uno de los dos. Interroga de nuevo estos rasgos antes de descartar; con un 4AT positivo se mantiene la sospecha [@inouye1990][@tieges2021].'));
  } else if(!c1&&hv(cu,'cronico')&&hv(at,'cons')){
    x.push(par('Declive de meses con la atención conservada no es delirium: orienta a un trastorno neurocognitivo. Revisa su pestaña y descarta causas reversibles. <span class="rem">↪ Diferencia en «Visión de conjunto»</span>'));
  } else {
    x.push(par('El patrón no cumple los dos rasgos iniciales de la CAM (inicio agudo fluctuante e inatención). Si el cambio es de horas a días y el informante lo confirma, repite la evaluación [@inouye1990].'));
  }
  if(cumple){
    if(hv(mo,'hiper')) x.push(par('Subtipo <b>hiperactivo</b>: el riesgo es la lesión (caídas, golpe de calor); empieza por las medidas no farmacológicas [@kane8].'));
    else if(hv(mo,'hipo')) x.push(par('Subtipo <b>hipoactivo</b>: pasa por cansancio o depresión y en cuidados críticos se asoció a mayor mortalidad hospitalaria; aplica la CAM en cada contacto [@hughes2021].'));
    else if(hv(mo,'mixto')) x.push(par('Subtipo <b>mixto</b>: alterna fases; reevalúa en cada contacto y no clasifiques por un solo momento [@kane8]. Es la secuencia del caso: inquietud el día previo y luego somnolencia.'));
    else x.push(par('Define el patrón psicomotor para fijar el subtipo (hiperactivo, hipoactivo o mixto) [@kane8].'));
    if(hv(de,'si')) x.push(par('<b>Delirium sobre demencia</b>: la demencia es predisponente; no atribuyas el cambio agudo a ella y busca la misma causa [@wilson2020].'));
    else if(hv(de,'ign')) x.push(par('La demencia previa es desconocida porque vive solo: pregunta al hijo por la basal y reevalúa la cognición cuando el cuadro agudo resuelva [@dsm5tr][@witlox2010].'));
    var cs=[];
    if(hv(pi,'t40')) cs.push('<b>Golpe de calor</b>: temperatura central por encima de 40 °C con disfunción neurológica. Prueba: temperatura central; conducta: enfriamiento rápido y apoyo remoto del especialista [@bouchama2022].');
    if(hv(pi,'gl')) cs.push('<b>Estado hiperosmolar hiperglucémico</b>: glucemia capilar muy alta, con pH de 7,30 o más y bicarbonato de 18 mmol/L o más en la mayoría. Prueba: glucemia, sodio y osmolalidad si hay laboratorio, y búsqueda de cetoacidosis [@ada2024].');
    if(hv(pi,'ca')) cs.push('<b>Hipercalcemia</b>: poliuria, sed y estreñimiento de semanas. Prueba: ECG (QTc corto), calcio corregido o ionizado y PTH [@tonon2022][@walker2022].');
    if(hv(pi,'calor')) cs.push('<b>Deshidratación hipertónica</b>: horas de calor y poca ingesta de agua. Prueba: signos vitales con hidratación, sodio, urea y creatinina [@ada2024][@chauhan2019].');
    if(hv(pi,'inf')) cs.push('<b>Infección</b>: el cuadro viral o urinario es un precipitante clásico. Prueba: temperatura y tira de orina [@wilson2020].');
    if(hv(pi,'farm')) cs.push('<b>Fármacos</b>: los anticolinérgicos y sedantes inducen o empeoran el delirium. Prueba: revisión de la lista de fármacos con el hijo [@beers2023].');
    if(hv(pi,'hip')) cs.push('<b>Hipoxemia</b>: SpO₂ baja. Prueba: oximetría y búsqueda de neumonía o falla cardiaca [@harrison22].');
    if(cs.length){
      x.push(par('Busca primero: '+cs[0]));
      for(var i=1;i<cs.length;i++) x.push(par('También: '+cs[i]));
    } else {
      x.push(par('Sin pistas: mide la glucemia capilar, los signos vitales con temperatura y SpO₂, haz tira de orina y ECG, y revisa los fármacos [@inouye1990][@tonon2022].'));
    }
  }
  x.push('<span class="cf">Si la atención se conserva y el curso pasa a meses → el cuadro se aleja del delirium hacia un trastorno neurocognitivo; si aparece una temperatura central por encima de 40 °C → la prioridad cambia a golpe de calor y enfriamiento rápido [@inouye1990][@bouchama2022].</span>');
  out(dc,x.join(''));
}

function dcE1t(dc){
  var ca=sel(dc,'causa'),si=sel(dc,'sit'),ag=sel(dc,'ag'),d=num(dc,'dosis');
  if(!(ca.length||si.length||ag.length||!isNaN(d))){
    vacio(dc,'Elige la causa identificada, la situación del paciente, la agitación y, si quieres, la dosis de haloperidol por toma. El simulador propone la reposición y el antipsicótico con su tope; los fármacos son los de la tabla.');return;}
  var x=[];
  var cr=hv(si,'cr'),may=hv(si,'mayor'),pk=hv(si,'park'),qt=hv(si,'qt');
  if(!ca.length){
    x.push(par('Sin causa elegida, la conducta es buscarla: glucemia capilar, signos vitales, ECG y electrolitos. El delirium se trata corrigiendo la causa [@wilson2020][@nice_cg103].'));
  }
  if(hv(ca,'ca')){
    x.push(par('<b>Hipercalcemia sintomática</b>: solución salina 0,9 % IV, 1 a 2 L al inicio y luego 200 a 300 mL/h con diuresis objetivo de 100 a 150 mL/h; calcitonina 4 U/kg SC o IM cada 12 h si hay disponibilidad; el bisfosfonato intravenoso (ácido zoledrónico 4 a 8 mg IV en 15 min) es el tratamiento inicial de la hipercalcemia sintomática o grave junto con la hidratación [@tonon2022][@walker2022].'+(cr?' Con insuficiencia cardiaca o renal vigila la sobrecarga y pide apoyo del especialista: la revisión plantea denosumab o diálisis en insuficiencia renal y limita la furosemida a la sobrecarga de volumen [@walker2022][@tonon2022].':'')));
  }
  if(hv(ca,'hhs')){
    var inicio=(cr||may)?'bolos menores (por ejemplo 250 mL) con reevaluación':'500 a 1 000 mL/h durante las primeras 2 a 4 h';
    x.push(par('<b>Hiperglucemia con hiperosmolaridad</b>: solución salina 0,9 % IV, '+inicio+'; corrige el déficit en 24 a 48 h y baja el sodio no más de 10 mmol/L en 24 h. La insulina se difiere hasta que la glucemia deje de bajar solo con líquidos y el potasio sea mayor de 3,5 mmol/L [@ada2024].'));
  }
  if(hv(ca,'na')){
    x.push(par('<b>Hipernatremia por deshidratación</b>: repón volumen y corrige el sodio despacio con controles seriados; se ha sugerido no más de 0,5 mmol/L por hora, aunque no hay una guía firme [@chauhan2019]. '+((cr||may)?'En el adulto mayor frágil o con insuficiencia cardiaca o renal usa bolos menores y vigila la sobrecarga [@ada2024].':'')));
  }
  if(hv(ca,'golpe')) x.push(par('<b>Golpe de calor</b>: enfriamiento rápido, único tratamiento específico, junto con la reposición de volumen y apoyo remoto del especialista [@bouchama2022].'));
  if(hv(ca,'inf')) x.push(par('<b>Infección</b>: trata el foco que identifiques y reevalúa el delirium cuando ceda [@wilson2020].'));
  if(hv(ca,'farm')) x.push(par('<b>Fármaco nocivo</b>: retira o sustituye anticolinérgicos, benzodiacepinas, hipnóticos Z, opioides y antagonistas H2 [@beers2023].'));
  x.push(par('<b>Medidas no farmacológicas</b> en todos los casos: hidratación, orientación, sueño, movilización, gafas y audífonos, y acompañamiento del hijo [@inouye1999][@hshieh2018].'));
  if(hv(ag,'no')||hv(ag,'leve')){
    x.push(par('<b>Sin antipsicótico</b>: no hay riesgo ni angustia grave; la angustia leve cede con desescalada verbal y medidas ambientales. Los antipsicóticos no acortaron el delirium frente a placebo [@nice_cg103][@nikooie2019].'));
  } else if(hv(ag,'riesgo')){
    if(pk){
      x.push(par('<b>Parkinson: no uses haloperidol</b>, contraindicado en la ficha; la Beers 2023 solo exceptúa clozapina, pimavanserina y quetiapina. La dosis de quetiapina no está establecida en las fuentes revisadas: pide apoyo especializado [@haloperidol_dm][@beers2023].'));
    } else {
      var tope=2,dd=isNaN(d)?0.5:d;
      if(dd<=0){
        x.push(par('La dosis debe ser mayor de cero. Inicia en el extremo bajo del rango geriátrico de la ficha (0,5 mg) [@haloperidol_dm].'));
      } else {
        var dm=Math.min(dd,tope);
        var t='<b>Haloperidol '+String(rd(dm,1)).replace('.',',')+' mg VO por toma</b>, cada 8 a 12 h y por una semana o menos, a la dosis más baja que controle el riesgo [@haloperidol_dm][@nice_cg103].';
        if(dd>tope) t+=' Pediste '+String(rd(dd,1)).replace('.',',')+' mg: el tope por toma del rango geriátrico de la ficha es '+tope+' mg y se aplicó.';
        t+=' Uso fuera de la indicación de la ficha; el haloperidol no mejoró la duración del delirium frente a placebo [@nikooie2019].';
        if(qt) t+=' Con QT prolongado, la ficha describe torsades de pointes con haloperidol: pide apoyo especializado antes de usarlo [@haloperidol_dm].';
        x.push(par(t));
      }
    }
  } else if(!isNaN(d)){
    x.push(par('Elige el nivel de agitación: el antipsicótico solo se considera si hay riesgo para el paciente o para otros, o angustia grave [@nice_cg103].'));
  }
  x.push(par('Evita benzodiacepinas (salvo abstinencia alcohólica) y anticolinérgicos [@beers2023].'));
  x.push('<span class="cf">Si hay enfermedad de Parkinson → el haloperidol deja de ser opción y pasa a quetiapina con apoyo del especialista; si la agitación pasa de angustia a riesgo para sí o para otros → de ningún antipsicótico a haloperidol a dosis baja por una semana o menos [@haloperidol_dm][@beers2023][@nice_cg103].</span>');
  out(dc,x.join(''));
}
