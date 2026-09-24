"""Hundred-and-fifty-third registered prediction set (PREDICTIONS.md, WC1-WC5): capture-recapture inside one city.
Writes results/predict_test153.md."""
import rtools as R
from predict_test18 import level
from predict_test140 import major
from predict_test147 import chapman


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Hundred-and-fifty-third registered predictions: capture-recapture inside one city', 'predict_test153')
    seals = [r for r in F if r['type'].startswith('SEAL')]

    def catch(site, lab):
        nm, hd = {}, {}
        for r in seals:
            if recs[r['sealid']][3] != site:
                continue
            k = lab(r)
            if k:
                for b, e in R.names_in(r):
                    if b:
                        nm.setdefault(k, set()).add((b, e))
                        hd.setdefault(k, set()).add(b[-1])
        return nm, hd

    def run(key, title, site, lab, a, b, what, hi):
        nm, hd = catch(site, lab)
        d = nm if what == 'names' else hd
        x, y = d.get(a, set()), d.get(b, set())
        obs = len(x | y)
        lp = chapman(len(x), len(y), len(x & y))
        ok = lp >= 3 * obs if hi else lp <= 1.5 * obs
        rd.rec(key, title, '%s %s: %s %d, %s %d, both %d, together %d; estimate %.0f (%.2fx); threshold %s' % (
            site, what, a, len(x), b, len(y), len(x & y), obs, lp, lp / max(1, obs), 'at least 3x' if hi else 'at most 1.5x'), ok)
    ar = lambda r: major(recs[r['sealid']][4])
    lv = lambda s: (lambda r: level(s, recs[r['sealid']]))
    run('WC1', 'names, DK against HR', 'Mohenjo-daro', ar, 'DK', 'HR', 'names', True)
    run('WC2', 'names, early against late', 'Mohenjo-daro', lv('Mohenjo-daro'), 'E', 'L', 'names', True)
    run('WC3', 'heads, DK against HR', 'Mohenjo-daro', ar, 'DK', 'HR', 'heads', False)
    run('WC4', 'heads, early against late', 'Mohenjo-daro', lv('Mohenjo-daro'), 'E', 'L', 'heads', False)
    run('WC5', 'names, Harappa early against late', 'Harappa', lv('Harappa'), 'E', 'L', 'names', True)
    rd.finish()


if __name__ == '__main__':
    main()
