// GStA PK ACTApro web search harvest: node gsta_harvest.js OUT.json [digi] term1 term2 ...
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const out=process.argv[2];let terms=process.argv.slice(3);let digi=false;if(terms[0]=='digi'){digi=true;terms.shift();}
const b=await chromium.launch();const p=await b.newPage();const res={};
for(const t of terms){
 await p.goto('https://archive.spk-berlin.de/actaproweb/search.xhtml',{waitUntil:'networkidle',timeout:90000});
 await p.fill('#searchForm\\:searchTerm_input',t);
 try{await p.click('label[for="searchForm:j_idt249:4:item"]',{timeout:3000});}catch(e){await p.check('#searchForm\\:j_idt249\\:4\\:item',{force:true}).catch(()=>{});}
 if(digi) await p.check('#searchForm\\:onlyWithDigitalDocuments',{force:true}).catch(e=>console.error('digi fail'));
 await p.click('#searchForm\\:searchButton'); await p.waitForLoadState('networkidle').catch(()=>{}); await p.waitForTimeout(5000);
 const txt=await p.innerText('body'); const m=txt.match(/(\d+) - (\d+) von (\d+) Dokumenten/);
 const i=txt.indexOf('Dokumenten angezeigt'); 
 res[t]={count:m?m[0]:'0', text: i>0?txt.slice(i+20):txt.slice(0,300)};
 console.error(t, res[t].count);
 fs.writeFileSync(out,JSON.stringify(res,null,1)); await p.waitForTimeout(2500);
}
await b.close();})();
