// archieven.nl site search: list the inventories (Archieftoegang) holding each term. usage: node anl_list.js out.jsonl term [term...]  (env ADT=<miadt> to limit to one archive, CAP=max rows)
const { chromium } = require('playwright'); const fs = require('fs');
const out = process.argv[2], terms = process.argv.slice(3); const adt = process.env.ADT || '0'; const cap = parseInt(process.env.CAP || '600');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const t of terms) {
    let invs = [], start = parseInt(process.env.START || "0"), total = null;
    while (true) {
      let ok = false;
      for (let k = 0; k < 3 && !ok; k++) { try { const r = await p.goto(`https://www.archieven.nl/nl/zoeken?mivast=0&mizig=0&miadt=${adt}&miview=tbl&milang=nl&mif3=4&mistart=${start}&mizk_alle=${encodeURIComponent(t)}`, { waitUntil: 'networkidle', timeout: 90000 }); if (r && [403, 429].includes(r.status())) { console.log('STOP', r.status()); process.exit(1); } await p.waitForTimeout(2000); ok = true; } catch (e) { await p.waitForTimeout(8000); } }
      const r = await p.evaluate(() => ({ n: (document.body.innerText.match(/([\d.]+)\s+zoekresulta/) || [])[1], rows: [...document.querySelectorAll('tr.rowlink')].map(tr => ({ url: tr.getAttribute('data-url'), cells: [...tr.querySelectorAll('td.mi_value')].map(td => td.innerText.trim()) })) }));
      if (total === null) total = parseInt((r.n || '0').replace(/\./g, ''));
      invs = invs.concat(r.rows); start += 15;
      if (!r.rows.length || start >= total || start >= cap) break;
    }
    console.log(t, 'total', total, 'listed', invs.length);
    for (const iv of invs) { const m = iv.url.match(/miadt=(\d+).*micode=([^&]*)/) || []; fs.appendFileSync(out, JSON.stringify({ term: t, adt: m[1], code: decodeURIComponent(m[2] || ''), fond: iv.cells[1], archive: iv.cells[2], total }) + '\n'); }
    if (!invs.length) fs.appendFileSync(out, JSON.stringify({ term: t, total }) + '\n');
  }
  await b.close();
})();
