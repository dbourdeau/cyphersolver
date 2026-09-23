"""Which names take 520? The two endings as a noun class, against the class systems of the
candidate languages.

The ending is fixed per name (bench.py: 5 of 881 names take both). The class of a name is read from
its last sign before the ending (Dravidian, Munda and Sumerian compounds are head-final). Each such
sign is put in a category by what it depicts: human figures and the stroke numerals by their shape,
the fish series (Parpola's 'stars') as a group, the rest from Fairservis 1992's identification of the
drawing (keys/fairservis1992_raw.tsv, 'sure' or 'likely' matches), else 'unidentified'. The ICIT-
derived corpus and the M77 additions are pooled (each line one name + ending).

C1  Share of 520 by category, with a Fisher exact test of each category against all others.
C2  What each candidate class system predicts:
    - Tamil (Old Tamil grammar): rational (uyartinai: humans, gods) against non-rational (aḵrinai:
      animals, things, stars); a title 'he of the X' is rational whatever X is.
    - Proto-Dravidian as in Old Telugu (Mahadevan 1998): masculine against non-masculine (women,
      animals, things, stars).
    - Sumerian: human against non-human.
    - Sanskrit: masculine / feminine / neuter by the noun; the nakshatra names are mostly feminine,
      measure words mostly masculine.
    - Munda (Hoffmann 1903, Mundari Grammar: 'all heavenly bodies ... are considered as living
      beings'): animate (humans, animals, heavenly bodies, rain) against inanimate (plants, things);
      marked by number only, with no class suffix on a singular noun.

Writes results/noun_class.md.
"""
import csv
import math
import os
from collections import Counter, defaultdict

from numerals import NUMS
from signs import FISH, load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
HUMAN = {'90', '100', '93', '95', '96', '97', '98', '111', '112', '122', '123', '125', '127', '137', '142', '146',
         '150', '151', '154', '71'}


def say(s=''):
    OUT.append(s)
    print(s)


def fisher_right(a, b, c, d):
    """P(X >= a) for the 2x2 table [[a, b], [c, d]] (hypergeometric)."""
    n1, n2, k = a + b, c + d, a + c
    tot = n1 + n2

    def lc(n, r):
        return math.lgamma(n + 1) - math.lgamma(r + 1) - math.lgamma(n - r + 1)
    p = 0.0
    for x in range(a, min(n1, k) + 1):
        p += math.exp(lc(n1, x) + lc(n2, k - x) - lc(tot, k))
    return min(1.0, p)


def split_end(t):
    if len(t) >= 3 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
        return tuple(t[:-2]), t[-2]
    if len(t) >= 2 and t[-1] in ('740', '520'):
        return tuple(t[:-1]), t[-1]
    return None, None


def main():
    ident = {}
    for r in csv.DictReader((ln for ln in open(os.path.join(HERE, 'keys', 'fairservis1992_raw.tsv'), encoding='utf-8')
                             if not ln.startswith('#')), delimiter='\t'):
        if r['confidence'] in ('sure', 'likely') and r['icit']:
            ident.setdefault(r['icit'].split('|')[0], (r['fcode'], r['gloss'].split('=>')[0].strip()))

    def category(g):
        if g in FISH:
            return 'fish series ("stars")'
        if g in NUMS:
            return {'long': 'long strokes', 'short': 'short strokes',
                    'tiered': 'tiered numerals'}[NUMS[g][1]]
        if g in HUMAN or (g in ident and ident[g][0].startswith('A-')):
            return 'human figures'
        if g in ident:
            f = ident[g][0][0]
            return {'B': 'animals', 'C': 'animals', 'D': 'animals', 'E': 'plants', 'F': 'sky and weather',
                    'N': 'landscape and settlements'}.get(f, 'objects and tools')
        return 'unidentified'
    ends = defaultdict(Counter)
    for rows in (load(), load(only_m77=True)):
        for r in rows:
            for ln in r['seq']:
                s, e = split_end(ln)
                if s and s[-1] != '?':
                    ends[s[-1]][e] += 1
    cat = defaultdict(Counter)
    signs = defaultdict(list)
    for g, c in ends.items():
        k = category(g)
        cat[k] += c
        signs[k].append((g, c))
    say('# The two endings as a noun class')
    say()
    say('Lines ending in 740 or 520 (with or without 400/90/151 after it), ICIT-derived and M77 additions pooled: %d; '
        '520 in %d (%.1f%%).' % (sum(sum(c.values()) for c in cat.values()), sum(c['520'] for c in cat.values()),
                                 100 * sum(c['520'] for c in cat.values()) / sum(sum(c.values()) for c in cat.values())))
    say()
    say('## C1 Share of 520 by what the last sign of the name depicts')
    say()
    say('| category | lines | 520 | share | Fisher p (more 520 than the rest) | commonest signs (520/lines) |')
    say('|---|---|---|---|---|---|')
    T5 = sum(c['520'] for c in cat.values())
    T = sum(sum(c.values()) for c in cat.values())
    for k, c in sorted(cat.items(), key=lambda x: -x[1]['520'] / max(1, sum(x[1].values()))):
        n = sum(c.values())
        p = fisher_right(c['520'], n - c['520'], T5 - c['520'], T - n - (T5 - c['520']))
        top = sorted(signs[k], key=lambda x: -sum(x[1].values()))[:6]
        say('| %s | %d | %d | %.0f%% | %.2g | %s |' % (k, n, c['520'], 100 * c['520'] / n, p,
                                                      ', '.join('%s %d/%d' % (g, cc['520'], sum(cc.values())) for g, cc in top)))
    say()
    say('- signs that take 520 (5+ lines, 20%%+): %s.' % ', '.join(
        '%s %s (%d/%d)' % (g, ident.get(g, ('', ''))[1][:40] or category(g), c['520'], sum(c.values()))
        for g, c in sorted(ends.items(), key=lambda x: -x[1]['520'])
        if sum(c.values()) >= 5 and c['520'] / sum(c.values()) >= 0.2))
    say('- human figures, animals, plants, objects and settlements, sky and weather: 520 on %d of %d lines.' % (
        sum(cat[k]['520'] for k in ('human figures', 'animals', 'plants', 'objects and tools',
                                    'landscape and settlements', 'sky and weather')),
        sum(sum(cat[k].values()) for k in ('human figures', 'animals', 'plants', 'objects and tools',
                                           'landscape and settlements', 'sky and weather'))))
    say()
    say('## C2 Against the class systems of the candidate languages')
    say()
    say('The observed split. 520 is a small, closed class: the fish series (220, 240, 233, 231, 235: 154 of 254 lines) '
        'and one fixed unit, long 3 + 520 (56 of 63); almost nothing else takes it. Human figures, objects, tools, '
        'plants, buildings and landscape take 740 (24 of 754 lines with 520), and so do the long pair (0 of 76) and '
        'the tiered numerals. If 740 is a personal suffix ("he of the X", Mahadevan), the object at the end of a '
        'name does not decide its class; its referent does. The 520 names are the fish names, which Parpola reads as '
        'stars: persons (740) against stars (520).')
    say()
    say('| class system | persons, titles "he of the X" | stars | gods | fits |')
    say('|---|---|---|---|---|')
    say('| Old Tamil: rational (uyartinai) / non-rational (aḵrinai) | rational | non-rational | rational | yes, if the '
        'fish names are stars, not gods |')
    say('| Proto-Dravidian (Old Telugu): masculine / non-masculine | masculine | non-masculine | masculine or not by '
        'the god | yes |')
    say('| Sumerian: human / non-human | human | non-human | human | yes, if the fish names are stars, not gods |')
    say('| Sanskrit: gender of the noun | masculine | mostly feminine (Krttika, Rohini, Revati), some m. and n. | '
        'by the name | in part |')
    say('| Munda: animate / inanimate, by number only | animate | animate ("all heavenly bodies ... living beings", '
        'Hoffmann 1903) | animate | no: stars go with persons, and a singular noun takes no class suffix |')
    say()
    say('Two caveats. (1) The signs Fairservis identifies as sun and moon (803, 920, 820) take 740 (2 of 40); if those '
        'identifications hold, the class is not "heavenly bodies" but something narrower - which again fits a gender '
        'or rational/non-rational reading better than Munda animacy, where sun and moon are animate like persons. '
        '(2) Everything rests on 740 marking persons and the fish names being stars. Given those, a system that '
        'splits persons from stars fits Dravidian and Sumerian, fits Sanskrit gender in part, and does not fit Munda.')
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'noun_class.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
