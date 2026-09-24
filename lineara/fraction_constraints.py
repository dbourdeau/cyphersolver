"""Test published Linear A fraction values against written order and HT 34.

Evidence (sign identities only; editorial glosses in the corpus are not read):
  * adjacent pairs from fraction_order.py (largest-first writing assumed);
  * HT 104 total: 45 J + 20 J + 29 = 95, so J + J = 1;
  * HT 34 back-references (Younger's reading): line .7 PU F settles
    .4 QA+[?]+PU A, so the remainder F is at most A.
Each item carries a status so that disputed readings can be switched off.
Run fraction_order.py first.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORDER = json.loads((ROOT / 'fraction_order_results.json').read_text(encoding='utf-8'))

# Status of each attested order pair (a written before b). 'firm' unless noted.
NOTES = {
    'E J': ('doubtful', 'ZA 8.4; Corazza et al. 2021 n. 3 call it doubtful; SigLA has no fraction signs for ZA 8'),
    'L E': ('doubtful', 'PH 7b.3, damaged; Corazza et al. 2021 n. 2'),
    'A B': ('disputed', 'KH 86.2: GORILA/lineara and SigLA read A B B; Corazza et al. 2021 read A A'),
    'H K': ('firm', 'HT 34.3: lineara and SigLA agree (A706 then A708 on one line); Younger reads 2 H K'),
    'E B': ('firm', 'KH 9, NI E B'),
}

ARITH = [
    ('HT 104 total', 'firm', lambda v: 2 * v['J'] == 1),
    ('HT 34 PU F <= A (Younger back-reference)', 'interpretive', lambda v: v['F'] <= v['A']),
]

PUBLISHED = {
    'lineara.xyz gloss (Bennett-type)': dict(J=F(1, 2), E=F(1, 4), F=F(1, 8), K=F(1, 16), B=F(1, 3), D=F(1, 5),
                                             A=F(1, 6), H=F(1, 6)),
    'Corazza et al. 2021': dict(J=F(1, 2), E=F(1, 4), F=F(1, 8), H=F(1, 16), A=F(1, 24), B=F(1, 5), D=F(1, 6),
                                K=F(1, 10), L2=F(1, 20), L3=F(1, 30), L4=F(1, 40), L6=F(1, 60)),
    'Corazza et al. 2021, alternative B/D': dict(J=F(1, 2), E=F(1, 4), F=F(1, 8), H=F(1, 16), A=F(1, 24),
                                                 B=F(1, 6), D=F(1, 5), K=F(1, 10), L2=F(1, 20), L3=F(1, 30),
                                                 L4=F(1, 40), L6=F(1, 60)),
}
# Typologically attested values listed by Corazza et al. 2021 (section 2 and Table 7 range)
TYPOLOGICAL = [F(5, 6), F(3, 4), F(2, 3), F(1, 2), F(1, 3), F(1, 4), F(1, 5), F(1, 6), F(1, 8), F(1, 10),
               F(1, 12), F(1, 16), F(1, 20), F(1, 24), F(1, 30), F(1, 32), F(1, 36), F(1, 40), F(1, 48),
               F(1, 60), F(1, 64), F(1, 72), F(1, 84), F(3, 20), F(3, 10), F(2, 5)]
COMPOUND = {'JE': ('J', 'E')}


def value(v, s):
    if s in COMPOUND:
        return sum(v[x] for x in COMPOUND[s])
    return v.get(s)


def evaluate(v, include=('firm',)):
    out = {'order_ok': [], 'order_violated': [], 'order_unknown': [], 'arith': {}, 'cluster_sum_ge_1': []}
    for key, info in ORDER['adjacent_pairs'].items():
        a, b = key.split()
        status, note = NOTES.get(key, ('firm', ''))
        va, vb = value(v, a), value(v, b)
        rec = {'pair': key, 'count': info['count'], 'records': info['records'], 'status': status}
        if va is None or vb is None:
            out['order_unknown'].append(rec)
        elif va > vb:
            out['order_ok'].append(rec)
        else:
            out['order_violated'].append(rec)
    for key, info in ORDER['repeated_sign_pairs'].items():
        a = key.split()[0]
        if a in v and 2 * v[a] >= 1:
            out['cluster_sum_ge_1'].append({'pair': key, 'records': info['records']})
    for name, status, test in ARITH:
        try:
            out['arith'][name] = {'status': status, 'holds': bool(test(v))}
        except KeyError:
            out['arith'][name] = {'status': status, 'holds': None}
    return out


def compound_values(v, free):
    """Values written by attested multi-sign clusters made only of fixed signs."""
    out = set()
    for key in list(ORDER['adjacent_pairs']) + list(ORDER['repeated_sign_pairs']):
        signs = key.split()
        if any(s in free for s in signs) or any(value(v, s) is None for s in signs):
            continue
        out.add(sum(value(v, s) for s in signs))
    for extra in ORDER.get('longer_clusters', []):
        signs = extra.split()
        if not any(s in free for s in signs) and all(value(v, s) is not None for s in signs):
            out.add(sum(value(v, s) for s in signs))
    return out


def feasible_a_h(base, statuses, free=('A', 'H'), uniqueness=False):
    """Values for the free signs (typological list) consistent with the chosen evidence, others fixed.
    uniqueness=True adds Corazza et al.'s constraint 3 against attested compound values too."""
    fixed = {k: x for k, x in base.items() if k not in free}
    taken = set(fixed.values())
    if uniqueness:
        taken |= compound_values(fixed, free)
    ok = []
    for combo in product(TYPOLOGICAL, repeat=len(free)):
        if len(set(combo)) < len(combo) or any(x in taken for x in combo):
            continue  # Corazza et al. constraint 3: one value, one sign
        v = dict(fixed, **dict(zip(free, combo)))
        if any(2 * v[s] >= 1 for s in ('B', 'D') if s in v):
            continue
        r = evaluate(v)
        bad = [x for x in r['order_violated'] if x['status'] in statuses]
        arith_bad = [k for k, x in r['arith'].items() if x['status'] in statuses and x['holds'] is False]
        if not bad and not arith_bad:
            ok.append(tuple(str(x) for x in combo))
    return ok


def main():
    result = {'method': __doc__.strip(), 'notes_on_pairs': {k: {'status': s, 'note': n} for k, (s, n) in NOTES.items()},
              'published': {}, 'feasible_A_H': {}}
    for name, v in PUBLISHED.items():
        r = evaluate(v)
        result['published'][name] = r
        print(f'== {name}')
        print('   order satisfied:', sum(x['count'] for x in r['order_ok']),
              '| violated:', [(x['pair'], x['status'], x['records']) for x in r['order_violated']])
        print('   repeats summing to >= 1:', [(x['pair'], x['records']) for x in r['cluster_sum_ge_1']])
        print('   arithmetic:', {k: x['holds'] for k, x in r['arith'].items()})
    base = {k: x for k, x in PUBLISHED['Corazza et al. 2021'].items() if k not in ('A', 'H')}
    runs = [('firm order only', ('firm',)),
            ('firm + interpretive (HT 34 F<=A)', ('firm', 'interpretive')),
            ('firm + interpretive + disputed (KH 86 A B)', ('firm', 'interpretive', 'disputed'))]
    for free in [('A', 'H'), ('A', 'H', 'K')]:
        for uniq in (False, True):
            for label, statuses in runs:
                ok = feasible_a_h(base if 'K' not in free else PUBLISHED['Corazza et al. 2021'], statuses, free, uniq)
                vals = {s: sorted({c[i] for c in ok}, key=lambda z: F(z)) for i, s in enumerate(free)}
                key = f"free {'/'.join(free)}; uniqueness incl. compounds={uniq}; {label}"
                result['feasible_A_H'][key] = {'solutions': len(ok), 'values': vals, 'sample': ok[:20]}
                print(f'-- {key}: {len(ok)} solutions')
                for s_, vs in vals.items():
                    print(f'   {s_} in', vs)
    (ROOT / 'fraction_constraints_results.json').write_text(json.dumps(result, indent=2, default=str) + '\n',
                                                            encoding='utf-8')


if __name__ == '__main__':
    main()
