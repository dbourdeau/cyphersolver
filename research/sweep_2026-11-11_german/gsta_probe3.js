const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1400,height:1000}});
await p.goto(process.argv[2],{waitUntil:'networkidle',timeout:90000}).catch(()=>{}); await p.waitForTimeout(5000);
const n=p.locator('text=Nr. 5876').first(); console.log(await n.count());
await n.scrollIntoViewIfNeeded(); await n.click(); await p.waitForTimeout(6000);
const t=await p.innerText('body'); const i=t.indexOf('Derfflingers'); console.log(t.length,i); console.log(t.slice(Math.max(0,i-1500),i+1500));
await p.screenshot({path:process.argv[3]});
const html=await p.content(); require('fs').writeFileSync(process.argv[3]+'.html',html);
await b.close();})();
