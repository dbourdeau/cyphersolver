"""Clean held-out score: frozen cipher transcription decoded with frozen key, aligned (difflib) to interline strings; share of key-covered
cipher groups whose letter matches the aligned interline letter. 200 shuffled keys use the same pairing and alignment."""
import json, random, difflib, sys
key = {k: v for k, v in json.load(open(sys.argv[1])).items() if not k.startswith('_')}
ct = {}
for l in open(sys.argv[2]):
    if l.startswith('#') or l.startswith('seg'): continue
    s, c, sig = l.rstrip('\n').split('\t'); ct[s] = sig.split()
il = {}
for l in open(sys.argv[3]):
    if l.startswith('#') or l.startswith('seg'): continue
    s, t = l.rstrip('\n').split('\t'); il[s] = t.replace('è', 'e')
def pairs(x, k):
    best = None
    for off in (0, 1):
        p = [x[i]+x[i+1] for i in range(off, len(x)-1, 2)]
        h = sum(g in k for g in p)
        if best is None or h > best[0]: best = (h, p)
    return best[1]
def score(k, verbose=False):
    m = n = 0
    for s in il:
        p = pairs(ct[s], k); dec = ''.join(k.get(g, '#') for g in p); t = il[s]
        sm = difflib.SequenceMatcher(None, dec, t, autojunk=False)
        mm = sum(b.size for b in sm.get_matching_blocks())
        cov = sum(1 for ch in dec if ch != '#')
        m += mm; n += cov
        if verbose: print(s, dec.ljust(16), t.ljust(16), mm, '/', cov)
    return m / n, m, n
r, m, n = score(key, True)
random.seed(1); gs = list(key); vals = list(key.values()); sh = []
for _ in range(200):
    random.shuffle(vals); sh.append(score(dict(zip(gs, vals)))[0])
print(f'REAL {m}/{n} = {r:.1%}; shuffled max {max(sh):.1%}, mean {sum(sh)/len(sh):.1%}')
