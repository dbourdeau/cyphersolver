"""Hundred-and-thirty-third registered prediction set (PREDICTIONS.md, PH1-PH10): the physical findings within each
city. Writes results/predict_test133.md."""
from collections import Counter

import rtools as R
from predict_test43 import sp_perm

NONE = ('', 'None', '-', 'Unknown')
CITY = ('Mohenjo-daro', 'Harappa')


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-thirty-third registered predictions: the physical findings within each city', 'predict_test133')
    size = lambda r: float(recs[r['sealid']][31]) if recs[r['sealid']][31].strip() not in ('0', '', '-') else None
    mat = lambda r: recs[r['sealid']][13].strip() if recs[r['sealid']][13].strip() not in ('-', '') else None
    mot = lambda r: '' if recs[r['sealid']][18].strip() in NONE else recs[r['sealid']][18].split(':')[0].strip()
    lines = lambda r: [tuple(ln) for ln in r['seq'] if ln]
    L = lambda r: sum(len(t) for t in lines(r))
    grp = {'Mohenjo-daro': lambda s: s == 'Mohenjo-daro', 'Harappa': lambda s: s == 'Harappa', 'small sites': lambda s: s not in CITY}
    for key, g in (('PH1', 'Mohenjo-daro'), ('PH2', 'Harappa'), ('PH3', 'small sites')):
        ss = [r for r in F if r['type'].startswith('SEAL') and size(r) and lines(r) and grp[g](r['site'].strip())]
        o, p = sp_perm([size(r) for r in ss], [L(r) for r in ss])
        rd.rec(key, 'bigger seals say more (%s)' % g, 'seals %d; Spearman %.3f; p = %.4f' % (len(ss), o, p), o >= 0.2 and p < 0.05)
    for key, g in (('PH4', 'Mohenjo-daro'), ('PH5', 'Harappa')):
        rc = [not mot(r) for r in F if r['type'] == 'SEAL:R' and grp[g](r['site'].strip())]
        sq = [not mot(r) for r in F if r['type'] == 'SEAL:S' and grp[g](r['site'].strip())]
        rd.gtl(key, 'rectangular seals are pictureless (%s)' % g, 'no motif, rectangular', rc, sq)
    for key, g in (('PH6', 'Mohenjo-daro'), ('PH7', 'Harappa')):
        ne = [(mat(r) == 'Steatite', e) for r in F if mat(r) and grp[g](r['site'].strip()) for b, e in R.names_in(r) if b]
        rd.gtl(key, '520 is a steatite class (%s)' % g, '520, steatite names', [e == '520' for s, e in ne if s], [e == '520' for s, e in ne if not s])
    tb = [mat(r) for r in F if r['type'] == 'TAB:B' and mat(r) and r['site'].strip() == 'Harappa']
    rd.thr('PH8', 'Harappa moulded tablets are faience', 'faience (%s)' % dict(Counter(tb).most_common(3)), sum(m == 'Faience' for m in tb), len(tb), 0.5)
    for key, g in (('PH9', 'Mohenjo-daro'), ('PH10', 'Harappa')):
        fa = [L(r) for r in F if mat(r) == 'Faience' and lines(r) and grp[g](r['site'].strip())]
        st = [L(r) for r in F if mat(r) == 'Steatite' and lines(r) and grp[g](r['site'].strip())]
        rd.rank(key, 'faience says less (%s)' % g, 'steatite against faience', st, fa)
    rd.finish()


if __name__ == '__main__':
    main()
