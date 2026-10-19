// Pruebas funcionales y visuales del orquestador sobre un widget v10.
// Uso: node probar_navegador.js <url> <carpeta_capturas>
// Resolución: kit/node_modules (npm ci) primero; si no, playwright global.
const { chromium } = (() => { for (const m of ['playwright-core', 'playwright', '/opt/node22/lib/node_modules/playwright', '/opt/node22/lib/node_modules/@playwright/cli/node_modules/playwright-core']) { try { return require(m); } catch (e) {} } throw new Error('playwright no encontrado (ejecuta: cd kit && npm ci)'); })();
const fs = require('fs');
const [url, outDir] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });
const fails = [], notes = [];
// Chromium: env PW_CHROMIUM > /opt/pw-browsers/chromium > el de playwright.
const exe = [process.env.PW_CHROMIUM, '/opt/pw-browsers/chromium'].find(p => p && fs.existsSync(p));

const pausa = (page, ms) => page.evaluate(ms => new Promise(r => setTimeout(r, ms)), ms);

(async () => {
  const browser = await chromium.launch(exe ? { executablePath: exe } : {});
  const views = [
    { name: 'ipad', width: 820, height: 1180, scheme: 'light' },
    { name: 'ipad-oscuro', width: 820, height: 1180, scheme: 'dark' },
    { name: 'movil', width: 390, height: 844, scheme: 'light' },
    { name: 'movil-oscuro', width: 390, height: 844, scheme: 'dark' },
  ];
  for (const v of views) {
    const ctx = await browser.newContext({ viewport: { width: v.width, height: v.height }, colorScheme: v.scheme, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    const errs = [];
    page.on('pageerror', e => errs.push(e.message));
    page.on('console', m => { if (m.type() === 'error' && !/favicon/.test((m.location() || {}).url || '')) errs.push(m.text()); });
    await page.goto(url);
    const tabs = await page.locator('button.tb').evaluateAll(bs => bs.map(b => b.dataset.tab));
    for (const k of tabs) {
      await page.evaluate(k => show(k), k);
      const ov = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      if (ov > 1) fails.push(`${v.name}/${k}: desborde horizontal de ${ov}px`);
      const bad = await page.evaluate(() => [...document.querySelectorAll('section.tab.on *')].filter(e => {
        const r = e.getBoundingClientRect(); return r.width > 0 && r.right > document.documentElement.clientWidth + 1 && !e.closest('.tw') && !e.closest('nav');
      }).slice(0, 3).map(e => e.tagName + '.' + e.className));
      if (bad.length) fails.push(`${v.name}/${k}: elementos fuera del ancho ${bad.join(', ')}`);
      if (k === 'pan' || /^(e1|def|vis)$/.test(k)) await pausa(page, 300), await page.screenshot({ path: `${outDir}/${v.name}_${k}.png` });
    }
    if (v.name === 'ipad') {
      // simuladores: cada .dc reacciona a su primer control
      const n = await page.locator('.dc').count();
      for (let i = 0; i < n; i++) {
        const r = await page.evaluate(async i => {
          const dc = document.querySelectorAll('.dc')[i];
          show(dc.closest('section.tab').dataset.tab);
          const before = dc.querySelector('.out').textContent;
          const inp = dc.querySelector('input[type=number]');
          if (inp) { inp.value = '3'; inp.dispatchEvent(new Event('input', { bubbles: true })); }
          const chips = [...dc.querySelectorAll('.chip')];
          const groups = [...new Set(chips.map(c => c.dataset.g))];
          groups.forEach(g => { const c = chips.find(c => c.dataset.g === g); if (c) c.click(); });
          const after = dc.querySelector('.out').textContent;
          return { fn: dc.dataset.fn, changed: before !== after, err: /Error de cálculo/.test(after), cf: !!dc.querySelector('.out .cf') };
        }, i);
        if (!r.changed) fails.push(`simulador ${r.fn}: la salida no cambia al usar los controles`);
        if (r.err) fails.push(`simulador ${r.fn}: error de cálculo`);
        if (r.changed && !r.cf) notes.push(`simulador ${r.fn}: sin contrafactual con los primeros controles`);
      }
      // enlaces nodo ↔ signo
      const x = await page.evaluate(() => {
        const xs = [...document.querySelectorAll('.xref')]; let broken = 0;
        xs.forEach(b => { b.click(); const t = document.getElementById(b.dataset.ir); if (!t || !t.closest('section.tab.on')) broken++; });
        return { total: xs.length, broken };
      });
      if (x.broken) fails.push(`enlaces: ${x.broken} de ${x.total} xref no muestran su destino`);
      notes.push(`enlaces probados: ${x.total}`);
      // timeline en blanco y tabla en blanco
      const rc = await page.evaluate(() => {
        const s = [...document.querySelectorAll('section.tab')].find(s => s.querySelector('ol.tl'));
        if (!s) return 'sin timeline';
        show(s.dataset.tab); recon(s.dataset.tab, true);
        const hidden = [...s.querySelectorAll('.nodo .det')].every(d => getComputedStyle(d).display === 'none');
        recon(s.dataset.tab, false); return hidden ? 'ok' : 'detalles visibles en reconstrucción';
      });
      if (rc !== 'ok') fails.push('reconstrucción: ' + rc);
      const tb = await page.evaluate(() => { if (!document.querySelector('table.vis')) return 'n/a'; show(document.querySelector('table.vis').closest('section').dataset.tab); tabla(true); const c = document.querySelector('td.tap'); const t = getComputedStyle(c).color; tabla(false); return t; });
      notes.push(`tabla en blanco: ${tb === 'n/a' ? 'no aplica (mono)' : 'tapa celdas'}`);
      // contraste del cuerpo
      const contrast = await page.evaluate(() => {
        const lum = c => { const [r, g, b] = c.match(/\d+/g).slice(0, 3).map(n => { n /= 255; return n <= .03928 ? n / 12.92 : ((n + .055) / 1.055) ** 2.4 }); return .2126 * r + .7152 * g + .0722 * b; };
        const fg = getComputedStyle(document.body).color, bg = getComputedStyle(document.body).backgroundColor;
        const a = lum(fg), b = lum(bg); return ((Math.max(a, b) + .05) / (Math.min(a, b) + .05)).toFixed(1);
      });
      notes.push(`contraste texto/fondo: ${contrast}:1`);
    }
    if (v.name === 'ipad' || v.name === 'ipad-oscuro') {
      // capturas de componentes que el primer viewport no muestra
      for (const sel of ['.signo', '.fey', '.hb.vi', '.hb.ro', '.qv', 'ol.steps.tg', '.dc']) {
        const hay = await page.evaluate(s => { const e = document.querySelector(s); if (e) { show(e.closest('section.tab').dataset.tab); e.scrollIntoView({ block: 'center' }); } return !!e; }, sel);
        if (hay) { await pausa(page, 250); await page.locator(sel).first().screenshot({ path: `${outDir}/${v.name}_comp_${sel.replace(/[^a-z]/g, '')}.png` }); }
      }
      await page.evaluate(() => { const s = [...document.querySelectorAll('section.tab')].find(s => s.querySelector('ol.tl')); show(s.dataset.tab); recon(s.dataset.tab, true); document.getElementById('rec-bar-' + s.dataset.tab).scrollIntoView({ block: 'start' }); });
      await pausa(page, 250); await page.screenshot({ path: `${outDir}/${v.name}_recon.png` });
      await page.evaluate(() => { document.querySelectorAll('section.recon').forEach(s => recon(s.dataset.tab, false)); });
      if (await page.evaluate(() => !!document.querySelector('table.vis'))) {
        await page.evaluate(() => { const t = document.querySelector('table.vis'); show(t.closest('section').dataset.tab); tabla(true); document.getElementById('vb-bar').scrollIntoView({ block: 'start' }); const c = document.querySelectorAll('td.tap'); if (c[1]) c[1].click(); });
        await pausa(page, 250); await page.screenshot({ path: `${outDir}/${v.name}_tabla.png` }); await page.evaluate(() => tabla(false));
      }
    }
    if (errs.length) fails.push(`${v.name}: errores de consola: ${[...new Set(errs)].slice(0, 3).join(' | ')}`);
    await ctx.close();
  }
  await browser.close();
  fails.forEach(f => console.log('FALLA ' + f)); notes.forEach(n => console.log('NOTA ' + n));
  console.log(`NAVEGADOR: ${fails.length ? 'FALLA' : 'OK'} · fallas ${fails.length}`);
  process.exit(fails.length ? 1 : 0);
})().catch(e => { console.log('FALLA prueba: ' + e.message); process.exit(1); });
