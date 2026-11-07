"""Segmentation-aware decoding test: for a run of groups, compare every way of cutting it into consecutive words
(each word spelled by its groups) using position fit + frequency prior (+ bigram with clear neighbours).
Gold: [1026 8416] = bonne|sante (2 words), [7027 0312] = portante (1 word), [6816 4001 6129 8328] = pigeons (1), [5504 1122 2514 3316] = mercadier (1)."""
import sys,itertools
import bench_loop as B
sys.stdout.reconfigure(encoding="utf8")
B.CFG.update(dict(unigram=True,bigram=False))
def top_chunk(groups,n=3,left=None,right=None):
    k=len(groups); best=[]
    t0=B.target(groups[0])
    for x in B.CANDS:
        if len(x)<k or (k==1 and len(x)<2): continue
        if k>1 and not any(abs(B.pos(x[:j])-t0)<0.07 for j in range(1,min(5,len(x))+1)): continue
        s=B.score(x,list(groups),None,None)
        if s is not None: best.append((s,x))
    best.sort(reverse=True); return best[:n]
cache={}
def chunk(groups):
    g=tuple(groups)
    if g not in cache: cache[g]=top_chunk(g)
    return cache[g]
def segmentations(n):
    for mask in range(1<<(n-1)):
        cuts=[i+1 for i in range(n-1) if mask>>i&1]
        yield [0]+cuts+[n]
def decode(run,left=None,right=None):
    n=len(run); res=[]
    for seg in segmentations(n):
        words=[];tot=0.0
        for a,b in zip(seg,seg[1:]):
            c=chunk(run[a:b])
            if not c: tot=None;break
            tot+=c[0][0]; words.append(c[0][1])
        if tot is None: continue
        # bigram between adjacent chosen words and clear neighbours
        seq=([left] if left else [])+words+([right] if right else [])
        bg=sum(B.lp_bi(a,b) for a,b in zip(seq,seq[1:]))
        res.append((tot+bg,tot,bg,words))
    res.sort(reverse=True)
    return res
tests=[("bonne sante",["1026","8416"],"en",None,"bonne sante"),
       ("portante",["7027","0312"],"bien","a","portante"),
       ("pigeons",["6816","4001","6129","8328"],"par","dabord","pigeons"),
       ("mercadier",["5504","1122","2514","3316"],None,None,"mercadier"),
       ("est bien (single est)",["3407"],None,"bien","est")]
for name,run,l,r,gold in tests:
    res=decode(run,l,r)
    print("\n%s  groups %s  (context left=%s right=%s)"%(name," ".join(run),l,r))
    for s,t,bg,w in res[:5]: print("   score %7.1f (fit+prior %6.1f, bigram %5.1f)  %s"%(s,t,bg," | ".join(w)))
    rk=next((i+1 for i,(s,t,bg,w) in enumerate(res) if " ".join(w)==gold),None)
    print("   gold '%s' rank %s of %d segmentations"%(gold,rk,len(res)))
