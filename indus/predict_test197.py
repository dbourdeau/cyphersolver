"""Hundred-and-ninety-seventh registered prediction set (PREDICTIONS.md, DN1-DN5): decipherment loop 22, Indus name
structure against the candidates (Tamil-Brahmi, Prakrit), typology-matched decoys (Japanese, Turkish) and controls
(Ur III Sumerian, Linear B). Writes results/predict_test197.md."""
import math
import random
from collections import Counter

import lang_names as L
import rtools as R
from predict_test165 import jsd
from predict_test171 import lens
from predict_test173 import aks, ratio
from predict_test174 import taks


def measures(names, n, rnd_seed=0):
    random.seed(rnd_seed)
    r = ratio(names, n)
    ln = lens(names)
    long3 = [a for a in names if len(a) >= 3]
    head = sum(v for k, v in Counter(a[-2:] for a in long3).most_common(10)) / max(1, len(long3))
    dom = Counter(a[-1] for a in names).most_common(1)[0][1] / len(names)
    return r, ln, head, dom


def indus_measures(full, n, seed=0):
    random.seed(seed)
    bodies = [x[:-1] for x in full if len(x) >= 3]
    r = ratio(bodies, n)
    head = sum(v for k, v in Counter(b[-1] for b in bodies).most_common(10)) / len(bodies)
    dom = Counter(x[-1] for x in full).most_common(1)[0][1] / len(full)
    return r, lens(bodies), head, dom


def rank(ind, langs):
    d = {}
    for k, (r, ln, head, dom) in langs.items():
        d[k] = (abs(math.log(r / ind[0])), jsd(ln, ind[1]), abs(head - ind[2]), abs(dom - ind[3]))
    ranks = {k: 0.0 for k in d}
    for j in range(4):
        for i, k in enumerate(sorted(d, key=lambda k: d[k][j])):
            ranks[k] += (i + 1) / 4
    return sorted(ranks, key=ranks.get), ranks, d


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-ninety-seventh registered predictions: decipherment loop 22, name structure against typology-matched decoys', 'predict_test197')
    full = L.indus(F)
    owners, fathers = L.sum_names()
    C = {'Tamil-Brahmi': [a for a in (taks(last) for f, last, fem in L.tb_names()) if len(a) >= 2],
         'Prakrit': [a for a in sorted({aks(nm) for nm, s, f in L.pra_luders()}) if len(a) >= 2],
         'Japanese': [m for m, fem in L.jp_names() if len(m) >= 2],
         'Turkish': [s for s, fem in L.tr_names() if len(s) >= 2],
         'Ur III Sumerian': [s for cf, s in owners if len(s) >= 2 and 'x' not in s],
         'Linear B': [x for x in L.linb() if len(x) >= 2]}
    n = min([len(v) for v in C.values()] + [len([x for x in full if len(x) >= 3]) // 2])
    rd.say('- names: %s; Indus %d (bodies of 2+ signs %d); rarefied to %d.' % (', '.join('%s %d' % (k, len(v)) for k, v in C.items()), len(full), sum(len(x) >= 3 for x in full), n))
    langs = {k: measures(v, n) for k, v in C.items()}
    ind = indus_measures(full, n)
    order, ranks, d = rank(ind, langs)
    rd.say('- Indus: R %.2f, head share %.2f, dominant ending %.2f.' % (ind[0], ind[2], ind[3]))
    for k in order:
        r, ln, head, dom = langs[k]
        rd.say('- %s: mean rank %.2f; R %.2f, head share %.2f, dominant final %.2f; distances %s.' % (k, ranks[k], r, head, dom, ', '.join('%.3f' % x for x in d[k])))
    rd.say()
    cand, dec, ctl = ('Tamil-Brahmi', 'Prakrit'), ('Japanese', 'Turkish'), ('Ur III Sumerian', 'Linear B')
    rd.rec('DN1', 'the nearest language is a candidate', 'order: %s' % ', '.join(order), order[0] in cand)
    pos = {k: i for i, k in enumerate(order)}
    rd.rec('DN2', 'both candidates nearer than both decoys', 'positions %s' % {k: pos[k] + 1 for k in cand + dec}, max(pos[k] for k in cand) < min(pos[k] for k in dec))
    rd.rec('DN3', 'both controls below both candidates', 'positions %s' % {k: pos[k] + 1 for k in cand + ctl}, max(pos[k] for k in cand) < min(pos[k] for k in ctl))
    rnd = random.Random(197)
    fl = sorted(set(full))
    rnd.shuffle(fl)
    h = len(fl) // 2
    firsts = []
    for half in (fl[:h], fl[h:]):
        o, rk, _ = rank(indus_measures(half, n), langs)
        firsts.append(o[0])
        rd.say('- half: order %s.' % ', '.join(o))
    rd.rec('DN4', 'the same nearest language in both halves', 'nearest: %s' % ', '.join(firsts), firsts[0] == firsts[1])
    rd.rec('DN5', 'progress rule', 'DN1 %s, DN4 %s' % (order[0] in cand, firsts[0] == firsts[1]), order[0] in cand and firsts[0] == firsts[1])
    rd.finish()


if __name__ == '__main__':
    main()
