// "How it was solved": <figure class="sreplay" data-src="steps/slug.json">, inserted by _build_site.py from the target's
// profile.json.  Every solution step is a bead on a track: moves that worked stay on the line, failed and ruled-out moves
// drop below it as dead ends.  A playhead walks the steps when the reader presses play; beads can be stepped or clicked.
(()=>{
  const figs=document.querySelectorAll('.sreplay[data-src]'); if(!figs.length) return;
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const KIND={'access':['⤓','getting the documents'],'transcription':['✎','transcription'],'statistics':['Σ','statistics'],
    'hypothesis':['?','hypothesis'],'crib':['“','crib'],'solver':['⚙','solver run'],'control':['⚖','control'],
    'sibling key':['⇄','sibling key'],'key from source':['⚿','key from a source'],'prediction':['→','prediction'],
    'reading':['¶','reading'],'verification':['✓','verification'],'literature search':['§','literature search']};
  const RES={'worked':'worked','partial':'partly worked','failed':'failed','ruled out':'ruled out','unknown':'unknown'};
  const cls=r=>({'worked':'ok','partial':'part','failed':'fail','ruled out':'out'}[r]||'unk');
  const fmt=d=>{ if(!d) return ''; const m=/^(\d{4})-(\d{2})-(\d{2})$/.exec(d); if(!m) return d;
    return `${+m[3]} ${['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'][m[2]-1]} ${m[1]}`; };

  function build(fig,d){
    const S=d.steps, n=S.length, dead=S.filter(s=>s.result==='failed'||s.result==='ruled out').length;
    const days=(d.first && d.last && /^\d{4}-/.test(d.first) && /^\d{4}-/.test(d.last)) ? Math.round((new Date(d.last)-new Date(d.first))/864e5)+1 : null;
    const o=d.outcome||{}, pr=d.prior||{};
    const chips=[o.class&&`<span class="sr-c out-${cls(o.class==='read'?'worked':o.class==='read in part'?'partial':'x')}">${esc(o.class)}</span>`,
      d.attack&&d.attack!=='none'&&`<span class="sr-c">attack: ${esc(d.attack)}</span>`,
      pr.exists&&pr.exists!=='no'&&`<span class="sr-c">earlier reading: ${esc(pr.exists)}${pr.found?' &middot; found '+esc(pr.found):''}</span>`].filter(Boolean).join('');
    fig.innerHTML=`<div class="sr-head"><div><span class="sr-kick">How it was solved</span>
      <h3>${n} moves${dead?`, <em>${dead} dead end${dead>1?'s':''}</em>`:''}${days?` <small>over ${days} day${days>1?'s':''}</small>`:''}</h3></div>
      <div class="sr-ctl"><button type="button" class="sr-prev" aria-label="Previous step">&#9664;</button>
      <button type="button" class="sr-play" aria-label="Play">&#9654;</button>
      <button type="button" class="sr-next" aria-label="Next step">&#9654;&#9654;</button></div></div>
      ${chips?`<div class="sr-chips">${chips}</div>`:''}
      <div class="sr-track" role="list"></div>
      <div class="sr-card" aria-live="polite"></div>
      <div class="sr-legend"><span><i class="ok"></i>worked</span><span><i class="part"></i>partly</span><span><i class="fail"></i>failed</span><span><i class="out"></i>ruled out</span><span class="sr-lk">dead ends hang below the line</span></div>
      <details class="sr-all"><summary>Every step as a list</summary><ol>${S.map(s=>`<li class="${cls(s.result)}"><b>${esc((KIND[s.kind]||['',s.kind])[1])}</b> &middot; <span>${esc(RES[s.result]||s.result)}</span>${s.date?` &middot; <time>${esc(fmt(s.date))}</time>`:''}<br>${esc(s.what)}</li>`).join('')}</ol></details>
      <figcaption>From the target&rsquo;s <a href="https://github.com/dbourdeau/cyphersolver/blob/main/${esc(d.slug==='bordeaux1653'?'bordeaux':d.slug)}/profile.json">profile.json</a>, the step-by-step record kept for the study of how a language model does against historical ciphers. Failures are recorded as they happened.</figcaption>`;
    const track=fig.querySelector('.sr-track'), card=fig.querySelector('.sr-card'), play=fig.querySelector('.sr-play');
    let lastDate=null;
    const beads=S.map((s,i)=>{
      const b=document.createElement('button'); b.type='button'; b.setAttribute('role','listitem');
      const k=KIND[s.kind]||['•',s.kind||'step'];
      b.className=`sr-b ${cls(s.result)}${(s.result==='failed'||s.result==='ruled out')?' dead':''}`;
      b.innerHTML=`<span>${k[0]}</span>`; b.title=`${k[1]} — ${RES[s.result]||s.result}`;
      b.setAttribute('aria-label',`Step ${i+1}: ${k[1]}, ${RES[s.result]||s.result}`);
      if(s.date && s.date!==lastDate){ const day=document.createElement('small'); day.className='sr-day'; day.textContent=fmt(s.date).replace(/ \d{4}$/,''); b.appendChild(day); lastDate=s.date; }
      b.addEventListener('click',()=>{ stop(); show(i); });
      track.appendChild(b); return b;
    });
    let cur=-1, timer=0;
    function show(i){
      cur=Math.max(0,Math.min(n-1,i));
      beads.forEach((b,j)=>{ b.classList.toggle('seen',j<=cur); b.classList.toggle('cur',j===cur); });
      const s=S[cur], k=KIND[s.kind]||['•',s.kind];
      card.className='sr-card '+cls(s.result);
      card.innerHTML=`<div class="sr-meta"><span class="sr-n">${cur+1}/${n}</span><span class="sr-k">${esc(k[0])} ${esc(k[1])}</span><span class="sr-r">${esc(RES[s.result]||s.result)}</span>${s.date?`<time>${esc(fmt(s.date))}</time>`:''}</div><p>${esc(s.what)}</p>`;
    }
    function stop(){ clearInterval(timer); timer=0; play.innerHTML='&#9654;'; play.setAttribute('aria-label','Play'); }
    function start(){ if(cur>=n-1) cur=-1; show(cur+1); play.innerHTML='&#10074;&#10074;'; play.setAttribute('aria-label','Pause');
      timer=setInterval(()=>{ if(cur>=n-1){ stop(); return; } show(cur+1); }, Math.max(900,Math.min(2200,24000/n))); }
    play.addEventListener('click',()=>timer?stop():start());
    fig.querySelector('.sr-prev').addEventListener('click',()=>{ stop(); show(cur-1); });
    fig.querySelector('.sr-next').addEventListener('click',()=>{ stop(); show(cur+1); });
    fig.addEventListener('keydown',e=>{ if(e.target.closest('.sr-track') && (e.key==='ArrowRight'||e.key==='ArrowLeft')){ e.preventDefault(); stop();
      show(cur+(e.key==='ArrowRight'?1:-1)); beads[cur].focus(); } });
    if(still){ show(n-1); return null; }
    beads.forEach(b=>b.classList.remove('seen')); card.innerHTML=`<p class="sr-idle">Press play, or click any step.</p>`;
    return start;
  }
  // the replay waits for the reader: play, or click a step
  figs.forEach(fig=>fetch(fig.dataset.src).then(r=>r.json()).then(d=>{ build(fig,d); })
    .catch(()=>{ fig.remove(); }));
})();
