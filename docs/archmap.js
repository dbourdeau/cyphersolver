// The map on To the Archive: every open request at the town of its archive (#amapdata, placed by _archives_page.py), on the
// Atlas's Natural Earth land. The list below owns the filters (window.archList): a ring's size is the requests there under
// the kind, source and search filters, and clicking a ring filters the list to that town.
(async()=>{
  const root=document.getElementById('amap'), L=window.archList; if(!root || !L || !window.d3 || !window.topojson) return;
  const $=id=>document.getElementById(id);
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches, phone=matchMedia('(max-width:860px)');
  const LAND='https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/';
  const towns=JSON.parse($('amapdata').textContent).towns;
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const plural=(n,w)=>`${n} ${w}${n===1?'':'s'}`;
  const land50=await fetch(LAND+'land-50m.json').then(r=>r.json());

  const dots=Object.entries(towns).map(([n,c])=>({n,c,v:0}));
  const far=d=>d.c[1]<-12||d.c[1]>45||d.c[0]<34||d.c[0]>64;
  let view='europe', W=1000, H=560, proj, K=1, landNow=topojson.feature(land50,land50.objects.land), landEurope=landNow, landWorld=null;
  const svg=d3.select(root).insert('svg',':first-child').attr('role','img').attr('aria-label','Map of the towns whose archives hold the requested pieces');
  const sea=svg.append('rect').attr('class','sea'), g=svg.append('g');
  const pGrat=g.append('path').attr('class','grat'), pLand=g.append('path').attr('class','land'), gRings=g.append('g'), gLabels=g.append('g');
  const EUROPE=[[-10,35.5],[36,36],[30,61],[-8,58]], CORE=[[-7,37],[21,37],[21,58],[-6,56]], WORLD=[[-125,-38],[152,-38],[150,64],[-125,64]];
  const rad=d=>(phone.matches?2:2.6)+Math.sqrt(d.v)*(phone.matches?.9:1.3);
  const rg=gRings.selectAll('circle').data(dots).join('circle').attr('class','ring').attr('vector-effect','non-scaling-stroke')
    .attr('tabindex',0).attr('role','button').each(function(d){ d.el=this; });
  rg.append('title');
  const lb=gLabels.selectAll('text').data(dots).join('text').attr('dy','.35em').text(d=>d.n).each(function(d){ d.tx=this; });

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
      this.setAttribute('aria-label',`${d.n}: ${plural(d.v,'request')}`); this.firstChild.textContent=`${d.n}: ${plural(d.v,'request')}. Click to list them.`; });
    labels();
    const none=cnt['']||0;
    $('amapn').textContent=`${plural(n,'request')} in ${plural(p,'town')}`;
    const wb=$('amworld'); wb.hidden=view==='europe'&&!out;
    wb.textContent=view==='world'?'Back to Europe':`World map: ${plural(out,'request')} beyond Europe`;
    side(none);
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
  const panel=$('amapside');
  function side(none){
    const sel=L.place();
    if(sel===null){
      const top=dots.filter(d=>d.v).slice(0,8);   // draw() has sorted the dots, busiest first
      panel.innerHTML=`<p class="am-sub">Click a ring to list only the requests held in that town. The kind and source filters below change the rings too.</p>`+
        (top.length?`<h3 class="am-h">Busiest towns</h3><ul class="am-ls">${top.map(d=>`<li><button type="button" class="linky" data-pl="${esc(d.n)}">${esc(d.n)}</button> <b>${d.v}</b></li>`).join('')}</ul>`:'')+
        (none?`<button type="button" class="am-only" data-pl="">Not on the map: ${plural(none,'request')}</button><p class="am-sub">A library or a database will do, or the archive is not yet identified.</p>`:'');
      return;
    }
    const arch=L.archives(), tot=arch.reduce((a,x)=>a+x.n,0);
    panel.innerHTML=`<header><h3 tabindex="-1">${esc(sel===''?'Not on the map':sel)}</h3><button type="button" class="linky" data-pl="all">Every place ×</button></header>
      <p class="am-sub">${plural(tot,'request')}${sel===''?'':` in ${plural(arch.length,'archive')}`}</p>
      <ul class="am-ls">${arch.map(a=>`<li><a href="#${esc(a.id)}" data-sec="${esc(a.id)}">${esc(a.name)}</a> <b>${a.n}</b></li>`).join('')}</ul>
      <p class="am-cta"><a href="#list" data-sec="">See the ${plural(tot,'request')} below &darr;</a></p>`;
  }
  panel.addEventListener('click',e=>{
    const b=e.target.closest('[data-pl]'); if(b){ L.pick(b.dataset.pl==='all'?null:b.dataset.pl); if(L.place()!==null) panel.querySelector('h3')?.focus({preventScroll:true}); return; }
    const a=e.target.closest('[data-sec]'); if(a&&a.dataset.sec){ const d=$(a.dataset.sec); if(d){ d.hidden=false; d.open=true; } }
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
  $('amzin').addEventListener('click',by(1.6)); $('amzout').addEventListener('click',by(1/1.6));
  $('amzreset').addEventListener('click',()=>svg.transition().duration(still?0:400).call(zoom.transform,d3.zoomIdentity));
  $('amworld').addEventListener('click',async()=>{
    view=view==='world'?'europe':'world';
    if(view==='world'&&!landWorld){ try{ const w=await fetch(LAND+'land-110m.json').then(r=>r.json()); landWorld=topojson.feature(w,w.objects.land); }catch(err){ landWorld=landEurope; } }
    landNow=view==='world'?landWorld:landEurope; K=1; svg.call(zoom.transform,d3.zoomIdentity); layout(); });

  L.onchange=draw;
  let rz=0; new ResizeObserver(()=>{ clearTimeout(rz); rz=setTimeout(()=>{ if(root.clientWidth!==W||root.clientHeight!==H) layout(); },120); }).observe(root);
  layout();
})();
