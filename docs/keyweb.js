// The Key Web: keys.json + pages.json. Keys and letters that connect to something else are a force-directed graph, letters
// pulled towards their year on the x axis; a key used on one letter alone is a mark in the date strip under the graph.
// Keys coloured by who made them (period / scholar / rebuilt here), sized by the letters they were used on; failed tests as
// red dashed edges behind a filter; hub spokes only for a selected hub; zoom and pan; a key card with its image; a link per
// key (keys.html#k-balbases).
(async()=>{
  const root=document.getElementById('kw'); if(!root || !window.d3) return;
  const [K,pages]=await Promise.all([fetch('keys.json').then(r=>r.json()),fetch('pages.json').then(r=>r.json())]);
  const page=Object.fromEntries(pages.map(p=>[p.slug,p]));
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const yr=y=>y==null?'':Math.floor(y);
  const BANDS=[['period','Keys of the period'],['scholar',"Scholars' keys"],['here','Rebuilt here']];
  const band=k=>k.kind==="scholar's key"?'scholar':k.kind==='rebuilt here'?'here':'period';
  const EDGES=[['rebuilt','rebuilt from',h=>/rebuilt/.test(h)],['unchanged','used unchanged',h=>/unchanged|explained/.test(h)],
               ['adapted','adapted or partial',h=>/adapt|partial/.test(h)],['tried','tried, did not fit',h=>h==='tried']];
  const ecls=h=>(EDGES.find(e=>e[2](h))||EDGES[1])[0];
  // keys.json keeps its edge values; this is how they read on the page
  const HOW={'read unchanged':'key used unchanged','rebuilt from':'key rebuilt from this letter','adapted':'key adapted','partial':'key fits in part','explained':'explained with this key','tried':''};
  const narrow=root.clientWidth<700, W=narrow?620:1100, H=narrow?780:640, CW=narrow?1.4:1;

  // nodes: keys, letters, sources; edges: use links, tried links, source links. A letter's date is .date: .x and .y are the layout's
  const nodes=[], byId={}, add=n=>(byId[n.id]=n,nodes.push(n),n);
  K.keys.forEach(k=>add({...k,type:'key',band:band(k),reads:[],tried:[],srcs:[],srcIds:new Set()}));
  (K.sources||[]).forEach(s=>add({...s,type:'src'}));
  const letter=slug=>{ const p=page[slug]; if(!p) return null;
    return byId['t:'+slug]||add({id:'t:'+slug,type:'t',slug,label:p.label,date:typeof p.y==='number'?p.y:null,st:p.st,stt:p.stt,reads:[],tried:[]}); };
  const links=[];
  K.links.forEach(l=>{ const k=byId[l.key], t=letter(l.target); if(!k||!t) return;
    const e={source:k,target:t,how:l.how||'',note:l.note||'',e:ecls(l.how||'')}; links.push(e); k.reads.push(e); t.reads.push(e); });
  (K.tried||[]).forEach(l=>{ const k=byId[l.key], t=letter(l.target); if(!k||!t) return;
    const e={source:k,target:t,how:'tried',note:l.note||'',e:'tried'}; links.push(e); k.tried.push(e); t.tried.push(e); });
  (K.source_links||[]).forEach(l=>{ const s=byId[l.source], k=byId[l.key]; if(!s||!k) return; links.push({source:s,target:k,how:'src',e:'src',me:s.id==='s-cyphersolver'}); k.srcIds.add(s.id); if(s.id!=='s-cyphersolver') k.srcs.push(s.label); });
  for(let i=nodes.length-1;i>=0;i--){ const n=nodes[i]; if(n.type==='key'&&!n.reads.length&&!n.tried.length){ delete byId[n.id]; nodes.splice(i,1); } }
  nodes.forEach(n=>{
    if(n.type==='key'){ n.letters=new Set(n.reads.map(e=>e.target.slug)).size; n.tonly=!n.letters; }
    if(n.type==='t') n.tonly=!n.reads.length;
    n.hay=(n.type==='key'?[n.id,n.label,n.by,n.kind,n.note,n.year,n.found,...n.srcs,...[...n.reads,...n.tried].flatMap(e=>[e.target.slug,e.target.label,e.note])]
         :n.type==='t'?[n.slug,n.label,...[...n.reads,...n.tried].flatMap(e=>[e.source.label,e.note])]:[n.label]).join(' ').toLowerCase();
    // the graph's short name: the part before any bracket, then cut
    const s=n.type==='t'?n.label.replace(/\s*\(.*?\)\s*/g,' ').trim():(n.label.replace(/\s*\(.*$/,'').length>=10?n.label.replace(/\s*\(.*$/,''):n.label);
    n.sh=s.length>38?s.slice(0,36)+'…':s;
  });
  const keys=nodes.filter(n=>n.type==='key');

  // stats
  const lset=new Set(K.links.map(l=>l.target).filter(s=>page[s])), ntried=(K.tried||[]).length;
  document.getElementById('kwstats').innerHTML=[[keys.filter(k=>k.letters).length,'keys used on a letter'],[lset.size,'letters and series they were used on'],
    [keys.filter(k=>k.letters>=2).length,'keys used on more than one'],[keys.filter(k=>k.band==='here'&&k.letters).length,'keys rebuilt here'],[ntried,'tests of a key that did not fit']]
    .map(([n,t])=>`<span><b>${n}</b>${t}</span>`).join('');

  // layout: years on x, computed from a fixed seed so the web looks the same on every visit. It is a function of whether failed
  // tests count: a group of one key and one letter goes to the strip, a group of three or more to the graph
  const kyear=k=>{ const ys=[...k.reads,...(k.letters?[]:k.tried)].map(e=>e.target.date).filter(y=>y!=null); return ys.length?d3.mean(ys):(k.year||1600); };
  nodes.forEach(n=>{ n.y0=n.type==='t'?(n.date??1600):n.type==='key'?kyear(n):null; });
  const ext=d3.extent(nodes.filter(n=>n.type!=='src'),n=>n.y0), x=d3.scaleLinear().domain([Math.floor(ext[0]/25)*25,Math.ceil(ext[1]/25)*25]).range([70,W-70]);
  const deg=n=>n.type==='key'?n.letters:0, hubN=s=>links.filter(l=>l.source===s).length;
  let sim, pairs=[];
  function place(withTried){
    const counted=l=>l.e!=='src'&&(withTried||l.e!=='tried');
    const up=new Map(nodes.map(n=>[n,n])), find=a=>{ while(up.get(a)!==a){ up.set(a,up.get(up.get(a))); a=up.get(a); } return a; };
    links.filter(counted).forEach(l=>{ if(up.has(l.source)&&up.has(l.target)) up.set(find(l.source),find(l.target)); });
    const size=d3.rollup(nodes,v=>v.length,find);
    nodes.forEach(n=>{ const s=size.get(find(n)); n.strip=n.type!=='src'&&s===2; n.ing=n.type!=='src'&&s>=3; });
    const one=new Map(); links.filter(l=>counted(l)&&l.source.strip).forEach(l=>{ if(!one.has(l.source)) one.set(l.source,{key:l.source,letter:l.target,e:l.e,date:l.target.date??l.source.y0}); });
    pairs=[...one.values()];
    nodes.filter(n=>n.type==='src').forEach(s=>{ const ks=links.filter(l=>l.source===s&&l.target.ing).map(l=>l.target.y0); s.ing=ks.length>0; s.y0=ks.length?d3.mean(ks):1600; });
    const on=nodes.filter(n=>n.ing), ls=links.filter(l=>l.source.ing&&l.target.ing&&(l.e==='src'||counted(l)));
    const rnd=d3.randomLcg(0.4242);
    on.forEach(n=>{ n.x=x(n.y0)+(rnd()-.5)*20; n.y=H/2+(rnd()-.5)*H*.42; n.vx=n.vy=0; n.fx=n.fy=null; });
    sim=d3.forceSimulation(on).randomSource(rnd)
      .force('link',d3.forceLink(ls).distance(l=>l.e==='src'?110:l.e==='tried'?60:40).strength(l=>l.e==='src'?.05:l.e==='tried'?(l.source.tonly?.6:.05):.75))
      .force('charge',d3.forceManyBody().strength(n=>n.type==='t'?-80:n.type==='src'?-160:-160-deg(n)*30).distanceMax(320))
      .force('x',d3.forceX(n=>x(n.y0)).strength(n=>n.type==='src'?.03:.2))
      .force('y',d3.forceY(H/2).strength(withTried?.1:.04))
      .force('collide',d3.forceCollide(n=>n.type==='t'?9:n.type==='src'?28:12+deg(n)*2))
      .stop();
    for(let i=0;i<420;i++) sim.tick();
    on.forEach(n=>{ n.x=Math.max(30,Math.min(W-30,n.x)); n.y=Math.max(30,Math.min(H-60,n.y)); });
    sim.on('tick',draw);
  }

  // drawing
  const svg=d3.select(root).insert('svg',':first-child').attr('viewBox',`0 0 ${W} ${H}`).attr('role','img').style('aspect-ratio',`${W}/${H}`)
    .attr('aria-label','Network of cipher keys and the letters they were used on');
  const view=svg.append('g');
  const ax=view.append('g').attr('class','axis');
  x.ticks(8).forEach(t=>{ ax.append('line').attr('x1',x(t)).attr('x2',x(t)).attr('y1',10).attr('y2',H-40);
    ax.append('text').attr('x',x(t)).attr('y',H-26).attr('text-anchor','middle').text(t); });
  const lk=view.append('g').selectAll('path').data(links).join('path').attr('class',l=>'lk '+l.e+(l.me?' me':''));
  const nd=view.append('g').selectAll('g').data(nodes).join('g')
    .attr('class',n=>['nd',n.type,n.band?'b-'+n.band:'',n.st||'',n.tonly?'tonly':'',n.id==='s-cyphersolver'?'me':''].join(' '))
    .attr('tabindex',0).attr('role','button').attr('aria-label',n=>n.label);
  const KEYPATH='M-3,-2.5a4.5,4.5 0 1,1 0,5h10l2,-2.5l-2,-2.5z';          // a small key: bow and blade
  nd.filter(n=>n.type==='key').append('path').attr('d',KEYPATH).attr('transform',n=>`scale(${1.05+Math.min(n.letters,8)*.32})`);
  nd.filter(n=>n.type==='src').append('circle').attr('r',n=>7+Math.sqrt(hubN(n))*1.3);
  nd.filter(n=>n.type==='t').append('circle').attr('r',n=>3.5+Math.min(n.reads.length+n.tried.length,4));
  nd.append('text').attr('dy',n=>n.type==='t'?'-.9em':n.type==='src'?'2.3em':'1.9em').text(n=>n.sh);
  const arc=l=>{ const dx=l.target.x-l.source.x, dy=l.target.y-l.source.y, dr=Math.hypot(dx,dy)*1.6;
    return `M${l.source.x},${l.source.y}A${dr},${dr} 0 0,1 ${l.target.x},${l.target.y}`; };
  function draw(){ lk.attr('d',l=>l.source.ing&&l.target.ing?arc(l):null); nd.attr('transform',n=>n.ing?`translate(${n.x},${n.y})`:null); }

  // standing labels: sources and keys biggest first, then letters when there is room, skipping overlaps. Near the edges a label
  // runs inward so it is not cut off
  function labels(withTried){
    const boxes=[], fits=(n,w,y0,y1)=>{ n.anc=n.x<w/2+12?'start':n.x>W-w/2-12?'end':'middle';
      const x0=n.anc==='start'?n.x-6:n.anc==='end'?n.x-w+6:n.x-w/2, b={x0,x1:x0+w,y0:n.y+y0,y1:n.y+y1};
      if(boxes.some(o=>b.x0<o.x1&&b.x1>o.x0&&b.y0<o.y1&&b.y1>o.y0)) return false; boxes.push(b); return true; };
    nodes.forEach(n=>{ n.lab=false; n.anc='middle'; });
    nodes.filter(n=>n.ing&&(n.type==='src'||(n.type==='key'&&(!withTried||n.letters>=2)))).sort((a,b)=>(b.type==='src')-(a.type==='src')||deg(b)-deg(a)).forEach(n=>{ n.lab=fits(n,n.sh.length*6.2*CW,narrow?16:8,narrow?33:24); });
    if(!withTried&&!narrow) nodes.filter(n=>n.ing&&n.type==='t').forEach(n=>{ n.lab=fits(n,n.sh.length*5.2,-20,-6); });
    nd.classed('lab',n=>!!n.lab); nd.select('text').attr('text-anchor',n=>n.anc||'middle');
  }

  // zoom and pan; labels keep their size as you zoom in
  const zoom=d3.zoom().scaleExtent([.6,8]).on('zoom',e=>{ view.attr('transform',e.transform);
    nd.selectAll('text').attr('transform',`scale(${1/Math.sqrt(e.transform.k)})`); });
  svg.call(zoom).on('dblclick.zoom',null);
  const fit=(ns,dur=600,kmax=8)=>{ const xs=ns.map(n=>n.x), ys=ns.map(n=>n.y); if(!ns.length) return;
    const [x0,x1]=d3.extent(xs), [y0,y1]=d3.extent(ys), k=Math.min(kmax,.85/Math.max((x1-x0+80)/W,(y1-y0+80)/H));
    const to=d3.zoomIdentity.translate(W/2,H/2).scale(Math.max(.6,k)).translate(-(x0+x1)/2,-(y0+y1)/2);
    if(matchMedia('(prefers-reduced-motion: reduce)').matches||document.hidden) svg.call(zoom.transform,to);
    else svg.transition().duration(dur).call(zoom.transform,to); };
  document.getElementById('kwfit').addEventListener('click',()=>fit(nodes.filter(n=>n.ing&&!hidden(n)),500));
  const lb=document.getElementById('kwlabels');
  lb.addEventListener('click',()=>{ const on=!root.classList.contains('all'); root.classList.toggle('all',on); lb.setAttribute('aria-pressed',on); });

  // drag a node (a light reheat of the layout)
  nd.call(d3.drag().on('start',(e,n)=>{ if(!e.active) sim.alpha(.15).restart(); n.fx=n.x; n.fy=n.y; })
    .on('drag',(e,n)=>{ n.fx=e.x; n.fy=e.y; }).on('end',(e,n)=>{ if(!e.active) sim.alphaTarget(0); n.fx=null; n.fy=null; }));

  // the strip: one mark per lone key and letter, at the letter's date, stacked like a histogram; key on the left, letter on the right.
  // The nearest mark answers the pointer, so small marks are still easy to hit
  const stripBox=document.getElementById('kwstripbox'), tip=document.getElementById('kwtip');
  const strip=d3.select(stripBox).insert('svg',':first-child').attr('tabindex',0).attr('aria-label','Keys used on one letter alone, by date. Arrow keys move, Enter opens the card');
  let marks=strip.selectAll('g.pr'), hotPair=null;
  const shownPairs=()=>pairs.filter(p=>!hidden(p.key)&&!hidden(p.letter)).sort((a,b)=>a.date-b.date);
  function renderStrip(){
    const w=stripBox.clientWidth||600, pw=w<500?9:13, ph=8, axisH=20, sx=x.copy().range([10,w-10]), rows=[], ps=[...pairs].sort((a,b)=>a.date-b.date);
    ps.forEach(p=>{ const t=sx(p.date); let r=rows.findIndex(e=>e+pw-t<=pw); if(r<0){ r=rows.length; rows.push(-1e9); } p.cx=Math.max(t,rows[r]+pw); rows[r]=p.cx; p.r=r; });   // a mark may slide up to one mark right of its date
    const h=rows.length*ph+6+axisH, base=h-axisH, half=(pw-2)/2;
    strip.attr('viewBox',`0 0 ${w} ${h}`).attr('height',h).selectAll('*').remove();
    const a=strip.append('g').attr('class','axis'); a.append('line').attr('x1',0).attr('x2',w).attr('y1',base+1).attr('y2',base+1);
    sx.ticks(w<500?5:8).forEach(t=>a.append('text').attr('x',sx(t)).attr('y',base+14).attr('text-anchor','middle').text(t));
    marks=strip.append('g').selectAll('g').data(ps).join('g').attr('class',p=>`pr b-${p.key.band} ${p.letter.st||''}${p.e==='tried'?' tr':''}`)
      .attr('transform',p=>`translate(${p.cx-half},${base-(p.r+1)*ph})`);
    marks.append('rect').attr('class','mk').attr('width',half).attr('height',ph-1.5);
    marks.append('rect').attr('class','ml').attr('x',half).attr('width',half).attr('height',ph-1.5);
    ps.forEach(p=>{ p.my=base-(p.r+.5)*ph; });
    document.getElementById('kwstripn').textContent=pairs.length;
  }
  function hotMark(p){ hotPair=p; marks.classed('hot',q=>q===p);
    if(!p){ tip.hidden=true; return; }
    tip.textContent=`${p.key.label} → ${p.letter.label}${p.letter.date!=null?' ('+yr(p.letter.date)+')':''}`; tip.hidden=false;
    const w=stripBox.clientWidth, half=tip.offsetWidth/2; tip.style.left=Math.max(half,Math.min(w-half,p.cx))+'px'; tip.style.top=(p.my-8)+'px'; }
  const nearest=e=>{ const [mx,my]=d3.pointer(e,strip.node()); let best=null, bd=18*18; shownPairs().forEach(p=>{ const d=(p.cx-mx)**2+(p.my-my)**2; if(d<bd){ bd=d; best=p; } }); return best; };
  strip.on('pointermove',e=>{ if(e.pointerType!=='touch') hotMark(nearest(e)); }).on('pointerleave',()=>hotMark(null))
    .on('click',e=>{ const p=nearest(e); if(p){ hotMark(null); pin(pinned===p.key?null:p.key); } });
  strip.on('blur',()=>hotMark(null)).on('keydown',e=>{ const ps=shownPairs(), i=ps.indexOf(hotPair);
    if(e.key==='ArrowRight'||e.key==='ArrowDown'){ e.preventDefault(); hotMark(ps[Math.min(ps.length-1,i+1)]); }
    else if(e.key==='ArrowLeft'||e.key==='ArrowUp'){ e.preventDefault(); hotMark(ps[Math.max(0,i<0?0:i-1)]); }
    else if((e.key==='Enter'||e.key===' ')&&hotPair){ e.preventDefault(); pin(hotPair.key); } });

  // filters: bands, edge kinds, one source and a search. Failed tests start hidden; the rest dims rather than disappears
  const st={q:'',src:null,bands:new Set(BANDS.map(b=>b[0])),edges:new Set(['rebuilt','unchanged','adapted'])};
  const chips=(el,list,set,cls,after)=>{ el.innerHTML=list.map(([id,label])=>`<button type="button" class="kw-chip ${cls(id)}" data-v="${id}" aria-pressed="${set.has(id)}">${cls(id).startsWith('e-')?'<i></i>':''}${esc(label)}</button>`).join('');
    el.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; const v=b.dataset.v;
      set.has(v)?set.delete(v):set.add(v); b.setAttribute('aria-pressed',set.has(v)); after?after(v):apply(); }); };
  chips(document.getElementById('kwband'),BANDS,st.bands,id=>'b-'+id);
  chips(document.getElementById('kwedge'),EDGES,st.edges,id=>'e-'+id,v=>v==='tried'?relayout():apply());
  // one source at a time: its spokes appear in the graph and its keys stay lit, in the strip too
  const srcEl=document.getElementById('kwsrc'), srcs=nodes.filter(n=>n.type==='src').sort((a,b)=>hubN(b)-hubN(a));
  srcEl.innerHTML='<span class="kw-lab">Held or published by</span>'+srcs.map(s=>`<button type="button" class="kw-chip" data-v="${esc(s.id)}" aria-pressed="false">${esc(s.label.replace(/\s*\(.*$/,''))} <small>${hubN(s)}</small></button>`).join('');
  srcEl.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; st.src=st.src===b.dataset.v?null:b.dataset.v;
    srcEl.querySelectorAll('button').forEach(o=>o.setAttribute('aria-pressed',o.dataset.v===st.src)); apply(); });
  const q=document.getElementById('kwq');
  q.addEventListener('input',()=>{ st.q=q.value.trim().toLowerCase(); apply(); });
  q.addEventListener('keydown',e=>{ if(e.key==='Enter'){ const m=nodes.filter(n=>n.type!=='src'&&n.ing&&!hidden(n)&&matches(n)); if(m.length) fit(m.length>40?m.slice(0,40):m); else if(pairs.some(p=>keyOn(p.key))) stripBox.scrollIntoView({block:'center'}); } });
  const showE=l=>l.e==='src'||st.edges.has(l.e);
  const hidden=n=>n.type==='src'?false:![...n.reads,...n.tried].some(showE);
  const matches=n=>(!st.q||st.q.split(/\s+/).every(w=>n.hay.includes(w)));
  const keyOn=k=>st.bands.has(k.band)&&matches(k)&&(!st.src||k.srcIds.has(st.src));
  const lit=n=>n.type==='key'?keyOn(n):n.type==='t'?((st.q&&matches(n))||[...n.reads,...n.tried].some(l=>showE(l)&&keyOn(l.source))):(n.id===st.src||(!st.q&&!st.src));
  function apply(){
    nd.style('display',n=>!n.ing||hidden(n)?'none':null).classed('dim',n=>!lit(n));
    lk.style('display',l=>l.source.ing&&l.target.ing&&showE(l)&&!hidden(l.source)&&!hidden(l.target)?null:'none').classed('dim',l=>l.e==='src'?l.source.id!==st.src&&!!st.q:!(keyOn(l.source)))
      .classed('on',l=>l.e==='src'&&l.source.id===st.src);
    marks.style('display',p=>hidden(p.key)||hidden(p.letter)?'none':null).classed('dim',p=>!keyOn(p.key)).classed('pin',p=>p.key===pinned||p.letter===pinned);
    const shown=keys.filter(k=>!hidden(k)&&keyOn(k)).length;
    document.getElementById('kwcount').textContent=`${shown} of ${keys.length} keys`;
    renderTried();
  }
  function relayout(){ place(st.edges.has('tried')); labels(st.edges.has('tried')); renderStrip(); svg.interrupt().call(zoom.transform,d3.zoomIdentity); draw(); apply(); focus(pinned); }
  const setTried=()=>{ if(st.edges.has('tried')) return; st.edges.add('tried'); document.querySelector('#kwedge [data-v="tried"]').setAttribute('aria-pressed','true'); relayout(); };

  // focus: a node, its edges and neighbours; a click pins it and opens its card
  const side=document.getElementById('kwside'), card=document.getElementById('kwcard'), idle=card.innerHTML;
  const nb=n=>links.filter(l=>(l.source===n||l.target===n)&&showE(l));
  function focus(n){
    root.classList.toggle('focus',!!n&&n.ing);
    if(!n){ nd.classed('hot',false); lk.classed('hot',false); return; }
    const ls=nb(n), set=new Set([n]); ls.forEach(l=>{ set.add(l.source); set.add(l.target); });
    nd.classed('hot',d=>set.has(d)); lk.classed('hot',l=>ls.includes(l));
  }
  const decode=k=>{ const m=(k.kind==='DECODE key record')&&(k.label.match(/\bR(\d{2,5})\b/)||k.id.match(/^k-r(\d{2,5})$/)); return m?`https://de-crypt.org/decrypt-web/RecordsView/${m[1]}`:null; };
  const howNote=e=>[HOW[e.how]??e.how,e.note].filter(Boolean).map(esc).join(' · ');
  const tli=e=>`<li><a href="${e.target.slug}.html">${esc(e.target.label)}</a><small>${[howNote(e),e.target.date!=null?yr(e.target.date):'',esc(e.target.stt)].filter(Boolean).join(' · ')}</small></li>`;
  const kli=e=>`<li><button type="button" class="kn" data-key="${esc(e.source.id)}">${esc(e.source.label)}</button><small>${howNote(e)}</small></li>`;
  function cardFor(n){
    if(n.type==='key'){ const bl=BANDS.find(b=>b[0]===n.band)[1], dl=decode(n);
      return `<p class="k">${esc(n.kind)}${n.band==='period'?' · '+bl:''}</p><h3>${esc(n.label)}</h3>
      <p class="by">${[n.by,n.year&&('key of '+n.year),n.found&&((n.band==='scholar'?'published ':'found ')+n.found)].filter(Boolean).map(esc).join(' · ')}${n.srcs.length?'<br>Held or published by '+n.srcs.map(esc).join(', '):''}</p>
      ${n.image?`<figure data-credit="${esc(n.image.credit)}"><a href="${esc(n.image.page)}.html"><img src="${esc(n.image.src)}" alt="${esc(n.image.caption||n.label)}" loading="lazy"></a><figcaption>${esc((n.image.caption||'').slice(0,160))}${(n.image.caption||'').length>160?'…':''} <span class="credit">Image: ${esc(n.image.credit)}</span></figcaption></figure>`:''}
      <p>${esc(n.note)}</p>
      ${n.reads.length?`<h4>Used on ${n.letters} letter${n.letters>1?'s':''}</h4><ul>${n.reads.map(tli).join('')}</ul>`:''}
      ${n.tried.length?`<h4>Tried, did not fit</h4><ul>${n.tried.map(tli).join('')}</ul>`:''}
      <div class="acts"><button type="button" data-copy>Copy link</button>${dl?`<a href="${dl}" rel="noopener">DECODE record &#8599;</a>`:''}</div>`; }
    if(n.type==='t') return `<p class="k">Letter · ${esc(n.stt)}${n.date!=null?' · '+yr(n.date):''}</p><h3><a href="${n.slug}.html">${esc(n.label)}</a></h3>
      ${n.reads.length?`<h4>Keys used</h4><ul>${n.reads.map(kli).join('')}</ul>`:''}${n.tried.length?`<h4>Tried, did not fit</h4><ul>${n.tried.map(kli).join('')}</ul>`:''}
      <div class="acts"><a href="${n.slug}.html">Open the write-up &rarr;</a></div>`;
    const ks=links.filter(l=>l.source===n).map(l=>l.target);
    return `<p class="k">Source</p><h3>${esc(n.label)}</h3><ul>${ks.map(k=>`<li><button type="button" class="kn" data-key="${esc(k.id)}">${esc(k.label)}</button><small>${k.letters} letter${k.letters===1?'':'s'}</small></li>`).join('')}</ul>`;
  }
  let pinned=null;
  function pin(n,{zoomTo=false,push=true}={}){
    pinned=n||null;
    if(n&&n.type==='key'&&n.tonly) setTried();
    nd.classed('pin',d=>d===pinned); marks.classed('pin',p=>p.key===pinned||p.letter===pinned); focus(pinned);
    if(!n){ card.innerHTML=idle; side.classList.remove('open'); if(push) history.replaceState(null,'',location.pathname+location.search); return; }
    card.innerHTML=cardFor(n); side.classList.add('open'); side.scrollTop=0;
    if(push&&n.type==='key') history.replaceState(null,'','#'+n.id);
    if(zoomTo&&n.ing){ const ns=[n,...nb(n).filter(l=>l.e!=='src').map(l=>l.source===n?l.target:l.source)]; fit(ns,600,4); }
  }
  nd.on('pointerenter',(e,n)=>{ if(!pinned&&e.pointerType!=='touch') focus(n); }).on('pointerleave',()=>{ if(!pinned) focus(null); })
    .on('focus',(e,n)=>{ if(!pinned) focus(n); }).on('blur',()=>{ if(!pinned) focus(null); })
    .on('click',(e,n)=>{ e.stopPropagation(); pin(pinned===n?null:n); })
    .on('keydown',(e,n)=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); pin(n); } });
  svg.on('click',e=>{ if(e.defaultPrevented) return; if(pinned) pin(null); });
  document.addEventListener('click',e=>{
    const b=e.target.closest('[data-key]'); if(b){ const n=byId[b.dataset.key]; if(n){ if(b.dataset.tried) setTried(); pin(n,{zoomTo:true}); (n.strip?stripBox:root).scrollIntoView({block:'nearest'}); } return; }
    if(e.target.closest('[data-copy]')){ const u=location.href; (navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(()=>{ e.target.textContent='Link copied'; },()=>prompt('Link to this key',u)); }
  });
  side.querySelector('.x').addEventListener('click',()=>pin(null));
  document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&pinned&&!document.querySelector('#search:not([hidden])')) pin(null); });

  // places to start: the key that did the most work, a key rebuilt and reused, a famous table, the letter that ruled out the most keys
  const most=d3.greatest(nodes.filter(n=>n.type==='t'),n=>n.tried.length);
  const START=[['k-lasry-gl',n=>`Lasry's French keys, used on ${n.letters} letters`],['k-balbases',n=>`Balbases key: rebuilt from ten letters, used on ${n.letters-1} more`],
    ['k-grandchiffre1812-shd',()=>'The Grand Chiffre of 1812'],[most.id,n=>`${n.tried.length} keys ruled out on ${n.sh}`,true]];
  document.getElementById('kwstart').insertAdjacentHTML('beforeend',START.filter(s=>byId[s[0]]).map(([id,f,t])=>`<button type="button" class="kw-chip" data-key="${esc(id)}"${t?' data-tried="1"':''}>${esc(f(byId[id]))}</button>`).join(''));

  // keys tried and ruled out, grouped by letter in date order; twelve until asked for all, or while a search or filter is on
  let showAll=false;
  document.getElementById('triedlist').insertAdjacentHTML('afterend','<button type="button" class="kw-chip" id="triedmore" hidden></button>');
  const more=document.getElementById('triedmore'); more.addEventListener('click',()=>{ showAll=true; renderTried(); });
  function renderTried(){
    const ts=nodes.filter(n=>n.type==='t'&&n.tried.some(e=>keyOn(e.source))).sort((a,b)=>(a.date??0)-(b.date??0));
    const filtered=st.q||st.src||st.bands.size<BANDS.length, list=showAll||filtered?ts:ts.slice(0,12);
    more.hidden=list.length===ts.length; more.textContent=`Show all ${ts.length} letters`;
    document.getElementById('triedlist').innerHTML=list.map(t=>`<li><div class="tgt"><a href="${t.slug}.html">${esc(t.label)}</a><small>${t.date!=null?yr(t.date)+' · ':''}${esc(t.stt)}</small></div>
      <ul>${t.tried.filter(e=>keyOn(e.source)).map(e=>`<li><button type="button" class="kn" data-key="${esc(e.source.id)}">${esc(e.source.label)}</button>${e.note?' — '+esc(e.note):''}</li>`).join('')}</ul></li>`).join('')
      ||'<li class="kw-help">No ruled-out key matches.</li>';
  }

  const fromHash=()=>{ const h=decodeURIComponent(location.hash.slice(1));
    if(h.startsWith('q=')){ q.value=h.slice(2); st.q=h.slice(2).toLowerCase(); apply(); }
    else if(byId[h]){ pin(byId[h],{zoomTo:true,push:false}); const el=byId[h].strip?stripBox:root; window.scrollTo({top:el.getBoundingClientRect().top+scrollY-90,behavior:'instant'}); } };
  window.addEventListener('hashchange',fromHash);
  place(false); labels(false); renderStrip(); draw(); apply();
  let stripW=stripBox.clientWidth;
  new ResizeObserver(()=>{ if(stripBox.clientWidth!==stripW){ stripW=stripBox.clientWidth; renderStrip(); apply(); } }).observe(stripBox);
  setTimeout(fromHash,80);   // after the layout settles, or the scroll to the web lands short
})();
