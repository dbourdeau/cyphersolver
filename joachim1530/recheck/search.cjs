// Seeded incremental homophonic/monoalphabetic search. Run from repository root.
const fs=require('fs');
const dir='joachim1530/recheck/';
const data=JSON.parse(fs.readFileSync(dir+'input.json','utf8'));
const raw=fs.readFileSync(dir+'it4.bin');
const lp=new Float32Array(raw.buffer,raw.byteOffset,raw.length/4);
const mode=process.argv[2]||'dotted', R=+(process.argv[3]||100), steps=+(process.argv[4]||100000);
let seed=+(process.argv[5]||2351);
function rand(){seed^=seed<<13;seed^=seed>>>17;seed^=seed<<5;return (seed>>>0)/4294967296;}
let items=data.items.map(z=>z.map(t=>mode.includes('merge')?t.replace(/d$/,'').replace('S2','S'):t));
if(mode.includes('PL'))items=items.map(z=>z.map(t=>t==='L'?'P':t));
let syms=[...new Set(items.flat())].sort();
const enc=items.map(z=>z.map(t=>syms.indexOf(t))), A=data.alpha.length,N=syms.length;
const W=enc.flatMap(z=>z.slice(3).map((_,i)=>z.slice(i,i+4)));
const touches=Array.from({length:N},(_,s)=>W.flatMap((w,i)=>w.includes(s)?[i]:[]));
const pair=Array.from({length:N},(_,a)=>Array.from({length:N},(_,b)=>[...new Set([...touches[a],...touches[b]])]));
const letters=[...'abcdefghilmnopqrstuz'].map(c=>data.alpha.indexOf(c));
const mono=mode.includes('mono');
const freq={a:.117,b:.009,c:.045,d:.037,e:.118,f:.011,g:.016,h:.015,i:.113,l:.065,m:.025,n:.069,o:.098,p:.030,q:.005,r:.064,s:.050,t:.056,u:.054,z:.012};
const count=syms.map(s=>items.flat().filter(t=>t===s).length),total=count.reduce((a,b)=>a+b,0);
function penalty(key){let obs=new Float64Array(A);for(let i=0;i<N;i++)obs[key[i]]+=count[i];let kl=0;for(let i=0;i<A;i++)if(obs[i])kl+=obs[i]*Math.log(obs[i]/total/(freq[data.alpha[i]]||.001));return 3*kl;}
if(mono&&N>letters.length)throw new Error('Too many symbols');
function val(w,key){return lp[((key[w[0]]*A+key[w[1]])*A+key[w[2]])*A+key[w[3]]];}
function output(score,key){return {score,key:Object.fromEntries(syms.map((s,i)=>[s,data.alpha[key[i]]])),text:enc.map(z=>z.map(s=>data.alpha[key[s]]).join(''))};}
let best=-Infinity,bkey;
for(let r=0;r<R;r++){
 let key=mono?letters.slice().sort(()=>rand()-.5):syms.map(()=>letters[Math.floor(rand()*letters.length)]);
 let pen=penalty(key),score=W.reduce((s,w)=>s+val(w,key),0)-pen;
 for(let j=0;j<steps;j++){
  let a=Math.floor(rand()*N),b=Math.floor(rand()*key.length),swap=mono||rand()<.45;
  if(a===b&&swap)continue;
  const olda=key[a],oldb=key[b];
  const ids=swap&&b<N?pair[a][b]:touches[a];
  let delta=0;for(const i of ids)delta-=val(W[i],key);
  if(swap){key[a]=oldb;key[b]=olda;}else key[a]=letters[Math.floor(rand()*letters.length)];
  for(const i of ids)delta+=val(W[i],key);
  const newpen=penalty(key);delta+=pen-newpen;
  const temperature=Math.max(.12,12*Math.pow(1-j/steps,3));
  if(delta>=0||rand()<Math.exp(delta/temperature)){
   score+=delta;
   pen=newpen;
   if(score>best){best=score;bkey=key.slice();}
  }else {key[a]=olda;key[b]=oldb;}
 }
 if(r%10===0)console.log(r,best.toFixed(1),output(best,bkey).text[0]);
}
let result={mode,restarts:R,steps,...output(best,bkey)};
fs.writeFileSync(dir+'result_'+mode+'.json',JSON.stringify(result,null,2));
console.log(JSON.stringify(result,null,2));
