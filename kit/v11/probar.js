// Pruebas funcionales y visuales del widget v11 en Chromium (Playwright).
// Uso: node kit/v11/probar.js <url> <carpeta_capturas>
// Resolución de playwright: kit/node_modules (cd kit && npm ci) primero; si no, global.
const path = require('path');
const { chromium } = (() => { for (const m of [path.join(__dirname, '..', 'node_modules', 'playwright-core'), 'playwright-core', 'playwright', '/opt/node22/lib/node_modules/playwright', '/opt/node22/lib/node_modules/@playwright/cli/node_modules/playwright-core']) { try { return require(m); } catch (e) {} } throw new Error('playwright no encontrado (ejecuta: cd kit && npm ci)'); })();
const fs = require('fs');
const [url, outDir] = process.argv.slice(2);
if (!url || !outDir) { console.log('Uso: node kit/v11/probar.js <url> <carpeta_capturas>'); process.exit(2); }
fs.mkdirSync(outDir, { recursive: true });
const fails = [], notes = [];
const exe = [process.env.PW_CHROMIUM, '/opt/pw-browsers/chromium'].find(p => p && fs.existsSync(p));
const pausa = (page, ms) => page.evaluate(ms => new Promise(r => setTimeout(r, ms)), ms);

// visible = ocupa caja, no display:none ni visibility:hidden
const VIS = `(e => { if (!e) return false; const s = getComputedStyle(e), r = e.getBoundingClientRect(); return s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0 && r.height > 0; })`;

(async () => {
  const browser = await chromium.launch(exe ? { executablePath: exe } : {});
  const views = [
    { name: 'movil', width: 390, height: 844, scheme: 'light' },
    { name: 'movil-oscuro', width: 390, height: 844, scheme: 'dark' },
    { name: 'ipad', width: 820, height: 1180, scheme: 'light' },
    { name: 'ipad-horizontal', width: 1180, height: 820, scheme: 'dark' },
    { name: 'mac', width: 1440, height: 900, scheme: 'light' },
  ];
  for (const v of views) {
    const ctx = await browser.newContext({ viewport: { width: v.width, height: v.height }, colorScheme: v.scheme, deviceScaleFactor: 1 });
    const page = await ctx.newPage();
    const errs = [];
    page.on('pageerror', e => errs.push(e.message));
    page.on('console', m => { if (m.type() === 'error' && !/favicon/.test((m.location() || {}).url || '')) errs.push(m.text()); });
    await page.goto(url);
    await pausa(page, 200);
    const tabs = await page.locator('button.tb').evaluateAll(bs => bs.map(b => b.dataset.tab));
    const movil = v.width < 760;

    // navegación adaptable
    const nv = await page.evaluate(`(() => { const vis = ${VIS}; return { bottom: vis(document.querySelector('nav.bottom')), side: vis(document.querySelector('nav.side')), hasB: !!document.querySelector('nav.bottom'), hasS: !!document.querySelector('nav.side'), filtro: !!document.querySelector('.perla-filtro') }; })()`);
    if (!nv.hasB || !nv.hasS) fails.push(`${v.name}: falta nav.${!nv.hasB ? 'bottom' : 'side'} (la genera el script desde nav.tabs)`);
    else if (movil && (!nv.bottom || nv.side)) fails.push(`${v.name}: <760 px debe verse nav.bottom (${nv.bottom}) y no nav.side (${nv.side})`);
    else if (!movil && (nv.bottom || !nv.side)) fails.push(`${v.name}: ≥760 px debe verse nav.side (${nv.side}) y no nav.bottom (${nv.bottom})`);
    if (!nv.filtro) fails.push(`${v.name}: falta .perla-filtro`);

    for (const k of tabs) {
      await page.evaluate(k => show(k), k);
      await pausa(page, 120);
      const ov = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      if (ov > 1) fails.push(`${v.name}/${k}: desborde horizontal de ${ov}px`);
      const bad = await page.evaluate(() => [...document.querySelectorAll('section.tab.on *')].filter(e => {
        const r = e.getBoundingClientRect(); return r.width > 0 && r.right > document.documentElement.clientWidth + 1 && !e.closest('.tw') && !e.closest('nav');
      }).slice(0, 3).map(e => e.tagName + '.' + e.className));
      if (bad.length) fails.push(`${v.name}/${k}: elementos fuera del ancho ${bad.join(', ')}`);
      if (k === 'pan' || k === tabs[1] || /^(e1|def|vis)$/.test(k)) await page.screenshot({ path: `${outDir}/${v.name}_${k}.png` });
    }

    if (v.name === 'ipad') {
      // simuladores: cada .dc produce salida (y cambia al usar controles)
      const n = await page.locator('.dc').count();
      for (let i = 0; i < n; i++) {
        const r = await page.evaluate(async i => {
          const dc = document.querySelectorAll('.dc')[i];
          show(dc.closest('section.tab').dataset.tab);
          const before = dc.querySelector('.out').textContent;
          const inp = dc.querySelector('input[type=number]');
          if (inp) { inp.value = '3'; inp.dispatchEvent(new Event('input', { bubbles: true })); }
          const chips = [...dc.querySelectorAll('.chip')];
          [...new Set(chips.map(c => c.dataset.g))].forEach(g => { const c = chips.find(c => c.dataset.g === g); if (c) c.click(); });
          const after = dc.querySelector('.out').textContent;
          return { fn: dc.dataset.fn, changed: before !== after, empty: !after.trim(), err: /Error de cálculo/.test(after), cf: !!dc.querySelector('.out .cf') };
        }, i);
        if (r.empty) fails.push(`simulador ${r.fn}: sin salida`);
        else if (!r.changed) fails.push(`simulador ${r.fn}: la salida no cambia al usar los controles`);
        if (r.err) fails.push(`simulador ${r.fn}: error de cálculo`);
        if (r.changed && !r.cf) notes.push(`simulador ${r.fn}: sin contrafactual con los primeros controles`);
      }
      notes.push(`simuladores probados: ${n}`);
      // enlaces nodo ↔ signo
      const x = await page.evaluate(() => {
        const xs = [...document.querySelectorAll('.xref')]; let broken = 0;
        xs.forEach(b => { b.click(); const t = document.getElementById(b.dataset.ir); if (!t || !t.closest('section.tab.on')) broken++; });
        return { total: xs.length, broken };
      });
      if (x.broken) fails.push(`enlaces: ${x.broken} de ${x.total} xref no muestran su destino`);
      notes.push(`enlaces probados: ${x.total}`);
    }

    if (v.name === 'ipad' || v.name === 'movil') {
      // filtro de perlas: oculta y muestra
      const f = await page.evaluate(() => {
        const norm = s => (s || '').toLowerCase().replace(/[^a-z0-9]/g, '');
        const btns = [...document.querySelectorAll('.perla-filtro button')];
        const codeOf = b => { const c = norm(b.dataset.ex || b.dataset.f || b.dataset.filtro || b.textContent); return /^(puce|caces|usmle1|usmle2|mir|enarm)$/.test(c) ? c : null; };
        const todos = btns.find(b => !codeOf(b));
        const sec = [...document.querySelectorAll('section.tab')].find(s => s.querySelectorAll('aside.perla').length >= 1 && [...s.querySelectorAll('aside.perla')].some(a => (a.dataset.ex || '').trim()));
        if (!btns.length || !sec) return { skip: !sec ? 'sin perlas' : 'sin botones de filtro' };
        show(sec.dataset.tab);
        const vis = e => { const st = getComputedStyle(e), r = e.getBoundingClientRect(); return st.display !== 'none' && st.visibility !== 'hidden' && r.width > 0 && r.height > 0; };
        const ps = [...sec.querySelectorAll('aside.perla')];
        let res = null;
        for (const b of btns.filter(codeOf)) {
          const c = codeOf(b), want = ps.filter(a => (a.dataset.ex || '').split(/\s+/).includes(c)).length;
          if (want === ps.length && btns.filter(codeOf).indexOf(b) < btns.filter(codeOf).length - 1) continue;
          b.click();
          const got = ps.filter(vis).length;
          if (todos) todos.click();
          const all = ps.filter(vis).length;
          res = { code: c, want, got, all, total: ps.length }; break;
        }
        return res || { skip: 'ningún código aplicable' };
      });
      if (f.skip) notes.push(`${v.name}: filtro de perlas no probado (${f.skip})`);
      else {
        if (f.got !== f.want) fails.push(`${v.name}: filtro «${f.code}» deja ${f.got} perlas visibles (esperadas ${f.want})`);
        if (f.all !== f.total) fails.push(`${v.name}: «Todos» no restaura las perlas (${f.all}/${f.total})`);
        if (f.want === f.total) notes.push(`${v.name}: filtro «${f.code}» no discrimina en la pestaña probada`);
      }
    }

    if (v.name === 'ipad' || v.name === 'movil' || v.name === 'mac') {
      // ejercicio Ordenar
      const cnt = await page.evaluate(() => [...document.querySelectorAll('button')].filter(b => b.textContent.trim() === 'Ordenar').length);
      if (!cnt) fails.push(`${v.name}: sin botón «Ordenar» en ningún bloque`);
      let ok = 0;
      for (let i = 0; i < cnt; i++) {
        // localizar el bloque (ol.tl / ol.steps.tg) asociado y activar
        const info = await page.evaluate(i => {
          const b = [...document.querySelectorAll('button')].filter(b => b.textContent.trim() === 'Ordenar')[i];
          const sec = b.closest('section.tab'); show(sec.dataset.tab);
          let blk = null, n = b;
          while (n && !blk) { if (n.matches && n.matches('ol.tl,ol.steps.tg')) blk = n; else blk = n.querySelector && n.querySelector('ol.tl,ol.steps.tg'); if (!blk) n = n.nextElementSibling || (n.parentElement && n.parentElement !== sec ? n.parentElement.nextElementSibling : null); }
          if (!blk) return { err: 'bloque asociado no encontrado' };
          const exp = [...blk.children].map(li => (li.dataset.paso || '').trim());
          b.scrollIntoView({ block: 'center' });
          return { exp, kind: blk.className };
        }, i);
        if (info.err) { fails.push(`${v.name}/Ordenar #${i + 1}: ${info.err}`); continue; }
        const btn = page.locator('button', { hasText: /^Ordenar$/ }).nth(i);
        await btn.click(); await pausa(page, 250);
        const st = await page.evaluate(() => { const o = document.querySelector('.ord'); return o ? { chips: o.querySelectorAll('.ord-bank .ord-chip').length, slots: o.querySelectorAll('.ord-slots .ord-slot').length, vis: !!(o.getBoundingClientRect().height) } : null; });
        const tag = `${v.name}/Ordenar #${i + 1} (${info.kind})`;
        if (!st || !st.vis) { fails.push(`${tag}: no aparece .ord al activar`); continue; }
        if (st.chips !== info.exp.length || st.slots !== info.exp.length) { fails.push(`${tag}: ${st.chips} frases y ${st.slots} huecos (esperados ${info.exp.length})`); continue; }
        // colocar tocando: frase → hueco
        for (let j = 0; j < info.exp.length; j++) {
          await page.locator('.ord .ord-bank .ord-chip').first().click();
          await page.locator('.ord .ord-slots .ord-slot:not(:has(.ord-chip))').first().click();
        }
        const left = await page.locator('.ord .ord-bank .ord-chip').count();
        if (left) { fails.push(`${tag}: quedan ${left} frases sin colocar tras tocar frase→hueco`); continue; }
        const lenAntes = await page.evaluate(() => document.querySelector('.ord').parentElement.innerText.length);
        if (i === 0 && v.name !== 'mac') await page.screenshot({ path: `${outDir}/${v.name}_ordenar_colocado.png` });
        await page.locator('button', { hasText: /^Revisar$/ }).first().click();
        await pausa(page, 1800);
        const res = await page.evaluate(() => {
          const o = document.querySelector('.ord'); const slots = [...o.querySelectorAll('.ord-slots .ord-slot')];
          return { got: slots.map(s => (s.querySelector('.ord-chip') || s).textContent.replace(/^\s*\d+[.)]?\s*/, '').trim()), ok: o.querySelectorAll('.ord-ok').length, ko: o.querySelectorAll('.ord-ko').length,
            len: o.parentElement.innerText.length, reiniciar: [...document.querySelectorAll('button')].some(b => b.textContent.trim() === 'Reiniciar'), salir: [...document.querySelectorAll('button')].some(b => b.textContent.trim() === 'Salir') };
        });
        const norm = s => s.replace(/\s+/g, ' ').trim();
        const bien = res.got.length === info.exp.length && res.got.every((g, j) => norm(g).includes(norm(info.exp[j])) || norm(info.exp[j]).includes(norm(g)));
        if (!bien) fails.push(`${tag}: tras Revisar el orden mostrado no es el correcto (${res.got.map(g => g.slice(0, 18)).join(' | ')})`);
        else ok++;
        if (res.ok + res.ko < 1) fails.push(`${tag}: Revisar no marca aciertos/errores (.ord-ok/.ord-ko)`);
        if (res.len <= lenAntes + 40) fails.push(`${tag}: Revisar no despliega la explicación (texto ${lenAntes}→${res.len})`);
        if (!res.reiniciar || !res.salir) fails.push(`${tag}: faltan botones «Reiniciar»/«Salir» tras revisar`);
        if (i === 0 && v.name !== 'mac') { await page.locator('.ord').first().scrollIntoViewIfNeeded(); await page.screenshot({ path: `${outDir}/${v.name}_ordenar_revisado.png` }); }
        // reiniciar vuelve a barajar; salir cierra
        await page.locator('button', { hasText: /^Reiniciar$/ }).first().click(); await pausa(page, 250);
        const r2 = await page.evaluate(() => document.querySelectorAll('.ord .ord-bank .ord-chip').length);
        if (r2 !== info.exp.length) fails.push(`${tag}: «Reiniciar» no devuelve las ${info.exp.length} frases (hay ${r2})`);
        await page.locator('button', { hasText: /^Salir$/ }).first().click(); await pausa(page, 250);
        const cerrado = await page.evaluate(`!document.querySelector('.ord') || !${VIS}(document.querySelector('.ord'))`);
        if (!cerrado) fails.push(`${tag}: «Salir» no cierra el ejercicio`);
      }
      if (cnt) notes.push(`${v.name}: Ordenar correcto en ${ok}/${cnt} bloques`);
    }
    if (errs.length) fails.push(`${v.name}: errores de consola: ${[...new Set(errs)].slice(0, 3).join(' | ')}`);
    await ctx.close();
  }
  // vista 820 también a 1180 en claro/oscuro ya cubierta; 820 oscuro solo desborde
  const c2 = await browser.newContext({ viewport: { width: 820, height: 1180 }, colorScheme: 'dark' }); const p2 = await c2.newPage(); await p2.goto(url);
  for (const k of await p2.locator('button.tb').evaluateAll(bs => bs.map(b => b.dataset.tab))) { await p2.evaluate(k => show(k), k); const ov = await p2.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth); if (ov > 1) fails.push(`ipad-oscuro/${k}: desborde horizontal de ${ov}px`); }
  await p2.screenshot({ path: `${outDir}/ipad-oscuro.png` }); await c2.close();
  await browser.close();
  fails.forEach(f => console.log('FALLA ' + f)); notes.forEach(n => console.log('NOTA ' + n));
  console.log(`NAVEGADOR v11: ${fails.length ? 'FALLA' : 'OK'} · fallas ${fails.length}`);
  process.exit(fails.length ? 1 : 0);
})().catch(e => { console.log('FALLA prueba: ' + e.message); process.exit(1); });
