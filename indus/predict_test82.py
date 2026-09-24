"""Eighty-second registered prediction set (PREDICTIONS.md, PS1-PS20): counted 520 and the suffixes 90, 400, 151.
Writes results/predict_test82.md. Distinct lines and names."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from signs import FISH

random.seed(102)
SUF = ('90', '400', '151')


def suffix_lines(lines):
    out = []
    for t in lines:
        nm = R.name_of(list(t))
        if nm and nm[0]:
            i = max(j for j, g in enumerate(t) if g in R.END)
            out.append((nm[0], nm[1], t[i + 1] if i + 1 < len(t) else '#'))
    return out


def jperm(rows, a, b):
    hh = [h for h, f in rows]
    ff = [f for h, f in rows]

    def jac(fs):
        x = {h for h, f in zip(hh, fs) if f == a}
        y = {h for h, f in zip(hh, fs) if f == b}
        return len(x & y) / max(1, len(x | y))
    obs = jac(ff)
    sh = ff[:]
    le = 0
    for _ in range(R.N):
        random.shuffle(sh)
        le += jac(sh) <= obs
    return obs, (le + 1) / (R.N + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    cat = R.cat_of()
    rd = R.Round('Eighty-second registered predictions: counted 520 and the suffixes 90, 400, 151', 'predict_test82')
    DL = sorted({tuple(t) for t in AB})
    n5 = [(t, i) for t in DL for i in range(1, len(t)) if t[i] == '520' and t[i - 1] in R.NUMS]
    rd.say("- 'N 520' tokens %d." % len(n5))
    rd.say()
    rd.thr('PS1', "'N 520' ends the line", "line-final 'N 520'", sum(i == len(t) - 1 for t, i in n5), len(n5), 0.8)
    val = lambda t, i: sum(R.NUMS[g][0] for g in t[max(j for j in range(i) if not all(x in R.NUMS for x in t[j:i])) + 1 if any(t[j] not in R.NUMS for j in range(i)) else 0:i])
    vc = Counter(val(t, i) for t, i in n5)
    rd.thr('PS2', 'few numbers before 520', 'two commonest values (%s)' % dict(vc.most_common(5)), sum(n for _, n in vc.most_common(2)), len(n5), 0.8)
    FD = sorted({(r['site'].strip(), r['type'][:3], tuple(ln)) for r in F for ln in r['seq'] if ln})
    has5 = [(ty, any(t[i] == '520' and t[i - 1] in R.NUMS for i in range(1, len(t)))) for s, ty, t in FD if '520' in t]
    rd.gtl('PS3', "'N 520' is a tablet form", "tablet, 'N 520' lines", [ty == 'TAB' for ty, x in has5 if x], [ty == 'TAB' for ty, x in has5 if not x])

    def before_run(t, i):
        j = i - 1
        while j > 0 and t[j - 1] in R.NUMS:
            j -= 1
        return t[j - 1] if j > 0 else None
    bb = [before_run(t, i) for t, i in n5]
    bb = [g for g in bb if g]
    rd.thr('PS4', 'a fish is counted with 520', 'fish before the number', sum(g in FISH for g in bb), len(bb), 0.3)
    et = [(t[i], i > 0 and t[i - 1] in R.NUMS) for t in DL for i in range(len(t)) if t[i] in R.END]
    rd.gtl('PS5', '520 is counted, 740 is not', 'after a numeral, 520', [x for g, x in et if g == '520'], [x for g, x in et if g == '740'])

    def after_end(sign, lines):
        tk = [(t, i) for t in lines for i in range(len(t)) if t[i] == sign]
        return sum(i > 0 and t[i - 1] in R.END for t, i in tk), len(tk)
    k, n = after_end('90', DL)
    rd.thr('PS6', '90 is a suffix only', '90 tokens after an ending', k, n, 0.9)
    k, n = after_end('400', DL)
    rd.thr('PS7', '400 has other uses', '400 tokens after an ending', k, n, 0.5, above=False)
    k, n = after_end('151', DL)
    rd.thr('PS8', '151 has other uses', '151 tokens after an ending', k, n, 0.5, above=False)
    SL = suffix_lines(DL)
    hs = defaultdict(set)
    for b, e, f in SL:
        if f in ('90', '400'):
            hs[b[-1]].add(f)
    rd.thr('PS9', 'a head takes one suffix', 'heads with only one of 90 and 400', sum(len(v) == 1 for v in hs.values()), len(hs), 0.8)
    L7 = [(b[-1], f) for b, e, f in SL if e == '740']
    s151 = {h for h, f in L7 if f == '151'}
    s90 = {h for h, f in L7 if f == '90'}
    s400 = {h for h, f in L7 if f == '400'}
    j90 = len(s151 & s90) / max(1, len(s151 | s90))
    j400 = len(s151 & s400) / max(1, len(s151 | s400))
    rd.rec('PS10', '151 goes with 90', "Jaccard 151-90 %.3f, 151-400 %.3f (151 heads: %s)" % (j90, j400, ', '.join(sorted(s151))), j90 > j400)
    cc = [(cat[h], f == '90') for h, f in L7 if h in cat]
    rd.mi('PS11', 'the shape calls 90', '740 lines with a categorised head', [a for a, _ in cc], [b for _, b in cc])
    cnt = lambda b: len(b) >= 2 and b[-2] in R.NUMS
    rd.ltl('PS12', '90 heads are not counted', 'counted, 90 lines', [cnt(b) for b, e, f in SL if f == '90'], [cnt(b) for b, e, f in SL if f == '400'])
    fsl = [(s, ty, f) for s, ty, t in FD for b, e, f in suffix_lines([t]) if f in ('90', '400')]
    rd.gtl('PS13', '400 is a tablet suffix', 'tablet, 400 lines', [ty == 'TAB' for s, ty, f in fsl if f == '400'], [ty == 'TAB' for s, ty, f in fsl if f == '90'])
    rd.gtl('PS14', '400 is a Harappa suffix', 'Harappa, 400 lines', [s == 'Harappa' for s, ty, f in fsl if f == '400'], [s == 'Harappa' for s, ty, f in fsl if f == '90'])
    fish = lambda b: any(g in FISH for g in b)
    rd.ltl('PS15', '90 names have no fish', 'fish, 90 bodies', [fish(b) for b, e, f in SL if f == '90'], [fish(b) for b, e, f in SL if f == '400'])
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    top = {h for h, _ in Counter(b[-1] for b, e in ns).most_common(20)}
    sh_ = {b[-1] for b, e, f in SL if f in SUF}
    allh = {b[-1] for b, e in ns}
    rd.gtl('PS16', 'common heads take suffixes', 'top-20, heads with a suffix line', [h in top for h in sh_], [h in top for h in allh - sh_])
    objs = defaultdict(set)
    for r in F:
        for b, e in R.names_in(r):
            objs[(b, e)].add(r['sealid'])
    fsn = {(b, e, f) for r in F for ln in r['seq'] if ln for b, e, f in suffix_lines([tuple(ln)]) if f in ('90', '400')}
    rd.gtl('PS17', '90 names are personal', 'one-off, 90 names', [len(objs[(b, e)]) == 1 for b, e, f in fsn if f == '90'],
           [len(objs[(b, e)]) == 1 for b, e, f in fsn if f == '400'])
    h54 = [b[-1] for b, e, f in SL if e == '520' and f == '400']
    rd.thr('PS18', "'520 400' heads are fish", "fish heads, '520 400' (%s)" % ', '.join(sorted(set(h54))), sum(h in FISH for h in h54), len(h54), 0.5)
    DB = sorted({tuple(t) for t in B})
    k, n = after_end('90', DB)
    rd.thr('PS19', '90 is a suffix only (B)', '90 tokens after an ending', k, n, 0.9)
    LB = [(b[-1], f) for b, e, f in suffix_lines(DB) if e == '740' and f in ('90', '400')]
    o, p = jperm(LB, '90', '400')
    rd.rec('PS20', '90 and 400 take different heads (B)', 'lines %d; Jaccard %.3f; p = %.4f' % (len(LB), o, p), p < 0.05)
    rd.finish()


if __name__ == '__main__':
    main()
