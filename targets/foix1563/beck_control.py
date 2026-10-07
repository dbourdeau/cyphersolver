"""Control for Beck's proposed R9241 key (PR #18): is the decrypt more French than a key of the
same size can make out of shuffled ciphertext?  Run from the repo root:
    PYTHONUTF8=1 python targets/foix1563/beck_control.py
"""
import json, math, random, sys
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT)); sys.path.insert(0, str(ROOT / 'targets/foix1563/beck-preliminary/scripts'))
from lang import lm
from decode import load_inputs

src, key = load_inputs(ROOT / 'targets/foix1563/beck-preliminary')
passages = []
for row in src:
    if not passages or passages[-1][0] != row['passage']:
        passages.append([row['passage'], []])
    passages[-1][1].extend(u['label'] for u in row['units'])
toks = [t for _, p in passages for t in p]
types = Counter(toks)
keyed = [t for t in toks if t in key]
used = {t for t in keyed}
print(f'tokens {len(toks)}  types {len(types)}  keyed tokens {len(keyed)}  key entries {len(key)}  used entries {len(used)}')
print(f'  entries used once: {sum(1 for t in used if types[t]==1)}  nulls (empty value): {sum(1 for t in used if key[t]=="")}')

M = lm.load('fr-1600-letters', spaces=False)
def dec(seq, k):
    return lm.norm(''.join(k.get(t, '') for t in seq), spaces=False)
def score(seqs, k):
    s = ''.join(dec(q, k) for q in seqs)
    return M.per_char(s) if s else -99, len(s)

seqs = [[t for t in p if t in key] for _, p in passages]
real, n = score(seqs, key)
print(f'Beck key on real order: {real:.3f}/char over {n} chars')
ref = lm.norm(open(ROOT/'targets/foix1563/beck-preliminary/results/literal.txt', encoding='utf-8').read(), spaces=False)

rng = random.Random(1)
syms = sorted(used); vals = [key[s] for s in syms]
sh = []
for _ in range(500):
    v = vals[:]; rng.shuffle(v); sh.append(score(seqs, dict(zip(syms, v)))[0])
mu = sum(sh)/len(sh); sd = (sum((x-mu)**2 for x in sh)/len(sh))**.5
print(f'value-shuffled keys: mean {mu:.3f} sd {sd:.3f} max {max(sh):.3f}; Beck z = {(real-mu)/sd:.1f}')

# Overfitting control: hill-climb a key of the same size (values drawn from Beck's value pool,
# so multi-letter values and nulls are allowed) on token-shuffled ciphertext and on the real order.
def climb(sq, iters, seed):
    # values are a permutation of Beck's own values (swap moves), so letter frequencies and
    # word values stay fixed and the score cannot be gamed by repeating one word
    r = random.Random(seed)
    v = vals[:]; r.shuffle(v); k = dict(zip(syms, v))
    best = score(sq, k)[0]
    for i in range(iters):
        a, b = r.sample(syms, 2); k[a], k[b] = k[b], k[a]
        sc = score(sq, k)[0]
        if sc >= best: best = sc
        else: k[a], k[b] = k[b], k[a]
    return best, k
it = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
for seed in range(3):
    flat = [t for q in seqs for t in q]; r = random.Random(100+seed); r.shuffle(flat)
    b, k = climb([flat], it, seed)
    print(f'fitted key, shuffled ciphertext seed {seed}: {b:.3f}  sample: {dec(flat[:60], k)[:70]}')
b, k = climb(seqs, it, 9)
print(f'fitted key from random start, real order: {b:.3f}  sample: {dec(seqs[0][:60], k)[:70]}')

# Word-level measure: share of decrypt letters covered by corpus words of >= 5 letters (DP cover).
# Per-char LM scores are gameable by word-valued signs; long-word coverage is much harder to fake.
import re
from lang import corpora
cnt = Counter(re.findall(r'[a-z]+', lm.norm(corpora.text(['fr-henri4']), spaces=True)))
V = {w for w, c in cnt.items() if len(w) >= 5 and c >= 3}
def cover(s):
    n = len(s); best = [0]*(n+1)
    for i in range(n):
        best[i+1] = max(best[i+1], best[i])
        for L in range(5, 15):
            if i+L <= n and s[i:i+L] in V: best[i+L] = max(best[i+L], best[i]+L)
    return best[n]/max(n, 1)
real_txt = ''.join(dec(q, key) for q in seqs)
print(f'\nlong-word cover, Beck key real order: {cover(real_txt):.1%}')
for seed in range(3):
    flat = [t for q in seqs for t in q]; r = random.Random(100+seed); r.shuffle(flat)
    b, k = climb([flat], it, seed)
    print(f'long-word cover, fitted key on shuffled ciphertext seed {seed}: {cover(dec(flat, k)):.1%} (lm {b:.3f})')
    print(f'long-word cover, Beck key on same shuffled ciphertext: {cover(dec(flat, key)):.1%}')
