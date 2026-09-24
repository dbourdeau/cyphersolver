"""Round 62 (saturation loop 4): does the descriptor slot mark which goods an entry is about? BH at 5% across the
seven.

R1  On multi-commodity tablets, an entry whose commodity differs from the previous entry's has a descriptor word
    more often than an entry that continues the same commodity.
R2  The number of commodities on a tablet correlates with the share of its word entries in the descriptor slot.
R4  On single-commodity tablets, a smaller share of entries carries a commodity sign than on multi-commodity tablets.
R5  KU-RO stands directly before a commodity sign more often on multi-commodity tablets than on single-commodity ones.
R9  Amounts after descriptor words are multiples of 10 more often than amounts after name words.
R11 Headings of multi-commodity tablets are terms (words also used in the descriptor slot) more often.
R13 On multi-commodity tablets, descriptor entries open a commodity block (first entry of that commodity) more often
    than other entries with a commodity sign.
"""
from collections import Counter, defaultdict
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402
import round59 as N  # noqa: E402
import round60 as PP  # noqa: E402
import round61 as QQ  # noqa: E402

B, X = R.B, R.X
WORD = N.WORD
com_of = N.com_of


def entry_table():
    recs = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        ents = defaultdict(list)
        for t in r['tokens']:
            if t['cls'] != 'apparatus':
                ents[t['entry']].append(t)
        rows = []
        for e, toks in sorted(ents.items()):
            coms = [com_of(t) for t in toks if t['cls'] == 'commodity' and com_of(t)]
            desc = any(toks[i]['cls'] in WORD and toks[i + 1]['cls'] == 'commodity' for i in range(len(toks) - 1))
            kuro_desc = any(toks[i]['label'] == 'KU-RO' and toks[i + 1]['cls'] == 'commodity' for i in range(len(toks) - 1))
            has_word = any(t['cls'] in WORD for t in toks)
            rows.append({'com': coms[0] if coms else None, 'desc': desc, 'word': has_word, 'kuro_desc': kuro_desc,
                         'kuro': any(t['label'] == 'KU-RO' for t in toks)})
        tcoms = {x['com'] for x in rows if x['com']}
        recs.append({'name': r['name'], 'rows': rows, 'ncom': len(tcoms)})
    return recs


RECS = entry_table()


def R1():
    items = []
    for rec in RECS:
        if rec['ncom'] < 2:
            continue
        prev = None
        for x in rec['rows']:
            if x['com']:
                if prev is not None:
                    items.append((x['com'] != prev, x['desc']))
                prev = x['com']
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'A switch of commodity carries a descriptor word more often', {'switch': a, 'continue': b, 'p': round(p, 4)}, {}


def R2():
    rows = [(rec['ncom'], sum(x['desc'] for x in rec['rows']) / max(1, sum(x['word'] for x in rec['rows']))) for rec in RECS if rec['ncom'] >= 1 and sum(x['word'] for x in rec['rows'])]
    xs, ys = [a for a, _ in rows], [b for _, b in rows]
    real = B.spearman(xs, ys)
    null = []
    for _ in range(5000):
        y2 = list(ys)
        R.rng.shuffle(y2)
        null.append(B.spearman(xs, y2))
    p = R.pv_hi(null, real)
    return p, 'More commodities, more descriptor entries', {'spearman': round(real, 3), 'p': round(p, 4), 'tablets': len(rows)}, {}


def R4():
    items = [(rec['ncom'] == 1, sum(1 for x in rec['rows'] if x['com']) / len(rec['rows'])) for rec in RECS if rec['ncom'] >= 1 and len(rec['rows']) >= 3]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1], lower=True)
    return p, 'Single-commodity tablets repeat the commodity sign less', {'single': a, 'multi': b, 'p': round(p, 4)}, {}


def R5():
    items = [(rec['ncom'] >= 2, x['kuro_desc']) for rec in RECS for x in rec['rows'] if x['kuro']]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'KU-RO before a commodity sign on multi-commodity tablets', {'multi': a, 'single': b, 'p': round(p, 4)}, {}


def R9():
    items = [x for x in N.TOK if x['q'] > 0]
    r_, p, a, b = R.flag_compare(items, lambda x: x['slot'] == 'desc', lambda x: x['q'] % 10 == 0)
    return p, 'Amounts after descriptor words are multiples of 10 more often', {'desc': a, 'name': b, 'p': round(p, 4)}, {}


def R11():
    ncom = {X.whole(rec['name']): rec['ncom'] for rec in RECS}
    items = [(ncom.get(k, 0) >= 2, h in PP.DSET) for k, h in QQ.HEADS.items() if ncom.get(k, 0) >= 1]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'Headings of multi-commodity tablets are terms more often', {'multi': a, 'single': b, 'p': round(p, 4)}, {}


def R13():
    items = []
    for rec in RECS:
        if rec['ncom'] < 2:
            continue
        seen = set()
        for x in rec['rows']:
            if x['com']:
                items.append((x['desc'], x['com'] not in seen))
                seen.add(x['com'])
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'Descriptor entries open a commodity block more often', {'desc_opens': a, 'other_opens': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round62', 'the descriptor slot on mixed tablets', __doc__, [R1, R2, R4, R5, R9, R11, R13])
