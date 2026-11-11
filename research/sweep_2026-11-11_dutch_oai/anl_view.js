// archieven.nl: open an inventory item found by a search term, open its scan viewer and screenshot each page (to a scratch dir, never the repo).
// usage: node anl_view.js <miadt> <micode> <term> <unitid> <outdir> [first=1] [last=all] [step=1]
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const [adt, code, term, uid, out] = process.argv.slice(2); const first = parseInt(process.argv[7] || '1'), last = parseInt(process.argv[8] || '100000'), step = parseInt(process.argv[9] || '1');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1500, height: 1900 } });
  await p.goto(`https://www.archieven.nl/nl/zoeken?mivast=0&mizig=210&miadt=${adt}&miview=inv2&milang=nl&mizk_alle=${encodeURIComponent(term)}&micode=${code}`, { waitUntil: 'networkidle', timeout: 90000 }); await p.waitForTimeout(3000);
  const bt = p.locator('button.mi_btn_toggle').first(); if (await bt.count()) { await bt.click().catch(() => {}); await p.waitForTimeout(5000); }
  const a = p.locator('.mi_inv_searchresults a.mi_hyperlink').filter({ hasText: new RegExp('^\\s*' + uid.replace('.', '\\.') + '\\s') }).first();
  await a.click().catch(e => console.log('item not found')); await p.waitForTimeout(6000);
  await p.locator('img.mi_stripthumb_img').first().click().catch(e => console.log('no thumbs')); await p.waitForTimeout(6000);
  const total = await p.evaluate(() => { const m = document.body.innerText.match(/Bestand\s*\/\s*(\d+)/); return m ? parseInt(m[1]) : 0; }); console.log('pages', total);
  for (let i = first; i <= Math.min(last, total); i += step) {
    if (i > 1) { const inp = p.locator('input').filter({ visible: true }).first(); await inp.fill(String(i)); await inp.press('Enter'); await p.waitForTimeout(1500); await p.waitForLoadState('networkidle').catch(() => {}); await p.waitForTimeout(2500); }
    await p.screenshot({ path: `${out}/p${String(i).padStart(4, '0')}.png`, clip: { x: 70, y: 100, width: 1245, height: 1700 } });
  }
  await b.close();
})();
