function e1par(t){return '<p>'+t+'</p>';}
function e1hv(a,v){return a.indexOf(v)>-1;}
function e1vacio(dc,t){out(dc,e1par(t));}

function dcE1dx(dc){
  var ed=sel(dc,'edad'),pr=sel(dc,'prur'),pa=sel(dc,'panal'),al=sel(dc,'alarma'),ig=sel(dc,'iga');
  var uk=num(dc,'uk'),sc=num(dc,'scorad'),ea=num(dc,'easi');
  if(!(ed.length||pr.length||pa.length||al.length||ig.length)&&isNaN(uk)&&isNaN(sc)&&isNaN(ea)){
    e1vacio(dc,'Elige la edad, el prurito, los criterios del Reino Unido presentes, el área del pañal y las escalas de gravedad. El simulador integra el diagnóstico, la gravedad y la conducta inicial; no calcula probabilidades.');return;}
  var x=[];
  if(e1hv(al,'si')){
    x.push(e1par('<b>Eccema herpético</b>: vesiculopústulas dolorosas con fiebre sobre una dermatitis atópica son una urgencia. Falta confirmar el virus del herpes simple con cultivo o PCR, sin retrasar el tratamiento; el hemograma suele mostrar leucopenia y linfopenia relativas [@e1_traidl2021][@e1_chan2022]. Conducta inicial: derivación urgente a hospital y aciclovir intravenoso [@e1_almoalem2022].'));
  }
  if(!isNaN(uk)&&(uk<0||uk>5)){
    x.push(e1par('Los criterios del Reino Unido adicionales al prurito van de 0 a 5: revisa el número [@e1_williams1994].'));
  } else if(e1hv(pr,'no')){
    x.push(e1par('<b>Sin prurito marcado</b>: la dermatitis atópica pierde sustento, porque la condición pruriginosa es la puerta de entrada de los criterios del Reino Unido [@e1_williams1994]. '+(e1hv(ed,'lact')?'En el lactante con placas rojas y escama en cuero cabelludo y cara, considera la dermatitis seborreica; falta ver si el área del pañal está afectada. ':'')+'Conducta inicial: revisa otra dermatosis descamativa; ver la pestaña «D. seborreica» y «Visión».'));
  } else if(e1hv(pr,'si')){
    if(e1hv(ed,'lact')&&e1hv(pa,'afect')){
      x.push(e1par('<b>Prurito con afectación del área del pañal en un lactante</b>: una erupción del pañal rara vez es dermatitis atópica [@e1_peters2019]. Falta explorar cuero cabelludo y pliegues y valorar la dermatitis seborreica. Conducta inicial: no cierres como atópica sin otro dato; revisa el diferencial en «Visión».'));
    } else if(!isNaN(uk)){
      if(uk>=3){
        x.push(e1par('<b>Dermatitis atópica</b>: prurito más '+uk+' criterios adicionales cumple la regla de tres o más de los criterios del Reino Unido [@e1_williams1994]. Falta medir la gravedad con SCORAD, EASI o IGA y buscar sobreinfección. Conducta inicial: emoliente diario y tratamiento según la gravedad (ver «Tratamiento») [@sidbury2023].'));
      } else {
        x.push(e1par('<b>Prurito con menos de tres criterios adicionales</b>: no cumple la regla de los criterios del Reino Unido [@e1_williams1994]. Falta completar la historia (piel seca, inicio antes de 2 años, asma, dermatitis flexural visible) y evaluar el diferencial. Conducta inicial: seguimiento y reevaluación; los criterios son clínicos y no hay prueba definitiva [@e1_de2006].'));
      }
    } else {
      x.push(e1par('<b>Prurito presente</b>: compatible con dermatitis atópica si hay curso crónico y distribución típica por edad [@e1_peters2019]. Falta contar los criterios del Reino Unido adicionales al prurito [@e1_williams1994].'));
    }
  }
  var g=[];
  if(!isNaN(sc)){
    if(sc<0||sc>103){g.push('SCORAD fuera de rango (0 a 103) [@e1_scorad1993]');}
    else{var b=sc<10?'piel clara':sc<29?'leve':sc<49?'moderada':'grave';g.push('SCORAD '+sc+': '+b);}
  }
  if(!isNaN(ea)){
    if(ea<0||ea>72){g.push('EASI fuera de rango (0 a 72) [@e1_hanifin2001]');}
    else{var c=ea===0?'piel clara':ea<6?'leve':ea<23?'moderada':'grave';g.push('EASI '+ea+': '+c);}
  }
  if(ig.length){var m={claro:'clara',leve:'leve',mod:'moderada',grave:'grave'};g.push('IGA: '+m[ig[0]]);}
  if(g.length){
    var nota=e1hv(ed,'adol')?'':' Los cortes de SCORAD y EASI se establecieron en 13 años o más; en niños úsalos con cautela.';
    x.push(e1par('<b>Gravedad</b>: '+g.join('; ')+' [@e1_chopra2017].'+nota+' La gravedad fija el escalón del tratamiento; ver «Tratamiento».'));
  }
  if(!x.length) x.push(e1par('Los datos elegidos no bastan para sostener un diagnóstico. Define el prurito y cuenta los criterios del Reino Unido.'));
  x.push('<span class="cf">Si el lactante tiene afectado el área del pañal y no hay prurito → el diagnóstico pasa de dermatitis atópica a dermatitis seborreica; si aparecen vesiculopústulas dolorosas con fiebre → eccema herpético y urgencia con aciclovir [@e1_peters2019][@e1_traidl2021].</span>');
  out(dc,x.join(''));
}

function dcE1tx(dc){
  var ed=sel(dc,'edad'),gr=sel(dc,'grav'),zo=sel(dc,'zona'),fa=sel(dc,'fase'),inf=sel(dc,'inf'),p=num(dc,'peso');
  if(!(ed.length||gr.length||zo.length||fa.length||inf.length)&&isNaN(p)){
    e1vacio(dc,'Elige la edad, la gravedad, la zona, la situación y los signos de infección; escribe el peso si el niño pasa a dupilumab. El simulador propone el escalón con posología y no calcula probabilidades.');return;}
  var x=[];
  if(e1hv(inf,'vesic')){
    x.push(e1par('<b>Eccema herpético</b>: derivación urgente a hospital y <b>aciclovir intravenoso</b>; la dosis pediátrica por peso sigue el protocolo hospitalario y no se fija aquí [@e1_almoalem2022][@e1_chan2022]. El diagnóstico y el tratamiento rápidos son cruciales [@e1_traidl2021].'));
    x.push('<span class="cf">Si las vesiculopústulas dolorosas y la fiebre no están y solo hay costras → es sobreinfección bacteriana y se maneja con cultivo y el plan tópico [@e1_peters2019].</span>');
    out(dc,x.join(''));return;
  }
  x.push(e1par('<b>Base para todos</b>: emoliente diario sobre toda la piel, incluso sin lesiones, y plan de acción escrito para la familia [@sidbury2023][@e1_eichenfield2014]. Posología en «Tratamiento».'));
  if(e1hv(inf,'costras')){
    x.push(e1par('Costras y exudado: sospecha sobreinfección por <i>S. aureus</i>; toma cultivo para guiar el tratamiento y no uses antimicrobianos ni antisépticos tópicos de rutina [@e1_peters2019][@sidbury2023].'));
  }
  var refr=e1hv(fa,'refrac')||e1hv(gr,'grave');
  if(!refr){
    if(e1hv(zo,'cara')){
      x.push(e1par('<b>Cara, pliegues o genitales</b>: corticoide de baja potencia (hidrocortisona 1 %) o tacrolimus ungüento 0,03 % en niños (0,1 % en mayores), capa fina sobre las lesiones activas [@e1_eichenfield2014][@e1_martins2015][@e1_yan2008].'));
    } else if(e1hv(zo,'cuerpo')){
      x.push(e1par('<b>Tronco y extremidades</b>: corticoide tópico con potencia según la gravedad, capa fina sobre las lesiones activas; ver «Visión» para la escalera de potencias [@sidbury2023][@e1_eichenfield2014].'));
    }
    if(e1hv(gr,'leve')||e1hv(gr,'mod')){
      if(e1hv(ed,'lact')){
        x.push(e1par('En menores de 2 años no hay ensayos verificados de crisaborol ni de ruxolitinib aquí: usa corticoide de baja potencia o tacrolimus [@e1_paller2016][@e1_eichenfield2025].'));
      } else if(e1hv(ed,'pre')||e1hv(ed,'esc')){
        x.push(e1par('Alternativa en dermatitis leve a moderada: crisaborol ungüento dos veces al día por 28 días (ensayos desde los 2 años) o ruxolitinib crema 0,75 % o 1,5 % dos veces al día por 8 semanas (2 a 11 años, IGA 2 o 3, 3 a 20 % de superficie) [@e1_paller2016][@e1_eichenfield2025].'));
      } else if(e1hv(ed,'adol')){
        x.push(e1par('Alternativa en dermatitis leve a moderada: crisaborol (dos veces al día, 28 días en ensayos) o ruxolitinib crema; la guía AAD da recomendación fuerte a los agentes PDE-4 y JAK tópicos en adultos [@e1_paller2016][@sidbury2023].'));
      }
    }
  } else {
    x.push(e1par('<b>Enfermedad grave o sin respuesta a tópicos optimizados</b>: revisa adherencia, sobreinfección y diagnóstico, y deriva a dermatología. Considera fototerapia o un sistémico [@davis2024].'));
    if(e1hv(ed,'lact')||e1hv(ed,'pre')){
      if(isNaN(p)){
        x.push(e1par('Escribe el peso para fijar la dosis de dupilumab por banda de peso (6 meses a menos de 6 años) [@e1_paller2022].'));
      } else if(p<5){
        x.push(e1par('Peso de '+p+' kg: por debajo de los 5 kg del ensayo; dupilumab no está respaldado en esta banda, decide el especialista [@e1_paller2022].'));
      } else if(p>=30){
        x.push(e1par('Peso de '+p+' kg: sobre la banda estudiada en menores de 6 años; la dosis la fija el especialista y no se verificó aquí [@e1_paller2022].'));
      } else {
        var d=Math.min(300,p<15?200:300);
        x.push(e1par('<b>Dupilumab subcutáneo: '+rd(d)+' mg cada 4 semanas</b> (5 kg a menos de 15 kg: 200 mg; 15 kg a menos de 30 kg: 300 mg; tope 300 mg por dosis), con corticoide tópico de baja potencia durante 16 semanas en el ensayo; vigila conjuntivitis [@e1_paller2022].'));
      }
    } else if(e1hv(ed,'esc')){
      x.push(e1par('De 6 a 11 años: la dosis de dupilumab y de los demás sistémicos no se verificó aquí y la fija el especialista [@davis2024].'));
    } else if(e1hv(ed,'adol')){
      x.push(e1par('La guía AAD 2024 (adultos) recomienda con fuerza dupilumab, tralokinumab, abrocitinib, baricitinib y upadacitinib; de forma condicional fototerapia, azatioprina, ciclosporina, metotrexato y micofenolato, y condicional en contra el corticoide sistémico. La dosis la fija el especialista [@davis2024].'));
    }
  }
  x.push('<span class="cf">Si aparecen vesiculopústulas dolorosas con fiebre → eccema herpético: el plan cambia de tópicos a aciclovir intravenoso en hospital [@e1_traidl2021][@e1_almoalem2022].</span>');
  out(dc,x.join(''));
}
