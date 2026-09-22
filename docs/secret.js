// Write a secret letter: encipher a message with one of the site's rebuilt keys (secret-keys.json), draw it as a letter
// on aged paper with a wax seal (canvas, downloadable), or share a link that carries only the ciphertext.
(async()=>{
  const $=id=>document.getElementById(id);
  const K=(await (await fetch('secret-keys.json')).json()).keys, byId=Object.fromEntries(K.map(k=>[k.id,k]));
  const SITE='dbourdeau.github.io/cyphersolver';
  const fold=s=>s.normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();
  const pick=a=>a[Math.floor(Math.random()*a.length)];

  // ---------------------------------------------------------------- enciphering
  // tokens: {g, p} cipher group and its value; {g:'', p, cls:'plain'} left in clear; {g:'|', p:' ', cls:'null'} word gap (pigpen)
  function encipher(key, text){
    const out=[], t=fold(text).replace(/[’`]/g,"'");
    if(key.kind==='code') return encCode(key,t);
    const phrases=Object.keys(key.enc).filter(p=>p.length>1).sort((a,b)=>b.length-a.length);
    let i=0;
    while(i<t.length){
      const c=t[i];
      if(/\s/.test(c)){ if(key.kind==='pigpen' && out.length && out[out.length-1].g!=='|') out.push({g:'|',p:' ',cls:'null'}); i++; continue; }
      // whole-word codes (de, la, le roi, Monsieur...) only at word boundaries
      const ph=phrases.find(p=>t.startsWith(p,i) && (i===0||/[^a-z]/.test(t[i-1])) && !/[a-z]/.test(t[i+p.length]||''));
      if(ph){ out.push({g:pick(key.enc[ph]),p:ph,cls:ph.length>2?'code':''}); i+=ph.length; continue; }
      const l=key.fold[c]&&!key.enc[c]?key.fold[c]:c;
      if(key.enc[l]) out.push({g:pick(key.enc[l]),p:l});
      else if(/[a-z0-9]/.test(c)) out.push({g:'',p:c,cls:'plain'});
      i++;
    }
    while(out.length && out[out.length-1].g==='|') out.pop();
    return out;
  }
  // a numbered code: whole words first, then the longest syllables that spell the word, else the word in clear
  let codeIdx=null;
  function encCode(key,t){
    if(!codeIdx){ codeIdx=new Map(); for(const [p,gs] of Object.entries(key.enc)) codeIdx.set(p.toLowerCase(),gs); }
    const parts=Object.keys(key.enc).map(p=>p.toLowerCase()).filter(p=>/^[a-z]+$/.test(p)).sort((a,b)=>b.length-a.length);
    const out=[];
    for(const w of t.match(/[a-z]+|[0-9]+/g)||[]){
      if(codeIdx.has(w)){ out.push({g:pick(codeIdx.get(w)),p:w}); continue; }
      // cheapest spelling by dynamic programming over the syllables
      const best=new Array(w.length+1).fill(null); best[0]=[];
      for(let i=0;i<w.length;i++){ if(!best[i]) continue;
        for(const p of parts){ if(w.startsWith(p,i)){ const j=i+p.length, cand=best[i].concat([p]);
          if(!best[j] || cand.length<best[j].length) best[j]=cand; } } }
      if(best[w.length]) best[w.length].forEach((p,k)=>out.push({g:pick(codeIdx.get(p)),p,cls:k?'unc':''}));
      else out.push({g:'',p:w,cls:'plain'});
    }
    return out;
  }

  // ---------------------------------------------------------------- the letter
  const cv=$('letter'), ctx=cv.getContext('2d');
  let fontsReady=document.fonts?Promise.all([document.fonts.load('40px "IM Fell English"'),document.fonts.load('italic 26px "IM Fell English"')]).catch(()=>{}):Promise.resolve();
  const PAPER=(()=>{ // grain drawn once, reused
    const c=document.createElement('canvas'); c.width=550; c.height=700; const x=c.getContext('2d');
    const im=x.createImageData(c.width,c.height);
    for(let i=0;i<im.data.length;i+=4){ const n=Math.random()*38; im.data[i]=120+n; im.data[i+1]=95+n; im.data[i+2]=55+n; im.data[i+3]=Math.random()<.5?10:0; }
    x.putImageData(im,0,0); return c; })();
  function seeded(seed){ let s=seed>>>0||1; return ()=>{ s^=s<<13; s^=s>>>17; s^=s<<5; return ((s>>>0)%10000)/10000; }; }
  // the sheet's outline: deckled, frayed edges with a few nicks, walked clockwise
  const ROLL=44;   // height of the rolled ends of the scroll, top and bottom
  function edge(W,H,rand){
    const pts=[], I=16, T=ROLL*.62, step=3;
    let j=0;
    const side=(len,fn)=>{ const a=rand()*6.3, b=rand()*6.3, f1=.006+rand()*.004, f2=.021+rand()*.012; let nick=0, dn=0;
      for(let t=0;t<=len;t+=step){
        j=j*.55+(rand()-.5)*2.6;                                   // correlated jitter: fibres, not a saw
        if(nick<=0 && rand()<.006){ nick=6+(rand()*10|0); dn=4+rand()*8; }
        let d=Math.sin(t*f1+a)*3.2+Math.sin(t*f2+b)*1.6+j;
        if(nick>0){ d+=dn*Math.sin(Math.PI*nick/12); nick--; }
        fn(t,d); } };
    side(W,(t,d)=>pts.push([t,T+d*.5]));
    side(H,(t,d)=>pts.push([W-I-d,t]));
    side(W,(t,d)=>pts.push([W-t,H-T-d*.5]));
    side(H,(t,d)=>pts.push([I+d,H-t]));
    const path=new Path2D(); path.moveTo(...pts[0]); for(const q of pts) path.lineTo(...q); path.closePath();
    return path;
  }
  function stain(x,y,r,rand){      // an irregular tide mark: a few overlapping blobs, darker at the rim
    for(let i=0;i<4;i++){ const ox=x+(rand()-.5)*r*.5, oy=y+(rand()-.5)*r*.5, rr=r*(.55+rand()*.45);
      const s=ctx.createRadialGradient(ox,oy,rr*.1,ox,oy,rr);
      s.addColorStop(0,'rgba(140,95,35,.025)'); s.addColorStop(.8,'rgba(135,90,32,.05)'); s.addColorStop(.95,'rgba(115,72,25,.07)'); s.addColorStop(1,'rgba(140,95,35,0)');
      ctx.fillStyle=s; ctx.beginPath(); ctx.ellipse(ox,oy,rr,rr*(.7+rand()*.3),rand()*3,0,7); ctx.fill(); }
  }
  function roll(W,y,rand,top){     // the rolled end: a cylinder of the same paper, its spiral showing at each end
    const x0=6, x1=W-6, h=ROLL, r=h/2;
    const g=ctx.createLinearGradient(0,y,0,y+h);
    g.addColorStop(0,'#8a6534'); g.addColorStop(.2,'#d9c08e'); g.addColorStop(.42,'#f3e5c3'); g.addColorStop(.7,'#c9a86f'); g.addColorStop(1,'#6e4c22');
    ctx.save(); ctx.shadowColor='rgba(0,0,0,.35)'; ctx.shadowBlur=10; ctx.shadowOffsetY=top?5:-2;
    ctx.fillStyle=g; ctx.beginPath(); ctx.roundRect(x0,y,x1-x0,h,r*.5); ctx.fill(); ctx.restore();
    ctx.save(); ctx.beginPath(); ctx.roundRect(x0,y,x1-x0,h,r*.5); ctx.clip();
    ctx.globalAlpha=.55; for(let yy=y;yy<y+h;yy+=PAPER.height) for(let xx=0;xx<W;xx+=PAPER.width) ctx.drawImage(PAPER,xx,yy); ctx.globalAlpha=1;
    const e=ctx.createLinearGradient(x0,0,x1,0); e.addColorStop(0,'rgba(80,50,15,.45)'); e.addColorStop(.06,'rgba(80,50,15,0)'); e.addColorStop(.94,'rgba(80,50,15,0)'); e.addColorStop(1,'rgba(80,50,15,.45)');
    ctx.fillStyle=e; ctx.fillRect(x0,y,x1-x0,h);
    ctx.strokeStyle='rgba(90,58,20,.18)'; ctx.lineWidth=1;
    for(let i=0;i<3;i++){ const yy=y+h*(.3+i*.2)+(rand()-.5)*3; ctx.beginPath(); ctx.moveTo(x0+30,yy); ctx.bezierCurveTo(W*.35,yy+(rand()-.5)*4,W*.65,yy+(rand()-.5)*4,x1-30,yy); ctx.stroke(); }
    ctx.restore();
    for(const cx of [x0+r*.5, x1-r*.5]){  // the spiral at each end
      ctx.save(); ctx.translate(cx,y+r); ctx.scale(.42,1);
      ctx.fillStyle='#b8955c'; ctx.beginPath(); ctx.arc(0,0,r*.98,0,7); ctx.fill();
      ctx.strokeStyle='rgba(70,44,14,.7)'; ctx.lineWidth=1.6; ctx.beginPath();
      for(let t=0;t<16;t+=.1){ const rr=r*.94*(1-t/17); ctx.lineTo(Math.cos(t)*rr,Math.sin(t)*rr); } ctx.stroke();
      ctx.restore(); }
    ctx.strokeStyle='rgba(55,32,8,.5)'; ctx.lineWidth=1.2; ctx.beginPath(); ctx.roundRect(x0,y,x1-x0,h,r*.5); ctx.stroke();
  }
  function paper(W,H,rand){
    ctx.clearRect(0,0,W,H);
    const sheet=edge(W,H,rand);
    ctx.save(); ctx.clip(sheet);
    ctx.fillStyle='#e9d6ac'; ctx.fillRect(0,0,W,H);
    const g=ctx.createRadialGradient(W/2,H*.45,Math.min(W,H)*.22,W/2,H/2,Math.max(W,H)*.72);
    g.addColorStop(0,'rgba(255,247,222,.38)'); g.addColorStop(.65,'rgba(150,108,48,.14)'); g.addColorStop(1,'rgba(92,58,18,.5)');
    ctx.fillStyle=g; ctx.fillRect(0,0,W,H);
    for(let i=0;i<6;i++) stain(rand()*W,rand()*H,50+rand()*150,rand);
    for(let i=0;i<60;i++){ const x=rand()*W, y=rand()*H, r=.8+rand()*(rand()<.12?5:2.2);   // foxing
      ctx.fillStyle=`rgba(${118+rand()*30|0},${68+rand()*20|0},${24+rand()*15|0},${.07+rand()*.2})`;
      ctx.beginPath(); ctx.ellipse(x,y,r,r*(.6+rand()*.5),rand()*3,0,7); ctx.fill(); }
    ctx.save(); ctx.globalAlpha=.9; for(let y=0;y<H;y+=PAPER.height) for(let x=0;x<W;x+=PAPER.width) ctx.drawImage(PAPER,x,y); ctx.restore();
    // laid-paper chain lines and a few fibres
    ctx.strokeStyle='rgba(120,85,40,.04)'; ctx.lineWidth=1.2;
    for(let x=60+rand()*40;x<W;x+=95){ ctx.beginPath(); ctx.moveTo(x,0); ctx.lineTo(x+(rand()-.5)*6,H); ctx.stroke(); }
    ctx.strokeStyle='rgba(95,65,30,.12)'; ctx.lineWidth=.8;
    for(let i=0;i<40;i++){ const x=rand()*W, y=rand()*H, a=rand()*6.3, l=6+rand()*18;
      ctx.beginPath(); ctx.moveTo(x,y); ctx.quadraticCurveTo(x+Math.cos(a+1)*l*.5,y+Math.sin(a+1)*l*.5,x+Math.cos(a)*l,y+Math.sin(a)*l); ctx.stroke(); }
    // the folds: one across, one down
    const f=ctx.createLinearGradient(0,H/2-14,0,H/2+14); f.addColorStop(0,'rgba(90,60,20,0)'); f.addColorStop(.5,'rgba(90,60,20,.15)'); f.addColorStop(.52,'rgba(255,250,235,.26)'); f.addColorStop(1,'rgba(90,60,20,0)');
    ctx.fillStyle=f; ctx.fillRect(0,H/2-14,W,28);
    const v=ctx.createLinearGradient(W/2-10,0,W/2+10,0); v.addColorStop(0,'rgba(90,60,20,0)'); v.addColorStop(.5,'rgba(90,60,20,.07)'); v.addColorStop(.53,'rgba(255,250,235,.14)'); v.addColorStop(1,'rgba(90,60,20,0)');
    ctx.fillStyle=v; ctx.fillRect(W/2-10,0,20,H);
    // shadow thrown by the rolls onto the sheet
    for(const [y0,dir] of [[ROLL*.6,1],[H-ROLL*.6,-1]]){ const c=ctx.createLinearGradient(0,y0,0,y0+dir*40);
      c.addColorStop(0,'rgba(60,36,10,.35)'); c.addColorStop(1,'rgba(60,36,10,0)'); ctx.fillStyle=c; ctx.fillRect(0,Math.min(y0,y0+dir*40),W,40); }
    // the edges browned and scorched: wide soft strokes along the outline, clipped to the inside
    for(const [w,a] of [[90,.045],[56,.065],[32,.09],[16,.15],[6,.28]]){ ctx.lineWidth=w; ctx.strokeStyle=`rgba(88,52,16,${a})`; ctx.stroke(sheet); }
    ctx.lineWidth=1.6; ctx.strokeStyle='rgba(60,32,8,.5)'; ctx.stroke(sheet);
    ctx.restore();
    roll(W,0,rand,true); roll(W,H-ROLL,rand,false);
  }
  function pigpen(x,y,s,g){ // box shape by grid position, dot below or inside
    const i=+g[0], dot=g[1], L=x, R=x+s, T=y-s, B=y;
    const sides={0:'rb',1:'lrb',2:'lb',3:'trb',4:'tlrb',5:'tlb',6:'tr',7:'tlr',8:'tl'}[i];
    ctx.beginPath();
    if(sides.includes('t')){ ctx.moveTo(L,T); ctx.lineTo(R,T); }
    if(sides.includes('b')){ ctx.moveTo(L,B); ctx.lineTo(R,B); }
    if(sides.includes('l')){ ctx.moveTo(L,T); ctx.lineTo(L,B); }
    if(sides.includes('r')){ ctx.moveTo(R,T); ctx.lineTo(R,B); }
    ctx.stroke();
    if(dot){ ctx.beginPath(); ctx.arc(x+s/2, dot==='.'?B+s*.32:y-s/2, s*.09,0,7); ctx.fill(); }
  }
  function seal(cx,cy,r,letter,rand){
    ctx.save(); ctx.translate(cx,cy); ctx.rotate(-.2);
    ctx.fillStyle='rgba(60,10,5,.35)'; ctx.beginPath(); ctx.ellipse(6,9,r*1.05,r*1.02,0,0,7); ctx.fill();
    // an irregular blob of wax
    ctx.beginPath(); for(let a=0;a<=Math.PI*2+.01;a+=Math.PI/18){ const rr=r*(1+(rand()-.5)*.1); ctx.lineTo(Math.cos(a)*rr,Math.sin(a)*rr); } ctx.closePath();
    const g=ctx.createRadialGradient(-r*.35,-r*.4,r*.1,0,0,r*1.05); g.addColorStop(0,'#d8574a'); g.addColorStop(.45,'#9b2a22'); g.addColorStop(1,'#5a120d');
    ctx.fillStyle=g; ctx.fill();
    ctx.lineWidth=r*.07; ctx.strokeStyle='rgba(60,8,5,.55)'; ctx.beginPath(); ctx.arc(0,0,r*.72,0,7); ctx.stroke();
    ctx.lineWidth=r*.025; ctx.strokeStyle='rgba(255,190,170,.35)'; ctx.beginPath(); ctx.arc(-1,-1.5,r*.72,0,7); ctx.stroke();
    ctx.setLineDash([r*.05,r*.07]); ctx.lineWidth=r*.03; ctx.strokeStyle='rgba(60,8,5,.5)'; ctx.beginPath(); ctx.arc(0,0,r*.6,0,7); ctx.stroke(); ctx.setLineDash([]);
    ctx.font=`${Math.round(r*.78)}px "IM Fell English", Georgia, serif`; ctx.textAlign='center'; ctx.textBaseline='middle';
    ctx.fillStyle='rgba(50,6,4,.75)'; ctx.fillText(letter,1.5,4); ctx.fillStyle='rgba(255,200,185,.28)'; ctx.fillText(letter,-.5,2);
    ctx.restore();
  }
  function draw(key,tokens,sig,seed,to){
    const rand=seeded(seed), W=1100, M=110, ink='#2b1c0e';
    const fs=key.kind==='pigpen'?0:(key.kind==='code'?40:44), gap=key.kind==='pigpen'?10:18, lh=key.kind==='pigpen'?74:66;
    ctx.font=`${fs||40}px "IM Fell English", Georgia, serif`;
    // lay the groups out first to know the height
    const lines=[[]]; let x=0;
    for(const t of tokens){
      const txt=t.g||t.p, w=key.kind==='pigpen'?(t.g==='|'?26:34):ctx.measureText(txt).width + (t.cls==='plain'?4:0);
      if(t.g==='|' && x===0) continue;
      if(x+w>W-2*M && lines[lines.length-1].length){ lines.push([]); x=0; if(t.g==='|') continue; }
      lines[lines.length-1].push({t,w,x}); x+=w+gap;
    }
    const H=Math.max(1150, 360+(to?80:0)+lines.length*lh+(sig?120:0)+330);
    cv.height=H; paper(W,H,rand);
    ctx.fillStyle=ink; ctx.strokeStyle=ink; ctx.textBaseline='alphabetic';
    ctx.font='italic 26px "IM Fell English", Georgia, serif'; ctx.globalAlpha=.8;
    ctx.fillText(`In the cipher of ${key.who}, ${key.year}`,M,150);
    ctx.globalAlpha=1; ctx.lineWidth=1; ctx.beginPath(); ctx.moveTo(M,172); ctx.lineTo(M+180,172); ctx.stroke();
    let y=270;
    if(to){ ctx.font='italic 40px "IM Fell English", Georgia, serif'; ctx.fillText(to,M,y-10); y+=80; }
    for(const line of lines){
      for(const {t,w,x} of line){
        const jx=(rand()-.5)*2, jy=(rand()-.5)*3;
        ctx.globalAlpha=.78+rand()*.22;
        if(key.kind==='pigpen'){ if(t.g!=='|'){ ctx.lineWidth=2.8; ctx.lineCap='round'; pigpen(M+x+jx,y+jy,30,t.g); } }
        else{ ctx.font=(t.cls==='plain'?'italic ':'')+`${fs}px "IM Fell English", Georgia, serif`; ctx.fillText(t.g||t.p,M+x+jx,y+jy); }
      }
      y+=lh;
    }
    ctx.globalAlpha=1;
    if(sig){ ctx.font='italic 40px "IM Fell English", Georgia, serif'; ctx.textAlign='right'; ctx.fillText(sig,W-M,y+60); ctx.textAlign='left'; }
    seal(M+90,H-230,78,key.seal||key.who[0],rand);
    ctx.font='21px "IM Fell English", Georgia, serif'; ctx.globalAlpha=.72; ctx.textAlign='right';
    ctx.fillText('Can you read it? The key is at',W-M,H-120);
    ctx.font='22px "JetBrains Mono", Consolas, monospace'; ctx.fillText(SITE+'/'+key.slug+'.html',W-M,H-88);
    ctx.textAlign='left'; ctx.globalAlpha=1;
  }

  // ---------------------------------------------------------------- the page
  let key=K[0], tokens=[], seed=Date.now()%100000;
  const msg=$('msg'), sig=$('sig'), to=$('to');
  $('keys').innerHTML=K.map(k=>`<button type="button" class="sl-key" data-k="${k.id}" aria-pressed="false"><b>${k.name}</b><span>${k.who}, ${k.year}</span><i></i></button>`).join('');
  const btns=[...document.querySelectorAll('.sl-key')];
  function sample(k){ const t=encipher(k,'burn this letter'); return k.kind==='pigpen'?'☐ ⊔ ┗ ┓ · ☐':t.map(x=>x.g||x.p).filter(g=>g!=='|').join(' '); }
  btns.forEach(b=>{ b.querySelector('i').textContent=sample(byId[b.dataset.k]); b.addEventListener('click',()=>{ key=byId[b.dataset.k]; update(true); }); });
  function update(reroll){
    if(reroll) seed=Math.floor(Math.random()*1e6);
    btns.forEach(b=>b.setAttribute('aria-pressed',b.dataset.k===key.id));
    $('keynote').innerHTML=`${key.note} <a href="${key.slug}.html">The write-up &rarr;</a>`;
    const r=Math.random; Math.random=seeded(seed); tokens=encipher(key,msg.value); Math.random=r;
    const n=tokens.filter(t=>t.g&&t.g!=='|').length, clear=tokens.filter(t=>t.cls==='plain').length;
    $('count').textContent=`${msg.value.length} / 400`;
    $('stats').textContent=`${n} ${key.kind==='code'?'code groups':key.kind==='pigpen'?'signs':'figures'}`+(clear?`, ${clear} left in clear (the key has no sign for them)`:'');
    fontsReady.then(()=>draw(key,tokens,sig.value.trim(),seed,to.value.trim()));
  }
  let tmr=0; const later=()=>{ clearTimeout(tmr); tmr=setTimeout(()=>update(false),120); };
  msg.addEventListener('input',later); sig.addEventListener('input',later); to.addEventListener('input',later);
  $('reroll').addEventListener('click',()=>update(true));
  const say=t=>{ $('status').textContent=t; setTimeout(()=>{ if($('status').textContent===t) $('status').textContent=''; },4000); };
  $('dl').addEventListener('click',()=>cv.toBlob(b=>{ const a=document.createElement('a'); a.href=URL.createObjectURL(b);
    a.download=`secret-letter-${key.id}.png`; a.click(); setTimeout(()=>URL.revokeObjectURL(a.href),4000); say('Letter saved.'); },'image/png'));
  // the sealed link: key, groups (clear words prefixed with ~), signature; never the plaintext
  const pack=()=>tokens.map(t=>t.g==='|'?'|':t.g||('~'+t.p)).join('.');
  $('link').addEventListener('click',async()=>{
    const url=`${location.origin}${location.pathname}#k=${key.id}&c=${encodeURIComponent(pack())}`+(sig.value.trim()?`&s=${encodeURIComponent(sig.value.trim())}`:'')+(to.value.trim()?`&t=${encodeURIComponent(to.value.trim())}`:'');
    try{ await navigator.clipboard.writeText(url); say('Sealed link copied. Only the ciphertext travels in it.'); }catch(e){ prompt('Copy this link',url); }
  });

  // ---------------------------------------------------------------- receiving a sealed link
  const h=new URLSearchParams(location.hash.slice(1));
  if(h.get('k') && h.get('c') && byId[h.get('k')]){
    const k=byId[h.get('k')], c=h.get('c').split('.'), s=h.get('s')||'', tt=h.get('t')||'';
    const tk=c.map(g=>g==='|'?{g:'|',p:' ',cls:'null'}:g[0]==='~'?{g:'',p:g.slice(1),cls:'plain'}:{g,p:k.dec[g]??'?',cls:k.dec[g]?'':'unk'})
      .filter(t=>!(k.kind==='pigpen' && t.g==='|'));
    key=k; tokens=c.map(g=>g==='|'?{g:'|',p:' ',cls:'null'}:g[0]==='~'?{g:'',p:g.slice(1),cls:'plain'}:{g,p:k.dec[g]||'?'});
    $('recv').hidden=false;
    $('recv-h').textContent=(s?`${s} has sent `:'Someone has sent ')+(tt?`${tt} a letter in cipher`:'you a letter in cipher');
    $('recv-p').innerHTML=`It is written in the cipher of ${k.who}, ${k.year}. Scroll down and it will decipher itself with the key rebuilt on <a href="${k.slug}.html">that write-up</a>; hover a group to see every place it recurs. Then write one back.`;
    const data={title:`A letter in the cipher of ${k.who.split(',')[0]}`,unit:k.kind==='code'?'code groups':k.kind==='pigpen'?'signs':'figures',
      caption:`Sent with a sealed link from ${SITE}/secret.html.`,key_note:k.note,tokens:tk};
    const fig=$('recv-reveal'); fig.dataset.src=URL.createObjectURL(new Blob([JSON.stringify(data)],{type:'application/json'}));
    const s2=document.createElement('script'); s2.src='cipher-reveal.js?again'; document.body.appendChild(s2);
    msg.value=''; sig.value=''; to.value='';
    btns.forEach(b=>b.setAttribute('aria-pressed',b.dataset.k===key.id));
    $('keynote').innerHTML=`${key.note} <a href="${key.slug}.html">The write-up &rarr;</a>`;
    fontsReady.then(()=>draw(key,tokens,s,seed,tt));
    msg.addEventListener('focus',()=>{ if(!msg.value) update(false); },{once:true});
  } else update(true);
})();
