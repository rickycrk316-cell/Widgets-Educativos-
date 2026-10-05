// Convierte Informe_Competencia_cute_orito.html en PDF A4 con Chromium (Playwright).
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve(__dirname, 'Informe_Competencia_cute_orito.html'));
  await p.pdf({ path: path.resolve(__dirname, 'Informe_Competencia_cute_orito.pdf'), format: 'A4', printBackground: true });
  await b.close();
})();
