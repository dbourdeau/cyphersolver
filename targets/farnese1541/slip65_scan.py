"""Fourth pass (slips) helper for 65r: list one-slip dictionary words of 5+ letters that fall inside unread stretches.

  python slip65_scan.py [reading_65r.txt] [minlen]

Aligns the reading with align91, takes every maximal run of unread digits, and lists, per run, the dictionary words
(wordfit's lattice with slips=1) that lie inside the run (one digit of slack either side) and need one wrong digit.
Exact words (no slip) of 5+ letters are listed too, marked '=', for comparison.
"""
import sys, os
import align91, vdot, k2d, probe, wordfit

path = sys.argv[1] if len(sys.argv) > 1 else 'reading_65r.txt'
minlen = int(sys.argv[2]) if len(sys.argv) > 2 else 5
items = align91.parse_reading(path)
D = vdot.Dec(only=set(it[-1] for it in items))
key = {k: list(v) for k, v in k2d.KEY.items()}
pth, info = align91.align(items, key, D)
flat = [t for _, ts, _ in D.S for t in ts]
unread = [False] * len(flat)
for pi, i, pj, j, inf in pth:
    if inf[0] == 'U':
        for q in range(pi, i):
            unread[q] = True
off = probe.span('65r.1')[0]
runs = []
q = 0
while q < len(flat):
    if unread[q]:
        r = q
        while r < len(flat) and unread[r]:
            r += 1
        runs.append((q, r))
        q = r
    else:
        q += 1
W = wordfit.load_words()
T = wordfit.trie_of(W)
for a, b in runs:
    i0, i1 = off + a, off + b
    t0, t1 = probe.FLAT[i0], probe.FLAT[i1 - 1]
    digs = ' '.join(probe.tok(t) for t in probe.FLAT[i0:i1])
    print(f'== {t0[0]}:{t0[1]}-{t1[0]}:{t1[1]}  {digs}')
    F = wordfit.fits(max(0, i0 - 1), min(len(probe.FLAT), i1 + 1), T, W, 1)
    out = []
    for s, e, w, sc, p in F:
        if len(w) < minlen or w not in W:
            continue
        bad = [x for x in p if x.endswith('!')]
        st = probe.FLAT[s]
        out.append((-(len(w)), -sc, f"  {'!' if bad else '='} {st[0]}:{st[1]:<3} {w:14} {' '.join(p)}"))
    for o in sorted(out)[:30]:
        print(o[2])
