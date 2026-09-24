"""Hundred-and-thirty-fifth registered prediction set (PREDICTIONS.md, RD1-RD10): does a proposed reading respect the
structure? Uses ICIT field 35 (romanised reading, source not identified). Writes results/predict_test135.md."""
import math
import random
import re
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test43 import sp_perm

random.seed(155)
HEAD = ('817', '820', '861')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-thirty-fifth registered predictions: does a proposed reading respect the structure?', 'predict_test135')
    rows = []
    for r in F:
        rec = recs[r['sealid']]
        # values 'ref:NNN' point to another object's reading and '-' marks none; both are left out
        if len(rec) > 35 and rec[35].strip() and not rec[35].strip().startswith('ref:') and rec[35].strip() not in ('-', 'None'):
            ls = [tuple(ln) for ln in r['seq'] if ln]
            rdg = re.sub(r'[^a-z]', '', rec[35].lower())
            if len(ls) == 1 and rdg:
                rows.append((ls[0], rdg))
    rd.say('- single-line texts with a reading: %d.' % len(rows))
    rd.say()
    fin = lambda s: s[-1]
    e7 = [fin(x) for t, x in rows if t[-1] == '740']
    ot = defaultdict(list)
    for t, x in rows:
        if t[-1] not in R.NUMS and t[-1] != '740':
            ot[t[-1]].append(fin(x))
    share = lambda xs: Counter(xs).most_common(1)[0][1] / len(xs)
    osh = [share(v) for v in ot.values() if len(v) >= 5]
    rd.rec('RD1', 'the 740 ending has a fixed sound', '740 texts %d: final-letter share %.2f (%s); other last signs (5+ texts) mean %.2f' % (
        len(e7), share(e7), Counter(e7).most_common(3), sum(osh) / max(1, len(osh))), share(e7) > sum(osh) / max(1, len(osh)))
    en = [(t[-1], fin(x)) for t, x in rows if t[-1] in R.END]
    rd.mi('RD2', 'the two endings sound different', 'texts ending 740/520', [a for a, _ in en], [b for _, b in en])
    by = defaultdict(set)
    cnt = Counter()
    for t, x in rows:
        by[t].add(x)
        cnt[t] += 1
    rep = [t for t in cnt if cnt[t] >= 2]
    rd.thr('RD3', 'the same text, the same reading', 'repeated texts with one reading', sum(len(by[t]) == 1 for t in rep), len(rep), 0.95)
    o, p = sp_perm([len(t) for t, x in rows], [len(x) for t, x in rows])
    rd.rec('RD4', 'longer texts, longer readings', 'Spearman %.3f; p = %.4f' % (o, p), o >= 0.5 and p < 0.05)

    def pairs_test(key, title, keyf, valf):
        g = defaultdict(list)
        for t, x in rows:
            g[keyf(t)].append(valf(x))
        same = [sum(1 for i in range(len(v)) for j in range(i + 1, len(v)) if v[i] == v[j]) / max(1, len(v) * (len(v) - 1) / 2) for v in g.values() if len(v) >= 2]
        obs = sum(same) / max(1, len(same))
        allv = [valf(x) for t, x in rows]
        rnd = sum(1 for _ in range(20000) if random.choice(allv) == random.choice(allv)) / 20000
        rd.rec(key, title, 'within-group agreement %.3f, random pairs %.3f' % (obs, rnd), obs > 2 * rnd)
    pairs_test('RD5', 'the first sign sets the first letter', lambda t: t[0], lambda x: x[0])
    pairs_test('RD6', 'the last sign sets the last letters', lambda t: t[-1], lambda x: x[-2:])
    lp = [len(x) / len(t) for t, x in rows if len(t) >= 2]
    m = sum(lp) / len(lp)
    sd = math.sqrt(sum((v - m) ** 2 for v in lp) / len(lp))
    rd.rec('RD7', 'a steady rate of letters per sign', 'mean %.2f, CV %.2f; threshold 0.5' % (m, sd / m), sd / m < 0.5)
    x7 = [x for t, x in rows if len(t) == 2 and t[-1] == '740']
    rd.thr('RD8', "'X 740' readings end alike", 'commonest final two letters (%s)' % Counter(x[-2:] for x in x7).most_common(3),
           Counter(x[-2:] for x in x7).most_common(1)[0][1] if x7 else 0, len(x7), 0.6)
    hd = defaultdict(dict)
    for t, x in rows:
        if len(t) >= 3 and t[0] in HEAD:
            hd[t[1:]][t[0]] = x
    pr = [v for v in hd.values() if len(v) >= 2]
    ok = 0
    tot = 0
    for v in pr:
        xs = list(v.values())
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                a, b = xs[i], xs[j]
                k = 0
                while k < min(len(a), len(b)) and a[-1 - k] == b[-1 - k]:
                    k += 1
                tot += 1
                ok += k >= min(len(a), len(b)) - 4
    rd.thr('RD9', 'the heading changes only the front', 'heading-variant pairs sharing all but the first part', ok, tot, 0.5)
    ct = defaultdict(set)
    for t, x in rows:
        if len(t) >= 2 and t[-1] == '700' and all(g in R.NUMS for g in t[:-1]):
            ct[t].add(x)
    rd.thr('RD10', 'counts read consistently', 'count texts with one reading', sum(len(v) == 1 for v in ct.values()), len(ct), 0.9)
    rd.finish()


if __name__ == '__main__':
    main()
