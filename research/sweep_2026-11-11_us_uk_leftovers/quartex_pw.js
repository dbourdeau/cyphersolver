// Congregational Library (Quartex) search through headless Chromium: node quartex_pw.js <term> ...
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const t of process.argv.slice(2)) {
    await p.goto('https://congregationallibrary.quartexcollections.com/documents?returning=true&searchText=' + encodeURIComponent(t), { timeout: 60000 }).catch(e => console.log('ERR', String(e).slice(0, 80)));
    await p.waitForTimeout(7000);
    const txt = await p.evaluate(() => document.body.innerText);
    const m = txt.match(/[\d,]+\s+(results|documents|items)[^\n]*/i);
    console.log('==', t, m ? m[0] : '(no count)', txt.length);
    const i = txt.search(/results|Sort by/i);
    console.log(txt.slice(Math.max(0, i), i + 1500).replace(/\n+/g, ' | '));
  }
  await b.close();
})();
