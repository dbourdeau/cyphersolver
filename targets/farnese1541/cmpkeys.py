"""Compare key variants on R91 by LM score (length-neutral) and dictionary word coverage."""
import sys, json, copy
import vpoly, k2cur, importlib, os
from wordcov91 import coverage
M = vpoly.Model(B=48, lbonus=1.3, nullpen=4)
base = {k: list(v) for k, v in importlib.import_module(os.environ.get("BASEKEY", "k2cur")).KEY.items()}
def ev(key, name):
    s, out = M.text(key, B=48)
    t = ''.join(o for _, o in out)
    cov, seg = coverage(t)
    print(f'{name:28} score {s:8.1f}  cov3 {cov:.3f}  cov4 {coverage(t, 4)[0]:.3f}  len {len(t)}')
    return cov, seg
if __name__ == '__main__':
    ev(base, 'k2cur')
    for v in sys.argv[1:]:
        k = copy.deepcopy(base)
        for ch in v.split(','):
            op, rest = ch[0], ch[1:]
            c, o = rest.split('=')
            if op == '+': k.setdefault(c, []).append(o)
            elif op == '-': k[c] = [x for x in k.get(c, []) if x != o]
            elif op == '=': k[c] = o.split('|') if o else []
        ev(k, v)
