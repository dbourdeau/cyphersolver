"""Apply the final benchmark configuration (position + frequency prior + bigram context) to every group and run of the telegram.
Reports the readings with a clear margin between the best and second-best candidate."""
import re,sys,collections,json
import bench_loop as B
sys.stdout.reconfigure(encoding="utf8")
B.CFG.update(dict(unigram=True,bigram=True))
raw=open("inspecteurs_2nov_partial.txt",encoding="utf8").read().replace("’","'")
def strip(s): return B.strip(s)
seq=[]
for w in raw.replace("'"," ").split():
    if re.fullmatch(r"\d{4}",w): seq.append(("G",w))
    else:
        ww=re.sub(r"[^a-z0-9]","",strip(w.lower()))
        if ww: seq.append(("W",ww))
BEAC={"0101","0201","0301","0102","0202","0302","0103","0203","0303","0109","0113"}
# units: maximal runs of non-beacon groups; context = adjacent clear word (immediately before/after, skipping at most one beacon)
units=[]; i=0
while i<len(seq):
    t,w=seq[i]
    if t=="G" and w not in BEAC:
        j=i
        while j<len(seq) and seq[j][0]=="G" and seq[j][1] not in BEAC: j+=1
        groups=[x for _,x in seq[i:j]]
        def clear(k):
            return seq[k][1] if 0<=k<len(seq) and seq[k][0]=="W" else None
        left=clear(i-1) or (clear(i-2) if i-1>=0 and seq[i-1][0]=="G" and seq[i-1][1] in BEAC else None)
        right=clear(j) or (clear(j+1) if j<len(seq) and seq[j][0]=="G" and seq[j][1] in BEAC else None)
        units.append((i,tuple(groups),left,right)); i=j
    else: i+=1
print("units:",len(units),"distinct (groups,left,right):",len({(g,l,r) for _,g,l,r in units}))
known=set()
for n,g,gold,l,r in B.ITEMS: known.add(tuple(g))
cache={}
def firstok(x,g0):
    t=B.target(g0)
    return any(abs(B.pos(x[:j])-t)<0.07 for j in range(1,min(5,len(x))+1))
def rank(groups,left,right):
    key=(groups,left,right)
    if key in cache: return cache[key]
    k=len(groups); sc=[]
    for x in B.CANDS:
        if len(x)<k or (k==1 and len(x)<2): continue
        if k>1 and not firstok(x,groups[0]): continue
        s=B.score(x,list(groups),left,right)
        if s is not None: sc.append((s,x))
    sc.sort(reverse=True); cache[key]=sc[:5]; return cache[key]
out=[]
for idx,groups,left,right in units:
    if len(groups)>6: continue
    top=rank(groups,left,right)
    if len(top)>=2:
        out.append((top[0][0]-top[1][0],idx,groups,left,right,[(round(s,1),x) for s,x in top[:3]]))
out.sort(reverse=True)
json.dump([(m,i,list(g),l,r,t) for m,i,g,l,r,t in out],open("apply_telegram_out.json","w"),ensure_ascii=False)
print("\nmost confident readings (margin = best minus second-best log-score):")
seen=set()
for m,idx,groups,left,right,top in out:
    key=(groups)
    if key in seen: continue
    seen.add(key)
    ctx=" ".join(("[%s]"%x if t=="G" else x) for t,x in seq[max(0,idx-3):idx+len(groups)+3])
    print("  margin %5.1f  %-22s -> %-14s (2nd %s)   %s%s"%(m," ".join(groups),top[0][1],top[1][1],"known gold " if tuple(groups) in known else "",ctx))
    if len(seen)>=45: break
