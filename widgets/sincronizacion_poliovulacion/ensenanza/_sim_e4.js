function e4_has(a,v){return a.indexOf(v)>-1;}
function dcE4(dc){
  var m=sel(dc,'m'),o=sel(dc,'o');
  if(!m.length){out(dc,'<p>Elige el método de superovulación y los datos adicionales para obtener el protocolo y la conducta con las receptoras.</p>');return;}
  var r=[];
  if(e4_has(m,'fsh')){
    r.push('<p><b>FSH en dosis decrecientes</b>: se inicia unos 10 días tras el estro, dos veces al día (cada 12 h) durante 5 días, 5-4-3-2-2 mg por día o 6-5-4-3-2 mg por día repartidos en mañana y tarde, y PGF2α a doble dosis al final del esquema [@diapos]. Dosis de ficha: 400 mg NIH-FSH-P1 en total [@cimavet] [VERIFICAR EN FUENTE el número de dosis y el día de la PGF2α].</p>');
  } else {
    r.push('<p><b>eCG (PMSG) en inyección única</b>: 1 500 a 3 000 UI IM en el día 9 a 12 del ciclo [VERIFICAR EN FUENTE], PGF2α a doble dosis 2 días después y GnRH a mitad de dosis (50 µg) dos veces, 2 días más tarde y 1,5 h después [@diapos] [@cimavet] [VERIFICAR EN FUENTE los intervalos].</p>');
  }
  if(e4_has(o,'onda')) r.push('<p>La onda emergente es el momento ideal para empezar: el grupo de folículos reclutado responde mejor [@adams2008] [@bomapletoft2014].</p>');
  else r.push('<p>Sin onda confirmada, falta ecografía: iniciar sin ella aumenta la variabilidad de la respuesta [@bomapletoft2014].</p>');
  if(e4_has(o,'quiste')){
    if(e4_has(m,'ecg')) r.push('<p><b>Cambia a FSH</b>: la eCG permanece días en la sangre y dejó quistes antes; considera anti-eCG [@bomapletoft2014].</p>');
    else r.push('<p>La FSH, de vida media corta, evita la sobreestimulación prolongada de la eCG: buena elección tras quistes [@bomapletoft2014].</p>');
  }
  if(e4_has(o,'sinrec')) r.push('<p><b>Falta sincronizar receptoras</b>: ajusta sus protocolos (PGF2α, GnRH o progestágenos, ver otras pestañas) para que el celo sea casi el de la donante; si no, no inicies la superovulación [@silabo].</p>');
  else r.push('<p>Con receptoras sincronizadas, lava a los 7 días de la inseminación y transfiere los embriones evaluados [@silabo].</p>');
  r.push('<span class="cf">Si la donante muestra ovarios muy grandes o quistes tras la eCG → cambia a FSH en dosis decrecientes o usa anti-eCG [@bomapletoft2014].</span>');
  out(dc,r.join(''));
}

