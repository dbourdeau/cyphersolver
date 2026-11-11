// archieven.nl site search through headless Chromium (JS-only pages; no challenge met). usage: node anl.js out.jsonl term [term...]
// step 1: table view of inventories (Archieftoegang) holding the term; step 2: open each inventory with the term and keep the highlighted item descriptions.
const { chromium } = require('playwright'); const fs = require('fs');
const out = process.argv[2], terms = process.argv.slice(3);
const doneF = out + '.done.json'; const done = fs.existsSync(doneF) ? JSON.parse(fs.readFileSync(doneF)) : {};
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  const load = async u => { for (let k = 0; k < 3; k++) { try { const r = await p.goto(u, { waitUntil: 'networkidle', timeout: 90000 }); if (r && [403, 429].includes(r.status())) { console.log('STOP', r.status()); process.exit(1); } await p.waitForTimeout(2500); return true; } catch (e) { console.log('ERR', e.message.slice(0, 80)); await p.waitForTimeout(8000); } } return false; };
  for (const t of terms) {
    let invs = [], start = 0, total = null;
    while (true) {
      await load('https://www.archieven.nl/nl/zoeken?mivast=0&mizig=0&miadt=0&miview=tbl&milang=nl&mif3=4&mistart=' + start + '&mizk_alle=' + encodeURIComponent(t));
      const r = await p.evaluate(() => ({ n: (document.body.innerText.match(/([\d.]+)\s+zoekresultaten/) || [])[1], rows: [...document.querySelectorAll('tr.rowlink')].map(tr => ({ url: tr.getAttribute('data-url'), cells: [...tr.querySelectorAll('td.mi_value')].map(td => td.innerText.trim()) })) }));
      if (total === null) total = parseInt((r.n || '0').replace(/\./g, ''));
      invs = invs.concat(r.rows); start += 15;
      if (!r.rows.length || start >= total || start > (parseInt(process.env.CAP || '300'))) break;
    }
    console.log(t, 'inventories', total, 'listed', invs.length);
    for (const iv of invs) {
      const key = t + '|' + iv.url.replace(/.*miadt=(\d+).*micode=([^&]*).*/, '$1|$2');
      if (done[key]) continue;
      if (!await load(iv.url)) continue;
      let items = await p.evaluate(() => [...document.querySelectorAll('a.mi_hyperlink')].filter(a => a.querySelector('.mi_highlight')).map(a => ({ id: (a.querySelector('.mi_tree_unitid') || {}).innerText || '', text: a.innerText.trim().slice(0, 1500), oc: (a.getAttribute('onclick') || '').slice(0, 300) })));
      if (!items.length) { const l = p.locator('button.mi_btn_toggle').first(); if (await l.count()) { await l.click({ timeout: 8000 }).catch(() => {}); await p.waitForTimeout(1500); await p.waitForLoadState('networkidle').catch(() => {}); await p.waitForTimeout(2500); items = await p.evaluate(() => [...document.querySelectorAll('a.mi_hyperlink')].filter(a => a.querySelector('.mi_highlight')).map(a => ({ id: (a.querySelector('.mi_tree_unitid') || {}).innerText || '', text: a.innerText.trim().slice(0, 1500), oc: (a.getAttribute('onclick') || '').slice(0, 300) }))); } }
      const body = items.length ? '' : await p.evaluate(() => { const m = document.body.innerText.match(/.{0,200}gevonden archiefstuk.{0,200}/s); return m ? m[0] : ''; });
      fs.appendFileSync(out, JSON.stringify({ term: t, url: iv.url, code: iv.cells[0], fond: iv.cells[1], archive: iv.cells[2], n: items.length, items, note: body }) + '\n');
      done[key] = 1; fs.writeFileSync(doneF, JSON.stringify(done));
    }
  }
  await b.close();
})();
