// PRONI eCatalogue through headless Chromium: node proni_pw.js <outdir> <term> [more terms]
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const out = process.argv[2]; const terms = process.argv.slice(3);
  const b = await chromium.launch(); const p = await b.newPage();
  for (const t of terms) {
    await p.goto('https://apps.proni.gov.uk/eCatNI_IE/SearchPage.aspx', { timeout: 60000 });
    const cb = await p.$('#chkboxTerms'); if (cb) await cb.check().catch(() => {});
    await p.fill('#ContentPlaceHolder1_txtWords', t);
    await p.check('#ContentPlaceHolder1_radWordMatch_2').catch(() => {});
    const opts = await p.$$eval('#ContentPlaceHolder1_ddPageSize option', o => o.map(x => x.value));
    await p.selectOption('#ContentPlaceHolder1_ddPageSize', opts[opts.length - 1]).catch(() => {});
    await Promise.all([p.waitForLoadState('load'), p.click('#ContentPlaceHolder1_SearchArchiveBtn')]);
    await p.waitForTimeout(4000);
    const txt = await p.evaluate(() => document.body.innerText);
    fs.writeFileSync(`${out}/${t.replace(/\W+/g, '_')}.txt`, txt);
    fs.writeFileSync(`${out}/${t.replace(/\W+/g, '_')}.html`, await p.content());
    console.log(t, p.url(), txt.length, (txt.match(/Request Rejected|\d+ (records|results)[^\n]*/) || [''])[0]);
    await p.waitForTimeout(3000);
  }
  await b.close();
})();
