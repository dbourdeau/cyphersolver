const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
p.on('request',r=>{const u=r.url(); if(/search-service/.test(u)) console.log(r.method(),u.slice(0,300), (r.postData()||'').slice(0,300));});
await p.goto('https://polona.pl/',{waitUntil:'networkidle',timeout:60000}); await p.waitForTimeout(3000);
const inp=await p.$('input[type=search], input[type=text]'); console.log(!!inp);
await inp.fill('szyfr'); await inp.press('Enter'); await p.waitForTimeout(10000);
console.log(p.url()); console.log((await p.innerText('body')).slice(0,1200));
await b.close();})();
