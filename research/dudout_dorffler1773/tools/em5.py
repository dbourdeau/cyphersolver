# Token-level (syllable) monotone EM. code emits 0..LM tokens; gloss tokens skippable.
import sys, math, json, collections
import numpy as np
sys.path.insert(0,__file__.rsplit('/',1)[0])
from parse import load
from syl import tokens
NEG=-1e30
def prep(path,mode='block'):
    blocks=load(path); units=[]
    for b in blocks:
        seq=[(t,v) for t,v in b['lines'] if t in 'CG']
        if mode=='block':
            C=[x for t,v in seq if t=='C' for x in v]; S=[x for t,v in seq if t=='G' for x in tokens(v)]
            units.append({'id':b['id'],'C':C,'S':S})
        else:
            for k,(t,v) in enumerate(seq):
                if t!='C': continue
                up=[];dn=[];j=k-1
                while j>=0 and seq[j][0]=='G': up=tokens(seq[j][1])+up; j-=1
                j=k+1
                while j<len(seq) and seq[j][0]=='G': dn+=tokens(seq[j][1]); j+=1
                units.append({'id':'%s:%d'%(b['id'],k),'C':v,'S':up+dn})
    return units
def run(units,iters=30,LM=2,p0=0.08,skips=0.15,E=None,verbose=False):
    tc=collections.Counter(t for u in units for t in u['S']); T=sum(tc.values())
    lt={t:math.log(v/T) for t,v in tc.items()}
    LENP={0:p0,1:0.8,2:0.12}
    ls=math.log(skips)
    E=E or {}
    for it in range(iters):
        counts=collections.defaultdict(lambda: collections.defaultdict(float)); LL=0
        for u in units:
            C=u['C']; S=u['S']; n=len(C); m=len(S)
            if not S: continue
            EM=np.full((n,LM+1,m+1),NEG)
            for i,c in enumerate(C):
                d=None if c.startswith('?') else E.get(c)
                for L in range(0,LM+1):
                    for j in range(L,m+1):
                        t=tuple(S[j-L:j])
                        b=math.log(LENP[L])+sum(lt[x] for x in t)
                        if d is None: v=b
                        else:
                            v=d.get('|'.join(t)); v= v if v is not None else d['__f']+b
                        EM[i,L,j]=v
            js=np.concatenate([[0.0],np.cumsum([ls+lt[x] for x in S])])
            F=np.full((n+1,m+1),NEG); F[0]=js
            for i in range(1,n+1):
                G=np.full(m+1,NEG)
                for L in range(0,LM+1):
                    tmp=np.full(m+1,NEG); tmp[L:]=F[i-1][:m+1-L]+EM[i-1,L,L:]; G=np.logaddexp(G,tmp)
                F[i]=np.logaddexp.accumulate(G-js)+js
            Z=F[n,m]; LL+=Z
            B=np.full((n+1,m+1),NEG); B[n]=js[m]-js
            ar=js
            for i in range(n-1,-1,-1):
                G=np.full(m+1,NEG)
                for L in range(0,LM+1):
                    tmp=np.full(m+1,NEG); tmp[:m+1-L]=B[i+1][L:]+EM[i,L,L:]; G=np.logaddexp(G,tmp)
                B[i]=np.logaddexp.accumulate((G+ar)[::-1])[::-1]-ar
            for i in range(n):
                c=C[i]
                if c.startswith('?'): continue
                for L in range(0,LM+1):
                    post=F[i][:m+1-L]+EM[i,L,L:]+B[i+1][L:]-Z
                    for j in np.nonzero(post>-5)[0]:
                        counts[c]['|'.join(S[j:j+L])]+=math.exp(post[j])
        newE={}
        for c,d in counts.items():
            tt=sum(d.values())
            dd={t:math.log(v/(tt+0.5)) for t,v in d.items() if v>0.02}
            dd['__f']=math.log(0.5/(tt+0.5)); newE[c]=dd
        E=newE
        if verbose: print(it,round(LL,1),flush=True)
    return E,counts,LL
if __name__=='__main__':
    U=prep(sys.argv[1],sys.argv[2])
    E,counts,LL=run(U,iters=int(sys.argv[3]),verbose=False)
    print('LL',LL)
    json.dump(E,open(sys.argv[4],'w'))
    for c,d in sorted(counts.items(),key=lambda x:-sum(x[1].values()))[:90]:
        tt=sum(d.values()); top=sorted(d.items(),key=lambda x:-x[1])[:4]
        print(c,round(tt,1),' '.join('%s:%.2f'%(t,v/tt) for t,v in top))
