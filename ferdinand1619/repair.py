"""For each flagged word, try single-token substitutions among visually confusable numbers
(the digit pairs this hand blurs) and keep the variant the LM likes much better.
Every change it proposes is listed for a check against the images."""
import os, sys, itertools, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lang import lm
from solve import parse, is_code
from decode import K, dec

# digits this hand confuses: 0/6, 3/5, 1/4, 2/7, 4/7, 5/8, plus whole-token look-alikes
CONF = {'0': '6', '6': '0', '3': '5', '5': '3', '1': '4', '4': '1', '2': '7', '7': '2', '8': '5'}

def variants(t):
    out = {t}
    for i, ch in enumerate(t):
        if ch in CONF:
            out.add(t[:i] + CONF[ch] + t[i+1:])
    return [v for v in out if v in K]

if __name__ == '__main__':
    m = lm.load('de-1500s')
    P = parse()
    fixes = []
    for lid, items in P:
        for it in items:
            if it[0] != 'word' or is_code(it[1]): continue
            w = it[1]; d = dec(w); base = m.per_char(' ' + d + ' ')
            if base >= -3.2: continue
            best = (base, None)
            for i, t in enumerate(w):
                for v in variants(t):
                    if v == t: continue
                    w2 = w[:i] + [v] + w[i+1:]
                    s = m.per_char(' ' + dec(w2) + ' ')
                    if s > best[0]: best = (s, (i, t, v, dec(w2)))
            if best[1] and best[0] - base > 0.6:
                i, t, v, d2 = best[1]
                fixes.append((lid, '.'.join(w), d, t, v, d2, round(base, 2), round(best[0], 2)))
    print(f'{len(fixes)} proposed single-token corrections\n')
    for f in fixes: print(f'{f[0]}  {f[3]}->{f[4]}   {f[2]} -> {f[5]}   ({f[6]} -> {f[7]})')
