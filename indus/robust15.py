"""Post-test check on N4 (fifteenth set; not registered): freedom from distinct lines only, so that a recurring name
cannot lower its own signs' freedom by repeating their neighbours. Also: freedom from lines that are not names at
all (texts without an ending), which no name contributes to.

Usage: python robust15.py
Writes results/robust15.md.
"""
import os
from collections import Counter
import predict_test13 as T
import predict_test15 as P
from predict_test11 import freedom
from predict_test4 import name_of
P.N = 5000
OUT = []
def say(s=''):
    OUT.append(s); print(s)
say('# Check on N4 (after the test, not registered)')
say()
for lab, L in (('A', T.sample('A')), ('B', T.sample('B'))):
    cnt = Counter(T.names(L))
    for how, src in (('distinct lines', sorted(set(map(tuple, L)))),
                     ('lines without an ending (no names)', [t for t in L if not name_of(t)])):
        fr = freedom([list(t) for t in src])
        items = []
        for (body, end), c in cnt.items():
            v = [fr[g] for g in body if g in fr and g not in T.GRAM]
            if v:
                items.append((c == 1, min(len(body), 4), sum(v) / len(v)))
        o, p = P.strat_perm(items)
        say('- %s, freedom from %s (%d lines): once minus recurring %+.3f, p = %.4f.' % (lab, how, len(src), o, p))
open(os.path.join(T.HERE, 'results', 'robust15.md'), 'w', encoding='utf-8').write('\n'.join(OUT) + '\n')
