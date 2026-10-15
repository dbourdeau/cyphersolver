"""Shuffled-key control for a sign-by-sign reading. The reading (letters only; word signs dropped, which is
conservative) is segmented against the lexicon of a shared lang/ model (default fr-1600-letters); then the key's letter
values are permuted at random among the signs and segmented again. Score = share of letters inside lexicon words of
>= 3 letters.
    python control_shuffle.py read_final.txt [n_shuffles] [--model fr-1600-letters] [--mincount 20]
"""
import sys, os, random, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from measure import lexicon, load, seg, A

def score(lines, LEX, tr=None):
    cov = tot = 0
    for toks in lines:
        s = ''.join(v for k, v in toks if k == 'l')
        if tr: s = s.translate(tr)
        for w in seg(s, LEX):
            n = len(w.strip('[]')); tot += n
            if not w.startswith('[') and n >= 3: cov += n
    return cov / max(1, tot)

ap = argparse.ArgumentParser(); ap.add_argument('file'); ap.add_argument('n', nargs='?', type=int, default=50)
ap.add_argument('--model', default='fr-1600-letters'); ap.add_argument('--mincount', type=int, default=20)
a = ap.parse_args()
LEX, scheme = lexicon(a.model, a.mincount)
lines = load(a.file, scheme)
print(f'real key: {score(lines, LEX):.1%} of letters in lexicon words (>= 3 letters)')
random.seed(1); sh = []
for _ in range(a.n):
    p = list(A); random.shuffle(p); sh.append(score(lines, LEX, str.maketrans(A, ''.join(p))))
sh.sort(); print(f'{a.n} shuffled keys: median {sh[a.n//2]:.1%}, max {sh[-1]:.1%}')
