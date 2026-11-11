// archieven.nl: expand "Bekijk gevonden archiefstukken" for inventory+term pairs and keep the whole found-items text.
// usage: node anl_exp.js out.jsonl < lines "adt<TAB>code<TAB>term"   (resumes: skips pairs already in out)
const { chromium } = require('playwright'); const fs = require('fs');
const out = process.argv[2]; const done = new Set(fs.existsSync(out) ? fs.readFileSync(out, 'utf8').split('\n').filter(Boolean).map(l => { const d = JSON.parse(l); return d.adt + '|' + d.code + '|' + d.term; }) : []);
const jobs = fs.readFileSync(0, 'utf8').split('\n').filter(Boolean).map(l => l.split('\t'));
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [adt, code, term] of jobs) {
    if (done.has(adt + '|' + code + '|' + term)) continue;
    let rec = { adt, code, term };
    try {
      const r = await p.goto(`https://www.archieven.nl/nl/zoeken?mivast=0&mizig=210&miadt=${adt}&miview=inv2&milang=nl&mizk_alle=${encodeURIComponent(term)}&micode=${encodeURIComponent(code)}`, { waitUntil: 'networkidle', timeout: 90000 });
      if (r && [403, 429].includes(r.status())) { console.log('STOP', r.status()); process.exit(1); }
      await p.waitForTimeout(2500);
      rec.title = await p.title();
      rec.count = await p.evaluate(() => (document.body.innerText.match(/Bekijk gevonden archiefstukken \((\d+)\)/) || [])[1] || null);
      const bt = p.locator('button.mi_btn_toggle').first();
      if (await bt.count()) {
        await bt.click({ timeout: 8000 }).catch(() => {});
        for (let k = 0; k < 12; k++) { await p.waitForTimeout(1500); const n = await p.evaluate(() => document.querySelectorAll('.mi_inv_searchresults .mi_tree_content, .mi_inv_searchresults a.mi_hyperlink').length); if (n > 1) break; }
        await p.waitForTimeout(1500);
      }
      rec.items = await p.evaluate(() => { const e = document.querySelector('.mi_inv_searchresults'); if (!e) return []; return [...e.querySelectorAll('a.mi_hyperlink')].map(a => a.innerText.replace(/\s+/g, ' ').trim()).filter(t => t && !/^Bekijk gevonden|^Toon details/.test(t)).map(t => t.slice(0, 1200)); });
      if (!rec.items.length) rec.note = await p.evaluate(() => { const e = document.querySelector('.mi_inv_searchresults'); return e ? e.innerText.replace(/\s+/g, ' ').slice(0, 600) : 'no results block: ' + document.body.innerText.replace(/\s+/g, ' ').slice(0, 300); });
    } catch (e) { rec.err = e.message.slice(0, 100); }
    fs.appendFileSync(out, JSON.stringify(rec) + '\n'); console.log(adt, code, term, rec.count, (rec.items || []).length);
  }
  await b.close();
})();
