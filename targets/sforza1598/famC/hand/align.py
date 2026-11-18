"""Align the hand transcription (tokens per line) to signreader boxes, so each hand token gets an image box."""
import pickle,numpy as np,collections,math,json
from sklearn.cluster import AgglomerativeClustering
PG=[('R5518_I30589_P','famC/hand/t2.txt'),('R5514_I30585_P','famC/hand/t14.txt'),('R5517_I30588_P','famC/hand/t17.txt')]
G={};allg=[]
for p,_ in PG:
    r=pickle.load(open(f'sr_{p}/glyphs2.pkl','rb'))
    for g in r: allg.append(g)
    G[p]=collections.defaultdict(list)
    for g in r: G[p][g['line']].append(g)
F=np.array([g['feat'] for g in allg]); lab=AgglomerativeClustering(n_clusters=60,linkage='ward').fit(F).labels_
for g,l in zip(allg,lab): g['cl']=int(l)
H={p:[l.split() for l in open(f).read().strip().split('\n')] for p,f in PG}
H['R5514_I30585_P'][14]=H['R5514_I30585_P'][14]+H['R5514_I30585_P'][15]; del H['R5514_I30585_P'][15]
FORCED={'R5518_I30589_P':{i:i+1 for i in range(11)},'R5514_I30585_P':{i:i+1 for i in range(26)},'R5517_I30588_P':{**{i:i+2 for i in range(10)},**{i:i+3 for i in range(10,33)}}}
for p in G:
    for li in G[p]: G[p][li].sort(key=lambda g:g['x'])
cost=None
def mc(t,c): return 1.0 if cost is None else min(1.95,cost.get((t,c),1.95))
GT,GB=1.3,0.9   # token without box (merged), box without token (clear text, specks)
def align(toks,boxes):
    n,m=len(toks),len(boxes);D=np.full((n+1,m+1),1e9);B=np.zeros((n+1,m+1),int);D[0,:]=np.arange(m+1)*GB;D[:,0]=np.arange(n+1)*GT
    for i in range(1,n+1):
        for j in range(1,m+1):
            a=D[i-1,j-1]+mc(toks[i-1],boxes[j-1]['cl']);b=D[i-1,j]+GT;c=D[i,j-1]+GB
            D[i,j],B[i,j]=min((a,0),(b,1),(c,2))
    i,j,pairs=n,m,[]
    while i>0 and j>0:
        if B[i,j]==0: pairs.append((i-1,j-1));i-=1;j-=1
        elif B[i,j]==1: i-=1
        else: j-=1
    return D[n,m]/max(1,n),pairs[::-1]
def linemap(p):
    return FORCED[p]
def _old(p):
    toks=H[p]; dl=sorted(G[p]); n,m=len(toks),len(dl)
    S=[[align(toks[i],G[p][dl[j]])[0] for j in range(m)] for i in range(n)]
    D=np.full((n+1,m+1),1e9);D[0,:]=0;B={}
    for i in range(1,n+1):
        for j in range(1,m+1):
            a=D[i-1,j-1]+S[i-1][j-1]; b=D[i,j-1]
            D[i,j],B[i,j]=(a,0) if a<b else (b,1)
    i,j,mp=n,int(np.argmin(D[n])),{}
    while i>0 and j>0:
        if B[i,j]==0: mp[i-1]=dl[j-1];i-=1;j-=1
        else: j-=1
    return mp
for it in range(4):
    pairs=[]
    for p in G:
        mp=linemap(p)
        for i,li in mp.items():
            _,pr=align(H[p][i],G[p][li])
            pairs+= [(H[p][i][a],G[p][li][b]['cl']) for a,b in pr]
    ct=collections.Counter(pairs); tc=collections.Counter(t for t,_ in pairs)
    cost={(t,c):-math.log((n+0.1)/(tc[t]+6)) for (t,c),n in ct.items()}
    print('iter',it,'aligned',len(pairs),'of',sum(len(l) for p in H for l in H[p]),flush=True)
out=[]
for p in G:
    mp=linemap(p)
    for i,li in mp.items():
        _,pr=align(H[p][i],G[p][li])
        for a,b in pr:
            g=G[p][li][b]; out.append(dict(page=p,hline=i,ti=a,tok=H[p][i][a],line=li,k=g['k'],x=g['x'],w=g['w'],cl=g['cl']))
json.dump(out,open('famC/hand/align.json','w'))
pickle.dump({(o['page'],o['line'],o['k']):o for o in out},open('famC/hand/align.pkl','wb'))
print('line maps',{p:linemap(p) for p in G})
