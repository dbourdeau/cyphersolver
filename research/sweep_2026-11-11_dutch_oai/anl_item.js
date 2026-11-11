const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const [base, adt, code, term, uid] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage();
  const r0 = await p.goto(`${base}?mivast=${base.includes('archieven.nl') ? 0 : adt}&mizig=210&miadt=${adt}&miview=inv2&milang=nl&mizk_alle=${encodeURIComponent(term)}&micode=${code}`, { waitUntil: 'networkidle', timeout: 90000 }); console.log('status', r0.status()); await p.waitForTimeout(3000);
  const bt = p.locator('button.mi_btn_toggle').first(); if (await bt.count()) { await bt.click().catch(() => {}); await p.waitForTimeout(5000); }
  const h = await p.evaluate(() => { const e = document.querySelector('.mi_inv_searchresults'); return e ? e.outerHTML : 'NONE ' + document.body.innerText.slice(0, 500); });
  fs.writeFileSync('det.html', h); console.log(h.length);
  const a = p.locator('.mi_inv_searchresults a.mi_hyperlink').filter({ hasText: new RegExp('^\\s*' + uid.replace('.', '\\.') + '\\s') }).first();
  console.log('found', await a.count()); await a.click().catch(e => console.log('clickerr')); await p.waitForTimeout(6000);
  const h2 = await p.evaluate(() => { const e = document.querySelector('.mi_inv_searchresults'); return e ? e.outerHTML : ''; }); fs.writeFileSync('det2.html', h2);
  console.log(await p.evaluate(() => { const e = document.querySelector('.mi_inv_searchresults'); return e ? e.innerText.replace(/\n\s*\n/g, '\n').slice(0, 2500) : ''; }));
  await b.close();
})();
