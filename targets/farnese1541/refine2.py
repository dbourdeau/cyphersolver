"""Score variants of key 2 on R91: add one option to one code and report the gain in total log-prob."""
import sys, time, copy
from key1 import beam_decode, lm, lines
from key2 import K2
m = lm.load('it-cinquecento', order=5, spaces=False)
d = ''.join(t[0] for _, _, toks, _ in lines() for t in toks)
B = 24
def score(K):
    return beam_decode(d, K, m, B)[0]
t = time.time(); base = score(K2); print('base', round(base, 1), f'{time.time()-t:.0f}s')
tests = [('11', '')] + [(str(x), L) for L in 'sztdfgbhqmnplrcx' for x in range(10)]
if len(sys.argv) > 1:
    tests = [tuple(a.split('=')) for a in sys.argv[1:]]
res = []
for code, out in tests:
    K = copy.deepcopy(K2)
    if out in K.get(code, []): continue
    K.setdefault(code, []).append(out)
    g = score(K) - base
    res.append((g, code, out)); print(f'{code}={out!r:6} {g:+8.1f}', flush=True)
print(sorted(res, reverse=True)[:25])
