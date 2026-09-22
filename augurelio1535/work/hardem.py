import json,subprocess,sys,os,math
from collections import Counter,defaultdict
cur=sys.argv[1]; files=sys.argv[2:]
env=dict(os.environ,SP='1',PYTHONUTF8='1')
EM=json.load(open(os.environ.get('EMF','em1.json'),encoding='utf8'))
for it in range(int(os.environ.get('IT','4'))):
    cnt=defaultdict(Counter)
    for f in files:
        subprocess.run([sys.executable,'beam.py',cur,f,f'_h_{f}'],env=env,capture_output=True)
        for g,o in json.load(open(f'_h_{f}.aln.json',encoding='utf8')):
            o=o.strip()
            if o: cnt[g][o]+=1
    new={}
    for g,c in cnt.items():
        n=sum(c.values()); d={}
        for o,k in c.most_common(4): d[o]=(k+0.5)/(n+2)
        for o,p in EM.get(g,{}).items():   # keep EM alternatives as weak options
            if o not in d: d[o]=0.3*p*1/(n+2)**0.5
        new[g]={o:round(p,4) for o,p in sorted(d.items(),key=lambda x:-x[1])[:5]}
    cur=f'{os.environ.get("PFX","hk")}{it}.json'; json.dump(new,open(cur,'w',encoding='utf8'),ensure_ascii=False)
    print(it,{g:list(v)[:3] for g,v in sorted(new.items())},flush=True)
