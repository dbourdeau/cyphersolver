"""Control: encrypt period English with a random homophonic key of the same shape as R8499, then solve."""
import os, sys, random, json, collections
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
import solve

HERE = os.path.dirname(os.path.abspath(__file__))


def make(seed=0, n=3200, nsigns=150, noise=0.0):
    rng = random.Random(seed)
    txt = open(os.path.join(HERE, '..', 'lang', 'corpora', 'en-1640s-history.txt'), encoding='utf8', errors='replace').read()
    start = rng.randrange(len(txt) - 20000)
    pt = lm.norm(txt[start:start + 20000], 'early', spaces=False)[:n]
    freq = collections.Counter(pt)
    letters = sorted(freq, key=lambda c: -freq[c])
    # homophones proportional to frequency, at least 1
    alloc = {c: 1 for c in letters}
    left = nsigns - len(letters)
    while left > 0:
        c = max(letters, key=lambda c: freq[c] / alloc[c]); alloc[c] += 1; left -= 1
    signs = {}
    k = 0
    for c in letters:
        signs[c] = [f's{k + i}' for i in range(alloc[c])]; k += alloc[c]
    allsigns = [s for v in signs.values() for s in v]
    ct = []
    for ch in pt:
        s = rng.choice(signs[ch])
        if noise and rng.random() < noise:
            s = rng.choice(allsigns)
        ct.append(s)
    lines = [' '.join(ct[i:i + 30]) for i in range(0, len(ct), 30)]
    path = os.path.join(HERE, f'control_{seed}.txt')
    open(path, 'w', encoding='utf8').write('\n'.join(f'p0.{i:02d} {l}' for i, l in enumerate(lines)) + '\n')
    return path, pt


if __name__ == '__main__':
    seed = int(sys.argv[1]); it = int(sys.argv[2]); noise = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
    path, pt = make(seed, noise=noise)
    orig = solve.runs
    solve.runs = lambda: orig(path)
    s, key, txt = solve.main(seed, it)
    got = txt.replace(' ', '')
    acc = sum(a == b for a, b in zip(got, pt)) / len(pt)
    print('acc', round(acc, 3)); print(got[:300]); print(pt[:300])
