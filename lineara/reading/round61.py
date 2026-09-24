"""Round 61 (saturation loop 3): list types and the sealing system. BH at 5% across the ten.

Q1  Term-headed tablets record larger amounts (mean log amount per tablet) than other tablets.
Q2  Term-headed tablets carry fractions more often.
Q4  Single signs on sealings differ by site (sites with 10+ sealing signs).
Q5  Sealing signs are oil-ligature syllables (KI, U, MI, DI, TA, NE, E, RI, ME, TU, QE, RA, A) more often than
    tablet single signs are.
Q7  Khania's descriptor words also occur at Haghia Triada more often than Khania's name words do.
Q8  Tablets with a total carry name entries more often than descriptor entries (share of entries in the name slot).
Q10 Descriptor entries have an amount of 1 less often than name entries.
Q11 At Haghia Triada, sealing signs match the initial signs of tablet words more often than tablet single signs do.
Q12 At Haghia Triada, roundels and nodules use different single signs.
Q13 Tablets with descriptor entries are single-commodity more often than tablets without.
"""
from collections import Counter, defaultdict
from math import log
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round59 as N  # noqa: E402
import round60 as PP  # noqa: E402
import round50 as HV  # noqa: E402

B, X = R.B, R.X
TOK, DESC, NAME, DSET, NSET = N.TOK, N.DESC, N.NAME, PP.DSET, PP.NSET
SYL = re.compile(r'^[A-Z]{1,2}[0-9]?$')


def heads():
    out = {}
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        for t in r['tokens']:
            if t['cls'] in N.WORD and t.get('function') == 'heading':
                out.setdefault(X.whole(r['name']), t['label'])
                break
    return out


HEADS = heads()


def tablet_stats():
    st = defaultdict(lambda: {'q': [], 'frac': False, 'com': set(), 'desc': 0, 'name': 0, 'kuro': False})
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        k = X.whole(r['name'])
        for t in r['tokens']:
            if t['cls'] == 'number':
                st[k]['q'].append(t['value'])
            if t['cls'].startswith('fraction'):
                st[k]['frac'] = True
            if t['cls'] == 'commodity':
                m = re.findall(r'[A-Z]{3,}', t['label'])
                if m:
                    st[k]['com'].add(m[0])
            if t['label'] in ('KU-RO', 'PO-TO-KU-RO'):
                st[k]['kuro'] = True
    for x in TOK:
        st[X.whole(x['rec'])][x['slot']] += 1
    return st


ST = tablet_stats()


def Q1():
    items = [(HEADS[k] in DSET, sum(log(q) for q in ST[k]['q'] if q > 0) / len([q for q in ST[k]['q'] if q > 0])) for k in HEADS if any(q > 0 for q in ST[k]['q'])]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'Term-headed tablets record larger amounts', {'term_headed': a, 'other': b, 'p': round(p, 4)}, {}


def Q2():
    items = [(HEADS[k] in DSET, ST[k]['frac']) for k in HEADS]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'Term-headed tablets carry fractions more often', {'term_headed': a, 'other': b, 'p': round(p, 4)}, {}


def sealing_signs():
    out = []
    for r in B.READ['records']:
        if r['support'] in B.SEAL:
            for t in r['tokens']:
                if t['cls'] == 'single-sign' and SYL.match(t['label']):
                    out.append((r['site'], r['support'], t['label']))
    return out


SEALS = sealing_signs()


def Q4():
    c = Counter(s for s, _, _ in SEALS)
    pairs = [(s, sg) for s, _, sg in SEALS if c[s] >= 10]
    real, p, nm = R.assoc(pairs)
    return p, 'Sealing signs differ by site', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'sites': dict(Counter(s for s, _ in pairs))}, {}


def Q5():
    tab = [t['label'] for r in B.READ['records'] if r['support'] in B.ADMIN for t in r['tokens'] if t['cls'] == 'single-sign' and SYL.match(t['label'])]
    items = [('seal', s) for _, _, s in SEALS] + [('tab', s) for s in tab]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0] == 'seal', lambda x: x[1] in HV.OIL_ADJ)
    return p, 'Sealing signs are oil-ligature syllables more often than tablet single signs', {'seal': a, 'tablet': b, 'p': round(p, 4)}, {}


def Q7():
    kh = {x['label']: x['slot'] for x in TOK if x['site'] == 'Khania'}
    ht = {x['label'] for x in TOK if x['site'] == 'Haghia Triada'}
    items = list(kh.items())
    r_, p, a, b = R.flag_compare(items, lambda x: x[1] == 'desc', lambda x: x[0] in ht)
    return p, 'Khania descriptor words occur at HT more often than Khania names', {'desc_at_HT': a, 'name_at_HT': b, 'p': round(p, 4)}, {}


def Q8():
    items = [(v['kuro'], v['name'] / (v['name'] + v['desc'])) for v in ST.values() if v['name'] + v['desc'] >= 2]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'Tablets with a total carry name entries more often', {'with_total_name_share': a, 'without': b, 'p': round(p, 4)}, {}


def Q10():
    items = [x for x in TOK if x['q'] > 0]
    r_, p, a, b = R.flag_compare(items, lambda x: x['slot'] == 'desc', lambda x: x['q'] == 1, lower=True)
    return p, 'Descriptor entries have an amount of 1 less often', {'desc': a, 'name': b, 'p': round(p, 4)}, {}


def Q11():
    init = Counter(t['label'].split('-')[0] for r in B.READ['records'] if r['site'] == 'Haghia Triada' and r['support'] in B.ADMIN
                   for t in r['tokens'] if t['cls'] in N.WORD and '-' in t['label'])
    top = {s for s, _ in init.most_common(15)}
    seal = [s for site, _, s in SEALS if site == 'Haghia Triada']
    tab = [t['label'] for r in B.READ['records'] if r['site'] == 'Haghia Triada' and r['support'] in B.ADMIN for t in r['tokens'] if t['cls'] == 'single-sign' and SYL.match(t['label'])]
    items = [('seal', s) for s in seal] + [('tab', s) for s in tab]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0] == 'seal', lambda x: x[1] in top)
    return p, 'At HT, sealing signs are the common word-initial signs more often than tablet single signs', {'seal': a, 'tablet': b, 'p': round(p, 4)}, {'top initials': sorted(top)}


def Q12():
    pairs = [(sup, s) for site, sup, s in SEALS if site == 'Haghia Triada']
    c = Counter(s for _, s in pairs)
    pairs = [x for x in pairs if c[x[1]] >= 5]
    real, p, nm = R.assoc(pairs)
    return p, 'At HT, roundels and nodules use different signs', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4)}, {'supports': dict(Counter(sp for sp, _ in pairs))}


def Q13():
    items = [(v['desc'] > 0, len(v['com']) == 1) for v in ST.values() if v['com']]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'Tablets with descriptor entries are single-commodity more often', {'with_desc': a, 'without': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round61', 'list types and the sealing system', __doc__, [Q1, Q2, Q4, Q5, Q7, Q8, Q10, Q11, Q12, Q13])
