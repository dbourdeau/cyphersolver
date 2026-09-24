"""Hundred-and-ninety-sixth registered prediction set (PREDICTIONS.md, LT1-LT8): decipherment loop 21, the L bench with a
tolerant profile, and the fish-name / 520 signal by place and time. Writes results/predict_test196.md."""
import predict_test13 as T
import rtools as R
from lbench import gb_ok, groups, majority, rows, tolerant_wals
from predict_test178 import depiction
from rtools import fisher_less


def period(p):
    if not p.startswith('Period ') or p == 'Period 3B/C':
        return None
    x = p[7:]
    return 'early' if x[0] in '12' or x.startswith(('3A', '3B')) else ('late' if x[0] in '45' or x.startswith('3C') else None)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-ninety-sixth registered predictions: decipherment loop 21, the L bench repaired and the class signal by place and time', 'predict_test196')
    W, G = rows('wals_profile.tsv'), rows('grambank_profile.tsv')
    wg = groups(W, 'genus', tolerant_wals)
    gg = groups(G, 'family', gb_ok)
    wm, gm = majority(wg), majority(gg)
    ew, eg = 1 - len(wm) / len(wg), 1 - len(gm) / len(gg)
    rd.say('- tolerant WALS: %d genera assessed, %d compatible (%.1f%% excluded); Grambank: %d families, %d compatible (%.1f%% excluded).' % (len(wg), len(wm), 100 * ew, len(gg), len(gm), 100 * eg))
    rd.say('- compatible WALS genera: %s.' % ', '.join(sorted(wm)))
    rd.say()
    ia = [gb_ok(r) for r in G if r['indo_aryan'] == '1' and gb_ok(r) is not None]
    rd.rec('LT1', 'tolerant WALS keeps both candidates', 'Dravidian %s, Indic %s' % ('Dravidian' in wm, 'Indic' in wm), 'Dravidian' in wm and 'Indic' in wm)
    lt2 = 'Dravidian' in gm and 'Indo-European' in gm and sum(ia) > len(ia) / 2 and eg >= 0.5
    rd.rec('LT2', 'Grambank keeps both, excludes half', 'Dravidian %s, Indo-European %s, Indo-Aryan %d of %d; %.1f%% of families excluded' % ('Dravidian' in gm, 'Indo-European' in gm, sum(ia), len(ia), 100 * eg), lt2)
    rd.rec('LT3', 'WALS narrowing', '%.1f%% of %d genera excluded' % (100 * ew, len(wg)), ew >= 0.7)
    dep = depiction()
    by = {}
    for r in F:
        site = r['site'] if r['site'] in ('Mohenjo-daro', 'Harappa') else 'other'
        per = period(recs[r['sealid']][8]) if r['site'] == 'Harappa' and r['sealid'] in recs else None
        for ln in r['seq']:
            if ln:
                by.setdefault(site, set()).add(tuple(ln))
                if per:
                    by.setdefault(per, set()).add(tuple(ln))

    def test(lines):
        ns = [nm for nm in T.names(sorted(lines)) if nm[0] and dep.get(nm[0][-1])]
        f = [e == '520' for b, e in ns if dep[b[-1]] == 'fish']
        o = [e == '520' for b, e in ns if dep[b[-1]] != 'fish']
        p = fisher_less(sum(o), len(o) - sum(o), sum(f), len(f) - sum(f))
        return f, o, p

    res = {}
    for key, grp in (('LT4', 'Mohenjo-daro'), ('LT5', 'Harappa'), ('LT6', 'other')):
        f, o, p = test(by.get(grp, set()))
        res[grp] = (f, o, p)
        ok = p < 0.05 and sum(f) / max(1, len(f)) > sum(o) / max(1, len(o))
        rd.rec(key, 'fish names take 520 more, %s' % grp, 'fish-headed %d of %d (%.0f%%) against other heads %d of %d (%.0f%%); p = %.4f' % (
            sum(f), len(f), 100 * sum(f) / max(1, len(f)), sum(o), len(o), 100 * sum(o) / max(1, len(o)), p), ok)
    pe = {k: test(by.get(k, set())) for k in ('early', 'late')}
    dirs = {k: sum(f) / max(1, len(f)) > sum(o) / max(1, len(o)) for k, (f, o, p) in pe.items()}
    lt7 = all(dirs.values()) and min(p for f, o, p in pe.values()) < 0.05
    rd.rec('LT7', 'early and late Harappa', '; '.join('%s: fish %d/%d, other %d/%d, p = %.4f' % (k, sum(f), len(f), sum(o), len(o), p) for k, (f, o, p) in pe.items()), lt7)
    place = all(r[2] < 0.05 and sum(r[0]) / max(1, len(r[0])) > sum(r[1]) / max(1, len(r[1])) for r in res.values())
    ok = ('Dravidian' in wm and 'Indic' in wm and lt2 and ew >= 0.7) or (place and lt7)
    rd.rec('LT8', 'progress rule', 'L world: %s; class signal everywhere: %s' % ('Dravidian' in wm and 'Indic' in wm and lt2 and ew >= 0.7, place and lt7), ok)
    rd.finish()


if __name__ == '__main__':
    main()
