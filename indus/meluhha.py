"""Seventh pass, lead 5: the two Meluhhan personal names in cuneiform against the Indus name slot.

Laursen and Steinkeller (2017: 83-84) identify the only two personal names that may be Meluhhan:
Na-na-za and Sab-ma-ar (Samar), royal slaves and bezoar shepherds, oil allotment of 'the men of
Meluhha', Nisaba 15 371 (Urusagrig, Su-Suen 6). Two properties can be set against the seals:

- length: 3 and 2 syllables. On a logo-syllabic script (1-2 syllables a sign) a name of 2-3
  syllables takes 1-3 signs. What share of seal name slots (the text less the opening formula
  and the ending) is 1-3 signs long?
- reduplication: Na-na-za opens with a doubled syllable. How often does an Indus name slot open
  with the same sign twice, against the rate of doubled signs anywhere in the slot?

With two names neither is a test of the language; the aim is to state whether the seals leave
room for names of this shape.

Writes results/meluhha.md.
"""
import os
from collections import Counter

from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
OPENERS = {'817', '820', '861'}


def say(s=''):
    OUT.append(s)
    print(s)


def slot(t):
    if len(t) >= 2 and t[0] in OPENERS and t[1] in ('2', '60', '1'):
        t = t[2:]
    if len(t) >= 2 and t[-1] in ('400', '90', '151') and t[-2] in ('740', '520'):
        t = t[:-2]
    elif t and t[-1] in ('740', '520'):
        t = t[:-1]
    return t


def main():
    rows = [r for r in load() if r['flat'] and r['type'] == 'SEAL:S' and len(r['seq']) == 1]
    slots = [slot(r['seq'][0]) for r in rows]
    slots = [s for s in slots if s]
    ln = Counter(min(len(s), 7) for s in slots)
    n = len(slots)
    say('# The Meluhhan names Nanaza and Samar against the Indus seal name slot')
    say()
    say('- square seals with one line, name slot (text less opener formula and ending) non-empty: %d.' % n)
    say('- slot length: %s (7 = 7 or more); 1-3 signs: %d (%.0f%%).' % (
        ', '.join('%d: %d' % kv for kv in sorted(ln.items())), sum(ln[k] for k in (1, 2, 3)),
        100 * sum(ln[k] for k in (1, 2, 3)) / n))
    two = [s for s in slots if len(s) >= 2]
    init = sum(1 for s in two if s[0] == s[1])
    anyw = sum(1 for s in two for a, b in zip(s, s[1:]) if a == b)
    pairs = sum(len(s) - 1 for s in two)
    say('- slots of 2+ signs opening with a doubled sign: %d of %d (%.1f%%); doubled adjacent signs anywhere in '
        'the slot: %d of %d pairs (%.1f%%).' % (init, len(two), 100 * init / len(two), anyw, pairs, 100 * anyw / pairs))
    say('- the doubled openers: %s.' % ', '.join('%s x%d' % kv for kv in Counter(
        s[0] for s in two if s[0] == s[1]).most_common(8)))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'meluhha.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main()
