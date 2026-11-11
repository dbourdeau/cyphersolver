const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('https://archive.spk-berlin.de/actaproweb/welcome.xhtml',{waitUntil:'networkidle',timeout:60000});
console.log(p.url(), await p.title());
console.log((await p.innerText('body')).slice(0,1500));
const ins=await p.$$eval('input,button,a',els=>els.slice(0,80).map(e=>e.tagName+' '+(e.id||'')+' '+(e.name||'')+' '+(e.type||'')+' '+(e.innerText||e.value||'').slice(0,40)+' '+(e.href||'')));
console.log(ins.join('\n'));
await b.close();})();
