// shared behaviour: theme, menu, active link, contents strip, scroll-reveal, card glow, interlinear tiles, queue filter
(function(){
  // theme: stored choice wins, otherwise follow the OS
  const root=document.documentElement;
  let stored=null; try{ stored=localStorage.getItem('theme'); }catch(e){}
  const prefersLight=matchMedia('(prefers-color-scheme: light)').matches;
  root.dataset.theme = stored || (prefersLight ? 'light' : 'dark');
  document.querySelectorAll('.nav .theme').forEach(b=>b.addEventListener('click',()=>{
    root.dataset.theme = root.dataset.theme==='dark' ? 'light' : 'dark';
    try{ localStorage.setItem('theme', root.dataset.theme); }catch(e){}
  }));
  // mobile menu
  const nav=document.querySelector('.nav'), tog=document.querySelector('.navtoggle');
  if(tog){ tog.addEventListener('click',()=>{ const open=nav.classList.toggle('open'); tog.setAttribute('aria-expanded',open); }); }
  // write-ups dropdown: close on outside click or Escape
  // dropdowns (Write-ups, Explore): one open at a time; close on outside click or Escape
  const menus=[...document.querySelectorAll('.nav details.menu')];
  menus.forEach(m=>m.addEventListener('toggle',()=>{ if(m.open) menus.forEach(o=>{ if(o!==m) o.open=false; }); }));
  if(menus.length){
    document.addEventListener('click',e=>{ menus.forEach(m=>{ if(m.open && !m.contains(e.target)) m.open=false; }); });
    document.addEventListener('keydown',e=>{ if(e.key==='Escape'){ menus.forEach(m=>m.open=false); nav.classList.remove('open'); if(tog) tog.setAttribute('aria-expanded','false'); } });
  }
  // active section links (index) and active page
  const here=location.pathname.split('/').pop()||'index.html';
  document.querySelectorAll('.nav .links > a').forEach(a=>{ const h=a.getAttribute('href').split('#')[0]; if(h===here && !a.getAttribute('href').includes('#')) a.classList.add('active'); });
  document.querySelectorAll('.nav .panel a[aria-current]').forEach(a=>{ const sum=a.closest('details.menu')?.querySelector('summary'); if(sum) sum.classList.add('active'); });
  // card glow follows the pointer
  document.querySelectorAll('.card').forEach(c=>c.addEventListener('pointermove',e=>{ const r=c.getBoundingClientRect(); c.style.setProperty('--mx',((e.clientX-r.left)/r.width*100)+'%'); }));
  // contents strip: highlight the section in view
  const toc=document.querySelector('.toc');
  if(toc && 'IntersectionObserver' in window){
    const links=[...toc.querySelectorAll('a')]; const map=new Map(links.map(a=>[a.getAttribute('href').slice(1),a]));
    const io=new IntersectionObserver(es=>{ es.forEach(e=>{ if(e.isIntersecting){ links.forEach(l=>l.classList.remove('on')); const l=map.get(e.target.id); if(l) l.classList.add('on'); } }); },{rootMargin:'-20% 0px -70% 0px'});
    map.forEach((a,id)=>{ const h=document.getElementById(id); if(h) io.observe(h); });
  }
  // scroll reveal (kept subtle; never leaves content hidden)
  const els=document.querySelectorAll('main > h2, main > p, main > table, main > figure, main > blockquote, main > .callout, main > .cards, main > .stats, main > ol, main > ul, main > #decoder, main > details, main > h3, main > .tg, main > .item');
  if(!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const rio=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); rio.unobserve(e.target);} }),{threshold:.05,rootMargin:'0px 0px -5% 0px'});
  els.forEach(el=>{ if(el.getBoundingClientRect().top < innerHeight*1.1) return; el.classList.add('reveal'); rio.observe(el); });
  setTimeout(()=>els.forEach(el=>el.classList.add('in')),2000);
})();
// render [{g:'972', p:'the', cls:''}, ...] as interlinear tiles into a container
function renderTiles(el, items){
  el.innerHTML='';
  for(const it of items){
    const t=document.createElement('span'); t.className='tile '+(it.cls||'');
    const p=document.createElement('span'); p.className='p'; p.textContent=it.p;
    const g=document.createElement('span'); g.className='g'; g.textContent=it.g||' ';
    t.appendChild(p); t.appendChild(g); el.appendChild(t);
  }
}
// 'show more' blocks on the home page
document.querySelectorAll('.showmore').forEach(b=>b.addEventListener('click',()=>{ const box=b.previousElementSibling; const open=box.hasAttribute('hidden'); if(open) box.removeAttribute('hidden'); else box.setAttribute('hidden',''); b.textContent = open ? 'Show fewer' : b.dataset.label || b.textContent; }));
document.querySelectorAll('.showmore').forEach(b=>b.dataset.label=b.textContent);
// big-news rotation: one panel at a time, every 9 s; pauses on hover, focus, hidden tab or the pause button; no auto-rotate under reduced motion
(function(){
  const box=document.querySelector('.bignews.bn-rot'); if(!box) return;
  const panels=[...box.querySelectorAll('.bn-panel')]; if(panels.length<2) return;
  const dots=box.querySelector('.bn-dots'), pauseBtn=box.querySelector('.bn-pause');
  let i=0, timer=null, paused=matchMedia('(prefers-reduced-motion: reduce)').matches, hovering=false;
  panels.forEach((p,k)=>{ const b=document.createElement('button'); b.type='button'; b.setAttribute('role','tab'); b.setAttribute('aria-label','Show item '+(k+1)); b.addEventListener('click',()=>{ go(k); restart(); }); dots.appendChild(b); });
  const db=[...dots.children];
  function go(k, instant){
    i=(k+panels.length)%panels.length;
    if(instant){ box.classList.add('instant'); requestAnimationFrame(()=>requestAnimationFrame(()=>box.classList.remove('instant'))); }
    panels.forEach((p,n)=>{ const on=n===i; p.classList.toggle('on',on); if(on) p.removeAttribute('hidden'); else if(instant) p.setAttribute('hidden',''); else setTimeout(()=>{ if(!p.classList.contains('on')) p.setAttribute('hidden',''); },650); });
    db.forEach((b,n)=>b.setAttribute('aria-selected', n===i?'true':'false'));
  }
  function tick(){ if(!paused && !hovering && !document.hidden) go(i+1); }
  function restart(){ clearInterval(timer); timer=setInterval(tick,9000); }
  function setPause(v){ paused=v; pauseBtn.setAttribute('aria-pressed',v); pauseBtn.setAttribute('aria-label',v?'Resume rotation':'Pause rotation'); pauseBtn.innerHTML=v?'&#9654;':'&#10074;&#10074;'; }
  box.querySelector('.bn-prev').addEventListener('click',()=>{ go(i-1); restart(); });
  box.querySelector('.bn-next').addEventListener('click',()=>{ go(i+1); restart(); });
  pauseBtn.addEventListener('click',()=>setPause(!paused));
  box.addEventListener('pointerenter',()=>hovering=true); box.addEventListener('pointerleave',()=>hovering=false);
  box.addEventListener('focusin',()=>hovering=true); box.addEventListener('focusout',e=>{ if(!box.contains(e.relatedTarget)) hovering=false; });
  box.addEventListener('keydown',e=>{ if(e.key==='ArrowLeft'){ go(i-1); restart(); } else if(e.key==='ArrowRight'){ go(i+1); restart(); } });
  if(paused) setPause(true);
  const start=/[?&]bn=(\d+)/.exec(location.search); // ?bn=N opens on panel N (1-based)
  go(start ? +start[1]-1 : 0, true); restart();
})();
// priority-queue filter: show one tier at a time
(function(){
  const btns=document.querySelectorAll('.qf'); if(!btns.length) return;
  const tiers=document.querySelectorAll('h3.tier');
  const cards=document.querySelectorAll('.tg');
  function apply(f, remember){
    cards.forEach(c=>{ c.hidden = !(f==='all' || c.classList.contains(f)); });
    tiers.forEach(t=>{ t.hidden = !(f==='all' || t.dataset.t===f); });
    btns.forEach(b=>b.classList.toggle('on', b.dataset.f===f));
    if(remember){ try{ history.replaceState(null,'',f==='live'?location.pathname:'#q='+f); }catch(e){} }
  }
  btns.forEach(b=>b.addEventListener('click',()=>apply(b.dataset.f, true)));
  const m=/^#q=(\w+)$/.exec(location.hash); apply(m ? m[1] : 'live', false);
  // each queue block shows three lines until clicked
  cards.forEach(c=>{ const p=c.querySelector('.tg-b p'); if(!p) return; const t=document.createElement('div'); t.className='tgmore'; t.textContent='more'; p.after(t);
    const toggle=()=>{ const on=c.classList.toggle('x'); t.textContent=on?'less':'more'; }; p.addEventListener('click',toggle); t.addEventListener('click',toggle); });
})();
// write-ups index: outcome / period / source chips, text search, state in the hash (writeups.html#kind=solved&q=rome)
(function(){
  const items=[...document.querySelectorAll('ul.wl li')]; if(!items.length) return;
  const chips=[...document.querySelectorAll('.wfilters .chip[data-facet]')], q=document.getElementById('wq'),
        count=document.getElementById('wcount'), reset=document.getElementById('wreset');
  const state={f:{}, q:''};
  function parse(){
    state.f={}; state.q='';
    location.hash.slice(1).split('&').forEach(kv=>{ if(!kv) return; const i=kv.indexOf('='); const k=i<0?kv:kv.slice(0,i), v=i<0?'':decodeURIComponent(kv.slice(i+1));
      if(k==='q') state.q=v; else if(k) state.f[k]=v.split(',').filter(Boolean); });
  }
  function apply(remember){
    chips.forEach(c=>c.setAttribute('aria-pressed', (state.f[c.dataset.facet]||[]).includes(c.dataset.val)?'true':'false'));
    if(q.value!==state.q) q.value=state.q;
    const needle=state.q.trim().toLowerCase(); let n=0;
    items.forEach(li=>{ let ok=true;
      for(const k in state.f){ const vs=state.f[k]; if(vs.length && !vs.includes(li.dataset[k])) ok=false; }
      if(ok && needle && !(li.dataset.q||'').includes(needle)) ok=false;
      li.hidden=!ok; if(ok) n++; });
    document.querySelectorAll('.wsec').forEach(s=>{ s.hidden=![...s.querySelectorAll('li')].some(li=>!li.hidden); });
    count.textContent = n===items.length ? 'All '+n+' entries' : n+' of '+items.length+' entries';
    if(remember){ const parts=[]; for(const k in state.f) if(state.f[k].length) parts.push(k+'='+state.f[k].join(','));
      if(needle) parts.push('q='+encodeURIComponent(state.q.trim()));
      try{ history.replaceState(null,'', parts.length ? '#'+parts.join('&') : location.pathname+location.search); }catch(e){} }
  }
  chips.forEach(c=>c.addEventListener('click',()=>{ const a=state.f[c.dataset.facet]=state.f[c.dataset.facet]||[]; const i=a.indexOf(c.dataset.val); if(i<0) a.push(c.dataset.val); else a.splice(i,1); apply(true); }));
  q.addEventListener('input',()=>{ state.q=q.value; apply(true); });
  reset.addEventListener('click',()=>{ state.f={}; state.q=''; apply(true); });
  window.addEventListener('hashchange',()=>{ parse(); apply(false); });
  parse(); apply(false);
})();
// site search: a palette opened from the nav button, "/" or Ctrl+K. The index (search.json, one entry per page,
// per h2 section and per catalogue entry) is fetched the first time the box opens; matching is accent- and
// case-insensitive, every term must occur, "quoted phrases" are one term, and results link straight to the section.
(function(){
  const box=document.getElementById('search'), input=document.getElementById('sq'), res=document.getElementById('sres'), sn=document.getElementById('sn');
  if(!box||!input||!res) return;
  const btns=document.querySelectorAll('.searchbtn'), closeBtn=box.querySelector('.sclose');
  const ver=(document.currentScript&&document.currentScript.src.split('?')[1])||'';
  let idx=null, loading=null, items=[], sel=-1, opener=null;
  // fold case, accents and curly quotes one UTF-16 unit at a time, so an index into the folded text is an index into the original
  const foldCh=c=>{ const f=c.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[‘’]/g,"'"); return f.length===1?f:(f.length?f[0]:''); };
  const fold=s=>s.replace(/[\s\S]/g,foldCh);
  function msg(t){ res.innerHTML=''; const p=document.createElement('p'); p.className='smsg'; p.textContent=t; res.appendChild(p); }
  function load(){
    if(loading) return loading;
    msg('Loading the index…');
    loading=fetch('search.json'+(ver?'?'+ver:'')).then(r=>{ if(!r.ok) throw new Error(r.status); return r.json(); }).then(d=>{
      idx=d.map(e=>({e, ft:fold(e.t+(e.h?' '+e.h:'')), fp:fold(e.p+' '+e.y+' '+e.stt), fb:fold(e.b)}));
      return idx;
    }).catch(()=>{ idx=null; loading=null; msg('The search index could not be loaded.'); });
    return loading;
  }
  function terms(q){
    const out=[], re=/"([^"]+)"|(\S+)/g; let m;
    while((m=re.exec(q))){ const t=fold(m[1]||m[2]).trim(); if(t) out.push(t); }
    return out;
  }
  function count(h,t){ let n=0,i=0; while((i=h.indexOf(t,i))>=0){ n++; i+=t.length; if(n>=20) break; } return n; }
  function wordStart(h,t){ const i=h.indexOf(t); return i===0 || (i>0 && /[^a-z0-9]/.test(h[i-1])); }
  function score(r,ts,whole){
    let s=0;
    for(const t of ts){
      const inT=r.ft.indexOf(t)>=0, inP=r.fp.indexOf(t)>=0, nB=count(r.fb,t);
      if(!inT&&!inP&&!nB) return 0;
      if(inT){ s+=30; if(wordStart(r.ft,t)) s+=10; if(!r.e.h) s+=15; }
      if(inP){ s+=20; if(!r.e.h) s+=10; }
      if(nB){ s+=5+Math.min(nB,10); if(wordStart(r.fb,t)) s+=3; }
    }
    if(ts.length>1 && whole && (r.ft.indexOf(whole)>=0 || r.fb.indexOf(whole)>=0)) s+=25;
    return s;
  }
  // mark every term occurrence in text (ftext is its folded twin), longest terms first, without overlaps
  function hilite(frag,text,ftext,ts){
    const marks=[];
    for(const t of [...ts].sort((a,b)=>b.length-a.length)){
      let i=0; while((i=ftext.indexOf(t,i))>=0){ const j=i+t.length; if(!marks.some(m=>i<m[1]&&j>m[0])) marks.push([i,j]); i=j; }
    }
    marks.sort((a,b)=>a[0]-b[0]);
    let at=0;
    for(const [i,j] of marks){ if(i>at) frag.appendChild(document.createTextNode(text.slice(at,i))); const m=document.createElement('mark'); m.textContent=text.slice(i,j); frag.appendChild(m); at=j; }
    if(at<text.length) frag.appendChild(document.createTextNode(text.slice(at)));
  }
  function snippet(r,ts){
    const b=r.e.b, fb=r.fb; if(!b) return null;
    let pos=-1; for(const t of ts){ const i=fb.indexOf(t); if(i>=0 && (pos<0||i<pos)) pos=i; }
    let start=0;
    if(pos>60){ start=pos-60; const sp=b.lastIndexOf(' ',start); if(sp>=0 && start-sp<30) start=sp+1; }
    let end=Math.min(b.length,start+180); if(end<b.length){ const sp=b.indexOf(' ',end); if(sp>0 && sp<end+24) end=sp; }
    const frag=document.createDocumentFragment();
    if(start>0) frag.appendChild(document.createTextNode('…'));
    hilite(frag,b.slice(start,end),fb.slice(start,end),ts);
    if(end<b.length) frag.appendChild(document.createTextNode('…'));
    return frag;
  }
  function render(q){
    if(!idx) return;
    const ts=terms(q); res.innerHTML=''; items=[]; sel=-1; input.removeAttribute('aria-activedescendant');
    if(!ts.length){ sn.textContent=''; msg(idx.length+' pages, sections and catalogue entries. Try a name, a place, a shelfmark, a year or a word of the cipher.'); return; }
    const whole=fold(q.replace(/"/g,'')).trim();
    const hits=[]; for(const r of idx){ const s=score(r,ts,whole); if(s) hits.push([s,r]); }
    hits.sort((a,b)=>b[0]-a[0]);
    const per={}, out=[];
    for(const [s,r] of hits){ const k=r.e.u.split('#')[0]; per[k]=(per[k]||0)+1; if(per[k]>3) continue; out.push(r); if(out.length>=40) break; }
    sn.textContent=hits.length?hits.length+(hits.length===1?' match':' matches'):'';
    if(!out.length){ msg('Nothing found for “'+q.trim()+'”.'); return; }
    out.forEach((r,n)=>{
      const e=r.e, a=document.createElement('a'); a.className='sr'; a.href=e.u; a.id='sr-'+n; a.setAttribute('role','option');
      const t=document.createElement('span'); t.className='srt'; hilite(t,e.t,fold(e.t),ts);
      if(e.h){ const h=document.createElement('span'); h.className='sec'; hilite(h,e.h,fold(e.h),ts); t.appendChild(h); }
      a.appendChild(t);
      const m=document.createElement('span'); m.className='srm';
      const lab=document.createElement('span'); lab.textContent=e.p+(e.y?' · '+e.y:''); m.appendChild(lab);
      if(e.stt){ const st=document.createElement('span'); st.className='st '+(e.st||''); st.textContent=e.stt; m.appendChild(st); }
      a.appendChild(m);
      const sp=snippet(r,ts); if(sp){ const p=document.createElement('p'); p.className='srs'; p.appendChild(sp); a.appendChild(p); }
      a.addEventListener('click',()=>close());      // then the browser follows the link
      res.appendChild(a); items.push(a);
    });
  }
  function open(){
    if(!box.hidden){ input.focus(); return; }
    opener=document.activeElement; box.hidden=false; document.documentElement.classList.add('sopen');
    input.focus(); input.select();
    load().then(()=>{ if(idx) render(input.value); });
  }
  function close(){
    if(box.hidden) return;
    box.hidden=true; document.documentElement.classList.remove('sopen');
    if(opener&&opener.focus&&opener!==document.body) opener.focus();
  }
  function move(d){
    if(!items.length) return;
    if(sel>=0) items[sel].classList.remove('on');
    sel=(sel+d+items.length)%items.length;
    items[sel].classList.add('on'); items[sel].scrollIntoView({block:'nearest'}); input.setAttribute('aria-activedescendant',items[sel].id);
  }
  btns.forEach(b=>b.addEventListener('click',open));
  closeBtn.addEventListener('click',close);
  box.addEventListener('click',e=>{ if(e.target===box) close(); });
  input.addEventListener('input',()=>render(input.value));
  input.addEventListener('keydown',e=>{
    if(e.key==='ArrowDown'){ e.preventDefault(); move(1); }
    else if(e.key==='ArrowUp'){ e.preventDefault(); move(-1); }
    else if(e.key==='Enter'){ const a=items[sel>=0?sel:0]; if(a){ e.preventDefault(); a.click(); } }
  });
  document.addEventListener('keydown',e=>{
    if(e.key==='Escape'){ close(); return; }
    const t=e.target, typing=t&&(t.tagName==='INPUT'||t.tagName==='TEXTAREA'||t.tagName==='SELECT'||t.isContentEditable);
    if((e.key==='/' && !typing && !e.ctrlKey && !e.metaKey && !e.altKey) || ((e.key==='k'||e.key==='K') && (e.ctrlKey||e.metaKey))){ e.preventDefault(); open(); }
  });
  // ?q=word on any page but the catalogue (which has its own filter box) opens the search with that query
  const qm=/[?&]q=([^&#]+)/.exec(location.search);
  if(qm && !document.getElementById('q')){ input.value=decodeURIComponent(qm[1].replace(/\+/g,' ')); open(); }
})();
// ledger timeline: drop-in entrance, year cursor, rich tooltip (hover, focus, tap to pin), legend filters
(function(){
  const svg=document.querySelector('svg.tl'); if(!svg) return;
  const wrap=svg.parentNode, tip=wrap.querySelector('.tltip'), cur=svg.querySelector('.cursor'), curYr=cur&&cur.querySelector('.cur-yr');
  const pts=[...svg.querySelectorAll('.pt')];
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(!reduce && 'IntersectionObserver' in window){
    svg.classList.add('pre');
    const io=new IntersectionObserver(es=>{ if(es.some(e=>e.isIntersecting)){ svg.classList.remove('pre'); svg.classList.add('armed'); io.disconnect(); } },{threshold:.3});
    io.observe(svg);
  }
  const esc=s=>(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const clip=(s,n)=>s.length>n? s.slice(0,s.lastIndexOf(' ',n)).replace(/[;,.:]$/,'')+'…' : s;
  let pinned=null, hot=null;
  function show(p){
    const d=p.dataset, col=getComputedStyle(p.querySelector('.core')).fill;
    tip.style.setProperty('--c',col);
    const link=p.tagName.toLowerCase()==='a';
    tip.innerHTML=`<div class="tt-in"><span class="tt-yr">${esc(String(d.year))}</span>`+
      `<span class="tt-pill"><i></i>${esc(d.label)}</span>`+
      `<div class="tt-name">${esc(clip(d.name,110))}</div><div class="tt-date">${esc(d.date)}${d.when?` · ${esc(d.whenhead.toLowerCase())} ${esc(d.when)}`:''}</div>`+
      (d.note?`<p class="tt-note"><b>${esc(d.notehead)}</b>${esc(clip(d.note,190))}</p>`:'')+
      `<div class="tt-go"><span>${link?'Read the write-up →':'Notes only, no page yet'}</span><span>${link&&matchMedia('(hover:none)').matches?'tap again':''}</span></div>`+
      `<span class="tt-arrow"></span></div>`;
    tip.hidden=false;
    if(hot) hot.classList.remove('hot'); hot=p; p.classList.add('hot'); svg.classList.add('dim');
    // place above the dot, clamped inside the wrapper; flip below if no room
    const wr=wrap.getBoundingClientRect(), pr=p.querySelector('.core').getBoundingClientRect();
    const cx=pr.left+pr.width/2-wr.left, tw=tip.offsetWidth, th=tip.offsetHeight;
    let x=Math.max(4,Math.min(wr.width-tw-4,cx-tw/2)), y=pr.top-wr.top-th-14, below=false;
    if(pr.top-th-14<8){ y=pr.bottom-wr.top+14; below=true; }
    tip.classList.toggle('below',below);
    tip.style.setProperty('--tx',x+'px'); tip.style.setProperty('--ty',y+'px');
    tip.style.setProperty('--ax',(cx-x)+'px'); tip.style.setProperty('--ox',(cx-x)+'px');
    requestAnimationFrame(()=>tip.classList.add('show'));
    if(cur){ const c=p.querySelector('.core'); cur.setAttribute('transform',`translate(${c.getAttribute('cx')},0)`); curYr.textContent=d.year; cur.classList.add('on'); }
  }
  function hide(){
    if(pinned) return;
    tip.classList.remove('show'); if(hot) hot.classList.remove('hot'); hot=null; svg.classList.remove('dim'); if(cur) cur.classList.remove('on');
  }
  pts.forEach(p=>{
    p.addEventListener('pointerenter',e=>{ if(e.pointerType!=='touch' && !pinned) show(p); });
    p.addEventListener('pointerleave',e=>{ if(e.pointerType!=='touch') hide(); });
    p.addEventListener('focus',()=>{ if(!pinned) show(p); });
    p.addEventListener('blur',hide);
    p.addEventListener('click',e=>{
      // touch: first tap pins the card, second tap on the same dot follows the link
      if(matchMedia('(hover:none)').matches && pinned!==p){ e.preventDefault(); pinned=null; show(p); pinned=p; tip.classList.add('pinned'); }
    });
  });
  document.addEventListener('click',e=>{ if(pinned && !pinned.contains(e.target) && !tip.contains(e.target)){ pinned=null; tip.classList.remove('pinned'); hide(); } });
  document.addEventListener('keydown',e=>{ if(e.key==='Escape' && hot){ pinned=null; hide(); } });
  window.addEventListener('resize',()=>{ pinned=null; hide(); });
  // legend chips isolate one or more outcomes
  const legend=document.querySelector('.sb-legend');
  if(legend) legend.addEventListener('click',e=>{
    const b=e.target.closest('.lg'); if(!b) return;
    b.setAttribute('aria-pressed', b.getAttribute('aria-pressed')==='true' ? 'false' : 'true');
    const on=[...legend.querySelectorAll('.lg[aria-pressed=true]')].map(x=>x.dataset.cat);
    legend.classList.toggle('filtering',on.length>0);
    pts.forEach(p=>p.classList.toggle('off', on.length>0 && !on.includes(p.dataset.cat)));
  });
})();

/* scoreboard numbers count up from zero when they scroll into view */
(()=>{
  const bs=document.querySelectorAll('.sb-big b'); if(!bs.length) return;
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const run=b=>{
    const t=b.firstChild; if(!t || t.nodeType!==3) return;
    const m=t.textContent.match(/[\d,]+/); if(!m) return;
    const end=+m[0].replace(/,/g,''), comma=m[0].includes(','), fmt=v=>comma?v.toLocaleString('en-US'):String(v);
    // the number counts inside a box held at its final width, so nothing around it moves
    const pre=t.textContent.slice(0,m.index), post=t.textContent.slice(m.index+m[0].length);
    const n=document.createElement('span'); n.className='sb-n'; n.textContent=m[0];
    t.textContent=pre; b.insertBefore(n,t.nextSibling); if(post) b.insertBefore(document.createTextNode(post),n.nextSibling);
    // the display face has proportional figures: reserve the width of the widest digit in every place
    const w=s=>{ n.textContent=s; return n.getBoundingClientRect().width; };
    const wide=[...'0123456789'].reduce((a,d)=>w(d)>w(a)?d:a,'0');
    n.style.minWidth=Math.ceil(w(m[0].replace(/\d/g,wide)))+'px';
    n.textContent=fmt(0);
    const dur=Math.min(2200, 900+end/15); let t0=null;
    const step=now=>{
      if(t0===null) t0=now;
      const k=Math.max(0,Math.min(1,(now-t0)/dur)), e=1-Math.pow(1-k,3);
      n.textContent=fmt(Math.round(end*e));
      if(k<1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if(still || !('IntersectionObserver' in window)) return;
  const io=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ io.unobserve(e.target); run(e.target); } }),{threshold:.6});
  bs.forEach(b=>io.observe(b));
})();
