import re,sys,json,em
from seg import split, units
def norm5(t):
    # DECODE writes the 5 as '21' or '13' (and other 1x forms); fold to '5'
    if t[:2]=='21' and len(t)>=4: return '51'+t[2:]
    if t[:2]=='13' and len(t)>=4: return '53'+t[2:]
    return t
def lines(a,b):
    out=[]
    for i,l in enumerate(open('img/DOC_R1874_D3607_3607.txt',encoding='utf8')):
        if a<=i+1<=b and l.strip() and not l.startswith(('#','<')):
            s=l.replace('?','').replace("'",'')
            gs=[]
            for g in re.split(r'\s{2,}',s.strip()):
                g=g.replace(' ','')
                if not g.isdigit(): continue
                gs+= split(g) if len(g)>4 else [g]
            out+=gs
    return out
FOLD='fold' in sys.argv
def prep(G): return [norm5(g) if FOLD else g for g in G]
txt=open('tx/decipherment.txt',encoding='utf8').read()
P=dict((int(k),em.norm(v)) for k,v in re.findall(r'\[(\d+)\]\n([^\[]*)',txt))
i=P[5].index('etgiasie')
A=P[5][i:]+P[6]+P[7]
G=prep(lines(74,117))
print(len(G),len(A),len(A)/len(G))
t,cnt=em.run([(G,A)],iters=30)
key={g:max(d,key=d.get) for g,d in t.items()}
json.dump({g:[key[g],round(max(t[g].values()),2)] for g in key},open('key1%s.json'%('f' if FOLD else ''),'w'),indent=0)
import collections
c=collections.Counter(G)
for g,n in c.most_common(60): print(g,n,key.get(g),round(max(t[g].values()),2) if g in t else '')
