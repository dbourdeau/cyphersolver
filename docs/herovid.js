// The site's pixel-art videos (tools/hero_video): the front page's and the contribute page's. Until someone plays
// one, it loops muted on its own (the only autoplay browsers allow), with its narration burned in as captions. Once
// they play it (sound, play or a chapter), it plays once and is not started again by itself, on this visit or a
// later one (remembered in localStorage). Never starts by itself for reduced motion; pauses while scrolled away.
// Without JavaScript the browser's own controls are shown.
// The figure's data-links, written by the renderer, are [from, to, href, label]: with a 'to', a link under the
// chapters while that stretch plays (the write-up of the cipher on screen, the ledger, the catalogue); with none,
// a button over the close and over the poster after the end. '#random' opens a random write-up.
(()=>{
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const random=async()=>{ const rb=document.querySelector('.randbtn'); if(rb){ rb.click(); return; }
    try{ const ps=await (await fetch('pages.json')).json(); location.href=ps[Math.floor(Math.random()*ps.length)].slug+'.html'; }
    catch(e){ location.href='writeups.html'; } };
  document.querySelectorAll('.herovid').forEach(hv=>{
    const v=hv.querySelector('video'), tg=hv.querySelector('.hv-toggle'), mu=hv.querySelector('.hv-mute'),
      snd=hv.querySelector('.hv-sound'), chs=[...hv.querySelectorAll('.hv-ch button')];
    const T=chs.map(b=>+b.dataset.t), KEY=hv.dataset.key||'hero-video-played';
    let links=[]; try{ links=JSON.parse(hv.dataset.links||'[]'); }catch(e){}
    const during=links.filter(l=>l[1]!=null), end=links.filter(l=>l[1]==null), endAt=end.length?end[0][0]:Infinity;
    let played=false; try{ played=localStorage.getItem(KEY)==='1'; }catch(e){}
    // on a phone, or with data saving on, the poster waits for a tap and nothing of the video is fetched before it
    const lite=matchMedia('(max-width:760px)').matches || !!(navigator.connection&&navigator.connection.saveData);
    let held=still||played||lite||hv.hasAttribute('data-wait'), mine=false, over=false;   // data-wait: in a dialog, opened by a button (home.js)
    v.controls=false;
    hv.classList.add('fresh');
    if(lite){ v.preload='none'; hv.classList.add('lite'); const sh=snd.querySelector('.hv-short'); if(sh) sh.textContent='Play, with sound'; }

    // the link under the chapters, and the buttons over the end
    const goEl=document.createElement('p'); goEl.className='hv-go'; goEl.setAttribute('aria-live','polite');
    hv.querySelector('figcaption').append(goEl);
    const endEl=document.createElement('div'); endEl.className='hv-end';
    endEl.innerHTML=end.map((l,i)=>`<a class="${i?'':'first'}" href="${esc(l[2])}">${esc(l[3])} &rarr;</a>`).join('')
      +'<button type="button" class="again">Watch again</button>';
    hv.querySelector('.hv-frame').append(endEl);
    endEl.querySelectorAll('a[href="#random"]').forEach(a=>a.addEventListener('click',e=>{ e.preventDefault(); random(); }));
    let cur=null;
    const showGo=l=>{ if(l===cur) return; cur=l;
      goEl.innerHTML=l?`<a href="${esc(l[2])}">${esc(l[3])} &rarr;</a>`:''; goEl.classList.toggle('on',!!l); };

    const sync=()=>{ const p=v.paused, m=v.muted; hv.classList.toggle('paused',p); hv.classList.toggle('muted',m);
      tg.setAttribute('aria-pressed',String(p)); tg.setAttribute('aria-label',p?'Play the video':'Pause the video');
      mu.setAttribute('aria-pressed',String(m)); mu.setAttribute('aria-label',m?'Turn the sound on':'Turn the sound off'); };
    const go=()=>{ held=false; over=false; v.play().catch(()=>{}); };
    const own=()=>{ if(mine) return; mine=true; v.loop=false; hv.classList.remove('fresh');
      try{ localStorage.setItem(KEY,'1'); }catch(e){} };
    tg.addEventListener('click',()=>{ if(v.paused){ own(); go(); } else { held=true; v.pause(); } });
    mu.addEventListener('click',()=>{ own(); v.muted=!v.muted; if(!v.muted && v.paused) go(); });
    snd.addEventListener('click',()=>{ own(); v.muted=false; v.currentTime=0; go(); });
    endEl.querySelector('.again').addEventListener('click',()=>{ own(); v.currentTime=0; go(); });
    chs.forEach((b,i)=>b.addEventListener('click',()=>{ own(); v.currentTime=T[i]; go(); }));
    // at the end: back to the poster, with the buttons still over it
    v.addEventListener('ended',()=>{ held=true; over=true; v.load(); hv.classList.add('at-end'); });
    ['play','pause','volumechange','emptied'].forEach(e=>v.addEventListener(e,sync));
    v.addEventListener('timeupdate',()=>{ const t=v.currentTime, d=v.duration||60;
      chs.forEach((b,i)=>{ const a=T[i], z=i+1<T.length?T[i+1]:d;
        b.style.setProperty('--p',Math.max(0,Math.min(1,(t-a)/(z-a)))); b.classList.toggle('on',t>=a&&t<z); });
      showGo(during.find(l=>t>=l[0]&&t<l[1])||null);
      hv.classList.toggle('at-end',over||t>=endAt); });
    new IntersectionObserver(es=>es.forEach(e=>{
      if(!e.isIntersecting) v.pause(); else if(!held) v.play().catch(()=>{}); }),{threshold:.25}).observe(v);
    if(!held) v.play().catch(()=>{});
    sync();
  });
})();
