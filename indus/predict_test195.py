"""Hundred-and-ninety-fifth registered prediction set (PREDICTIONS.md, LW1-LW6): decipherment loop 20, the L bench
against the world's languages (lbench.py). Writes results/predict_test195.md."""
import rtools as R
from lbench import GB_CORE, WALS_CLASS, WALS_CORE, gb_ok, groups, rows, share_excluded, wals_ok


def main():
    rd = R.Round('Hundred-and-ninety-fifth registered predictions: decipherment loop 20, the L bench against the world', 'predict_test195')
    W, G = rows('wals_profile.tsv'), rows('grambank_profile.tsv')
    wg = groups(W, 'genus', lambda r: wals_ok(r, WALS_CORE))
    wgc = groups(W, 'genus', lambda r: wals_ok(r, WALS_CLASS))
    gf = groups(G, 'family', gb_ok)
    gfc = groups(G, 'family', lambda r: gb_ok(r, True))
    rd.say('- WALS: %d genera assessed, %.1f%% excluded (core), %.1f%% with class; Grambank: %d families assessed, %.1f%% excluded (core), %d with class, %.1f%% excluded.'
           % (len(wg), 100 * share_excluded(wg), 100 * share_excluded(wgc), len(gf), 100 * share_excluded(gf), len(gfc), 100 * share_excluded(gfc)))
    comp = sorted(k for k, v in gfc.items() if any(v))
    rd.say('- Grambank families compatible with core + class: %s.' % ', '.join(comp))
    rd.say('- WALS genera compatible (core): %s.' % ', '.join(sorted(k for k, v in wg.items() if any(v))))
    rd.say()
    rd.rec('LW1', 'Grambank replicates the narrowing', 'core profile excludes %.1f%% of %d Glottolog families (WALS %.1f%% of %d genera)' % (100 * share_excluded(gf), len(gf), 100 * share_excluded(wg), len(wg)), share_excluded(gf) >= 0.5)
    dw = [(r['name'], wals_ok(r, WALS_CORE)) for r in W if r['family'] == 'Dravidian']
    iw = [(r['name'], wals_ok(r, WALS_CORE)) for r in W if r['genus'] == 'Indic']
    dg = [(r['name'], gb_ok(r)) for r in G if r['family'] == 'Dravidian']
    ig = [(r['name'], gb_ok(r)) for r in G if r['indo_aryan'] == '1']
    bad = [n for n, o in dw + iw + dg + ig if o is False]
    rd.say('- assessed: WALS Dravidian %d, Indic %d; Grambank Dravidian %d, Indo-Aryan %d.' % tuple(sum(o is not None for n, o in x) for x in (dw, iw, dg, ig)))
    rd.rec('LW2', 'both candidates compatible', 'incompatible Dravidian / Indo-Aryan languages: %s' % (', '.join(bad) or 'none'), not bad)
    rate = lambda x: sum(o for n, o in x if o is not None) / max(1, sum(o is not None for n, o in x))
    rd.rec('LW3', 'the core profile does not separate them', 'compatible: WALS Dravidian %.2f, Indic %.2f; Grambank Dravidian %.2f, Indo-Aryan %.2f' % (rate(dw), rate(iw), rate(dg), rate(ig)),
           rate(dw) == rate(iw) and rate(dg) == rate(ig))
    byname = {r['name']: r for r in G}
    dec = {n: gb_ok(byname[n], True) for n in ('Turkish', 'Japanese', 'Basque') if n in byname}
    keep = [(r['name'], gb_ok(r, True)) for r in G if r['family'] == 'Dravidian' or r['indo_aryan'] == '1']
    lost = [n for n, o in keep if o is False]
    rd.rec('LW4', 'the class variant drops the decoys, keeps the candidates', 'decoys %s; candidates dropped: %s' % (dec, ', '.join(lost) or 'none'),
           all(v is False for v in dec.values()) and len(dec) == 3 and not lost)
    fr = 1 - share_excluded(gfc)
    rd.rec('LW5', 'few families pass core + class', '%d of %d families compatible (%.1f%%)' % (len(comp), len(gfc), 100 * fr), fr <= 0.10)
    ok = share_excluded(gf) >= 0.5 and not bad
    rd.rec('LW6', 'progress rule', 'LW1 %s, LW2 %s' % (share_excluded(gf) >= 0.5, not bad), ok)
    rd.finish()


if __name__ == '__main__':
    main()
