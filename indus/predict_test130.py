"""Hundred-and-thirtieth registered prediction set (PREDICTIONS.md, MS1-MS12): material and size. Writes
results/predict_test130.md. Field 13 = material; field 31 = main dimension (mm), inferred from its values."""
import random

import rtools as R
from predict_test43 import sp_perm
from predict_test44 import nonname
from predict_test103 import CL
from predict_test108 import genre

random.seed(150)
HEAD = ('817', '820', '861')
NONE = ('', 'None', '-', 'Unknown')


def two_rank(a, b):
    d1, p1 = R.rank_perm(a, b)
    d2, p2 = R.rank_perm(b, a)
    return min(1, 2 * min(p1, p2))


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-thirtieth registered predictions: material and size', 'predict_test130')
    size = lambda r: float(recs[r['sealid']][31]) if recs[r['sealid']][31].strip() not in ('0', '', '-') else None
    mat = lambda r: recs[r['sealid']][13].strip() if recs[r['sealid']][13].strip() not in ('-', '') else None
    mot = lambda r: '' if recs[r['sealid']][18].strip() in NONE else recs[r['sealid']][18].split(':')[0].strip()
    lines = lambda r: [tuple(ln) for ln in r['seq'] if ln]
    seals = [r for r in F if r['type'].startswith('SEAL') and size(r) and lines(r)]
    rd.say('- seals with a size %d; objects with a material %d.' % (len(seals), sum(1 for r in F if mat(r))))
    rd.say()
    L = lambda r: sum(len(t) for t in lines(r))
    o, p = sp_perm([size(r) for r in seals], [L(r) for r in seals])
    rd.rec('MS1', 'bigger seals say more', 'seals %d; Spearman %.3f; p = %.4f' % (len(seals), o, p), o >= 0.2 and p < 0.05)
    hd = lambda r: any(len(t) >= 3 and t[0] in HEAD and t[1] in ('2', '60', '1') for t in lines(r))
    rd.rank('MS2', 'titled seals are bigger', 'headed against unheaded', [size(r) for r in seals if hd(r)], [size(r) for r in seals if not hd(r)])
    ms = [r for r in seals if mot(r)]
    rd.rank('MS3', 'unicorn seals are bigger', 'unicorn against other', [size(r) for r in ms if mot(r) == 'Bull1'], [size(r) for r in ms if mot(r) != 'Bull1'])
    nm = [size(r) for r in seals if any(genre(t) == 'name' for t in lines(r))]
    cl = [size(r) for r in seals if any(genre(t) == 'closer' for t in lines(r))]
    p = two_rank(nm, cl)
    rd.rec('MS4', 'name and closer seals differ in size', 'medians name %.1f, closer %.1f; two-sided p = %.4f' % (sorted(nm)[len(nm) // 2], sorted(cl)[len(cl) // 2], p), p < 0.05)
    fa = [L(r) for r in F if mat(r) == 'Faience' and lines(r)]
    st = [L(r) for r in F if mat(r) == 'Steatite' and lines(r)]
    rd.rank('MS5', 'faience says less', 'steatite against faience lengths', st, fa)
    tm = [(mat(r), genre(t)) for r in F if r['type'].startswith('TAB') and mat(r) for t in lines(r)]
    rd.mi('MS6', 'tablet material goes with genre', 'tablet lines', [a for a, _ in tm], [b for _, b in tm])
    tb = [mat(r) for r in F if r['type'] == 'TAB:B' and mat(r)]
    rd.thr('MS7', 'moulded tablets are faience', 'TAB:B faience (%s)' % dict(__import__('collections').Counter(tb).most_common(4)), sum(m == 'Faience' for m in tb), len(tb), 0.5)
    ne = [(mat(r) == 'Steatite', e) for r in F if mat(r) for b, e in R.names_in(r) if b]
    a = [e == '520' for s, e in ne if s]
    c = [e == '520' for s, e in ne if not s]
    p = min(1, 2 * min(R.hyper_ge(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c)), R.fisher_less(sum(a), len(a) - sum(a), sum(c), len(c) - sum(c))))
    rd.rec('MS8', 'material and the 520 class', '520, steatite names %s' % R.fl(sum(a), len(a), sum(c), len(c), p), p < 0.05)
    sm = [size(r) for r in seals if r['site'].strip() == 'Mohenjo-daro']
    sh = [size(r) for r in seals if r['site'].strip() == 'Harappa']
    p = two_rank(sm, sh)
    rd.rec('MS9', 'the cities cut different seals', 'medians Mohenjo-daro %.1f, Harappa %.1f; two-sided p = %.4f' % (sorted(sm)[len(sm) // 2], sorted(sh)[len(sh) // 2], p), p < 0.05)
    lv = lambda r: R.level('Harappa', recs[r['sealid']])
    rd.rank('MS10', 'later seals are bigger', 'later against earlier Harappa seals', [size(r) for r in seals if r['site'].strip() == 'Harappa' and lv(r) == 'L'],
            [size(r) for r in seals if r['site'].strip() == 'Harappa' and lv(r) == 'E'])
    allo = [r for r in F if size(r) and lines(r)]
    rd.rank('MS11', 'counts are on small objects', 'name against count objects', [size(r) for r in allo if any(genre(t) == 'name' for t in lines(r))],
            [size(r) for r in allo if any(genre(t) == 'count' for t in lines(r))])
    num = lambda r: any(nonname(list(t)) and any(g in R.NUMS for g in t) for t in lines(r))
    rd.rank('MS12', 'counting seals are bigger', 'numeral-formula against name-only seals', [size(r) for r in seals if num(r)],
            [size(r) for r in seals if not num(r) and any(genre(t) == 'name' for t in lines(r))])
    rd.finish()


if __name__ == '__main__':
    main()
