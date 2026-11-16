# Mesure PREREG Holbeck — fraction des lettres du TEST décodé qui tombent dans des mots reconnus
import sys,json,re,random,itertools
key=json.load(open(sys.argv[1])); test=open(sys.argv[2]).read()
def norm(w):
    w=w.lower().replace('y','i').replace('v','u').replace('j','i')
    w=re.sub(r'(.)\1+',r'\1',w)
    if len(w)>2 and w.endswith('e'): w=w[:-1]
    return w
lex=set()
for src in ['/usr/share/dict/words','lex-supp.txt']:
    for w in open(src).read().split():
        if w.isalpha() and (len(w)>1 or w.lower() in ('a','i')): lex.add(norm(w))
toks=[w for w in re.sub(r'#.*?#',' ',test).split()]
def score(k):
    tot=ok=0
    for t in toks:
        sets=[k.get(c,['?']) for c in t]
        n=len(t); tot+=n
        cnt=1
        for s in sets: cnt*=len(s)
        good=False
        if cnt<=4096:
            for combo in itertools.product(*sets):
                if norm(''.join(combo)) in lex: good=True;break
        if good: ok+=n
    return ok/tot
real=score(key)
glyphs=sorted(key); vals=[key[g] for g in glyphs]
ctl=[]
for seed in range(200):
    r=random.Random(seed); v=vals[:]; r.shuffle(v); ctl.append(score(dict(zip(glyphs,v))))
best=max(ctl)
print(json.dumps({"test":sys.argv[2],"score":round(real,4),"best_control":round(best,4),"mean_control":round(sum(ctl)/len(ctl),4),
 "pass":real>=0.85 and real>=best+0.30},indent=1))
if len(sys.argv)>3:
    k=key
    for t in toks:
        sets=[k.get(c,['?']) for c in t]; good=False
        for combo in itertools.product(*sets):
            if norm(''.join(combo)) in lex: good=True;break
        if not good: print(t, ''.join(s[0] for s in sets))
