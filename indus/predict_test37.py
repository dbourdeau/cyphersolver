"""Thirty-seventh registered prediction set (PREDICTIONS.md, RG1-RG10): regional name habits. Writes
results/predict_test37.md."""
import random
from collections import Counter

import rtools as R

random.seed(57)


def main():
    A, B, rowsA, recs, F = R.load_all()
    rd = R.Round('Thirty-seventh registered predictions: regional name habits', 'predict_test37')
    seals = [r for r in F if r['type'].startswith('SEAL') and R.region(r['site']) and R.names_in(r)]
    sn = [(R.region(r['site']), r['site'].strip(), R.names_in(r)[0]) for r in seals]
    rd.mi('RG1', 'the head depends on the region', 'seal names', [g for g, _, _ in sn], [n[0][-1] for _, _, n in sn])
    rd.mi('RG2', 'the first sign depends on the region', 'seal names', [g for g, _, _ in sn], [n[0][0] for _, _, n in sn])
    rd.rank('RG3', 'Gujarat names are shorter', 'Sindh against Gujarat name lengths',
            [len(n[0]) for g, _, n in sn if g == 'sindh'], [len(n[0]) for g, _, n in sn if g == 'gujarat'])
    items = [(R.region(r['site']) == 'sindh', R.lstrat(len(ln)), 1 if R.headed(ln) else 0) for r in F
             if r['type'].startswith('SEAL') and R.region(r['site']) in ('sindh', 'gujarat') for ln in r['seq'] if len(ln) >= 3]
    rd.strat('RG4', 'Gujarat seals lack the heading', 'Sindh minus Gujarat', items)
    two = {n[0][-1] for _, s, n in sn if s in ('Mohenjo-daro', 'Harappa')}
    gu = [n[0][-1] not in two for g, _, n in sn if g == 'gujarat']
    rd.thr('RG5', 'Gujarat has heads of its own', 'Gujarat names with a head unseen in the two cities', sum(gu), len(gu), 0.3)
    hr = {}
    for g, _, n in sn:
        hr.setdefault(n[0][-1], Counter())[g] += 1
    only = [h for h, c in hr.items() if sum(c.values()) >= 5 and len(c) == 1]
    rd.rec('RG6', 'region-only heads', 'heads with 5+ names in one region only: %d (%s)' % (
        len(only), ', '.join('%s %s' % (h, dict(hr[h])) for h in only[:8])), len(only) >= 3)
    nums = [(R.region(r['site']), R.kind(g)) for r in F if R.region(r['site']) for g in r['flat'] if g in R.NUMS]
    rd.mi('RG7', 'notation depends on the region', 'numerals', [a for a, _ in nums], [b for _, b in nums])
    rd.gtl('RG8', 'Kalibangan names are 520 names', '520, Kalibangan seal names',
           [n[1] == '520' for _, s, n in sn if s == 'Kalibangan'], [n[1] == '520' for _, s, n in sn if s == 'Harappa'])
    rd.rank('RG9', 'Dholavira texts are longer', 'Dholavira against other Gujarat texts',
            [len(r['flat']) for r in F if r['site'].strip() == 'Dholavira'],
            [len(r['flat']) for r in F if R.region(r['site']) == 'gujarat' and r['site'].strip() != 'Dholavira'])
    md = {n[0][-1] for _, s, n in sn if s == 'Mohenjo-daro'}
    rd.gtl('RG10', 'neighbours share heads', 'head seen at Mohenjo-daro, Chanhu-daro names',
           [n[0][-1] in md for _, s, n in sn if s == 'Chanhu-daro'], [n[0][-1] in md for _, s, n in sn if s == 'Lothal'])
    rd.finish()


if __name__ == '__main__':
    main()
