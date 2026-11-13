const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
p.on('response',r=>{const u=r.url(); if(/api|search|solr/.test(u)&&!/\.(js|css|png|svg)/.test(u)) console.log(r.status(),u.slice(0,200));});
await p.goto(process.argv[2],{waitUntil:'networkidle',timeout:60000});
console.log((await p.title()));
console.log((await p.innerText('body')).slice(0,1500));
await b.close();})();
