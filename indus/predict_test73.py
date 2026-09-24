"""Seventy-third registered prediction set (PREDICTIONS.md, DN1-DN20): findings recounted on distinct texts. Writes
results/predict_test73.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test41 import dbl
from predict_test44 import nonname
from predict_test53 import lab_perm, rate
from signs import FISH

random.seed(93)


def shuf(items, stat, lower=False, n=R.N // 10):
    obs = sum(map(stat, items))
    c = 0
    for _ in range(n):
        k = 0
        for t in items:
            s = list(t)
            random.shuffle(s)
            k += stat(s)
        c += (k <= obs) if lower else (k >= obs)
    return obs, (c + 1) / (n + 1)


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    rd = R.Round('Seventy-third registered predictions: the findings recounted on distinct texts', 'predict_test73')
    DL = sorted({tuple(t) for t in AB})
    ns = sorted({(b, e) for b, e in T.names(AB) if b})
    rd.say('- distinct lines %d (of %d), distinct names %d (of %d).' % (len(DL), len(AB), len(ns), len(T.names(AB))))
    rd.say()
    rd.mi('DN1', 'the head sets the ending', 'distinct names', [b[-1] for b, e in ns], [e for b, e in ns])
    hc = defaultdict(Counter)
    for b, e in ns:
        hc[b[-1]][e] += 1
    h5 = [h for h in hc if sum(hc[h].values()) >= 5]
    rd.thr('DN2', 'heads fix their ending', 'heads (5+ names) with one ending in 80%+', sum(max(hc[h].values()) / sum(hc[h].values()) >= 0.8 for h in h5), len(h5), 0.8)
    fh = [(b[-1], e) for b, e in ns if b[-1] in FISH]
    rd.mi('DN3', 'each fish head has its ending', 'distinct fish-headed names', [h for h, _ in fh], [e for _, e in fh])
    pre = lambda b, i: i > 0 and b[i - 1] in R.NUMS
    rd.gtl('DN4', 'fish are counted', 'after a numeral, fish body tokens', [pre(b, i) for b, _ in ns for i, g in enumerate(b) if g in FISH],
           [pre(b, i) for b, _ in ns for i, g in enumerate(b) if g not in FISH])
    pv = [(b[i - 1], g) for b, _ in ns for i, g in enumerate(b) if g in FISH and i > 0]
    rd.mi('DN5', 'the neighbour picks the fish', 'fish tokens with a preceding sign', [a for a, _ in pv], [g for _, g in pv])
    bs = sorted({b for b, _ in ns if len(b) >= 3})
    rep = lambda b: any(b[i] == b[j] and b[i] not in R.NUMS for i in range(len(b)) for j in range(i + 2, len(b)))
    o, p = shuf(bs, rep, lower=True)
    rd.rec('DN6', 'names avoid repeats', 'bodies %d; repeats %d; p = %.4f (1,000 shuffles)' % (len(bs), o, p), p < 0.05)
    fol = [(t[i], t[i + 1] == '400') for t in DL for i in range(len(t) - 1) if t[i] in R.END]
    rd.ltl('DN7', '520 does not take 400', 'followed by 400, 520', [x for g, x in fol if g == '520'], [x for g, x in fol if g == '740'])
    nt = [g for t in DL for g in t if g in R.NUMS]
    rd.gtl('DN8', 'the tiered form is for larger numbers', 'tiered, values 5-8', [R.kind(g) == 'tiered' for g in nt if 5 <= R.NUMS[g][0] <= 8],
           [R.kind(g) == 'tiered' for g in nt if 1 <= R.NUMS[g][0] <= 4])
    pr = [(R.kind(x), y) for t in DL for x, y in zip(t, t[1:]) if x in R.NUMS and y not in R.NUMS]
    rd.mi('DN9', 'the sign sets the numeral kind', 'numeral + sign pairs', [k for k, _ in pr], [y for _, y in pr])
    pos = [(R.kind(g), i == 0) for t in DL for i, g in enumerate(t) if g in R.NUMS]
    rd.gtl('DN10', 'long numbers open the line', 'first, long numerals', [f for k, f in pos if k == 'long'], [f for k, f in pos if k == 'short'])
    fm = [t for t in DL if nonname(list(t))]
    slots = [(t, j) for t in fm for j in range(len(t) - 1) if t[j] in R.NUMS and t[j + 1] not in R.NUMS]
    vals = [R.NUMS[t[j]][0] for t, j in slots]
    nxt = [t[j + 1] for t, j in slots]
    obs = len(set(zip(vals, nxt)))
    vv = vals[:]
    le = 0
    for _ in range(R.N):
        random.shuffle(vv)
        le += len(set(zip(vv, nxt))) <= obs
    p = (le + 1) / (R.N + 1)
    rd.rec('DN11', 'number and sign are idioms', 'pairs %d; distinct %d; p = %.4f' % (len(slots), obs, p), p < 0.05)
    res = defaultdict(set)
    wn = [t for t in fm if any(g in R.NUMS for g in t)]
    for t in wn:
        res[tuple(g for g in t if g not in R.NUMS)].add(tuple(R.NUMS[g][0] for g in t if g in R.NUMS))
    k = sum(len(res[tuple(g for g in t if g not in R.NUMS)]) >= 2 for t in wn if any(g not in R.NUMS for g in t))
    rd.thr('DN12', 'the same formula with different numbers', 'distinct numeral formulas sharing their residue', k, len(wn), 0.2)
    num = lambda t: any(g in R.NUMS for g in t)
    nl = [t for t in DL if R.name_of(list(t))]
    rd.gtl('DN13', 'the number opens the formula', 'numeral first, formulas with a numeral', [t[0] in R.NUMS for t in fm if num(t)],
           [t[0] in R.NUMS for t in nl if num(t)])
    o, p = lab_perm([list(t) for t in nl], [list(t) for t in fm], lambda a, b: rate(a) - rate(b), R.N // 10)
    rd.rec('DN14', 'names are the repetitive genre', 'repeat rate names %.3f, formulas %.3f; p = %.4f (1,000 shuffles)' % (
        rate([list(t) for t in nl]), rate([list(t) for t in fm]), p), o > 0 and p < 0.05)
    o, p = shuf(DL, lambda t: len(dbl(list(t))))
    rd.rec('DN15', 'doubling is deliberate', 'doubles %d; p = %.4f (1,000 shuffles)' % (o, p), p < 0.05)
    FL = {(r['site'].strip(), r['type'][:3], tuple(ln)) for r in F for ln in r['seq'] if ln}
    val = lambda t: sum(R.NUMS[g][0] for g in t if g in R.NUMS)
    S = [t for s, ty, t in FL if ty == 'SEA' and nonname(list(t)) and num(t)]
    Tb = [t for s, ty, t in FL if ty == 'TAB' and nonname(list(t)) and num(t)]
    rd.rank('DN16', 'seals count higher', 'seal against tablet values', [val(t) for t in S], [val(t) for t in Tb])
    rd.gtl('DN17', 'seals use the tiered form', 'tiered, seal numerals', [R.kind(g) == 'tiered' for t in S for g in t if g in R.NUMS],
           [R.kind(g) == 'tiered' for t in Tb for g in t if g in R.NUMS])
    items = [(s == 'Harappa', R.lstrat(len(t)), 1 if t[0] in R.NUMS else 0) for s, ty, t in FL if s in ('Harappa', 'Mohenjo-daro') and nonname(list(t))]
    rd.strat('DN18', 'Harappa formulas open with a number', 'Harappa minus Mohenjo-daro', items)
    full = lambda r: '' if recs[r['sealid']][18].strip() in ('', 'None') else recs[r['sealid']][18].strip()
    st = {(tuple(tuple(ln) for ln in r['seq'] if ln), full(r).split(':')[0].strip()) for r in F if r['type'].startswith('SEAL') and full(r) and r['seq']}
    pure = lambda tx: all(R.name_of(list(ln)) for ln in tx)
    rd.gtl('DN19', 'unicorn seals carry pure names', 'pure-name texts, unicorn', [pure(tx) for tx, m in st if m == 'Bull1'], [pure(tx) for tx, m in st if m != 'Bull1'])
    sn = {(b, e, full(r).split(':')[0].strip()) for r in F if r['type'].startswith('SEAL') and full(r) for b, e in R.names_in(r)}
    rd.ltl('DN20', '520 is not the unicorn ending', 'unicorn, distinct seal 520 names', [m == 'Bull1' for b, e, m in sn if e == '520'],
           [m == 'Bull1' for b, e, m in sn if e == '740'])
    rd.finish()


if __name__ == '__main__':
    main()
