"""Swap-annealing substitution solver for R731 (R731_signs.txt), validated first on a control: Pápai's own
deciphered Hungarian, cut to the same line lengths and enciphered with a random key."""
import re, glob, math, random, collections, sys, unicodedata
from pathlib import Path
R = Path(__file__).resolve().parent
P = R.parent / 'papai1706'   # training text: Papai's deciphered letters (split 14 Oct 2026; they stay in papai1706)
def clean(t):
    t = unicodedata.normalize('NFD', t.lower()); return ''.join(c for c in t if 'a' <= c <= 'z')
corp = ''
for f in sorted(glob.glob(str(P/'*read.txt'))):
    for l in open(f, encoding='utf-8'):
        if not l.startswith(('#', '=')): corp += clean(re.sub(r'\[[^\]]*\]|[{}]', '', l))
N = 4
cnt = collections.Counter(corp[i:i+N] for i in range(len(corp)-N+1)); tot = sum(cnt.values())
A = sorted(set(corp)); floor = math.log(0.5/tot)
LP = {g: math.log(c/tot) for g, c in cnt.items()}
def score(segs, k):
    s = 0.0
    for seg in segs:
        t = ''.join(k[c] for c in seg)
        for i in range(len(t)-N+1): s += LP.get(t[i:i+N], floor)
    return s
def solve(segs, restarts=20, iters=30000, seed=0):
    rnd = random.Random(seed); signs = sorted(set(''.join(segs)))
    cf = [c for c, _ in collections.Counter(''.join(segs)).most_common()]
    lf = [c for c, _ in collections.Counter(corp).most_common()]
    best = (-1e18, None)
    for r in range(restarts):
        pool = lf[:]; key = {}
        for i, c in enumerate(cf): key[c] = pool[i] if r == 0 else None
        if r: 
            rnd.shuffle(pool); key = dict(zip(cf, pool))
        spare = [l for l in A if l not in key.values()]
        cur = score(segs, key); T0 = 10.0
        for it in range(iters):
            T = T0*(1-it/iters)+0.2; a = rnd.choice(signs)
            if spare and rnd.random() < 0.3:
                j = rnd.randrange(len(spare)); old = key[a]; key[a] = spare[j]; spare[j] = old
                new = score(segs, key)
                if new >= cur or rnd.random() < math.exp((new-cur)/T): cur = new
                else: spare[j] = key[a]; key[a] = old
            else:
                b = rnd.choice(signs); key[a], key[b] = key[b], key[a]; new = score(segs, key)
                if new >= cur or rnd.random() < math.exp((new-cur)/T): cur = new
                else: key[a], key[b] = key[b], key[a]
        if cur > best[0]: best = (cur, dict(key))
    n = sum(max(0, len(s)-N+1) for s in segs)
    return best[0]/n, best[1], ' | '.join(''.join(best[1][c] for c in s) for s in segs)
def sign_lines():
    out = []
    for l in open(R/'R731_signs.txt', encoding='utf-8'):
        l = re.sub(r'\[.*?\]', '', l).strip()
        if l and not l.startswith(('#', 'P1', 'P2', 'P3')): out.append(l)
    return out
if __name__ == '__main__':
    base = sign_lines(); rnd = random.Random(7)
    pos = 5000; ctl = []
    for l in base:
        n = len(l.replace(':', '')); ctl.append(corp[pos:pos+n]); pos += n+40
    # control with the cipher's sign budget: letters beyond 16 distinct collapse (homophone-free, many-to-one)
    perm = dict(zip(A, rnd.sample(A, len(A))))
    c = solve([''.join(perm[x] for x in s) for s in ctl], restarts=10)
    print('CONTROL per-4gram', round(c[0], 2)); print('  got ', c[2][:240]); print('  true', ' | '.join(ctl)[:240])
    t = [corp[i:i+N] for i in range(0, 20000)]
    print('real-text per-4gram', round(sum(LP.get(g, floor) for g in t)/len(t), 2))
    for name, f in [('as read', lambda s: s), ('no dots', lambda s: s.replace(':', '')), ('no dots, no a', lambda s: s.replace(':', '').replace('a', '')),
                    ('reversed, no dots', lambda s: s[::-1].replace(':', ''))]:
        segs = [x for x in (f(s) for s in base) if x]
        r = solve(segs, restarts=10); print(name, round(r[0], 2)); print('  ', r[2][:400])
