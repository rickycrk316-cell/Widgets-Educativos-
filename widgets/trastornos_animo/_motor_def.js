DECKS.tg=[].concat.apply([],Object.keys(TERMS).map(function(k){return DECKS[k].map(function(c){return {q:c.q,a:c.a,h:c.h,t:k};});}));
const RC={};
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function el(k,s){return document.getElementById('rc-'+k+'-'+s);}
function isCloze(c){return c.q.indexOf('{{')>=0;}
function front(c){return esc(c.q).replace(/\{\{[^}]*\}\}/g,'[ ? ]');}
function back(c){return esc(c.q).replace(/\{\{([^}]*)\}\}/g,'<b>$1</b>');}
function shuffle(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}
function show(id,btn){
  document.querySelectorAll('.tab').forEach(function(s){s.classList.toggle('active',s.id===id);});
  document.querySelectorAll('.tb').forEach(function(b){b.classList.toggle('active',b===btn);});
  try{btn.scrollIntoView({inline:'center',block:'nearest'});}catch(e){}
}
function tog(b){b.parentElement.classList.toggle('op');}
function rc_reset(k){
  var n=DECKS[k].length,idx=[];
  for(var i=0;i<n;i++)idx.push(i);
  RC[k]={queue:shuffle(idx),first:{},fails:{},shown:false,done:0,n:n};
  if(el(k,'e'))el(k,'e').innerHTML='';
  rc_render(k);
}
function rc_render(k){
  var s=RC[k],card=el(k,'c');
  if(!card)return;
  if(!s.queue.length){rc_end(k);return;}
  var c=DECKS[k][s.queue[0]],f=s.fails[s.queue[0]]||0;
  el(k,'n').textContent='Tarjeta '+(s.done+1)+' de '+s.n+(k==='tg'&&s.shown?' · '+TERMS[c.t]:'');
  var h='<p class="rc-q">'+(s.shown&&isCloze(c)?back(c):front(c))+'</p>';
  if(s.shown&&!isCloze(c))h+='<p class="rc-a"><b>Respuesta.</b> '+esc(c.a)+'</p>';
  if(!s.shown&&f>=2)h+='<p class="rc-hint">Pista: '+esc(c.h)+'</p>';
  card.innerHTML=h;
  var b='';
  if(!s.shown){b+='<button class="go" onclick="rc_show(\''+k+'\')">Mostrar respuesta</button>';}
  else{
    b+='<button class="gr ok" onclick="rc_grade(\''+k+'\',\'ok\')">La sabía</button>';
    b+='<button class="gr mid" onclick="rc_grade(\''+k+'\',\'mid\')">A medias</button>';
    b+='<button class="gr ko" onclick="rc_grade(\''+k+'\',\'ko\')">No la sabía</button>';
  }
  b+='<button class="ghost" onclick="rc_reset(\''+k+'\')">Reiniciar mazo</button>';
  el(k,'b').innerHTML=b;
}
function rc_show(k){RC[k].shown=true;rc_render(k);}
function rc_grade(k,g){
  var s=RC[k],i=s.queue.shift();
  if(s.first[i]===undefined)s.first[i]=(g==='ok');
  if(g==='ok'){s.done++;}
  else{s.fails[i]=(s.fails[i]||0)+1;s.queue.push(i);}
  s.shown=false;
  rc_render(k);
}
function rc_verdict(p){return p>=80?['ok','Término consolidado']:['rep','Repasar hoy'];}
function rc_end(k){
  var s=RC[k],ok=0,i,rows='';
  for(i=0;i<s.n;i++)if(s.first[i])ok++;
  var p=Math.round(100*ok/s.n),v=rc_verdict(p);
  el(k,'n').textContent='Mazo completado';
  el(k,'c').innerHTML='<p class="rc-q">Cola agotada: todas las tarjetas se resolvieron.</p>';
  el(k,'b').innerHTML='<button class="ghost" onclick="rc_reset(\''+k+'\')">Reiniciar mazo</button>';
  var h='<div class="rc-end '+v[0]+'">Aciertos al primer intento: '+ok+' de '+s.n+' ('+p+' %). <b>'+v[1]+'</b>.</div>';
  if(k==='tg'){
    Object.keys(TERMS).forEach(function(t){
      var tot=0,hit=0;
      for(i=0;i<s.n;i++){if(DECKS.tg[i].t===t){tot++;if(s.first[i])hit++;}}
      var pp=Math.round(100*hit/tot),vv=rc_verdict(pp);
      rows+='<tr><td>'+esc(TERMS[t])+'</td><td>'+hit+' de '+tot+' ('+pp+' %)</td><td>'+vv[1]+'</td></tr>';
    });
    h+='<div class="tw"><table><thead><tr><th>Término</th><th>Aciertos 1er intento</th><th>Veredicto</th></tr></thead><tbody>'+rows+'</tbody></table></div>';
  }
  el(k,'e').innerHTML=h;
}
Object.keys(DECKS).forEach(rc_reset);
</script>
</div></body></html>
