// shared behaviour: theme, menu, active link, contents strip, card glow, interlinear tiles, queue filter
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
// the Write-ups menu's Latest and By outcome groups live in menu.json, so a new write-up does not rewrite every page
(function(){
  const panel=document.querySelector('.nav .panel.wp'), nav=document.querySelector('.nav'); if(!panel) return;
  let asked=false;
  const fill=()=>{ if(asked) return; asked=true;
    fetch('menu.json').then(r=>r.ok?r.json():Promise.reject()).then(m=>{
      panel.insertAdjacentHTML('afterbegin',m.groups);
      const here=location.href.split('#')[0];
      panel.querySelectorAll('.grp a').forEach(a=>{ if(a.href===here) a.setAttribute('aria-current','page'); });
      const all=panel.querySelector('.foot .all'); if(all) all.textContent=m.all;
    }).catch(()=>{});
  };
  ['pointerover','focusin','touchstart'].forEach(ev=>nav.addEventListener(ev,fill,{once:true,passive:true}));
  if('requestIdleCallback' in window) requestIdleCallback(fill,{timeout:4000}); else setTimeout(fill,2000);
})();
// reading aids: skip link, section menu on long pages, heading links, expand all, cite buttons, long hero summaries on phones
(function(){
  const pageUrl=location.pathname+location.search;
  // a page with <base> (solve, further, 404) would send a bare #anchor to the base address
  if(document.querySelector('base')) document.querySelectorAll('a[href^="#"]').forEach(a=>{ a.href=pageUrl+a.getAttribute('href'); });
  const skip=document.querySelector('.nav .skip'), target=document.getElementById('content');
  if(skip&&target) skip.addEventListener('click',e=>{ e.preventDefault(); target.focus(); });
  const copy=(text,el,done)=>{
    if(!navigator.clipboard) return;
    navigator.clipboard.writeText(text).then(()=>{ const was=el.textContent; el.textContent=done; setTimeout(()=>{ el.textContent=was; },1400); },()=>{});
  };
  document.querySelectorAll('.cite [data-copy]').forEach(b=>b.addEventListener('click',()=>copy(b.dataset.copy,b,'Copied')));
  // each section heading carries a link to itself; a click copies the address
  document.querySelectorAll('main h2[id], main h3[id]').forEach(h=>{
    const a=document.createElement('a'); a.className='hlink'; a.href=pageUrl+'#'+h.id; a.textContent='#';
    a.setAttribute('aria-label','Copy a link to this section'); a.title='Copy a link to this section';
    a.addEventListener('click',e=>{ e.preventDefault(); history.replaceState(null,'',a.href); copy(a.href,a,'copied'); });
    h.appendChild(a);
  });
  // expand all: the collapsed texts of a page, also opened for printing
  const folds=[...document.querySelectorAll('main details')].filter(d=>!d.closest('.cfilters')&&!d.classList.contains('cite'));
  const toggles=[];
  const syncToggles=()=>{ const open=folds.every(d=>d.open); toggles.forEach(b=>{ b.textContent=open?'Collapse all':'Expand all '+folds.length; b.setAttribute('aria-pressed',open?'true':'false'); }); };
  const makeToggle=()=>{ const b=document.createElement('button'); b.type='button'; b.className='expandall'; toggles.push(b);
    b.addEventListener('click',()=>{ const open=!folds.every(d=>d.open); folds.forEach(d=>{ d.open=open; }); syncToggles(); }); return b; };
  if(folds.length>=3){
    const texts=document.getElementById('texts');
    if(texts){ const lead=texts.nextElementSibling&&texts.nextElementSibling.tagName==='P'?texts.nextElementSibling:texts; lead.after(makeToggle()); }
    folds.forEach(d=>d.addEventListener('toggle',syncToggles));
    let reopen=[];
    addEventListener('beforeprint',()=>{ reopen=folds.filter(d=>!d.open); reopen.forEach(d=>{ d.open=true; }); });
    addEventListener('afterprint',()=>{ reopen.forEach(d=>{ d.open=false; }); });
  }
  // sections: a rail beside the text on a wide screen, a button with a list on anything narrower
  const toc=document.querySelector('main .toc');
  const links=toc?[...toc.querySelectorAll('a')]:[];
  if(links.length>=3 && document.documentElement.scrollHeight>innerHeight*3 && 'IntersectionObserver' in window){
    const box=document.createElement('aside'); box.className='secnav'; box.setAttribute('aria-label','Sections');
    const btn=document.createElement('button'); btn.type='button'; btn.className='secbtn'; btn.textContent='Sections'; btn.setAttribute('aria-expanded','false'); btn.setAttribute('aria-controls','seclist');
    const list=document.createElement('nav'); list.className='seclist'; list.id='seclist'; list.setAttribute('aria-label','On this page');
    const head=document.createElement('p'); head.className='sechead'; head.textContent='On this page'; list.appendChild(head);
    const own=new Map();
    links.forEach(l=>{ const a=l.cloneNode(true); a.classList.remove('on'); list.appendChild(a); own.set(l.getAttribute('href').split('#').pop(),a); });
    const cite=document.getElementById('cite');
    if(cite){ const a=document.createElement('a'); a.href=pageUrl+'#cite'; a.textContent='Cite this page'; a.className='seccite'; a.addEventListener('click',()=>{ cite.open=true; }); list.appendChild(a); }
    if(folds.length>=3){ const t=document.createElement('div'); t.className='sectools'; t.appendChild(makeToggle()); list.appendChild(t); }
    box.append(list,btn); document.body.appendChild(box); document.body.classList.add('has-secnav');
    const setOpen=on=>{ box.classList.toggle('open',on); btn.setAttribute('aria-expanded',on?'true':'false'); };
    btn.addEventListener('click',e=>{ e.stopPropagation(); setOpen(!box.classList.contains('open')); });
    list.addEventListener('click',e=>{ if(e.target.closest('a')) setOpen(false); });
    document.addEventListener('click',e=>{ if(!box.contains(e.target)) setOpen(false); });
    document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&box.classList.contains('open')){ setOpen(false); btn.focus(); } });
    new IntersectionObserver(es=>{ box.classList.toggle('past',!es[es.length-1].isIntersecting); }).observe(toc);
    // the section in view: the last heading above the upper third of the window, so a jump lands on the right one too
    const heads=[...own.keys()].map(id=>[id,document.getElementById(id)]).filter(x=>x[1]);
    let tick=0, shown=null;
    const spot=()=>{ tick=0; let cur=null;
      for(const [id,h] of heads){ if(h.getBoundingClientRect().top<=innerHeight*.3) cur=id; else if(cur) break; }
      if(cur===shown) return; shown=cur;
      own.forEach((a,id)=>a.classList.toggle('on',id===cur));
      const a=own.get(cur); if(!a) return;
      const r=a.getBoundingClientRect(), R=list.getBoundingClientRect(); if(R.height&&(r.top<R.top||r.bottom>R.bottom)) list.scrollTop+=r.top-R.top-R.height/2; };
    addEventListener('scroll',()=>{ if(!tick) tick=setTimeout(spot,80); },{passive:true}); spot();
  }
  syncToggles();
  // phones: a long hero summary folds to a few lines, so the page itself comes sooner
  if(matchMedia('(max-width:760px)').matches){
    document.querySelectorAll('section.hero:not(.solve) > p.sub').forEach(p=>{
      const line=parseFloat(getComputedStyle(p).lineHeight)||26;
      if(p.offsetHeight<line*6.5) return;
      p.classList.add('folded');
      const b=document.createElement('button'); b.type='button'; b.className='subless'; b.textContent='More'; b.setAttribute('aria-expanded','false');
      b.addEventListener('click',()=>{ const on=p.classList.toggle('folded'); b.textContent=on?'More':'Less'; b.setAttribute('aria-expanded',on?'false':'true'); });
      p.after(b);
    });
  }
})();
// 'show more' blocks on the home page
// .showmore reveals its hidden box; with data-step it reveals the box's <li> a batch at a time, then offers to fold them back
document.querySelectorAll('.showmore').forEach(b=>b.addEventListener('click',()=>{
  const box=b.previousElementSibling, step=+b.dataset.step||0;
  if(!step){ const open=box.hasAttribute('hidden'); if(open) box.removeAttribute('hidden'); else box.setAttribute('hidden',''); b.textContent = open ? 'Show fewer' : b.dataset.label || b.textContent; return; }
  const items=[...box.querySelectorAll('li')], shown=items.filter(li=>!li.hidden).length;
  if(!box.hasAttribute('hidden') && shown>=items.length){ box.setAttribute('hidden',''); items.forEach(li=>li.hidden=false); b.textContent=b.dataset.label; b.scrollIntoView({block:'center'}); return; }
  const first=box.hasAttribute('hidden'); if(first){ items.forEach(li=>li.hidden=true); box.removeAttribute('hidden'); }
  const upto=(first?0:shown)+step; items.forEach((li,i)=>{ if(i<upto) li.hidden=false; });
  const left=items.length-Math.min(upto,items.length);
  b.textContent = left ? `Show ${Math.min(step,left)} more (${left} left)` : 'Show fewer';
}));
document.querySelectorAll('.showmore').forEach(b=>b.dataset.label=b.textContent);
// the nav stickers hang below the bar only at the top of the page; once scrolled they tuck into it (style.css)
(function(){
  const nav=document.querySelector('.nav'); if(!nav) return;
  const f=()=>nav.classList.toggle('scrolled',scrollY>24);
  addEventListener('scroll',f,{passive:true}); f();
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
// write-ups index: method / extent / language / century / where dropdowns, text search, state in the hash
// (writeups.html#kind=ct&q=rome). Same toolbar as catalogue.html: each chip counts the entries it would show given
// every other facet and the search, empty chips dim, each dropdown button names what is chosen in it.
(function(){
  const items=[...document.querySelectorAll('ul.wl li')]; if(!items.length) return;
  const chips=[...document.querySelectorAll('.cfilters .chip[data-facet]')], q=document.getElementById('wq'),
        count=document.getElementById('wcount')||{}, reset=document.getElementById('wreset'),
        dds=[...document.querySelectorAll('.cfilters details.dd')];
  const state={f:{}, q:''};
  const vals=(li,k)=>(li.dataset[k]||'').split(' ').filter(Boolean);   // lang and by hold several space-separated ids
  dds.forEach(d=>d.addEventListener('toggle',()=>{ if(!d.open) return; dds.forEach(o=>{ if(o!==d) o.open=false; });
    const p=d.querySelector('.pop'); p.style.left=''; p.style.right='';
    if(p.getBoundingClientRect().right>document.documentElement.clientWidth-8){ p.style.left='auto'; p.style.right='0'; } }));
  document.addEventListener('click',ev=>{ if(!ev.target.closest('.cfilters details.dd')) dds.forEach(d=>d.open=false); });
  document.addEventListener('keydown',ev=>{ if(ev.key==='Escape') dds.forEach(d=>{ if(d.open){ d.open=false; d.querySelector('summary').focus(); } }); });
  function parse(){
    state.f={}; state.q='';
    location.hash.slice(1).split('&').forEach(kv=>{ if(!kv) return; const i=kv.indexOf('='); const k=i<0?kv:kv.slice(0,i), v=i<0?'':decodeURIComponent(kv.slice(i+1));
      if(k==='q') state.q=v; else if(k) state.f[k]=v.split(',').filter(Boolean); });
  }
  function match(li,needle,skip){
    if(needle && !(li.dataset.q||'').includes(needle)) return false;
    for(const k in state.f){ const vs=state.f[k]; if(k===skip || !vs.length) continue; const d=vals(li,k); if(!vs.some(v=>d.includes(v))) return false; }
    return true;
  }
  function apply(remember){
    if(q && q.value!==state.q) q.value=state.q;
    const needle=state.q.trim().toLowerCase(); let n=0;
    items.forEach(li=>{ const ok=match(li,needle); li.hidden=!ok; if(ok) n++; });
    document.querySelectorAll('.wsec').forEach(s=>{ s.hidden=![...s.querySelectorAll('li')].some(li=>!li.hidden); });
    const c={}; new Set(chips.map(b=>b.dataset.facet)).forEach(k=>items.forEach(li=>{ if(match(li,needle,k)) vals(li,k).forEach(v=>{ c[k+'|'+v]=(c[k+'|'+v]||0)+1; }); }));
    chips.forEach(b=>{ const on=(state.f[b.dataset.facet]||[]).includes(b.dataset.val), x=c[b.dataset.facet+'|'+b.dataset.val]||0;
      b.setAttribute('aria-pressed',on?'true':'false'); b.querySelector('.n').textContent=x; b.classList.toggle('z',!x&&!on); });
    dds.forEach(d=>{ const k=d.dataset.dd, on=(state.f[k]||[]).map(v=>{ const b=d.querySelector(`.chip[data-facet="${k}"][data-val="${CSS.escape(v)}"]`); return b?b.firstChild.textContent:v; });
      d.querySelector('.dv').textContent=on.length?': '+(on.length>2?on.length+' chosen':on.join(', ')):''; d.classList.toggle('act',on.length>0); });
    count.textContent = n===items.length ? 'All '+n+' entries' : n+' of '+items.length+' entries';
    if((state.f.by||[]).length){ let nm={}; try{ nm=JSON.parse(count.dataset.names||'{}'); }catch(e){}
      count.textContent += ', credited to '+state.f.by.map(v=>nm[v]||v).join(' or '); }
    let nf=0; for(const k in state.f) nf+=state.f[k].length;
    if(reset){ reset.hidden=!(nf||needle); reset.textContent=nf?'clear '+nf+' filter'+(nf>1?'s':''):'clear search'; }
    if(remember){ const parts=[]; for(const k in state.f) if(state.f[k].length) parts.push(k+'='+state.f[k].map(encodeURIComponent).join(','));
      if(needle) parts.push('q='+encodeURIComponent(state.q.trim()));
      try{ history.replaceState(null,'', parts.length ? '#'+parts.join('&') : location.pathname+location.search); }catch(e){} }
  }
  chips.forEach(c=>c.addEventListener('click',()=>{ const k=c.dataset.facet, a=state.f[k]=state.f[k]||[], i=a.indexOf(c.dataset.val); if(i<0) a.push(c.dataset.val); else a.splice(i,1); if(!a.length) delete state.f[k]; apply(true); }));
  if(q) q.addEventListener('input',()=>{ state.q=q.value; apply(true); });
  if(reset) reset.addEventListener('click',()=>{ state.f={}; state.q=''; apply(true); });
  window.addEventListener('hashchange',()=>{ parse(); apply(false); });
  parse();
  // arriving with no hash: start on complete + partial, hiding the "text not obtained" rows (a hash, even #kind=ct, overrides)
  if(!location.hash){ state.f.extent=['complete','partial']; apply(true); } else apply(false);
})();
// site search: a palette opened from the nav button, "/" or Ctrl+K. The index (search.json, one entry per page,
// per h2 section and per catalogue entry) is fetched the first time the box opens; matching is accent- and
// case-insensitive, every term must occur, "quoted phrases" are one term, and results link straight to the section.
(function(){
  const box=document.getElementById('search'), input=document.getElementById('sq'), res=document.getElementById('sres'), sn=document.getElementById('sn');
  if(!box||!input||!res) return;
  const btns=document.querySelectorAll('.searchbtn'), closeBtn=box.querySelector('.sclose');
  const ver=(document.currentScript&&document.currentScript.src.split('?')[1])||'';
  let idx=null, loading=null, byU=new Map(), nextShard=0, shardBusy=false, fullAsked=false, shardFail=false, items=[], sel=-1, opener=null, typing=0;
  const SHARDS=16;      // _build_site.py has the same number
  // fold case, accents and curly quotes one UTF-16 unit at a time, so an index into the folded text is an index into the original
  const foldCh=c=>{ const f=c.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[‘’]/g,"'"); return f.length===1?f:(f.length?f[0]:''); };
  const fold=s=>s.replace(/[^\x00-\x40\x5b-\x7f]/g,foldCh);     // plain lowercase ASCII is most of it, and stays as it is
  function msg(t){ res.innerHTML=''; const p=document.createElement('p'); p.className='smsg'; p.textContent=t; res.appendChild(p); }
  function load(){
    if(loading) return loading;
    msg('Loading the index…');
    loading=fetch('search-t.json'+(ver?'?'+ver:'')).then(r=>{ if(!r.ok) throw new Error(r.status); return r.json(); }).then(d=>{
      idx=d.map(e=>(e.b='', {e, ft:fold(e.t+(e.h?' '+e.h:'')), fp:fold(e.p+' '+e.y+' '+e.stt), fb:''}));
      idx.forEach(r=>byU.set(r.e.u,r));
      return idx;
    }).catch(()=>{ idx=null; loading=null; msg('The search index could not be loaded.'); });
    return loading;
  }
  // the page and section texts are the big part of the index: fetched shard by shard after the first query, the results
  // drawn again as each arrives (titles, places and years match in the meantime). Closing the box stops the fetching; a
  // reader on a slow or data-saving connection is asked first.
  const slowNet=()=>{ const c=navigator.connection; return !!c&&(c.saveData||/2g/.test(c.effectiveType||'')); };
  const bodiesDone=()=>nextShard>=SHARDS||shardFail;
  async function loadBodies(){
    if(!idx||shardBusy||bodiesDone()||(slowNet()&&!fullAsked)) return;
    shardBusy=true;
    try{
      while(nextShard<SHARDS&&!box.hidden){
        const r=await fetch('search-b/'+String(nextShard).padStart(2,'0')+'.json'+(ver?'?'+ver:''));
        if(!r.ok) throw new Error(r.status);
        const rows=await r.json();
        let t=performance.now();
        for(const [u,b] of rows){
          const x=byU.get(u); if(x){ x.e.b=b; x.fb=fold(b); }
          if(performance.now()-t>12){ await new Promise(ok=>setTimeout(ok)); t=performance.now(); }
        }
        nextShard++;
        if(!box.hidden&&sel<0) render(input.value); else progress();
      }
    }catch(e){ shardFail=true; }
    shardBusy=false;
    if(!box.hidden&&sel<0&&bodiesDone()) render(input.value);
  }
  let nHits='';
  function progress(){ sn.textContent=nHits+(bodiesDone()||!nextShard&&!shardBusy?'':(nHits?' · ':'')+'searching full text '+Math.round(nextShard/SHARDS*100)+'%')+(shardFail?(nHits?' · ':'')+'full text not available':''); }
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
    nHits='';
    if(!ts.length){ sn.textContent=''; msg(idx.length+' pages, sections and catalogue entries. Try a name, a place, a shelfmark, a year or a word of the cipher.'); return; }
    const whole=fold(q.replace(/"/g,'')).trim();
    const hits=[]; for(const r of idx){ const s=score(r,ts,whole); if(s) hits.push([s,r]); }
    hits.sort((a,b)=>b[0]-a[0]);
    const per={}, out=[];
    for(const [s,r] of hits){ const k=r.e.u.split('#')[0]; per[k]=(per[k]||0)+1; if(per[k]>3) continue; out.push(r); if(out.length>=40) break; }
    nHits=hits.length?hits.length+(hits.length===1?' match':' matches'):''; progress();
    if(!out.length&&bodiesDone()){ msg('Nothing found for “'+q.trim()+'”.'); return; }
    if(!out.length&&!slowNet()){ msg('Nothing in the titles; still searching the full text…'); return; }
    if(slowNet()&&!fullAsked&&!bodiesDone()){ const b=document.createElement('button'); b.type='button'; b.className='sfull'; b.textContent='Also search the full text (about 8 MB)';
      b.addEventListener('click',()=>{ fullAsked=true; b.remove(); loadBodies(); }); if(!out.length) msg('Nothing in the titles.'); res.appendChild(b); }
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
    load().then(()=>{ if(idx){ if(input.value.trim().length>1) loadBodies(); render(input.value); } });
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
  input.addEventListener('input',()=>{ clearTimeout(typing); typing=setTimeout(()=>{ if(input.value.trim().length>1) loadBodies(); render(input.value); },nextShard?110:30); });
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
  let pinned=null, hot=null, TL=[];
  let asked=false;
  const load=()=>{ if(asked) return; asked=true; fetch('timeline.json').then(r=>r.json()).then(t=>{ TL=t; if(hot) show(hot); }).catch(()=>{}); };
  svg.addEventListener('pointerover',load,{once:true}); svg.addEventListener('focusin',load,{once:true}); svg.addEventListener('touchstart',load,{once:true,passive:true});
  function show(p){
    const d=Object.assign({},p.dataset,TL[p.dataset.i]||{label:'',name:'',date:''}), col=getComputedStyle(p.querySelector('.core')).fill;
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
    // the kept dots fall to the axis: re-stack them in the lowest free lanes (same greedy rule as _build_stats.py)
    const lanes=[];
    pts.map(p=>{ const c=p.querySelector('.core'); return {p, x:+c.getAttribute('cx'), y:+c.getAttribute('cy'), base:+c.getAttribute('cy')+parseFloat(p.style.getPropertyValue('--dy'))}; })
      .sort((a,b)=>a.x-b.x).forEach(d=>{
        d.p.style.setProperty('--wave',(d.x/1000*260|0)+'ms');
        if(!on.length || d.p.classList.contains('off')){ d.p.style.removeProperty('--fall'); return; }
        let li=lanes.findIndex(last=>d.x-last>=11); if(li<0){ li=lanes.length; lanes.push(0); } lanes[li]=d.x;
        d.p.style.setProperty('--fall',(d.base-9-li*13-d.y)+'px');
      });
  });
})();

// Cursor trail: faint cipher letters drift up and fade behind the pointer.
(function(){
  if(matchMedia('(prefers-reduced-motion: reduce)').matches || !matchMedia('(pointer: fine)').matches) return;
  const glyphs='ABCDEFGHIKLMNOPQRSTVXZ0123456789+·∆⊕☉♃♀Ꝑꝯ§';
  let last=0, lx=0, ly=0;
  addEventListener('pointermove', e=>{
    const now=performance.now(), dx=e.clientX-lx, dy=e.clientY-ly;
    if(now-last<45 || dx*dx+dy*dy<400) return;
    last=now; lx=e.clientX; ly=e.clientY;
    const s=document.createElement('span');
    s.className='cipher-trail'; s.setAttribute('aria-hidden','true');
    s.textContent=glyphs[Math.random()*glyphs.length|0];
    s.style.left=(e.clientX+(Math.random()*24-12))+'px';
    s.style.top=(e.clientY+(Math.random()*24-12))+'px';
    s.style.setProperty('--rot',(Math.random()*40-20)+'deg');
    document.body.appendChild(s);
    s.addEventListener('animationend',()=>s.remove());
  },{passive:true});
})();
