// The Cipher Atlas: atlas.json (places, letters), pages.json (labels, methods, correspondents), atlas-open.json (the unread
// layer), atlas_stories.json (chapters) and atlas/<slug>.json (what a letter says, fetched when it opens), on Natural Earth land.
// One state S drives the routes, the cities, the panel and the URL; a line is one route, its width the letters on it.
(async()=>{
  const root=document.getElementById('atlas'); if(!root || !window.d3) return;
  const $=id=>document.getElementById(id);
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches, phone=matchMedia('(max-width:860px)');
  const LAND='https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/';
  const [atlas,pages,open,stories,land50]=await Promise.all([
    fetch('atlas.json').then(r=>r.json()), fetch('pages.json').then(r=>r.json()).catch(()=>[]),
    fetch('atlas-open.json').then(r=>r.json()).catch(()=>({places:{},letters:[]})),
    fetch('atlas_stories.json').then(r=>r.json()).catch(()=>[]),
    fetch(LAND+'land-50m.json').then(r=>r.json())]);
  const page=Object.fromEntries(pages.map(p=>[p.slug,p]));
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const plural=(n,w)=>`${n} ${w}${n===1?'':'s'}`;
  const span=(a,b)=>a===b?String(a):`${a}–${b}`;

  // how the text was obtained (docs/_methods.py), in the five families the map can colour
  const FAM={ct:'rebuilt',extpt:'rebuilt',adjpt:'rebuilt',extkey:'applied',known:'applied',deciph:'prior',notsolved:'none',na:'na'};
  const FAMS={rebuilt:['key recovered','green'],applied:['existing key applied','blue'],prior:['existing decipherment','violet'],none:['not solved','red'],na:['not applicable','muted']};

  // ---------------------------------------------------------------- the letters and their routes
  const letters=atlas.letters.map((l,i)=>({...l,i,pg:page[l.slug]})).filter(l=>atlas.places[l.from]&&atlas.places[l.to]).sort((x,y)=>x.year-y.year);
  const byRoute=new Map(); const label=l=>l.pg?l.pg.label:l.label;
  for(const l of letters){
    l.who=l.who||(l.pg&&l.pg.people)||[]; l.fam=FAM[l.pg&&l.pg.m]||'na'; l.route=l.from+' → '+l.to; l.key=l.slug+'~'+l.doc;
    if(!byRoute.has(l.route)) byRoute.set(l.route,{id:l.route,from:l.from,to:l.to,all:[],v:[],pc:-1,pf:''});
    byRoute.get(l.route).all.push(l);
  }
  const routes=[...byRoute.values()].sort((a,b)=>b.all.length-a.all.length);
  routes.forEach((r,i)=>{ r.top=i<12; r.all.forEach(l=>{ l.r=r; }); });
  const letterOf=k=>letters.find(l=>l.key===k);
  const y0All=Math.floor(letters[0].year), y1All=Math.floor(letters.at(-1).year);
  const beyond=n=>{ const c=atlas.places[n]||open.places[n]; return c[1]<-12||c[1]>45||c[0]<34||c[0]>64; };
  routes.forEach(r=>{ r.far=beyond(r.from)||beyond(r.to); });

  // ---------------------------------------------------------------- the state
  const S={T:null,W:10,range:null,who:[],city:null,route:null,slugs:null,slugPage:null,story:null,hide:new Set(),unread:true,view:'europe',tab:'stories',cover:true};
  const stack=[];        // the panel's sheet: {k:'list'}, {k:'letter',l,ctx}, {k:'story',s}, {k:'unread',at}
  let playing=false;
  const hiNow=()=>playing?S.T:Math.floor(S.T)+1;
  const range=()=>{
    if(S.range) return [S.range[0],S.range[1]+1];
    if(S.T==null) return [-Infinity,Infinity];
    const hi=hiNow(); return [S.W?hi-S.W:-Infinity,hi];
  };
  const pk=p=>p.img||'n:'+p.name;
  const matchWho=l=>S.who.every(k=>l.who.some(p=>pk(p)===k));
  const matches=(l,{route=true}={})=>matchWho(l) && (!S.slugs||S.slugs.has(l.slug)) && (!S.city||l.from===S.city||l.to===S.city) && (!route||!S.route||l.route===S.route);
  const filtered=()=>S.who.length||S.city||S.route||S.slugs;

  // ---------------------------------------------------------------- the map
  let W=1200,H=700,proj,path,K=1;
  const svg=d3.select(root).insert('svg',':first-child').attr('role','img').attr('aria-label','Map of the routes of the ciphered letters');
  const defs=svg.append('defs'); defs.append('clipPath').attr('id','pinclip').append('circle').attr('r',13);
  const sea=svg.append('rect').attr('class','sea');
  const g=svg.append('g');
  const pGrat=g.append('path').attr('class','grat'), pLand=g.append('path').attr('class','land');
  const gRoutes=g.append('g'), gFlow=g.append('g'), gHits=g.append('g'), gRings=g.append('g'), gCities=g.append('g'), gPulse=g.append('g'), gPins=g.append('g');
  let landNow=topojson.feature(land50,land50.objects.land), landEurope=landNow, landWorld=null;
  const EUROPE=[[-10,35.5],[36,36],[30,61],[-8,58]], CORE=[[-7,37],[21,37],[21,58],[-6,56]], WORLD=[[-125,-36],[150,-36],[150,68],[-125,68]];
  const P=name=>{ const c=atlas.places[name]||open.places[name]; return c?proj([c[1],c[0]]):null; };

  const rEls=gRoutes.selectAll('path').data(routes).join('path').attr('class','rt').attr('vector-effect','non-scaling-stroke').each(function(r){ r.el=this; });
  const fEls=gFlow.selectAll('path').data(routes).join('path').attr('class','flow').attr('vector-effect','non-scaling-stroke').each(function(r){ r.fl=this; });
  const hEls=gHits.selectAll('path').data(routes).join('path').attr('class','rt hit').attr('vector-effect','non-scaling-stroke').each(function(r){ r.hit=this; });
  const curve=r=>{ const [x0,y0]=r.a,[x1,y1]=r.b, dx=x1-x0, dy=y1-y0, d=Math.hypot(dx,dy)||1;
    if(d<3) return `M${x0},${y0}m-4,0a4,4 0 1,0 8,0a4,4 0 1,0 -8,0`;
    const k=Math.min(.3,34/d+.1), mx=(x0+x1)/2-dy*k, my=(y0+y1)/2+dx*k; return `M${x0},${y0}Q${mx},${my} ${x1},${y1}`; };

  // cities: drawn from the first letter on, labelled by what they carry now
  const cnt=new Map(); letters.forEach(l=>{ for(const n of [l.from,l.to]) { if(!cnt.has(n)) cnt.set(n,{n,first:l.year,c:0,v:0}); cnt.get(n).c++; } });
  const cities=[...cnt.values()].sort((a,b)=>a.c-b.c);   // the busiest last, so their labels stay on top
  const radius=v=>2+Math.min(phone.matches?7:10,Math.sqrt(v)*(phone.matches?.65:.85));
  const cg=gCities.selectAll('g').data(cities).join('g').attr('class','city').each(function(d){ d.el=this; });
  cg.append('circle').attr('class','hitc'); cg.append('circle').attr('class','cdot'); cg.append('text').attr('dy','.35em').text(d=>d.n);
  cg.append('title').text(d=>`${d.n}: ${plural(d.c,'letter')}`);

  // the unread layer: open catalogue letters at their place
  const openBy=d3.group(open.letters,o=>o.at);
  const rings=[...openBy.keys()].map(n=>({n,all:openBy.get(n),v:0}));
  const rg=gRings.selectAll('circle').data(rings).join('circle').attr('class','ring').each(function(d){ d.el=this; });
  rg.append('title').text(d=>`${d.n}: ${plural(d.all.length,'letter')} with no known decipherment`);

  function layout(){
    W=root.clientWidth||1200; H=root.clientHeight||700;
    const world=S.view==='world', pts=world?WORLD:(W/H<1.1?CORE:EUROPE);
    proj=(world?d3.geoNaturalEarth1().rotate([-12,0]):d3.geoConicConformal().rotate([-14,0]).parallels([38,58]))
      .fitExtent([[10,world?24:44],[W-10,H-10]],{type:'MultiPoint',coordinates:pts});
    path=d3.geoPath(proj);
    svg.attr('viewBox',`0 0 ${W} ${H}`); sea.attr('width',W).attr('height',H);
    pGrat.attr('d',path(d3.geoGraticule10())); pLand.attr('d',path(landNow));
    for(const r of routes){ r.a=P(r.from); r.b=P(r.to); const d=curve(r); r.el.setAttribute('d',d); r.fl.setAttribute('d',d); r.hit.setAttribute('d',d); }
    cities.forEach(d=>{ d.p=P(d.n); });
    rings.forEach(d=>{ d.p=P(d.n); d.el.setAttribute('cx',d.p[0]); d.el.setAttribute('cy',d.p[1]); });
    placeMarks();
  }
  const placeMarks=()=>{ for(const d of cities) d.el.setAttribute('transform',`translate(${d.p}) scale(${1/K})`); placePins(); };

  // zoom and pan: one finger on a phone scrolls the page, two move the map. Past Europe's limit the map becomes the world
  // map: this projection pulls anything far from Europe out of place
  const OUT={europe:.5,world:.6};
  const zoom=d3.zoom().scaleExtent([OUT.europe,14])
    .filter(e=>e.type==='touchstart'?e.touches.length>1:(!e.ctrlKey||e.type==='wheel')&&!e.button)
    .on('zoom',e=>{ K=e.transform.k; g.attr('transform',e.transform); placeMarks(); })
    .on('end',()=>{ labels();
      if(S.view==='europe'&&K<=OUT.europe*1.01){ leaveCover(); setView('world').then(()=>{ update(); writeHash(); }); } });
  svg.call(zoom).on('dblclick.zoom',null);
  const toFrame=t=>{ (still?svg:svg.transition().duration(800)).call(zoom.transform,t); };
  const resetZoom=()=>toFrame(d3.zoomIdentity);
  const seenH=()=>phone.matches&&stack.length?Math.max(200,H-.12*innerHeight):H;   // on a phone the sheet covers the foot of the map
  function focus(ls){
    if(!ls.length) return resetZoom();
    const H=seenH();
    const pts=ls.flatMap(l=>[l.r.a,l.r.b]), xs=pts.map(p=>p[0]), ys=pts.map(p=>p[1]);
    const x0=Math.min(...xs),x1=Math.max(...xs),y0=Math.min(...ys),y1=Math.max(...ys);
    const k=Math.max(1,Math.min(5,.72*W/(x1-x0||1),.68*H/(y1-y0||1)));
    toFrame(d3.zoomIdentity.translate(W/2-k*(x0+x1)/2,H/2-k*(y0+y1)/2+10).scale(k));
  }
  $('azin').addEventListener('click',()=>svg.transition().duration(still?0:250).call(zoom.scaleBy,1.6));
  $('azout').addEventListener('click',()=>svg.transition().duration(still?0:250).call(zoom.scaleBy,1/1.6));
  $('azreset').addEventListener('click',resetZoom);

  async function setView(v){
    if(S.view===v) return; S.view=v; labelKey=''; zoom.scaleExtent([OUT[v],14]);
    if(v==='world'&&!landWorld){ try{ const w=await fetch(LAND+'land-110m.json').then(r=>r.json()); landWorld=topojson.feature(w,w.objects.land); }catch(e){ landWorld=landEurope; } }
    landNow=v==='world'?landWorld:landEurope; K=1; svg.call(zoom.transform,d3.zoomIdentity); layout(); update();
  }

  // ---------------------------------------------------------------- legend, timeline
  const fams=[...Object.keys(FAMS)].filter(f=>letters.some(l=>l.fam===f));
  $('alegend').innerHTML=fams.map(f=>`<button type="button" data-f="${f}" aria-pressed="true"><i style="background:var(--${FAMS[f][1]})"></i>${FAMS[f][0]}</button>`).join('')+
    `<button type="button" data-f="unread" aria-pressed="true" class="un"><i></i><span id="aunreadn">still unread</span></button>`;
  $('alegend').addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; const f=b.dataset.f;
    if(f==='unread'){ S.unread=!S.unread; b.setAttribute('aria-pressed',S.unread); }
    else { S.hide.has(f)?S.hide.delete(f):S.hide.add(f); b.setAttribute('aria-pressed',!S.hide.has(f)); }
    leaveCover(); changed(); });

  const YMIN=1395,YMAX=1945, hist=d3.select('#ahist').attr('viewBox',`0 0 ${YMAX-YMIN} 38`);
  const bins=d3.range(1390,1950,10).map(y=>({y,n:letters.filter(l=>l.year>=y&&l.year<y+10).length}));
  const hy=d3.scaleSqrt().domain([0,d3.max(bins,b=>b.n)]).range([0,36]);
  const bars=hist.selectAll('rect').data(bins).join('rect').attr('x',b=>Math.max(0,b.y-YMIN)+.5).attr('width',9).attr('y',b=>38-hy(b.n)).attr('height',b=>hy(b.n));
  $('aticks').innerHTML=[1400,1500,1600,1700,1800,1900].map(y=>`<span style="left:${(y-YMIN)/(YMAX-YMIN)*100}%">${y}</span>`).join('');

  // ---------------------------------------------------------------- drawing
  const tip=$('atip'), slider=$('aslider'), yearEl=$('ayear'), countEl=$('acount'), feed=$('afeed'), worldBtn=$('aworld');
  let labelKey='';
  function update(){
    const [lo,hi]=range(); let n=0;
    routes.forEach(r=>{ r.v.length=0; }); cities.forEach(d=>{ d.v=0; d.was=false; });
    for(const l of letters){
      const c0=cnt.get(l.from), c1=cnt.get(l.to);
      if(l.year<lo&&matches(l)&&!S.hide.has(l.fam)){ c0.was=c1.was=true; }
      if(l.year>=lo&&l.year<hi&&!S.hide.has(l.fam)&&matches(l)){ l.r.v.push(l); c0.v++; c1.v++; n++; }
    }
    const live=routes.filter(r=>r.v.length).sort((a,b)=>b.v.length-a.v.length), flow=new Set(still?[]:live.slice(0,28));
    const open1=stack.at(-1), hot=open1&&open1.k==='letter'?open1.l.r:null;
    if(hot&&!still) flow.add(hot);
    for(const r of routes){
      const c=r.v.length;
      if(c!==r.pc){ const w=c?Math.min(9,1+Math.sqrt(c)*.85):0;
        r.el.style.strokeWidth=w; r.fl.style.strokeWidth=Math.max(2.2,w*.7); r.hit.style.display=c?'':'none'; r.el.classList.toggle('off',!c); r.pc=c; }
      if(c){ const tally={}; for(const l of r.v) tally[l.fam]=(tally[l.fam]||0)+1;
        const f=Object.keys(tally).sort((a,b)=>tally[b]-tally[a])[0];
        if(f!==r.pf){ r.el.setAttribute('class',`rt ${f}${r.top?' top':''}${c?'':' off'}`); r.fl.setAttribute('class','flow '+f); r.pf=f; } }
      r.fl.style.display=c&&flow.has(r)?'':'none';
      r.el.classList.toggle('hot',r===hot);
    }
    svg.classed('cover',S.cover).classed('held',!!hot);
    // cities and rings
    for(const d of cities){
      const on=d.v>0, here=S.city===d.n, shown=on||d.was||here;
      d.el.style.display=shown?'':'none'; d.el.classList.toggle('sel',here); d.el.classList.toggle('faint',!on);
      if(shown){ const rad=on?radius(d.v):1.3; d.el.children[1].setAttribute('r',rad); d.el.children[0].setAttribute('r',Math.max(phone.matches?13:8,rad+5)); }
    }
    labels();
    const showRings=S.unread&&!S.who.length&&!S.route&&!S.slugs; let un=0;
    for(const d of rings){ d.v=showRings&&(!S.city||S.city===d.n)?d.all.filter(o=>o.y>=lo&&o.y<hi).length:0; un+=d.v;
      d.el.style.display=d.v?'':'none'; if(d.v) d.el.setAttribute('r',2.4+Math.sqrt(d.v)*1.25); }
    $('aunreadn').textContent=`still unread${un?' ('+un+')':''}`;
    // the labels above the timeline
    const rs=live.length, far=S.view==='europe'?live.reduce((a,r)=>a+(r.far?r.v.length:0),0):0;
    if(S.range) yearEl.textContent=span(S.range[0],S.range[1]);
    else if(S.T==null) yearEl.textContent=`${y0All}–${y1All}`;
    else yearEl.textContent=Math.floor(S.T);
    const within=S.T!=null&&!S.range&&S.W?` · ${Math.floor(lo)}–${Math.ceil(hi)-1}`:'';
    countEl.textContent=`${plural(n,'letter')} on ${plural(rs,'route')}${within}`+(S.cover?' · the 12 busiest stand out':'');
    worldBtn.hidden=S.view==='europe'&&!far;
    worldBtn.textContent=S.view==='world'?'Back to Europe':`World map: ${plural(far,'letter')} beyond this one`;
    // timeline
    slider.value=S.range?S.range[1]:S.T==null?YMAX:Math.floor(S.T);
    bars.attr('class',b=>b.y+10>lo&&b.y<hi?'on':null);
    document.querySelectorAll('#awin button').forEach(b=>b.setAttribute('aria-pressed',S.T!=null&&!S.range&&+b.dataset.w===S.W));
    $('aall').setAttribute('aria-pressed',S.T==null&&!S.range);
    pins();
  }

  // labels: the busiest cities first, skipping any that would overlap one already placed
  function labels(){
    const t=d3.zoomTransform(svg.node()), placed=[], list=cities.filter(d=>d.v>0||S.city===d.n).sort((a,b)=>(S.city===b.n)-(S.city===a.n)||b.v-a.v);
    const key=list.map(d=>d.n).join()+t.k.toFixed(2)+t.x.toFixed(0)+t.y.toFixed(0);
    if(key===labelKey) return; labelKey=key;
    cities.forEach(d=>{ d.el.children[2].style.display='none'; });
    const fh=phone.matches?15:14, least=t.k<1.6&&list.length>45?3:0;   // the full map labels only the cities that carry something
    for(const d of list){
      if(d.v<least&&S.city!==d.n) continue;
      const x=t.x+t.k*d.p[0]+radius(d.v)+3, y=t.y+t.k*d.p[1]-fh/2, w=d.n.length*6.4+4;
      if(x<0||x+w>W||y<0||y+fh>H) continue;
      if(placed.some(b=>x<b.x+b.w&&x+w>b.x&&y<b.y+fh&&y+fh>b.y)) continue;
      placed.push({x,y,w}); const tx=d.el.children[2]; tx.style.display=''; tx.setAttribute('x',radius(d.v)+3);
    }
  }

  // ---------------------------------------------------------------- portraits
  const initial=n=>(n.replace(/^[“"]|^(the |cardinal |nuncio |doge |duke of |bishop of |archbishop of |comte d’|comte d'|comte de |marqués de los |conde de |van der |van |de |la )+/gi,'')[0]||n[0]).toUpperCase();
  const face=p=>p.img?`<img src="${esc(p.img)}" alt="" loading="lazy">`:`<span class="monog" aria-hidden="true">${esc(initial(p.name))}</span>`;
  const avs=ps=>ps.length?`<span class="avs">${ps.slice(0,3).map(face).join('')}</span>`:'';
  const people=new Map();
  for(const l of letters) for(const p of l.who){ if(!people.has(pk(p))) people.set(pk(p),{key:pk(p),name:p.name,img:p.img,letters:[]}); people.get(pk(p)).letters.push(l); }
  const plist=[...people.values()].sort((a,b)=>b.letters.length-a.letters.length||a.letters[0].year-b.letters[0].year);
  const whoSlug=k=>k.replace(/^portrait_|\.jpg$/g,'').replace(/^n:/,'n-').replace(/\s+/g,'_');
  const whoFrom=s=>plist.find(q=>whoSlug(q.key)===s);

  function pins(){
    const spots=[], [lo,hi]=range();
    for(const k of S.who){ const q=people.get(k), seen=new Set(); if(!q) continue;
      for(const l of q.letters){ if(l.year<lo||l.year>=hi||!matches(l)||S.hide.has(l.fam)) continue;
        const role=(l.who.find(p=>pk(p)===k)||{}).role, c=role==='recipient'?l.to:l.from;
        if(!seen.has(c)){ seen.add(c); spots.push({k:k+'@'+c,img:q.img,name:q.name,c}); } } }
    gPins.selectAll('g.pin').data(spots,d=>d.k).join(en=>{ const e=en.append('g').attr('class','pin');
        e.append('circle').attr('r',15);
        e.filter(d=>d.img).append('image').attr('href',d=>d.img).attr('x',-13).attr('y',-13).attr('width',26).attr('height',26).attr('clip-path','url(#pinclip)').attr('preserveAspectRatio','xMidYMid slice');
        e.filter(d=>!d.img).append('text').attr('class','monot').attr('dy','.36em').attr('text-anchor','middle').text(d=>initial(d.name));
        e.append('title').text(d=>`${d.name} at ${d.c}`); return e; });
    placePins();
  }
  const placePins=()=>gPins.selectAll('g.pin').attr('transform',d=>{ const p=P(d.c); return `translate(${p[0]},${p[1]-20/K}) scale(${1/K})`; });

  // ---------------------------------------------------------------- what a letter says
  const texts=new Map();
  const load=slug=>{ if(!texts.has(slug)) texts.set(slug,fetch(`atlas/${slug}.json`).then(r=>r.ok?r.json():{letters:{}}).catch(()=>({letters:{}}))); return texts.get(slug); };
  const entryOf=(rec,l)=>{ const d=rec.letters||{}; if(d[l.doc]) return d[l.doc]; if(d.all) return d.all; const v=Object.values(d); return v.length===1?{...v[0],set:true}:null; };
  const paras=t=>t.split(/\n\s*\n/).map(x=>`<p>${esc(x).replace(/\n/g,' ')}</p>`).join('');
  const parties=l=>{ const ps=[...l.who].sort((a,b)=>(a.role!=='sender')-(b.role!=='sender')); return ps.map(p=>`<span class="pty">${face(p)}<small>${({sender:'from',recipient:'to'})[p.role]||'with'}</small> ${esc(p.name)}</span>`).join(''); };
  const dot=l=>`<i class="fd" style="background:var(--${FAMS[l.fam][1]})" aria-hidden="true"></i>`;
  const row=l=>`<button type="button" class="a-l" data-l="${l.i}"><span class="d">${dot(l)}${esc(l.date||Math.floor(l.year))}</span><b>${esc(label(l))}</b><span class="m">${esc(l.from)} → ${esc(l.to)}</span></button>`;
  const byIdx=new Map(letters.map(l=>[l.i,l]));

  // ---------------------------------------------------------------- the panel's sheet
  const sheet=$('asheet'), panel=$('apanel');
  function renderSheet(){
    const v=stack.at(-1);
    sheet.hidden=!v; panel.classList.toggle('open',!!v); document.body.classList.toggle('a-sheet-open',!!v&&phone.matches);
    if(!v){ sheet.innerHTML=''; return; }
    const head=`<header class="a-sh">${stack.length>1?'<button type="button" data-act="back">‹ Back</button>':'<span></span>'}<button type="button" data-act="close" aria-label="Close and go back to the whole map">Close ×</button></header>`;
    sheet.innerHTML=head+`<div class="a-sc">${({list:listView,letter:letterView,story:storyView,unread:unreadView})[v.k](v)}</div>`;
    sheet.scrollTop=0; const sc=sheet.querySelector('.a-sc'); if(sc) sc.scrollTop=0;
    if(v.k==='letter') fillLetter(v);
    if(v.k==='story') fillStory(v);
  }
  function openSheet(v,{push=true,focusIt=true}={}){
    if(push) stack.push(v); else { stack.length=0; stack.push(v); }
    renderSheet(); update(); writeHash(v.k==='letter');
    if(focusIt){ sheet.focus({preventScroll:true});
      if(phone.matches){ const y=root.getBoundingClientRect().top+scrollY-(document.querySelector('.nav')?.offsetHeight||56)-4; scrollTo({top:y,behavior:still?'auto':'smooth'}); } }
  }
  function back(){ stack.pop(); if(!stack.length) return closeAll(); renderSheet(); update(); writeHash(); }
  function closeAll(){
    stack.length=0; const wasStory=S.story||S.range;
    Object.assign(S,{who:[],city:null,route:null,slugs:null,slugPage:null,story:null,range:null});
    if(S.T==null) S.cover=true;
    renderSheet(); if(wasStory&&S.view==='world') setView('europe'); resetZoom(); changed();
  }

  function listView(){
    const [lo,hi]=range(), ls=letters.filter(l=>l.year>=lo&&l.year<hi&&!S.hide.has(l.fam)&&matches(l)).slice().sort((a,b)=>a.year-b.year);
    const who=S.who.map(k=>people.get(k)).filter(Boolean), slugs=new Set(ls.map(l=>l.slug));
    let title='';
    if(S.slugPage) title=esc(label({pg:page[S.slugPage],label:S.slugPage}));
    else if(who.length===2) title=`Letters between ${esc(who[0].name)} and ${esc(who[1].name)}`;
    else if(who.length===1) title=esc(who[0].name);
    if(S.city) title+=(title?', through ':'Letters from or to ')+esc(S.city);
    if(S.route) title+=(title?', ':'')+esc(S.route);
    const hint=who.length===1?'<p class="a-hint">Pick a second person under People to see only the letters between them.</p>':'';
    const openHere=S.city&&S.unread?(openBy.get(S.city)||[]).filter(o=>o.y>=lo&&o.y<hi):[];
    const empty=!ls.length?`<p class="a-hint">None in these years.${S.T!=null||S.range?' <button type="button" class="linky" data-act="allyears">Show all years</button>':''}</p>`:'';
    return `<div class="a-cap">${avs(who)}<div><h3 tabindex="-1">${title}</h3><p class="a-sub">${plural(ls.length,'letter')} · ${plural(slugs.size,'write-up')}${isFinite(lo)||isFinite(hi)?' · '+esc(yearEl.textContent):''}</p></div></div>${hint}${empty}<div class="a-ls">${ls.map(row).join('')}</div>${unreadList(openHere,S.city)}`;
  }
  function unreadList(rows,at){
    if(!rows.length) return '';
    return `<h4 class="a-unh">Still unread at ${esc(at)} <span>${rows.length}</span></h4><ul class="a-un">${rows.slice(0,14).map(o=>`<li><a href="solve/${esc(o.id)}.html"><small>${o.y}</small> ${esc(o.t)}</a></li>`).join('')}</ul>${rows.length>14?`<p class="a-hint">and ${rows.length-14} more</p>`:''}<p class="a-cta"><a href="catalogue.html">These are open. Help solve them &rarr;</a></p>`;
  }
  function unreadView(v){
    const [lo,hi]=range(), rows=(openBy.get(v.at)||[]).filter(o=>o.y>=lo&&o.y<hi);
    return `<div class="a-cap"><div><h3 tabindex="-1">${esc(v.at)}</h3><p class="a-sub">Letters with no known decipherment, in the catalogue</p></div></div>${unreadList(rows,v.at)}`;
  }
  function letterView(v){
    const l=v.l, ctx=v.ctx||[], i=ctx.indexOf(l), prev=ctx[i-1], next=ctx[i+1];
    const nav=ctx.length>1?`<nav class="a-pn" aria-label="Other letters here"><button type="button" ${prev?`data-l="${prev.i}" data-keep="1"`:'disabled'}>‹ Earlier</button><span>${i+1} of ${ctx.length}</span><button type="button" ${next?`data-l="${next.i}" data-keep="1"`:'disabled'}>Later ›</button></nav>`:'';
    return `<article class="a-letter"><p class="a-kick">${dot(l)}${esc(l.pg?l.pg.stt:FAMS[l.fam][0])}</p>
      <h3 tabindex="-1">${esc(label(l))}</h3>
      <p class="a-sub">${esc(l.date||Math.floor(l.year))} · ${esc(l.from)} → ${esc(l.to)}</p>
      <div class="a-pty">${parties(l)}</div>
      <div id="atext" class="a-text"><p class="a-hint">Opening the letter…</p></div>
      <p class="a-go"><a href="${esc(l.slug)}.html">Full write-up &rarr;</a> <button type="button" class="linky" data-act="copy">Copy link</button></p></article>${nav}`;
  }
  async function fillLetter(v){
    const rec=await load(v.l.slug); if(stack.at(-1)!==v) return;
    const box=$('atext'); if(!box) return;
    const e=entryOf(rec,v.l); let h='';
    if(rec.snip) h+=`<figure class="a-snip"><img src="${esc(rec.snip.src)}" alt="${esc(rec.snip.cap)}" loading="lazy"><figcaption>${esc(rec.snip.cap)}. <span>${esc(rec.snip.credit)}</span></figcaption></figure>`;
    if(rec.withheld) h+=`<p class="a-hint">The text of this letter is not reproduced here. The write-up says what can be shown.</p>`;
    else if(e){
      if(e.set) h+=`<p class="a-hint">From a set of letters covered together in the write-up.</p>`;
      if(e.summary) h+=`<p class="a-sum">${esc(e.summary)}</p>`;
      if(e.state==='decoded, not read') h+=`<p class="a-hint">Decoded for checking, not yet read as sentences.</p>`;
      if(e.en) h+=`<h4>In English</h4><div class="a-en">${paras(e.en)}</div><p class="a-hint">${e.cut?'The opening only. ':''}[?] and […] mark uncertain or lost words; the write-up gives the conventions.</p>`;
    } else h+=`<p class="a-hint">No text is recorded for this letter on the map. The write-up has what is known.</p>`;
    if(rec.by&&rec.by.length) h+=`<p class="a-hint">Contributed by ${rec.by.map(esc).join(', ')}.</p>`;
    if(rec.system) h+=`<details class="a-sys"><summary>The cipher</summary><p>${esc(rec.system)}</p></details>`;
    box.innerHTML=h;
  }
  const chapterIdx=s=>stories.indexOf(s);
  function storyView(v){
    const s=v.s, i=chapterIdx(s), prev=stories[i-1], next=stories[i+1];
    const ls=(s.letters||[]).map(x=>letterOf(x.slug+'~'+x.doc)).filter(Boolean);
    return `<div class="a-story"><p class="a-kick">Chapter ${i+1} of ${stories.length} · ${span(s.y0,s.y1)}</p><h3 tabindex="-1">${esc(s.title)}</h3>${s.text.map(t=>`<p>${esc(t)}</p>`).join('')}
      <h4>Open a letter</h4><div class="a-ls spot" id="aspot">${ls.map(l=>`<button type="button" class="a-l" data-l="${l.i}" data-ctx="story"><span class="d">${dot(l)}${esc(l.date||Math.floor(l.year))}</span><b>${esc(label(l))}</b><span class="m" data-sum="${esc(l.key)}">${esc(l.from)} → ${esc(l.to)}</span></button>`).join('')}</div>
      <nav class="a-pn ch" aria-label="Chapters">${prev?`<button type="button" data-story="${esc(prev.id)}">‹ ${esc(prev.title)}</button>`:'<span></span>'}${next?`<button type="button" class="pri" data-story="${esc(next.id)}">${esc(next.title)} ›</button>`:'<button type="button" class="pri" data-act="close">Explore the whole map</button>'}</nav></div>`;
  }
  async function fillStory(v){
    for(const x of v.s.letters||[]){ const l=letterOf(x.slug+'~'+x.doc); if(!l) continue;
      const rec=await load(l.slug); if(stack.at(-1)!==v) return;
      const e=entryOf(rec,l), el=sheet.querySelector(`[data-sum="${CSS.escape(l.key)}"]`);
      if(el&&e&&e.summary&&!rec.withheld) el.textContent=e.summary.length>170?e.summary.slice(0,170).replace(/\s+\S*$/,'')+'…':e.summary; }
  }

  // ---------------------------------------------------------------- moves
  const leaveCover=()=>{ S.cover=false; };
  function changed(){ update(); renderTab(); if(stack.at(-1)?.k==='list') renderSheet(); writeHash(); }
  function pick(fn){ leaveCover(); S.story=null; S.slugs=null; S.slugPage=null; fn(); if(S.range){ S.range=null; S.T=null; } }
  function openList(){ if(filtered()) openSheet({k:'list'},{push:false}); else { stack.length=0; renderSheet(); } }
  async function openLetter(l,ctx){
    leaveCover();
    if(!ctx) ctx=l.r.all;
    if(stack.at(-1)?.k==='letter') stack.pop();
    if(l.r.far&&S.view==='europe') await setView('world');
    openSheet({k:'letter',l,ctx});
    // keep the route in sight when the map has been zoomed away from it
    const t=d3.zoomTransform(svg.node()), h=seenH(), out=p=>{ const x=t.x+t.k*p[0], y=t.y+t.k*p[1]; return x<8||x>W-8||y<8||y>h-8; };
    if(out(l.r.a)||out(l.r.b)) focus([l]);
  }
  async function openStory(s){
    Object.assign(S,{who:[],city:null,route:null,slugPage:null,story:s,range:[s.y0,s.y1],slugs:s.slugs?new Set(s.slugs):null,cover:false});
    stopPlay(); await setView(s.view||'europe');
    openSheet({k:'story',s},{push:false}); renderTab();
    const [lo,hi]=range(); focus(letters.filter(l=>l.year>=lo&&l.year<hi&&matches(l)));
  }
  function selectRoute(id){ pick(()=>{ S.route=S.route===id?null:id; S.city=null; }); openList(); changed(); }

  // the map's clicks and hovers
  hEls.on('pointerenter',(e,r)=>{ if(e.pointerType==='touch') return;
      svg.classed('dim',true); r.el.classList.add('hov');
      const ls=r.v, a=ls[0], b=ls.at(-1), wr=new Set(ls.map(l=>l.slug)).size;
      tip.innerHTML=ls.length===1?`${avs(a.who)}<b>${esc(label(a))}</b>${esc(r.id)}<br><span>${esc(a.date||Math.floor(a.year))} · ${esc(a.pg?a.pg.stt:FAMS[a.fam][0])}</span>`
        :`<b>${esc(r.id)}</b>${plural(ls.length,'letter')} · ${plural(wr,'write-up')}<br><span>${span(Math.floor(a.year),Math.floor(b.year))} · click to list them</span>`;
      tip.style.opacity=1; })
    .on('pointermove',e=>{ const q=root.getBoundingClientRect(); let x=e.clientX-q.left+14, y=e.clientY-q.top+14;
      if(x>q.width-290) x-=300; if(y>q.height-110) y-=120; tip.style.left=x+'px'; tip.style.top=y+'px'; })
    .on('pointerleave',(e,r)=>{ svg.classed('dim',false); r.el.classList.remove('hov'); tip.style.opacity=0; })
    .on('click',(e,r)=>{ tip.style.opacity=0; svg.classed('dim',false); r.el.classList.remove('hov');
      if(r.v.length===1) return openLetter(r.v[0],r.v);
      selectRoute(r.id); });
  cg.on('click',(e,d)=>{ e.stopPropagation(); pick(()=>{ S.city=S.city===d.n?null:d.n; S.route=null; }); openList(); changed(); });
  rg.on('click',(e,d)=>{ e.stopPropagation(); leaveCover(); openSheet({k:'unread',at:d.n},{push:false}); });
  worldBtn.addEventListener('click',()=>{ leaveCover(); setView(S.view==='world'?'europe':'world').then(()=>{ update(); writeHash(); }); });

  // the panel's clicks
  panel.addEventListener('click',e=>{
    const t=e.target.closest('[data-l],[data-act],[data-story],[data-tab],[data-who],[data-route],[data-start]'); if(!t) return;
    if(t.dataset.tab){ S.tab=t.dataset.tab; renderTab(); writeHash(); return; }
    if(t.dataset.start!==undefined) return openStory(stories[0]);
    if(t.dataset.story) return openStory(stories.find(s=>s.id===t.dataset.story));
    if(t.dataset.who){ const k=t.dataset.who, i=S.who.indexOf(k); pick(()=>{ if(i>=0) S.who.splice(i,1); else { S.who.push(k); if(S.who.length>2) S.who.shift(); } S.route=null; }); openList(); changed(); return; }
    if(t.dataset.route) return selectRoute(t.dataset.route);
    if(t.dataset.l){ const l=byIdx.get(+t.dataset.l), cur=stack.at(-1);
      if(t.dataset.keep) return openLetter(l,cur.ctx);
      if(t.dataset.ctx==='story') return openLetter(l,(cur.s.letters||[]).map(x=>letterOf(x.slug+'~'+x.doc)).filter(Boolean));
      if(cur&&cur.k==='list'){ const [lo,hi]=range(); return openLetter(l,letters.filter(x=>x.year>=lo&&x.year<hi&&!S.hide.has(x.fam)&&matches(x))); }
      return openLetter(l); }
    const a=t.dataset.act;
    if(a==='back') return back();
    if(a==='close') return closeAll();
    if(a==='allyears'){ S.T=null; S.range=null; return changed(); }
    if(a==='copy'){ try{ navigator.clipboard.writeText(location.href); t.textContent='Link copied'; }catch(err){ t.textContent=location.href; } }
  });
  feed.addEventListener('click',e=>{ const t=e.target.closest('[data-l]'); if(t){ stopPlay(); openLetter(byIdx.get(+t.dataset.l)); } });

  // ---------------------------------------------------------------- the tabs
  const body=$('abody'); let pq='';
  const tabHtml={
    stories(){ return `<p class="a-intro">Nine moments when the lines on this map carried something that mattered. Each opens the letters themselves.</p>
      <button type="button" class="a-start" data-start>Start the story &rarr;</button>
      <ol class="a-chapters">${stories.map(s=>`<li><button type="button" data-story="${esc(s.id)}"${S.story===s?' aria-current="true"':''}><small>${span(s.y0,s.y1)}</small><b>${esc(s.title)}</b></button></li>`).join('')}</ol>`; },
    people(){ const ql=pq.trim().toLowerCase(), rows=plist.filter(q=>!ql||q.name.toLowerCase().includes(ql));
      return `<div class="a-find"><input id="apq" type="search" placeholder="Find a correspondent" aria-label="Find a correspondent" value="${esc(pq)}"><span>${rows.length}</span></div>
      <p class="a-hint">Pick one to see their letters, two to see the letters between them.</p>
      <div class="a-plist">${rows.map(q=>`<button type="button" class="a-p" data-who="${esc(q.key)}" aria-pressed="${S.who.includes(q.key)}">${face(q)}<b>${esc(q.name)}</b><i>${q.letters.length}</i><small>${span(Math.floor(q.letters[0].year),Math.floor(q.letters.at(-1).year))}</small></button>`).join('')}</div>`; },
    routes(){ const [lo,hi]=range();
      const rs=routes.map(r=>({r,ls:r.all.filter(l=>l.year>=lo&&l.year<hi&&!S.hide.has(l.fam)&&matches(l,{route:false}))})).filter(x=>x.ls.length).sort((a,b)=>b.ls.length-a.ls.length).slice(0,40);
      return `<p class="a-hint">The busiest routes for what is on the map now. Open one for its letters.</p>`+(rs.length?`<div class="a-rlist">${rs.map(({r,ls})=>`<button type="button" data-route="${esc(r.id)}" aria-pressed="${S.route===r.id}"><b>${esc(r.id)}</b><span>${plural(ls.length,'letter')} · ${span(Math.floor(ls[0].year),Math.floor(ls.at(-1).year))}</span></button>`).join('')}</div>`:'<p class="a-hint">No located letters for this choice.</p>'); }
  };
  function renderTab(){
    if(playing&&S.tab!=='stories') return;
    document.querySelectorAll('.a-tabs [data-tab]').forEach(b=>{ const on=b.dataset.tab===S.tab; b.setAttribute('aria-selected',on); b.tabIndex=on?0:-1; });
    const focused=document.activeElement&&document.activeElement.id==='apq', pos=focused?document.activeElement.selectionStart:0;
    body.innerHTML=tabHtml[S.tab]();
    if(focused){ const i=$('apq'); if(i){ i.focus(); i.setSelectionRange(pos,pos); } }
  }
  body.addEventListener('input',e=>{ if(e.target.id==='apq'){ pq=e.target.value; renderTab(); } });

  // ---------------------------------------------------------------- time
  const btn=$('aplay'); let raf=0, last=0;
  function pulse(l){ if(still||!l.r.b) return; gPulse.append('circle').attr('class','pulse').attr('cx',l.r.b[0]).attr('cy',l.r.b[1]).attr('r',2)
    .attr('vector-effect','non-scaling-stroke').transition().duration(900).attr('r',16).style('opacity',0).remove(); }
  function stopPlay(){ if(!playing&&!raf) return; cancelAnimationFrame(raf); raf=0; playing=false; root.classList.remove('playing'); S.T=Math.floor(S.T);
    btn.innerHTML='&#9654; Play'; btn.setAttribute('aria-label','Play through time'); update(); renderTab(); writeHash(); }
  function step(now){
    const dt=Math.min(.1,(now-last)/1000); last=now; const prev=S.T;
    const busy=letters.some(l=>l.year>prev&&l.year<prev+6&&matches(l));   // slow down where the letters are, hurry through empty years
    S.T=Math.min(prev+dt*(busy?13:60),YMAX); update();
    let newest=null; for(const l of letters){ if(l.year>S.T) break; if(l.year>prev&&!S.hide.has(l.fam)&&matches(l)){ newest=l; pulse(l); } }
    if(newest) feed.innerHTML=`<b>${esc(newest.date||Math.floor(newest.year))}</b> · ${esc(newest.from)} → ${esc(newest.to)} · <button type="button" class="linky" data-l="${newest.i}">${esc(label(newest))}</button>`;
    if(S.T>=YMAX) return stopPlay(); raf=requestAnimationFrame(step); }
  btn.addEventListener('click',()=>{ if(raf) return stopPlay();
    if(S.T==null||S.T>=YMAX-1||S.range) S.T=YMIN;
    S.range=null; S.story=null; S.slugPage=null; if(stack.at(-1)?.k==='story'){ stack.length=0; renderSheet(); S.slugs=null; } leaveCover();
    playing=true; root.classList.add('playing'); btn.innerHTML='&#10074;&#10074; Pause'; btn.setAttribute('aria-label','Pause'); last=performance.now(); raf=requestAnimationFrame(step); });
  slider.addEventListener('input',()=>{ if(raf) stopPlay(); leaveCover();
    if(S.story){ S.story=null; S.slugs=null; if(stack.at(-1)?.k==='story'){ stack.length=0; renderSheet(); } }
    S.range=null; S.T=+slider.value; changed(); });
  $('awin').addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; S.W=+b.dataset.w; leaveCover();
    if(S.story){ S.story=null; S.slugs=null; if(stack.at(-1)?.k==='story'){ stack.length=0; renderSheet(); } }
    if(S.T==null||S.range) S.T=S.range?S.range[1]:1560; S.range=null; changed(); });
  $('aall').addEventListener('click',()=>{ if(raf) stopPlay(); S.T=null; S.range=null;
    if(S.story){ S.story=null; S.slugs=null; if(stack.at(-1)?.k==='story'){ stack.length=0; renderSheet(); } }
    changed(); });
  addEventListener('keydown',e=>{ if(e.key==='Escape'&&stack.length&&!document.querySelector('.search:not([hidden])')) back(); });

  // ---------------------------------------------------------------- every view has a URL
  let written=location.hash;
  function hashNow(){
    const a=[]; const add=(k,v)=>a.push(k+'='+encodeURIComponent(v));
    if(S.story) add('story',S.story.id);
    else {
      if(S.range) add('r',S.range.join('-'));
      else if(S.T!=null){ add('y',Math.floor(S.T)); add('w',S.W); }
      if(S.who.length) add('who',S.who.map(whoSlug).join(','));
      if(S.city) add('city',S.city);
      if(S.route) add('route',S.route);
      if(S.slugPage) add('slug',S.slugPage);
    }
    if(S.hide.size) add('hide',[...S.hide].join(','));
    if(!S.unread) add('unread','0');
    if(S.view==='world'&&!S.story) add('view','world');
    if(S.tab!=='stories') add('tab',S.tab);
    const v=stack.at(-1);
    if(v&&v.k==='letter') add('letter',v.l.key);
    if(v&&v.k==='unread') add('at',v.at);
    return a.length?'#'+a.join('&'):'';
  }
  function writeHash(push){
    if(playing) return;
    const h=hashNow(); if(h===written||(!h&&!/=/.test(location.hash))) return;
    written=h; try{ history[push?'pushState':'replaceState'](null,'',h||location.pathname+location.search); }catch(e){}
  }
  async function readHash(){
    const hash=location.hash; if(hash&&!/=/.test(hash)) return false;   // a plain anchor such as #about
    const q=Object.fromEntries(hash.slice(1).split('&').filter(Boolean).map(kv=>{ const i=kv.indexOf('='); return [kv.slice(0,i),decodeURIComponent(kv.slice(i+1))]; }));
    written=hash; stack.length=0;
    Object.assign(S,{T:null,W:10,range:null,who:[],city:null,route:null,slugs:null,slugPage:null,story:null,cover:!['story','r','y','who','city','route','slug','letter','at','hide','view','unread'].some(k=>k in q),tab:q.tab&&tabHtml[q.tab]?q.tab:'stories'});
    S.hide=new Set((q.hide||'').split(',').filter(f=>FAMS[f])); S.unread=q.unread!=='0';
    document.querySelectorAll('#alegend [data-f]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.f==='unread'?S.unread:!S.hide.has(b.dataset.f)));
    const story=q.story&&stories.find(s=>s.id===q.story);
    if(story){ S.story=story; S.range=[story.y0,story.y1]; S.slugs=story.slugs?new Set(story.slugs):null; stack.push({k:'story',s:story}); }
    else {
      if(q.r){ const m=q.r.split('-').map(Number); if(m.length===2&&m.every(isFinite)) S.range=m; }
      if(q.y&&isFinite(+q.y)){ S.T=+q.y; S.W=isFinite(+q.w)?+q.w:10; }
      if(q.who) S.who=q.who.split(',').map(whoFrom).filter(Boolean).map(p=>p.key).slice(0,2);
      if(q.city&&cnt.has(q.city)) S.city=q.city;
      if(q.route&&byRoute.has(q.route)) S.route=q.route;
      if(q.slug&&page[q.slug]){ S.slugPage=q.slug; S.slugs=new Set([q.slug]); }
      if(filtered()) stack.push({k:'list'});
    }
    const l=q.letter&&letterOf(q.letter);
    if(l){ const v=stack.at(-1), [lo,hi]=range(); let ctx=l.r.all;
      if(v&&v.k==='story') ctx=(story.letters||[]).map(x=>letterOf(x.slug+'~'+x.doc)).filter(Boolean);
      else if(v&&v.k==='list') ctx=letters.filter(x=>x.year>=lo&&x.year<hi&&!S.hide.has(x.fam)&&matches(x));
      stack.push({k:'letter',l,ctx}); }
    if(q.at&&openBy.has(q.at)&&!stack.length) stack.push({k:'unread',at:q.at});
    await setView(story?(story.view||'europe'):(q.view==='world'||(l&&l.r.far)?'world':'europe'));
    renderSheet(); update(); renderTab();
    if(story||filtered()){ const [lo,hi]=range(), ls=letters.filter(x=>x.year>=lo&&x.year<hi&&matches(x)); if(ls.length&&!l) focus(ls); }
    if(l) focus([l]);
    if(phone.matches&&stack.length) scrollTo(0,root.getBoundingClientRect().top+scrollY-(document.querySelector('.nav')?.offsetHeight||56)-4);
    return true;
  }
  addEventListener('popstate',readHash);
  addEventListener('hashchange',()=>{ if(location.hash!==written) readHash(); });

  // ---------------------------------------------------------------- start
  let rz=0; new ResizeObserver(()=>{ clearTimeout(rz); rz=setTimeout(()=>{ if(root.clientWidth!==W||root.clientHeight!==H){ labelKey=''; layout(); update(); } },120); }).observe(root);
  layout(); renderTab(); update();
  await readHash();
})();
