# Model B5: bare sign -> letter; sign^digit -> letter + vowel (digit map fixed or free); sign^stroke -> own letter;
# sign under a bar -> code word (breaks the n-gram chain); dots ignored.
import sys, math, random, json
import numpy as np
sys.path.insert(0,'/home/claude/keyless/_cs'); sys.path.insert(0,'/home/claude/keyless/ercole1547/work')
import solver as S
LM=S.LM; A=len(LM.alpha)
def units(rows,opts):
    res=[]
    for ln,row in rows:
        r=[]
        for b,mk in row:
            if mk=='-' : r.append(None)
            elif mk=='': r.append((b,))
            elif mk in S.DIG: r.append((b,'^'+mk))
            elif opts.get('strokes')=='null': r.append((b,))
            elif opts.get('strokes')=='vowel': r.append((b,'^'+mk))
            else: r.append((b+'^'+mk,))
        res.append(r)
    return res
def segs(U,key):
    out=[]; cur=[]
    for line in U:
        for tok in line:
            if tok is None:
                if cur: out.append(''.join(cur)); cur=[]
            else: cur.append(''.join(key[s] for s in tok))
    if cur: out.append(''.join(cur))
    return out
def score(U,key,raw=False,W=4.0):
    tot=0.0; n=0; allx=[]
    for s in segs(U,key):
        x=LM.encode(s); allx.append(x)
        if len(x)>=5: tot+=LM.score_idx(x); n+=len(x)-4
    base=tot/max(1,n)
    if raw: return base
    x=np.concatenate(allx) if allx else np.zeros(0,dtype=np.int64)
    f=np.bincount(x,minlength=A)/max(1,len(x))
    return base-W*np.abs(f-S.EXP).sum()
def anneal(U,seed,iters,fixed,T0=0.3,T1=0.01,W=4.0):
    rnd=random.Random(seed)
    syms=sorted({s for line in U for tok in line if tok for s in tok})
    dom={s:(['']+list(S.VOW) if s.startswith('^') else list(S.LET)) for s in syms}
    key={s:rnd.choice(dom[s]) for s in syms}; key.update({k:v for k,v in fixed.items() if k in key})
    free=[s for s in syms if s not in fixed]
    N=sum(1 for l in U for t in l if t)
    cur=score(U,key,W=W); best=cur; bk=dict(key)
    for it in range(iters):
        T=T0*(T1/T0)**(it/iters)
        if rnd.random()<0.7:
            s=rnd.choice(free); old=key[s]; new=rnd.choice(dom[s])
            if new==old: continue
            key[s]=new; undo=[(s,old)]
        else:
            a,b=rnd.sample(free,2)
            if key[a]==key[b] or key[b] not in dom[a] or key[a] not in dom[b]: continue
            undo=[(a,key[a]),(b,key[b])]; key[a],key[b]=key[b],key[a]
        sc=score(U,key,W=W)
        if sc>cur or rnd.random()<math.exp((sc-cur)*N/(T*100)):
            cur=sc
            if sc>best: best=sc; bk=dict(key)
        else:
            for s,v in undo: key[s]=v
    return best,bk
if __name__=='__main__':
    opts=json.loads(sys.argv[1]); seeds=[int(x) for x in sys.argv[2].split(',')]; iters=int(sys.argv[3])
    fixed=opts.get('fixed',{}); merge=opts.get('merge')
    U=units(S.read(range(1,7),merge),opts)
    for sd in seeds:
        b,k=anneal(U,sd,iters,fixed,W=opts.get('W',4.0))
        print('OPTS',json.dumps(opts),'seed',sd,'score',round(b,4),'raw',round(score(U,k,True),4))
        print('   ',' | '.join(segs(U,k)))
        print('   key',' '.join('%s=%s'%(s,v or '-') for s,v in sorted(k.items())))
        sys.stdout.flush()
