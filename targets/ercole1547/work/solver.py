import sys, re, math, random, json
import numpy as np
sys.path.insert(0,'/home/claude/keyless/_cs')
from lang import lm
LM=lm.DenseLM(np.load('/home/claude/keyless/ercole1547/work/it1540.o5.ns.npy'),5,lm.alphabet('early',False))
CONS='bcdfghlmnpqrstuz'; VOW='aeiou'; LET='abcdefghilmnopqrstuz'
DIG=('s','4','6','7','8','9','2','4s')
def read(lines,merge=None,path='/home/claude/keyless/ercole1547/TRANSCRIPTION.tsv'):
    out=[]
    for l in open(path):
        if not l.startswith('16v'): continue
        pg,ln,t=l.rstrip('\n').split('\t')
        if int(ln) not in lines: continue
        row=[]
        for tok in t.split():
            if tok.startswith('{') or tok.startswith('.'): continue
            tok=tok.replace('?','')
            b,_,mk=tok.partition('^')
            if merge: b=merge.get(b,b)
            row.append((b,mk))
        out.append((int(ln),row))
    return out
def units(rows,model):
    """return list of lines, each a list of tokens, each token a tuple of symbol names"""
    res=[]
    for ln,row in rows:
        r=[]
        for b,mk in row:
            if model=='A': r.append((b,))
            elif model=='B':
                if mk=='' : r.append((b,))
                elif mk in DIG: r.append((b,'^'+mk))
                else: r.append((b+'^'+mk,))
            elif model=='B2':   # stroke marks ignored (null), digit marks vowels
                if mk in DIG: r.append((b,'^'+mk))
                else: r.append((b,))
            elif model=='B3':   # every mark is a following-letter symbol
                if mk=='': r.append((b,))
                else: r.append((b,'^'+mk))
            elif model=='C': r.append((b+('^'+mk if mk else ''),))
        res.append(r)
    return res
def domain(sym,model):
    if sym.startswith('^'):
        if model=='B3': return ['']+list(LET)
        return ['']+list(VOW)
    return list(LET)
def decode(U,key):
    return [''.join(''.join(key[s] for s in tok) for tok in line) for line in U]
def _expected():
    import collections
    t=lm.norm(open('/home/claude/leads_15nov/dl/serristori_legazioni.txt',encoding='utf-8',errors='replace').read(),'early',False)
    c=collections.Counter(t); n=sum(c.values())
    return np.array([c.get(a,0)/n for a in LM.alpha])
EXP=_expected(); W=4.0
def score(U,key,raw=False):
    s=''.join(decode(U,key))
    x=LM.encode(s)
    n=max(1,len(x)-4)
    base=LM.score_idx(x)/n
    if raw: return base,len(x)
    f=np.bincount(x,minlength=len(LM.alpha))/max(1,len(x))
    return base-W*np.abs(f-EXP).sum(), len(x)
def anneal(U,model,seed,iters=150000,T0=0.25,T1=0.01,fixed=None,verbose=False):
    rnd=random.Random(seed)
    syms=sorted({s for line in U for tok in line for s in tok})
    dom={s:domain(s,model) for s in syms}
    key={s:rnd.choice(dom[s]) for s in syms}
    if fixed: key.update(fixed)
    free=[s for s in syms if not fixed or s not in fixed]
    cur,_=score(U,key); best=cur; bk=dict(key)
    N=sum(len(l) for l in U)
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
        sc,_=score(U,key)
        if sc>cur or rnd.random()<math.exp((sc-cur)*N/ (T*100)):
            cur=sc
            if sc>best: best=sc; bk=dict(key)
        else:
            for s,v in undo: key[s]=v
    return best,bk
if __name__=='__main__':
    model=sys.argv[1]; seeds=[int(x) for x in sys.argv[2].split(',')]; iters=int(sys.argv[3])
    merge=json.loads(sys.argv[4]) if len(sys.argv)>4 else None
    rows=read(range(1,7),merge); U=units(rows,model)
    Uh=units(read((7,8),merge),model)
    for sd in seeds:
        b,k=anneal(U,model,sd,iters)
        hk={s:k.get(s,'?') for line in Uh for tok in line for s in tok}
        print('MODEL',model,'seed',sd,'score',round(b,4),'raw',round(score(U,k,True)[0],4),'len',score(U,k)[1])
        for d in decode(U,k): print('   ',d)
        print('   key',' '.join('%s=%s'%(s,v or '-') for s,v in sorted(k.items())))
        sys.stdout.flush()
