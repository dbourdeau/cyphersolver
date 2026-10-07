"""Shuffled-key control for the f.276 reading. The real reading (letters only; word signs dropped, which is conservative)
is segmented against the French lexicon; then the key's letter values are permuted at random (same sign stream, values
reassigned among letters) and segmented again. Score = share of letters inside lexicon words of >= 3 letters.
    python control_shuffle.py f276/read1.txt [n_shuffles]
"""
import sys, re, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from segment import seg
A = 'abcdefghilmnopqrstuxz'
def load(p):
    out = []
    for l in open(p):
        m = re.match(r'^\s*(L\d\d):\s*(.+)$', l)
        if not m or m.group(2).startswith('['): continue
        toks = []
        for t in m.group(2).split():
            if t.startswith('=') or t == '###' or t.startswith('['): continue
            v = t.split('/')[0].replace('?', '')
            if len(v) >= 1 and all(c in A + 'y' for c in v): toks.append(v.replace('y', 'i'))
        out.append(''.join(toks))
    return out
def score(lines):
    cov = tot = 0
    for s in lines:
        _, words = seg(s)
        for w in words:
            tot += len(w.strip('[]'))
            if not w.startswith('[') and len(w) >= 3: cov += len(w)
    return cov / tot
lines = load(sys.argv[1]); n = int(sys.argv[2]) if len(sys.argv) > 2 else 50
real = score(lines); print(f'real key: {real:.1%} of letters in lexicon words (>=3 letters)')
random.seed(1); sh = []
for _ in range(n):
    p = list(A); random.shuffle(p); tr = str.maketrans(A, ''.join(p))
    sh.append(score([s.translate(tr) for s in lines]))
sh.sort(); print(f'{n} shuffled keys: median {sh[n//2]:.1%}, max {sh[-1]:.1%}')
