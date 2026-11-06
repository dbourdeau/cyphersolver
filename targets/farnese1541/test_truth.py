"""Score Klee's IA-2 key on a 2956-digit stretch of IA-2 with the vsa decoder: the control's target score."""
import sys, numpy as np, time
from vsa import *
m = lm.load('it-cinquecento', order=5, spaces=False)
K = {'5':'a','8':'e','6':'i','4':'o','1':'u','7':'n','2':'r','0':'s','3':'m','03':'l','73':'d','80':'t','57':'p',
     '27':'c','72':'b','37':'f','75':'g','07':'z','9':None}
def assign_of(K):
    a = np.full(110, -1, np.int64)
    for k, v in K.items():
        c = int(k) if len(k) == 1 else 10 + int(k)
        a[c] = -2 if v is None else m.index[v]
    return a
dig = load_cipher('ia2', 2956, int(sys.argv[1]) if len(sys.argv) > 1 else 0)
lp = m.lp.astype(np.float64)
for lb in (0, 2.5):
    t = time.time()
    sc, path = decode(dig, assign_of(K), lp, m.A, m.A**4, 8, 4.0, 12.0, lb)
    txt, segs = render(dig, assign_of(K), path, m.alpha)
    print(lb, round(sc, 1), f'{time.time()-t:.3f}s', txt[:300])
rng = np.random.default_rng(0)
a = assign_of(K); act = [c for c in range(110) if a[c] != -1]
for _ in range(3):
    b = np.full(110, -1, np.int64); perm = rng.choice(110, len(act), replace=False)
    for c, p in zip(act, perm): b[p] = a[c]
    print('random', round(decode(dig, b, lp, m.A, m.A**4, 8, 4.0, 12.0, 2.5)[0], 1))
