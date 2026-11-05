// Deep-zoom viewer: click any figure image in a page to open it full screen in OpenSeadragon (loaded on first use).
// If docs/zoom/<image name>.json exists, its lines are laid over the scan where they are written, each with its
// reading, and a switch hides them.  Data: {image, source, iiif?, lines:[{x, y, w, h, text, gloss}]}, box in
// fractions of the image; "iiif" (an info.json URL) replaces the local image with the archive's full-resolution one.
(()=>{
  const imgs=[...document.querySelectorAll('main figure img, figure.lead img')].filter(i=>!i.closest('a'));
  if(!imgs.length) return;
  const OSD='https://cdn.jsdelivr.net/npm/openseadragon@4.1.1/build/openseadragon/openseadragon.min.js';
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  let lib=null, box=null, viewer=null, lastFocus=null;
  const load=()=>lib||(lib=new Promise((ok,no)=>{ const s=document.createElement('script'); s.src=OSD; s.onload=()=>ok(window.OpenSeadragon); s.onerror=no; document.head.appendChild(s); }));
  const name=src=>src.split('/').pop().split('?')[0].replace(/\.[a-z]+$/i,'');
  imgs.forEach(img=>{ img.classList.add('zoomable'); img.tabIndex=0; img.setAttribute('role','button');
    img.setAttribute('aria-label',(img.alt?img.alt+'. ':'')+'Open in the zoom viewer');
    img.addEventListener('click',()=>open(img)); img.addEventListener('keydown',e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); open(img); } }); });

  function shell(){
    box=document.createElement('div'); box.className='zv'; box.setAttribute('role','dialog'); box.setAttribute('aria-modal','true'); box.hidden=true;
    box.innerHTML=`<div class="zv-bar"><p class="zv-cap"></p><div class="zv-btns">
      <button type="button" class="zv-tr" aria-pressed="true" hidden>Transcription</button>
      <button type="button" data-z="out" aria-label="Zoom out">&minus;</button><button type="button" data-z="in" aria-label="Zoom in">+</button>
      <button type="button" data-z="home" aria-label="Fit to screen">&#8634;</button>
      <button type="button" class="zv-x" aria-label="Close the viewer">&times;</button></div></div>
      <div class="zv-view"></div><p class="zv-src"></p>`;
    document.body.appendChild(box);
    box.querySelector('.zv-x').addEventListener('click',close);
    box.querySelectorAll('[data-z]').forEach(b=>b.addEventListener('click',()=>{ if(!viewer) return; const vp=viewer.viewport;
      if(b.dataset.z==='home') vp.goHome(); else vp.zoomBy(b.dataset.z==='in'?1.6:1/1.6); vp.applyConstraints(); }));
    box.querySelector('.zv-tr').addEventListener('click',e=>{ const v=box.classList.toggle('zv-off'); e.currentTarget.setAttribute('aria-pressed',!v); });
    box.addEventListener('keydown',e=>{ if(e.key==='Escape') close();
      if(e.key==='Tab'){ const f=[...box.querySelectorAll('button:not([hidden])')]; const i=f.indexOf(document.activeElement);
        if(e.shiftKey && i<=0){ e.preventDefault(); f[f.length-1].focus(); } else if(!e.shiftKey && i===f.length-1){ e.preventDefault(); f[0].focus(); } } });
  }
  async function open(img){
    if(!box) shell(); lastFocus=document.activeElement;
    const fig=img.closest('figure'), cap=fig && fig.querySelector('figcaption');
    box.querySelector('.zv-cap').innerHTML=cap?cap.innerHTML:esc(img.alt);
    box.querySelector('.zv-src').textContent=''; box.classList.remove('zv-off');
    const tr=box.querySelector('.zv-tr'); tr.hidden=true; tr.setAttribute('aria-pressed','true');
    box.hidden=false; document.documentElement.classList.add('zv-lock'); box.querySelector('.zv-x').focus();
    let data=null; try{ const r=await fetch('zoom/'+name(img.getAttribute('src'))+'.json'); if(r.ok) data=await r.json(); }catch(e){}
    let OS; try{ OS=await load(); }catch(e){ box.querySelector('.zv-view').innerHTML='<p class="zv-err">The zoom viewer could not be loaded.</p>'; return; }
    if(viewer){ viewer.destroy(); viewer=null; }
    const view=box.querySelector('.zv-view'); view.innerHTML='';
    viewer=OS({element:view,tileSources:data&&data.iiif?data.iiif:{type:'image',url:img.src},
      showNavigationControl:false,showNavigator:true,navigatorPosition:'BOTTOM_RIGHT',maxZoomPixelRatio:4,visibilityRatio:.6,
      animationTime:matchMedia('(prefers-reduced-motion: reduce)').matches?0:1.1,gestureSettingsMouse:{clickToZoom:false,dblClickToZoom:true}});
    if(!data || !(data.lines||[]).length) return;
    tr.hidden=false;
    if(data.source) box.querySelector('.zv-src').textContent='Transcription from '+data.source+'. Lines are placed by eye on the scan.';
    viewer.addOnceHandler('open',()=>{
      const size=viewer.world.getItemAt(0).getContentSize(), ar=size.y/size.x, els=[];
      data.lines.forEach((l,i)=>{ const el=document.createElement('div'); el.className='zv-line';
        el.innerHTML=`<div class="in"><span class="t">${esc(l.text)}</span>${l.gloss?`<span class="gl">${esc(l.gloss)}</span>`:''}</div>`;
        el._n=Math.max([...l.text].length*.62,l.gloss?[...l.gloss].length*.5*1.15:0,4);
        el.title=l.gloss?`${l.text} — ${l.gloss}`:l.text;
        viewer.addOverlay({element:el,location:new OS.Rect(l.x,l.y*ar,l.w,l.h*ar)}); els.push(el); });
      const fit=()=>els.forEach(el=>{ const r=el.getBoundingClientRect(), two=!!el.querySelector('.gl');
        el.style.fontSize=Math.max(6,Math.min(r.height*(two?.38:.6),(r.width-6)/el._n))+'px'; });
      viewer.addHandler('update-viewport',fit); fit();
    });
  }
  function close(){ if(!box||box.hidden) return; box.hidden=true; document.documentElement.classList.remove('zv-lock');
    if(viewer){ viewer.destroy(); viewer=null; } if(lastFocus) lastFocus.focus(); }
})();
