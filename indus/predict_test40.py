"""Fortieth registered prediction set (PREDICTIONS.md, MB1-MB10): the core findings in Mahadevan's transcription (B).
Writes results/predict_test40.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test36 import make_tests

random.seed(60)


class GB:
    def __init__(self, lines):
        self.objs = []
        self.lines = lines
        self.names = T.names(lines)


def main():
    A, B, rowsA, recs, F = R.load_all()
    cat = R.cat_of()
    g = GB(B)
    rd = R.Round("Fortieth registered predictions: the core findings in Mahadevan's transcription", 'predict_test40')
    rd.say('- B lines %d, names %d.' % (len(g.lines), len(g.names)))
    rd.say()
    tests = make_tests(cat, {}, lambda r: '')
    for key, title, tk in (('MB1', 'the tiered form is for larger numbers', '10'), ('MB2', 'long strokes count containers', '11'),
                           ('MB3', 'long numbers open the line', '20'), ('MB4', 'affixed fish are attributes', '8'),
                           ('MB5', 'the head fixes the ending', '16'), ('MB6', 'the sign decides the number', '12'),
                           ('MB7', 'the last sign decides the ending', '1')):
        line, good, n = tests[tk](g)
        rd.rec(key, title, line + ('; under 20 cases, not testable' if n < 20 else ''), good and n >= 20)
    two = lambda t: sum(x in R.END for x in t) >= 2
    rd.gtl('MB8', 'long lines hold two names', 'two or more endings, long lines',
           [two(t) for t in B if len(t) >= 8], [two(t) for t in B if 5 <= len(t) <= 7])
    ns = set(g.names)
    keyc = defaultdict(Counter)
    for body, end in ns:
        for i in range(len(body)):
            keyc[(end, len(body), body[:i], body[i + 1:])][body[i]] += 1
    by_sign = defaultdict(dict)
    for k_, c_ in keyc.items():
        for s, n2 in c_.items():
            by_sign[s][k_] = n2

    def pc(x, y):
        da, db = by_sign.get(x, {}), by_sign.get(y, {})
        if len(da) > len(db):
            da, db = db, da
        return sum(n2 * db.get(k_, 0) for k_, n2 in da.items())
    pairs = [('220', '233'), ('220', '235'), ('220', '240')]
    obs = sum(pc(x, y) for x, y in pairs)
    tk_ = Counter(s for b, _ in ns for s in b)
    S = [s for s in tk_ if tk_[s] >= 5]
    q = T.quintiles(tk_, S)
    byq = defaultdict(list)
    for s in S:
        byq[q[s]].append(s)
    ge = 0
    for _ in range(R.N):
        tot = 0
        for x, y in pairs:
            if x not in q or y not in q:
                continue
            while True:
                u, v = random.choice(byq[q[x]]), random.choice(byq[q[y]])
                if u != v:
                    break
            tot += pc(u, v)
        ge += tot >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('MB9', 'fish variants alternate with the plain fish', 'pairs %s; total %d; p = %.4f' % (
        ', '.join('%s/%s %d' % (x, y, pc(x, y)) for x, y in pairs), obs, p), p < 0.05)
    bs = defaultdict(Counter)
    for t in B:
        for x, y in zip(t, t[1:]):
            if x in R.NUMS and y not in R.NUMS:
                bs[y][R.NUMS[x][0]] += 1
    sh = [c.most_common(1)[0][1] / sum(c.values()) for c in bs.values() if sum(c.values()) >= 10]
    rd.rec('MB10', 'each sign has its number', 'signs after a numeral 10+ times %d; mean share of the commonest value %.2f; threshold 0.60' % (
        len(sh), sum(sh) / max(1, len(sh))), bool(sh) and sum(sh) / len(sh) >= 0.6)
    rd.finish()


if __name__ == '__main__':
    main()
