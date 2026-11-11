// archieven.nl: full description (scope note, dates, scans yes/no) of found items. usage: node anl_det.js out.jsonl < lines "adt<TAB>code<TAB>term<TAB>unitid" (unitid * = every found item, max 40)
const { chromium } = require('playwright'); const fs = require('fs');
const out = process.argv[2]; const jobs = fs.readFileSync(0, 'utf8').split('\n').filter(Boolean).map(l => l.split('\t'));
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [adt, code, term, uid] of jobs) {
    try {
      await p.goto(`https://www.archieven.nl/nl/zoeken?mivast=0&mizig=210&miadt=${adt}&miview=inv2&milang=nl&mizk_alle=${encodeURIComponent(term)}&micode=${encodeURIComponent(code)}`, { waitUntil: 'networkidle', timeout: 90000 }); await p.waitForTimeout(2500);
      const bt = p.locator('button.mi_btn_toggle').first(); if (await bt.count()) { await bt.click({ timeout: 8000 }).catch(() => {}); for (let k = 0; k < 10; k++) { await p.waitForTimeout(1500); if (await p.evaluate(() => document.querySelectorAll('.mi_inv_searchresults a.mi_hyperlink').length) > 1) break; } }
      let links = p.locator('.mi_inv_searchresults a.mi_hyperlink'); const n = await links.count(); let done = 0;
      for (let i = 0; i < n && done < 40; i++) {
        const a = links.nth(i); const t = (await a.innerText().catch(() => '')).replace(/\s+/g, ' ').trim();
        if (!t || /^Bekijk gevonden|^Toon details/.test(t)) continue;
        if (uid !== '*' && !t.startsWith(uid + ' ')) continue;
        await a.click({ timeout: 8000 }).catch(() => {}); await p.waitForTimeout(3500);
        const det = await a.evaluate(el => { let e = el; for (let k = 0; k < 4 && e.parentElement; k++) { e = e.parentElement; if ((e.innerText || '').length > el.innerText.length + 40) break; } return { text: (e.innerText || '').replace(/[ \t]+/g, ' ').replace(/\n\s*\n/g, '\n').slice(0, parseInt(process.env.MAXT || "3000")), thumbs: e.querySelectorAll('img.mi_stripthumb_img').length, hl: [...e.querySelectorAll('.mi_highlight')].map(h => h.parentElement.innerText.replace(/\s+/g, ' ').slice(0, 400)) }; }).catch(() => ({}));
        fs.appendFileSync(out, JSON.stringify({ adt, code, term, item: t.slice(0, 200), ...det }) + '\n'); done++; console.log(adt, code, t.slice(0, 60), (det.text || '').length, det.thumbs);
      }
      if (!done) console.log(adt, code, uid, 'NOT FOUND');
    } catch (e) { console.log('ERR', adt, code, e.message.slice(0, 80)); }
  }
  await b.close();
})();
