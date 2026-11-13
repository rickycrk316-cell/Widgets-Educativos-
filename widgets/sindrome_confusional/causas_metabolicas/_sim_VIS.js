function dcVis(dc){
  var t=sel(dc,'tg'),l=sel(dc,'lab'),h=sel(dc,'his');
  if(!(t.length||l.length||h.length)){
    vacio(dc,'Elige los hallazgos de cabecera que tienes. El simulador lista todas las entidades compatibles por urgencia, el hallazgo que falta y la conducta inicial; no calcula probabilidades.');return;}
  var x=[],n=0;
  var tem=hv(t,'tem'),glu=hv(t,'glu'),cet=hv(t,'cet'),kus=hv(t,'kus');
  var nat=hv(l,'nat'),uri=hv(l,'uri'),cal=hv(l,'cal'),est=hv(h,'est');
  if(tem){n++;x.push(par('<b>Golpe de calor</b>: temperatura alta con encefalopatía tras el calor es su perfil [@bouchama2022]. Falta confirmar que la temperatura central rectal supera 40 °C y buscar glucemia y sodio, porque coexiste con deshidratación. Conducta: enfriar de inmediato antes de cualquier estudio [@eifling2024]. ↪ Pestaña «Golpe de calor».'));}
  if(glu&&!(cet&&kus)){n++;x.push(par('<b>Estado hiperosmolar</b>: glucemia capilar muy alta con deshidratación y confusión [@umpierrez2024]. Falta la glucemia y la osmolalidad efectiva del laboratorio, con cetonas escasas; sin osmolalidad medida, apóyate en sodio y glucosa. Conducta: reponer volumen antes que insulina y vigilar el potasio [@pasquel2014]. ↪ Pestaña «Estado hiperosmolar».'));}
  if(glu&&cet&&kus){x.push(par('Cetonas con respiración de Kussmaul y glucemia alta orientan a cetoacidosis diabética o a un cuadro mixto; el estado hiperosmolar típico tiene cetosis leve y sin acidosis grave [@umpierrez2024]. El manejo inicial de volumen y potasio está en «Estado hiperosmolar».'));n++;}
  else if((cet||kus)&&!glu){x.push(par('Cetonas o Kussmaul sin glucemia alta: no es el perfil del estado hiperosmolar; mide la glucemia y busca otra acidosis [@umpierrez2024].'));}
  if(cal||(est&&!glu)){n++;x.push(par('<b>Hipercalcemia</b>: semanas de poliuria y estreñimiento, o QT corto, la sugieren [@walker2022] [@elsherif2011]. Falta el calcio corregido por albúmina (luego PTH si hay; si no, déjalo anotado para referir). Conducta: hidratar con solución salina; el tratamiento específico depende de la gravedad. ↪ Pestaña «Hipercalcemia».'));}
  if(nat){n++;x.push(par('<b>Hipernatremia</b>: sodio sérico mayor de 145 mEq/L es déficit de agua libre [@chauhan2019]. Falta la causa: diuresis, glucemia y calcio. Conducta: calcular el agua libre y bajar el sodio despacio. ↪ Pestaña «Hipernatremia».'));}
  if(uri){n++;x.push(par('<b>Azotemia prerrenal</b>: diuresis escasa con urea alta orienta a hipoperfusión renal [@khwaja2012]. Falta ver la creatinina que mejora con volumen y descartar el globo vesical. Conducta: reponer volumen, suspender nefrotóxicos y medir la diuresis cada hora. ↪ Pestaña «Azotemia prerrenal».'));}
  if(!tem) x.push(par('Sin temperatura rectal medida, no descartes el golpe de calor: mídela ahora.'));
  if(n>1) x.push(par('Pueden coexistir: la hiperglucemia o el calcio alto producen poliuria, hipernatremia y azotemia prerrenal; busca todas [@umpierrez2024] [@walker2022].'));
  x.push('<span class="cf">Si la temperatura rectal pasa de 40 °C con encefalopatía → golpe de calor y se enfría primero; si la glucemia capilar es normal → se descarta el estado hiperosmolar; si el sodio es alto con calcio y glucemia normales → hipernatremia o azotemia prerrenal sin causa metabólica añadida.</span>');
  out(dc,x.join(''));
}
