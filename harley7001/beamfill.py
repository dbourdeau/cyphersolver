# Constrained search for the code groups blank on the Windebank key (R9115).
# Candidates: every word of the en-1640s-history corpus (freq >= 3) lying alphabetically between the nearest
# lower and upper code groups whose value is on the key. Each candidate is scored by the en-1640s LM in the full
# decoded context (length-normalised by comparing against the same sentence), best 5 printed per group.
import re, collections, sys
sys.path.insert(0, '.')
from lang import lm
sys.path.insert(0, 'harley7001')
from key import K
M = lm.load('en-1640s')
words = collections.Counter(re.findall(r"[a-z]+", open('lang/corpora/en-1640s-history.txt', encoding='utf8').read().lower()))
vocab = [w for w, n in words.items() if n >= 3]
# key values actually on the sheet (not rebuilt here): codes >= 100 with single-word values
REBUILT = {'100', '275', '437', '524', '562', '573', '660', '153'}
known = sorted((int(k), v.lower().split()[0]) for k, v in K.items() if k.isdigit() and int(k) >= 100 and k not in REBUILT)
toks = [x for l in open('harley7001/ct.txt') if l[:2] in ('A:', 'B:') for x in l[2:].split()]
sig = [x for x in toks if K.get(x) != '·']
gaps = ['90', '160', '319', '359', '444', '452', '455', '487', '539', '650', '673', '718']
def text(fill):
    return ' '.join(fill.get(i, K.get(x, 'x')) for i, x in enumerate(sig))
def sc(t): return M.score(M.norm(t) if hasattr(M, 'norm') else lm.norm(t))
for g in gaps:
    n = int(g)
    lo = max((c, w) for c, w in known if c < n) if n > 100 else None
    hi = min(((c, w) for c, w in known if c > n), default=None)
    cand = [w for w in vocab if (lo is None or w > lo[1]) and (hi is None or w < hi[1])] if n >= 100 else vocab
    if len(cand) > 4000: cand = sorted(cand, key=lambda w: -words[w])[:4000]
    for i, x in enumerate(sig):
        if x == g:
            a, b = max(0, i - 8), min(len(sig), i + 8)
            ctx = [K.get(y, '@' if j == i else 'x') for j, y in enumerate(sig[a:b], a)]
            base = ' '.join(ctx)
            r = sorted(((sc(base.replace('@', w)) + 0.0 * len(w), w) for w in cand), reverse=True)[:5]
            print(g, 'bracket', lo, hi, len(cand), 'cands |', ' '.join(f'{w}({s:.0f})' for s, w in r))
            break
