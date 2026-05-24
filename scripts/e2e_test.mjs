import { chromium } from '/home/stev/.nvm/versions/node/v22.21.1/lib/node_modules/@playwright/mcp/node_modules/playwright/index.mjs';

const BASE = process.env.E2E_BASE || 'http://127.0.0.1:8765';
const routes = [
  '/', '/index.html', '/tesis', '/casos', '/casos/01_caso_clima',
  '/casos/04_caso_energia', '/casos/16_caso_deforestacion',
  '/casos/19_caso_acidificacion_oceanica', '/casos/24_caso_microplasticos',
  '/casos/26_caso_starlink', '/capitulos', '/capitulos/06-cierre',
  '/bibliografia', '/st'
];

const browser = await chromium.launch();
const context = await browser.newContext();
const results = [];

for (const route of routes) {
  const page = await context.newPage();
  const consoleErrors = [];
  const pageErrors = [];
  page.on('pageerror', err => pageErrors.push(err.message));
  page.on('console', msg => {
    if (msg.type() === 'error') consoleErrors.push(msg.text());
  });

  let title = '', body = '', status = 0, gotoErr = null;
  try {
    const resp = await page.goto(BASE + route, { waitUntil: 'networkidle', timeout: 15000 });
    status = resp ? resp.status() : 0;
    // small wait for React render
    await page.waitForTimeout(500);
    title = await page.title();
    body = await page.locator('body').innerText().catch(() => '');
  } catch (e) {
    gotoErr = e.message;
  }

  const isNotFound = /Sección no encontrada|Caso no encontrado|Capítulo no encontrado|404|Not Found/i.test(body);
  const snippet = body.replace(/\s+/g, ' ').slice(0, 160);

  results.push({ route, status, title, isNotFound, snippet, pageErrors, consoleErrors, gotoErr });
  console.log(`[${status}] ${route.padEnd(45)} NF:${isNotFound ? 'YES' : 'no '} | ${snippet.slice(0, 90)}`);
  if (pageErrors.length) console.log(`   pageErrors: ${pageErrors.join(' || ')}`);
  if (consoleErrors.length) console.log(`   consoleErrors(${consoleErrors.length}): ${consoleErrors.slice(0,2).join(' || ')}`);

  await page.close();
}

await browser.close();

console.log('\n========== SUMMARY ==========');
const broken = results.filter(r => r.isNotFound || r.status >= 400 || r.gotoErr);
console.log(`Total routes: ${results.length}`);
console.log(`Broken (NotFound/4xx/error): ${broken.length}`);
for (const b of broken) {
  console.log(` - ${b.route} | status=${b.status} | NF=${b.isNotFound} | err=${b.gotoErr || '-'}`);
  console.log(`     body: "${b.snippet}"`);
}
console.log('\n========== FULL JSON ==========');
console.log(JSON.stringify(results, null, 2));
