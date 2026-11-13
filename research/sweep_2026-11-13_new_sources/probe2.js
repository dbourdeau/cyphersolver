const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
p.on('response',async r=>{const u=r.url(); if(/polona\.pl\/api/.test(u)) {console.log(r.status(),u.slice(0,250)); }});
await p.goto(process.argv[2],{waitUntil:'networkidle',timeout:60000}); await p.waitForTimeout(8000);
console.log(await p.title()); console.log((await p.innerText('body')).slice(0,800));
await b.close();})();
