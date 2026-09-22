"""Propose corrections for a badly-reading line: search over group re-splits of the line's digit string and
<=K digit substitutions from visually confusable pairs, score the decipherment with the Italian LM.
Usage: python fixline.py "P2 L17" [K]"""
import sys,itertools,collections
sys.path.insert(0,'..')
from lang import lm
from decode import lines,KEY
M=lm.load('it-cinquecento',spaces=False)
CONF={'1':'2','2':'1','0':'9','9':'0','7':'4','4':'7','8':'0','3':'8','5':'6','6':'5'}
lab=sys.argv[1]; K=int(sys.argv[2]) if len(sys.argv)>2 else 2
row=[it for l,it in lines() if l==lab][0]
gs=[v for k,v in row if k=='g']
digits=''.join(gs)
FORMS=[2,3,4]
def splits(s):
    out=[]
    def rec(i,acc):
        if len(out)>40000: return
        if i==len(s): out.append(tuple(acc)); return
        for L in FORMS:
            g=s[i:i+L]
            if len(g)<L: continue
            if g[0] not in '56': continue
            if g[0]=='5' and g[1] not in '13': continue
            rec(i+L,acc+[g])
    rec(0,[]); return out
def dec(gg): return ''.join(KEY.get(g,'#') for g in gg)
best=[]
base=splits(digits)
print(f'{lab}: {len(gs)} groups, {len(digits)} digits, {len(base)} splits')
cands=[(digits,0)]
for k in range(1,K+1):
    for pos in range(len(digits)):
        d=digits[pos]
        if d in CONF: cands.append((digits[:pos]+CONF[d]+digits[pos+1:],1))
for s,nsub in cands:
    for gg in splits(s):
        t=dec(gg)
        if '#' in t or len(t)<8: continue
        sc=M.per_char(lm.norm(t,'early'))-0.05*nsub
        best.append((sc,nsub,t,' '.join(gg)))
best.sort(reverse=True)
seen=set()
for sc,n,t,g in best[:12]:
    if t in seen: continue
    seen.add(t); print(f'{sc:6.2f} subs={n} {t}\n        {g}')
print('current:',dec(gs))
