"""Change over time with the excavators' periods (fuller ICIT-derived corpus; see icit_full.py).

The records give Mohenjo-daro objects Mackay's Early / Intermediate / Late periods and Harappa objects HARP's
Periods 3B and 3C. Earlier tests had to use object type as the clock (seventh pass).

PD1 Per site, earlier against later: objects, mean signs, share of name lines ending in 520, the heading formula,
    740 + 90 against 740 + 400, stroke numerals.
PD2 Grammar against names: Jensen-Shannon divergence between earlier and later of (a) the grammatical signs
    (headings, endings, second slot, stroke numerals) and (b) all other signs (the names), each against 500
    permutations of the period labels among objects (z-score). Stable grammar with changing names is what a language
    in use does; changing grammar would point to a change of convention.

Usage: python periods.py path/to/icit_full_records_indusscript_net.csv
Writes results/periods.md.
"""
import csv
import math
import os
import random
import statistics
import sys
from collections import Counter

import icit_full
from numerals import NUMS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
GRAM = {'817', '820', '861', '740', '520', '400', '90', '151'} | set(NUMS)


def say(s=''):
    OUT.append(s)
    print(s)


def jsd(a, b):
    na, nb = sum(a.values()), sum(b.values())
    if not na or not nb:
        return 0.0
    out = 0.0
    for g in set(a) | set(b):
        pa, pb = a[g] / na, b[g] / nb
        m = (pa + pb) / 2
        out += 0.5 * (pa * math.log2(pa / m) if pa else 0) + 0.5 * (pb * math.log2(pb / m) if pb else 0)
    return out


def stats(rs):
    n = len(rs)
    lines = [ln for r in rs for ln in r['seq'] if len(ln) >= 2]
    e740 = e520 = 0
    s90 = s400 = 0
    for t in lines:
        if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
            e = t[-2]
            s90 += t[-2] == '740' and t[-1] == '90'
            s400 += t[-2] == '740' and t[-1] == '400'
        elif t[-1] in ('740', '520'):
            e = t[-1]
        else:
            continue
        e740 += e == '740'
        e520 += e == '520'
    head = sum(1 for r in rs if len(r['flat']) >= 3 and r['flat'][0] in ('817', '820', '861') and r['flat'][1] in ('2', '60', '1'))
    num = sum(1 for r in rs if any(g in NUMS for g in r['flat']))
    return ('%d objects, mean %.1f signs, 520 on %.1f%% of name lines (%d/%d), heading %.1f%%, 740+90 %d / 740+400 %d, '
            'a stroke numeral on %.0f%%' % (n, sum(len(r['flat']) for r in rs) / max(n, 1), 100 * e520 / max(1, e740 + e520),
                                           e520, e740 + e520, 100 * head / max(n, 1), s90, s400, 100 * num / max(n, 1)))


def divergence(early, late, rng):
    core = {'817', '820', '861', '740', '520', '400', '90', '151'}
    sets = {'headings and endings': lambda g: g in core, 'stroke numerals': lambda g: g in NUMS,
            'name signs': lambda g: g not in GRAM}

    def dist(rs, f):
        return Counter(g for r in rs for g in r['flat'] if f(g))
    out = {}
    both = early + late
    for lab, f in sets.items():
        obs = jsd(dist(early, f), dist(late, f))
        sims = []
        for _ in range(500):
            rng.shuffle(both)
            sims.append(jsd(dist(both[:len(early)], f), dist(both[len(early):], f)))
        sd = statistics.pstdev(sims) or 1e-9
        out[lab] = (obs, (obs - statistics.mean(sims)) / sd, sum(1 for s in sims if s >= obs) / 500)
    return out


def main(path):
    rng = random.Random(137)
    recs = {rec[0]: rec for rec in icit_full.records(path)}
    rows = icit_full.objects(path, intact_only=True)
    say('# Change over time with the excavators\' periods')
    say()
    groups = []
    md = [r for r in rows if r['site'] == 'Mohenjo-daro' and r['flat']]
    md_e = [r for r in md if recs[r['sealid']][9].strip().startswith(('Early', 'Interm'))]
    md_l = [r for r in md if recs[r['sealid']][9].strip().startswith('Late')]
    groups.append(('Mohenjo-daro', 'Early + Intermediate', md_e, 'Late', md_l))
    ha = [r for r in rows if r['site'] == 'Harappa' and r['flat'] and recs[r['sealid']][9].strip() == '3']
    ha_b = [r for r in ha if recs[r['sealid']][10].strip() in ('B', 'B?')]
    ha_c = [r for r in ha if recs[r['sealid']][10].strip() == 'C']
    groups.append(('Harappa', 'Period 3B', ha_b, 'Period 3C', ha_c))
    for site, le, e, ll, l in groups:
        say('## %s' % site)
        say()
        say('- PD1 %s: %s.' % (le, stats(e)))
        say('- PD1 %s: %s.' % (ll, stats(l)))
        d = divergence(e, l, rng)
        say('- PD2 divergence earlier / later: %s.' % '; '.join(
            '%s %.3f bits (z %.1f, permutations as large %.3f)' % (k, v[0], v[1], v[2]) for k, v in d.items()))
 
        ce = Counter(g for r in e for g in set(r['flat']) if g not in GRAM)
        cl = Counter(g for r in l for g in set(r['flat']) if g not in GRAM)
        ne_, nl_ = len(e), len(l)
        diff = sorted(((cl[g] / nl_ - ce[g] / ne_), g) for g in set(ce) | set(cl) if ce[g] + cl[g] >= 8)
        say('- name signs that gain most in the later level (share of objects, earlier -> later): %s; that lose most: %s.' % (
            ', '.join('%s %.0f%% -> %.0f%%' % (g, 100 * ce[g] / ne_, 100 * cl[g] / nl_) for d_, g in diff[::-1][:5]),
            ', '.join('%s %.0f%% -> %.0f%%' % (g, 100 * ce[g] / ne_, 100 * cl[g] / nl_) for d_, g in diff[:5])))
        say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'periods.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
