"""Ludendorff (w791 parts) and legation five-figure telegrams: is any additive reused, within or across telegrams?
Kappa test on whole groups and digits at every offset; a shared additive over code would raise it."""
import re, sys, collections, math, random
sys.stdout.reconfigure(encoding='utf-8')
T = {}; cur = None
for l in open(sys.argv[1] if len(sys.argv) > 1 else 'transcription_pass1.txt', encoding='utf-8'):
    if l.startswith('#'): continue
    if l.startswith('@'):
        cur = l.split()[0][1:]; T[cur] = []; continue
    T[cur] += [g for g in l.split() if re.fullmatch(r'\d{5}', g)]
ids = ['w791', 'w769', 'w716', 'w592', 'w628', 'w611']
seqs = {k: T[k] for k in ids}
def kappa(a, b, off):
    n = eq = 0
    for i, x in enumerate(a):
        j = i + off
        if 0 <= j < len(b):
            for c in range(5):
                n += 1; eq += x[c] == b[j][c]
    return eq, n
print('digit kappa at every offset, |z| >= 3.5 only (expected 0.100); many offsets tested')
tests = 0
for i, a in enumerate(ids):
    for b in ids[i:]:
        sa, sb = seqs[a], seqs[b]
        rng = range(1, len(sb)) if a == b else range(-len(sa) + 1, len(sb))
        for off in rng:
            eq, n = kappa(sa, sb, off)
            if n < 50: continue
            tests += 1
            z = (eq - .1 * n) / math.sqrt(.09 * n)
            if abs(z) >= 3.5:
                print(f'  {a} {b} off={off} n={n} kappa={eq/n:.3f} z={z:.1f}')
print('offset tests', tests, 'expected |z|>=3.5 by chance', round(tests * 0.00047, 1))
print('repeats of whole groups, within and across')
pos = collections.defaultdict(list)
for k, s in seqs.items():
    for i, g in enumerate(s): pos[g].append((k, i))
for g, p in pos.items():
    if len(p) > 1: print(' ', g, p)
n = sum(len(s) for s in seqs.values())
print('total groups', n, 'expected chance repeat pairs', round(n * (n - 1) / 2 / 100000, 2))
print('digit-difference of repeats and first-digit histogram per telegram')
for k, s in seqs.items():
    c = collections.Counter(x for g in s for x in g)
    chi = sum((c[str(d)] - 5 * len(s) / 10) ** 2 / (5 * len(s) / 10) for d in range(10))
    print(f'  {k} n={len(s)} digit chi2(9)={chi:.1f}', [c[str(d)] for d in range(10)])
print('family B / D first-digit and range')
for k in ('w749', 'w746', 'w512', 'w513', 'w643', 'w752', 'w763', 'w765', 'w735', 'w2635'):
    pass
