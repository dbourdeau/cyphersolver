"""Sixty-third registered prediction set (PREDICTIONS.md, CN1-CN10): sign 700 and counted signs. Writes
results/predict_test63.md. A 700 token counts as 'inside a name body' when its line is a name line and the token falls
within the body span name_of keeps (heading unit and ending excluded)."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test51 import counted

random.seed(83)


def body_span(t):
    nm = R.name_of(t)
    if not nm:
        return None
    b = nm[0]
    for s in range(len(t) - len(b) + 1):
        if tuple(t[s:s + len(b)]) == b:
            return s, s + len(b)
    return None


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Sixty-third registered predictions: sign 700 and counted signs', 'predict_test63')
    fl = [(r, ln) for r in F for ln in r['seq'] if ln]
    ct = lambda ln: len(ln) >= 2 and ln[-1] == '700' and all(g in R.NUMS for g in ln[:-1])
    tb = [(r['type'], ct(ln)) for r, ln in fl if r['type'] in ('TAB:B', 'TAB:I')]
    a = [c for ty, c in tb if ty == 'TAB:B']
    c = [c for ty, c in tb if ty == 'TAB:I']
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('CN1', 'counts are moulded', 'count tokens, TAB:B %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p < 0.05 and sum(a) / len(a) > sum(c) / len(c))
    val = lambda ln: sum(R.NUMS[g][0] for g in ln[:-1])
    tv = [(r['type'], val(ln)) for r, ln in fl if ct(ln) and r['type'] in ('TAB:B', 'TAB:I')]
    rd.mi('CN2', 'the medium sets the count', 'count tokens on tablets', [a_ for a_, _ in tv], [b_ for _, b_ in tv])
    tc = Counter(tuple(ln) for r, ln in fl if ct(ln))
    rd.thr('CN3', 'counts are stamped', 'distinct count texts on 2+ objects (%s)' % ', '.join(
        '%s x%d' % (' '.join(k), n) for k, n in tc.most_common(5)), sum(n >= 2 for n in tc.values()), len(tc), 0.5)
    toks = [(r, ln, i) for r, ln in fl for i, g in enumerate(ln) if g == '700']
    after = lambda ln, i: i > 0 and ln[i - 1] in R.NUMS
    rd.thr('CN4', '700 is counted', '700 tokens after a numeral', sum(after(ln, i) for _, ln, i in toks), len(toks), 0.8)

    def inside(ln, i):
        sp = body_span(ln)
        return bool(sp) and sp[0] <= i < sp[1]
    na = [(ln, i) for _, ln, i in toks if not after(ln, i)]
    rd.thr('CN5', 'uncounted 700 is a name sign', 'uncounted 700 tokens inside a name body', sum(inside(ln, i) for ln, i in na), len(na), 0.5)
    ins = [(ln, i) for _, ln, i in toks if inside(ln, i)]
    rd.thr('CN6', '700 heads the name', '700 in a body standing last', sum(i == body_span(ln)[1] - 1 for ln, i in ins), len(ins), 0.5)
    dd = [(r, ln) for r, ln in fl if any(x == y == '700' for x, y in zip(ln, ln[1:]))]
    rd.thr('CN7', '700 700 is a Harappa tablet form', 'lines with 700 700 on Harappa tablets',
           sum(r['site'].strip() == 'Harappa' and r['type'].startswith('TAB') for r, _ in dd), len(dd), 0.8)
    kinds = defaultdict(set)
    n_ = Counter()
    for t in AB:
        for x, y in zip(t, t[1:]):
            if x in R.NUMS and y not in R.NUMS:
                kinds[y].add(R.kind(x))
                n_[y] += 1
    s5 = [g for g in n_ if n_[g] >= 5]
    rd.thr('CN8', 'one notation per thing', 'signs counted 5+ times with one kind', sum(len(kinds[g]) == 1 for g in s5), len(s5), 0.6)
    vs = []
    for r, ln, i in toks:
        j = i
        while j > 0 and ln[j - 1] in R.NUMS:
            j -= 1
        if j < i:
            vs.append(sum(R.NUMS[g][0] for g in ln[j:i]))
    rd.thr('CN9', '700 counts two to four', 'values 2-4 (%s)' % dict(sorted(Counter(vs).items())), sum(2 <= v <= 4 for v in vs), len(vs), 0.95)
    md = [(ln, i) for r, ln, i in toks if r['site'].strip() == 'Mohenjo-daro']
    rd.thr('CN10', 'at Mohenjo-daro 700 is a name sign', 'Mohenjo-daro 700 tokens inside a name body', sum(inside(ln, i) for ln, i in md), len(md), 0.6)
    rd.finish()


if __name__ == '__main__':
    main()
