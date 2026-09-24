"""Hundred-and-eighteenth registered prediction set (PREDICTIONS.md, CE1-CE15): are the closers endings? Writes
results/predict_test118.md."""
from collections import Counter, defaultdict

import rtools as R
from predict_test4 import OPEN
from predict_test43 import sp_perm
from predict_test103 import CL

CITY = ('Mohenjo-daro', 'Harappa')


def strip(t):
    t = list(t)
    if len(t) >= 3 and t[0] in OPEN and t[1] in ('2', '60', '1'):
        t = t[2:]
    return tuple(t)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Hundred-and-eighteenth registered predictions: are the closers endings?', 'predict_test118')
    DL = sorted({tuple(t) for t in AB})
    c4 = [(t, i) for t in DL for i in range(1, len(t)) if t[i] == '400' and t[i - 1] in CL]
    rd.say("- distinct 'closer 400' tokens %d." % len(c4))
    rd.say()

    def ce1(lines, key, lab):
        x = [(t, i) for t in lines for i in range(1, len(t)) if t[i] == '400' and t[i - 1] in CL]
        rd.thr(key, 'closer + 400 ends the line%s' % lab, "line-final 400 after a closer", sum(i == len(t) - 1 for t, i in x), len(x), 0.8)
    ce1(DL, 'CE1', '')
    Fn = [r for r in F if r['type'] != 'TAB:C']
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in Fn for ln in r['seq'] if ln})
    hc = lambda t: any(t[i] in CL for i in range(len(t)))
    c400 = lambda t: any(t[i] == '400' and i > 0 and t[i - 1] in CL for i in range(len(t)))

    def ce2(fd, key, lab):
        rd.gtl(key, 'closer + 400 is a tablet form%s' % lab, "tablet, 'closer 400' lines", [ty == 'TAB' for s, ty, t in fd if hc(t) and c400(t)],
               [ty == 'TAB' for s, ty, t in fd if hc(t) and not c400(t)])
    ce2(FD, 'CE2', '')
    rd.gtl('CE3', 'closer + 400 is Harappan', "Harappa, 'closer 400' lines", [s == 'Harappa' for s, ty, t in FD if hc(t) and c400(t) and s in CITY],
           [s == 'Harappa' for s, ty, t in FD if hc(t) and not c400(t) and s in CITY])
    n90 = sum(1 for t in DL if any(t[i] == '90' and t[i - 1] in CL for i in range(1, len(t))))
    rd.rec('CE4', '90 belongs to 740', "distinct lines with 'closer 90': %d; threshold under 3" % n90, n90 < 3)
    both = [t for t in DL if '740' in t and hc(t)]
    rd.thr('CE5', 'the closer follows the name', "lines where 740 directly precedes a closer", sum(any(t[i] in CL and t[i - 1] == '740' for i in range(1, len(t))) for t in both), len(both), 0.5)
    hd = defaultdict(Counter)
    for t in DL:
        s = strip(t)
        for i in range(1, len(s)):
            if s[i] in CL:
                hd[s[i - 1]]['C'] += 1
            elif s[i] == '740':
                hd[s[i - 1]]['740'] += 1
            elif s[i] == '520':
                hd[s[i - 1]]['520'] += 1
    h5 = [h for h in hd if sum(hd[h].values()) >= 5]
    o, p = sp_perm([hd[h]['C'] / sum(hd[h].values()) for h in h5], [-hd[h]['740'] / sum(hd[h].values()) for h in h5])
    rd.rec('CE6', 'closer and 740 replace each other', 'heads %d; Spearman(closer share, -740 share) %.3f; p = %.4f' % (len(h5), o, p), o >= 0.3 and p < 0.05)
    b740 = set()
    bcl = set()
    for t in DL:
        s = strip(t)
        for i in range(1, len(s)):
            if s[i] == '740':
                b740.add(s[:i])
            if s[i] in CL:
                bcl.add(s[:i])
    n = len(b740 & bcl)
    rd.rec('CE7', 'the same body takes either', 'bodies before both 740 and a closer: %d; threshold 5' % n, n >= 5)
    e7c = sum(1 for t in DL if len(t) >= 2 and t[-1] in CL and t[-2] == '740')
    rd.rec('CE8', "'740 + closer' is a line type", "lines ending '740 + closer': %d; threshold 10" % e7c, e7c >= 10)
    cnt_c = [i >= 2 and s[i - 2] in R.NUMS for t in DL for s in [strip(t)] for i in range(1, len(s)) if s[i] in CL]
    cnt_7 = [i >= 2 and s[i - 2] in R.NUMS for t in DL for s in [strip(t)] for i in range(1, len(s)) if s[i] == '740']
    a, c = cnt_c, cnt_7
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('CE9', 'closers count like 740', 'counted head, closers %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p >= 0.05)
    cl = [t for t in DL if hc(t)]
    l7 = [t for t in DL if '740' in t]
    s1 = sum(c400(t) for t in cl) / len(cl)
    s2 = sum(any(t[i] == '400' and t[i - 1] == '740' for i in range(1, len(t))) for t in l7) / len(l7)
    rd.rec('CE10', 'closers take 400 as often as 740 does', "'closer 400' share %.3f, '740 400' share %.3f; ratio %.2f" % (s1, s2, s1 / s2), 0.5 <= s1 / s2 <= 2)
    BL = sorted({tuple(t) for t in B})
    ce1(BL, 'CE11', ' (B)')
    ce2(FD, 'CE12', " (F', same data as CE2)")
    bc4 = {strip(t)[:strip(t).index(t[i - 1])] for t, i in c4 if t[i - 1] in strip(t)}
    rd.thr('CE13', "'closer 400' bodies are names", "bodies also before 740", len(bc4 & b740), len(bc4), 0.2)
    OS = [t for s, ty, t in FD if s not in CITY]
    n = sum(c400(t) for t in set(OS))
    rd.rec('CE14', "'closer 400' at the small sites", 'distinct lines %d; threshold 3' % n, n >= 3)
    nt = [t[i + 1] for t in DL for i in range(len(t) - 1) if t[i] in CL and t[i + 1] != '400']
    rd.thr('CE15', 'other closer tails are counts', 'first sign a numeral (%s)' % dict(Counter(nt).most_common(5)), sum(g in R.NUMS for g in nt), len(nt), 0.5)
    rd.finish()


if __name__ == '__main__':
    main()
