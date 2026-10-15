import json, re, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'caprile1519'))   # shared fastanneal.py (split 14 Oct 2026)
import fastanneal as F
cnt=json.load(open('key21_counts.json'))
fixed={}
for t,c in cnt.items():
    n=sum(c.values()); l,m=max(c.items(),key=lambda x:x[1])
    if n>=6 and m/n>=0.85 and l in F.M.index: fixed[t]=l
fixed['OSO']='o'
seqs=[]
for line in open('c21_merged.txt',encoding='utf8'):
    if not line.split()[0] in ('R1139','R1136','V1921'): continue
    s=re.sub(r'\[[^\]]*\]',' | ',line.split(':',1)[1]).replace('o SL o','OSO')
    cur=[]
    for x in s.split():
        x=x.rstrip('?')
        if x=='|' or x.startswith('#'):
            if cur: seqs.append(cur); cur=[]
            continue
        cur.append(x)
    if cur: seqs.append(cur)
print('fixed',len(fixed),fixed)
(sc,key),toks=F.run(seqs,100000,10,seed=5,fixed=fixed)
k={t:F.M.alpha[v] for t,v in zip(toks,key)}
print('free:',{t:k[t] for t in toks if t not in fixed})
json.dump(k,open('key21_polished.json','w'),indent=0)
for s in seqs: print(''.join(k[t] for t in s))
