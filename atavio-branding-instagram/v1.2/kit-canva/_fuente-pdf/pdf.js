process.env.PLAYWRIGHT_BROWSERS_PATH='/opt/pw-browsers';
const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+__dirname+'/brand-guidelines.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
const over=await p.evaluate(()=>[...document.querySelectorAll('.page')].map((s,i)=>s.scrollHeight>s.clientHeight+1?i+1:0).filter(Boolean));
console.log('desbordes',over);
await p.pdf({path:__dirname+'/Atavio-Brand-Guidelines-Canva-v1.2.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});await b.close();})();
