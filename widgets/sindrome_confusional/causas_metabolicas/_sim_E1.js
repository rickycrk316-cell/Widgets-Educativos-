function e1_f(x,d){return String(rd(x,d)).replace('.',',');}
function dcE1d(dc){
var na=num(dc,'na'),glu=num(dc,'glu');
var vol=sel(dc,'vol')[0],diu=sel(dc,'diu')[0],uos=sel(dc,'uos')[0],dur=sel(dc,'dur')[0];
if(isNaN(na)&&!vol&&!diu&&!uos&&!dur){vacio(dc,'Escribe el sodio y elige el volumen, la diuresis, la osmolalidad urinaria y la evolución para ver la clasificación.');return;}
var h='';
if(!isNaN(na)){
if(na<=145){vacio(dc,'Sodio de '+e1_f(na,0)+' mEq/L: no cumple el criterio de hipernatremia (mayor de 145 mEq/L) [@yun2022]. Busca otra causa del delirium.');return;}
h+=par('<b>Sodio '+e1_f(na,0)+' mEq/L:</b> hipernatremia [@yun2022].');
if(!isNaN(glu)&&glu>100){h+=par('Sodio corregido por glucosa: '+e1_f(na+0.024*(glu-100),1)+' (Hillier) o '+e1_f(na+0.016*(glu-100),1)+' (Katz) mEq/L [@yun2022]. Con glucemia alta, considera diuresis osmótica: «Estado hiperosmolar».');}
}
if(vol==='hipo')h+=par('<b>Hipovolémica:</b> pierde agua y sodio, más agua. Causas: sudor, diuresis osmótica, diuréticos, diarrea. Si hay shock, salina isotónica primero; luego agua libre [@yun2022].');
else if(vol==='eu')h+=par('<b>Euvolémica:</b> pérdida de agua sin sodio (diabetes insípida, piel y respiración). Agua libre [@yun2022].');
else if(vol==='hiper')h+=par('<b>Hipervolémica:</b> ganancia de sodio hipertónico, a menudo iatrogénica. Agua libre con dextrosa y diurético [@yun2022].');
if(dur==='ag')h+=par('<b>Aguda (menos de 48 h):</b> se tolera un descenso de hasta 1 mEq/L por hora [@qian2019].');
else if(dur==='cr')h+=par('<b>Crónica o desconocida:</b> descenso menor de 0,5 mmol/L por hora (12 mmol/L por día; unos 10 según otra fuente) [@yun2022] [@qian2019].');
if(uos==='alta')h+=par('Orina de más de 800 mOsm/kg: pérdida extrarrenal (piel, intestino) o poca ingesta; la respuesta renal es la adecuada [@yun2022].');
else if(uos==='med')h+=par('Orina de 300 a 800 mOsm/kg: diabetes insípida parcial o diuresis osmótica; mide glucemia [@yun2022].');
else if(uos==='baja')h+=par('Orina de menos de 300 mOsm/kg'+(diu==='pol'?' con poliuria: patrón de diabetes insípida. Busca calcio sobre 11 mg/dL (2,75 mmol/L), potasio bajo 3,0 mmol/L y litio [@yun2022] [@qian2019].':': orina diluida con hipertonicidad indica falla de concentración [@yun2022].'));
else if(uos==='nd')h+=par('Sin osmolalidad urinaria: apóyate en historia (calor, ingesta), volumen de orina y glucemia.');
if(diu==='pol'&&uos!=='baja')h+=par('Poliuria de más de 3 L/día: diabetes insípida o diuresis osmótica [@yun2022].');
h+=par('<b>Qué buscar ahora:</b> glucemia, calcio corregido, potasio, urea y creatinina.');
h+='<span class="cf">Si la glucemia está muy alta → «Estado hiperosmolar»; si el calcio supera 11 mg/dL → «Hipercalcemia»; si hay fiebre muy alta tras el calor → «Golpe de calor».</span>';
out(dc,h);}
function dcE1t(dc){
var peso=num(dc,'peso'),na=num(dc,'na'),nao=num(dc,'nao');
var sx=sel(dc,'sx')[0],ed=sel(dc,'ed')[0],dur=sel(dc,'dur')[0],sh=sel(dc,'sh')[0],beb=sel(dc,'beb')[0],cond=sel(dc,'cond');
if(isNaN(peso)||isNaN(na)||isNaN(nao)||!sx||!ed||!dur||!sh||!beb){vacio(dc,'Completa peso, sodio actual y objetivo, sexo, edad, evolución, estado hemodinámico y si puede beber.');return;}
if(na<=nao){vacio(dc,'El sodio actual no supera el objetivo: no hay déficit de agua libre que calcular.');return;}
var fr=(sx==='m'?0.6:0.5)-(ed==='may'?0.05:0);
var tbw=peso*fr,def=tbw*(na/nao-1);
var tope=dur==='ag'?24:12,drop=na-nao,d1=Math.min(drop,tope);
var v=Math.min(3*peso*d1,def*1000);
var h='';
h+=par('Agua corporal total: '+e1_f(fr*100,0)+' % de '+e1_f(peso,0)+' kg = '+e1_f(tbw,1)+' L. Déficit de agua libre = '+e1_f(def,1)+' L [@yun2022].');
h+=par('<b>Primer día:</b> descenso de '+e1_f(d1,0)+' mmol/L; tope '+tope+' mmol/L por 24 h ('+(dur==='ag'?'1 mEq/L por hora, aguda':'0,5 mmol/L por hora, crónica')+') [@yun2022] [@qian2019]. Cohortes de críticos no hallaron daño con más rápido [@chauhan2019] [@feigin2023]; aquí se mantiene el tope.');
if(sh==='si'){h+=par('<b>Shock o hipotensión:</b> primero solución salina 0,9 % o cristaloide balanceado hasta restaurar el volumen, sin importar el sodio [@yun2022] [@nacl09_iv]. Volumen por carga: no establecido en las fuentes. Luego, agua libre así.');}
var free=v;
if(cond.indexOf('hv')>-1)h+=par('Con sobrecarga de volumen: agua libre con dextrosa al 5 % y diurético [@yun2022].');
if(cond.indexOf('glu')>-1)h+=par('Con hiperglucemia marcada la dextrosa al 5 % está contraindicada [@dextrosa_iv]: usa salina 0,45 % (la mitad es agua libre) y trata la glucemia.');
if(beb==='si'&&sh==='no'&&cond.indexOf('glu')<0){h+=par('<b>Agua por vía oral</b> fraccionada: '+e1_f(free,0)+' mL en 24 h (3 mL/kg por mmol/L de descenso, tope: el déficit calculado) [@yun2022] [@qian2019].');}
else if(cond.indexOf('glu')>-1){h+=par('<b>Salina 0,45 % IV:</b> '+e1_f(free*2,0)+' mL en 24 h, unos '+e1_f(free*2/24,0)+' mL/h [@nacl045_iv] [@yun2022]. Cambio esperado del sodio por litro: '+e1_f((77-na)/(tbw+1),1)+' mEq/L (Adrogué–Madias) [@yun2022].');}
else{h+=par('<b>Dextrosa al 5 % IV o agua por sonda:</b> '+e1_f(free,0)+' mL en 24 h, unos '+e1_f(free/24,0)+' mL/h; ritmo de inicio de la fuente 1,35 mL/kg/h = '+e1_f(1.35*peso,0)+' mL/h [@yun2022] [@dextrosa_iv]. Cambio esperado del sodio por litro: '+e1_f((0-na)/(tbw+1),1)+' mEq/L; falla con hipovolemia grave e insuficiencia renal [@yun2022].');}
h+=par('Suma pérdidas insensibles y continuas. Mide el sodio cada 2 h al inicio y ajusta la velocidad [@qian2019]. Si se pasó del objetivo, no vuelvas a subirlo [@yun2022].');
h+='<span class="cf">Si hay hipotensión → primero solución salina isotónica; si la glucemia está muy alta → sin dextrosa al 5 % y ve a «Estado hiperosmolar».</span>';
out(dc,h);}
