"""EM alignment of cipher units (round-6 p*r.txt) with the clear letters (clear_running.txt).
Writes ext/alignment.json (per unit: line, sign, emitted letters, word index, type) and ext/counts.json."""
import json,math,sys,collections
import numpy as np
sys.path.insert(0,'.')
import dec14
U=dec14.U
def units(toks):
    out=[];i=0
    while i<len(toks):
        t=toks[i]; n=toks[i+1] if i+1<len(toks) else None; n2=toks[i+2] if i+2<len(toks) else None
        if t=='o' and n=='H' and n2 in U: out.append(('oH',2));i+=2;continue
        if t=='H' and n=='o': out.append(('Ho',2));i+=2;continue
        if t in('6','6A') and n=='gA': out.append(('LL',2));i+=2;continue
        if t=='G' and n in('a','p'): out.append(('G'+n,2));i+=2;continue
        if t=='v' and n=='e': out.append(('ve',2));i+=2;continue
        if t=='O' and out and out[-1][0] in dec14.USIGN: out.append(('Om',1));i+=1;continue
        if t=='n': out.append(('nq' if n in U else 'ni',1));i+=1;continue
        out.append((t if t not in('','?','??') else '_',1));i+=1
    return out
UN=[];LN=[]
for h,t in dec14.lines():
    for s,n in units(t): UN.append((s,n));LN.append(h)
signs=[s for s,_ in UN]
words=json.load(open('ext/clear_words.json'))
L=''.join(words); N=len(L)
wid=[];ws=[]  # word index of each letter
for k,w in enumerate(words):
    ws.append(len(wid)); wid+= [k]*len(w)
wstart=np.array(ws); wend=np.array(ws[1:]+[N])
freq=collections.Counter(L); f={c:freq[c]/N for c in freq}
def prior(s):
    if s=='': return 0.03
    p={1:0.9,2:0.05,3:0.005}[len(s)]
    if len(s)==2 and s[0]==s[1]: return 0.05*f.get(s[0],1e-4)
    for c in s: p*=f.get(c,1e-4)
    return p
CODEP=1e-6
key=json.load(open('key_final.json'))
cnt=collections.defaultdict(collections.Counter)
for s,v in key.items():
    if v=='#': continue
    for alt in v.split('/'): cnt[s][alt]+=3
SEED={'Gp':{'non':2},'y':{'ducentamilia':1}}  # hypotheses from first pass (Gp before 'citius'/'noua'); kept as weak persistent seeds
for a,d in SEED.items():
    for v,c in d.items(): cnt[a][v]+=c
g=5.0
def ecost(s,string,code=False):
    c=cnt[s]; C=sum(c.values()); a=1.0
    p=(c[string]+a*(CODEP if code else prior(string)))/(C+a)
    return -math.log(p)
NU=len(signs)
def run():
    INF=1e9
    D=np.full(N+1,INF,dtype=np.float64); D[:]=g*np.arange(N+1)*0.3  # free-ish start
    bt=np.zeros((NU+1,N+1),dtype=np.int8); bsrc=np.zeros((NU+1,N+1),dtype=np.int32)
    rows=[D]
    idx=np.arange(N+1)
    cache={}
    for u,s in enumerate(signs):
        new=np.full(N+1,INF); typ=np.full(N+1,-1,dtype=np.int8); src=idx.copy()
        if s=='_':
            ek={0:3.0,1:1.5,2:3.0,3:4.5}
            vecs={k:np.full(N+1-k,ek[k]) for k in range(4)}
        else:
            if s not in cache:
                vecs={}
                for k in range(4):
                    strs=[L[i:i+k] for i in range(N+1-k)]
                    m={x:ecost(s,x) for x in set(strs)}
                    vecs[k]=np.array([m[x] for x in strs])
                cache[s]=vecs
            vecs=cache[s]
        for k in range(4):
            cand=D[:N+1-k]+vecs[k]
            better=cand<new[k:]
            new[k:]=np.where(better,cand,new[k:]); typ[k:]=np.where(better,k,typ[k:]); src[k:]=np.where(better,idx[:N+1-k],src[k:])
        if s!='_':
            for nw in range(1,5):
                if nw>len(words): break
                st=wstart[:len(words)-nw+1]; en=wend[nw-1:]
                cc=np.array([ecost(s,L[a:b],True) for a,b in zip(st,en)])
                cand=D[st]+cc
                for a,b,c in zip(st,en,cand):
                    if c<new[b]: new[b]=c; typ[b]=10+nw; src[b]=a
        # skip clear letters (writer omission)
        adj=new-g*idx; cm=np.minimum.accumulate(adj)
        # argmin positions for cummin
        arg=np.maximum.accumulate(np.where(adj<=cm+1e-12,idx,0))
        skipped=(cm+g*idx)<new-1e-9
        newD=np.minimum(new,cm+g*idx)
        typ=np.where(skipped,-2,typ); src=np.where(skipped,arg,src)
        bt[u+1]=typ; bsrc[u+1]=src
        D=newD
    endc=D+g*0.3*(N-idx); i=int(np.argmin(endc))
    path=[]
    for u in range(NU,0,-1):
        t=bt[u,i]; sr=bsrc[u,i]
        if t==-2:
            # skipped letters sr..i inside row u, real emission ends at sr
            path.append(('skip',u,sr,i)); i=sr; t=bt[u,i]; sr=bsrc[u,i]
        path.append(('emit',u-1,sr,i,int(t))); i=sr
    path.reverse()
    return path,float(np.min(endc)),i
for it in range(6):
    path,score,st=run()
    newc=collections.defaultdict(collections.Counter); nskip=0; nemit=0
    for p in path:
        if p[0]=='skip': nskip+=p[3]-p[2]; continue
        _,u,a,b,t=p; s=signs[u]
        if s=='_': continue
        newc[s][L[a:b]]+=1; nemit+=b-a
    # keep a small trace of key14 to break ties
    for s,v in key.items():
        if v=='#': continue
        for alt in v.split('/'): newc[s][alt]+=0.3
    for a,d in SEED.items():
        for v,c in d.items(): newc[a][v]+=c
    cnt=newc
    g=min(8.0,max(3.0,-math.log(max(nskip,1)/(nskip+nemit))))
    print('iter',it,'score',round(score,1),'skipped letters',nskip,'g',round(g,2),flush=True)
out=[]
for p in path:
    if p[0]=='skip': out.append({'type':'skip','u':p[1],'a':int(p[2]),'b':int(p[3])}); continue
    _,u,a,b,t=p
    out.append({'type':'code' if t>=10 else 'emit','u':u,'sign':signs[u],'line':LN[u],'ntok':UN[u][1],'a':int(a),'b':int(b),'txt':L[a:b]})
json.dump({'L':L,'words':words,'wid':wid,'start':int(st),'path':out},open('ext/alignment.json','w'))
