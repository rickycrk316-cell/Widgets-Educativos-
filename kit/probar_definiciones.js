// Pruebas funcionales y visuales del widget de definiciones.
// Uso: node probar_definiciones.js <url> <carpeta_capturas>
const { chromium } = (() => { for (const m of ['playwright', '/opt/node22/lib/node_modules/playwright', '/opt/node22/lib/node_modules/@playwright/cli/node_modules/playwright-core']) { try { return require(m); } catch (e) {} } throw new Error('playwright no encontrado'); })();
const fs = require('fs');
const [url, outDir] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });
const fails = [], notes = [];

async function runDeck(page, sec) {
  // recorre el mazo de la sección visible: Mostrar respuesta → La sabía, hasta el final
  for (let i = 0; i < 400; i++) {
    const st = await page.evaluate(sec => {
      const s = document.getElementById(sec), rc = s.querySelector('.rc');
      if (!rc) return 'sin-rc';
      if (rc.querySelector('.rc-end')) return 'fin';
      const show = [...rc.querySelectorAll('button')].find(b => /mostrar respuesta/i.test(b.textContent) && b.offsetParent);
      if (show) { show.click(); return 'show'; }
      const ok = [...rc.querySelectorAll('button.gr.ok')].find(b => b.offsetParent);
      if (ok) { ok.click(); return 'grade'; }
      return 'atascado';
    }, sec);
    if (st === 'fin') return 'ok';
    if (st === 'sin-rc' || st === 'atascado') return st;
  }
  return 'no termina';
}

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const views = [
    { name: 'ipad', width: 820, height: 1180, scheme: 'light' },
    { name: 'ipad-oscuro', width: 820, height: 1180, scheme: 'dark' },
    { name: 'movil', width: 390, height: 844, scheme: 'light' },
  ];
  for (const v of views) {
    const ctx = await browser.newContext({ viewport: { width: v.width, height: v.height }, colorScheme: v.scheme });
    const page = await ctx.newPage();
    const errs = [];
    page.on('pageerror', e => errs.push(e.message));
    page.on('console', m => { if (m.type() === 'error' && !/favicon/.test((m.location() || {}).url || '')) errs.push(m.text()); });
    await page.goto(url);
    const n = await page.$$eval('nav.tabs button.tb', b => b.length);
    for (let i = 0; i < n; i++) {
      await page.evaluate(i => document.querySelectorAll('nav.tabs button.tb')[i].click(), i);
      await page.waitForTimeout(120);
      const sec = await page.evaluate(() => (document.querySelector('section.tab.active') || {}).id);
      if (!sec) { fails.push(`${v.name}: el botón ${i + 1} no activa ninguna sección`); continue; }
      const ov = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      if (ov > 1) fails.push(`${v.name}/${sec}: desborde horizontal de ${ov}px`);
      if (i === 0 || i === n - 1) await page.screenshot({ path: `${outDir}/${v.name}_${i === 0 ? 'primera' : 'repaso'}.png` });
      if (v.name === 'ipad') {
        const r = await runDeck(page, sec);
        if (r !== 'ok') fails.push(`recall ${sec}: ${r}`);
        else {
          const end = await page.evaluate(sec => document.querySelector('#' + sec + ' .rc-end').textContent.trim().slice(0, 80), sec);
          notes.push(`recall ${sec}: completo · «${end}»`);
        }
      }
    }
    if (v.name === 'ipad') {
      const acc = await page.evaluate(() => { const a = document.querySelector('.acc:not(.op) .acc-h'); if (!a) return 'n/a'; a.click(); return a.closest('.acc').classList.contains('op') ? 'ok' : 'no abre'; });
      if (acc !== 'ok' && acc !== 'n/a') fails.push('acordeón: ' + acc);
      const tbl = await page.evaluate(() => { const s = [...document.querySelectorAll('section.tab')].pop(); return !!s.querySelector('table'); });
      notes.push(`tabla resumen del repaso global: ${tbl ? 'presente' : 'ausente'}`);
      if (!tbl) fails.push('repaso global: no aparece la tabla resumen al terminar');
    }
    if (errs.length) fails.push(`${v.name}: errores de consola: ${[...new Set(errs)].slice(0, 3).join(' | ')}`);
    await ctx.close();
  }
  await browser.close();
  fails.forEach(f => console.log('FALLA ' + f)); notes.forEach(x => console.log('NOTA ' + x));
  console.log(`NAVEGADOR DEFINICIONES: ${fails.length ? 'FALLA' : 'OK'} · fallas ${fails.length}`);
  process.exit(fails.length ? 1 : 0);
})().catch(e => { console.log('FALLA prueba: ' + e.message); process.exit(1); });
