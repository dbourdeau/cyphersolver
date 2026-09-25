"""Three-hundred-and-nineteenth registered prediction set (PREDICTIONS.md, SM1-SM3): decipherment loop 144, tablet
referents on seals. Tablet referent units (both pools, set 312's configuration, sign units only) whose picture is an
animal also shown on seals (Elep, Rhin, Goat, Bull1, Gaur, Zebu, Buff, Tigr; Bult counted as Bull1): among seals
carrying such a unit, the share showing that animal, against the same animal's share on all pictured seals; pooled
over units, against 1,000 shuffles of the seal animals. Writes results/predict_test319.md."""
import random

import rtools as R
import referents as X
from predict_test200 import objects

ANIMALS = {'Elep', 'Rhin', 'Goat', 'Bull1', 'Gaur', 'Zebu', 'Buff', 'Tigr'}
ALIAS = {'Bult': 'Bull1'}


def tablet_units(P):
    u = {}
    for lab, (clean, both) in P.items():
        for n in (2, 3):
            for g, m in X.q_pairs(both, 2, 0.67, n).items():
                u[g] = ALIAS.get(m, m)
        for g, m in X.q_pairs(both, 3, 0.67, 1).items():
            u[g] = ALIAS.get(m, m)
    return {g: m for g, m in u.items() if m in ANIMALS}


def hits(seals, units):
    h = n = 0
    for t, m in seals:
        for g, a in units.items():
            k = len(g)
            if any(t[i:i + k] == g for i in range(len(t) - k + 1)):
                n += 1
                h += m == a
    return h, n


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Three-hundred-and-nineteenth registered predictions: decipherment loop 144, tablet referents on seals', 'predict_test319')
    P = X.pools(F, recs)
    units = tablet_units(P)
    seals = objects(F, recs, ('SEAL:S', 'SEAL:R', 'SEAL'))
    h, n = hits(seals, units)
    rnd = random.Random(319)
    texts, pics = [t for t, m in seals], [m for t, m in seals]
    null = []
    for _ in range(1000):
        rnd.shuffle(pics)
        null.append(hits(list(zip(texts, pics)), units)[0])
    p = (1 + sum(x >= h for x in null)) / 1001
    rd.say('- %d animal-labelled tablet units (%s); %d seal matches, %d showing the unit\'s animal; shuffles median %d; p = %.3f.' % (len(units), ', '.join(sorted(set(units.values()))), n, h, sorted(null)[500], p))
    rd.say()
    rd.rec('SM1', 'seals carrying a tablet referent show its animal more than chance (p < 0.05)', '%d vs median %d, p = %.3f' % (h, sorted(null)[500], p), p < 0.05)
    nb = sum(1 for g, a in units.items() if a != 'Bull1')
    rd.rec('SM2', 'at least one matched unit names an animal other than the default bull', '%d non-bull units' % nb, nb > 0 and h > 0)
    rd.rec('SM3', 'progress rule: SM1 (referents travel from tablets to seals; a new finding)', 'SM1 %s' % (p < 0.05), p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
