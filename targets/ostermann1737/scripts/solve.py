import sys,random,math,collections
sys.path.insert(0,'/home/claude/keyless/ostermann1737/scripts')
from common import *
import rulm
def text_words(lines, sep=('l','Z'), spaces=True):
    ws=[]
    for ln,words in load(lines):
        for w in words:
            cur=[]
            for s in w:
                if s in sep or s=='?':
                    if cur: ws.append(cur); cur=[]
                else: cur.append(s)
            if cur: ws.append(cur)
    return ws
def render(ws,key,spaces=True):
    j=' ' if spaces else ''
    return j.join(''.join(key.get(s,'?') for s in w) for w in ws)
def anneal(ws,m,signs,alpha,iters=30000,T0=6.0,seed=0,spaces=True,init=None,fixed=()):
    rnd=random.Random(seed)
    if init: key=dict(init)
    else:
        fr=collections.Counter(s for w in ws for s in w)
        order=[s for s,_ in fr.most_common()]+[s for s in signs if s not in fr]
        fl='оеаинтъсрвлкдмпуыгябьзхчжѣюшцщф'
        fl=''.join(c for c in fl if c in alpha)
        key={s:fl[i%len(fl)] for i,s in enumerate(order)}
        for f,v in fixed: key[f]=v
    free=[s for s in signs if s not in dict(fixed)]
    cur=m.score(render(ws,key,spaces)); best=cur; bk=dict(key)
    for it in range(iters):
        T=T0*(1-it/iters)+0.05
        a=rnd.choice(free); k2=dict(key)
        if rnd.random()<0.7:
            b=rnd.choice(free)
            if a==b: continue
            k2[a],k2[b]=key[b],key[a]
        else:
            used=set(key.values()); un=[c for c in alpha if c not in used]
            if not un: continue
            k2[a]=rnd.choice(un)
        sc=m.score(render(ws,k2,spaces))
        if sc>cur or rnd.random()<math.exp((sc-cur)/T):
            key,cur=k2,sc
            if cur>best: best,bk=cur,dict(key)
    return best,bk
if __name__=='__main__':
    order=int(sys.argv[1]) if len(sys.argv)>1 else 5
    spaces=(sys.argv[2]!='nosp') if len(sys.argv)>2 else True
    nres=int(sys.argv[3]) if len(sys.argv)>3 else 12
    m=rulm.LM(rulm.corpus(),order)
    ws=text_words(TRAIN)
    signs=sorted(set(s for w in ws for s in w))
    print('signs',len(signs),'chars',sum(map(len,ws)),'words',len(ws),flush=True)
    res=[]
    for seed in range(nres):
        b,k=anneal(ws,m,signs,rulm.ALPHA,seed=seed,spaces=spaces)
        res.append((b,k)); print(seed,round(b,1),render(ws,k,spaces)[:150],flush=True)
    b,k=max(res,key=lambda x:x[0])
    print('BEST',b); print(render(ws,k,spaces)); print(sorted(k.items()))
