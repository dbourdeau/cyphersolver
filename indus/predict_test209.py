"""Two-hundred-and-ninth registered prediction set (PREDICTIONS.md, RL1-RL5): decipherment loop 34, do closer-line bodies
behave as name bodies (head before the closer, modifiers before it)? Writes results/predict_test209.md."""
import random
from collections import Counter

import rtools as R
from predict_test103 import CL
from predict_test108 import genre
from predict_test7 import fisher_less
from signs import load


def closer_bodies(lines):
    out = []
    for t in lines:
        if genre(t) != 'closer':
            continue
        k = max((i for i, g in enumerate(t) if g in CL), default=None)
        if k is None or k == 0:
            continue
        body = [g for g in t[:k] if g not in R.NUMS]
        if body:
            out.append(body)
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Two-hundred-and-ninth registered predictions: decipherment loop 34, roles in closer lines', 'predict_test209')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln} - set(DA))
    heads = {t[i - 1] for t in DA for i, g in enumerate(t) if g in R.END and i > 0}
    mods = set()
    for t in DA:
        nm = R.name_of(list(t))
        if nm and nm[0]:
            mods |= set(nm[0][:-1])
    ca, cb = closer_bodies(DA), closer_bodies(DB)
    rd.say('- closer-line bodies: A %d, B %d; known heads %d, known modifiers %d.' % (len(ca), len(cb), len(heads), len(mods)))
    rd.say()

    def test(key, title, bodies):
        last = [b[-1] in heads for b in bodies]
        other = [g in heads for b in bodies for g in b[:-1]]
        p = fisher_less(sum(other), len(other) - sum(other), sum(last), len(last) - sum(last))
        ok = p < 0.05 and sum(last) / max(1, len(last)) > sum(other) / max(1, len(other))
        rd.rec(key, title, 'last body sign a known head %d of %d (%.0f%%) against other body signs %d of %d (%.0f%%); p = %.4f' % (
            sum(last), len(last), 100 * sum(last) / max(1, len(last)), sum(other), len(other), 100 * sum(other) / max(1, len(other)), p), ok)
        return ok
    r1 = test('RL1', 'the sign before a closer is a name head (A)', ca)
    r2 = test('RL2', 'and in B', cb)
    endh = [t[i - 1] in heads for t in DB for i, g in enumerate(t) if g in R.END and i > 0]
    ch = [b[-1] in heads for b in cb]
    a, e = sum(ch) / max(1, len(ch)), sum(endh) / max(1, len(endh))
    rd.rec('RL3', 'at least half as often as before 740 / 520 (B)', 'before a closer %.0f%%, before 740 / 520 %.0f%%' % (100 * a, 100 * e), a >= e / 2)
    tok = Counter(g for t in DA + DB for g in t)
    ranked = sorted(tok, key=tok.get)
    band = {g: ranked[max(0, i - 10):i + 11] for i, g in enumerate(ranked)}
    obs = [g for b in cb for g in b[:-1]]
    rate = sum(g in mods for g in obs) / max(1, len(obs))
    rnd = random.Random(209)
    ge = 0
    for _ in range(1000):
        ge += sum(rnd.choice(band[g]) in mods for g in obs) / max(1, len(obs)) >= rate
    rd.rec('RL4', 'earlier body signs are known modifiers (B)', '%d of %d (%.0f%%); frequency-matched draws as high %d of 1000' % (sum(g in mods for g in obs), len(obs), 100 * rate, ge), ge < 50)
    rd.rec('RL5', 'progress rule', 'RL1 %s, RL2 %s' % (r1, r2), r1 and r2)
    rd.finish()


if __name__ == '__main__':
    main()
