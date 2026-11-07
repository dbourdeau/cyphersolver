import pickle,numpy as np,collections,random,sys
from sklearn.cluster import AgglomerativeClustering
pages=sys.argv[2].split(',')
recs=[]
for t in pages:
    recs+=pickle.load(open(f'sr_{t}/glyphs.pkl','rb'))
F=np.array([g['feat'] for g in recs])
def reps(lab,shuf=False,seed=1):
    lines={}
    for g,l in zip(recs,lab): lines.setdefault((g['page'],g['line']),[]).append(l)
    if shuf:
        flat=[t for v in lines.values() for t in v]; random.seed(seed); random.shuffle(flat)
        i=0;new={}
        for k,v in lines.items(): new[k]=flat[i:i+len(v)]; i+=len(v)
        lines=new
    out=[]
    for k in (3,4,5,6,8):
        c=collections.Counter()
        for v in lines.values():
            for i in range(len(v)-k+1): c[tuple(v[i:i+k])]+=1
        out.append(sum(x-1 for x in c.values() if x>1))
    return out
for n in [int(x) for x in sys.argv[1].split(',')]:
    lab=AgglomerativeClustering(n_clusters=n,linkage='ward').fit(F).labels_
    print(n,'real',reps(lab),'shuf',reps(lab,True),reps(lab,True,2))
