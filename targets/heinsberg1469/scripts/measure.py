# One measure on H (letter 2), PREREG.md section 5. Usage: python3 -I scripts/measure.py KEY.tsv LEX.txt
import sys,random
sys.path.insert(0,'scripts')
from norm import load,words
K=dict(l.rstrip('\n').split('\t') for l in open(sys.argv[1]) if '\t' in l and not l.startswith('#'))
LEX=set(w.strip() for w in open(sys.argv[2]) if w.strip() and not w.startswith('#'))
def nm(w): return w.lower().replace('v','u').replace('j','i').replace('y','i')
LEXn=set(nm(w) for w in LEX)
def dec(w,k): return ''.join(k.get(c,'#') for c in w)
def S(W,k):
    tot=hit=0
    for w in W:
        d=dec(w,k); tot+=len(d)
        if '#' not in d and nm(d) in LEXn: hit+=len(d)
    return hit/tot
signs=sorted(K); vals=[K[s] for s in signs]
for p in 'AB':
    W=words(load(f'transcription/TRANSCRIPTION-{p}.txt',p,'L2'))
    s=S(W,K); ctr=[]
    for seed in range(1,201):
        r=random.Random(seed); v=vals[:]; r.shuffle(v); ctr.append(S(W,dict(zip(signs,v))))
    print(f'H-pass{p}: words={len(W)} S={s:.4f} max_control={max(ctr):.4f} mean_control={sum(ctr)/len(ctr):.4f}')
