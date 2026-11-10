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

  // the wordmark: every letter deciphers out of a run of glyphs, left to right; afterwards one letter now and then
  // slips back into cipher and is read again
  const wm=document.querySelector('.wordmark .wm');
  if(wm && !still){
    const Ls=[...wm.querySelectorAll('.l')], WG='0123456789§¶†‡∴⊕ABDFGKMNQTXZ';
    const g=()=>WG[Math.random()*WG.length|0];
    const flip=(l,ms)=>new Promise(res=>{ l.classList.add('enc'); const t0=performance.now(); let last=0;
      const f=now=>{ if(now-last>55){ l.dataset.g=g(); last=now; }
        if(now-t0<ms) return requestAnimationFrame(f);
        l.classList.remove('enc'); l.classList.add('flash'); requestAnimationFrame(()=>requestAnimationFrame(()=>l.classList.remove('flash'))); res(); };
      requestAnimationFrame(f); });
    Ls.forEach(l=>{ l.dataset.g=g(); l.classList.add('enc'); });
    Ls.forEach((l,i)=>setTimeout(()=>flip(l,380+Math.random()*260),300+i*90));
    (async()=>{ await wait(3000); for(;;){ await wait(3500+Math.random()*4500); if(document.hidden) continue;
      await flip(Ls[Math.random()*Ls.length|0],300+Math.random()*300); } })();
  }

  // the hero video: herovid.js

  // On a phone the four reference sections (results, browse, the catalogue queue, contributors) fold to a row each:
  // style.css hides their bodies under html.js until .open. The row is the heading, with a hint of what is inside and
  // a button over it; a link to anything inside a folded section opens it first.
  const setOpen=(s,on)=>{ s.classList.toggle('open',on); const b=s.querySelector('.fold-btn');
    b.setAttribute('aria-expanded',String(on)); b.setAttribute('aria-label',(on?'Hide: ':'Show: ')+b.dataset.name); };
  [['#scoreboard',s=>{ const b=s.querySelector('.sb-big b'); return b?b.textContent+' keys recovered':''; }],
   ['.browse',s=>{ const m=/([\d,]+) write-ups/.exec(s.textContent); return m?m[1]+' write-ups':''; }],
   ['.catq',s=>{ const m=/^\s*([\d,]+)/.exec((s.querySelector('p')||{}).textContent||''); return m?m[1]+' open':''; }],
   ['#contributors',()=>'who did what']].forEach(([q,hint])=>{
    const s=document.querySelector(q), h=s&&s.querySelector('h2'); if(!h) return;
    const name=[...h.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent).join('').trim(), t=document.createElement('span'), b=document.createElement('button');
    t.className='fold-hint'; t.textContent=hint(s);
    b.type='button'; b.className='fold-btn'; b.dataset.name=name;
    h.append(t,b); s.classList.add('folds'); setOpen(s,false);
    b.addEventListener('click',()=>setOpen(s,!s.classList.contains('open')));
  });
  const unfold=()=>{ let t=null; try{ t=location.hash.length>1&&document.getElementById(decodeURIComponent(location.hash.slice(1))); }catch(e){}
    const s=t&&t.closest('.folds'); if(s&&!s.classList.contains('open')){ setOpen(s,true); t.scrollIntoView(); } };
  unfold(); addEventListener('hashchange',unfold);
  document.addEventListener('click',e=>{ if(e.target.closest('a[href^="#"]')) setTimeout(unfold,0); });

  // ...and a bar of the common routes comes up once the hero's own buttons have scrolled away
  const cta=document.querySelector('.hero-cta');
  if(cta && 'IntersectionObserver' in window){
    const bar=document.createElement('nav'); bar.className='tabbar'; bar.setAttribute('aria-label','Shortcuts');
    bar.innerHTML='<a href="writeups.html">Results</a><a href="catalogue.html">Help solve</a>'+
      '<button type="button"><svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="4.6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10.5 10.5L14 14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>Search</button>';
    document.body.append(bar);
    bar.querySelector('button').addEventListener('click',()=>{ const b=document.querySelector('.searchbtn'); if(b) b.click(); });
    new IntersectionObserver(es=>bar.classList.toggle('on',!es[0].isIntersecting && es[0].boundingClientRect.top<0)).observe(cta);
  }

  // the live strip: three lines beside the video, one line under the wordmark on a phone
  const strip=document.querySelector('.hero .cipherstrip'); if(!strip || !strip.offsetParent) return;
  const one=matchMedia('(max-width:760px)').matches, NL=one?1:3, NC=one?24:28;
  let seen=true;
  if('IntersectionObserver' in window) new IntersectionObserver(es=>{ seen=es[0].isIntersecting; }).observe(strip);
  const GL='0123456789abcdefghilmnopqrstuxyz§†∴';
  const rnd=n=>{ let s=''; for(let i=0;i<n;i++) s+=GL[Math.random()*GL.length|0]; return s; };
  let list=[]; try{ list=await (await fetch('reveal/index.json')).json(); }catch(e){ return; }
  if(!list.length) return;
  strip.classList.add('live');
  const order=list.map(x=>[Math.random(),x]).sort((a,b)=>a[0]-b[0]).map(x=>x[1]);
  let k=0, hover=false;
  strip.addEventListener('pointerenter',()=>hover=true); strip.addEventListener('pointerleave',()=>hover=false);
  // NL lines of about NC characters of cipher, groups kept whole, starting at a random cipher run
  function lines(tokens){
    const c=tokens.filter(t=>t.g && t.cls!=='plain' && t.cls!=='null');
    const start=c.length>40 ? Math.floor(Math.random()*(c.length-36)) : 0, out=[];
    let cur=[], len=0;
    for(const t of c.slice(start)){ const w=t.g.length+1;
      if(len+w>NC && cur.length){ out.push(cur); cur=[]; len=0; if(out.length===NL) break; }
      cur.push(t); len+=w; }
    if(cur.length && out.length<NL) out.push(cur);
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
    await wait(6500); while(hover || document.hidden || !seen) await wait(500);      // no fetching for a strip nobody sees
    strip.classList.add('fade'); await wait(600);
    show();
  }
  show();
})();
