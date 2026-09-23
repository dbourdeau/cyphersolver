// The Cipher Atlas: atlas.json (places, letters) + pages.json (labels, outcomes, correspondents) drawn on Natural Earth land with d3.
// One filter state (up to two correspondents, a city, a route) drives the arcs, the pinned portraits, the caption and the route cards.
(async()=>{
  const root=document.getElementById('atlas'); if(!root || !window.d3) return;
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const [atlas,pages,world]=await Promise.all([
    fetch('atlas.json').then(r=>r.json()), fetch('pages.json').then(r=>r.json()).catch(()=>[]),
    fetch('https://cdn.jsdelivr.net/npm/world-atlas@2/land-50m.json').then(r=>r.json())]);
  const page=Object.fromEntries(pages.map(p=>[p.slug,p]));
  const ST={solved:'read',found:'explained / found read',partial:'read in part',stuck:'attempted'};
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const W=1200,H=700;
  const land=topojson.feature(world,world.objects.land);
  const proj=d3.geoConicConformal().rotate([-14,0]).parallels([38,58])
    .fitExtent([[10,40],[W-10,H-10]],{type:'MultiPoint',coordinates:[[-10,35.5],[36,36],[30,61],[-8,58]]});
  const path=d3.geoPath(proj);
  const svg=d3.select(root).insert('svg',':first-child').attr('viewBox',`0 0 ${W} ${H}`).attr('role','img')
    .attr('aria-label','Map of Europe with the routes of the ciphered letters');
  svg.append('defs').append('clipPath').attr('id','pinclip').append('circle').attr('r',13);
  svg.append('rect').attr('class','sea').attr('width',W).attr('height',H);
  const g=svg.append('g');
  g.append('path').attr('class','grat').attr('d',path(d3.geoGraticule10()));
  g.append('path').attr('class','land').attr('d',path(land));
  const gArcs=g.append('g'), gHits=g.append('g'), gCities=g.append('g'), gPulse=g.append('g'), gPins=g.append('g');

  const P=name=>{ const c=atlas.places[name]; return c?proj([c[1],c[0]]):null; };
  const letters=atlas.letters.map((l,i)=>({...l,i,a:P(l.from),b:P(l.to),pg:page[l.slug]})).filter(l=>l.a && l.b)
    .sort((x,y)=>x.year-y.year);
  letters.forEach(l=>{ l.who=(l.pg&&l.pg.people)||[]; l.route=l.from+' → '+l.to; });
  const curve=l=>{ const [x0,y0]=l.a,[x1,y1]=l.b, dx=x1-x0, dy=y1-y0, d=Math.hypot(dx,dy)||1;
    if(d<2) return `M${x0},${y0}m-4,0a4,4 0 1,0 8,0a4,4 0 1,0 -8,0`;
    const k=Math.min(.32,40/d+.12), mx=(x0+x1)/2-dy*k, my=(y0+y1)/2+dx*k; return `M${x0},${y0}Q${mx},${my} ${x1},${y1}`; };
  const arcs=gArcs.selectAll('path').data(letters).join('path').attr('class',l=>'arc '+l.st).attr('d',curve)
    .attr('stroke-width',1.6).attr('opacity',0).attr('vector-effect','non-scaling-stroke');
  arcs.each(function(l){ l.len=this.getTotalLength(); l.el=this; });
  const hits=gHits.selectAll('path').data(letters).join('path').attr('class','arc hit').attr('d',curve).attr('vector-effect','non-scaling-stroke');
  hits.each(function(l){ l.hit=this; });

  // cities, sized by traffic; click one to isolate the letters through it
  const cnt={}; letters.forEach(l=>{ cnt[l.from]=(cnt[l.from]||0)+1; cnt[l.to]=(cnt[l.to]||0)+1; });
  const cities=Object.keys(cnt).map(n=>({n,p:P(n),c:cnt[n]})).sort((a,b)=>b.c-a.c);
  const cg=gCities.selectAll('g').data(cities).join('g').attr('class','city').attr('transform',d=>`translate(${d.p})`);
  cg.append('circle').attr('class','hitc').attr('r',d=>7+Math.sqrt(d.c)*1.1);
  cg.append('circle').attr('r',d=>1.6+Math.sqrt(d.c)*1.1);
  cg.filter(d=>d.c>=5).append('text').attr('x',d=>4+Math.sqrt(d.c)*1.1).attr('dy','.35em').text(d=>d.n);
  cg.append('title').text(d=>`${d.n}: ${d.c} letter${d.c>1?'s':''}. Click to isolate.`);

  // zoom and pan
  let K=1;
  const zoom=d3.zoom().scaleExtent([.6,10]).on('zoom',e=>{ K=e.transform.k; g.attr('transform',e.transform);
    cg.attr('transform',d=>`translate(${d.p}) scale(${1/Math.sqrt(K)})`);
    placePins(); });
  svg.call(zoom).on('dblclick.zoom',null);

  // ---------------------------------------------------------------- the filter state
  const F={who:[], city:null, route:null};           // who: up to two portrait keys, newest last
  // a correspondent is keyed by their portrait, or by name when there is none; those get a lettered circle
  const pk=p=>p.img||'n:'+p.name;
  const initial=n=>(n.replace(/^[“"]|^(the |cardinal |nuncio |doge |duke of |bishop of |archbishop of |comte d’|comte d'|comte de |marqués de los |conde de |van der |van |de |la )+/gi,'')[0]||n[0]).toUpperCase();
  const face=p=>p.img?`<img src="${esc(p.img)}" alt="" loading="lazy">`:`<span class="mono" aria-hidden="true">${esc(initial(p.name))}</span>`;
  const matchWho=l=>F.who.every(k=>l.who.some(p=>pk(p)===k));
  const matches=(l,{route=true}={})=>matchWho(l) && (!F.city || l.from===F.city || l.to===F.city) && (!route || !F.route || l.route===F.route);
  const active=()=>F.who.length || F.city || F.route;

  // legend filters
  const on=new Set(Object.keys(ST));
  d3.select('#alegend').selectAll('button').data(Object.keys(ST)).join('button').attr('type','button')
    .attr('aria-pressed','true').html(s=>`<i style="background:var(--${{solved:'green',found:'blue',partial:'amber',stuck:'red'}[s]})"></i>${ST[s]}`)
    .on('click',function(e,s){ on.has(s)?on.delete(s):on.add(s); this.setAttribute('aria-pressed',on.has(s)); draw(T,false); });

  // histogram by decade
  const hist=d3.select('#ahist').attr('viewBox','0 0 525 38'), bins=d3.range(1420,1950,10).map(y=>({y,n:letters.filter(l=>l.year>=y&&l.year<y+10).length}));
  const hy=d3.scaleLinear().domain([0,d3.max(bins,b=>b.n)]).range([0,36]);
  const bars=hist.selectAll('rect').data(bins).join('rect').attr('x',b=>b.y-1420+.5).attr('width',9).attr('y',b=>38-hy(b.n)).attr('height',b=>hy(b.n));

  // ---------------------------------------------------------------- correspondents
  const people=new Map();
  for(const l of letters) for(const p of l.who){
    if(!people.has(pk(p))) people.set(pk(p),{key:pk(p),name:p.name,img:p.img,letters:[],slugs:new Set()});
    const q=people.get(pk(p)); q.letters.push(l); q.slugs.add(l.slug);
  }
  const plist=[...people.values()].sort((a,b)=>b.letters.length-a.letters.length || a.letters[0].year-b.letters[0].year);
  const row=document.getElementById('arow');
  row.innerHTML=plist.map(q=>`<button type="button" class="a-p" data-k="${esc(q.key)}" aria-pressed="false" title="${esc(q.name)}: ${q.letters.length} letter${q.letters.length>1?'s':''} on the map, ${Math.floor(q.letters[0].year)}${q.letters.at(-1).year-q.letters[0].year>=1?'–'+Math.floor(q.letters.at(-1).year):''}">${face(q)}<b>${esc(q.name)}</b><i>${q.letters.length}</i></button>`).join('');
  const chips=[...row.querySelectorAll('.a-p')], chipOf=Object.fromEntries(chips.map(c=>[c.dataset.k,c]));
  chips.forEach(c=>c.addEventListener('click',()=>{
    const k=c.dataset.k, i=F.who.indexOf(k);
    if(i>=0) F.who.splice(i,1); else { F.who.push(k); if(F.who.length>2) F.who.shift(); }
    F.route=null; refresh();
  }));
  document.getElementById('apq').addEventListener('input',e=>{ const q=e.target.value.trim().toLowerCase();
    chips.forEach(c=>{ c.hidden=q && !people.get(c.dataset.k).name.toLowerCase().includes(q); }); });
  const avs=ps=>ps.length?`<span class="avs">${ps.slice(0,3).map(face).join('')}</span>`:'';

  const tip=document.getElementById('atip'), yearEl=document.getElementById('ayear'), countEl=document.getElementById('acount'),
        feed=document.getElementById('afeed'), slider=document.getElementById('aslider'), cap=document.getElementById('afilter');
  let T=1945, shown=new Set(), playing=false;
  function pulse(l){ if(still) return; gPulse.append('circle').attr('class','pulse').attr('cx',l.b[0]).attr('cy',l.b[1]).attr('r',2)
    .attr('vector-effect','non-scaling-stroke').transition().duration(900).attr('r',18).style('opacity',0).remove(); }
  function draw(t,animate){
    T=t; yearEl.textContent=Math.floor(t); slider.value=Math.floor(t);
    let n=0, newest=null;
    for(const l of letters){
      const vis=l.year<=t && on.has(l.st) && matches(l), age=t-l.year;
      if(vis){ n++;
        const op=Math.max(.22,1-age/70); l.el.style.opacity=op; l.el.classList.toggle('fresh',age<4);
        if(!shown.has(l.i)){ shown.add(l.i);
          if(animate && !still){ l.el.style.strokeDasharray=l.len; l.el.style.strokeDashoffset=l.len;
            d3.select(l.el).transition().duration(1100).ease(d3.easeCubicOut).style('stroke-dashoffset',0).on('end',()=>{ l.el.style.strokeDasharray=''; pulse(l); });
            newest=l; } }
      } else { l.el.style.opacity=0; shown.delete(l.i); }
      l.el.classList.toggle('off',!vis);
      l.hit.style.display=vis?'':'none';
    }
    bars.attr('class',b=>b.y<=t?'on':null);
    countEl.textContent=`${n} letter${n===1?'':'s'} on the map`;
    if(newest) feed.innerHTML=`<b>${esc(newest.date||Math.floor(newest.year))}</b> &middot; ${esc(newest.from)} &rarr; ${esc(newest.to)} &middot; <a href="${newest.slug}.html">${esc(newest.pg?newest.pg.label:newest.label)}</a>`;
    // the correspondents writing in the last decade light up while the atlas plays
    row.classList.toggle('playing',playing);
    if(playing) for(const q of plist) chipOf[q.key].classList.toggle('live',q.letters.some(l=>l.year<=t && l.year>t-10));
    else chips.forEach(c=>c.classList.remove('live'));
    pins();
  }

  // portraits pinned where the chosen correspondents wrote from or received letters
  function pins(){
    const spots=[];
    for(const k of F.who){ const q=people.get(k), seen=new Set();
      for(const l of q.letters){ if(l.year>T || !matches(l) || !on.has(l.st)) continue;
        const role=(l.who.find(p=>pk(p)===k)||{}).role, c=role==='recipient'?l.to:l.from;
        if(!seen.has(c)){ seen.add(c); spots.push({k:k+'@'+c,img:q.img,name:q.name,c,p:P(c)}); } } }
    gPins.selectAll('g.pin').data(spots,d=>d.k).join(en=>{ const e=en.append('g').attr('class','pin');
        e.append('circle').attr('r',15);
        e.filter(d=>d.img).append('image').attr('href',d=>d.img).attr('x',-13).attr('y',-13).attr('width',26).attr('height',26)
          .attr('clip-path','url(#pinclip)').attr('preserveAspectRatio','xMidYMid slice');
        e.filter(d=>!d.img).append('text').attr('class','mono').attr('dy','.36em').attr('text-anchor','middle').text(d=>initial(d.name));
        e.append('title').text(d=>`${d.name} at ${d.c}`); return e; });
    placePins();
  }
  // a pin sits just above its city and keeps its size on screen as the map zooms
  const placePins=()=>gPins.selectAll('g.pin').attr('transform',d=>`translate(${d.p[0]},${d.p[1]-18/Math.sqrt(K)}) scale(${1/Math.sqrt(K)})`);

  // the caption: what is isolated, with the write-ups behind it
  function caption(){
    if(!active()){ cap.hidden=true; cap.innerHTML=''; return; }
    const ls=letters.filter(l=>matches(l)), slugs=[...new Set(ls.map(l=>l.slug))], read=slugs.filter(s=>page[s]&&page[s].st==='solved').length;
    const who=F.who.map(k=>people.get(k)), parts=[];
    if(who.length===1) parts.push(`<b>${esc(who[0].name)}</b>`);
    if(who.length===2) parts.push(`Letters between <b>${esc(who[0].name)}</b> and <b>${esc(who[1].name)}</b>`);
    if(F.city) parts.push(`${who.length?'through':'Letters from or to'} <b>${esc(F.city)}</b>`);
    if(F.route) parts.push(`on the route <b>${esc(F.route)}</b>`);
    const links=slugs.slice(0,8).map(s=>`<a href="${s}.html">${esc(page[s]?page[s].label:s)}</a>`).join(', ')+(slugs.length>8?`, and ${slugs.length-8} more`:'');
    cap.innerHTML=avs(who)+`<span class="what">${parts.join(' ')}: `+
      (ls.length?`${slugs.length} write-up${slugs.length>1?'s':''}, ${read} read &middot; ${ls.length} letter${ls.length>1?'s':''} on the map. ${links}`:'no letters on the map.')+
      `</span><button type="button" id="aclear">Show everyone</button>`;
    cap.hidden=false;
    document.getElementById('aclear').addEventListener('click',()=>{ F.who=[]; F.city=null; F.route=null; refresh(); });
  }

  // busiest routes: the cards follow the correspondents and the city, and pick a route in turn
  const top=document.getElementById('atop');
  function routes(){
    const ls=letters.filter(l=>matches(l,{route:false}));
    const rs=d3.rollups(ls,v=>({n:v.length,slugs:new Set(v.map(l=>l.slug)).size,y0:d3.min(v,l=>l.year),y1:d3.max(v,l=>l.year),
        who:[...new Map(v.flatMap(l=>l.who).map(p=>[pk(p),p])).values()]}),l=>l.route)
      .sort((a,b)=>b[1].n-a[1].n).slice(0,active()?30:9);
    top.innerHTML=rs.length?rs.map(([r,v])=>`<button type="button" data-r="${esc(r)}" aria-pressed="${r===F.route}">${avs(v.who)}<b>${esc(r)}</b><span>${v.n} letter${v.n>1?'s':''} &middot; ${v.slugs} write-up${v.slugs>1?'s':''} &middot; ${Math.floor(v.y0)}${v.y1-v.y0>=1?'&ndash;'+Math.floor(v.y1):''}</span></button>`).join('')
      :'<p class="none">No located letters for this choice.</p>';
    top.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{ F.route=F.route===b.dataset.r?null:b.dataset.r; refresh(); }));
  }

  function refresh(){
    chips.forEach(c=>c.setAttribute('aria-pressed',F.who.includes(c.dataset.k)));
    row.classList.toggle('picking',F.who.length>0);
    cg.classed('sel',d=>d.n===F.city);
    draw(T,false); caption(); routes();
  }
  cg.on('click',(e,d)=>{ e.stopPropagation(); F.city=F.city===d.n?null:d.n; F.route=null; refresh(); });

  // tooltip + neighbourhood
  hits.on('pointerenter',(e,l)=>{
      svg.classed('dim',true); arcs.classed('hot',d=>d.slug===l.slug);
      const ps=[...l.who].sort((a,b)=>(a.role!=='sender')-(b.role!=='sender'));
      tip.innerHTML=avs(ps)+`<b>${esc(l.pg?l.pg.label:l.label)}</b>${ps.length?`<span>${ps.map(p=>(p.role==='sender'?'from ':'to ')+esc(p.name)).join(' ')}</span><br>`:''}${esc(l.from)} &rarr; ${esc(l.to)}<br><span>${esc(l.date||Math.floor(l.year))} &middot; ${esc(l.pg?l.pg.stt:ST[l.st])}</span>`;
      tip.style.opacity=1; })
    .on('pointermove',e=>{ const r=root.getBoundingClientRect(); let x=e.clientX-r.left+14, y=e.clientY-r.top+14;
      if(x>r.width-290) x-=300; tip.style.left=x+'px'; tip.style.top=y+'px'; })
    .on('pointerleave',()=>{ svg.classed('dim',false); arcs.classed('hot',false); tip.style.opacity=0; })
    .on('click',(e,l)=>{ location.href=l.slug+'.html'; });

  // play
  const btn=document.getElementById('aplay'); let raf=0, last=0;
  function stop(){ cancelAnimationFrame(raf); raf=0; playing=false; btn.innerHTML='&#9654; Play'; btn.setAttribute('aria-label','Play through time'); draw(T,false); }
  function step(now){ const dt=Math.min(.1,(now-last)/1000); last=now;
    const busy=letters.some(l=>l.year>T && l.year<T+6 && matches(l));   // slow down where the letters are, hurry through empty years
    const t=T+dt*(busy?14:60); draw(Math.min(t,1945),true); if(t>=1945){ stop(); return; } raf=requestAnimationFrame(step); }
  btn.addEventListener('click',()=>{ if(raf){ stop(); return; } if(T>=1944) { shown.clear(); draw(1420,false); }
    playing=true; btn.innerHTML='&#10074;&#10074; Pause'; btn.setAttribute('aria-label','Pause'); last=performance.now(); raf=requestAnimationFrame(step); });
  slider.addEventListener('input',()=>{ if(raf) stop(); draw(+slider.value,true); });
  document.getElementById('aall').addEventListener('click',()=>{ if(raf) stop(); draw(1945,false); });

  // open on the whole map; it plays only when the reader presses Play
  refresh();
})();
