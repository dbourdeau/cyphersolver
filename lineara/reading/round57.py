"""Round 57: the syntax of an entry (the order of word, commodity sign and number). Benjamini-Hochberg at 5% across
the nine.

SY1  In entries with both a word and a commodity sign, the word comes first more often than not.
SY2  Word-first versus commodity-first order differs by site.
SY3  It differs by scribe.
SY4  Commodity-first entries are the first entry of their tablet more often than word-first entries.
SY5  A number follows a commodity sign directly more often than it follows a word directly (per preceding token).
SY6  Linear A puts the word first less often than Linear B does.
SY8  Heading words are followed directly by a commodity sign more often than entry labels.
SY9  Transaction terms (SA-RA2, KU-PA, A-DU, KA-PA, DA-RE) are followed directly by a commodity sign more often
     than other words.
SY10 Entry labels are followed directly by a number more often than heading words.
"""
from collections import Counter, defaultdict
from math import comb
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import roundlib as R  # noqa: E402

B, X = R.B, R.X
WORD = ('word', 'term', 'word-with-unknown-sign')
TERMS = {'SA-RA2', 'KU-PA', 'A-DU', 'KA-PA', 'DA-RE'}


def entries():
    rows = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        ents = defaultdict(list)
        for t in r['tokens']:
            if t['cls'] != 'apparatus':
                ents[t['entry']].append(t)
        first = min(ents) if ents else None
        for e, toks in ents.items():
            wi = next((i for i, t in enumerate(toks) if t['cls'] in WORD), None)
            ci = next((i for i, t in enumerate(toks) if t['cls'] == 'commodity'), None)
            if wi is not None and ci is not None:
                rows.append({'word_first': wi < ci, 'site': r['site'], 'scribe': X.SCRIBE_W.get(X.whole(r['name'])), 'first': e == first})
    return rows


ROWS = entries()


def pairs_next():
    out = []
    for r in B.READ['records']:
        if r['support'] not in B.ADMIN:
            continue
        toks = [t for t in r['tokens'] if t['cls'] != 'apparatus']
        for i in range(len(toks) - 1):
            out.append((toks[i], toks[i + 1]))
    return out


PAIRS = pairs_next()


def SY1():
    k = sum(x['word_first'] for x in ROWS)
    n = len(ROWS)
    p = sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n
    return p, 'The word precedes the commodity sign more often than not', {'word_first': f'{k}/{n}', 'p': round(p, 6)}, {}


def assoc_by(key):
    rows = [x for x in ROWS if x[key]]
    c = Counter(x[key] for x in rows)
    rows = [x for x in rows if c[x[key]] >= 5]
    return R.assoc([(x[key], x['word_first']) for x in rows]), rows


def SY2():
    (real, p, nm), rows = assoc_by('site')
    return p, 'Entry order differs by site', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4)},\
        {'word-first share by site': {s: round(sum(x['word_first'] for x in rows if x['site'] == s) / n, 2) for s, n in Counter(x['site'] for x in rows).items()}}


def SY3():
    (real, p, nm), rows = assoc_by('scribe')
    return p, 'Entry order differs by scribe', {'chi2': round(real, 1), 'null': round(nm, 1), 'p': round(p, 4), 'entries': len(rows)}, {}


def SY4():
    r_, p, a, b = R.flag_compare(ROWS, lambda x: not x['word_first'], lambda x: x['first'])
    return p, 'Commodity-first entries are first entries more often', {'commodity_first_in_first_entry': a, 'word_first_in_first_entry': b, 'p': round(p, 4)}, {}


def SY5():
    items = [(a['cls'], b['cls'] == 'number') for a, b in PAIRS if a['cls'] in ('commodity',) + WORD]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0] == 'commodity', lambda x: x[1])
    return p, 'A number follows a commodity sign more often than a word', {'after_commodity': a, 'after_word': b, 'p': round(p, 4)}, {}


def lb_word_first():
    k = n = 0
    for _, r in B.LB_RECS:
        if r.get('site') not in ('Knossos', 'Pylos'):
            continue
        tw = [t.strip() for t in r.get('transliteratedWords', [])]
        # split into lines at newline markers
        line = []
        for t in tw + ['\n']:
            if t == '\n':
                wi = next((i for i, x in enumerate(line) if re.fullmatch(r'[a-z0-9*]+(-[a-z0-9*]+)+', x)), None)
                ci = next((i for i, x in enumerate(line) if re.match(r'^\*?[A-Z]{3,}', x)), None)
                if wi is not None and ci is not None:
                    n += 1
                    k += wi < ci
                line = []
            else:
                line.append(t)
    return k, n


def SY6():
    la_k = sum(x['word_first'] for x in ROWS)
    la_n = len(ROWS)
    lb_k, lb_n = lb_word_first()
    labels = [1] * la_n + [0] * lb_n
    vals = [1] * la_k + [0] * (la_n - la_k) + [1] * lb_k + [0] * (lb_n - lb_k)
    stat = lambda lab: sum(v for v, l in zip(vals, lab) if l) / la_n - sum(v for v, l in zip(vals, lab) if not l) / lb_n
    real = stat(labels)
    null = []
    for _ in range(R.REPS):
        R.rng.shuffle(labels)
        null.append(stat(labels))
    p = R.pv_lo(null, real)
    return p, 'Linear A puts the word first less often than Linear B', {'LA': f'{la_k}/{la_n}', 'LB': f'{lb_k}/{lb_n}', 'p': round(p, 4)}, {}


def follows(pred_a, pred_b):
    items = [(a, b) for a, b in PAIRS if a['cls'] in WORD]
    return [(pred_a(a), pred_b(b)) for a, b in items]


def SY8():
    items = [(a.get('function'), b['cls'] == 'commodity') for a, b in PAIRS if a['cls'] in WORD and a.get('function') in ('heading', 'entry label')]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0] == 'heading', lambda x: x[1])
    return p, 'Heading words are followed by a commodity sign more often than entry labels', {'heading': a, 'entry_label': b, 'p': round(p, 4)}, {}


def SY9():
    items = [(a['label'] in TERMS, b['cls'] == 'commodity') for a, b in PAIRS if a['cls'] in WORD]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0], lambda x: x[1])
    return p, 'Transaction terms are followed by a commodity sign more often than other words', {'terms': a, 'other_words': b, 'p': round(p, 4)}, {}


def SY10():
    items = [(a.get('function'), b['cls'] == 'number') for a, b in PAIRS if a['cls'] in WORD and a.get('function') in ('heading', 'entry label')]
    r_, p, a, b = R.flag_compare(items, lambda x: x[0] == 'entry label', lambda x: x[1])
    return p, 'Entry labels are followed by a number more often than headings', {'entry_label': a, 'heading': b, 'p': round(p, 4)}, {}


if __name__ == '__main__':
    R.run('round57', 'the syntax of an entry', __doc__, [SY1, SY2, SY3, SY4, SY5, SY6, SY8, SY9, SY10])
