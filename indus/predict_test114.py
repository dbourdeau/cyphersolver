"""Hundred-and-fourteenth registered prediction set (PREDICTIONS.md, SR1-SR20): small-then-large numeral runs.
Writes results/predict_test114.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test112 import runs

random.seed(134)
HEAD = ('817', '820', '861')


def rows(lines):
    """(line, i, j, run) for runs not directly after a heading sign."""
    return [(t, i, j, r) for t in lines for i, j, r in runs(t) if not (i > 0 and t[i - 1] in HEAD)]


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-fourteenth registered predictions: small-then-large numeral runs', 'predict_test114')
    DL = sorted({tuple(t) for t in AB})
    V = lambda g: R.NUMS[g][0]
    R_ = rows(DL)
    two = [x for x in R_ if len(x[3]) == 2]
    small = lambda r: V(r[0]) < V(r[1])
    large = lambda r: V(r[0]) > V(r[1])
    is2N = lambda r: len(r) == 2 and r[0] == '2'
    rd.say('- runs %d; 2-sign %d; small-first %d; large-first %d.' % (len(R_), len(two), sum(small(x[3]) for x in two), sum(large(x[3]) for x in two)))
    rd.say()

    def sr1(rr, key, lab):
        s = [x for x in rr if len(x[3]) == 2 and small(x[3])]
        rd.thr(key, 'the small first element is a stroke%s' % lab, "small-first runs starting with '2' or '1'", sum(x[3][0] in ('2', '1') for x in s), len(s), 0.7)

    def sr2(rr, key, lab):
        rd.gtl(key, "'2 N' opens lines%s" % lab, "line-initial, '2 N' runs", [x[1] == 0 for x in rr if is2N(x[3])], [x[1] == 0 for x in rr if not is2N(x[3])])
    sr1(R_, 'SR1', '')
    sr2(R_, 'SR2', '')
    nx = Counter(x[0][x[2]] for x in R_ if is2N(x[3]) and x[2] < len(x[0]))
    rd.thr('SR3', "'2 N' counts few things", 'five commonest followers (%s)' % ', '.join('%s x%d' % kv for kv in nx.most_common(5)), sum(n for _, n in nx.most_common(5)), sum(nx.values()), 0.5)
    subs = set()
    for t in DL:
        for k in range(len(t) - 1):
            subs.add(t[k:k + 2])

    def sr4(lines, rr, key, lab):
        sb = {t[k:k + 2] for t in lines for k in range(len(t) - 1)}
        cases = [(x[0], x[1], x[2]) for x in rr if is2N(x[3]) and x[2] < len(x[0])]
        ok = 0
        for t, i, j in cases:
            nxp = (t[i + 1], t[j])
            if any(u[k:k + 2] == nxp and not (k > 0 and u[k - 1] == '2') for u in lines for k in range(len(u) - 1) if u is not t):
                ok += 1
        rd.thr(key, "the '2' is an added prefix%s" % lab, "'2 N X' with 'N X' attested without the '2'", ok, len(cases), 0.5)
    sr4(DL, R_, 'SR4', '')
    allnum = [g for t in DL for g in t if g in R.NUMS]
    after2 = [x[3][1] for x in R_ if is2N(x[3])]
    rd.gtl('SR5', "'2' comes before long numbers", "long kind, after the '2' prefix", [R.kind(g) == 'long' for g in after2], [R.kind(g) == 'long' for g in allnum])
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in Fn for ln in r['seq'] if ln})
    has2N = lambda t: any(is2N(x[3]) for x in rows([t]))
    x = [ty for s, ty, t in FD if has2N(t)]
    rd.thr('SR6', "'2 N' lines are seal lines", "'2 N' lines on seals", sum(ty == 'SEA' for ty in x), len(x), 0.7)
    rd.gtl('SR7', "'2 N' is Mohenjo-daran", "'2 N' lines, Mohenjo-daro", [has2N(t) for s, ty, t in FD if s == 'Mohenjo-daro'], [has2N(t) for s, ty, t in FD if s == 'Harappa'])
    rd.thr('SR8', 'doubled numerals', '2-sign runs of two identical numerals', sum(x[3][0] == x[3][1] for x in two), len(two), 0.1)
    nn = lambda x: x[2] < len(x[0]) and x[0][x[2]] not in R.NUMS
    a = [nn(x) for x in two if large(x[3])]
    c = [nn(x) for x in two if small(x[3])]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('SR9', 'both orders count things', 'followed by a sign, large-first %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p >= 0.05)
    r1 = [x for x in R_ if len(x[3]) == 2 and x[3][0] == '1']
    rd.thr('SR10', "'1 N' follows the ending", "'1 N' runs after 740/520", sum(x[1] > 0 and x[0][x[1] - 1] in R.END for x in r1), len(r1), 0.3)
    rd.gtl('SR11', 'small-first opens lines', 'line-initial, small-first', [x[1] == 0 for x in two if small(x[3])], [x[1] == 0 for x in two if large(x[3])])
    rd.thr('SR12', "the N in '2 N' is large", 'N worth 3+', sum(V(x[3][1]) >= 3 for x in R_ if is2N(x[3])), sum(1 for x in R_ if is2N(x[3])), 0.8)
    single = defaultdict(Counter)
    for x in R_:
        if len(x[3]) == 1 and x[2] < len(x[0]) and x[0][x[2]] not in R.NUMS:
            single[x[0][x[2]]][V(x[3][0])] += 1
    eqN = eqN2 = 0
    for x in R_:
        if is2N(x[3]) and nn(x):
            X = x[0][x[2]]
            if single[X]:
                c_ = single[X].most_common(1)[0][0]
                eqN += c_ == V(x[3][1])
                eqN2 += c_ == V(x[3][1]) + 2
    rd.rec('SR13', "the '2' is not added", 'X commonest count equals N: %d; equals N + 2: %d' % (eqN, eqN2), eqN > eqN2)

    def sr14(lines, key, lab):
        rr = [(t, i, j, r) for t in lines for i, j, r in runs(t)]
        un = {t[j] for t, i, j, r in rr if len(r) == 2 and r[0] == '2' and not (i > 0 and t[i - 1] in HEAD) and j < len(t) and t[j] not in R.NUMS}
        hd = {t[j] for t, i, j, r in rr if i > 0 and t[i - 1] in HEAD and r[0] == '2' and j < len(t) and t[j] not in R.NUMS}
        tok = Counter(g for t in lines for g in t if g not in R.NUMS)
        pool = sorted(tok, key=lambda g: -tok[g])[:200]
        obs = len(un & hd) / max(1, len(un | hd))
        ge = 0
        for _ in range(R.N // 10):
            rs = set(random.sample(pool, min(len(un), len(pool))))
            ge += len(rs & hd) / max(1, len(rs | hd)) >= obs
        p = (ge + 1) / (R.N // 10 + 1)
        rd.rec(key, "unheaded '2 N' is a heading remnant%s" % lab, 'Jaccard %.3f; p = %.4f (1,000 random sets)' % (obs, p), p < 0.05)
    sr14(DL, 'SR14', '')
    rd.thr('SR15', 'numbers are short', 'runs of 3+ signs', sum(len(x[3]) >= 3 for x in R_), len(R_), 0.03, above=False)
    BL = sorted({tuple(t) for t in B})
    RB = rows(BL)
    sr1(RB, 'SR16', ' (B)')
    sr2(RB, 'SR17', ' (B)')
    FL = sorted({t for s, ty, t in FD})
    RF = rows(FL)
    sr1(RF, 'SR18', " (F')")
    sr4(FL, RF, 'SR19', " (F')")
    sr14(FL, 'SR20', " (F')")
    rd.finish()


if __name__ == '__main__':
    main()
