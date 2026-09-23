"""Lead 4 (sixth pass): does Proto-Elamite have the Indus text shape [name] + [fixed phrase]?

In the Indus texts a recurring tail (845 (61) 407; 740 400; 740 90) follows different 'names'.
Here the same measure on both corpora: the share of multi-sign units (Indus lines; Proto-Elamite
entries, i.e. the signs before a number) that end in a two-sign tail found after at least three
different preceding signs; and the commonest such tails. And the header: the share of Proto-Elamite
texts whose first line carries no number (a heading, as the Indus opening formula is).

Usage: python pe_formula.py path/to/pe-sign-value-data/corpus
Writes results/pe_formula.md.
"""
import glob
import os
import re
import sys
from collections import Counter, defaultdict

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def tails(units):
    heads = defaultdict(set)
    for u in units:
        if len(u) >= 3:
            heads[tuple(u[-2:])].add(u[-3])
    shared = {t for t, h in heads.items() if len(h) >= 3}
    k = sum(1 for u in units if len(u) >= 3 and tuple(u[-2:]) in shared)
    n = sum(1 for u in units if len(u) >= 3)
    top = sorted(((len(heads[t]), t) for t in shared), reverse=True)[:8]
    return k, n, top


def norm(s):
    return re.sub(r'~.*', '', s.split('<')[-1] if '<' in s else s)


def main(corpus):
    say('# Proto-Elamite and the Indus text shape')
    say()
    ind = [ln for r in load() if r['flat'] for ln in r['seq']]
    k, n, top = tails(ind)
    say('- Indus: %d of %d lines of 3+ signs (%.0f%%) end in a two-sign tail found after 3+ different signs; '
        'commonest: %s.' % (k, n, 100 * k / n, ', '.join('%s (%d heads)' % (' '.join(t), h) for h, t in top)))
    entries, texts, headed = [], 0, 0
    for f in glob.glob(os.path.join(corpus, '*.atf')):
        lines = [ln for ln in open(f, encoding='utf-8') if re.match(r"^\s*\d+'?\.", ln)]
        if not lines:
            continue
        texts += 1
        if ',' not in lines[0] or not re.search(r'\(N\d', lines[0]):
            headed += 1
        for ln in lines:
            m = re.match(r"^\s*\d+'?\.\s*(.*?)\s*,\s*(.+)$", ln)
            if m:
                s = [norm(x) for x in m.group(1).split() if x not in ('...', 'x', '[...]')]
                if s:
                    entries.append(s)
    k, n, top = tails(entries)
    say('- Proto-Elamite: %d of %d entries of 3+ signs (%.0f%%) end in a two-sign tail found after 3+ '
        'different signs; commonest: %s.' % (k, n, 100 * k / n, ', '.join('%s (%d heads)' % (' '.join(t), h) for h, t in top)))
    say('- Proto-Elamite texts whose first line has no number (a heading): %d of %d (%.0f%%). Indus seals '
        'opening with the formula [817/820/861] + [2/60/1]: see leads.md L6 (97 of 1,469 seals exactly; '
        '317 texts with any name sign after it).' % (headed, texts, 100 * headed / texts))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'pe_formula.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
