"""LM hill-climb of R1862 key values: fixed = R1874 groups seen >=4 times with p>=.8 (unless listed in key_over.json);
free = everything else. Objective: it-cinquecento log-prob of the whole deciphered text (clear passages excluded)."""
import json,sys,os,random,collections
sys.path.insert(0,'..')
from lang import lm
from decode import lines, OVER
base=json.load(open('../r1874/key2.json'))
M=lm.load('it-cinquecento',spaces=False)
LAM=1.69  # per-letter compensation: mean -logP of real Italian, removes the length bias
L=lines()
segs=[]; cur=[]
for lab,it in L:
    for k,v in it:
        if k=='clear':
            if cur: segs.append(cur); cur=[]
        else: cur.append(v)
if cur: segs.append(cur)
allg=collections.Counter(g for s in segs for g in s)
fixed={g:v[0] for g,v in base.items() if v[2]>=4 and v[1]>=.8}
for g,v in OVER.items():
    if not g.startswith('_'): fixed[g]=v
free=[g for g in allg if g not in fixed]
cons=['','b','c','d','f','g','h','l','m','n','p','qu','r','s','t','v','z','gn','gl','st','tr','pr','ss','nt','ch','sp','sc','br','gr','cr','fr','pl']
C=sorted({c+v for c in cons for v in 'aeiou'}|set('bcdfglmnprstvz')|{'che','con','per','non','il','et','del','nel','in','di','la','le','lo','sua','suo','se','si','ave','lei','an','en','in','on','un','ar','er','or','ur','al','el','ol','nte','nti','nto','ss','ll','mente','quel','questo','quello','sse','sto','no','cardinale','imperatore','spagna','spagnoli','francia','mantova','papa','duca'})
key={g:fixed.get(g) or (base[g][0] if g in base else random.choice(C)) for g in allg}
def score(k):
    t=lm.norm(''.join(''.join(k[g] for g in s) for s in segs),'early')
    return M.per_char(t)*len(t)+LAM*len(t)
best=score(key)
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 0)
for rnd in range(6):
    changed=0
    for g in sorted(free,key=lambda g:-allg[g]):
        old=key[g]; bv,bs=old,best
        for c in C:
            key[g]=c; s=score(key)
            if s>bs: bv,bs=c,s
        key[g]=bv
        if bv!=old: changed+=1; best=bs
    print('round',rnd,'changed',changed,'score',round(best,1),file=sys.stderr)
    if not changed: break
json.dump({g:key[g] for g in free},open('climb_out.json','w'),indent=0,ensure_ascii=False)
for g in sorted(free,key=lambda g:-allg[g]): print(g,allg[g],base.get(g,['-'])[0],'->',key[g])
