function dcE5tx(dc){
  var c=sel(dc,'cuadro'),s=sel(dc,'sit');
  function e5par(t){return '<p>'+t+'</p>';}
  function e5hv(a,v){return a.indexOf(v)>-1;}
  if(!c.length&&!s.length){
    out(dc,e5par('Elige el cuadro y la situación de la paciente. El simulador propone la conducta con su posología; no calcula probabilidades.'));return;}
  var pru=e5hv(s,'pru'),emb=e5hv(s,'emb'),pal=e5hv(s,'pal'),sinm=e5hv(s,'sinm'),rf=e5hv(s,'rf'),nino=e5hv(s,'nino');
  var ext=e5hv(c,'ext');
  var r=[];
  r.push(e5par('<b>Base</b>: tranquiliza y espera la resolución en 6 a 8 semanas; explica que es autolimitada [@e5_leung2021][@e5_villalon2018].'));
  if(pru){
    if(nino) r.push(e5par('<b>Prurito en menor de 6 años</b>: la ficha de cetirizina cubre desde los 6 años y la de hidrocortisona 1 % desde los 2; no hay dosis de ficha para este grupo, así que usa emoliente y consulta con pediatría o dermatología [@e5_dmcet][@e5_dmhc].'));
    else r.push(e5par('<b>Prurito</b>: emoliente, más cetirizina 10 mg VO cada 24 h (máximo una tableta en 24 h) [@e5_dmcet]; si hay placas muy pruriginosas, hidrocortisona 1 % crema en capa fina hasta 3 a 4 veces al día, hasta 7 días y consulta si persiste [@e5_dmhc].'));
  }
  if(ext){
    if(emb) r.push(e5par('<b>Cuadro extenso en embarazo</b>: no hay dosis gestacional de aciclovir en las fuentes revisadas; decide el antiviral con obstetricia en alto riesgo [@e5_manduca2025].'));
    else if(nino) r.push(e5par('<b>Cuadro extenso en menor de 6 años</b>: no hay dosis pediátrica de aciclovir en las fuentes revisadas; deriva a pediatría o dermatología [@e5_drago2006].'));
    else r.push(e5par('<b>Cuadro extenso o de la primera semana</b>: puedes considerar aciclovir 800 mg VO 5 veces al día por 7 días, de mayor beneficio si se inicia en la primera semana; uso fuera de indicación, con evidencia moderada para la erupción e inconclusa para el prurito [@e5_drago2006][@e5_contreras2019][@e5_rodriguez2018].'));
  }
  if(emb){
    r.push(e5par('<b>Embarazo</b>: pide vigilancia obstétrica; el riesgo de pérdida es mayor si el inicio es antes de la semana 15, con enantema, síntomas generales o afectación de más de la mitad del cuerpo [@e5_drago2018][@e5_manduca2025].'));
  }
  if(pal||sinm||rf){
    r.push(e5par('<b>Descarta sífilis secundaria</b>: solicita VDRL o RPR antes de rotular como pitiriasis rosada; si es reactivo, maneja como sífilis y no como pitiriasis [@e5_villalon2018][@e5_scarvaglieri2025].'));
  }
  r.push('<span class="cf">Si el medallón único es anular con borde escamoso y el KOH es positivo → es tiña del cuerpo y se trata con antifúngico; si hay palmas o plantas con VDRL o RPR reactivo → es sífilis secundaria [@e5_trayes2018][@e5_scarvaglieri2025].</span>');
  out(dc,r.join(''));
}
