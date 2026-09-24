"""Per-person ration proportions as evidence for fraction values (after Montecchi 2013 on KH 7a).

On KH 7a, E-NA-SI has VIR 10 followed by CYP+D J, and QA-TI-KI VIR 4 followed by CYP+D B. A constant ration
per man gives J/10 = B/4, so B = 1/5 when J = 1/2. This script looks for the same structure everywhere: a
quantity of persons (an entry whose commodity is VIR or MUL) followed, in the next entry, by a commodity and an
amount. Pairs are grouped by record and by the commodity that follows.

For every group with 2+ pairs, the per-person rates are computed with the Corazza et al. 2021 values. Groups
are reported as consistent (one rate fits all), inconsistent, or informative: one pair contains a sign whose
value is disputed or unknown, and a constant rate with another pair implies a value for it.
"""
from collections import defaultdict
from fractions import Fraction as F
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
READ = json.loads((ROOT / 'reading/reading.json').read_text(encoding='utf-8'))
V = dict(J=F(1, 2), E=F(1, 4), F=F(1, 8), B=F(1, 5), D=F(1, 6), K=F(1, 10), L2=F(1, 20), L3=F(1, 30), L4=F(1, 40),
         L6=F(1, 60), JE=F(3, 4))
PERSONS = ('VIR', 'MUL')


def entries(r):
    by = defaultdict(list)
    for t in r['tokens']:
        by[t['entry']].append(t)
    out = []
    for e in sorted(by):
        ts = by[e]
        com = [re.findall(r'[A-Z]{3,}', t['label'])[0] for t in ts if t['cls'] == 'commodity']
        ints = sum(t['value'] for t in ts if t['cls'] == 'number')
        fr = [s for t in ts if t.get('fraction_signs') for s in t['fraction_signs']]
        dmg = any(t['damaged'] for t in ts)
        out.append({'entry': e, 'commodity': com[0] if com else None, 'label': ' '.join(t['label'] for t in ts)[:60],
                    'int': ints, 'fractions': fr, 'damaged': dmg})
    return out


def value(x):
    """Numeric amount if every fraction sign has a published value, else None."""
    if any(s not in V for s in x['fractions']):
        return None
    return F(x['int']) + sum((V[s] for s in x['fractions']), F(0))


def main():
    groups = defaultdict(list)
    for r in READ['records']:
        es = entries(r)
        for a, b in zip(es, es[1:]):
            if a['commodity'] in PERSONS and a['int'] and not a['fractions'] and b['commodity'] and \
                    b['commodity'] not in PERSONS and (b['int'] or b['fractions']) and not a['damaged'] and not b['damaged']:
                groups[(r['name'], b['commodity'])].append({'persons': a['int'], 'person_entry': a['label'],
                                                            'amount_entry': b['label'], 'int': b['int'],
                                                            'fractions': b['fractions']})
    out = []
    for (rec, com), pairs in groups.items():
        if len(pairs) < 2:
            continue
        rates = [(p, value(p) / p['persons'] if value(p) is not None else None) for p in pairs]
        known = {str(r_) for _, r_ in rates if r_ is not None}
        unknown = [p for p, r_ in rates if r_ is None]
        implied = []
        if len(known) == 1 and unknown:
            rate = F(next(iter(known)))
            for p in unknown:
                target = rate * p['persons'] - p['int'] - sum((V[s] for s in p['fractions'] if s in V), F(0))
                implied.append({'entry': p['amount_entry'], 'unknown_signs': [s for s in p['fractions'] if s not in V],
                                'implied_total_of_unknown_signs': str(target)})
        status = ('informative' if implied else 'consistent' if len(known) == 1 else
                  'inconsistent' if len(known) > 1 else 'no valued pair')
        out.append({'record': rec, 'commodity': com, 'status': status,
                    'pairs': [{'persons': p['persons'], 'amount': p['amount_entry'],
                               'rate_per_person': str(r_) if r_ is not None else None} for p, r_ in rates],
                    'implied': implied})
    out.sort(key=lambda x: ['informative', 'consistent', 'inconsistent', 'no valued pair'].index(x['status']))
    res = {'method': __doc__.strip(), 'groups': out}
    (ROOT / 'reading/fraction_ratios_results.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    for g in out:
        print(f"{g['record']:10} {g['commodity']:5} {g['status']:13}", [(p['persons'], p['amount'], p['rate_per_person']) for p in g['pairs']])
        for i in g['implied']:
            print('        implied:', i)


if __name__ == '__main__':
    main()
