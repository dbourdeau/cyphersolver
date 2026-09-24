"""Seventy-eighth registered prediction set (PREDICTIONS.md, FG1-FG20): the grammar of the formulas. Writes
results/predict_test78.md. Counts over distinct lines."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test44 import nonname

random.seed(98)


def parse(t):
    """(pre, [(value, item, index)]) for a line with a numeral, else None."""
    t = list(t)
    first = next((i for i, g in enumerate(t) if g in R.NUMS), None)
    if first is None:
        return None
    runs = []
    for i in range(1, len(t)):
        if t[i] not in R.NUMS and t[i - 1] in R.NUMS:
            j = i - 1
            while j > 0 and t[j - 1] in R.NUMS:
                j -= 1
            runs.append((sum(R.NUMS[g][0] for g in t[j:i]), t[i], i))
    return tuple(t[:first]), runs


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Seventy-eighth registered predictions: the grammar of the formulas', 'predict_test78')

    def setup(lines):
        ns = {(b, e) for b, e in T.names(lines) if b}
        fl = [t for t in sorted({tuple(t) for t in lines}) if nonname(list(t)) and parse(t)]
        return {b for b, e in ns}, {b[-1] for b, e in ns}, [(t, parse(t)) for t in fl]
    bodies, heads, P = setup(AB)
    withpre = [(t, pre, runs) for t, (pre, runs) in P if pre]
    rd.say('- numeral formulas %d; with a pre %d.' % (len(P), len(withpre)))
    rd.say()
    rd.thr('FG1', 'the pre is a name', 'pres that are name bodies', sum(pre in bodies for t, pre, runs in withpre), len(withpre), 0.2)

    def fg2(wp, hd, key, lab):
        x = y = 0
        for t, pre, runs in wp:
            if runs:
                a, c = pre[-1] in hd, runs[0][1] in hd
                x += a and not c
                y += c and not a
        p = R.binom_ge(x, x + y)
        rd.rec(key, 'the pre ends in a head%s' % lab, 'pre only %d, item only %d; p = %.4f' % (x, y, p), x > y and p < 0.05)

    def fg3(wp, key, lab):
        pi = [(pre[-1], runs[0][1]) for t, pre, runs in wp if runs]
        rd.mi(key, 'the pre selects the item%s' % lab, 'formulas', [a for a, _ in pi], [b for _, b in pi])
    fg2(withpre, heads, 'FG2', '')
    fg3(withpre, 'FG3', '')
    pi = defaultdict(set)
    pc = Counter()
    for t, pre, runs in withpre:
        pc[pre] += 1
        if runs:
            pi[pre].add(runs[0][1])
    rep = [p_ for p_ in pc if pc[p_] >= 2]
    rd.thr('FG4', 'a header takes many items', 'repeated pres with 2+ items', sum(len(pi[p_]) >= 2 for p_ in rep), len(rep), 0.5)
    rd.thr('FG5', 'pres end in heads', 'pres ending in a name head', sum(pre[-1] in heads for t, pre, runs in withpre), len(withpre), 0.6)
    FD = {(r['type'][:3], tuple(ln)) for r in F for ln in r['seq'] if ln and nonname(ln) and parse(ln)}
    sp = [(ty, parse(t)[0]) for ty, t in FD if ty in ('SEA', 'TAB')]
    rd.gtl('FG6', 'seal formulas have a header', 'pre, seal formulas', [bool(p_) for ty, p_ in sp if ty == 'SEA'], [bool(p_) for ty, p_ in sp if ty == 'TAB'])
    rd.gtl('FG7', 'seal headers are names', 'pre is a name, seal formulas', [p_ in bodies for ty, p_ in sp if ty == 'SEA' and p_],
           [p_ in bodies for ty, p_ in sp if ty == 'TAB' and p_])

    def fg8(Pl, key, lab):
        vi = [(min(v, 8), it) for t, (pre, runs) in Pl for v, it, i in runs]
        rd.mi(key, 'the item sets the count%s' % lab, 'counted items', [it for _, it in vi], [v for v, _ in vi])
    fg8(P, 'FG8', '')
    bsig = {g for b in bodies for g in b}
    items = [it for t, (pre, runs) in P for v, it, i in runs]
    pres = [g for t, (pre, runs) in P for g in pre if g not in R.NUMS]
    rd.gtl('FG9', 'items are formula words', 'formula-only, item tokens', [g not in bsig for g in items], [g not in bsig for g in pres])
    after = [t[i + 1] for t, (pre, runs) in P for v, it, i in runs if i + 1 < len(t)]
    rd.thr('FG10', 'the item is closed off', 'signs after the item that are 400, 90, 151 or numerals (%s)' % ', '.join(
        '%s x%d' % kv for kv in Counter(after).most_common(5)), sum(g in ('400', '90', '151') or g in R.NUMS for g in after), len(after), 0.3)
    b400 = [t[-2] for t, _ in P if len(t) >= 2 and t[-1] == '400' and t[-2] not in R.NUMS]
    rd.thr('FG11', 'few things are received', 'three commonest items before a final 400 (%s)' % ', '.join('%s x%d' % kv for kv in Counter(b400).most_common(3)),
           sum(n for _, n in Counter(b400).most_common(3)), len(b400), 0.5)
    iv = defaultdict(set)
    ic = Counter()
    for t, (pre, runs) in P:
        for v, it, i in runs:
            iv[it].add(v)
            ic[it] += 1
    i3 = [it for it in ic if ic[it] >= 3]
    rd.thr('FG12', 'items take many counts', 'items counted 3+ times with 3+ values', sum(len(iv[it]) >= 3 for it in i3), len(i3), 0.5)
    FS = {(r['site'].strip(), tuple(ln)) for r in F for ln in r['seq'] if ln and nonname(ln) and parse(ln)}
    vs = defaultdict(set)
    for s, t in FS:
        if s in ('Harappa', 'Mohenjo-daro'):
            for v, it, i in parse(t)[1]:
                vs[(v, it)].add(s)
    rd.thr('FG13', 'counts are shared between the cities', '(value, item) types at both', sum(len(x) == 2 for x in vs.values()), len(vs), 0.3)
    two = [(runs[0], runs[1]) for t, (pre, runs) in P if len(runs) >= 2]
    rd.thr('FG14', 'lists hold different things', 'two-run formulas with different items', sum(a[1] != b[1] for a, b in two), len(two), 0.9)
    x = sum(a[0] > b[0] for a, b in two)
    y = sum(a[0] < b[0] for a, b in two)
    p = R.binom_ge(x, x + y)
    rd.rec('FG15', 'lists run large to small', 'first larger %d, smaller %d; p = %.4f' % (x, y, p), x > y and p < 0.05)
    fi = [a[1] for a, b in two]
    si = [b[1] for a, b in two]
    rec_ = lambda s_: sum(n >= 2 for n in Counter(zip(fi, s_)).values())
    obs = rec_(si)
    ss = si[:]
    ge = 0
    for _ in range(R.N):
        random.shuffle(ss)
        ge += rec_(ss) >= obs
    p = (ge + 1) / (R.N + 1)
    rd.rec('FG16', 'lists pair set items', 'two-run formulas %d; item pairs in 2+ formulas %d; p = %.4f' % (len(two), obs, p), p < 0.05)
    bB, hB, PB = setup(B)
    wB = [(t, pre, runs) for t, (pre, runs) in PB if pre]
    fg2(wB, hB, 'FG17', ' (B)')
    fg3(wB, 'FG18', ' (B)')
    for key, site in (('FG19', 'Harappa'), ('FG20', 'Mohenjo-daro')):
        fg8([(t, parse(t)) for s, t in FS if s == site], key, ' (%s)' % site)
    rd.finish()


if __name__ == '__main__':
    main()
