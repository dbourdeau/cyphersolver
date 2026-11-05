// The unread map on To the Archive: the Atlas's "still unread" layer alone (atlas-open.json, the open catalogue letters at
// the place they were written), on the same Natural Earth land, with no read routes. A ring is gold when at least one of
// its letters has a request on this page (the ids in #amapreq); its list links to the request, the others to their entry.
(async()=>{
  const root=document.getElementById('amap'); if(!root || !window.d3 || !window.topojson) return;
  const $=id=>document.getElementById(id);
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches, phone=matchMedia('(max-width:860px)');
  const req=new Set(JSON.parse(($('amapreq')||{}).textContent||'[]').map(String));
  const [open,land50]=await Promise.all([
    fetch('atlas-open.json').then(r=>r.json()).catch(()=>({places:{},letters:[]})),
    fetch('https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/land-50m.json').then(r=>r.json())]);
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const plural=(n,w)=>`${n} ${w}${n===1?'':'s'}`;

  const byPlace=d3.group(open.letters,o=>o.at);
  const rings=[...byPlace].map(([n,all])=>({n,all:all.slice().sort((a,b)=>a.y-b.y||a.id-b.id),c:open.places[n]}))
    .filter(d=>d.c).map(d=>({...d,arch:d.all.filter(o=>req.has(String(o.id))).length}))
    .sort((a,b)=>b.all.length-a.all.length);   // the biggest first, so the small rings sit on top and stay clickable
  const S={only:false,sel:null};

  let W=1000,H=560,proj,K=1;
  const svg=d3.select(root).insert('svg',':first-child').attr('role','img').attr('aria-label','Map of the places where the unread catalogue letters were written');
  const sea=svg.append('rect').attr('class','sea'), g=svg.append('g');
  const pGrat=g.append('path').attr('class','grat'), pLand=g.append('path').attr('class','land'), gRings=g.append('g'), gLabels=g.append('g');
  const land=topojson.feature(land50,land50.objects.land);
  const EUROPE=[[-10,35.5],[36,36],[30,61],[-8,58]], CORE=[[-7,37],[21,37],[21,58],[-6,56]];
  const rad=d=>(phone.matches?2:2.6)+Math.sqrt(S.only?d.arch:d.all.length)*(phone.matches?.9:1.35);
  const rg=gRings.selectAll('circle').data(rings).join('circle').attr('class',d=>'ring'+(d.arch?' arch':''))
    .attr('vector-effect','non-scaling-stroke').attr('tabindex',0).attr('role','button')
    .attr('aria-label',d=>`${d.n}: ${plural(d.all.length,'unread letter')}${d.arch?`, ${d.arch} with an archive request`:''}`);
  const lb=gLabels.selectAll('text').data(rings.filter(d=>d.all.length>=6)).join('text').attr('dy','.35em').text(d=>d.n);

  function layout(){
    W=root.clientWidth||1000; H=root.clientHeight||560;
    proj=d3.geoConicConformal().rotate([-14,0]).parallels([38,58]).fitExtent([[10,20],[W-10,H-10]],{type:'MultiPoint',coordinates:W/H<1.1?CORE:EUROPE});
    const path=d3.geoPath(proj);
    svg.attr('viewBox',`0 0 ${W} ${H}`); sea.attr('width',W).attr('height',H);
    pGrat.attr('d',path(d3.geoGraticule10())); pLand.attr('d',path(land));
    rings.forEach(d=>{ d.p=proj([d.c[1],d.c[0]]); });
    rg.attr('cx',d=>d.p[0]).attr('cy',d=>d.p[1]);
    draw();
  }
  function draw(){
    let n=0, p=0;
    rg.each(function(d){ const on=!S.only||d.arch>0; this.style.display=on?'':'none';
      if(on){ n+=S.only?d.arch:d.all.length; p++; this.setAttribute('r',rad(d)/Math.sqrt(K)); }
      this.classList.toggle('sel',S.sel===d); });
    // labels: the biggest places first, skipping any that would overlap one already placed
    const t=d3.zoomTransform(svg.node()), placed=[];
    lb.attr('font-size',12/K).attr('x',d=>d.p[0]+rad(d)/Math.sqrt(K)+3/K).attr('y',d=>d.p[1])
      .each(function(d){ if(!d.w){ this.style.display=''; d.w=this.getComputedTextLength()*K+6; } })   // measured once, in screen pixels
      .style('display',d=>{ if(S.only&&!d.arch) return 'none';
        const x=t.x+t.k*d.p[0]+rad(d)*Math.sqrt(K)+3, y=t.y+t.k*d.p[1]-8, w=d.w;
        if(x<0||x+w>W-44||y<0||y+16>H||placed.some(b=>x<b.x+b.w&&x+w>b.x&&y<b.y+16&&y+16>b.y)) return 'none';
        placed.push({x,y,w}); return ''; });
    $('amapn').textContent=`${plural(n,'letter')} at ${plural(p,'place')}`;
  }

  // zoom and pan: one finger on a phone scrolls the page, two move the map
  const zoom=d3.zoom().scaleExtent([.7,12])
    .filter(e=>e.type==='touchstart'?e.touches.length>1:(!e.ctrlKey||e.type==='wheel')&&!e.button)
    .on('zoom',e=>{ K=e.transform.k; g.attr('transform',e.transform); draw(); });
  svg.call(zoom).on('dblclick.zoom',null);
  const by=f=>()=>svg.transition().duration(still?0:250).call(zoom.scaleBy,f);
  $('amzin').addEventListener('click',by(1.6)); $('amzout').addEventListener('click',by(1/1.6));
  $('amzreset').addEventListener('click',()=>svg.transition().duration(still?0:400).call(zoom.transform,d3.zoomIdentity));

  // the list beside the map: the letters of the chosen place, or how to read the map
  const side=$('amapside'), intro=side.innerHTML;
  function list(d){
    S.sel=d; draw();
    if(!d){ side.innerHTML=intro; return; }
    const rows=(S.only?d.all.filter(o=>req.has(String(o.id))):d.all);
    side.innerHTML=`<header><h3 tabindex="-1">${esc(d.n)}</h3><button type="button" class="linky" data-act="close">Close ×</button></header>
      <p class="am-sub">${plural(d.all.length,'letter')} written here with no known decipherment${d.arch?` · <b>${d.arch}</b> need${d.arch===1?'s':''} the archive`:''}</p>
      <ul class="am-ls">${rows.map(o=>{ const a=req.has(String(o.id));
        return `<li${a?' class="arch"':''}><a href="${a?'#c'+o.id:'solve/'+o.id+'.html'}"><small>${o.y}</small> ${esc(o.t)}</a>${a?'<span class="am-tag">archive request</span>':''}</li>`; }).join('')}</ul>
      <p class="am-cta"><a href="catalogue.html">The whole catalogue &rarr;</a> · <a href="atlas.html#at=${encodeURIComponent(d.n)}">${esc(d.n)} on the atlas &rarr;</a></p>`;
    side.querySelector('h3').focus({preventScroll:!phone.matches});
  }
  rg.on('click',(e,d)=>{ e.stopPropagation(); list(S.sel===d?null:d); })
    .on('keydown',(e,d)=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); list(S.sel===d?null:d); } });
  rg.append('title').text(d=>`${d.n}: ${plural(d.all.length,'unread letter')}${d.arch?`, ${d.arch} with an archive request`:''}`);
  side.addEventListener('click',e=>{ if(e.target.closest('[data-act=close]')) list(null); });
  $('amaponly').addEventListener('click',e=>{ S.only=!S.only; e.currentTarget.setAttribute('aria-pressed',S.only);
    if(S.sel&&S.only&&!S.sel.arch) list(null); else if(S.sel) list(S.sel); else draw(); });

  let rz=0; new ResizeObserver(()=>{ clearTimeout(rz); rz=setTimeout(()=>{ if(root.clientWidth!==W||root.clientHeight!==H) layout(); },120); }).observe(root);
  layout();
})();
