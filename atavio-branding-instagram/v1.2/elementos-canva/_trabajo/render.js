process.env.PLAYWRIGHT_BROWSERS_PATH='/opt/pw-browsers';
const {chromium}=require('/opt/node22/lib/node_modules/playwright');
const fs=require('fs'),path=require('path');
const jobs=JSON.parse(fs.readFileSync(process.argv[2]));
(async()=>{const b=await chromium.launch();const p=await b.newPage();
for(const j of jobs){
  const svg=fs.readFileSync(j.src,'utf8');
  const m=svg.match(/viewBox="([-\d.\s]+)"/); const vb=m[1].trim().split(/\s+/).map(Number);
  const ar=vb[2]/vb[3]; const L=j.long||2400;
  let w=ar>=1?L:Math.round(L*ar), h=ar>=1?Math.round(L/ar):L;
  w=Math.max(w,8); h=Math.max(h,8);
  await p.setViewportSize({width:w,height:h});
  const s2=svg.replace(/<svg([^>]*?)\swidth="[^"]*"/,'<svg$1').replace(/<svg([^>]*?)\sheight="[^"]*"/,'<svg$1').replace('<svg','<svg width="'+w+'" height="'+h+'"');
  await p.setContent('<html><body style="margin:0;background:transparent">'+s2+'</body></html>');
  fs.mkdirSync(path.dirname(j.out),{recursive:true});
  await p.screenshot({path:j.out,omitBackground:true,clip:{x:0,y:0,width:w,height:h}});
}
await b.close();console.log('ok',jobs.length);})();
