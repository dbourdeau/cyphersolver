"""Hundred-and-eighty-sixth registered prediction set (PREDICTIONS.md, JV1-JV8): decipherment loop 11, the strokes inside
the jar (740 plain; 741, 742, 745 with one, two, three strokes). Writes results/predict_test186.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from signs import load

random.seed(255)
STROKED = ('741', '742', '745')


def final(t, i):
    return all(g in ('400', '90') for g in t[i + 1:])


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-eighty-sixth registered predictions: decipherment loop 11, the strokes inside the jar', 'predict_test186')
    DA = sorted({tuple(t) for t in A})
    DB = sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})
    tok = lambda D, S: [(t, i) for t in D for i, g in enumerate(t) if g in S]
    rd.ltl('JV1', 'stroked jars are final less often (A)', 'final, stroked', [final(t, i) for t, i in tok(DA, STROKED)], [final(t, i) for t, i in tok(DA, ('740',))])
    b1 = [final(t, i) for t, i in tok(DB, STROKED)]
    b0 = [final(t, i) for t, i in tok(DB, ('740',))]
    rd.ltl('JV2', 'on B', 'final, stroked (B)', b1, b0)
    DAB = DA + DB
    nx = lambda t, i: i + 1 < len(t) and t[i + 1] in R.END
    s_n = [nx(t, i) for t, i in tok(DAB, STROKED)]
    p_n = [nx(t, i) for t, i in tok(DAB, ('740',))]
    rd.gtl('JV3', 'a stroked jar can take the ending', 'followed by 740 / 520, stroked', s_n, p_n)
    pv = lambda t, i: i > 0 and t[i - 1] in R.NUMS
    rd.ltl('JV4', 'the inner strokes do the counting', 'preceded by a numeral, stroked', [pv(t, i) for t, i in tok(DAB, STROKED)], [pv(t, i) for t, i in tok(DAB, ('740',))])
    shares = []
    for g in ('740', '741', '742', '745'):
        xs = [final(t, i) for t, i in tok(DAB, (g,))]
        shares.append(sum(xs) / max(1, len(xs)))
    rho = T.spearman([0, 1, 2, 3], shares)
    rd.rec('JV5', 'the strokes are graded', 'share final by strokes 0-3: %s; Spearman %.2f' % (', '.join('%.2f' % s for s in shares), rho), abs(rho) == 1)
    seals = Counter(g for r in F if r['type'].startswith('SEAL') for g in r['flat'])
    tabs = Counter(g for r in F if r['type'].startswith('TAB') for g in r['flat'])
    a = sum(tabs[g] for g in STROKED)
    b = sum(seals[g] for g in STROKED)
    rd.gt('JV6', 'stroked jars favour tablets', 'on tablets, stroked jars', a, a + b, tabs['740'], tabs['740'] + seals['740'])
    fr = defaultdict(Counter)
    for t in DAB:
        s = ('#',) + t + ('#',)
        for i in range(1, len(s) - 1):
            fr[s[i]][(s[i - 1], s[i + 1])] += 1
        for i in range(1, len(s) - 2):
            if s[i] == '740' and s[i + 1] == '1':
                fr['740+1'][(s[i - 1], s[i + 2])] += 1

    def ov(a, b):
        A_, B_ = fr[a], fr[b]
        inter = sum(min(A_[k], B_[k]) for k in A_)
        return inter / max(1, min(sum(A_.values()), sum(B_.values())))
    obs = ov('741', '740+1')
    tc = Counter(g for t in DAB for g in t)
    n1 = sum(fr['740+1'].values())
    cands = [g for g in tc if abs(tc[g] - n1) <= max(5, n1) and g not in ('741', '740')]
    rnd = [ov(random.choice(cands), '740+1') for _ in range(500)] if cands else [0]
    q = sum(x >= obs for x in rnd)
    rd.rec('JV7', 'the stroke inside = a stroke after', "frame overlap of 741 with '740 1' %.2f ('740 1' in %d frames); random signs %d of 500 as high" % (obs, n1, q), q < 25)
    jv1 = sum(final(t, i) for t, i in tok(DA, STROKED)) / max(1, len(tok(DA, STROKED))) < sum(final(t, i) for t, i in tok(DA, ('740',))) / max(1, len(tok(DA, ('740',))))
    jv2 = sum(b1) / max(1, len(b1)) < sum(b0) / max(1, len(b0))
    rd.rec('JV8', 'the progress rule', 'JV1 direction A %s, B %s' % (jv1, jv2), jv1 and jv2)
    rd.finish()


if __name__ == '__main__':
    main()
