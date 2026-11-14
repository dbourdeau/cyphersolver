// cipher reveal: <figure class="creveal" data-src="reveal/slug.json"></figure> plus <script src="cipher-reveal.js" defer>.
// The groups scramble and settle into plaintext when the figure scrolls into view; hovering or focusing a group lights
// every occurrence of it, its homophones (other groups with the same value) and its row in the key.
// Data: {title, caption, unit, key_note, tokens:[{g, p, cls, w}]}, cls one of '' unk unc code plain null; w:1 marks the first
// group of a plaintext word. When any token carries w, the tiles of each word are kept together and words are spaced.
// Above the tiles runs the reading line: the same passage as ordinary text, a word at a time as it deciphers, nulls
// left out and the words spaced. It is what a reader reads; the tiles show how each letter was reached. A passage with
// no w marks whose values are whole words (codes, avg. four letters or more) is spaced a group to a word; any other
// passage without marks shows its letters unspaced (python _reveal_words.py --audit lists them).
(()=>{
  const figs=document.querySelectorAll('.creveal[data-src]'); if(!figs.length) return;
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const GLYPHS='ABCDEFGHIKLMNOPQRSTVXYZabcdefghilmnopqrstuxyz0123456789§¶†‡∴⊕';
  const rnd=n=>{ let s=''; for(let i=0;i<n;i++) s+=GLYPHS[Math.random()*GLYPHS.length|0]; return s; };
  const isCipher=t=>t.g && t.cls!=='plain';

  function build(fig, d){
    const toks=d.tokens.map(t=>({g:t.g||'', p:t.p==null?'':String(t.p), cls:t.cls||'', show:t.show, w:!!t.w}));   // show: displayed in place of p (a sealed letter's uu = w)
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
      <p class="cr-read" translate="no" aria-label="The passage as it reads"></p>
      <div class="cr-tiles" translate="no"></div>
      <button type="button" class="cr-more" hidden></button>
      <p class="cr-info" aria-live="polite"><span>${ciph.length} ${unit} &middot; ${read} read &middot; ${key.size} distinct.</span> <span class="cr-hint">${toks.some(t=>t.cls==='plain'&&t.p.trim().length>1)?'Italic words were written in clear. ':''}Hover or tab to a group to trace it through the text and the key.</span></p>
      <details class="cr-key"><summary>The key for this passage <span>${key.size} ${unit}</span></summary><div class="cr-grid" translate="no"></div>${d.key_note?`<p class="cr-note">${esc(d.key_note)}</p>`:''}</details>
      ${d.caption?`<figcaption>${esc(d.caption)}</figcaption>`:''}`;
    const box=fig.querySelector('.cr-tiles'), grid=fig.querySelector('.cr-grid'), info=fig.querySelector('.cr-info'), bar=fig.querySelector('.cr-bar i');
    const vals=ciph.filter(t=>t.cls!=='null'&&t.cls!=='unk'&&t.p!=='?'&&t.p.trim()), avg=vals.reduce((a,t)=>a+[...t.p].length,0)/Math.max(1,vals.length);
    // marked: the data carries word starts, or writes the spaces between words as clear tokens of their own
    const marked=toks.filter(t=>t.w).length*12>=ciph.length||toks.filter(t=>t.cls==='plain'&&t.p!==''&&(!t.p.trim()||t.p.trim()==='\u00b7')).length>=3, perGroup=!marked&&avg>=3.5;   // perGroup: every group is a word of its own
    const words=marked||perGroup; let wd=null, rw=null, solo=true, glue=false;   // solo: the open word takes no more groups
    const line=fig.querySelector('.cr-read');
    if(words) box.classList.add('words'); else line.classList.add('run');
    let fresh=false, started=false, afterLb=false;                                  // fresh: a word has begun and its space is still owed
    const put=(t,el,rt)=>{
      const lb=t.cls==='plain' && t.p.trim()==='/';   // a line break of the manuscript: shown among the tiles, no break in the word
      const divider=t.p!=='' && (!t.p.trim() || (t.cls==='plain' && t.p.trim()==='\u00b7')), phrase=!lb && t.cls==='plain' && !divider && [...t.p.trim()].length>1;
      const alone=divider || phrase;   // clear phrases and word dividers stand alone; a null or a single clear letter stays in its word
      const newTile=words && (!wd || solo || alone || t.w || perGroup), newRead=!rw || newTile || (!words && (alone || solo));
      if(newTile){ wd=document.createElement('span'); wd.className='cr-w'; box.appendChild(wd); } else if(!wd) wd=box;
      if(newRead){ rw=document.createElement('span'); rw.className='cr-rw'; line.appendChild(rw); fresh=true; if(words){ wd._r=rw; rw._w=wd; } }
      // the space is set when the word's first letter arrives, so a divider or a null adds none of its own;
      // none before a closing stop or after an apostrophe: d'hostel, Navarre, aurez
      const v=said(t);
      if(v){ if(fresh && started && !glue && !(t.cls==='plain' && /^[,.;:!?)\]’']/.test(v))) line.insertBefore(document.createTextNode(' '),rw);
        glue=fresh && /^[’'(\[]$/.test(v.trim()); fresh=false; started=true; }
      wd.appendChild(el); rw.appendChild(rt); solo=alone; afterLb=lb; };
    // what a group contributes to the reading line: nothing for a null or a divider, ? for an unread group
    const said=t=>{ if(t.cls==='null') return ''; if(t.cls==='unk'||t.p==='?') return '?'; const raw=String(t.cls==='plain'?t.p:(t.show??t.p)), v=(words||t.cls==='plain')?raw.trim():raw; return (t.cls==='plain'&&v==='/')?'':v.replace(/\u00b7/g,''); };
    const els=toks.map(t=>{
      const el=document.createElement('span'); el.className='tile cr-t '+t.cls;
      el.innerHTML=`<span class="p"></span><span class="g">${esc(t.g||' ')}</span>`;
      if(isCipher(t)){ el.tabIndex=0; el.dataset.g=t.g; el.setAttribute('aria-label',`${t.g} = ${t.cls==='unk'?'unread':t.p}`); }
      const rt=document.createElement('span'); rt.className='cr-rt '+t.cls; rt.textContent=said(t); el._r=rt;
      if(t.cls==='plain') rt.classList.add('done');
      el._p=el.firstChild; put(t,el,rt); return el;
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
    // a word of the reading line and its tiles light each other
    let curW=null;
    const word=w=>{ if(w===curW) return; if(curW){ curW.classList.remove('on'); curW._r.classList.remove('on'); } curW=w; if(w){ w.classList.add('on'); w._r.classList.add('on'); } };
    const on=e=>{ const r=e.target.closest('.cr-rw'), w=r?r._w:e.target.closest('.cr-w'); word(w&&w._r&&fig.contains(w)?w:null);
      const t=e.target.closest('[data-g]'); if(t && fig.contains(t)) trace(t.dataset.g); else if(r) trace(null); };
    fig.addEventListener('pointerover',on); fig.addEventListener('focusin',on);
    fig.addEventListener('pointerleave',()=>{ trace(null); word(null); });
    fig.addEventListener('focusout',e=>{ if(!fig.contains(e.relatedTarget)) trace(null); });
    grid.addEventListener('click',e=>{ const r=e.target.closest('[data-g]'); if(!r) return; cur=null; trace(r.dataset.g);
      els.find(el=>el.dataset.g===r.dataset.g).scrollIntoView({block:'nearest',behavior:still?'auto':'smooth'}); });

    // a long passage shows its first rows of tiles and a button: the reading line above already gives all of it,
    // and 200 tiles are 2,500 px on a phone. Tracing a group from the key opens the rest.
    const more=fig.querySelector('.cr-more');
    const fold=on=>{ box.classList.toggle('clip',on); more.textContent=on?`Show all ${ciph.length} ${d.unit||'groups'}, sign by sign`:'Show fewer'; more.setAttribute('aria-expanded',on?'false':'true'); };
    if(!fig.dataset.manual) requestAnimationFrame(()=>{ const lim=parseFloat(getComputedStyle(box).getPropertyValue('--crh'))*parseFloat(getComputedStyle(document.documentElement).fontSize);
      if(box.scrollHeight>lim*1.5){ more.hidden=false; fold(true); } });
    more.addEventListener('click',()=>{ const on=!box.classList.contains('clip'); fold(on); if(on) fig.scrollIntoView({block:'nearest'}); });
    grid.addEventListener('click',()=>{ if(box.classList.contains('clip')) fold(false); },true);
    addEventListener('beforeprint',()=>{ if(box.classList.contains('clip')) fold(false); });
    let run=0;
    const settle=(el,t)=>{ el._p.textContent=(t.show??t.p)||' '; el.classList.add('done'); el._r.classList.add('done'); };
    function play(){
      const me=++run; fig.classList.remove('cipher'); fig.querySelector('.cr-mode').setAttribute('aria-pressed','false');
      els.forEach((el,i)=>{ el.classList.remove('done'); if(toks[i].cls!=='plain') el._r.classList.remove('done'); el._p.textContent=toks[i].cls==='plain'?toks[i].p:' '; });
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
