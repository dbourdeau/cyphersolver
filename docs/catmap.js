// The map on the Unsolved Catalogue: every open cipher at the town of the archive that holds it, on the Atlas's Natural
// Earth land (the To the Archive map, archmap.js, is its model). The list above owns the filters (window.catList, set by
// the page script): a ring's size is the ciphers held in that town under the search, the years and the filters, and
// clicking a ring filters the list to the archives of that town.
(async()=>{
  const root=document.getElementById('cmap'), L=window.catList; if(!root || !L || !window.d3 || !window.topojson) return;
  const $=id=>document.getElementById(id);
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches, phone=matchMedia('(max-width:900px)');
  const LAND='https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/';
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const plural=(n,w)=>`${n} ${w}${n===1?'':'s'}`;
  let land50; try{ land50=await fetch(LAND+'land-50m.json').then(r=>r.json()); }catch(err){ root.closest('.amap-wrap').hidden=true; return; }

  const dots=Object.entries(L.towns).map(([n,c])=>({n,c,v:0}));
  const far=d=>d.c[1]<-12||d.c[1]>45||d.c[0]<34||d.c[0]>64;
  let view='europe', W=1000, H=560, proj, K=1, landNow=topojson.feature(land50,land50.objects.land), landEurope=landNow, landWorld=null;
  const svg=d3.select(root).insert('svg',':first-child').attr('role','img').attr('aria-label','Map of the towns whose archives hold the open ciphers');
  const sea=svg.append('rect').attr('class','sea'), g=svg.append('g');
  const pGrat=g.append('path').attr('class','grat'), pLand=g.append('path').attr('class','land'), gRings=g.append('g'), gLabels=g.append('g');
  const EUROPE=[[-10,35.5],[36,36],[30,61],[-8,58]], CORE=[[-7,37],[21,37],[21,58],[-6,56]], WORLD=[[-125,-38],[152,-38],[150,64],[-125,64]];
  const rad=d=>(phone.matches?2:2.6)+Math.sqrt(d.v)*(phone.matches?.9:1.3);
  const rg=gRings.selectAll('circle').data(dots).join('circle').attr('class','ring').attr('vector-effect','non-scaling-stroke')
    .attr('tabindex',0).attr('role','button').each(function(d){ d.el=this; });
  rg.append('title');
  const lb=gLabels.selectAll('text').data(dots).join('text').attr('dy','.35em').text(d=>d.n.split(',')[0]).each(function(d){ d.tx=this; });

  function layout(){
    W=root.clientWidth||1000; H=root.clientHeight||560;
    const world=view==='world';
    proj=(world?d3.geoNaturalEarth1().rotate([-12,0]):d3.geoConicConformal().rotate([-14,0]).parallels([38,58]))
      .fitExtent([[world?20:10,world?40:20],[W-(world?56:10),H-10]],{type:'MultiPoint',coordinates:world?WORLD:(W/H<1.1?CORE:EUROPE)});
    const path=d3.geoPath(proj);
    svg.attr('viewBox',`0 0 ${W} ${H}`); sea.attr('width',W).attr('height',H);
    pGrat.attr('d',path(d3.geoGraticule10())); pLand.attr('d',path(landNow));
    dots.forEach(d=>{ d.p=proj([d.c[1],d.c[0]]); d.w=0; });
    rg.attr('cx',d=>d.p[0]).attr('cy',d=>d.p[1]);
    draw();
  }

  // ---------------------------------------------------------------- drawing, from the list's filters
  function draw(){
    const cnt=L.counts(), sel=L.place(); let n=0, p=0, out=0;
    for(const d of dots){ d.v=cnt[d.n]||0; if(d.v){ n+=d.v; p++; if(far(d)) out+=d.v; } }
    dots.sort((a,b)=>b.v-a.v);   // the biggest first, so the small rings sit on top and stay clickable
    for(const d of dots) d.el.parentNode.appendChild(d.el);
    rg.each(function(d){ this.style.display=d.v?'':'none'; if(!d.v) return;
      this.setAttribute('r',rad(d)/Math.sqrt(K)); this.classList.toggle('sel',sel===d.n); this.classList.toggle('dim',!!sel&&sel!==d.n);
      this.setAttribute('aria-label',`${d.n}: ${plural(d.v,'cipher')}`); this.firstChild.textContent=`${d.n}: ${plural(d.v,'cipher')}. Click to list them.`; });
    labels();
    $('cmapn').textContent=`${plural(n,'cipher')} in ${plural(p,'town')}`;
    const wb=$('cmworld'); wb.hidden=view==='europe'&&!out;
    wb.textContent=view==='world'?'Back to Europe':`World map: ${plural(out,'cipher')} beyond Europe`;
    side(cnt['']||0);
  }
  // labels: the busiest towns first, skipping any that would overlap one already placed or leave the frame
  function labels(){
    const t=d3.zoomTransform(svg.node()), placed=[], sel=L.place();
    const order=dots.filter(d=>d.v).sort((a,b)=>(b.n===sel)-(a.n===sel)||b.v-a.v);
    dots.forEach(d=>{ d.tx.style.display='none'; });
    for(const d of order){
      d.tx.setAttribute('font-size',12/K); d.tx.setAttribute('x',d.p[0]+rad(d)/Math.sqrt(K)+3/K); d.tx.setAttribute('y',d.p[1]);
      if(!d.w){ d.tx.style.display=''; d.w=d.tx.getComputedTextLength()*K+6; d.tx.style.display='none'; }
      const x=t.x+t.k*d.p[0]+rad(d)*Math.sqrt(K)+3, y=t.y+t.k*d.p[1]-8;
      if(x<0||x+d.w>W-44||y<0||y+16>H||placed.some(b=>x<b.x+b.w&&x+d.w>b.x&&y<b.y+16&&y+16>b.y)) continue;
      placed.push({x,y,w:d.w}); d.tx.style.display='';
    }
  }

  // ---------------------------------------------------------------- the panel beside the map
  const panel=$('cmapside');
  function side(none){
    const sel=L.place();
    if(sel===null){
      const top=dots.filter(d=>d.v).slice(0,10);   // draw() has sorted the dots, busiest first
      panel.innerHTML=`<p class="am-sub">Click a ring to list only the ciphers held in that town. The search, the years and the filters above the list change the rings too.</p>`+
        (top.length?`<h3 class="am-h">Busiest towns</h3><ul class="am-ls">${top.map(d=>`<li><button type="button" class="linky" data-pl="${esc(d.n)}">${esc(d.n)}</button> <b>${d.v}</b></li>`).join('')}</ul>`:'')+
        (none?`<p class="am-sub">Not on the map: ${plural(none,'cipher')} known only from a printed edition, or in an archive not yet identified or placed.</p>`:'');
      return;
    }
    const arch=L.archives(sel), tot=arch.reduce((a,x)=>a+x.n,0);
    panel.innerHTML=`<header><h3 tabindex="-1">${esc(sel)}</h3><button type="button" class="linky" data-pl="all">Every place ×</button></header>
      <p class="am-sub">${plural(tot,'cipher')} in ${plural(arch.length,'archive')}</p>
      <ul class="am-ls">${arch.map(a=>`<li><button type="button" class="linky" data-ar="${esc(a.id)}">${esc(a.name)}</button> <b>${a.n}</b></li>`).join('')}</ul>
      <p class="am-cta"><button type="button" class="linky" data-show="1">See the ciphers in the list &uarr;</button></p>`;
  }
  panel.addEventListener('click',e=>{
    const b=e.target.closest('[data-pl]'); if(b){ L.pick(b.dataset.pl==='all'?null:b.dataset.pl); if(L.place()!==null) panel.querySelector('h3')?.focus({preventScroll:true}); return; }
    const a=e.target.closest('[data-ar]'); if(a){ L.only(a.dataset.ar); L.show(); return; }
    if(e.target.closest('[data-show]')) L.show();
  });
  function pick(d){ L.pick(L.place()===d.n?null:d.n); if(L.place()!==null) panel.querySelector('h3')?.focus({preventScroll:true}); }
  rg.on('click',(e,d)=>{ e.stopPropagation(); pick(d); })
    .on('keydown',(e,d)=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); pick(d); } });

  // ---------------------------------------------------------------- zoom, pan and the world view
  // the map sits in a long page, so the wheel scrolls the page and zooms only with Ctrl (or Cmd); one finger on a phone
  // scrolls the page, two move the map
  const zoom=d3.zoom().scaleExtent([.7,12])
    .filter(e=>e.type==='wheel'?e.ctrlKey||e.metaKey:e.type==='touchstart'?e.touches.length>1:!e.ctrlKey&&!e.button)
    .on('zoom',e=>{ K=e.transform.k; g.attr('transform',e.transform); rg.attr('r',d=>rad(d)/Math.sqrt(K)); labels(); });
  svg.call(zoom).on('dblclick.zoom',null);
  const by=f=>()=>svg.transition().duration(still?0:250).call(zoom.scaleBy,f);
  $('cmzin').addEventListener('click',by(1.6)); $('cmzout').addEventListener('click',by(1/1.6));
  $('cmzreset').addEventListener('click',()=>svg.transition().duration(still?0:400).call(zoom.transform,d3.zoomIdentity));
  $('cmworld').addEventListener('click',async()=>{
    view=view==='world'?'europe':'world';
    if(view==='world'&&!landWorld){ try{ const w=await fetch(LAND+'land-110m.json').then(r=>r.json()); landWorld=topojson.feature(w,w.objects.land); }catch(err){ landWorld=landEurope; } }
    landNow=view==='world'?landWorld:landEurope; K=1; svg.call(zoom.transform,d3.zoomIdentity); layout(); });

  L.onchange=draw;
  let rz=0; new ResizeObserver(()=>{ clearTimeout(rz); rz=setTimeout(()=>{ if(root.clientWidth!==W||root.clientHeight!==H) layout(); },120); }).observe(root);
  layout();
})();
