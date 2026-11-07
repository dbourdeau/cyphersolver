"""Joint decoder + hypothesis loop for the alphabetical inspectors' code (Steenackers to Mercadier, Tours 2 Nov 1870).
Decoder: beam-Viterbi over the whole telegram. Clear words are fixed; beacon groups reset the LM; each run of groups is cut into chunks;
a chunk of k groups is one string (k=1: whole-word group; k>=2: a word spelled in k pieces). Chunk score = alphabetical position fit
(Gaussian, sigma 0.02, +0.015 bias) + weight*log unigram; chunks are chained by a bigram LM.
Benchmark: the 20 gold word occurrences; a hit = the decode produces exactly that word at that place. Keep a hypothesis if it adds >= 1 hit; stop after 3 losses in a row.
Run: python joint_loop.py"""
import re,sys,math,collections,json,time
import numpy as np
import bench_loop as B
sys.stdout.reconfigure(encoding="utf8")
B.CFG.update(dict(unigram=False,bigram=False))
SIG=0.02; BIAS=0.015
WORDS=[w for w in B.CANDS if len(w)>=2]
RAWP=np.array([B.rawpos(w) for w in WORDS])
LOGU=np.array([B.lp_uni(w) for w in WORDS])
LEN=np.array([len(w) for w in WORDS])
# prefix / suffix position ranges for fast filtering of spelled candidates
def rng(w,kind):
    ps=[B.rawpos(w[:j]) for j in range(1,min(6,len(w))+1)] if kind=="pre" else [B.rawpos(w[-j:]) for j in range(1,min(7,len(w))+1)]
    return min(ps),max(ps)
PRE=np.array([rng(w,"pre") for w in WORDS]); SUF=np.array([rng(w,"suf") for w in WORDS])
raw=open("inspecteurs_2nov_partial.txt",encoding="utf8").read().replace("’","'")
TOK=[]
for w in raw.replace("'"," ").split():
    if re.fullmatch(r"\d{4}",w): TOK.append(("B",w) if w in {"0101","0201","0301","0102","0202","0302","0103","0203","0303"} else ("G",w))
    else:
        ww=re.sub(r"[^a-z0-9]","",B.strip(w.lower()))
        if ww: TOK.append(("W",ww))
L=len(TOK)
tgt=lambda g: int(g)/9999.0+BIAS
# ---------------- gold occurrences: (start token, [group tokens], [gold word strings])
def find(pattern):
    out=[];n=len(pattern)
    for i in range(L-n+1):
        if all(TOK[i+j][1]==pattern[j] for j in range(n)): out.append(i)
    return out
GOLD=[]   # (start, ngroups, words)  words = list of accepted-gold lists, one per chunk
def addgold(name,pattern,off,groups,chunks):
    for i in find(pattern): GOLD.append((name,i+off,groups,chunks))
addgold("general",["au","4007"],1,1,[{"general"}])
addgold("est",["3407","bien"],0,1,[{"est"}])
addgold("bonne-sante",["1026","8416"],0,2,[{"bonne"},{"sante"}])
addgold("portante",["bien","7027","0312","a"],1,2,[{"portante"}])
addgold("trochu",["9113","8317","1504"],0,3,[{"trochu"}])
addgold("mercadier",["5504","1122","2514","3316"],0,4,[{"mercadier"}])
addgold("pigeons",["6816","4001","6129","8328"],0,4,[{"pigeons"}])
addgold("steenackers",["8328","9214","0218","4906","3316","8328"],0,6,[{"steenackers","steenakers"}])
addgold("ballon",["0919","5121","6129"],0,3,[{"ballon","ballons"}])
NGOLD=sum(len(c) for _,_,_,c in GOLD)
# ---------------- candidate lists
H=dict(spelled_bracket=False,free_seg=False,consist=False,mono=False,N=40,wu=1.0,spell_pen=1.0)
cache={}
def single_cands(g,lo=None,hi=None,force=None):
    t=tgt(g)
    s=-0.5*((RAWP-t)/SIG)**2+H["wu"]*LOGU
    if lo is not None: s=np.where((RAWP>=lo)&(RAWP<=hi),s,-1e9)
    idx=np.argpartition(-s,H["N"])[:H["N"]]
    out=[(float(s[i]),WORDS[i]) for i in idx if s[i]>-1e8]
    if not out:      # window empty: fall back to the unconstrained candidates
        s=-0.5*((RAWP-t)/SIG)**2+H["wu"]*LOGU
        idx=np.argpartition(-s,H["N"])[:H["N"]]
        out=[(float(s[i]),WORDS[i]) for i in idx]
    if force: out=[(sc,w) for sc,w in out if w==force] or [(0.0,force)]
    return out
def spelled_cands(groups):
    key=tuple(groups)
    if key in cache: return cache[key]
    k=len(groups); t0=tgt(groups[0]); tl=tgt(groups[-1]); sl=0.07
    m=(LEN>=k)&(PRE[:,0]-sl<=t0)&(t0<=PRE[:,1]+sl)&(SUF[:,0]-sl<=tl)&(tl<=SUF[:,1]+sl)
    res=[]
    for i in np.nonzero(m)[0]:
        c=B.split_cost(WORDS[i],list(groups))
        if c is not None: res.append((-c+H["wu"]*LOGU[i]-H["spell_pen"],WORDS[i]))
    res.sort(reverse=True); cache[key]=res[:H["N"]]; return cache[key]
B.CFG["bias"]=BIAS; B.CFG["sigma"]=SIG
# ---------------- Viterbi
def decode(lex=None,bounds=None,beam=25):
    lex=lex or {}
    states=[dict() for _ in range(L+1)]
    states[0][None]=(0.0,None)
    def push(p,key,sc,bp):
        cur=states[p].get(key)
        if cur is None or sc>cur[0]: states[p][key]=(sc,bp)
    for p in range(L):
        st=states[p]
        if not st: continue
        items=sorted(st.items(),key=lambda kv:-kv[1][0])[:beam]
        kind,val=TOK[p]
        if kind=="W":
            for last,(sc,_) in items: push(p+1,val,sc+(B.lp_bi(last,val) if last else 0.0),(p,last,1,val))
        elif kind=="B":
            for last,(sc,_) in items: push(p+1,None,sc,(p,last,1,None))
        else:
            r=0
            while p+r<L and TOK[p+r][0]=="G": r+=1
            before_b=(p==0 or TOK[p-1][0]=="B"); after_b=(p+r<L and TOK[p+r][0]=="B")
            for m in range(1,min(r,6)+1):
                groups=[TOK[p+j][1] for j in range(m)]
                if m>=2:
                    ok=H["free_seg"] and m<=4
                    if H["spelled_bracket"] and before_b and after_b and m==r: ok=True
                    if not ok: continue
                    cl=spelled_cands(groups)
                else:
                    g=groups[0]
                    lo=hi=None
                    if bounds and g in bounds: lo,hi=bounds[g]
                    cl=single_cands(g,lo,hi,lex.get(g))
                for last,(sc,_) in items:
                    for ls,w in cl:
                        push(p+m,w,sc+ls+(B.lp_bi(last,w) if last else 0.0),(p,last,m,w))
    end=max(states[L].items(),key=lambda kv:kv[1][0])
    # backtrack
    chunks={}; p=L; key=end[0]
    while p>0:
        sc,bp=states[p][key]; pp,last,m,w=bp
        if TOK[pp][0]=="G": chunks[pp]=(m,w)
        p=pp; key=last
    return chunks
def score_gold(chunks):
    hit=0;rows=[]
    for name,start,ng,chs in GOLD:
        pos=start; ok_all=True; got=[]
        # consume chunks across the span
        covered=0; i=start
        while covered<ng and i in chunks:
            m,w=chunks[i]; got.append(w); covered+=m; i+=m
        # compare with gold chunks only if the chunk structure matches
        if len(got)==len(chs) and covered==ng:
            for g,gold in zip(got,chs):
                if g in gold: hit+=1
        rows.append((name,start,got))
    return hit,rows
def vote(chunks,prev_lex,thr=0.6):
    occ=collections.defaultdict(list)
    for i,(m,w) in chunks.items():
        if m==1: occ[TOK[i][1]].append(w)
    lex=dict(prev_lex)
    for g,ws in occ.items():
        if len(ws)>=2:
            w,c=collections.Counter(ws).most_common(1)[0]
            if c/len(ws)>=thr: lex[g]=w
    return lex
def mono_bounds(chunks,lex):
    """alphabetical-order constraint: a group's position must lie between those of the nearest confident groups on each side"""
    conf=sorted((int(g),B.rawpos(w)) for g,w in lex.items())
    bounds={}
    gs=sorted({TOK[i][1] for i in range(L) if TOK[i][0]=="G"},key=int)
    for g in gs:
        v=int(g); lo=0.0;hi=1.0
        for gv,pv in conf:
            if gv<v: lo=max(lo,pv)
            elif gv>v: hi=min(hi,pv); break
        if lo-0.02<=hi+0.02: bounds[g]=(lo-0.02,hi+0.02)   # skip inverted windows (non-monotone lexicon)
    return bounds
def run():
    chunks=decode()
    if H["consist"]:
        lex={}
        for it in range(3):
            lex=vote(chunks,lex)
            bounds=mono_bounds(chunks,lex) if H["mono"] else None
            chunks=decode(lex,bounds)
    elif H["mono"]:
        lex=vote(chunks,{},0.0)   # use all decoded groups with >=2 occurrences as neighbours
        for it in range(3):
            bounds=mono_bounds(chunks,lex); chunks=decode({},bounds); lex=vote(chunks,{},0.0)
    return score_gold(chunks),chunks
HYPS=[
 ("H1 bracket hypothesis: a run between two beacons may be one spelled word",dict(spelled_bracket=True)),
 ("H2 segmentation: any run may be cut into spelled chunks of up to 4 groups",dict(free_seg=True)),
 ("H3 consistency: a group has one meaning everywhere (hard-EM voting, 3 passes)",dict(consist=True)),
 ("H4 monotonicity: strings must follow the numeric order of the groups (neighbour bounds)",dict(mono=True)),
 ("H5 search breadth: 100 candidates per chunk instead of 40",dict(N=100)),
 ("H6 weaker frequency prior (0.5) to stop function words crowding out content words",dict(wu=0.5)),
]
if __name__=="__main__":
    print("tokens",L,"gold occurrences",len(GOLD),"gold words",NGOLD)
    t0=time.time()
    (hit,rows),chunks=run(); best=hit
    print("LOOP 0 baseline (whole-word groups only, position+prior+bigram): %d/%d gold words  [%.0fs]"%(hit,NGOLD,time.time()-t0)); sys.stdout.flush()
    log=[("baseline",hit)]; noprog=0
    for n,(name,change) in enumerate(HYPS,1):
        old={k:H[k] for k in change}; H.update(change); cache.clear()
        t0=time.time(); (hit,rows),chunks=run()
        verdict="KEPT" if hit>=best+1 else "rejected"
        print("LOOP %d  %s\n    %d/%d gold words (%+d) -> %s   [%.0fs]"%(n,name,hit,NGOLD,hit-best,verdict,time.time()-t0)); sys.stdout.flush()
        log.append((name,hit,verdict))
        if hit>=best+1: best=hit; noprog=0
        else: H.update(old); noprog+=1
        if noprog>=3: print("STOP: 3 loops without progress"); break
    print("\nFINAL: %d/%d gold words with config %s"%(best,NGOLD,{k:v for k,v in H.items()}))
    json.dump(log,open("joint_loop_log.json","w"))
