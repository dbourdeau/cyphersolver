// Paste into the javascript tool of a portal.yek.gov.tr tab opened on /works/advancedsearch/full (any rule).
// Rebuilds the harvest loop used on 25 Nov 2026. Run jobs in the background and poll ST / DB.size; one call may last at most 45 s.
window.DB = new Map(); window.LOG = []; window.ST = { queue: [], errs: [], pages: 0, running: false, cur: '' };
const sleep = ms => new Promise(r => setTimeout(r, ms)); window.sleep = sleep;
const clean = s => (s || '').replace(/\s+/g, ' ').trim();
window.mkRule = (rules, cond) => JSON.stringify({ condition: cond || 'AND', rules: rules.map(r => ({ id: r[0], field: r[0], type: 'string', input: 'text', operator: r[2] || 'in', value: r[1] })) });
// Date filter on the Hijri istinsah year, STRING comparison: only same-length ranges are safe ([200,299]..[800,899], [1000,1110], [y,y]).
window.dxf = (a, b) => '&filter_options_date_type%5Bistinsah_yil%5D=0&istinsah_yil=' + encodeURIComponent(JSON.stringify([a, b]));
window.qurl = (rules, off, extra, cond) => 'https://portal.yek.gov.tr/works/advancedsearch/full' + (off ? '/' + off : '') +
  '?key=&search_key_type=3&search_form_type=ALL_FIELDS&rule=' + encodeURIComponent(mkRule(rules, cond)) + (extra || '');
window.xjAt = async (url, fun, args) => {
  const body = 'xjxfun=' + fun + '&xjxr=' + Date.now() + args.map(a => '&xjxargs[]=' + encodeURIComponent(typeof a == 'object' ? JSON.stringify(a) : (a === false ? 'Bfalse' : 'S' + a))).join('');
  const r = await fetch(url, { method: 'POST', credentials: 'include', headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' }, body });
  return (await r.json()).xjxobj;
};
window.parseRes = h => { const d = new DOMParser().parseFromString(h, 'text/html'); const m = d.body.textContent.replace(/\s+/g, ' ').match(/kayıt içerisinden ([\d,]+) sonuç/); return { tot: m && +m[1].replace(/,/g, ''), d }; };
window.run = async (rules, off, extra, cond) => { const c = await xjAt(qurl(rules, off, extra, cond), 'xajaxSetFilter', [JSON.parse(mkRule(rules, cond)), false]); const dr = c.find(x => x.id == 'data_result'); return dr ? parseRes(dr.data) : null; };
window.parseRows = d => [...d.querySelectorAll('.biblio_result_row')].map(r => {
  const g = {}; r.querySelectorAll('.marc-content-results-label').forEach(l => { const k = clean(l.textContent); const v = clean(l.nextElementSibling ? l.nextElementSibling.textContent : '').replace(/^:\s*/, ''); if (!(k in g)) g[k] = v; });
  return { b: g['Bibliyografik kayıt no.'] || '', t: clean((r.querySelector('.summary_title') || {}).textContent).replace(/^\d+\.\s*/, ''), a: g['Müellif adı'] || '', l: g['Dil'] || '', c: g['Tasnif no./Konu'] || '', d: g['İstinsah tarihi'] || '', p: g['Fiziksel özellikler'] || '', lib: g['Kütüphane adı'] || '', co: g['Koleksiyon'] || '', cn: (g['Koleksiyon no.'] || '').replace(/\s*\[.*$/, ''), m: g['Materyal türü'] || '', i: [...r.querySelectorAll('a')].some(a => /^Görüntü$/.test(clean(a.textContent))) ? 1 : 0 };
});
// job = {label, rules:[[field,value]...], cond:'AND', extra: dxf(a,b), max, adaptive:true (re-run in slices [200,999] and [1000,1110] when over 1500 hits)}
window.doJob = async job => {
  ST.cur = job.label; let off = 0, tot = null, n = 0, added = 0, split = false; const max = job.max || 5000;
  while (true) {
    let p = null;
    for (let k = 0; k < 3; k++) { try { p = await run(job.rules, off, job.extra, job.cond); break; } catch (e) { ST.errs.push(job.label + ' ' + off + ' ' + e.message); await sleep(3000); } }
    if (!p) { if (tot === null) tot = 0; break; }
    if (tot === null) tot = p.tot;
    const rows = parseRows(p.d); ST.pages++;
    rows.forEach(r => { if (!r.b) return; let e = DB.get(r.b); if (!e) { e = Object.assign({}, r, { tags: [] }); DB.set(r.b, e); added++; } if (!e.tags.includes(job.label)) e.tags.push(job.label); });
    n += rows.length; off += 100;
    if (job.adaptive && !job.extra && tot > (job.limit || 1500)) { split = true; ST.queue.unshift({ label: job.label + '|E2', rules: job.rules, cond: job.cond, extra: dxf(1000, 1110), max: 3000 }, { label: job.label + '|E1', rules: job.rules, cond: job.cond, extra: dxf(200, 999), max: 3000 }); break; }
    if (rows.length < 100 || off >= tot || off >= max) break;
    await sleep(1000 + Math.random() * 500);
  }
  LOG.push({ label: job.label, tot: tot || 0, got: n, added, split }); return LOG[LOG.length - 1];
};
window.startLoop = async () => { while (ST.queue.length) { const j = ST.queue.shift(); await doJob(j); await sleep(800); } };
// Snapshot to the portal origin's IndexedDB (db yekharvest / store kv / key db), as {rows, log, t}.
window.idbSave = () => new Promise((res, rej) => { const o = indexedDB.open('yekharvest', 1); o.onupgradeneeded = () => o.result.createObjectStore('kv'); o.onsuccess = () => { const tx = o.result.transaction('kv', 'readwrite'); tx.objectStore('kv').put(JSON.stringify({ rows: [...DB.values()], log: LOG, t: Date.now() }), 'db'); tx.oncomplete = () => res(DB.size); tx.onerror = () => rej(tx.error); }; });
// Never use multi-word values (OR of tokens): use one rule per token with cond 'AND'. Put 1 or 2 loops (startLoop()) at most, 800-1500 ms apart.
// Example: ST.queue.push({label:'A:ist800-899', rules:[['title','']], extra:dxf(800,899), max:9000}); startLoop();
