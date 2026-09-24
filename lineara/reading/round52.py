"""Round 52: the heading sign TE, first words and transaction terms, and non-adjacent consonant harmony.
Benjamini-Hochberg at 5% across the ten. Tablet sides merged where a tablet is the unit.

OP1  Tablets that open with TE record a single commodity more often than other tablets.
OP2  Tablets that open with TE carry a KU-RO total more often.
OP3  Opening with TE is tied to particular scribes (chi-square, scribes with 3+ tablets).
OP4  TE opens tablets at Haghia Triada and elsewhere (first-entry share against other single signs; larger p).
OP6  A tablet's first word is associated with its main commodity beyond chance.
OP10 The token after TE is a word or commodity logogram (not a number) more often than after other single signs.
OP14 Transaction terms (SA-RA2, KA-PA, A-DU, DA-RE, KU-PA) are associated with particular commodities.
OP17 Transaction terms are associated with particular sites.
OP19 Syllables one apart (first and third of three) share a consonant more often in Linear A than in Linear B.
OP22 The word after TE recurs across TE-opened tablets more than chance.
"""
from collections import Counter, defaultdict
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round29 as P  # noqa: E402
import round51 as CMr  # noqa: E402

B, X = R.B, R.X
whole = X.whole
cons = P.cons
TERMS = ('SA-RA2', 'KA-PA', 'A-DU', 'DA-RE', 'KU-PA')


def tablets():
    tabs = {}
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        toks = [t for t in r['tokens'] if t['cls'] != 'apparatus']
        if not toks:
            continue
        k = whole(r['name'])
        t = tabs.setdefault(k, {'first': None, 'next': None, 'com': Counter(), 'kuro': False, 'site': r['site'], 'first_word': None, 'terms': set()})
        if t['first'] is None:
            t['first'] = toks[0]['label'] if toks[0]['cls'] == 'single-sign' else None
            if t['first'] == 'TE':
                nxt = [x for x in toks[1:] if x['cls'] in ('word', 'term', 'commodity', 'word-with-unknown-sign')]
                t['next'] = nxt[0]['label'] if nxt else None
        for x in toks:
            if x['cls'] == 'commodity':
                m = re.findall(r'[A-Z]{3,}', x['label'])
                if m:
                    t['com'][m[0]] += 1
            if x['label'] in ('KU-RO', 'PO-TO-KU-RO'):
                t['kuro'] = True
            if x['cls'] in ('word', 'term') and t['first_word'] is None:
                t['first_word'] = x['label']
            if x['label'] in TERMS:
                t['terms'].add(x['label'])
    return tabs


TABS = tablets()
KEYS = sorted(TABS)
TE = lambda t: t['first'] == 'TE'


def OP1():
    items = [TABS[k] for k in KEYS if TABS[k]['com']]
    r_, p, a, b = R.flag_compare(items, TE, lambda t: len(t['com']) == 1)
    return p, 'TE-opened tablets record a single commodity more often', {'TE': a, 'other': b, 'p': round(p, 4)}, {}


def OP2():
    items = [TABS[k] for k in KEYS]
    r_, p, a, b = R.flag_compare(items, TE, lambda t: t['kuro'])
    return p, 'TE-opened tablets carry a total more often', {'TE': a, 'other': b, 'p': round(p, 4)}, {}


def OP3():
    pairs = [(X.SCRIBE_W[k], TE(TABS[k])) for k in KEYS if k in X.SCRIBE_W]
    c = Counter(s for s, _ in pairs)
    pairs = [x for x in pairs if c[x[0]] >= 3]
    real, p, nm = R.assoc(pairs)
    return p, 'Opening with TE is tied to particular scribes', {'chi2': round(real, 2), 'null': round(nm, 2), 'p': round(p, 4), 'tablets': len(pairs)},\
        {'TE tablets by scribe': dict(Counter(s for s, f in pairs if f))}


def OP4():
    res, ps = {}, []
    for name, pred in (('HT', lambda s: s == 'Haghia Triada'), ('other', lambda s: s != 'Haghia Triada')):
        rows = [x for x in CMr.ROWS if pred(TABS.get(x['tab'], {}).get('site', ''))]
        r_, p, a, b = R.flag_compare(rows, lambda x: x['sign'] == 'TE', lambda x: x['first'])
        res[name] = {'TE_first': a, 'other_first': b, 'p': round(p, 4)}
        ps.append(p)
    return max(ps), 'TE opens tablets at HT and elsewhere', {**res, 'p (larger)': round(max(ps), 4)}, {}


def OP6():
    items = [(TABS[k]['first_word'], TABS[k]['com'].most_common(1)[0][0]) for k in KEYS if TABS[k]['first_word'] and TABS[k]['com']]
    c = Counter(w for w, _ in items)
    items = [x for x in items if c[x[0]] >= 3]
    real, p, nm = R.assoc(items)
    return p, 'The first word is associated with the main commodity', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'tablets': len(items)},\
        {'first words (tablets)': dict(Counter(w for w, _ in items).most_common(10))}


def OP10():
    rows = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        toks = [t for t in r['tokens'] if t['cls'] != 'apparatus']
        for i, t in enumerate(toks):
            if t['cls'] == 'single-sign' and re.fullmatch(r'[A-Z]{1,2}[0-9]?', t['label']):
                nxt = toks[i + 1] if i + 1 < len(toks) else None
                rows.append((t['label'], bool(nxt) and nxt['cls'] in ('word', 'term', 'commodity', 'word-with-unknown-sign')))
    r_, p, a, b = R.flag_compare(rows, lambda x: x[0] == 'TE', lambda x: x[1])
    return p, 'TE is followed by a word or logogram more often than other single signs', {'TE': a, 'other': b, 'p': round(p, 4)}, {}


def OP14():
    pairs = [(term, c) for k in KEYS for term in TABS[k]['terms'] for c in TABS[k]['com']]
    real, p, nm = R.assoc(pairs)
    tab = Counter(pairs)
    return p, 'Transaction terms are associated with particular commodities', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'pairs': len(pairs)},\
        {'term + commodity': [f'{a} + {b} x{n}' for (a, b), n in tab.most_common(12)]}


def OP17():
    pairs = [(term, TABS[k]['site']) for k in KEYS for term in TABS[k]['terms']]
    real, p, nm = R.assoc(pairs)
    return p, 'Transaction terms are associated with particular sites', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'pairs': len(pairs)},\
        {'term @ site': [f'{a} @ {b} x{n}' for (a, b), n in Counter(pairs).most_common(12)]}


def OP19():
    f = lambda ws: sum(1 for w in ws for i in range(len(w) - 2) if cons(w[i]) and cons(w[i]) == cons(w[i + 2])) / max(1, sum(max(0, len(w) - 2) for w in ws))
    r, p, nm = R.compare(R.LA, R.LB, f)
    return p, 'Syllables one apart share a consonant more often than in Linear B', {'LA': round(f(R.LA), 4), 'LB': round(f(R.LB), 4), 'p': round(p, 4)}, {}


def OP22():
    nx = [TABS[k]['next'] for k in KEYS if TE(TABS[k]) and TABS[k]['next']]
    real = sum(n - 1 for n in Counter(nx).values() if n >= 2)
    pool = [TABS[k]['first_word'] for k in KEYS if TABS[k]['first_word']]
    null = []
    for _ in range(R.REPS):
        smp = R.rng.sample(pool, len(nx))
        null.append(sum(n - 1 for n in Counter(smp).values() if n >= 2))
    p = R.pv_hi(null, real)
    return p, 'The word after TE recurs across TE-opened tablets', {'repeats': real, 'null': round(sum(null) / len(null), 2), 'p': round(p, 4), 'TE_tablets': len(nx)}, {'after TE': dict(Counter(nx).most_common(8))}


if __name__ == '__main__':
    R.run('round52', 'TE, first words, transaction terms, harmony', __doc__, [OP1, OP2, OP3, OP4, OP6, OP10, OP14, OP17, OP19, OP22])
