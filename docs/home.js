// The home page's live header: the wordmark deciphers itself; the random button opens any write-up.
(async()=>{
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const wait=ms=>new Promise(r=>setTimeout(r,ms));

  // random cipher
  const rb=document.querySelector('.randbtn');
  if(rb) rb.addEventListener('click',async()=>{ try{ const ps=await (await fetch('pages.json')).json();
    location.href=ps[Math.floor(Math.random()*ps.length)].slug+'.html'; }catch(e){ location.href='writeups.html'; } });

  // the wordmark: every letter deciphers out of a run of glyphs, left to right, once. It then stays still: the name
  // has to be readable, and the decipher panel beside it is the one thing in the hero that keeps moving
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
  }

  // the hero video: herovid.js. It waits in a dialog; the film button opens it and plays it from the start with sound,
  // closing it stops it. Without JavaScript, or without <dialog>, the button is a plain link to the file.
  // the poster shelf (_films_page.py): a card opens the dialog with its data-film id; a card with no dialog stays a link
  const fds=[...document.querySelectorAll('.filmdlg')];
  document.querySelectorAll('.filmbtn,.filmcard[data-film]').forEach((fb,i)=>{
    const fd=fb.dataset.film?document.querySelector(`.filmdlg[data-film="${fb.dataset.film}"]`):fds[i]; if(!fd || !fd.showModal) return;
    const fv=fd.querySelector('video');
    fb.addEventListener('click',e=>{ e.preventDefault(); fd.showModal(); const b=fd.querySelector('.hv-sound'); if(b) b.click(); });
    fd.addEventListener('close',()=>{ if(fv) fv.pause(); });
    fd.addEventListener('click',e=>{ if(e.target===fd || e.target.closest('.film-x')) fd.close(); });
  });

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

})();
