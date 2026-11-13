const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
p.on('response',async r=>{const u=r.url(); console.log(r.status(),u.slice(0,200));});
await p.goto('https://polona.pl/item-view/'+process.argv[2],{waitUntil:'networkidle',timeout:60000}); await p.waitForTimeout(6000);
console.log(await p.title()); console.log((await p.innerText('body')).slice(0,600));
await b.close();})();
