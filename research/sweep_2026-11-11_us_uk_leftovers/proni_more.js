// PRONI eCatalogue, full descriptions: node proni_more.js <outdir> <term> [skipRefsFile]
// Runs the word search (all words, page size max), then opens every row's "More" page and appends
// {ref, text} to <outdir>/<term>_full.jsonl. Rows whose reference is already in the jsonl are skipped.
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const out = process.argv[2]; const t = process.argv[3];
  const f = `${out}/${t.replace(/\W+/g, '_')}_full.jsonl`;
  const have = new Set(fs.existsSync(f) ? fs.readFileSync(f, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l).ref) : []);
  const skip = new Set(process.argv[4] ? fs.readFileSync(process.argv[4], 'utf8').split('\n') : []);
  const b = await chromium.launch(); const p = await b.newPage();
  async function search() {
    await p.goto('https://apps.proni.gov.uk/eCatNI_IE/SearchPage.aspx', { timeout: 60000 });
    await p.fill('#ContentPlaceHolder1_txtWords', t);
    const opts = await p.$$eval('#ContentPlaceHolder1_ddPageSize option', o => o.map(x => x.value));
    await p.selectOption('#ContentPlaceHolder1_ddPageSize', opts[opts.length - 1]).catch(() => {});
    await Promise.all([p.waitForLoadState('load'), p.click('#ContentPlaceHolder1_SearchArchiveBtn')]);
    await p.waitForTimeout(2500);
  }
  await search();
  const refs = await p.$$eval('table tr', rs => rs.map(r => r.cells && r.cells.length > 2 ? r.cells[0].innerText.trim() : '').filter(x => x && x !== 'PRONI Reference'));
  console.log(t, refs.length, 'rows');
  for (let i = 0; i < refs.length; i++) {
    if (have.has(refs[i]) || skip.has(refs[i]) || /^D4686/.test(refs[i])) continue;
    try {
      const btn = await p.$(`#ContentPlaceHolder1_GridView1_btnItemView_${i}`);
      if (!btn) { fs.appendFileSync(f, JSON.stringify({ ref: refs[i], text: '(no More button)' }) + '\n'); continue; }
      await Promise.all([p.waitForLoadState('load'), btn.click()]);
      await p.waitForTimeout(2500);
      const txt = await p.evaluate(() => document.body.innerText);
      fs.appendFileSync(f, JSON.stringify({ ref: refs[i], text: txt }) + '\n');
      await search();
    } catch (e) { console.log('ERR', refs[i], String(e).slice(0, 100)); await search(); }
  }
  await b.close();
})();
