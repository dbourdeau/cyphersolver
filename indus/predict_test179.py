"""Hundred-and-seventy-ninth registered prediction set (PREDICTIONS.md, SP1-SP7): decipherment loop 4, sound values from
substitution. Substitutable signs (minimal pairs of names) should sound alike under a correct key; Linear B as the
control with a known answer. Writes results/predict_test179.md."""
import csv
import os
import random
from collections import Counter, defaultdict

import bench
import predict_test13 as T
import rtools as R
from predict_test103 import CL
from predict_test152 import LINB
from signs import load

random.seed(199)
YAJ = os.environ.get('YAJ', 'C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher--claude-worktrees-florence-1414-'
                     'cipher-160632/03a95ee0-e290-45c7-bab7-1e38cbd68d34/scratchpad/yaj/xlits.csv')
M = set(R.END) | set(CL) | {'400', '90'}


def lev(a, b):
    d = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, cb in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (ca != cb))
    return d[-1]


def sim(x, y):
    a, b = bench.skelv(x), bench.skelv(y)
    if not a and not b:
        return 1.0
    return 1 - lev(a, b) / max(len(a), len(b), 1)


def subst_pairs(bodies, ok):
    byl = defaultdict(list)
    for b in bodies:
        byl[len(b)].append(b)
    pairs = Counter()
    for L, bs in byl.items():
        for i in range(L):
            grp = defaultdict(set)
            for b in bs:
                grp[b[:i] + b[i + 1:]].add(b[i])
            for vs in grp.values():
                vs = sorted(v for v in vs if ok(v))
                for x in range(len(vs)):
                    for y in range(x + 1, len(vs)):
                        pairs[(vs[x], vs[y])] += 1
    return pairs


def test(pairs, key, n=1000):
    ps = {p: w for p, w in pairs.items() if p[0] in key and p[1] in key}
    if not ps:
        return None, None, 0, 0
    tot = sum(ps.values())
    stat = lambda k: sum(w * sim(k[a], k[b]) for (a, b), w in ps.items()) / tot
    obs = stat(key)
    signs = sorted({s for p in ps for s in p})
    vals = [key[s] for s in signs]
    ge = 0
    mean = 0.0
    for _ in range(n):
        random.shuffle(vals)
        v = stat(dict(zip(signs, vals)))
        mean += v / n
        ge += v >= obs
    return obs, mean, len(ps), (ge + 1) / (n + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-seventy-ninth registered predictions: decipherment loop 4, sound values from substitution', 'predict_test179')
    lex = lambda g: g not in R.NUMS and g not in M
    bodies = lambda lines: sorted({b for b, e in T.names(lines) if b})
    pa = subst_pairs(bodies(A), lex)
    pb = subst_pairs(bodies(sorted({tuple(ln) for r in load(only_m77=True) for ln in r['seq'] if ln})), lex)
    pall = pa + pb
    words = set()
    with open(os.path.join(LINB, 'corpus_damos_words.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['status'] == 'complete' and '*' not in r['word']:
                words.add(tuple(r['word'].split('-')))
    lp = subst_pairs(sorted(words), lambda s: True)
    lkey = {s: s for p in lp for s in p}
    o, m, n, p = test(lp, lkey)
    rd.rec('SP1', 'Linear B control', 'syllabogram pairs %d; similarity %.3f against %.3f shuffled; p = %.4f' % (n, o, m, p), p < 0.05)
    keys = {}
    for name, fn in (('Fairservis', 'fairservis1992.tsv'), ('Parpola', 'parpola1994.tsv'), ('Mahadevan', 'mahadevan2014.tsv'), ('Kak', 'kak1988.tsv')):
        meta, k, g = bench.load_key(os.path.join(R.HERE, 'keys', fn))
        keys[name] = k
    keys['Yajnadevam'] = bench.load_yajnadevam(YAJ)[1]
    both = []
    for key_id, name in (('SP2', 'Fairservis'), ('SP3', 'Parpola'), ('SP4', 'Yajnadevam'), ('SP5', 'Mahadevan'), ('SP6', 'Kak')):
        o, m, n, p = test(pall, keys[name])
        if o is None:
            rd.rec(key_id, '%s key' % name, 'no keyed substitution pair', False)
            continue
        ok = n >= 10 and p < 0.05
        rd.rec(key_id, '%s key' % name, 'keyed pairs %d; similarity %.3f against %.3f shuffled; p = %.4f' % (n, o, m, p), ok)
        oa, ma, na, pa_ = test(pa, keys[name])
        ob, mb, nb, pb_ = test(pb, keys[name])
        rd.say('- %s on A-names: %s; on B-names: %s.' % (name, 'p = %.4f (%d pairs)' % (pa_, na) if oa is not None else 'none',
                                                         'p = %.4f (%d pairs)' % (pb_, nb) if ob is not None else 'none'))
        if oa is not None and ob is not None and pa_ < 0.05 and pb_ < 0.05 and na >= 10 and nb >= 10:
            both.append(name)
    rd.rec('SP7', 'a key passes on both samples', 'passing on A and B: %s' % (', '.join(both) or 'none'), bool(both))
    rd.finish()


if __name__ == '__main__':
    main()
