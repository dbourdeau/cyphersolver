const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1300,height:900}});
p.on('request',r=>{const u=r.url(); if(!/\.(js|css|woff2?|svg|ico)(\?|$)/.test(u)) console.log(r.method(),u.slice(0,200));});
await p.goto('https://polona.pl/item-view/'+process.argv[2]+'?page=0',{waitUntil:'load',timeout:60000}); await p.waitForTimeout(15000);
await p.screenshot({path:process.argv[3]});
console.log((await p.innerText('body')).slice(0,400));
await b.close();})();
