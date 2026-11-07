"""Hypothesis-testing engine driven by the wiki (see ../PROCESS.md).
  python engine.py calibrate      blind the supported entries and measure the gate on them (writes tests/T13.md)
  python engine.py loop [N]       run loops (default until 3 loops without a new accepted entry), writing claims, lexicon, log, index
State comes from ../lexicon_inspectors.json (accepted = supported/established); every accepted proposal is written back.
Units: a single undecided group = word unit; a maximal run of 2-6 undecided/known-piece groups = spelled unit.
Score of a candidate = alphabetical position fit (Gaussian sigma 0.02, +0.015 bias) + log unigram + bigram with the known neighbours (clear words or accepted readings), summed over every occurrence of the signature."""
import os,re,sys,math,json,collections,time,random
HERE=os.path.dirname(os.path.abspath(__file__)); TARGET=os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0,TARGET); sys.path.insert(0,HERE)
import numpy as np
import wikilib as W
import joint_loop as J
B=J.B
sys.stdout.reconfigure(encoding="utf8")
UNIQUE_MARGIN=10.0
PIECE_PATH=False   # H-piece (piece-level consistency gate) tested and rejected, see C034; kept for the record
SIG=0.02; BIAS=0.015; WU=1.0; SPELL_PEN=1.0; NCAND=40
WORDS=J.WORDS; RAWP=J.RAWP; LOGU=J.LOGU; LEN=J.LEN; PRE=J.PRE; SUF=J.SUF
W2I={w:i for i,w in enumerate(WORDS)}
TOPIC_LAM=0.25      # topic prior weight, fixed a priori (T17/C039); 0 disables
_tp=os.path.join(W.ROOT,"topic_counts.json")
if TOPIC_LAM>0 and os.path.exists(_tp):
    _D=json.load(open(_tp,encoding="utf8"))["counts"]; _ND=sum(_D.values()); _VD=len(_D)
    for _i,_w in enumerate(WORDS):
        _pd=(_D.get(_w,0)+0.1)/(_ND+0.1*_VD)
        LOGU[_i]=math.log(TOPIC_LAM*_pd+(1-TOPIC_LAM)*math.exp(LOGU[_i]))
P1=np.exp(LOGU)
succ=collections.defaultdict(list); pred=collections.defaultdict(list)
for (a,b),c in B.bi.items():
    if a in W2I and b in W2I: succ[a].append((W2I[b],c)); pred[b].append((W2I[a],c))
_lv={}; _rv={}
def left_vec(a):
    if a not in _lv:
        v=np.log(0.28*P1)
        ua=B.uni.get(a,0)
        for i,c in succ.get(a,[]): v[i]=math.log(0.72*c/ua+0.28*P1[i])
        _lv[a]=v
    return _lv[a]
def right_vec(b):
    if b not in _rv:
        pb=P1[W2I[b]] if b in W2I else 1e-9
        v=np.full(len(WORDS),math.log(0.28*pb))
        for i,c in pred.get(b,[]): v[i]=math.log(0.72*c/B.uni[WORDS[i]]+0.28*pb)
        _rv[b]=v
    return _rv[b]
TGT_OVR={}
def tgt(g): return TGT_OVR[g] if g in TGT_OVR else int(g)/9999.0+BIAS
BEACONS={"0101","0201","0301","0102","0202","0302","0103","0203","0303"}
# ------------------------------------------------------------------ state from the wiki
def accepted_lexicon(exclude=()):
    lex={}
    for e in W.load_lex("inspectors")["entries"]:
        if e["status"] in ("supported","established") and e["group"] not in exclude: lex[e["group"]]=(e["kind"],e["reading"])
    return lex
def resolve(tok,lex):
    """replace known groups by words where a whole word is known; return token list with ('W',w) / ('B',b) / ('G',g)"""
    out=[];i=0;n=len(tok)
    while i<n:
        k,v=tok[i]
        if k!="G": out.append((k,v)); i+=1; continue
        j=i
        while j<n and tok[j][0]=="G": j+=1
        block=[tok[x][1] for x in range(i,j)]
        # merge maximal runs of known pieces/words that form complete words: a known word group alone; consecutive known pieces form one word
        a=0
        while a<len(block):
            g=block[a]
            if g in lex and lex[g][0]=="word": out.append(("W",lex[g][1])); a+=1; continue
            if g in lex and lex[g][0]=="piece":
                b=a
                while b<len(block) and block[b] in lex and lex[block[b]][0]=="piece": b+=1
                # a run of known pieces is a complete word only if bracketed by beacons/clear words on both sides of the whole block
                bracket=(i>0 and tok[i-1][0]=="B" and j<n and tok[j][0]=="B")
                if a==0 and b==len(block) and bracket:      # only a wholly known beacon-bounded run becomes a word; partly known runs stay whole
                    out.append(("W","".join(lex[block[x]][1] for x in range(a,b)))); a=b; continue
            out.append(("G",g)); a+=1
        i=j
    return out
# ------------------------------------------------------------------ units
def units(tok2):
    """signature -> list of (left, right) contexts; also positions for greedy non-overlap"""
    sig=collections.defaultdict(list); n=len(tok2)
    def ctx(i,j):
        l=tok2[i-1][1] if i>0 and tok2[i-1][0]=="W" else None
        r=tok2[j][1] if j<n and tok2[j][0]=="W" else None
        return l,r
    i=0
    while i<n:
        if tok2[i][0]!="G": i+=1; continue
        j=i
        while j<n and tok2[j][0]=="G": j+=1
        grp=tuple(tok2[x][1] for x in range(i,j))
        for a in range(len(grp)):
            sig[(grp[a],)].append((ctx(i+a,i+a+1),(i+a,i+a+1)))
        bracket=(i>0 and tok2[i-1][0]=="B" and j<n and tok2[j][0]=="B")
        if 2<=len(grp)<=6 and bracket: sig[grp].append((ctx(i,j),(i,j)))   # C002: spelled words are the beacon-bounded runs
        i=j
    return sig
# ------------------------------------------------------------------ candidate scoring
def fit_word(g,t=None):
    t=tgt(g) if t is None else t
    return -0.5*((RAWP-t)/SIG)**2
def split_cost(x,groups,known):
    n=len(x);k=len(groups); INF=1e9
    if k>n: return None
    tg=[tgt(g) for g in groups]
    dp=[[INF]*(n+1) for _ in range(k+1)]; dp[0][0]=0.0
    for i in range(1,k+1):
        for j in range(i,n+1):
            for t in range(max(i-1,j-10),j):
                if dp[i-1][t]>=INF: continue
                piece=x[t:j]
                if groups[i-1] in known: c=0.0 if piece==known[groups[i-1]] else 1e3
                else:
                    e=(B.rawpos(piece)-tg[i-1])/SIG; c=0.5*e*e
                if dp[i-1][t]+c<dp[i][j]: dp[i][j]=dp[i-1][t]+c
    return None if dp[k][n]>=INF else dp[k][n]
def best_split(x,groups,known):
    n=len(x);k=len(groups); INF=1e9; tg=[tgt(g) for g in groups]
    dp=[[INF]*(n+1) for _ in range(k+1)]; dp[0][0]=0.0; bk={}
    for i in range(1,k+1):
        for j in range(i,n+1):
            for t in range(max(i-1,j-10),j):
                if dp[i-1][t]>=INF: continue
                piece=x[t:j]
                if groups[i-1] in known: c=0.0 if piece==known[groups[i-1]] else 1e3
                else: e=(B.rawpos(piece)-tg[i-1])/SIG; c=0.5*e*e
                if dp[i-1][t]+c<dp[i][j]: dp[i][j]=dp[i-1][t]+c; bk[(i,j)]=t
    cuts=[];j=n
    for i in range(k,0,-1): t=bk[(i,j)]; cuts.append(x[t:j]); j=t
    return cuts[::-1]
def known_pieces(lex): return {g:r for g,(k,r) in lex.items() if k=="piece"}
def cand_scores(sigt,contexts,lex,occ_subset=None,tfake=None):
    """returns list of (score, string index or word) sorted desc for a signature; contexts = list of (left,right)"""
    ctxs=contexts if occ_subset is None else [contexts[i] for i in occ_subset]
    k=len(sigt)
    if k==1:
        s=fit_word(sigt[0],tfake)+WU*LOGU
        for l,r in ctxs:
            if l: s=s+left_vec(l)
            if r: s=s+right_vec(r)
        idx=np.argpartition(-s,NCAND)[:NCAND]
        res=sorted(((float(s[i]),int(i)) for i in idx),reverse=True)
        return res
    t0=tgt(sigt[0]) if tfake is None else tfake[0]; tl=tgt(sigt[-1]) if tfake is None else tfake[-1]
    known=known_pieces(lex); sl=0.07
    m=(LEN>=k)&(PRE[:,0]-sl<=t0)&(t0<=PRE[:,1]+sl)&(SUF[:,0]-sl<=tl)&(tl<=SUF[:,1]+sl)
    res=[]
    for i in np.nonzero(m)[0]:
        x=WORDS[i]
        if len(x)<max(4,k+1): continue          # a word spelled in pieces has at least 4 letters
        c=split_cost(x,sigt,known)
        if c is None or c>1e2: continue
        s=-c+WU*LOGU[i]-SPELL_PEN
        for l,r in ctxs:
            if l: s+=left_vec(l)[i]
            if r: s+=right_vec(r)[i]
        res.append((s,int(i)))
    res.sort(reverse=True); return res[:NCAND]
def evaluate(sigt,contexts,lex,null_draws=0,rng=None):
    """full test battery for one signature; returns dict"""
    k=len(sigt); kp=known_pieces(lex)
    cs=cand_scores(sigt,contexts,lex)
    if len(cs)==0: return None
    if len(cs)==1: (s1,i1)=cs[0]; (s2,i2)=cs[0]; margin=UNIQUE_MARGIN     # a single surviving candidate: unique under the constraints
    else:
        (s1,i1),(s2,i2)=cs[0],cs[1]; margin=s1-s2
    x=WORDS[i1]
    def ctx_only(i):
        t=0.0
        for l,r in contexts:
            if l: t+=left_vec(l)[i]
            if r: t+=right_vec(r)[i]
        return t
    ctx_margin=ctx_only(i1)-ctx_only(i2)
    known_n=sum(1 for g in sigt if g in kp) if k>1 else 0
    if k==1: fit_err=abs(RAWP[i1]-tgt(sigt[0])); fit_ok=fit_err<=0.02
    else:
        cuts=best_split(x,sigt,kp)
        errs=[abs(B.rawpos(c)-tgt(g)) for c,g in zip(cuts,sigt) if g not in kp]
        fit_err=float(np.mean(errs)) if errs else 0.0; fit_ok=(fit_err<=0.02 and (max(errs) if errs else 0)<=0.035)
    rep=None
    if len(contexts)>=2:
        a_=cand_scores(sigt,contexts,lex,occ_subset=list(range(0,len(contexts),2)))[0][1]
        b_=cand_scores(sigt,contexts,lex,occ_subset=list(range(1,len(contexts),2)))[0][1]
        rep=(a_==i1 and b_==i1)
    null95=None
    rng=rng or random.Random(3)
    if null_draws and k==1:
        ms=[]
        for _ in range(null_draws):
            tf=rng.uniform(0.03,0.97); sc=cand_scores(sigt,contexts,lex,tfake=tf)
            ms.append(sc[0][0]-sc[1][0])
        null95=float(np.percentile(ms,95))
    nullfit5=None
    if null_draws and k>1 and known_n>=1:
        # null for the piece-consistency path: how well can the BEST string fit random values for the unknown groups when the same pieces are fixed?
        nf=[]; unk=[g for g in sigt if g not in kp]
        for _ in range(min(null_draws,30)):
            for g in unk: TGT_OVR[g]=rng.uniform(0.03,0.97)
            sc=cand_scores(sigt,contexts,lex)
            if sc:
                xi=WORDS[sc[0][1]]; cuts_=best_split(xi,sigt,kp)
                nf.append(float(np.mean([abs(B.rawpos(c)-tgt(g)) for c,g in zip(cuts_,sigt) if g not in kp])))
            else: nf.append(1.0)
            TGT_OVR.clear()
        nullfit5=float(np.percentile(nf,5))
    return dict(sig=sigt,word=x,second=WORDS[i2],margin=margin,ctx_margin=ctx_margin,known_n=known_n,fit_err=fit_err,fit_ok=fit_ok,rep=rep,null95=null95,nullfit5=nullfit5,n_occ=len(contexts),split=(best_split(x,sigt,kp) if k>1 else [x]))
UNIQUE_MARGIN=10.0
CTX_MIN=3.0
def passes(r,M):
    if r is None or not r["fit_ok"] or r["margin"]<M: return False
    if PIECE_PATH and len(r["sig"])>1 and r.get("known_n",0)>=1:
        # piece-consistency path (H-piece): the accepted pieces are the evidence; the margin must beat the null built with random values for the unknown groups
        return r.get("nullfit5") is not None and r["fit_err"]<=r["nullfit5"] and len(r["word"])>=max(4,len(r["sig"])+1)
    if r["ctx_margin"]<CTX_MIN: return False      # otherwise: context evidence beyond the frequency prior is required
    if r["null95"] is not None and r["margin"]<r["null95"]: return False
    if r["rep"] is None: return r["margin"]>=2*M
    return bool(r["rep"])
# ------------------------------------------------------------------ gold for calibration
GOLD_SIG={("4007",):{"general"},("3407",):{"est"},("1026",):{"bonne"},("8416",):{"sante"},("7027","0312"):{"portante"},("9113","8317","1504"):{"trochu"},
          ("5504","1122","2514","3316"):{"mercadier"},("6816","4001","6129","8328"):{"pigeons"},("8328","9214","0218","4906","3316","8328"):{"steenackers","steenakers"},("0919","5121","6129"):{"ballon","ballons"}}
GOLD_GROUPS={g for s in GOLD_SIG for g in s}
def run_proposals(lex,M,null_draws=60,only=None,verbose=False):
    tok2=resolve(J.TOK,lex); sig=units(tok2); out=[]
    for s,occ in sig.items():
        if only is not None and s not in only: continue
        if all(g in lex for g in s): continue
        ctxs=[c for c,pos in occ]
        r=evaluate(s,ctxs,lex,null_draws=null_draws)
        if r is None: continue
        r["pos"]=[pos for c,pos in occ]; r["passes"]=passes(r,M); out.append(r)
    return out,tok2
def greedy_accept(props,M):
    """accept passing proposals in order of margin, skipping overlaps (a group may be accepted only once)"""
    acc=[];used=set()
    for r in sorted((p for p in props if p["passes"]),key=lambda p:-p["margin"]):
        gs=set(r["sig"])
        if gs&used: continue
        acc.append(r); used|=gs
    return acc
def calibrate(Ms=(2,3,4,6,8,12,16)):
    base=accepted_lexicon(); blind=accepted_lexicon(exclude=GOLD_GROUPS)
    print("calibration: %d accepted entries, %d blinded gold groups"%(len(base),len(GOLD_GROUPS))); sys.stdout.flush()
    props,tok2=run_proposals(blind,0,null_draws=60,only=set(GOLD_SIG)|{(g,) for g in GOLD_GROUPS})
    rows=[]
    for M in Ms:
        for p in props: p["passes"]=passes(p,M)
        acc=greedy_accept([p for p in props],M)
        corr=inc=0;detail=[]
        for r in acc:
            gold=GOLD_SIG.get(r["sig"])
            if gold is None: continue    # single group inside a gold run: judged only when it is a gold unit
            ok=r["word"] in gold; corr+=ok; inc+=(not ok); detail.append((r["sig"],r["word"],"ok" if ok else "WRONG"))
        rows.append((M,corr,inc,detail))
        print("  M=%-3s accepted gold units: correct %d, incorrect %d"%(M,corr,inc)); sys.stdout.flush()
    # also show the raw best proposal for every gold unit
    print("\nbest proposal for every gold unit (blind):")
    for s,gold in GOLD_SIG.items():
        r=next((p for p in props if p["sig"]==s),None)
        if r: print("  %-34s -> %-12s second %-12s margin %5.1f fit %.3f rep %s null95 %s  gold %s %s"%(" ".join(s),r["word"],r["second"],r["margin"],r["fit_err"],r["rep"],"%.1f"%r["null95"] if r["null95"] is not None else "-","/".join(sorted(gold)),"HIT" if r["word"] in gold else "miss"))
    return rows,props

def calibrate_pieces():
    """leave-one-unit-out for the piece-consistency path: blind a gold spelled unit's groups EXCEPT those fixed by another gold unit"""
    spelled=[s for s in GOLD_SIG if len(s)>=3]
    base_inv=W.load_lex("inspectors")["entries"]
    full=accepted_lexicon()
    rows=[]
    for s in spelled:
        others=set(g for t in GOLD_SIG if t!=s for g in t)
        shared=[g for g in s if g in others]; blind=set(g for g in s if g not in others)
        lex=dict(full)
        for g in blind: lex.pop(g,None)
        # ballon: bal and l are hypothesis entries (not accepted), so 6129 alone is the known piece
        pr,_=run_proposals(lex,2,null_draws=30,only={s})
        r=pr[0] if pr else None
        gold=GOLD_SIG[s]
        if r is None: rows.append((s,None)); print("  %-34s no proposal"%" ".join(s)); continue
        ok=r["word"] in gold
        print("  %-34s known pieces %d/%d -> %-12s (second %-12s) margin %5.1f fit %.3f vs null 5th pct %s passes %s  gold %s %s"%(" ".join(s),sum(1 for g in s if g in lex and lex[g][0]=="piece"),len(s),r["word"],r["second"],r["margin"],r["fit_err"],"%.3f"%r["nullfit5"] if r.get("nullfit5") is not None else "-",r["passes"],"/".join(sorted(gold)),"HIT" if ok else "miss")); sys.stdout.flush()
        rows.append((s,r,ok))
    return rows

def coverage(lex):
    g=[v for k,v in J.TOK if k=="G"]
    return sum(1 for x in g if x in lex)/len(g),len(g)
def claim_for(r,status,conf,note,existing):
    cid=W.next_id("C",100,existing); existing.add(cid)
    sig=" ".join(r["sig"]); word=r["word"]
    body="Engine proposal for the unit `%s` (%d occurrence(s)): **%s** (second best %s). Margin %.1f nats; position fit error %.3f; replicate %s; null 95th percentile %s. %s"%(
        sig,r["n_occ"],word,r["second"],r["margin"],r["fit_err"],r["rep"],("%.1f"%r["null95"]) if r["null95"] is not None else "n/a",note)
    W.write_page("claim",cid,dict(id=cid,type="claim",title="%s = %s (engine)"%(sig,word),status=status,confidence=conf,evidence=["T13"],depends=["C001"],updated="2026-11-07"),body)
    return cid
def loop(max_loops=12,M=2):
    noprog=0; hist=[]
    existing=set(W.pages())
    for n in range(1,max_loops+1):
        inv=W.load_lex("inspectors"); lex=accepted_lexicon()
        cov0,ng=coverage(lex)
        props,tok2=run_proposals(lex,M,null_draws=60)
        demoted=[]
        for e in inv["entries"]:
            if e.get("auto")=="true" and e["status"]=="supported":
                sig=tuple(e["unit"].split("_"))
                lexb=accepted_lexicon(exclude=set(sig)); pr,_=run_proposals(lexb,M,null_draws=60,only={sig})
                r=pr[0] if pr else None
                if not (r and r["passes"] and r["word"]==e["unit_word"]): e["status"]="hypothesis"; demoted.append(e["group"])
        acc=greedy_accept(props,M)
        newc=[]
        have=set(tuple(e.get("unit","").split("_")) for e in inv["entries"] if e.get("auto")=="true" and e["status"]=="supported")
        for r in acc:
            if r["sig"] in have: continue
            cid=claim_for(r,"supported",round(min(0.8,0.5+r["margin"]/40),2),"Accepted by the gate (M=%s)."%M,existing); newc.append(cid)
            if len(r["sig"])==1: ents=[(r["sig"][0],"word",r["word"])]
            else: ents=[(g,"piece",p) for g,p in zip(r["sig"],r["split"])]
            for g,kind,rd in ents:
                if any(x["group"]==g and x["status"] in ("supported","established") for x in inv["entries"]): continue   # never overwrite an accepted entry
                inv["entries"]=[x for x in inv["entries"] if x["group"]!=g]
                inv["entries"].append(dict(group=g,kind=kind,reading=rd,status="supported",claims=[cid],confidence=0.6,auto="true",unit="_".join(r["sig"]),unit_word=r["word"]))
        titles={fm.get("title") for k,(fm,b,p) in W.pages().items() if fm}
        rej=[r for r in sorted(props,key=lambda p:-p["margin"]) if not r["passes"] and r["fit_ok"]][:6]
        for r in rej:
            title="%s = %s (engine)"%(" ".join(r["sig"]),r["word"])
            if title in titles: continue
            why=[]
            if r["margin"]<M: why.append("margin below %s"%M)
            if r["null95"] is not None and r["margin"]<r["null95"]: why.append("margin below the null 95th percentile (%.1f)"%r["null95"])
            if r["rep"] is False: why.append("odd and even occurrences disagree")
            if r["rep"] is None and r["margin"]<2*M: why.append("single occurrence needs margin >= %s"%(2*M))
            claim_for(r,"hypothesis",0.25,"Not accepted: %s. Evidence needed: a second occurrence with a known neighbour, or an independent source for the name or word."%"; ".join(why or ["failed the gate"]),existing)
        W.save_lex("inspectors",inv); lex=accepted_lexicon(); cov1,_=coverage(lex)
        hist.append((n,len(acc),len(demoted),cov0,cov1,len(props)))
        print("LOOP %d: %d units proposed, %d accepted, %d demoted; coverage %.1f%% -> %.1f%% of %d coded groups"%(n,len(props),len(acc),len(demoted),100*cov0,100*cov1,ng)); sys.stdout.flush()
        W.log("loop","engine loop %d"%n,"%d proposals, %d accepted (%s), %d demoted; coverage %.1f%% -> %.1f%%."%(len(props),len(acc),", ".join(newc) or "none",len(demoted),100*cov0,100*cov1))
        if not newc and not demoted: noprog+=1
        else: noprog=0
        if noprog>=3: print("STOP: 3 loops without progress"); break
    return hist
if __name__=="__main__":
    mode=sys.argv[1] if len(sys.argv)>1 else "calibrate"
    t0=time.time()
    if mode=="calibrate":
        rows,props=calibrate()
        print("[%.0fs]"%(time.time()-t0))
    elif mode=="pieces":
        calibrate_pieces(); print("[%.0fs]"%(time.time()-t0))
    elif mode=="loop":
        hist=loop(int(sys.argv[2]) if len(sys.argv)>2 else 12)
        print("[%.0fs]"%(time.time()-t0))
