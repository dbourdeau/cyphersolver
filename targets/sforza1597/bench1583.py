import pickle, numpy as np, collections, re, sys
from sklearn.cluster import AgglomerativeClustering
gt='C:/Users/dbour/cypher/targets/it1583/lasry2026/ctts/'
P=np.loadtxt(gt+'positions/1_positions.txt')
T=open(gt+'transcription/1.txt').read().strip().split('\n')[1:]
toks=[[t for t in l.split(';') if t] for l in T]
cnt=[len(t) for t in toks]; assert sum(cnt)<=len(P)
his=[];i=0
for l in toks:
    rows=P[i:i+len(l)]; i+=len(l)
    his.append((rows[:,0]+rows[:,2]/2, l))
recs=pickle.load(open('sr_it1583/glyphs.pkl','rb'))
n=int(sys.argv[1]) if len(sys.argv)>1 else 40
F=np.array([r['feat'] for r in recs]); lab=AgglomerativeClustering(n_clusters=n,linkage='ward').fit(F).labels_
mine=collections.defaultdict(list)
for r,l in zip(recs,lab): mine[r['line']].append((r['x']+r['w']/2,int(l)))
def norm(x): x=np.array(x,float); return (x-x.min())/(x.max()-x.min()+1e-9)
pairs=[]; conf=collections.defaultdict(collections.Counter); tot=0; hit=0
for hi,(hx,hl) in enumerate(his):
    best=None
    for ml,mv in mine.items():
        mx=np.array([a for a,_ in mv]); 
        if len(mx)<5: continue
        a=norm(hx); b=norm(mx)
        d=np.abs(a[:,None]-b[None,:]); j=d.argmin(1); ok=d[np.arange(len(a)),j]<0.01
        s=ok.sum()
        if best is None or s>best[0]: best=(s,ml,j,ok)
    s,ml,j,ok=best
    mv=mine[ml]
    for k in range(len(hl)):
        if ok[k]:
            conf[hl[k]][mv[j[k]][1]]+=1; hit+=1
        tot+=1
    pairs.append((hi+1,len(hl),ml,len(mv),int(s)))
print('line pairs (his line, his n, my line, my n, matched):',pairs)
print('matched glyphs',hit,'of',tot,'= segmentation recall',round(hit/tot,3))
# purity of my clusters w.r.t. his labels, and of his labels w.r.t. my clusters
mine_to=collections.defaultdict(collections.Counter)
for h,c in conf.items():
    for m,v in c.items(): mine_to[m][h]+=v
pur=sum(max(c.values()) for c in mine_to.values())/hit
inv=sum(max(c.values()) for c in conf.values())/hit
print('my clusters',n,'-> purity vs his labels',round(pur,3),'| his labels covered by one cluster',round(inv,3))
# adjusted rand
from sklearn.metrics import adjusted_rand_score
a=[];b=[]
for h,c in conf.items():
    for m,v in c.items(): a+= [h]*v; b+=[m]*v
print('ARI',round(adjusted_rand_score(a,b),3),'his types',len(conf),'my used',len(mine_to))
