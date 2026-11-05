# K = WAINUT key_frozen (values unchanged) + completion from 'ok' pairs of BUILD-PAIRES.tsv (PREREG rules)
import sys, collections
sys.path.insert(0, __import__('os').path.dirname(__file__))
from common import norm, load_key
K=load_key(sys.argv[1]); frozen={g:set(v) for g,v in K.items()}
cnt=collections.defaultdict(collections.Counter)
for line in open(sys.argv[2],encoding='utf-8'):
    if line.startswith('#'): continue
    f=line.rstrip('\n').split('\t')
    if len(f)<5 or f[4]!='ok': continue
    gs=[g for g in f[2].split('.') if not (g.isdigit() and len(g)==3)]
    gl=norm(f[3])
    if len(gs)!=len(gl): print('SKIP length',f); continue
    for g,c in zip(gs,gl):
        if '?' in g: continue
        cnt[g][c]+=1
out=dict((g,set(v)) for g,v in frozen.items()); added=[]
for g,c in cnt.items():
    if g not in frozen:
        m=max(c.values()); out[g]={k for k,v in c.items() if v==m}; added.append((g,'new',dict(c)))
    else:
        for k,v in c.items():
            if k not in frozen[g] and v>=2: out[g].add(k); added.append((g,'2nd',k,v))
with open(sys.argv[3],'w',encoding='utf-8') as fo:
    fo.write('# KEY K (PREREG rakoczi-1632): WAINUT key_frozen.tsv + completion from BUILD-PAIRES.tsv (491v, 492r). group\\tvalue(s)\n')
    for g in sorted(out,key=lambda s:(not s.isdigit(), int(s) if s.isdigit() else 0, s)):
        fo.write('%s\t%s\t%s\n'%(g,'/'.join(sorted(out[g])),'frozen' if g in frozen and out[g]==frozen[g] else ('new' if g not in frozen else 'frozen+2nd')))
for a in added: print(a)
# consistency of frozen key on BUILD pairs (descriptive)
agree=tot=0
for g,c in cnt.items():
    if g in frozen:
        for k,v in c.items():
            tot+=v; agree+=v*(k in frozen[g])
print('frozen key on BUILD pairs: %d/%d = %.3f'%(agree,tot,agree/tot))
