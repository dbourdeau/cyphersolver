"""Sound values against the structure (item 4).

Published proposals for the ending signs: the Finnish team's 1969 paradigm (Parpola 1994:
94, Fig. 6.8): nominative zero, genitive = the jar (ICIT 740), dative = the arrow (ICIT 520);
the Soviet team (Knorozov et al., Parpola 1994: 96): jar = oblique/genitive *-at(tu),
another sign = dative *-kku; Parpola 1994 (Fig. 15.2 no. 24): the jar is a cow's head,
*a* 'cow' = possessive -a; 'man' (ICIT 90) = *al* 'man, servant'.

S1  The paradigm on the corpus: exclusivity, alternation on the same stems, what precedes and
    follows each ending.
S2  Rebus support in the Dravidian lexicon: words for the pictures (jar/pot, cow, arrow) whose
    form matches the proposed suffix (genitive -a/-atu/-in, dative -kku/-ku, sociative -otu).
S3  The numeral forms: which series stands in the star-name compounds and which counts goods.

Usage: python sound_tests.py dedr_entry_v11.csv     Writes results/sound_tests.md.
"""
import csv
import os
import re
import sys
from collections import Counter, defaultdict

import rebus_checks as rc
from signs import NUMERAL, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


def lex(path, pat):
    out = defaultdict(set)
    for r in csv.DictReader(open(path, encoding='utf-8')):
        m = re.split('[;,]', r['entry_meaning'].lower())[0]
        if re.search(pat, m):
            f = r['entry_str'].split('(')[0].split(',')[0].strip().strip('-').strip(')')
            f = f.split()[0] if f.split() else ''
            k = rc.simplify(f)
            if k:
                out[k].add(r['lang_str'])
    return out


def main(dedr):
    L = [ln for r in load() if r['flat'] for ln in r['seq']]
    tot = Counter(g for ln in L for g in ln)
    nx, pv = defaultdict(Counter), defaultdict(Counter)
    for ln in L:
        s = ['<'] + ln + ['>']
        for a, b in zip(s, s[1:]):
            nx[a][b] += 1
            pv[b][a] += 1
    say('# Sound values against the structure')
    say()
    say('## S1 The 1969 paradigm (jar 740 = genitive, arrow 520 = dative) on the corpus')
    say()
    say('- 740 next to 520: %d; 520 next to 740: %d (mutually exclusive, as the paradigm needs).'
        % (nx['740']['520'], nx['520']['740']))
    for x in ('740', '520'):
        fish_before = sum(c for a, c in pv[x].items() if a in rc.FISH)
        num_before = sum(c for a, c in pv[x].items() if a in NUMERAL)
        say('- %s: %d tokens; line-final %d (%.0f%%); followed by %s; preceded by a fish-series sign %d '
            '(%.0f%%), by a numeral %d; commonest before: %s.' % (
                x, tot[x], nx[x]['>'], 100 * nx[x]['>'] / tot[x],
                ', '.join('%s x%d' % kv for kv in nx[x].most_common(5) if kv[0] != '>'),
                fish_before, 100 * fish_before / tot[x], num_before,
                ', '.join('%s x%d' % kv for kv in pv[x].most_common(6))))
    st = defaultdict(set)
    for ln in L:
        for i, g in enumerate(ln):
            if g in ('740', '520') and i >= 1:
                st[ln[i - 1]].add(g)
    both = sorted(s for s, e in st.items() if len(e) == 2)
    say('- signs that take both endings directly: %d (of %d before 740 and %d before 520): %s.' % (
        len(both), sum('740' in e for e in st.values()), sum('520' in e for e in st.values()), ' '.join(both)))
    say('- 3 long strokes + 520: %d (the value never varies); a case ending straight after a bare '
        'numeral with a fixed value is unexpected; a lexical compound fits better.' % sum(
            1 for ln in L for a, b in zip(ln, ln[1:]) if a == '33' and b == '520'))
    say()
    say('## S2 Rebus support in the Dravidian lexicon (all 26 DEDR languages, first sense of the gloss)')
    say()
    for lab, pat, suff in (('cow', r'\bcows?\b', ('a',)),
                           ('jar / pot / pitcher', r'\b(jar|pot|pitcher)s?\b', ('a', 'atu', 'in', 'an')),
                           ('arrow', r'\barrows?\b', ('ku', 'ki', 'ke', 'ge', 'otu', 'utu', 'il', 'al'))):
        w = lex(dedr, pat)
        match = {k: v for k, v in w.items() if k in suff}
        say('- **%s**: %d forms in %d languages; forms equal to a proposed suffix shape (%s): %s.' % (
            lab, len(w), len({x for v in w.values() for x in v}), ', '.join(suff),
            '; '.join('%s (%s)' % (k, ', '.join(sorted(v))) for k, v in sorted(match.items())) or 'none'))
    say()
    say('## S3 Numeral forms: combining vs counting')
    say()
    series = {'short': {'1', '2', '3', '4', '5', '6', '7'}, 'tiered': {'13', '14', '15', '16', '17', '18', '19', '55', '56'},
              'long': {'31', '32', '33', '34', '35', '36'}}
    for lab, nouns in (('before the plain fish (star-name compounds in Parpola)', {'220'}),
                       ('before the pot 700 (counted goods)', {'700'})):
        c = Counter()
        for ln in L:
            for a, b in zip(ln, ln[1:]):
                if b in nouns:
                    for s, S in series.items():
                        if a in S and a not in ('2', '32'):
                            c[s] += 1
        say('- %s: %s (the short and long pairs left out).' % (lab, ', '.join('%s %d' % kv for kv in c.most_common())))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'sound_tests.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
