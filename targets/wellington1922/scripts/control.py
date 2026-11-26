"""Random-key control for key 313, as frozen in PLAN.md: mean log bigram probability per letter of each run's
decryption (Spanish bigram model with add-one smoothing over the 27-letter alphabet), averaged over the runs, for key
313 and for 1,000 random 3-digit keys (digits 0-9, random.seed(20261123)).
python scripts/control.py <spanish_corpus.txt>
The run of 23 Nov 2026 used the clear text of the Epistolario de Francisco I. Madero, t. II (INEHRM 2021, Internet
Archive item afim-epistolario-t-2, its _djvu.txt), which is not committed (all rights reserved)."""
import sys, os, math, random, unicodedata, collections
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decrypt import dec, runs, A
def fold(t):
    o = []
    for ch in t.upper():
        if ch == 'Ñ': o.append(ch); continue
        d = unicodedata.normalize('NFD', ch)[0]
        if d in A: o.append(d)
    return ''.join(o)
corpus = fold(open(sys.argv[1], encoding='utf-8').read())
B = collections.Counter(corpus[i:i+2] for i in range(len(corpus)-1)); U = collections.Counter(corpus[:-1])
def score(s): return sum(math.log((B[s[i:i+2]]+1)/(U[s[i]]+27)) for i in range(len(s)-1))/(len(s)-1)
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = [s.replace('/', '') for _, _, _, s in runs(os.path.join(here, 'transcription_DCXXI.6.588.1.txt'))]
def total(k): return sum(score(dec(r, k).replace('%', '')) for r in R) / len(R)
random.seed(20261123); keys = [[random.randint(0, 9) for _ in range(3)] for _ in range(1000)]
cs = [total(k) for k in keys]; s = total([3, 1, 3])
same = sum(k == [3, 1, 3] for k in keys)
print(f'key 313: {s:.3f}; 1,000 random keys: max {max(cs):.3f}, mean {sum(cs)/len(cs):.3f}; lower than 313: {sum(c < s for c in cs)}; draws equal to 3-1-3: {same}')
best = sorted(zip(cs, map(tuple, keys)), reverse=True)[:5]
print('best five controls:', ', '.join(f'{"".join(map(str,k))} {c:.3f}' for c, k in best))
