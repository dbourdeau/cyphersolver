"""Round 50: high-value tests of what single signs and NI mean. Benjamini-Hochberg at 5% across the eight.

HV1  NI (single sign) and the fig logogram FIC avoid the same tablet (complementary, as two writings of figs).
HV2  A single sign and the term it would abbreviate avoid the same tablet: KU / KU-RO, KI / KI-RO, KA / KA-PA,
     SA / SA-RA2, DA / DA-RE, A / A-DU (pooled; single-sign labels shuffled across tablets).
HV3  Single KU stands in the last entry of a tablet, where KU-RO stands, more often than other single signs.
HV4  Single signs on oil (OLE) tablets are among the oil ligature adjuncts (KI, U, MI, DI, TA, NE, E, RI, ME, TU,
     QE, RA, A) more often than single signs on other tablets.
HV5  Entries with NI carry fractions more often than entries of men (VIR).
HV6  NI has a consistent place among the commodities of multi-commodity tablets (order asymmetry involving NI).
HV7  NI stands on grain (GRA) tablets more often than chance.
HV8  Amounts in NI entries are listed largest-first beyond chance.
"""
from collections import Counter, defaultdict
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round43 as FF  # noqa: E402
import round44 as GG  # noqa: E402
import vigorous2 as W2  # noqa: E402

B, X = R.B, R.X
whole = X.whole
ABBR = {'KU': 'KU-RO', 'KI': 'KI-RO', 'KA': 'KA-PA', 'SA': 'SA-RA2', 'DA': 'DA-RE', 'A': 'A-DU'}
OIL_ADJ = {'KI', 'U', 'MI', 'DI', 'TA', 'NE', 'E', 'RI', 'ME', 'TU', 'QE', 'RA', 'A'}


def tablets():
    tabs = defaultdict(lambda: {'singles': [], 'labels': set(), 'com': set(), 'last_entry_singles': set(), 'entries': []})
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        t = tabs[whole(r['name'])]
        last = max((tok['entry'] for tok in r['tokens']), default=0)
        ents = defaultdict(list)
        for tok in r['tokens']:
            ents[tok['entry']].append(tok)
            t['labels'].add(tok['label'])
            if tok['cls'] == 'single-sign':
                t['singles'].append(tok['label'])
                if tok['entry'] == last:
                    t['last_entry_singles'].add(tok['label'])
            if tok['cls'] == 'commodity':
                m = re.findall(r'[A-Z]{3,}', tok['label'])
                if m:
                    t['com'].add(m[0])
        for e, toks in sorted(ents.items()):
            t['entries'].append(toks)
    return dict(tabs)


TABS = tablets()
KEYS = sorted(TABS)


def cooc_test(has_a, has_b, lower):
    a = [has_a(TABS[k]) for k in KEYS]
    b = [has_b(TABS[k]) for k in KEYS]
    real = sum(x and y for x, y in zip(a, b))
    null = []
    for _ in range(R.REPS):
        R.rng.shuffle(b)
        null.append(sum(x and y for x, y in zip(a, b)))
    p = R.pv_lo(null, real) if lower else R.pv_hi(null, real)
    return real, p, sum(null) / len(null), sum(a), sum(b)


def HV1():
    real, p, nm, na, nb = cooc_test(lambda t: 'NI' in t['singles'], lambda t: 'FIC' in t['com'], lower=True)
    return p, 'NI and FIC avoid the same tablet', {'together': real, 'null': round(nm, 2), 'p': round(p, 4), 'NI_tablets': na, 'FIC_tablets': nb}, {}


def HV2():
    items = [(k, s) for k in KEYS for s in set(TABS[k]['singles']) if s in ABBR]
    stat = lambda labs: sum(ABBR[s] in TABS[k]['labels'] for (k, _), s in zip(items, labs))
    labs = [s for _, s in items]
    real = stat(labs)
    null = []
    for _ in range(R.REPS):
        R.rng.shuffle(labs)
        null.append(stat(labs))
    labs = [s for _, s in items]
    p = R.pv_lo(null, real)
    return p, 'Single signs and the terms they would abbreviate avoid the same tablet', {'together': real, 'null': round(sum(null) / len(null), 2), 'p': round(p, 4), 'single_tokens': len(items)},\
        {'by sign (tablets with both / with the single)': {s: f"{sum(ABBR[s] in TABS[k]['labels'] for k, s2 in items if s2 == s)}/{sum(1 for _, s2 in items if s2 == s)}" for s in ABBR}}


def HV3():
    items = [(s, s in TABS[k]['last_entry_singles']) for k in KEYS for s in set(TABS[k]['singles'])]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0] == 'KU', lambda x: x[1])
    return p, 'Single KU stands in the last entry more often than other single signs', {'KU_last': a, 'other_last': b, 'p': round(p, 4)}, {}


def HV4():
    items = [(('OLE' in TABS[k]['com']), s) for k in KEYS for s in TABS[k]['singles'] if re.fullmatch(r'[A-Z]{1,2}[0-9]?', s)]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1] in OIL_ADJ)
    return p, 'Single signs on oil tablets are oil-ligature syllables more often', {'on_oil_tablets': a, 'elsewhere': b, 'p': round(p, 4)}, {}


def entry_rows():
    rows = []
    for k in KEYS:
        for toks in TABS[k]['entries']:
            ni = any(t['cls'] == 'single-sign' and t['label'] == 'NI' for t in toks)
            vir = any(t['cls'] == 'commodity' and t['label'].startswith('VIR') for t in toks)
            frac = any(t['cls'].startswith('fraction') for t in toks)
            num = any(t['cls'] == 'number' for t in toks)
            q = sum(t['value'] for t in toks if t['cls'] == 'number')
            if num or frac:
                rows.append({'ni': ni, 'vir': vir, 'frac': frac, 'q': q, 'tab': k})
    return rows


ROWS = entry_rows()


def HV5():
    items = [x for x in ROWS if x['ni'] or x['vir']]
    r_, p, a, b = R.flag_compare(items, lambda x: x['ni'], lambda x: x['frac'])
    return p, 'NI entries carry fractions more often than VIR entries', {'NI': a, 'VIR': b, 'p': round(p, 4)}, {}


def HV6():
    seqs = []
    for rec in GG.VV.RECS:
        pass
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        seq = []
        for t in r['tokens']:
            g = None
            if t['cls'] == 'commodity':
                m = re.findall(r'[A-Z]{3,}', t['label'])
                g = m[0] if m else None
            elif t['cls'] == 'single-sign' and t['label'] == 'NI':
                g = 'NI'
            if g and g not in seq:
                seq.append(g)
        if 'NI' in seq and len(seq) >= 2:
            seqs.append(seq)

    def stat(ss):
        c = Counter()
        for s in ss:
            i = s.index('NI')
            for j, g in enumerate(s):
                if g != 'NI':
                    c[(g, j < i)] += 1
        return sum(abs(c[(g, True)] - c[(g, False)]) for g in {g for g, _ in c})
    real, p, nm = FF.shuffle_within(seqs, stat)
    c = Counter()
    for s in seqs:
        i = s.index('NI')
        for j, g in enumerate(s):
            if g != 'NI':
                c[f"{g} {'before' if j < i else 'after'} NI"] += 1
    return p, 'NI has a consistent place among the commodities', {'asymmetry': real, 'null': round(nm, 1), 'p': round(p, 4), 'tablets': len(seqs)}, {'counts': dict(c.most_common(10))}


def HV7():
    real, p, nm, na, nb = cooc_test(lambda t: 'NI' in t['singles'], lambda t: 'GRA' in t['com'], lower=False)
    return p, 'NI stands on grain tablets more often than chance', {'together': real, 'null': round(nm, 2), 'p': round(p, 4), 'NI_tablets': na, 'GRA_tablets': nb}, {}


def HV8():
    lists = []
    for k in KEYS:
        qs = [sum(t['value'] for t in toks if t['cls'] == 'number') for toks in TABS[k]['entries']
              if any(t['cls'] == 'single-sign' and t['label'] == 'NI' for t in toks)]
        qs = [q for q in qs if q > 0]
        if len(qs) >= 3:
            lists.append(qs)
    stat = lambda ls: sum(W2.tau(q) for q in ls) / max(1, len(ls))
    real, p, nm = FF.shuffle_within(lists, stat)
    return p, 'NI amounts are listed largest-first beyond chance', {'mean_tau': round(real, 3), 'null': round(nm, 3), 'p': round(p, 4), 'lists': len(lists)}, {}


if __name__ == '__main__':
    R.run('round50', 'what single signs and NI mean', __doc__, [HV1, HV2, HV3, HV4, HV5, HV6, HV7, HV8])
