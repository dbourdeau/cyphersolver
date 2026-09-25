"""Two-hundred-and-nineteenth registered prediction set (PREDICTIONS.md, AF1-AF4): decipherment loop 44, is the tail after
a count's counted sign a name (last sign a known head, the rest modifiers)? Writes results/predict_test219.md."""
import random
from collections import Counter

import rtools as R
from predict_test108 import genre
from signs import load


def tails(lines):
    out = []
    for t in lines:
        if genre(t) != 'count':
            continue
        i = next((i for i, g in enumerate(t) if g in R.NUMS), None)
        if i is None:
            continue
        j = i
        while j < len(t) and t[j] in R.NUMS:
            j += 1
        tail = [g for g in t[j + 1:] if g not in R.NUMS]
        if len(tail) >= 2:
            out.append(tail)
    return out


def test(obs, pool, band, rnd, n=1000):
    rate = sum(g in pool for g in obs) / max(1, len(obs))
    ge = sum(sum(rnd.choice(band[g]) in pool for g in obs) / max(1, len(obs)) >= rate for _ in range(n))
    return rate, (ge + 1) / (n + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-nineteenth registered predictions: decipherment loop 44, what follows a count', 'predict_test219')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    heads = {t[i - 1] for t in DA for i, g in enumerate(t) if g in R.END and i > 0}
    mods = set()
    for t in DA:
        nm = R.name_of(list(t))
        if nm and nm[0]:
            mods |= set(nm[0][:-1])
    tok = Counter(g for t in DA + DB for g in t)
    ranked = sorted(tok, key=tok.get)
    band = {g: ranked[max(0, i - 10):i + 11] for i, g in enumerate(ranked)}
    ta, tb = tails(DA), tails(DB)
    rd.say('- tails of 2+ signs after the counted sign: A %d, B %d.' % (len(ta), len(tb)))
    rd.say()
    ra, pa = test([x[-1] for x in ta], heads, band, random.Random(219))
    rd.rec('AF1', 'the tail ends in a name head (A)', 'known head %.0f%% of %d; frequency-matched p = %.4f' % (100 * ra, len(ta), pa), pa < 0.05)
    rb, pb = test([x[-1] for x in tb], heads, band, random.Random(220))
    rd.rec('AF2', 'and in B', 'known head %.0f%% of %d; p = %.4f' % (100 * rb, len(tb), pb), pb < 0.05)
    rm, pm = test([g for x in tb for g in x[:-1]], mods, band, random.Random(221))
    rd.rec('AF3', 'the rest are name modifiers (B)', 'known modifier %.0f%%; p = %.4f' % (100 * rm, pm), pm < 0.05)
    rd.rec('AF4', 'progress rule', 'AF1 %s, AF2 %s' % (pa < 0.05, pb < 0.05), pa < 0.05 and pb < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
