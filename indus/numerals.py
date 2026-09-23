"""Numbers and measures: do the Indus numerals follow the Harappan weight system?

Harappan cubical weights run 1, 2, 4, 8, 16, 32, 64 (binary; 1 = c. 13.7 g) and then
decimal multiples 160, 200, 320, 640, 1600 ... (Parpola 2005, n. 5: 1/16 ... 1, 2, 4, 8,
16 ... 800). If numeral + sign sequences record amounts in those units, the values should
favour powers of two, and the largest should reach 16 or more.

N1  Every numeral sign with its value, how it is built (rows of strokes) and its count.
N2  Values by series (short, tiered, long) and by the counted sign.
N3  The weight test: share of powers of two among the values, against the share expected if
    the values 1-12 were used as often as the counts of discrete things are (a flat and a
    Benford-like 1/n reference).
N4  The whole-text tablets 'numeral + sign' (e.g. 3 + 156, 3 long + pot): what the values are.

Writes results/numerals.md.
"""
import os
from collections import Counter, defaultdict

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []

# value and construction, read from the rendered glyphs (render_glyphs.py)
NUMS = {'1': (1, 'short', '1'), '2': (2, 'short', '2'), '3': (3, 'short', '3'), '4': (4, 'short', '4'),
        '5': (5, 'short', '5'), '6': (6, 'short', '6 in one row'), '7': (7, 'short', '7 in one row'),
        '13': (3, 'tiered', '2 over 1'), '14': (4, 'tiered', '2 over 2'), '15': (5, 'tiered', '3 over 2'),
        '16': (6, 'tiered', '3 over 3'), '17': (7, 'tiered', '4 over 3'), '18': (8, 'tiered', '4 over 4'),
        '19': (8, 'tiered', '4 over 4, slanting'), '55': (12, 'tiered', '4 + 4 + 4'),
        '56': (24, 'tiered', '8 + 8 + 8'), '31': (1, 'long', '1'), '32': (2, 'long', '2'),
        '33': (3, 'long', '3'), '34': (4, 'long', '4'), '35': (5, 'long', '5'), '36': (6, 'long', '6')}


def say(s=''):
    OUT.append(s)
    print(s)


def main():
    rows = [r for r in load(split=False) if r['flat']]
    lines = [ln for r in rows for ln in r['seq']]
    tot = Counter(g for ln in lines for g in ln)
    say('# Numbers and measures')
    say()
    say('## N1 Numeral signs')
    say()
    say('| sign | value | series | built as | occurrences |')
    say('|---|---|---|---|---|')
    for g, (v, s, b) in sorted(NUMS.items(), key=lambda x: (x[1][1], x[1][0])):
        say('| %s | %d | %s | %s | %d |' % (g, v, s, b, tot[g]))
    say()
    say('Largest value written: %d (sign 56, %d times). Strokes are never more than 4 in a tier '
        'except the one-row 6 and 7 (signs 6, 7: %d and %d times); 6, 7, 8 and 12 are built as 3+3, '
        '4+3, 4+4 and 4+4+4.' % (max(v for v, _, _ in NUMS.values()), tot['56'], tot['6'], tot['7']))
    say()
    say('## N2 Values by series and by the counted sign')
    say()
    by_series = defaultdict(Counter)
    by_noun = defaultdict(Counter)
    for ln in lines:
        for a, b in zip(ln, ln[1:]):
            if a in NUMS and b not in NUMS:
                v, s, _ = NUMS[a]
                by_series[s][v] += 1
                by_noun[(s, b)][v] += 1
    for s, c in by_series.items():
        say('- %s: %s' % (s, ', '.join('%d x%d' % kv for kv in sorted(c.items()))))
    say()
    say('| series | counted sign | values (count) | tokens |')
    say('|---|---|---|---|')
    for (s, b), c in sorted(by_noun.items(), key=lambda x: -sum(x[1].values()))[:25]:
        say('| %s | %s | %s | %d |' % (s, b, ', '.join('%d x%d' % kv for kv in sorted(c.items())),
                                      sum(c.values())))
    say()
    say('## N3 The weight test')
    say()
    allv = Counter()
    for c in by_series.values():
        allv.update(c)
    for lab, c in [('all series', allv)] + [(s, by_series[s]) for s in ('short', 'tiered', 'long')]:
        n = sum(c.values())
        p2 = sum(v for k, v in c.items() if k in (1, 2, 4, 8, 16, 32, 64))
        vals = sorted(c)
        flat = sum(1 for k in vals if k in (1, 2, 4, 8, 16)) / len(vals)
        inv = sum(1 / k for k in vals if k in (1, 2, 4, 8, 16)) / sum(1 / k for k in vals)
        say('- %s: %d numeral tokens; values %s; powers of two %d (%.0f%%); if the attested values '
            'were equally used %.0f%%; if used in proportion to 1/value %.0f%%.' % (
                lab, n, vals, p2, 100 * p2 / n, 100 * flat, 100 * inv))
    say()
    say('## N4 Whole texts made of a numeral and one sign')
    say()
    whole = Counter()
    for ln in lines:
        if len(ln) == 2 and ln[0] in NUMS and ln[1] not in NUMS:
            whole[(ln[1], NUMS[ln[0]][1], NUMS[ln[0]][0])] += 1
    per = defaultdict(Counter)
    for (b, s, v), c in whole.items():
        per[(b, s)][v] += c
    say('| sign | series | values (count) |')
    say('|---|---|---|')
    for (b, s), c in sorted(per.items(), key=lambda x: -sum(x[1].values())):
        if sum(c.values()) >= 3:
            say('| %s | %s | %s |' % (b, s, ', '.join('%d x%d' % kv for kv in sorted(c.items()))))
    say()
    say('## N5 Counted or fixed? How much the value varies before each sign')
    say()
    say('A sign that is counted takes several values; a numeral + sign pair whose value never '
        'changes is a fixed compound (a name or term with a number in it), not a count. Signs with '
        '10+ numeral tokens in one series:')
    say()
    say('| series | sign | tokens | values | commonest value (share) | verdict |')
    say('|---|---|---|---|---|---|')
    for (s, b), c in sorted(by_noun.items(), key=lambda x: -sum(x[1].values())):
        n = sum(c.values())
        if n < 10:
            continue
        v, k = c.most_common(1)[0]
        verdict = 'fixed' if k / n >= 0.9 else ('counted' if len(c) >= 3 and k / n < 0.75 else 'mostly one value')
        say('| %s | %s | %d | %s | %d (%.0f%%) | %s |' % (s, b, n, ', '.join(str(x) for x in sorted(c)),
                                                        v, 100 * k / n, verdict))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'numerals.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
