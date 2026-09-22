// cipher reveal: <figure class="creveal" data-src="reveal/slug.json"></figure> plus <script src="cipher-reveal.js" defer>.
// The groups scramble and settle into plaintext when the figure scrolls into view; hovering or focusing a group lights
// every occurrence of it, its homophones (other groups with the same value) and its row in the key.
// Data: {title, caption, unit, key_note, tokens:[{g, p, cls}]}, cls one of '' unk unc code plain null.
(()=>{
  const figs=document.querySelectorAll('.creveal[data-src]'); if(!figs.length) return;
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const GLYPHS='ABCDEFGHIKLMNOPQRSTVXYZabcdefghilmnopqrstuxyz0123456789§¶†‡∴⊕';
  const rnd=n=>{ let s=''; for(let i=0;i<n;i++) s+=GLYPHS[Math.random()*GLYPHS.length|0]; return s; };
  const isCipher=t=>t.g && t.cls!=='plain';

  function build(fig, d){
    const toks=d.tokens.map(t=>({g:t.g||'', p:t.p==null?'':String(t.p), cls:t.cls||''}));
    const ciph=toks.filter(isCipher);
    const key=new Map();                       // group -> {p, n, cls}
    for(const t of ciph){ const k=key.get(t.g)||{p:t.p,n:0,cls:t.cls}; k.n++; key.set(t.g,k); }
    const byP=new Map();                       // plaintext -> groups (homophones)
    for(const [g,k] of key){ if(!k.p.trim() || k.p==='?' || k.cls==='unk') continue; const s=byP.get(k.p)||[]; s.push(g); byP.set(k.p,s); }
    const read=ciph.filter(t=>t.cls!=='unk' && t.p!=='?').length;
    const unit=esc(d.unit||'groups');
    fig.innerHTML=`<div class="cr-head"><div><span class="cr-kick">Watch it decipher</span><h3>${esc(d.title||'')}</h3></div>
      <div class="cr-ctl"><button type="button" class="cr-play">&#8635; Replay</button>
      <button type="button" class="cr-mode" aria-pressed="false">Cipher only</button></div></div>
      <div class="cr-bar"><i></i></div>
      <div class="cr-tiles"></div>
      <p class="cr-info" aria-live="polite"><span>${ciph.length} ${unit} &middot; ${read} read &middot; ${key.size} distinct.</span> <span class="cr-hint">Hover or tab to a group to trace it through the text and the key.</span></p>
      <details class="cr-key"><summary>The key for this passage <span>${key.size} ${unit}</span></summary><div class="cr-grid"></div>${d.key_note?`<p class="cr-note">${esc(d.key_note)}</p>`:''}</details>
      ${d.caption?`<figcaption>${esc(d.caption)}</figcaption>`:''}`;
    const box=fig.querySelector('.cr-tiles'), grid=fig.querySelector('.cr-grid'), info=fig.querySelector('.cr-info'), bar=fig.querySelector('.cr-bar i');
    const els=toks.map(t=>{
      const el=document.createElement('span'); el.className='tile cr-t '+t.cls;
      el.innerHTML=`<span class="p"></span><span class="g">${esc(t.g||' ')}</span>`;
      if(isCipher(t)){ el.tabIndex=0; el.dataset.g=t.g; el.setAttribute('aria-label',`${t.g} = ${t.cls==='unk'?'unread':t.p}`); }
      el._p=el.firstChild; box.appendChild(el); return el;
    });
    const num=s=>/^\d+$/.test(s)?parseInt(s,10):NaN;
    const order=[...key.keys()].sort((a,b)=>{ const x=num(a),y=num(b); return (isNaN(x)||isNaN(y))?a.localeCompare(b):x-y; });
    const rows=new Map();
    for(const g of order){ const k=key.get(g); const r=document.createElement('button'); r.type='button'; r.className='cr-k '+k.cls;
      r.innerHTML=`<b>${esc(g)}</b><i>${esc(k.cls==='unk'?'?':(k.p.trim()?k.p:'␣'))}</i>${k.n>1?`<small>&times;${k.n}</small>`:''}`;
      r.dataset.g=g; grid.appendChild(r); rows.set(g,r); }

    const hint=info.innerHTML;
    let cur=null;
    function trace(g){
      if(g===cur) return; cur=g;
      fig.classList.toggle('tracing',!!g);
      els.forEach(el=>el.classList.remove('hl','hom')); rows.forEach(r=>r.classList.remove('hl','hom'));
      if(!g){ info.innerHTML=hint; return; }
      const k=key.get(g); const homs=(byP.get(k.p)||[]).filter(x=>x!==g);
      els.forEach(el=>{ if(el.dataset.g===g) el.classList.add('hl'); else if(homs.includes(el.dataset.g)) el.classList.add('hom'); });
      rows.get(g).classList.add('hl'); homs.forEach(h=>rows.get(h).classList.add('hom'));
      const val=k.cls==='unk'||k.p==='?'?'unread':(k.p.trim()?esc(k.p):'word break');
      info.innerHTML=`<b class="cr-g">${esc(g)}</b> = <b class="cr-p">${val}</b> &middot; ${k.n}&times; in this passage`+
        (homs.length?` &middot; <span class="cr-homs">also written ${homs.map(esc).join(', ')}</span> (homophones)`:'');
    }
    const on=e=>{ const t=e.target.closest('[data-g]'); if(t && fig.contains(t)) trace(t.dataset.g); };
    fig.addEventListener('pointerover',on); fig.addEventListener('focusin',on);
    fig.addEventListener('pointerleave',()=>trace(null));
    fig.addEventListener('focusout',e=>{ if(!fig.contains(e.relatedTarget)) trace(null); });
    grid.addEventListener('click',e=>{ const r=e.target.closest('[data-g]'); if(!r) return; cur=null; trace(r.dataset.g);
      els.find(el=>el.dataset.g===r.dataset.g).scrollIntoView({block:'nearest',behavior:still?'auto':'smooth'}); });

    let run=0;
    const settle=(el,t)=>{ el._p.textContent=t.p||' '; el.classList.add('done'); };
    function play(){
      const me=++run; fig.classList.remove('cipher'); fig.querySelector('.cr-mode').setAttribute('aria-pressed','false');
      els.forEach((el,i)=>{ el.classList.remove('done'); el._p.textContent=toks[i].cls==='plain'?toks[i].p:' '; });
      if(still){ els.forEach((el,i)=>settle(el,toks[i])); bar.style.width='100%'; return; }
      const n=els.length, step=fig.dataset.manual?Math.max(35,Math.min(110,5200/n)):Math.max(10,Math.min(70,3400/n)), lag=6, t0=performance.now();
      function frame(now){
        if(me!==run) return;
        const k=Math.floor((now-t0)/step); let left=false;
        for(let i=0;i<n;i++){ const el=els[i], t=toks[i]; if(el.classList.contains('done')) continue;
          if(i<=k-lag){ settle(el,t); continue; }
          left=true; if(i<=k && t.cls!=='plain') el._p.textContent=rnd(Math.max(1,Math.min(8,[...t.p].length))); }
        bar.style.width=Math.min(100,100*Math.max(0,k-lag)/n)+'%';
        if(left) requestAnimationFrame(frame); else bar.style.width='100%';
      }
      requestAnimationFrame(frame);
    }
    fig.querySelector('.cr-play').addEventListener('click',play);
    fig.querySelector('.cr-mode').addEventListener('click',e=>{ const v=fig.classList.toggle('cipher'); e.currentTarget.setAttribute('aria-pressed',v); });
    if(fig.dataset.manual){      // a letter someone sent: it stays sealed until the reader breaks the seal
      els.forEach((el,i)=>{ el._p.textContent=toks[i].cls==='plain'?toks[i].p:' '; });
      fig.classList.add('sealed');
      const gate=document.createElement('div'); gate.className='cr-gate';
      gate.innerHTML='<button type="button" class="cr-break"><span class="cr-seal" aria-hidden="true"><i></i><i></i></span><span class="cr-lbl">Break the seal and decipher</span></button>';
      fig.querySelector('.cr-tiles').after(gate);
      gate.querySelector('button').addEventListener('click',()=>{
        fig.classList.add('breaking');
        setTimeout(()=>{ gate.remove(); fig.classList.remove('sealed','breaking'); fig.classList.add('unsealed'); play(); },still?0:900);
      },{once:true});
    }
    return play;
  }

  const io='IntersectionObserver' in window ? new IntersectionObserver(es=>es.forEach(e=>{
    if(e.isIntersecting && e.target._play){ io.unobserve(e.target); e.target._play(); } }),{threshold:.3}) : null;
  figs.forEach(fig=>fetch(fig.dataset.src).then(r=>r.json()).then(d=>{ fig._play=build(fig,d); if(fig.dataset.manual) return; if(io) io.observe(fig); else fig._play(); })
    .catch(()=>{ fig.innerHTML='<p class="cr-info">The interactive decipherment could not be loaded.</p>'; }));
})();
