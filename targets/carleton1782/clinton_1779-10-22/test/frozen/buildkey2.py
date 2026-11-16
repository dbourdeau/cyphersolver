# Construit key2_armylist.tsv selon PREREG_2026-11-16.md (apprentissage v.758 seulement)
import sys,itertools,collections
sys.path.insert(0,'.')
from fit1778 import lines,pairs
byline=collections.defaultdict(list)
for a,b in pairs:
    r,c=map(int,a.split('-')); byline[r].append((c,b))
def sc(s,obs): return sum(1 for c,b in obs if 1<=c<=len(s) and s[c-1]==b)
key={}; log=[]
for r,s in sorted(lines.items()):
    obs=byline.get(r,[])
    base=sc(s,obs); best=base; tied=[s]; kbest=0
    for k in (1,2):
        vs={}
        for pos in itertools.combinations(range(len(s)),k):
            t=''.join(ch for i,ch in enumerate(s) if i not in pos); vs[t]=sc(t,obs)
        if not vs: continue
        m=max(vs.values())
        if m>best: best=m; kbest=k; tied=[t for t,v in vs.items() if v==m]
    L=max(len(t) for t in tied)
    for c in range(1,L+1):
        ls={t[c-1] if c<=len(t) else None for t in tied}
        key['%d-%d'%(r,c)]=ls.pop() if len(ls)==1 and None not in ls else '?'
    log.append((r,kbest,len(tied),best,len(obs)))
cnt=collections.defaultdict(collections.Counter)
for a,b in pairs: cnt[a][b]+=1
src={}
for k in key: src[k]='armylist-variante'
for a,c in cnt.items():
    key[a]=c.most_common(1)[0][0]; src[a]='appris(%d)'%sum(c.values())
with open('key2_armylist.tsv','w') as f:
    f.write('# cellule\tlettre\tsource  (PREREG_2026-11-16 ; apprentissage v.758 C1-C7)\n')
    for k in sorted(key,key=lambda s:tuple(map(int,s.split('-')))): f.write('%s\t%s\t%s\n'%(k,key[k],src[k]))
for x in log: print(x)
print('cells',len(key),'unknown',sum(v=='?' for v in key.values()))
