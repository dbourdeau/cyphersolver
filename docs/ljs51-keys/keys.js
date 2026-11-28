"use strict";
const byId = id => document.getElementById(id);
const repo = "https://github.com/dbourdeau/cyphersolver/blob/main/";
const records = new Map();
let index = [], active, selectedView, sequence = 0;
function el(tag, text, cls) {
  const x = document.createElement(tag);
  if (text !== undefined) x.textContent = text;
  if (cls) x.className = cls;
  return x;
}
function link(text, href) { const x = el("a", text); x.href = href; return x; }
function hash(id, sign) { return "#" + encodeURIComponent(id) + (sign ? "/" + encodeURIComponent(sign) : ""); }
function folioTitle(id) {
  return id.split("+").map(part => {
    const [leaf, line] = part.split(".");
    return "f. " + leaf + (line === "trees" ? " · trees" : ", line " + line);
  }).join(" + ");
}
function rowName(row) {
  const m = /^(\d+[rv])[._l]*(\d+)$/.exec(row);
  return m ? "f. " + m[1] + ", row " + Number(m[2]) : "row " + row;
}
function direction() { return (active.direction || "").toLowerCase().includes("left-to-right") ? "ltr" : "rtl"; }
function imageNo(leaf) { return 6 + (parseInt(leaf,10)-1)*2 + Number(leaf.endsWith("v")); }
function original(leaf) {
  return "https://openn.library.upenn.edu/Data/0001/ljs51/data/master/0084_" + String(imageNo(leaf)).padStart(4,"0") + ".tif";
}
function values(c) {
  const box=el("span",undefined,"values");
  if (c.text) {
    const ar=el("bdi",c.text,"ar"); ar.lang="ar"; ar.dir="rtl"; box.append(ar);
  } else {
    const pairs=Object.entries(c.values || {}).sort((a,b)=>b[1]-a[1]);
    if (!pairs.length) box.append(el("span","Unassigned","small"));
    for (const [letter,n] of pairs) {
      const v=el("span",undefined,"value"), ar=el("bdi",letter,"ar");
      ar.lang="ar"; ar.dir="rtl"; v.append(ar,el("small"," × "+n)); box.append(v);
    }
  }
  return box;
}
function picture(c) {
  const frame=el("span",undefined,"specimen");
  if (Number.isInteger(c.tile)) {
    const crop=el("span",undefined,"tile");
    crop.style.backgroundImage="url('sheets/"+encodeURIComponent(active.id)+".webp')";
    crop.style.backgroundPosition=(-128*(c.tile%6))+"px "+(-128*Math.floor(c.tile/6))+"px";
    crop.setAttribute("role","img"); crop.setAttribute("aria-label",c.description || "Manuscript specimen for "+c.id);
    frame.append(crop);
  } else if (c.context) {
    const img=el("img",undefined,"strip"); img.src="context/"+c.context; img.loading="lazy"; img.alt="Manuscript reference crop for "+c.id; frame.append(img);
  } else frame.append(el("span","No intact example","small"));
  return frame;
}
function showChoices() {
  const q=byId("find").value.toLowerCase().trim().replace(/^f\.\s*/,""), list=byId("folios");
  const hits=index.filter(x=>!q || x.id.toLowerCase().includes(q) || x.folios.some(f=>f.includes(q)));
  list.replaceChildren(...hits.map(x=>{const o=el("option",x.id.replace("+"," + "));o.value=x.id;return o;}));
  list.value=active?.id || ""; byId("found").textContent=hits.length+" of "+index.length+" keys";
}
function renderExample() {
  const box=byId("example");box.replaceChildren();box.hidden=false;
  if(active.id==="57v.4"){
    box.append(el("h3","The red letters on f. 57v"),el("p","All 80 signs agree with the letters written above them. Follow row 4 in reading order to see the first word against the manuscript."));
    box.append(link("Inspect row 4, sign 1",hash(active.id,"S1")));
  }else if(active.id==="37r.1"){
    box.append(el("h3","One red letter differs"),el("p","On row 4, sign 7 is aligned with ي in the plaintext. The red gloss reads ب. The two letters have the same undotted shape."));
    box.append(link("Inspect S8 at the disagreement",hash(active.id,"S8")));
  }else box.hidden=true;
}
function lineView(place, sign, target) {
  target.replaceChildren();
  const [row,pos]=place, line=active.lines[row];
  target.append(el("p",rowName(row)+" · sign "+pos+" in reading order","loc"));
  const leaf=/^(\d+[rv])/.exec(row)?.[1] || active.id.split(".")[0];
  target.append(link("Open manuscript leaf "+leaf+" ↗","../ljs51-book/pages/0084_"+String(imageNo(leaf)).padStart(4,"0")+".jpg"));
  if(!line) return;
  const tx=el("div",undefined,"tokens");tx.dir=direction();
  for(const [i,item] of line.entries()){
    const [label,letter,recordPos]=item;
    const b=el("button",undefined, label===sign && (recordPos ?? i+1)===pos ? "mark" : "");
    const ar=el("span",letter || "?","ar");ar.lang="ar";ar.dir="rtl";
    const note=active.marks?.[row+"/"+(recordPos ?? i+1)];
    if(note){b.classList.add("doubt"); ar.textContent+="*";}
    b.append(el("small",label),ar);b.type="button";b.title="Sign "+(recordPos ?? i+1)+", "+label+(note?" · "+note:"");
    b.addEventListener("click",()=>{ location.hash=hash(active.id,label)+"/"+encodeURIComponent(row)+"/"+(recordPos ?? i+1); });tx.append(b);
  }
  target.append(tx);
  const notes=Object.entries(active.marks || {}).filter(([k])=>k.startsWith(row+"/")).map(([,v])=>v);
  for(const n of new Set(notes))target.append(el("p","* "+n,"loc"));
}
function inspect(c, requested) {
  const panel=byId("detail");
  panel.hidden=!c;panel.replaceChildren();
  if(!c)return;
  const head=el("div",undefined,"detail-head"), title=el("h3",c.id+" ");
  title.append(values(c));head.append(title,link("Close detail",hash(active.id)));panel.append(head);
  if(Number.isInteger(c.tile)){
    const specimen=picture(c);
    specimen.classList.add("detail-specimen");
    panel.append(specimen);
  }
  if(c.description)panel.append(el("p",c.description));
  if(c.uncertainty){
    const u=c.uncertainty;
    panel.append(el("p",u.evidence));
    if(Array.isArray(u.candidates))panel.append(el("p","Recorded possibilities: "+u.candidates.join(" / "),"loc"));
  }
  for(const [row,pos,letter] of c.gloss || [])panel.append(el("p",rowName(row)+", sign "+pos+" has the red gloss "+letter+".","loc"));
  if(c.trees?.length) panel.append(el("p","Trees (row.position): "+c.trees.join(", "),"loc"));
  if(c.sample) panel.append(el("p",(c.manual?"Manually located detail":"Position-matched detail")+" · "+rowName(c.sample[0])+", sign "+c.sample[1],"loc"));
  if(c.context){
    const a=link("","context/"+c.context), im=el("img",undefined,"source-photo");
    im.src=a.href;im.alt="Manuscript reference crop for "+c.id;a.append(im);
    panel.append(el("p","Reader’s reference crop"+(c.locator?" · "+c.locator:""),"loc"),a,el("span","Open the image at full size. Manuscript: Penn LJS 51.","crop-credit"));
  }
  if(c.refs.length){
    const where=el("div"),bar=el("div",undefined,"occ"),text=el("div"),locs=new Map();
    for(const item of c.refs){const row=item[0];if(!locs.has(row))locs.set(row,[]);locs.get(row).push(item[1]);}
    where.append(el("h3","Occurrences in the transcription"),bar,text);panel.append(where);
    const chosen=c.refs.find(([row,pos]) => requested && row===requested[0] && pos===requested[1]) || c.sample || c.refs[0];
    function pick(item,b){
      for(const x of bar.children)x.setAttribute("aria-pressed",String(x===b));
      lineView(item,c.id,text);
    }
    for(const [row,positions] of locs)for(const pos of positions){
      const b=el("button",rowName(row)+" · "+pos);b.type="button";
      b.addEventListener("click",()=>pick([row,pos],b));bar.append(b);
      if(chosen[0]===row && chosen[1]===pos)pick([row,pos],b);
    }
  }
}
function displayMode(view) {
  const isStrip=view==="strips";
  byId("strip-mode").setAttribute("aria-pressed",String(isStrip));
  byId("card-mode").setAttribute("aria-pressed",String(!isStrip));
  byId("cards").hidden=isStrip;
  const panel=byId("strips");panel.hidden=!isStrip;panel.replaceChildren();
  if(!isStrip)return;
  const groups=new Map();
  for(const c of active.cards){
    const key=c.context || "__"+c.id;
    if(!groups.has(key))groups.set(key,[]);
    groups.get(key).push(c);
  }
  for(const cards of groups.values()){
    const block=el("section",undefined,"folio-strip"), first=cards[0];
    if(first.context){
      const img=el("img");img.src="context/"+first.context;img.loading="lazy";
      img.alt="Manuscript reference for "+cards.map(c=>c.id).join(", ");
      const a=link("",img.src);a.append(img);block.append(a);
    }
    for(const c of cards){
      const row=el("div",undefined,"reading-row");
      row.append(link(c.id,hash(active.id,c.id)),values(c));
      const info=el("div");
      if(c.description)info.append(el("div",c.description));
      const ref=c.refs[0];
      const where=c.locator || (ref ? "First recorded occurrence: "+rowName(ref[0])+", sign "+ref[1] : "");
      if(where)info.append(el("div",where,"loc"));
      if(!first.context && c.tile!==undefined)info.prepend(picture(c));
      row.append(info);block.append(row);
    }
    panel.append(block);
  }
}
for(const [id,mode] of [["strip-mode","strips"],["card-mode","cards"]]){
  byId(id).addEventListener("click",()=>{selectedView=mode;displayMode(mode);});
}
function render(sign, requested) {
  const r=active, entry=index.find(x=>x.id===r.id), ix=index.indexOf(entry);
  document.title=folioTitle(r.id)+" · Visual keys · Penn LJS 51";
  byId("title").textContent=folioTitle(r.id);byId("kind").textContent=r.state;byId("record").href=repo+r.source;
  const leaves=byId("leaves");leaves.replaceChildren(...entry.folios.map(f=>link("Master "+f+" ↗",original(f))));
  const ordinary=r.state.includes("letter key");
  byId("provenance").textContent=ordinary?"Reconstructed from the compiler’s plaintext. Counts give the occurrences aligned with each letter. These readings await independent confirmation.":
    r.state==="Tree rule"?"The right branches select an abjad word; the left branches select the letter’s place in it. Counts give the recorded attestations of each rule entry.":
    r.state==="Undotted-letter classes"?"Each manuscript sign represents an undotted Arabic letter shape. Letters that differ only by dots can share one sign.":"Values and counts follow the companion study’s transcription and key.";
  for(const [name,delta] of [["prev",-1],["next",1]]){
    const b=byId(name), item=index[ix+delta];b.hidden=!item;
    if(item){b.href=hash(item.id);b.textContent=delta<0?"← "+item.id:item.id+" →";}
  }
  if(r.id==="106v.6")byId("provenance").textContent+=" Some signs are damaged. On the second cipher line the group (M) H (K) remains unread and at least two letters are lost. Asterisks identify the affected occurrences.";
  if(r.id==="48r.8")byId("provenance").textContent+=" The final five rows are on f. 21r. The horned sign EK has two recorded readings in this continuation.";
  byId("count").textContent=r.cards.length+" entries";byId("cards").replaceChildren();
  for(const c of r.cards){
    const a=link("",hash(r.id,c.id));a.className="card";if(c.id===sign)a.setAttribute("aria-current","true");
    a.append(picture(c),el("span",c.id,"name"),values(c));
    if(!Number.isInteger(c.tile)&&c.context)a.append(el("span",c.description || "Reference crop","small"));
    byId("cards").append(a);
  }
  displayMode(selectedView || (r.cards.every(c=>c.tile!==undefined || !c.context)?"cards":"strips"));
  showChoices();renderExample();inspect(r.cards.find(c=>c.id===sign), requested);byId("article").hidden=false;
  byId("loading").hidden=true;
}
async function navigate() {
  const seq=++sequence;
  try{
    let [id,sign,row,pos]=location.hash.slice(1).split("/").map(decodeURIComponent);
    id ||= "57v.4";
    if(!index.some(i=>i.id===id))throw new Error("No key is indexed at "+id+". Choose a cipher from the folio list.");
    if(!records.has(id)){
      const resp=await fetch("records/"+encodeURIComponent(id)+".json");if(!resp.ok)throw new Error("The key record could not be loaded.");
      records.set(id,await resp.json());
    }
    if(seq!==sequence)return;
    active=records.get(id);
    if(sign && !active.cards.some(c=>c.id===sign))throw new Error("This sign does not occur in the selected key.");
    render(sign, row ? [row,Number(pos)] : undefined);
    if(sign)byId("detail").scrollIntoView({block:"start"});
  }catch(e){if(seq===sequence){byId("article").hidden=true;byId("loading").hidden=false;byId("loading").textContent=e.message;}}
}
byId("find").addEventListener("input",showChoices);
byId("find").addEventListener("keydown",e=>{if(e.key==="Enter" && byId("folios").options.length){location.hash=hash(byId("folios").options[0].value);}});
byId("folios").addEventListener("change",e=>{if(e.target.value)location.hash=hash(e.target.value);});
window.addEventListener("hashchange",navigate);
(async()=>{try{const r=await fetch("index.json");if(!r.ok)throw new Error();index=await r.json();showChoices();await navigate();}catch{byId("loading").textContent="The key index could not be loaded. Reload the page to retry.";}})();
