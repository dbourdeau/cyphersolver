"""Round 31 (loop round 3 of 10): word endings, beginnings and possible grammar.

S1  Final signs are associated with function (entry label vs heading).
S2  Final signs are associated with register (religious vs administrative).
S3  Initial signs are associated with function.
S4  Initial signs are associated with register.
S5  Words on the same tablet share final signs beyond chance (signs shuffled across tablets, tablet sizes kept).
S6  Words on the same tablet share initial signs beyond chance.
S7  Linear A entry-label finals resemble the stem-final syllables of Knossos names more than those of Pylos names.
S8  Two-sign endings attach to more distinct stems than chance (endings shuffled across words). Control: Linear B.
S9  Neighbouring words on a tablet share their final sign more than chance (order shuffled within the tablet).
S10 A heading and the next word share their final sign more than chance.
"""
from collections import Counter, defaultdict
from math import log2
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402

grid, LA, LB, X, B, T = R.grid, R.LA, R.LB, R.X, R.B, R.T
PLAIN = re.compile(r'^[a-z]+[0-9]?$')


def typed(role):
    fn = defaultdict(Counter)
    for r, t, w in B.LA_ADMIN:
        fn[w][t.get('function')] += 1
    return {w: c.most_common(1)[0][0] for w, c in fn.items() if c.most_common(1)[0][0] in role}


def assoc_test(words, labels, part, keep=10):
    sign = (lambda w: w[-1]) if part == 'final' else (lambda w: w[0])
    c = Counter(sign(w) for w in words)
    pairs = [(sign(w), l) for w, l in zip(words, labels) if c[sign(w)] >= keep]
    real, p, nm = R.assoc(pairs)
    return real, p, nm, len(pairs)


def fn_words():
    fn = typed(('entry label', 'heading'))
    words = sorted(fn)
    return words, [fn[w] for w in words]


def reg_words():
    rel = {w for _, _, w in B.LA_RELIG}
    adm = {w for _, _, w in B.LA_ADMIN} - rel
    words = sorted(rel | adm)
    return words, ['rel' if w in rel else 'adm' for w in words]


def S1():
    r, p, nm, n = assoc_test(*fn_words(), 'final')
    return p, 'Final signs are associated with function (entry vs heading)', {'chi2': round(r, 1), 'null': round(nm, 1), 'p': round(p, 4), 'words': n}, {}


def S2():
    r, p, nm, n = assoc_test(*reg_words(), 'final')
    return p, 'Final signs are associated with register', {'chi2': round(r, 1), 'null': round(nm, 1), 'p': round(p, 4), 'words': n}, {}


def S3():
    r, p, nm, n = assoc_test(*fn_words(), 'initial')
    return p, 'Initial signs are associated with function', {'chi2': round(r, 1), 'null': round(nm, 1), 'p': round(p, 4), 'words': n}, {}


def S4():
    r, p, nm, n = assoc_test(*reg_words(), 'initial')
    return p, 'Initial signs are associated with register', {'chi2': round(r, 1), 'null': round(nm, 1), 'p': round(p, 4), 'words': n}, {}


def tablet_words():
    tabs = defaultdict(list)
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        for t in r['tokens']:
            if t['cls'] == 'word' and t['label'] not in R.X.TERMS:
                w = tuple(t['label'].lower().split('-'))
                if len(w) >= 2 and all(PLAIN.match(x) for x in w):
                    tabs[R.X.whole(r['name'])].append((w, t.get('function')))
    return {k: v for k, v in tabs.items() if len(v) >= 3}


TABS = tablet_words()


def cluster(part):
    sign = (lambda w: w[-1]) if part == 'final' else (lambda w: w[0])
    keys = sorted(TABS)
    items = [(k, sign(w)) for k in keys for w, _ in TABS[k]]

    def stat(signs):
        by = defaultdict(list)
        for (k, _), s in zip(items, signs):
            by[k].append(s)
        return sum(sum(n * (n - 1) for n in Counter(v).values()) for v in by.values())
    real = stat([s for _, s in items])
    signs = [s for _, s in items]
    null = []
    for _ in range(R.REPS):
        R.rng.shuffle(signs)
        null.append(stat(signs))
    return real, R.pv_hi(null, real), sum(null) / len(null)


def S5():
    r, p, nm = cluster('final')
    return p, 'Words on the same tablet share final signs beyond chance', {'same_final_pairs': r, 'null': round(nm, 1), 'p': round(p, 4)}, {}


def S6():
    r, p, nm = cluster('initial')
    return p, 'Words on the same tablet share initial signs beyond chance', {'same_initial_pairs': r, 'null': round(nm, 1), 'p': round(p, 4)}, {}


def dist(syls):
    c = Counter(syls)
    n = sum(c.values())
    return {k: v / n for k, v in c.items()}


def jsd(p, q):
    keys = set(p) | set(q)
    m = {k: (p.get(k, 0) + q.get(k, 0)) / 2 for k in keys}
    kl = lambda a: sum(a[k] * log2(a[k] / m[k]) for k in keys if a.get(k, 0) > 0)
    return (kl(p) + kl(q)) / 2


def S7():
    ent = [w for w, f in typed(('entry label',)).items()]
    la = dist(w[-1] for w in ent)
    stemfin = lambda ws: dist(w[-2] for w in ws if len(w) >= 3)
    real, p, nm = R.compare(T.PY_N, T.KN_N, lambda ws: jsd(la, stemfin(ws)))
    return p, 'Linear A name finals resemble Knossos stem-final syllables more than Pylos ones', {'jsd_KN': round(jsd(la, stemfin(T.KN_N)), 4), 'jsd_PY': round(jsd(la, stemfin(T.PY_N)), 4), 'p': round(p, 4)}, {}


def productivity(ws, reps):
    long_ = [w for w in ws if len(w) >= 4]
    stat = lambda wl: sum(1 for e, n in Counter(w[-2:] for w in wl).items() if len({w[:-2] for w in wl if w[-2:] == e}) >= 3)
    real = stat(long_)
    ends = [w[-2:] for w in long_]
    stems = [w[:-2] for w in long_]
    null = []
    for _ in range(reps):
        R.rng.shuffle(ends)
        null.append(stat([s + e for s, e in zip(stems, ends)]))
    return real, sum(null) / len(null), R.pv_hi(null, real)


def S8():
    r, nm, p = productivity(LA, 500)
    lr, lnm, lp = productivity(LB, 100)
    return p, 'Two-sign endings attach to 3+ distinct stems more than chance', {'LA_endings': r, 'null': round(nm, 1), 'p': round(p, 4)}, {'Linear B': {'endings': lr, 'null': round(lnm, 1), 'p': round(lp, 4)}}


def adjacent(pred_first=lambda f: True):
    keys = sorted(TABS)

    def stat(tabs):
        return sum(1 for v in tabs for i in range(len(v) - 1) if pred_first(v[i][1]) and v[i][0][-1] == v[i + 1][0][-1])
    real = stat([TABS[k] for k in keys])
    null = []
    for _ in range(R.REPS):
        sh = []
        for k in keys:
            v = list(TABS[k])
            R.rng.shuffle(v)
            sh.append(v)
        null.append(stat(sh))
    return real, R.pv_hi(null, real), sum(null) / len(null)


def S9():
    r, p, nm = adjacent()
    return p, 'Neighbouring words share their final sign more than chance', {'pairs': r, 'null': round(nm, 2), 'p': round(p, 4)}, {}


def S10():
    r, p, nm = adjacent(lambda f: f == 'heading')
    return p, 'A heading and the next word share their final sign more than chance', {'pairs': r, 'null': round(nm, 2), 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round31', 'word endings, beginnings and possible grammar', __doc__, [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10])


def cluster_checks(part):
    """Added after the run: unique words per tablet, signs shuffled only among tablets of the same site."""
    sign = (lambda w: w[-1]) if part == 'final' else (lambda w: w[0])
    site = {R.X.whole(r['name']): r['site'] for r in B.READ['records']}
    keys = sorted(TABS)
    items = [(k, sign(w)) for k in keys for w in sorted({w for w, _ in TABS[k]})]

    def stat(signs):
        by = defaultdict(list)
        for (k, _), s in zip(items, signs):
            by[k].append(s)
        return sum(sum(n * (n - 1) for n in Counter(v).values()) for v in by.values())
    real = stat([s for _, s in items])
    idx = defaultdict(list)
    for i, (k, _) in enumerate(items):
        idx[site.get(k)].append(i)
    null = []
    for _ in range(1000):
        sh = [s for _, s in items]
        for st, ii in idx.items():
            v = [sh[i] for i in ii]
            R.rng.shuffle(v)
            for i, x in zip(ii, v):
                sh[i] = x
        null.append(stat(sh))
    return {'pairs': real, 'null': round(sum(null) / len(null), 1), 'p': round(R.pv_hi(null, real), 4)}
