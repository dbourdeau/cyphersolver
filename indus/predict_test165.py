"""Hundred-and-sixty-fifth registered prediction set (PREDICTIONS.md, CV1-CV10): does Mohenjo-daro converge on Harappa?
Writes results/predict_test165.md."""
import math
import random
from collections import Counter

import predict_test13 as T
import rtools as R
from predict_test108 import genre
from predict_test18 import level

random.seed(185)
N = 1000


def jsd(a, b):
    ta, tb = sum(a.values()), sum(b.values())
    if not ta or not tb:
        return float('nan')
    out = 0.0
    for k in set(a) | set(b):
        p, q = a[k] / ta, b[k] / tb
        m = (p + q) / 2
        if p:
            out += 0.5 * p * math.log2(p / m)
        if q:
            out += 0.5 * q * math.log2(q / m)
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-sixty-fifth registered predictions: does Mohenjo-daro converge on Harappa?', 'predict_test165')
    seals = [r for r in F if r['type'].startswith('SEAL')]
    site = lambda r: recs[r['sealid']][3]
    lv = lambda r: level(site(r), recs[r['sealid']])
    feats = {}
    for r in seals:
        nms = [(b, e) for b, e in R.names_in(r) if b]
        feats[r['sealid']] = {
            'heads': Counter(b[-1] for b, e in nms), 'signs': Counter(r['flat']), 'openers': Counter(b[0] for b, e in nms if len(b) >= 3),
            'len': [len(b) for b, e in nms], 'long': [R.NUMS[g][1] == 'long' for g in r['flat'] if g in R.NUMS],
            'bare': [genre(tuple(ln)) == 'bare' for ln in r['seq'] if ln]}
    md = [r for r in seals if site(r) == 'Mohenjo-daro' and lv(r)]
    ha = [r for r in seals if site(r) == 'Harappa']
    agg = lambda rs, k: sum((feats[r['sealid']][k] for r in rs), Counter())
    lst = lambda rs, k: [x for r in rs for x in feats[r['sealid']][k]]
    rd.say('- Mohenjo-daro seals with a level %d (early %d, late %d); Harappa seals %d.' % (len(md), sum(lv(r) == 'E' for r in md), sum(lv(r) == 'L' for r in md), len(ha)))
    rd.say()

    def perm(stat, rs=md, n=N):
        labs = [lv(r) for r in rs]
        obs = stat(labs)
        ge = 0
        for _ in range(n):
            random.shuffle(labs)
            ge += stat(labs) >= obs
        return obs, (ge + 1) / (n + 1)
    split = lambda labs, rs=md: ([r for r, l_ in zip(rs, labs) if l_ == 'E'], [r for r, l_ in zip(rs, labs) if l_ == 'L'])
    hae = [r for r in ha if lv(r) == 'E']
    HO = agg(hae, 'openers')

    def cv1(labs):
        e, l_ = split(labs)
        ce, cl = agg(e, 'openers'), agg(l_, 'openers')
        te, tl = max(1, sum(ce.values())), max(1, sum(cl.values()))
        ops = sorted(set(ce) | set(cl))
        return T.spearman([HO[o] for o in ops], [cl[o] / tl - ce[o] / te for o in ops])
    o, p = perm(cv1)
    rd.rec('CV1', 'the rising openers are Harappa\'s', 'Spearman %.3f; p = %.4f' % (o, p), o > 0 and p < 0.05)
    for key, k, title, rs in (('CV2', 'heads', 'heads converge', md), ('CV3', 'signs', 'all signs converge', md),
                              ('CV8', 'signs', 'all signs converge on square seals', [r for r in md if r['type'] == 'SEAL:S'])):
        H = agg([r for r in ha if (r['type'] == 'SEAL:S' or key != 'CV8')], k)
        st = lambda labs, rs=rs, k=k, H=H: (lambda e, l_: jsd(agg(e, k), H) - jsd(agg(l_, k), H))(*split(labs, rs))
        labs0 = [lv(r) for r in rs]
        e0, l0 = split(labs0, rs)
        o, p = perm(st, rs)
        rd.rec(key, title, 'JSD early %.3f, late %.3f; difference %+.3f; p = %.4f' % (jsd(agg(e0, k), H), jsd(agg(l0, k), H), o, p), o > 0 and p < 0.05)
    mean = lambda xs: sum(xs) / max(1, len(xs))
    for key, k, title in (('CV4', 'len', 'name length converges'), ('CV5', 'long', 'numeral notation converges')):
        h = mean(lst(ha, k))
        st = lambda labs, k=k, h=h: (lambda e, l_: abs(mean(lst(e, k)) - h) - abs(mean(lst(l_, k)) - h))(*split(labs))
        e0, l0 = split([lv(r) for r in md])
        o, p = perm(st)
        rd.rec(key, title, 'Harappa %.3f; Mohenjo-daro early %.3f, late %.3f; p = %.4f' % (h, mean(lst(e0, k)), mean(lst(l0, k)), p), o > 0 and p < 0.05)
    e0, l0 = split([lv(r) for r in md])
    rd.gtl('CV6', 'bare lines rise at Mohenjo-daro', 'bare lines, late', lst(l0, 'bare'), lst(e0, 'bare'))
    mde = agg(e0, 'signs')
    hal = [r for r in ha if lv(r)]
    st = lambda labs: (lambda e, l_: jsd(agg(e, 'signs'), mde) - jsd(agg(l_, 'signs'), mde))(*split(labs, hal))
    o, p = perm(st, hal)
    rd.rec('CV7', 'Harappa does not move towards Mohenjo-daro', 'difference %+.3f; p = %.4f (holds if p >= 0.05)' % (o, p), p >= 0.05)
    MO, HAo = agg([r for r in seals if site(r) == 'Mohenjo-daro'], 'openers'), agg(ha, 'openers')
    for key, sites in (('CV9', ('Lothal', 'Dholavira')), ('CV10', ('Kalibangan',))):
        S = agg([r for r in seals if site(r) in sites], 'openers')
        rd.rec(key, '%s openers are Harappa-like' % '/'.join(sites), 'openers %d; JSD to Harappa %.3f, to Mohenjo-daro %.3f' % (
            sum(S.values()), jsd(S, HAo), jsd(S, MO)), jsd(S, HAo) < jsd(S, MO))
    rd.finish()


if __name__ == '__main__':
    main()
