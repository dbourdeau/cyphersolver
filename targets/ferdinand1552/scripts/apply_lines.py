"""Turn cipher_lines.tsv into work/sel.pkl {(page,line): [sign indices]} (signs whose centre lies in the x range)."""
import pickle
P=pickle.load(open('work/pages.pkl','rb'))
sel={}
for l in open('cipher_lines.tsv',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    f=l.rstrip('\n').split('\t')
    p,rng=f[0],f[1]; xmin=float(f[2])/0.55 if len(f)>2 and f[2] else 0; xmax=float(f[3])/0.55 if len(f)>3 and f[3] else 1e9
    a,b=(rng.split('-')+[rng])[:2] if '-' in rng else (rng,rng)
    for j in range(int(a),int(b)+1):
        ss=sorted(P[p][j]['signs'],key=lambda s:s['x0'])
        idx=[i for i,s in enumerate(ss) if xmin<=(s['x0']+s['x1'])/2<=xmax]
        sel.setdefault((p,j),[]); sel[(p,j)]+=idx
pickle.dump(sel,open('work/sel.pkl','wb')); print(len(sel),'lines',sum(map(len,sel.values())),'signs')
