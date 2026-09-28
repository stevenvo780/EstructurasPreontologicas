import { chromium } from '/home/stev/.nvm/versions/node/v22.21.1/lib/node_modules/@playwright/mcp/node_modules/playwright/index.mjs';
const BASE = 'https://estructuras-preontologicas.vercel.app';
const routes = ['/index.html', '/casos/', '/capitulos/', '/tesis/', '/bibliografia/', '/st/', '/ruta-inexistente-xyz', '/'];
const browser = await chromium.launch();
const page = await browser.newPage();
for (const r of routes) {
  await page.goto(BASE + r, { waitUntil: 'networkidle' });
  await page.waitForTimeout(500); // allow redirects
  const url = page.url();
  // Get main content excluding nav/header
  const mainText = await page.locator('main').first().innerText().catch(() => '');
  const h1 = await page.locator('h1, h2').first().innerText().catch(() => '(no h1)');
  const isNF = /no encontrad|404/i.test(mainText) || /no encontrad|404/i.test(h1);
  console.log(`${r.padEnd(28)} | final: ${url.replace(BASE,'').padEnd(28)} | NF:${isNF ? 'YES' : 'no '} | h1: "${h1.slice(0, 60)}"`);
}
await browser.close();
