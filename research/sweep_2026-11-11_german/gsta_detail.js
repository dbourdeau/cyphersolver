// node gsta_detail.js OUT.json "<search term>" "<signature substring>" ...   (pairs)  -> opens the matching result, saves detail text + image URLs
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const out=process.argv[2];const a=process.argv.slice(3);const res=fs.existsSync(out)?JSON.parse(fs.readFileSync(out)):{};
const b=await chromium.launch();const p=await b.newPage();
for(let i=0;i<a.length;i+=2){const term=a[i],sig=a[i+1]; if(res[sig]) continue;
 try{
 await p.goto('https://archive.spk-berlin.de/actaproweb/search.xhtml',{waitUntil:'networkidle',timeout:90000});
 await p.fill('#searchForm\\:searchTerm_input',term);
 await p.click('label[for="searchForm:j_idt249:4:item"]',{timeout:3000}).catch(()=>{});
 await p.click('#searchForm\\:searchButton'); await p.waitForLoadState('networkidle').catch(()=>{}); await p.waitForTimeout(4000);
 const link=p.locator('a',{hasText:sig}).first();
 if(await link.count()==0){res[sig]={err:'not found'};console.error(sig,'not found');continue;}
 await link.click(); await p.waitForLoadState('networkidle').catch(()=>{}); await p.waitForTimeout(5000);
 const txt=await p.innerText('body'); const imgs=await p.$$eval('img',e=>e.map(x=>x.src).filter(s=>!/resource|logo|icon/.test(s)));
 const links=await p.$$eval('a',e=>e.map(x=>x.href).filter(s=>/document|permalink|digital|viewer|dfg|iiif/i.test(s)));
 res[sig]={url:p.url(),text:txt.slice(0,9000),imgs:imgs.slice(0,10),links:[...new Set(links)].slice(0,10)};
 console.error(sig,'ok',txt.length,imgs.length);
 }catch(e){res[sig]={err:String(e).slice(0,200)};console.error(sig,'ERR')}
 fs.writeFileSync(out,JSON.stringify(res,null,1)); await p.waitForTimeout(2000);
}
await b.close();})();
