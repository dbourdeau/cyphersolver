"""Round 51: do the single signs that Linear B uses as commodity abbreviations already work that way in Linear A?

Linear B abbreviates spices and plants with syllables: SA (sesame, sa-sa-ma), KU (cumin, ku-mi-no), KO (coriander,
ko-ri-ja-do-no), MA (fennel, ma-ra-tu-wo), MI (mint, mi-ta), SE (celery, se-ri-no), KA (safflower, ka-na-ko),
PO (po-ni-ki-jo). This set is fixed before testing; NI (figs, round 50) is left out to keep the tests independent.
Benjamini-Hochberg at 5% across the eight.

CM1 Single signs of the set are followed directly by a number more often than other single signs (NI excluded).
CM2 Their entries carry fractions more often than entries of other single signs.
CM3 They stand on tablets with commodity logograms other than VIR more often.
CM4 Across single signs, the rate of being followed by a number correlates with the rate of taking fractions.
CM5 Single TE stands in the first entry of a tablet more often than other single signs.
CM6 Single signs followed by numbers (NI excluded) hold consistent places among the commodities of a tablet.
CM7 Single signs of the set co-occur on the same tablets beyond chance.
CM8 Single signs followed by numbers stand in the first entry of a tablet less often than other single signs.
"""
from collections import Counter, defaultdict
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round43 as FF  # noqa: E402
import round50 as HV  # noqa: E402

B, X = R.B, R.X
SPICE = {'SA', 'KU', 'KO', 'MA', 'MI', 'SE', 'KA', 'PO'}
SYL = re.compile(r'^[A-Z]{1,2}[0-9]?$')


def single_rows():
    rows = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        toks = r['tokens']
        coms = {re.findall(r'[A-Z]{3,}', t['label'])[0] for t in toks if t['cls'] == 'commodity' and re.findall(r'[A-Z]{3,}', t['label'])}
        first_entry = min((t['entry'] for t in toks), default=0)
        ents = defaultdict(list)
        for t in toks:
            ents[t['entry']].append(t)
        for i, t in enumerate(toks):
            if t['cls'] == 'single-sign' and SYL.match(t['label']) and t['label'] != 'NI':
                nxt = toks[i + 1] if i + 1 < len(toks) else None
                e = ents[t['entry']]
                rows.append({'sign': t['label'], 'num': bool(nxt) and nxt['cls'] in ('number', 'fraction'),
                             'frac': any(x['cls'].startswith('fraction') for x in e), 'goods': bool(coms - {'VIR'}),
                             'first': t['entry'] == first_entry, 'tab': X.whole(r['name'])})
    return rows


ROWS = single_rows()


def CM1():
    r_, p, a, b = R.flag_compare(ROWS, lambda x: x['sign'] in SPICE, lambda x: x['num'])
    return p, 'Spice-abbreviation signs are followed by numbers more often', {'set': a, 'other': b, 'p': round(p, 4)}, {}


def CM2():
    r_, p, a, b = R.flag_compare(ROWS, lambda x: x['sign'] in SPICE, lambda x: x['frac'])
    return p, 'Spice-abbreviation sign entries carry fractions more often', {'set': a, 'other': b, 'p': round(p, 4)}, {}


def CM3():
    r_, p, a, b = R.flag_compare(ROWS, lambda x: x['sign'] in SPICE, lambda x: x['goods'])
    return p, 'Spice-abbreviation signs stand on goods tablets more often', {'set': a, 'other': b, 'p': round(p, 4)}, {}


def CM4():
    by = defaultdict(list)
    for x in ROWS:
        by[x['sign']].append(x)
    signs = [s for s, v in by.items() if len(v) >= 5]
    xs = [sum(x['num'] for x in by[s]) / len(by[s]) for s in signs]
    ys = [sum(x['frac'] for x in by[s]) / len(by[s]) for s in signs]
    real = B.spearman(xs, ys)
    null = []
    for _ in range(5000):
        y2 = list(ys)
        R.rng.shuffle(y2)
        null.append(B.spearman(xs, y2))
    p = R.pv_hi(null, real)
    return p, 'Number-following and fraction rates correlate across single signs', {'spearman': round(real, 3), 'p': round(p, 4), 'signs': len(signs)},\
        {'number-following rate by sign': {s: round(x, 2) for s, x in sorted(zip(signs, xs), key=lambda z: -z[1])[:12]}}


def CM5():
    r_, p, a, b = R.flag_compare(ROWS, lambda x: x['sign'] == 'TE', lambda x: x['first'])
    return p, 'Single TE stands in the first entry more often', {'TE_first': a, 'other_first': b, 'p': round(p, 4)}, {}


def CM6():
    numsigns = {s for s, n in Counter(x['sign'] for x in ROWS if x['num']).items() if n >= 3}
    seqs = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        seq = []
        toks = r['tokens']
        for i, t in enumerate(toks):
            g = None
            if t['cls'] == 'commodity':
                m = re.findall(r'[A-Z]{3,}', t['label'])
                g = m[0] if m else None
            elif t['cls'] == 'single-sign' and t['label'] in numsigns:
                nxt = toks[i + 1] if i + 1 < len(toks) else None
                if nxt and nxt['cls'] in ('number', 'fraction'):
                    g = 'S:' + t['label']
            if g and g not in seq:
                seq.append(g)
        if any(x.startswith('S:') for x in seq) and len(seq) >= 2:
            seqs.append(seq)

    def stat(ss):
        c = Counter()
        for s in ss:
            for i, a in enumerate(s):
                for j, b in enumerate(s):
                    if i < j and (a.startswith('S:') or b.startswith('S:')):
                        c[(a, b)] += 1
        return sum(abs(c[(a, b)] - c[(b, a)]) for (a, b) in {tuple(sorted(k)) for k in c})
    real, p, nm = FF.shuffle_within(seqs, stat)
    return p, 'Number-following single signs hold consistent places among commodities', {'asymmetry': real, 'null': round(nm, 1), 'p': round(p, 4), 'tablets': len(seqs)}, {'signs': sorted(numsigns)}


def CM7():
    tabs = defaultdict(set)
    for x in ROWS:
        if x['sign'] in SPICE:
            tabs[x['tab']].add(x['sign'])
    alltabs = sorted({x['tab'] for x in ROWS})
    sets = [tabs.get(t, set()) for t in alltabs]
    stat = lambda ss: sum(1 for s in ss if len(s) >= 2)
    real = stat(sets)
    # null: each spice token reassigned to a random tablet among those with single signs
    toks = [(x['tab'], x['sign']) for x in ROWS if x['sign'] in SPICE]
    null = []
    for _ in range(R.REPS):
        m = defaultdict(set)
        for _, s in toks:
            m[R.rng.choice(alltabs)].add(s)
        null.append(stat(m.values()))
    p = R.pv_hi(null, real)
    return p, 'Spice-abbreviation signs co-occur on the same tablets', {'tablets_with_2plus': real, 'null': round(sum(null) / len(null), 2), 'p': round(p, 4)}, {}


def CM8():
    r_, p, a, b = R.flag_compare(ROWS, lambda x: x['num'], lambda x: x['first'], lower=True)
    return p, 'Number-following single signs stand in the first entry less often', {'num_first': a, 'other_first': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round51', 'single signs as commodity abbreviations', __doc__, [CM1, CM2, CM3, CM4, CM5, CM6, CM7, CM8])
