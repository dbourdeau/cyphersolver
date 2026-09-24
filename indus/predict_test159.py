"""Hundred-and-fifty-ninth registered prediction set (PREDICTIONS.md, PL1-PL10): the packed-legend reading and the
word-divider question (Fuls 2024 against Wells 2011). Writes results/predict_test159.md."""
import math
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test103 import CL
from predict_test142 import cuts_of
from predict_test157 import kind, profile
from predict_test61 import units

random.seed(179)
CITIES = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-fifty-ninth registered predictions: the packed-legend reading and the word-divider question', 'predict_test159')
    seals = [r for r in F if r['type'].startswith('SEAL') and recs[r['sealid']][3] in CITIES]
    cat = {k: {c: Counter() for c in CITIES} for k in ('opener', 'core', 'post')}
    for r in seals:
        c = recs[r['sealid']][3]
        us = {'opener': set(), 'core': set(), 'post': set()}
        for ln in r['seq']:
            t = list(ln)
            nm = R.name_of(t)
            if nm and nm[0]:
                b, e = nm
                if len(b) >= 3:
                    us['opener'].add(b[0])
                    us['core'].add((b[1:], e))
                k = max(i for i, g in enumerate(t) if g in R.END)
                us['post'] |= {g for g in t[k + 1:] if g in CL or g in ('400', '90')}
        for k, v in us.items():
            for u in v:
                cat[k][c][u] += 1
    P = {k: profile(v) for k, v in cat.items()}
    for k, p in P.items():
        rd.say('- %s: %d / %d, shared %d; %.2f, %.2f, %.2f -> %s.' % (k, p['n'][0], p['n'][1], p['n'][2], p['ratio'], p['shared'], p['one'], kind(p)))
    rd.say()
    rd.rec('PL1', 'openers are title-like', 'opener profile -> %s' % kind(P['opener']), kind(P['opener']) == 'title-like')
    rd.rec('PL2', 'name cores are person-like', 'core profile -> %s' % kind(P['core']), kind(P['core']) == 'person-like')
    rd.thr('PL3', 'openers are shared', "smaller city's openers also in the other", P['opener']['m'], P['opener']['small'], 0.5)

    def z(xs, ys):
        o = T.mi(xs, ys)
        yy = list(ys)
        v = []
        for _ in range(1000):
            random.shuffle(yy)
            v.append(T.mi(xs, yy))
        m = sum(v) / len(v)
        sd = math.sqrt(sum((x - m) ** 2 for x in v) / len(v)) or 1e-9
        return (o - m) / sd, o
    mo = [(nm[0], recs[r['sealid']][18].strip()) for r in [x for x in F if x['type'].startswith('SEAL')] for nm in R.names_in(r)
          if nm[0] and len(nm[0]) >= 3 and recs[r['sealid']][18].strip() not in ('-', '')]
    zo, mio = z([b[0] for b, m in mo], [m for b, m in mo])
    zh, mih = z([b[-1] for b, m in mo], [m for b, m in mo])
    rd.rec('PL4', 'the opener tells the motif', 'names %d; opener MI %.3f (z %.2f), head MI %.3f (z %.2f)' % (len(mo), mio, zo, mih, zh), zo > zh)
    rd.rec('PL5', 'post-name signs are title-like', 'post-name profile -> %s' % kind(P['post']), kind(P['post']) == 'title-like')
    DL = sorted({tuple(t) for t in A + B})
    whole = set(DL)
    inner = defaultdict(list)
    for t in DL:
        for i in range(1, len(t) - 1):
            inner[t[i]].append(t[:i] in whole and t[i + 1:] in whole)
    pool = [v for s, xs in inner.items() if s not in ('1', '2') and len(xs) >= 20 for v in xs]
    for key, s in (('PL6', '1'), ('PL7', '2')):
        rd.gtl(key, 'sign %s as a word divider' % s, 'both sides attested as whole texts, sign %s' % s, inner[s], pool)
    texts = sorted({tuple(tuple(ln) for ln in r['seq'] if ln) for r in F if sum(1 for ln in r['seq'] if ln) >= 2})
    near = lambda t, c: sum(t[k - 1] in ('1', '2') or t[k] in ('1', '2') for k in c)
    res = []
    for order in ('as listed', 'reversed'):
        tx = [(sum(ls, ()), cuts_of(ls)) for ls in (t if order == 'as listed' else t[::-1] for t in texts)]
        obs = sum(near(t, c) for t, c in tx)
        ge = tot = 0
        for _ in range(10000):
            v = sum(near(t, random.sample(range(1, len(t)), len(c))) for t, c in tx)
            ge += v >= obs
            tot += v
        res.append((order, obs, tot / 10000, (ge + 1) / 10001))
    rd.rec('PL8', 'line breaks next to 1 or 2', ['%s: %d against %.1f, p = %.4f' % x for x in res], all(o > m and p < 0.05 for _, o, m, p in res))
    ns = sorted({(b, e) for b, e in T.names(A + B) if b})
    U = units(sorted({b for b, e in ns if len(b) >= 2}))
    signs = sum(len(b) for b, e in ns)
    words = sum(len(b) - sum((b[i], b[i + 1]) in U for i in range(len(b) - 1)) for b, e in ns)
    ml = signs / words
    rd.rec('PL9', "Fuls's word length", 'signs %d in %d words: mean %.2f; registered range 1.5-2.0' % (signs, words, ml), 1.5 <= ml <= 2.0)
    byop, byhd = defaultdict(Counter), defaultdict(Counter)
    for r in seals:
        c = recs[r['sealid']][3]
        for b, e in {x for x in R.names_in(r) if x[0]}:
            byhd[b[-1]][c] += 1
            if len(b) >= 3:
                byop[b[0]][c] += 1

    def pairs(d):
        same = sum(v[c] * (v[c] - 1) // 2 for v in d.values() for c in CITIES)
        cross = sum(v[CITIES[0]] * v[CITIES[1]] for v in d.values())
        return same, same + cross
    so, no = pairs(byop)
    sh, nh = pairs(byhd)
    rd.gt('PL10', 'same opener, same city', 'same-city pairs, opener-sharing', so, no, sh, nh)
    rd.finish()


if __name__ == '__main__':
    main()
