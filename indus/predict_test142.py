"""Hundred-and-forty-second registered prediction set (PREDICTIONS.md, LK1-LK8): line breaks as word boundaries. Every
test runs with the lines as listed and reversed. Writes results/predict_test142.md."""
import random

import predict_test13 as T
import rtools as R
from predict_test61 import units
from predict_test8 import bound_pairs
from predict_test103 import CL
from predict_test108 import genre

random.seed(162)
M = set(R.END) | set(CL) | {'400', '90'}
GOOD = ('name', 'closer', 'count', 'bare')
N = 10000


def cuts_of(lines):
    out, k = [], 0
    for ln in lines[:-1]:
        k += len(ln)
        out.append(k)
    return out


def segs(t, cuts):
    b = [0] + sorted(cuts) + [len(t)]
    return [t[b[i]:b[i + 1]] for i in range(len(b) - 1)]


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-forty-second registered predictions: line breaks as word boundaries', 'predict_test142')
    texts = sorted({tuple(tuple(ln) for ln in r['seq'] if ln) for r in F if sum(1 for ln in r['seq'] if ln) >= 2})
    U = units(sorted({b for b, _ in T.names(A + B) if len(b) >= 2}))
    BP = bound_pairs(R.FPATH)
    rd.say('- multi-line texts %d; junctions %d; units %d; bound pairs %d.' % (len(texts), sum(len(t) - 1 for t in texts), len(U), len(BP)))
    rd.say()
    stats = {
        'LK1': (lambda t, c, s: sum((t[k - 1], t[k]) in U for k in c), 'less'),
        'LK2': (lambda t, c, s: sum((t[k - 1], t[k]) in BP for k in c), 'less'),
        'LK3': (lambda t, c, s: sum(genre(x) in GOOD for x in s), 'more'),
        'LK4': (lambda t, c, s: sum(bool(x) and x[-1] in M for x in s), 'more'),
        'LK5': (lambda t, c, s: sum(t[k - 1] in R.NUMS and t[k] not in R.NUMS for k in c), 'less'),
    }
    res = {k: [] for k in stats}
    for order in ('as listed', 'reversed'):
        tx = [(sum(ls, ()), cuts_of(ls)) for ls in (t if order == 'as listed' else t[::-1] for t in texts)]
        obs = {k: sum(f(t, c, segs(t, c)) for t, c in tx) for k, (f, _) in stats.items()}
        ge = {k: 0 for k in stats}
        mean = {k: 0.0 for k in stats}
        for _ in range(N):
            draw = [(t, random.sample(range(1, len(t)), len(c))) for t, c in tx]
            for k, (f, d) in stats.items():
                v = sum(f(t, c, segs(t, c)) for t, c in draw)
                mean[k] += v / N
                ge[k] += (v <= obs[k]) if d == 'less' else (v >= obs[k])
        for k, (f, d) in stats.items():
            p = (ge[k] + 1) / (N + 1)
            ok = p < 0.05 and ((obs[k] < mean[k]) if d == 'less' else (obs[k] > mean[k]))
            res[k].append(('%s: %d against %.1f by chance, p = %.4f' % (order, obs[k], mean[k], p), ok))
    titles = {'LK1': 'junctions spare units', 'LK2': 'junctions spare bound pairs', 'LK3': 'each line is a text',
              'LK4': 'lines end in a marker', 'LK5': 'numerals stay with the next sign'}
    for k in stats:
        rd.rec(k, titles[k], [x for x, _ in res[k]], all(ok for _, ok in res[k]))
    two = [t for t in texts if len(t) == 2 and len(t[0]) + len(t[1]) >= 4]
    rd.thr('LK6', 'lines are unbalanced', 'two-line texts of 4+ signs whose lines differ by 2+', sum(abs(len(a) - len(b)) >= 2 for a, b in two), len(two), 0.5)
    rd.thr('LK7', 'a separate count line', 'texts with a numeral-only line', sum(any(all(g in R.NUMS for g in ln) for ln in t) for t in texts), len(texts), 0.2)
    isname = lambda ln: bool(T.name_of(list(ln)))
    pn = [t for t in texts if len(t) == 2 and (isname(t[0]) or isname(t[1]))]
    rd.thr('LK8', 'the lines are separate fields', 'two-line texts with a name line whose other line is not a name', sum(not (isname(t[0]) and isname(t[1])) for t in pn), len(pn), 0.7)
    rd.say('- line pairs: %s.' % '; '.join(' | '.join(' '.join(ln) for ln in t) for t in texts[:40]))
    rd.finish()


if __name__ == '__main__':
    main()
