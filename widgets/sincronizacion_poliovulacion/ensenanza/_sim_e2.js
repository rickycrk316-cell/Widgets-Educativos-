function e2_par(t){return '<p>'+t+'</p>';}
function e2_has(a,v){return a.indexOf(v)>-1;}

function dcE2(dc){
  var g=sel(dc,'esp'),o=sel(dc,'otros');
  if(!g.length){out(dc,e2_par('Elige la especie y el uso, y los datos adicionales, para obtener el protocolo.'));return;}
  var r=[],v=g[0],bov=(v==='leche'||v==='carne');
  if(e2_has(o,'prenez')&&v!=='prim'&&v!=='dest'){
    r.push(e2_par('<b>Posible gestación</b>: confirma por ecografía antes de todo. No apliques PGF2α, porque provoca aborto [@diapos].'));
  }
  if(bov&&e2_has(o,'anestro')){
    r.push(e2_par('<b>Sin CL ni folículo ≥ 10 mm</b>: la PGF2α no actúa sin cuerpo lúteo y la GnRH no ovula sin folículo capaz [@pursley1995] [VERIFICAR EN FUENTE]. No inicies Ovsynch: pasa a un protocolo con progestágeno (pestaña Progestágenos) [@diapos].'));
  } else if(v==='leche'){
    if(e2_has(o,'celo')) r.push(e2_par('<b>Select Synch</b>: gonadorelina 100 µg IM en D0, cloprostenol 500 µg IM en D7, observación de celo e IA a las positivas [@diapos] [@cimavet].'));
    else if(e2_has(o,'ciclo')) r.push(e2_par('<b>Presynch + Ovsynch</b>: cloprostenol 500 µg IM en D-12; luego gonadorelina 100 µg en D0, cloprostenol 500 µg en D7, gonadorelina 100 µg en D9 e IATF 17–24 h después, para iniciar en los días 5–12 del ciclo [@moreira2001] [@diapos] [@cimavet].'));
    else r.push(e2_par('<b>Ovsynch</b>: gonadorelina 100 µg IM en D0, cloprostenol 500 µg IM en D7, gonadorelina 100 µg IM en D9 e IATF 17–24 h después [@pursley1995] [@diapos] [@cimavet].'));
  } else if(v==='carne'){
    if(e2_has(o,'celo')) r.push(e2_par('<b>Heat Synch</b>: gonadorelina 100 µg IM en D0, cloprostenol 500 µg IM en D7, cipionato de estradiol (dosis [VERIFICAR EN FUENTE]) en D8, observación de celo e IATF en D10 [@diapos] [@cimavet].'));
    else r.push(e2_par('<b>Cosynch</b>: gonadorelina 100 µg IM en D0, cloprostenol 500 µg IM en D7, gonadorelina 100 µg IM en D9 con IATF en el mismo momento [@diapos] [@bo2014] [@cimavet].'));
  } else if(v==='yegua'){
    r.push(e2_par('<b>Yegua</b>: PGF2α en D0 (cloprostenol 250 µg o dinoprost 5 mg IM [VERIFICAR EN FUENTE]), GnRH en D6, PGF2α en D14, GnRH en D20 (dosis de GnRH [VERIFICAR EN FUENTE]); celo en D21 y servicio durante 4–6 días [@diapos] [@cimavet].'));
  } else if(v==='oveja'){
    r.push(e2_par('<b>Oveja</b>: Ovsynch con GnRH en D0, PGF2α en D7 (cloprostenol 125 µg IM [VERIFICAR EN FUENTE]) y GnRH en D9 (dosis [VERIFICAR EN FUENTE]); servicio 17–24 h después [@diapos] [@abecia2012].'));
  } else if(v==='prim'){
    r.push(e2_par('<b>Cerda primeriza</b>: altrenogest 20 mg VO cada 24 h durante 18 días; 1 día después GnRH, a las 78–80 h hCG, e IATF a las 24–26 h y a las 14–16 h [@diapos] [@cimavet]. Dosis de GnRH y hCG [VERIFICAR EN FUENTE].'));
  } else {
    r.push(e2_par('<b>Cerda destetada</b>: 1 día tras el destete GnRH, a las 72–74 h hCG, e IATF a las 24–26 h y a las 16–18 h [@diapos] [@knox2015]. Dosis de GnRH y hCG [VERIFICAR EN FUENTE].'));
  }
  if(bov||v==='oveja') r.push('<span class="cf">Si la hembra está anéstrica y no tiene folículo ≥ 10 mm → la GnRH no ovula y el protocolo falla; usa un progestágeno [@pursley1995] [VERIFICAR EN FUENTE].</span>');
  else if(v==='yegua') r.push('<span class="cf">Si la yegua está en anestro estacional → la PGF2α no tiene cuerpo lúteo que regresar [VERIFICAR EN FUENTE].</span>');
  else r.push('<span class="cf">Si la IATF se hace fuera de las 24–26 h tras la hCG → la inseminación cae antes o después de la ovulación y baja la fertilidad [@diapos].</span>');
  out(dc,r.join(''));
}

