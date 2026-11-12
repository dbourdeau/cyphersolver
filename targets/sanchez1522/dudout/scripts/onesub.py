"""onesub.py FLAGS SIGNS KEY : for each flagged word, the single-sign substitutions (sign label -> letter) that let it be
spelled by a contiguous run of whole tokens of its line (+ previous line for split words)."""
import sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from autotag import load, norm
from decode_lot3 import SIGN, NULLS
K, Q = load(sys.argv[3]); P = {}; order = []
for line in open(sys.argv[2], encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    f = line.split(); P[f[0]] = f[1:]; order.append(f[0])
def toks(ref):
    out = []
    for t in P.get(ref, []):
        t0 = t.rstrip('?').lstrip('^')
        if t0 in NULLS or t0 == '|': continue
        if t0.startswith('=') or t0.startswith('['): out.append((None, None)); continue
        if t0 in SIGN: out.append((t0, [norm(x) for x in SIGN[t0].strip('()').split('|')])); continue
        out.append((t0, K.get(t0)))
    return out
def spell(w, T, sub):
    def rec(j, r):
        if not r: return True
        if j >= len(T) or T[j][1] is None and j != sub: return False
        lab, opts = T[j]
        if j == sub:
            return lab in SIGN and len(r) >= 1 and rec(j + 1, r[1:]) and r[0]
        return any(o and r.startswith(o) and rec(j + 1, r[len(o):]) for o in opts)
    return any(rec(i, w) for i in range(len(T)))
for line in open(sys.argv[1]):
    if not line.startswith('FLAG'): continue
    _, ref, w = line.split()[:3]; w0 = norm(w)
    i = order.index(ref) if ref in order else -1
    T = (toks(order[i-1]) if i > 0 else []) + toks(ref)
    hits = set()
    for s in range(len(T)):
        if T[s][0] in SIGN:
            def rec2(j, r, used):
                if not r: return used
                if j >= len(T): return None
                lab, opts = T[j]
                if opts is None: return None
                res = None
                for o in opts:
                    if o and r.startswith(o):
                        res = rec2(j + 1, r[len(o):], used)
                        if res: return res
                if j == s and r:
                    return rec2(j + 1, r[1:], (lab, r[0]))
                return None
            for st in range(len(T)):
                u = rec2(st, w0, None)
                if u: hits.add('%s->%s' % u)
    print(ref, w, ' '.join(sorted(hits)) or 'NONE')
