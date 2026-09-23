// The home page's live header: real ciphertext from the reveal passages deciphers itself line by line and names its
// letter, then the next one; the random button opens any write-up.
(async()=>{
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const wait=ms=>new Promise(r=>setTimeout(r,ms));

  // random cipher
  const rb=document.querySelector('.randbtn');
  if(rb) rb.addEventListener('click',async()=>{ try{ const ps=await (await fetch('pages.json')).json();
    location.href=ps[Math.floor(Math.random()*ps.length)].slug+'.html'; }catch(e){ location.href='writeups.html'; } });

  // the live strip
  const strip=document.querySelector('.hero .cipherstrip'); if(!strip) return;
  const GL='0123456789abcdefghilmnopqrstuxyz§†∴';
  const rnd=n=>{ let s=''; for(let i=0;i<n;i++) s+=GL[Math.random()*GL.length|0]; return s; };
  let list=[]; try{ list=await (await fetch('reveal/index.json')).json(); }catch(e){ return; }
  if(!list.length) return;
  strip.classList.add('live');
  const order=list.map(x=>[Math.random(),x]).sort((a,b)=>a[0]-b[0]).map(x=>x[1]);
  let k=0, hover=false;
  strip.addEventListener('pointerenter',()=>hover=true); strip.addEventListener('pointerleave',()=>hover=false);
  // three lines of about 28 characters of cipher, groups kept whole, starting at a random cipher run
  function lines(tokens){
    const c=tokens.filter(t=>t.g && t.cls!=='plain' && t.cls!=='null');
    const start=c.length>40 ? Math.floor(Math.random()*(c.length-36)) : 0, out=[];
    let cur=[], len=0;
    for(const t of c.slice(start)){ const w=t.g.length+1;
      if(len+w>28 && cur.length){ out.push(cur); cur=[]; len=0; if(out.length===3) break; }
      cur.push(t); len+=w; }
    if(cur.length && out.length<3) out.push(cur);
    return out;
  }
  async function show(){
    const item=order[k++ % order.length];
    let d; try{ d=await (await fetch('reveal/'+item.slug+'.json')).json(); }catch(e){ return; }
    const L=lines(d.tokens||[]); if(!L.length) return;
    const joinP=l=>l.map(t=>t.cls==='unk'||t.p==='?'?'…':t.p).join(d.unit && /letter|sign/i.test(d.unit)?'':' ');
    strip.innerHTML=L.map(l=>`<span class="ls"><span class="lc">${esc(l.map(t=>t.g).join(' '))}</span><span class="lp"></span></span>`).join('')+
      `<a class="lsrc" href="${item.slug}.html">${esc(item.label)} &rarr;</a>`;
    strip.classList.remove('fade');
    const rows=[...strip.querySelectorAll('.ls')];
    for(let i=0;i<rows.length;i++){
      const lp=rows[i].querySelector('.lp'), target=joinP(L[i]);
      if(still){ lp.textContent=target; rows[i].classList.add('done'); continue; }
      await wait(i?500:900);
      const t0=performance.now();
      await new Promise(res=>{ const f=now=>{ const q=Math.min(1,(now-t0)/1100), n=Math.floor(q*target.length);
        lp.textContent=target.slice(0,n)+(q<1?rnd(Math.min(6,target.length-n)):''); if(q<1) requestAnimationFrame(f); else res(); };
        requestAnimationFrame(f); });
      rows[i].classList.add('done');
    }
    strip.querySelector('.lsrc').classList.add('on');
    if(still) return;
    await wait(6500); while(hover || document.hidden) await wait(500);
    strip.classList.add('fade'); await wait(600);
    show();
  }
  show();
})();

// the slides: when one comes round, its strip of cipher deciphers itself tile by tile
(()=>{
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches; if(still) return;
  const GL='0123456789abcdefghilmnopqrstuxyz';
  const run=panel=>{
    const tiles=[...panel.querySelectorAll('.bn-solve .bt:not(.more)')]; if(!tiles.length) return;
    const token=(panel._bt=(panel._bt||0)+1);
    tiles.forEach(t=>{ const p=t.querySelector('.p'); p.dataset.v=p.dataset.v||p.textContent; p.textContent=''; t.classList.add('scr'); t.classList.remove('hit'); });
    tiles.forEach((t,i)=>setTimeout(()=>{
      if(panel._bt!==token) return;
      const p=t.querySelector('.p'), v=p.dataset.v, t0=performance.now();
      const f=now=>{ if(panel._bt!==token) return; const q=Math.min(1,(now-t0)/380);
        p.textContent=q<1?Array.from({length:Math.max(1,v.length)},()=>GL[Math.random()*GL.length|0]).join(''):v;
        if(q<1) requestAnimationFrame(f); else { t.classList.remove('scr'); t.classList.add('hit'); } };
      requestAnimationFrame(f);
    },500+i*170));
  };
  const panels=document.querySelectorAll('.bn-panel');
  const mo=new MutationObserver(ms=>ms.forEach(m=>{ const el=m.target; if(el.classList.contains('on') && !m.oldValue?.split(' ').includes('on')) run(el); }));
  panels.forEach(p=>mo.observe(p,{attributes:true,attributeFilter:['class'],attributeOldValue:true}));
  const first=document.querySelector('.bn-panel.on'); if(first) run(first);
})();
