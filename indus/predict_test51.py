"""Fifty-first registered prediction set (PREDICTIONS.md, CT1-CT10): the seal count formulas. Writes
results/predict_test51.md."""
import random
from collections import Counter, defaultdict

import predict_test13 as T
import rtools as R
from predict_test43 import sp_perm
from predict_test44 import nonname

random.seed(71)
HEAD = ('817', '820', '861')


def counted(ln):
    """(value, counted sign, index) for each numeral run followed by a non-numeral sign."""
    out = []
    for i in range(1, len(ln)):
        if ln[i] not in R.NUMS and ln[i - 1] in R.NUMS:
            j = i - 1
            while j > 0 and ln[j - 1] in R.NUMS:
                j -= 1
            out.append((sum(R.NUMS[g][0] for g in ln[j:i]), ln[i], i))
    return out


def main():
    A, B, rowsA, recs, F = R.load_all()
    AB = A + B
    head, attr = R.classes(A)
    rd = R.Round('Fifty-first registered predictions: the seal count formulas', 'predict_test51')
    num = lambda t: any(g in R.NUMS for g in t)
    sc = [(r, ln) for r in F if r['type'].startswith('SEAL') for ln in r['seq'] if nonname(ln) and num(ln)]
    rd.say('- seal counts %d.' % len(sc))
    rd.say()
    tmpl = lambda t: t[0] in HEAD and len(t) >= 3 and all(g in R.NUMS for g in t[1:-1]) and t[-1] not in R.NUMS
    rd.thr('CT1', 'a fixed template', 'heading + numeral + sign', sum(tmpl(t) for _, t in sc), len(sc), 0.3)
    cs = [c for _, t in sc for c in counted(t)]
    rd.ltl('CT2', 'the counted sign is not a head', 'head class, counted signs', [s in head for _, s, _ in cs],
           [b[-1] in head for b, _ in T.names(AB) if b])
    vals = defaultdict(set)
    for v, s, _ in cs:
        vals[s].add(v)
    cn = Counter(s for _, s, _ in cs)
    k5 = [s for s in cn if cn[s] >= 5]
    rd.thr('CT3', 'a sign takes many counts', 'signs counted 5+ times with 3+ values (%s)' % ', '.join(
        '%s:%s' % (s, sorted(vals[s])) for s in sorted(k5, key=lambda s: -cn[s])), sum(len(vals[s]) >= 3 for s in k5), len(k5), 0.6)
    bsig = {g for b, _ in T.names(AB) for g in b}
    k3 = [s for s in cn if cn[s] >= 3]
    rd.thr('CT4', 'counted signs are name signs too', 'signs counted 3+ times found in name bodies', sum(s in bsig for s in k3), len(k3), 0.7)
    lv = [(len(t), max(v for v, _, _ in counted(t))) for _, t in sc if counted(t)]
    o, p = sp_perm([a for a, _ in lv], [b for _, b in lv])
    rd.rec('CT5', 'longer counts are larger', 'counts %d; Spearman %.3f; p = %.4f' % (len(lv), o, p), o > 0 and p < 0.05)
    hv = [max(v for v, _, _ in counted(t)) for _, t in sc if counted(t) and t[0] in HEAD]
    uv = [max(v for v, _, _ in counted(t)) for _, t in sc if counted(t) and t[0] not in HEAD]
    rd.rank('CT6', 'headed counts are larger', 'headed against unheaded', hv, uv)
    rd.thr('CT7', 'the counted sign closes the line', 'seal counts ending in their counted sign',
           sum(any(i == len(t) - 1 for _, _, i in counted(t)) for _, t in sc), len(sc), 0.4)
    sn = [r['type'] == 'SEAL:S' for r in F if r['type'].startswith('SEAL') for ln in r['seq'] if R.name_of(ln)]
    rd.gtl('CT8', 'counts are on square seals', 'square seals, seal counts', [r['type'] == 'SEAL:S' for r, _ in sc], sn)
    st = [(r['site'].strip(), c[1]) for r, t in sc if r['site'].strip() in ('Mohenjo-daro', 'Harappa') for c in counted(t)]
    rd.mi('CT9', 'each city counts its own things', 'counted signs', [a for a, _ in st], [b for _, b in st])
    tabc = {c[1] for r in F if r['type'].startswith('TAB') for ln in r['seq'] for c in counted(ln)}
    rd.thr('CT10', 'seals count other things than tablets', 'seal counted tokens of signs also counted on tablets',
           sum(s in tabc for _, s, _ in cs), len(cs), 0.5, above=False)
    rd.finish()


if __name__ == '__main__':
    main()
