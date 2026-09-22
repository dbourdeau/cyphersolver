import sys,random,math
sys.path.insert(0,'..')
from lang import lm
m=lm.load('fr-1530-despatches',order=4,spaces=False)
runs=[l.strip() for l in open('runs.txt') if l.strip()]
syms=sorted(set(''.join(runs)))
letters='abcdefghilmnopqrstuxyz'
def score(k):
    return sum(m.score(''.join(k[c] for c in r)) for r in runs)
best=None
for rs in range(int(sys.argv[1]) if len(sys.argv)>1 else 6):
    random.seed(rs)
    k={c:random.choice('eaisnrtuol') for c in syms}
    s=score(k);T=3.0
    for it in range(60000):
        c=random.choice(syms);old=k[c];k[c]=random.choice(letters)
        ns=score(k)
        if ns>s or random.random()<math.exp((ns-s)/T): s=ns
        else: k[c]=old
        T=max(0.05,T*0.9998)
    print(rs,round(s,1),' '.join(''.join(k[c] for c in r) for r in runs))
    print('  ',' '.join(f'{c}={k[c]}' for c in syms))
