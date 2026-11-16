"""Show each run's groups with key-v2 letters and the letters reachable by the allowed digit confusions (5/9, 3/7, 0/6, 2/7, 8->w); w6, ww shown as candidates i, o."""
import json, sys, re, itertools
key={k:v for k,v in json.load(open(sys.argv[1])).items() if not k.startswith('_')}
cand=dict(key); cand.update({'w6':'i*','ww':'o*','62':'q*'})
conf={'5':'9','9':'5','3':'7','7':'32','0':'6','6':'0','2':'7','8':'w'}
def alts(g):
    out=set()
    for a in [g[0]]+list(conf.get(g[0],'')):
        for b in [g[1]]+list(conf.get(g[1],'')):
            if a+b in cand: out.add(cand[a+b] if a+b==g else cand[a+b]+'~')
    return '/'.join(sorted(out)) or '.'
def toks(s):
    s=re.sub(r'\[([^/\]]+)/[^\]]*\]',r'\1',s)
    return [t for t in s.split() if t]
rows=[l.rstrip('\n').split('\t') for l in open(sys.argv[2]) if not l.startswith('#') and not l.startswith('leaf')]
rows=[r for r in rows if len(r)>=5 and not r[2].startswith('x') and r[0] not in ('19r','62r')]
if 'passB' in sys.argv[2]: rows=rows[::-1]
runs={}; order=[]
for r in rows:
    k=(r[0],r[2].split('(')[0])
    if k not in runs: runs[k]=[]; order.append(k)
    runs[k].append(r)
for k in order:
    rr=sorted(runs[k],key=lambda r:float(r[1])); s=[t for r in rr for t in toks(r[4])]
    print('##',k,len(s),'signs |',rr[0][3],'...',rr[-1][5])
    for off in (0,1):
        p=[s[j]+s[j+1] for j in range(off,len(s)-1,2)]
        print('  off',off,' '.join(f'{g}:{alts(g)}' for g in p))
