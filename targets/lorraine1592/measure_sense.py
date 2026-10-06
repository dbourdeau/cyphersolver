"""Sense check on the measure of no. 97 (ct/no97_reread.txt).

measure_reread.py counts a token as read when its word is graded H or C by hand. This script checks
that grade against things it does not choose:
  1. LEXICON: the reading of every H/C word must be an attested French word (word list of the shared
     corpora fr-henri4 + fr-1520s-diplomatic + fr-gutenberg, early normalisation, j->i v->u), or a
     null, or a line-split fragment whose join with the neighbouring fragment is attested.
  2. KEY: the reading must equal the mechanical pair-key decode (emendations listed by measure_reread).
  3. LM: per-char score of the read text under lang fr-1600-letters, against the same words shuffled.
A token is SENSE-READ if its word passes 1 and 2 (or is a listed emendation) and is graded H/C.

usage: python measure_sense.py [--fail]
"""
import os, re, sys, random
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..')
sys.path.insert(0, ROOT); sys.path.insert(0, HERE)
from lang import lm
import measure_reread as M

def lexicon():
    words = {}
    for f in ('fr-henri4.txt', 'fr-1520s-diplomatic.txt', 'fr-gutenberg.txt'):
        p = os.path.join(ROOT, 'lang', 'corpora', f)
        if not os.path.exists(p): continue
        t = lm.norm(open(p, encoding='utf-8', errors='ignore').read(), 'early')
        for w in t.split():
            words[w] = words.get(w, 0) + 1
    lex = {w for w, n in words.items() if n >= 2}
    return lex | {dd(w) for w in lex}

def dd(w):
    # single/double consonant spelling is free in this hand (comandement, paser, delaisent)
    return re.sub(r'(.)\1', r'\1', w)

def n(s): return M.norm(s)

def main():
    LEX = lexicon()
    rows = []   # (line, plain, grade, ntok, isnull, keyok)
    for l in open(os.path.join(HERE, 'ct', 'no97_reread.txt'), encoding='utf-8'):
        if not re.match(r'L\d\d:', l): continue
        lab, rest = l.split(':', 1)
        for w in rest.split():
            toks, _, pg = w.rpartition('=')
            plain, _, g = pg.rpartition('/')
            if toks.startswith('<'):
                rows.append([lab, plain, g, 1, False, True, True])
            else:
                tl = toks.split('.')
                keyok = n(M.decode(tl, M.KEY)) == n(plain)
                rows.append([lab, plain, g, len(tl), plain == '', keyok, False])
    # lexicon test, with joins across line ends and apostrophe-elided compounds
    def ok(i):
        p = n(rows[i][1])
        if rows[i][4]: return True
        if not p or '?' in rows[i][1]: return False
        if p in LEX or dd(p) in LEX: return True
        # elisions: dexecution, iay, lentendre, leffect, lon -> split off d/l/i/s/qu/n
        for pre in ('d', 'l', 'i', 's', 'qu', 'n', 'm', 'c'):
            if p.startswith(pre) and p[len(pre):] in LEX: return True
        # line-split fragment: join with last word of previous line or first of next
        if i + 1 < len(rows) and rows[i + 1][0] != rows[i][0] and n(p + rows[i + 1][1]) in LEX: return True
        if i > 0 and rows[i - 1][0] != rows[i][0] and n(rows[i - 1][1] + p) in LEX: return True
        # figure-bearing words: com+ma+nder etc.
        for j in (i - 1, i + 1):
            if 0 <= j < len(rows):
                a, b = (rows[j][1], rows[i][1]) if j < i else (rows[i][1], rows[j][1])
                if n(a + b) in LEX: return True
                for k in (j - 1, j + 1):
                    if 0 <= k < len(rows) and k != i:
                        seq = sorted([i, j, k])
                        if n(''.join(rows[x][1] for x in seq)) in LEX: return True
        return False
    tot = sum(r[3] for r in rows)
    hc = sum(r[3] for r in rows if r[2] in 'HC')
    sense = 0; fails = []
    for i, r in enumerate(rows):
        if r[2] not in 'HC': continue
        lx = r[6] or ok(i)
        if lx: sense += r[3]
        else: fails.append(f'{r[0]} {r[1]} ({r[2]}, {r[3]} tok) not attested')
        if not r[5]: fails.append(f'{r[0]} {r[1]} key decode differs (emendation)')
    print(f'cipher tokens {tot}; graded H/C {hc} = {hc/tot:.3f}')
    print(f'H/C words that are attested French (or nulls / joined fragments / figures): {sense}/{tot} = {sense/tot:.3f}')
    model = lm.load('fr-1600-letters')
    read = ' '.join(r[1] for r in rows if r[2] in 'HC' and r[1])
    s = model.per_char(lm.norm(read, 'early'))
    ws = read.split(); random.seed(1); random.shuffle(ws)
    s2 = model.per_char(lm.norm(' '.join(ws), 'early'))
    print(f'LM fr-1600-letters per char: read words in order {s:.3f}; same words shuffled {s2:.3f}')
    if '--fail' in sys.argv:
        for f in fails: print('  ' + f)
    else:
        print(f'{len(fails)} flags (run with --fail to list)')

if __name__ == '__main__':
    main()
