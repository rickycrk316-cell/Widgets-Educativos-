function e3_p(t){return '<p>'+t+'</p>';}
function e3_h(a,v){return a.indexOf(v)>-1;}

function dcE3(dc){
  var g=sel(dc,'esp'),o=sel(dc,'otros');
  if(!g.length){
    out(dc,e3_p('Elige la especie y el grupo, y añade si prefieres CIDR u Ovsynch, si hay anestro o si usas esponja. El simulador propone el protocolo con progestágeno, el dato que falta y la hora de la IATF; no calcula probabilidades.'));return;}
  var e=g[0],r=[],cf='';
  var anes=e3_h(o,'anes');
  if(e==='vl'){
    r.push(e3_p('<b>Vaquilla de leche · Crestar</b>: día 0 implante de norgestomet 3 mg más inyección de 3 mg de norgestomet y 5 mg de valerato de estradiol IM; día 9 retiro; IATF a las 48 h. Sin eCG ni PGF2α [@diapos][@cimavet].'));
    cf='Si la vaquilla no estaba ciclando o perdió el implante → no cuentes con la IATF a 48 h: revisa ovarios y repite el esquema.';
  }else if(e==='cl'){
    r.push(e3_p('<b>Vaca de leche · Crestar</b>: día 0 implante e inyección de norgestomet con valerato de estradiol; día 7 cloprostenol 500 µg IM para regresar el CL; día 9 retiro y eCG IM (dosis según ficha del producto); IATF a las 56 h [@diapos][@cimavet].'));
    cf='Si hay CL y no das la PGF2α del día 7 → el CL mantiene la P4 y la ovulación se dispersa.';
  }else if(e==='vc'||e==='cc'){
    var h=e==='vc'?48:56;
    r.push(e3_p('<b>'+(e==='vc'?'Vaquilla':'Vaca')+' de carne · Crestar</b>: día 0 implante e inyección; día 9 retiro con eCG (Folligon) IM (dosis según ficha del producto); IATF a las '+h+' h [@diapos][@cimavet].'));
    cf='Si hay anestro o condición corporal baja → la eCG al retiro es el punto crítico; sin ella el folículo no ovula bien [@bo2014].';
  }else if(e==='rep'){
    r.push(e3_p('<b>Vaca repetidora · resincronización</b>: tras la IATF, 13 días después coloca CIDR 1,38 g de P4 más BE 2 mg IM; día 7 retiro; día 8 BE 1 mg IM; IA a celo visto los días 9 a 12 [@diapos][@cimavet].'));
    cf='Si ves celo antes del día 7 → retira el CIDR y reinicia el protocolo.';
  }else if(e==='ove'||e==='cab'){
    var esp=e3_h(o,'esp');
    if(e==='ove') r.push(e3_p('<b>Oveja · '+(esp?'esponja Chronogest CR':'CIDR')+'</b>: dispositivo 12–14 días '+(esp?'(dosis según ficha del producto)':'(0,3 g de P4)')+'; al retiro eCG IM (dosis según ficha, raza y estación); celo y servicio a las 36–72 h [@diapos][@abecia2012].'));
    else if(esp) r.push(e3_p('<b>Cabra · esponja</b>: día 0 esponja; día 10 cloprostenol IM (dosis según ficha); día 12 retiro con eCG IM (dosis según ficha, raza y estación); servicio a las 36–40 h [@diapos][@abecia2012].'));
    else r.push(e3_p('<b>Cabra · CIDR</b>: 0,3 g de P4 por 14 días; al retiro eCG IM (dosis según ficha, raza y estación); servicio a las 36–48 h [@diapos][@cimavet].'));
    cf='Si es la época de anestro estacional → el efecto del dispositivo depende de la eCG; revisa la condición corporal.';
  }else if(e==='yeg'){
    r.push(e3_p('<b>Yegua · Regumate</b>: altrenogest 0,044 mg/kg VO cada 24 h por 15 días y PGF2α al retiro (dinoprost 5 mg IM); la diapositiva marca 2 días tras la PGF2α y 4–6 días hasta el celo y el servicio [@diapos][@cimavet].'));
    cf='Si la yegua está gestante → no uses altrenogest ni PGF2α sin confirmar vacía.';
  }else if(e==='cerp'){
    r.push(e3_p('<b>Cerda primeriza · Regumate</b>: altrenogest 20 mg por cerda VO cada 24 h por 18 días; celo a los 5–6 días tras el retiro; servicio al día siguiente [@diapos][@knox2015].'));
    cf='Si no sale en celo a los 6 días → revisa edad, peso y alimentación antes de repetir.';
  }else if(e==='cerd'){
    r.push(e3_p('<b>Cerda recién destetada · Regumate</b>: altrenogest 20 mg por cerda VO cada 24 h por 3 días desde el destete; celo a los 5–6 días; servicio al día siguiente [@diapos][@knox2015].'));
    cf='Si la cerda llegó con mala condición corporal → el celo se retrasa; mejora la ración tras el destete.';
  }
  if(anes&&(e==='vl'||e==='cl'||e==='rep'))
    r.push(e3_p('Con anestro o mala condición corporal, añade eCG al retiro aunque el esquema de leche no la lleve [@bo2014].'));
  if(e3_h(o,'ovs')&&(e==='vl'||e==='cl'||e==='vc'||e==='cc'||e==='rep'))
    r.push(e3_p('Alternativa CIDR + Ovsynch: día 0 CIDR más gonadorelina 100 µg IM; día 7 retiro y cloprostenol 500 µg IM; día 9 gonadorelina; IATF a las 18 h [@diapos][@cimavet].'));
  else if(e3_h(o,'cidr')&&(e==='vl'||e==='cl'||e==='vc'||e==='cc'))
    r.push(e3_p('Alternativa CIDR + BE: día 0 CIDR y BE 2 mg IM; día 7 retiro y cloprostenol 500 µg IM; día 8 BE 1 mg IM; IATF a las 30 h del BE [@diapos][@cimavet].'));
  r.push('<span class="cf">'+cf+'</span>');
  out(dc,r.join(''));
}

