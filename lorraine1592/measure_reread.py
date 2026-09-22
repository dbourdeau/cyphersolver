"""Measure the re-read of BnF fr. 3621 no. 97 (ct/no97_reread.txt).

RULE (what "read as sense" means here):
  * The unit is the cipher token of the transcription: one letter sign (a doubled letter written with
    dots is one token), one special sign, one null, or one nomenclator figure.
  * The reading groups tokens into words and grades each word H/C/M/I (H secure, C probable,
    M doubtful, I unread). A token is READ if its word is graded H or C, i.e. the word is a French
    word (or a null) that fits the sentence around it. M and I words are not read.
  * Each word is also decoded mechanically with the pair key below; where that decode differs
    from the stated reading, the word is an emendation (a glyph read differently with the key in
    hand, or a marked scribal slip). Emendations are counted and listed, so the reading cannot
    quietly depart from the key.
  * BEFORE: the same words decoded with the 18 Sept key and the 18 Sept tokens
    (no97_solution.txt, no97_eye.txt token names); a token counts as read-before if its word's old
    decode equals the reading. That is the old key's share of the text as now read.

usage: python measure_reread.py [--words]
"""
import re, sys, os, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))

PAIRS = "ai bp cf dq et gu ly mz ns or hx"
KEY = {}
for p in PAIRS.split():
    KEY[p[0]] = p[1]; KEY[p[1]] = p[0]
KEY.update({
    'v': 'r',      # the open o-form, a variant of o -> r
    'x': '',       # the looped ae sign: null
    'A': '',       # the large barred A: null
    'Z': '',       # reversed 3: null in most places
    'G': 'u',      # g with overbar: the ordinary g of this hand -> u
    'B': 'p',      # beta-like b -> p (the looped h, -> x, is marked B:x)
    'T': 'e', 'C': 't', 'J': 's', 'D': 's', 'L': 'u', 'H': 'h', 'Q': 'a',
    'N': 'ss',     # n with two dots under: doubled
    'K': 'ff',     # c with two dots under: doubled
    'S': 'nt',     # long s with overbar (abbreviation)
    'R': 'o', 'j': 'e',
})
UNKNOWN = set('WMUYEPOFV')   # special signs with no settled value

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isalpha())
    return s.replace('j', 'i').replace('v', 'u')

def decode(tokens, key, use_override=True):
    out = []
    for t in tokens:
        base, _, ov = t.partition(':')
        if use_override and ':' in t:
            out.append(ov)
        elif base in UNKNOWN or base not in key:
            out.append('?')
        else:
            out.append(key[base])
    return ''.join(out)

def old_key():
    k = {}
    for l in open(os.path.join(HERE, 'ct', 'no97_solution.txt'), encoding='utf-8'):
        m = re.match(r'\s+(\S) -> (\S)', l)
        if m: k[m.group(1)] = m.group(2)
    k['x'] = k.get('x', 's')
    return k

def main():
    show = '--words' in sys.argv
    OLD = old_key()
    tot = rd = fig = figrd = before = 0
    emend = []
    grades = {}
    lines = 0
    for l in open(os.path.join(HERE, 'ct', 'no97_reread.txt'), encoding='utf-8'):
        if not re.match(r'L\d\d:', l): continue
        lines += 1
        lab, rest = l.split(':', 1)
        for w in rest.split():
            toks, _, pg = w.rpartition('=')
            plain, _, g = pg.rpartition('/')
            grades[g] = grades.get(g, 0)
            if toks.startswith('<'):
                n = 1; fig += 1
                if g in 'HC': figrd += 1
            else:
                tl = toks.split('.')
                n = len(tl)
                dec = decode(tl, KEY)
                if g in 'HC' and norm(dec) != norm(plain):
                    emend.append(f'{lab} {w}  key gives "{dec}"')
                if g in 'HC' and norm(decode(tl, OLD, use_override=False)) == norm(plain):
                    before += n
                if show: print(f'{lab} {plain:16s} {g} {n:2d} {dec}')
            grades[g] += n
            tot += n
            if g in 'HC': rd += n
    print(f'lines {lines}  cipher tokens {tot}  (of which nomenclator figures {fig})')
    print(f'tokens by grade: ' + '  '.join(f'{g} {n}' for g, n in sorted(grades.items())))
    print(f'READ (words graded H or C): {rd}/{tot} = {rd/tot:.3f}')
    lt = tot - fig; lr = rd - figrd
    print(f'  letter signs only: {lr}/{lt} = {lr/lt:.3f};  figures read {figrd}/{fig}')
    print(f'BEFORE (old key + old tokens give the same word): {before}/{tot} = {before/tot:.3f}')
    print(f'emendations among read words (reading differs from the key decode): {len(emend)}')
    for e in emend: print('  ' + e)

if __name__ == '__main__':
    main()
