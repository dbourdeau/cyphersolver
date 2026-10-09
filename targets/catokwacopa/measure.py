"""Sense measure for the Catokwacopa pair (5 Oct 2026).

The 21 Sept figure (0.747) counted every character of a line as read whenever any published reading existed for
it, so it credited line 6 (SAID SIMPLY YOUR CAP IS HONESTY IN CHARACTER, 7 misprints), line 19 (BALLIOL MAN POSTED,
11 misprints), line 21 (HAD EXAMINATION, 3), line 5 (1 misprint, not the top fit), line 13 (no reading at all) and
the A.P. 138 line, whose meaning nobody knows. It measured coverage by proposals, not sense.

Here a cipher character counts as read only when
  * it is consumed, with no misprint, by a reading that the letters force: the reading is the top fit of the
    open-vocabulary search (search.py, no names) or of the phrase-level 5-gram search (beam.py), or it is a name
    frame that admits exactly one of 1,645 corpus names (names.py); and
  * the credited words score as English under lang en-modern (per char > -2.5; real text -1.1 to -1.8).
Where only the head of a line is forced, only the head's letters are credited (READ[ln] = letters of A, of B).
Numerals count when they read as the years of the Oxford reading (53/18 = 1853 etc.).

Usage: python measure.py
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from lang import lm
import mech
from ads import PAIRS

# line: (reading credited, letters of A read, letters of B read, basis)
READ = {
    1: ('summer term', None, None, 'search top (sum term); same words'),
    2: ('1853', None, None, 'numerals: year, cf. 22'),
    3: ('cap took away at college party', None, None, 'search + beam top; at college/catalogue the only rival'),
    4: ('old cap broke at corner left instead', None, None, 'search top'),
    6: ('used simply your cap', 10, 6, 'head forced in both searches (side/used simply your cap; SAID needs a misprint); tail open'),
    7: ('repeated', None, None, 'search + beam top'),
    8: ('i attended conington lecsures', None, None, 'name frame: Conington only'),
    10: ('hertford scholarship examination', None, None, 'name frame: Hertford only'),
    11: ('1853 4', None, None, 'numerals: year'),
    14: ('months previously disclosed', 10, 7, 'search + beam top for the head; adverb privately/previously; tail indulge/in college open'),
    15: ('conington told us to add a second motto', None, None, 'name frame: Conington only'),
    16: ('i added first line satirs', None, None, 'search top + positional rule'),
    17: ('qui fit', None, None, 'Latin search top (Horace)'),
    18: ('change adopted', None, None, 'search + beam top, exact'),
    22: ('1855 6', None, None, 'numerals: year'),
    24: ('told shirley', None, None, 'name frame: Shirley only'),
    25: ('i attended jowett lecsurs', None, None, 'name frame: Jowett only'),
    27: ('dying', None, None, 'exact, 0 omissions'),
    28: ('declaration', None, None, 'exact, 0 omissions'),
}
UNREAD = {
    5: 'CONINGTON MET ME IN GARDEN needs a misprint; searches give conviction/convention me me garden',
    9: 'mistrl/otenpu: phrase LM gives mist often purely; no forced reading',
    12: 'phrase LM: case land clutch so find size ...; junk',
    13: '1.6.9 / cotegr: no reading',
    19: 'BALLIOL MAN POSTED needs 11 misprints; phrase LM junk',
    20: 'A.P. 138: plain in both ads, meaning unknown',
    21: 'HOLIDAYS EXAMINE vs how days examine vs hold say mixing: not decided',
    23: 'phrase LM: with you but portion frog fit ...; junk',
    26: 'mistrl/oatvpu: moist relative put; junk',
    29: 'terrible flowed to him bare; junk; Latin junk',
}


# for the English test only: names to a common noun, W.'s spellings to standard, Latin to a gloss
LM_FORM = {'conington': 'smith', 'jowett': 'smith', 'shirley': 'smith', 'hertford': 'college', 'lecsures': 'lectures',
           'lecsurs': 'lectures', 'satirs': 'satires', 'qui fit': 'how comes'}


def lm_form(r):
    r = ' ' + r + ' '
    for k, v in LM_FORM.items(): r = r.replace(' ' + k + ' ', ' ' + v + ' ')
    return r


def chars(s): return sum(c.isalnum() for c in s)


def main():
    M = lm.load('en-modern')
    tot = rd = 0; tA = tB = rA = rB = 0
    print('%-3s %-26s %-16s %5s %5s  %s' % ('ln', 'A / B', '', 'chars', 'read', 'reading / reason'))
    for n, (A, B) in enumerate(PAIRS, 1):
        a, b = chars(A), chars(B); tot += a + b; tA += a; tB += b
        if n in READ:
            r, ra, rb, basis = READ[n]
            ra = a if ra is None else ra; rb = b if rb is None else rb
            if A.isalpha() and B.isalpha():
                c = mech.cost(r, A[:ra], B[:rb])
                assert c is not None and c[1] == 0, (n, r, c)
                pc = M.per_char(lm_form(r))
                assert pc > -2.5, (n, r, pc)
            rd += ra + rb; rA += ra; rB += rb
            print('%-3d %-43s %5d %5d  %s  [%s]' % (n, A + ' / ' + B, a + b, ra + rb, r.upper(), basis))
        else:
            print('%-3d %-43s %5d %5d  -- %s' % (n, A + ' / ' + B, a + b, 0, UNREAD[n]))
    print('\n8 May ad: %d/%d = %.3f   20 May ad: %d/%d = %.3f' % (rA, tA, rA / tA, rB, tB, rB / tB))
    print('overall: %d/%d characters read as sense = %.3f' % (rd, tot, rd / tot))


if __name__ == '__main__':
    main()
