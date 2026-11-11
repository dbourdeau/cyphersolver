// GStA PK ACTApro: full record for a search hit.  node gsta_detail.js OUT.json "<search term>" "<signature substring>" ... (pairs)
// Opens the hit in the Tektonik view, clicks its node and saves the "Vollansicht" text and whether images are attached.
const {chromium}=require('playwright');const fs=require('fs');
const norm=s=>s.replace(/\s+/g,' ').trim();
(async()=>{const out=process.argv[2];const a=process.argv.slice(3);const res=fs.existsSync(out)?JSON.parse(fs.readFileSync(out)):{};
const b=await chromium.launch();const ctx=await b.newContext();await ctx.route(/hotlog/,r=>r.abort());const p=await ctx.newPage();
for(let i=0;i<a.length;i+=2){const term=a[i],sig=a[i+1]; if(res[sig]&&!res[sig].err) continue;
 try{
 await p.goto('https://archive.spk-berlin.de/actaproweb/search.xhtml',{waitUntil:'domcontentloaded',timeout:90000});
 await p.waitForSelector('#searchForm\\:searchTerm_input',{timeout:60000});
 await p.waitForTimeout(4000); await p.fill('#searchForm\\:searchTerm_input',term);
 await p.click('label[for="searchForm:j_idt249:4:item"]',{timeout:3000}).catch(()=>{});
 await p.click('#searchForm\\:searchButton'); await p.waitForTimeout(7000);
 const idx=await p.$$eval('a',(els,sig)=>els.findIndex(e=>e.textContent.replace(/\s+/g,' ').includes(sig+' -')),sig);
 if(idx<0){res[sig]={err:'not found'};console.error(sig,'not found');fs.writeFileSync(out,JSON.stringify(res,null,1));continue;}
 await p.locator('a').nth(idx).click(); await p.waitForTimeout(7000);
 const idx2=await p.$$eval('a,span,div',(els,sig)=>{let best=-1;els.forEach((e,k)=>{if(e.children.length==0&&e.textContent.replace(/\s+/g,' ').includes(sig+' -'))best=k});return best},sig);
 if(idx2>=0){const n=p.locator('a,span,div').nth(idx2); await n.scrollIntoViewIfNeeded().catch(()=>{}); await n.click().catch(()=>{}); await p.waitForTimeout(5000);}
 let txt=await p.innerText('body'); const j=txt.indexOf('Vollansicht'); txt=j>=0?txt.slice(j,j+7000):'NO DETAIL';
 const k=txt.indexOf('\n \n'); if(k>0) txt=txt.slice(0,k);
 const imgs=await p.$$eval('img',e=>e.map(x=>x.src).filter(s=>!/javax.faces.resource|logo|icon/.test(s)));
 res[sig]={url:p.url(),text:txt,imgs:imgs.slice(0,6)};
 console.error(sig,'ok',txt.length,imgs.length);
 }catch(e){res[sig]={err:String(e).slice(0,200)};console.error(sig,'ERR')}
 fs.writeFileSync(out,JSON.stringify(res,null,1)); await p.waitForTimeout(2000);
}
await b.close();})();
