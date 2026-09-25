"""Two-hundred-and-twentieth registered prediction set (PREDICTIONS.md, LS1-LS5): decipherment loop 45, the L profile
without prefixes (WALS 26A = 2 only; Grambank GB431 = 0). Writes results/predict_test220.md."""
import rtools as R
from lbench import gb_ok, groups, majority, rows, tolerant_wals, wals_ok


def strict_wals(r, minc=3):
    prof = {'26A': {'2'}, '86A': {'1', '3'}, '87A': {'1', '3'}, '89A': {'1', '3'}}
    return wals_ok(r, prof, minc)


def gb_strict(r):
    o = gb_ok(r)
    if o is None:
        return None
    if r['GB431'] in ('0', '1'):
        return o and r['GB431'] == '0'
    return o


def main():
    rd = R.Round('Two-hundred-and-twentieth registered predictions: decipherment loop 45, no prefixes in the L profile', 'predict_test220')
    W, G = rows('wals_profile.tsv'), rows('grambank_profile.tsv')
    w0, w1 = groups(W, 'genus', tolerant_wals), groups(W, 'genus', strict_wals)
    g0, g1 = groups(G, 'family', gb_ok), groups(G, 'family', gb_strict)
    m0, m1, n0, n1 = majority(w0), majority(w1), majority(g0), majority(g1)
    e = lambda g, m: 1 - len(m) / len(g)
    rd.say('- WALS: tolerant %.1f%% of %d genera excluded, strict %.1f%% of %d; Grambank: %.1f%% of %d families, with GB431 = 0 %.1f%% of %d.' % (
        100 * e(w0, m0), len(w0), 100 * e(w1, m1), len(w1), 100 * e(g0, n0), len(g0), 100 * e(g1, n1), len(g1)))
    rd.say()
    ls1 = e(w1, m1) > e(w0, m0) and 'Dravidian' in m1 and 'Indic' in m1
    rd.rec('LS1', 'strict WALS excludes more, keeps both candidates', '%.1f%% (was %.1f%%); Dravidian %s, Indic %s' % (100 * e(w1, m1), 100 * e(w0, m0), 'Dravidian' in m1, 'Indic' in m1), ls1)
    ls2 = e(g1, n1) > e(g0, n0) and 'Dravidian' in n1 and 'Indo-European' in n1
    rd.rec('LS2', 'Grambank with GB431 = 0 excludes more, keeps both', '%.1f%% (was %.1f%%); Dravidian %s, Indo-European %s' % (100 * e(g1, n1), 100 * e(g0, n0), 'Dravidian' in n1, 'Indo-European' in n1), ls2)
    bw = [(r['name'], strict_wals(r)) for r in W if r['genus'] == 'Burushaski']
    bg = [(r['name'], gb_strict(r)) for r in G if r['family'] in ('Burushaski',) or r['name'] == 'Burushaski']
    ls3 = 'Burushaski' not in m1 and 'Burushaski' not in n1
    rd.rec('LS3', 'Burushaski excluded by both', 'WALS %s; Grambank %s' % (bw, bg), ls3)
    rd.rec('LS4', 'Munda kept by strict WALS', 'Munda compatible: %s' % ('Munda' in m1), 'Munda' in m1)
    rd.rec('LS5', 'progress rule', 'LS1 %s, LS2 %s; Burushaski excluded %s' % (ls1, ls2, ls3), ls1 and ls2)
    rd.finish()


if __name__ == '__main__':
    main()
