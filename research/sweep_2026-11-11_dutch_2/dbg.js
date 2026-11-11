const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto(process.argv[2], { waitUntil: 'networkidle', timeout: 90000 }); await p.waitForTimeout(4000);
  const info = await p.evaluate(() => ({ btn: [...document.querySelectorAll('button')].map(b => b.className + ':' + b.innerText.trim().slice(0, 50)), hl: document.querySelectorAll('.mi_highlight').length, txt: document.body.innerText.replace(/\n\s*\n/g, '\n').slice(0, 2500) }));
  console.log(JSON.stringify(info.btn), info.hl); console.log(info.txt);
  fs.writeFileSync(process.argv[3] || 'dbg.html', await p.content());
  await b.close();
})();
