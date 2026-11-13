// Previsualiza tarjetas v7 como las vería el reviewer de Anki: anverso y reverso, claro y noche,
// a ancho de iPhone (390 px) y de iPad (820 px). Detecta desbordes horizontales.
// Uso: node kit/anki/previsualizar.js <tarjetas.json> <carpeta_capturas_en_scratchpad> [N]
// No instala nada: usa playwright-core de kit/node_modules (cd kit && npm ci) o un playwright global,
// y el Chromium de PW_CHROMIUM o /opt/pw-browsers/chromium.
const { chromium } = (() => {
  for (const m of [__dirname + '/../node_modules/playwright-core', 'playwright-core', 'playwright',
    '/opt/node22/lib/node_modules/playwright']) { try { return require(m); } catch (e) {} }
  throw new Error('playwright no encontrado (ejecuta: cd kit && npm ci)');
})();
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');

const [json, outDir, n] = process.argv.slice(2);
if (!json || !outDir) { console.error('Uso: node kit/anki/previsualizar.js <tarjetas.json> <carpeta> [N]'); process.exit(2); }
const pagDir = path.join(path.resolve(outDir), '_paginas');
execFileSync('python3', [path.join(__dirname, 'paginas.py'), json, pagDir].concat(n ? [n] : []), { stdio: 'inherit' });
const exe = [process.env.PW_CHROMIUM, '/opt/pw-browsers/chromium'].find(p => p && fs.existsSync(p));
const DISP = { iphone: { width: 390, height: 844 }, ipad: { width: 820, height: 1180 } };

(async () => {
  const b = await chromium.launch(exe ? { executablePath: exe } : {});
  const problemas = [];
  let total = 0;
  for (const [disp, viewport] of Object.entries(DISP)) {
    const ctx = await b.newContext({ viewport, deviceScaleFactor: 2 });
    const p = await ctx.newPage();
    for (const f of fs.readdirSync(pagDir).filter(x => x.endsWith('.html')).sort()) {
      await p.goto('file://' + path.join(pagDir, f));
      const r = await p.evaluate(() => {
        const doc = document.documentElement;
        const tablas = [...document.querySelectorAll('.esq')].filter(e => e.scrollWidth > e.clientWidth + 1).length;
        const imgs = [...document.images].filter(i => !i.complete || i.naturalWidth === 0).length;
        return { desborde: doc.scrollWidth > window.innerWidth + 1, tablas, imgs };
      });
      const nombre = f.replace('.html', `_${disp}.png`);
      if (r.desborde) problemas.push(`${nombre}: desborde horizontal de la página`);
      if (r.tablas) problemas.push(`${nombre}: ${r.tablas} esquema(s) con desplazamiento horizontal (revisa columnas)`);
      if (r.imgs) problemas.push(`${nombre}: ${r.imgs} imagen(es) sin cargar`);
      await p.screenshot({ path: path.join(outDir, nombre), fullPage: true });
      total++;
    }
    await ctx.close();
  }
  await b.close();
  console.log(`${total} capturas en ${path.resolve(outDir)}`);
  problemas.forEach(x => console.log('AVISO: ' + x));
  console.log(problemas.length ? `RESULTADO: ${problemas.length} avisos` : 'RESULTADO: OK');
})();
