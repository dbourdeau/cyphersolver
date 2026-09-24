"""Round 41 (second loop, round 3 of 10): Linear A list names (entry labels).

DD1  Entry labels repeat the consonant of neighbouring syllables more often than other administrative words.
DD2  Entry labels end on a narrower set of final signs (lower final-sign entropy) than other administrative words.
DD3  Entry labels ending in -TI stand on personnel (VIR) tablets more often than other entry labels.
DD4  Entry labels contain unread signs less often than headings.
DD5  Entry labels on VIR tablets differ in syllable profile from entry labels on tablets of goods.
DD6  Entry labels with an amount of 1 differ in syllable profile from those with larger amounts.
DD7  Entry labels recurring on 2+ tablets match Knossos words (exactly or as stem + one syllable) more often than
     entry labels found once.
DD8  Entry labels in the same list share syllables more than entry labels from different lists of the same site.
DD9  Two-sign entry labels stand on VIR tablets more often than longer entry labels.
DD10 Entry labels matching Knossos words stand on VIR tablets more often than other entry labels.
"""
from collections import Counter, defaultdict
from math import log, log2
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round29 as P  # noqa: E402

B, X, V, T = R.B, R.X, R.V, R.T
grid, cons = R.grid, P.cons
PLAIN = re.compile(r'^[A-Z]+[0-9]?$')


def label_table():
    """Per entry-label token: word tuple, record, VIR tablet flag, amount."""
    rows = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        vir = any(t['cls'] == 'commodity' and t['label'].startswith('VIR') for t in r['tokens'])
        ents = defaultdict(list)
        for t in r['tokens']:
            ents[t['entry']].append(t)
        for e, toks in ents.items():
            q = sum(t['value'] for t in toks if t['cls'] == 'number')
            for t in toks:
                if t['cls'] in ('word', 'word-with-unknown-sign') and t.get('function') == 'entry label' and t['label'] not in X.TERMS:
                    rows.append({'label': t['label'], 'w': tuple(t['label'].lower().split('-')), 'rec': X.whole(r['name']),
                                 'site': r['site'], 'vir': vir, 'q': q})
    return rows


ROWS = label_table()
ENT = sorted({x['w'] for x in ROWS if all(PLAIN.match(s) for s in x['label'].split('-'))})
fn = defaultdict(Counter)
for _r, _t, _w in B.LA_ADMIN:
    fn[_w][_t.get('function')] += 1
NONENT = sorted(w for w, c in fn.items() if c.most_common(1)[0][0] != 'entry label')


def cmp(a, b, f, text, lower=False):
    r, p, nm = R.compare(a, b, f, lower=lower)
    return p, text, {'entries': round(f(a), 4), 'others': round(f(b), 4), 'p': round(p, 4), 'n': [len(a), len(b)]}, {}


def DD1():
    f = lambda ws: sum(1 for w in ws for i in range(len(w) - 1) if cons(w[i]) and cons(w[i]) == cons(w[i + 1])) / max(1, sum(len(w) - 1 for w in ws))
    return cmp(ENT, NONENT, f, 'Entry labels repeat the consonant of neighbouring syllables more often')


def fin_entropy(ws):
    c = Counter(w[-1] for w in ws)
    n = sum(c.values())
    return -sum(v / n * log(v / n) for v in c.values())


def DD2():
    return cmp(ENT, NONENT, fin_entropy, 'Entry labels end on a narrower set of final signs', lower=True)


def DD3():
    items = [x for x in ROWS]
    r_, p, a, b = R.flag_compare(items, lambda x: x['label'].endswith('-TI'), lambda x: x['vir'])
    return p, 'Entry labels ending in -TI stand on VIR tablets more often', {'TI_on_VIR': a, 'other_on_VIR': b, 'p': round(p, 4)}, {}


def DD4():
    heads = [w for w, c in fn.items() if c.most_common(1)[0][0] == 'heading']
    ent_all = [x['label'] for x in ROWS]
    head_all = []
    for r in B.READ['records']:
        if r['support'] in B.ADMIN:
            head_all += [t['label'] for t in r['tokens'] if t['cls'] in ('word', 'word-with-unknown-sign') and t.get('function') == 'heading']
    unread = lambda ls: sum('*' in l for l in ls) / max(1, len(ls))
    r, p, nm = R.compare(ent_all, head_all, unread, lower=True)
    return p, 'Entry labels contain unread signs less often than headings', {'entries': round(unread(ent_all), 4), 'headings': round(unread(head_all), 4), 'p': round(p, 4)}, {}


def jsd_words(a, b):
    ca, cb = Counter(s for w in a for s in w), Counter(s for w in b for s in w)
    na, nb = sum(ca.values()), sum(cb.values())
    keys = set(ca) | set(cb)
    p_ = {k: ca[k] / na for k in keys}
    q_ = {k: cb[k] / nb for k in keys}
    m = {k: (p_[k] + q_[k]) / 2 for k in keys}
    kl = lambda x: sum(x[k] * log2(x[k] / m[k]) for k in keys if x[k] > 0)
    return (kl(p_) + kl(q_)) / 2


def profile_split(flag, text):
    ws = {}
    for x in ROWS:
        if all(PLAIN.match(s) for s in x['label'].split('-')):
            ws.setdefault(x['w'], []).append(flag(x))
    a = [w for w, f in ws.items() if all(f)]
    b = [w for w, f in ws.items() if not any(f)]
    r, p, nm = R.compare(a, b, lambda x: 0) if False else (None, None, None)
    real = jsd_words(a, b)
    pool, k, null = a + b, len(a), []
    for _ in range(R.REPS):
        R.rng.shuffle(pool)
        null.append(jsd_words(pool[:k], pool[k:]))
    p = R.pv_hi(null, real)
    return p, text, {'jsd': round(real, 4), 'null': round(sum(null) / len(null), 4), 'p': round(p, 4), 'n': [len(a), len(b)]}, {}


def DD5():
    return profile_split(lambda x: x['vir'], 'Entry labels on VIR tablets differ in syllable profile from those on tablets of goods')


def DD6():
    return profile_split(lambda x: x['q'] == 1, 'Entry labels with amount 1 differ in syllable profile from those with larger amounts')


KN_ALL = set(V.kn_only)
kn_match = lambda w: w in KN_ALL or any(k[:-1] == w for k in KN_ALL if len(k) == len(w) + 1)
KN_STEMS = {k[:-1] for k in KN_ALL if len(k) >= 3}
kn_match = lambda w: w in KN_ALL or w in KN_STEMS


def DD7():
    recs = defaultdict(set)
    for x in ROWS:
        recs[x['w']].add(x['rec'])
    words = [w for w in recs if w in set(ENT)]
    r_, p, a, b = R.flag_compare(words, lambda w: len(recs[w]) >= 2, kn_match)
    return p, 'Recurring entry labels match Knossos words more often than one-off labels', {'recurring': a, 'once': b, 'p': round(p, 4)}, {}


def DD8():
    by = defaultdict(set)
    site = {}
    for x in ROWS:
        if all(PLAIN.match(s) for s in x['label'].split('-')):
            by[x['rec']].add(x['w'])
            site[x['rec']] = x['site']
    recs = [k for k, v in by.items() if len(v) >= 3]
    items = [(k, w) for k in recs for w in by[k]]
    jac = lambda a, b: len(set(a) & set(b)) / len(set(a) | set(b))

    def stat(labels):
        g = defaultdict(list)
        for (k, w), l in zip(items, labels):
            g[l].append(w)
        tot = n = 0
        for ws in g.values():
            for i in range(len(ws)):
                for j in range(i + 1, len(ws)):
                    tot += jac(ws[i], ws[j])
                    n += 1
        return tot / max(1, n)
    labels = [k for k, _ in items]
    real = stat(labels)
    idx = defaultdict(list)
    for i, (k, _) in enumerate(items):
        idx[site[k]].append(i)
    null = []
    for _ in range(500):
        sh = list(labels)
        for ii in idx.values():
            v = [labels[i] for i in ii]
            R.rng.shuffle(v)
            for i, x in zip(ii, v):
                sh[i] = x
        null.append(stat(sh))
    p = R.pv_hi(null, real)
    return p, 'Entry labels in the same list share syllables more than labels from other lists of the site', {'mean_jaccard': round(real, 4), 'null': round(sum(null) / len(null), 4), 'p': round(p, 4), 'lists': len(recs)}, {}


def DD9():
    r_, p, a, b = R.flag_compare(ROWS, lambda x: len(x['w']) == 2, lambda x: x['vir'])
    return p, 'Two-sign entry labels stand on VIR tablets more often', {'two_sign_on_VIR': a, 'longer_on_VIR': b, 'p': round(p, 4)}, {}


def DD10():
    items = [x for x in ROWS if all(PLAIN.match(s) for s in x['label'].split('-'))]
    r_, p, a, b = R.flag_compare(items, lambda x: kn_match(x['w']), lambda x: x['vir'])
    return p, 'Entry labels matching Knossos words stand on VIR tablets more often', {'matched_on_VIR': a, 'other_on_VIR': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round41', 'Linear A list names', __doc__, [DD1, DD2, DD3, DD4, DD5, DD6, DD7, DD8, DD9, DD10])
