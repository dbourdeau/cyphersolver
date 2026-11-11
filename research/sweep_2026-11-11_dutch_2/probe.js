// log the network requests the archieven.nl scan viewer makes (to find direct image URLs)
const { chromium } = require('playwright');
(async () => {
  const [adt, code, term, uid] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1500, height: 1900 } });
  let on = false; p.on('response', async r => { if (on && /prox\.ashx|\.jpg\?h=/.test(r.url())) { const t = await r.text().catch(()=>''); require('fs').writeFileSync(process.env.OUT + '/' + (r.url().includes('prox.ashx') ? 'prox.json' : 'embed.html'), t); } if (on && process.env.VERB) { const h = r.headers(); console.log(r.status(), h['content-type'], h['content-length'], r.url().slice(0, 400)); } });
  await p.goto(`https://www.archieven.nl/nl/zoeken?mivast=0&mizig=210&miadt=${adt}&miview=inv2&milang=nl&mizk_alle=${encodeURIComponent(term)}&micode=${code}`, { waitUntil: 'networkidle', timeout: 90000 }); await p.waitForTimeout(3000);
  const bt = p.locator('button.mi_btn_toggle').first(); if (await bt.count()) { await bt.click().catch(() => {}); await p.waitForTimeout(5000); }
  const a = p.locator('.mi_inv_searchresults a.mi_hyperlink').filter({ hasText: new RegExp('^\\s*' + uid.replace('.', '\\.') + '\\s') }).first();
  await a.click().catch(e => console.log('item not found')); await p.waitForTimeout(6000);
  on = true;
  await p.locator('img.mi_stripthumb_img').first().click().catch(e => console.log('no thumbs')); await p.waitForTimeout(8000);
  for (const f of p.frames()) console.log('FRAME', f.url().slice(0, 500));
  await b.close();
})();
