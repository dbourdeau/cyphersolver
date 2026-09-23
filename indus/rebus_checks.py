"""Test Parpola's 1994 rebus readings (Deciphering the Indus Script, Fig. 15.2 and Appendix)
against the corpora and against a chance baseline built from the Dravidian lexicon.

R1  Numerals before the plain fish, by stroke count, against the Tamil star names with a
    numeral first member in Parpola's own list of -min compounds (rebus/min_compounds.tsv).
R2  'Ligatured fish signs are never doubled or preceded by numbers' (1994: 196).
R3  The 24 readings of Fig. 15.2: how often each sign or sequence occurs (ICIT and M77) and,
    for sequences, whether the pair is above a within-line shuffle.
R4  Chance baseline for the check "the compound is attested in Tamil": for a fixed list of
    picture concepts, how often some Tamil word for the picture (Dravidian Database, DEDR
    lemmas) is the first member of a Tamil star name in -min, strictly and with the
    sound latitude the readings use (ai/ay/ey, final -am/-u/-i).

Usage: python rebus_checks.py <dedr_entry_v11.csv> <m77_indusscript_real_corpus.csv>
Writes results/rebus_checks.md.
"""
import csv
import math
import os
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict

from signs import FISH, NUMERAL, load

HERE = os.path.dirname(os.path.abspath(__file__))
random.seed(1994)
OUT = []


def say(s=''):
    OUT.append(s)
    print(s)


# --------------------------------------------------------------------------- lexicon
def simplify(w):
    """Tamil romanisation -> plain key: r-underdot-diaeresis (zh) -> l, drop diacritics,
    reduce geminates. The same function is applied to lemmas and to the -min keys."""
    w = w.lower().replace('r̤', 'l').replace('ḻ', 'l')   # r̤ / ḻ = zh
    w = unicodedata.normalize('NFD', w)
    w = ''.join(ch for ch in w if not unicodedata.combining(ch))
    w = re.sub(r'[^a-z]', '', w)
    return re.sub(r'(.)\1+', r'\1', w)


def loosen(k):
    k = re.sub(r'(ay|ey|ei)', 'ai', k)
    k = re.sub(r'(am|m|u|i)$', '', k) if len(k) > 3 else k
    return k


def load_min():
    rows = []
    with open(os.path.join(HERE, 'rebus', 'min_compounds.tsv'), encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('#') or ln.startswith('class'):
                continue
            c, comp, key, gloss = ln.rstrip('\n').split('\t')
            rows.append((c, comp, simplify(key), gloss))
    return rows


def load_tamil(path):
    words = defaultdict(set)      # simplified form -> meanings
    for r in csv.DictReader(open(path, encoding='utf-8')):
        if r['lang_str'] != 'Tamil':
            continue
        form = r['entry_str'].split('(')[0].split(',')[0].strip().strip('-').strip(')')
        form = form.split()[0] if form.split() else ''
        k = simplify(form)
        if len(k) >= 2:
            words[k].add(r['entry_meaning'].lower())
    return words


CONCEPTS = """man woman person fish jar pot vessel cup arrow bow spear lance comb ladder tree leaf fig
banyan crab bird snake bee insect scorpion turtle tortoise crocodile bull cow buffalo elephant
rhinoceros tiger goat deer antelope squirrel dog eye hand foot leg head horn mountain hill sun moon
river water rain field house roof fence wheel drum rope knot net basket boat bangle ring bracelet
stone hearth fire flower grain seed sprout stool seat cloth knife axe sword shield flag lamp mortar
pestle sieve plough yoke cart bone feather egg shell claw tail wing road door pillar post""".split()
TAMIL_NUMERALS = {1: ['oru', 'or', 'onru'], 2: ['iru', 'ir', 'irantu'], 3: ['mu', 'mun', 'munru'],
                  4: ['nal', 'nan', 'nanku'], 5: ['ai', 'aim', 'aintu'], 6: ['aru'], 7: ['elu'],
                  8: ['en', 'ettu'], 12: ['panniru', 'pannirantu']}


def words_for(concept, tamil, primary=False):
    """Tamil words whose DEDR gloss names the concept; primary=True looks only at the first
    sense (the gloss up to the first ';' or ',')."""
    pat = re.compile(r'\b%s(s|es)?\b' % re.escape(concept))
    if primary:
        return {k for k, ms in tamil.items() if any(pat.search(re.split('[;,]', m)[0]) for m in ms)}
    return {k for k, ms in tamil.items() if any(pat.search(m) for m in ms)}


def r4(tamil, mins):
    star = {k for c, _, k, _ in mins if 'S' in c}
    allk = {k for _, _, k, _ in mins}
    lstar = {loosen(k) for k in star}
    say('## R4 Chance baseline for "the compound is attested in Tamil"')
    say()
    say('Picture concepts: a fixed list of %d things the Indus signs are commonly taken to depict '
        '(set in the script before running it). For each, the Tamil words whose DEDR gloss names '
        'it; a hit is a word that is the first member of a Tamil star name in -min (%d distinct '
        'keys in Parpola\'s list) or of any -min compound (%d keys). Strict = same simplified form '
        '(no diacritics, geminates reduced) or +/- final u; loose = also ai/ay/ey and a dropped '
        'final -am/-m/-u/-i, the latitude used for mey/may/mai and vatam/vata.' % (
            len(CONCEPTS), len(star), len(allk)))
    say()
    for primary in (True, False):
        k1 = k2 = k3 = 0
        for c in CONCEPTS:
            ws = words_for(c, tamil, primary)
            k1 += any(w in star or w + 'u' in star or w.rstrip('u') in star for w in ws)
            k2 += any(loosen(w) in lstar for w in ws)
            k3 += any(w in allk or w + 'u' in allk or w.rstrip('u') in allk for w in ws)
        n = len(CONCEPTS)
        say('- %s: a Tamil word beginning a star name, strict %d/%d (%.0f%%), loose %d/%d (%.0f%%); '
            'beginning any -min compound, strict %d/%d (%.0f%%).' % (
                'first sense of the gloss only' if primary else 'any sense of the gloss',
                k1, n, 100 * k1 / n, k2, n, 100 * k2 / n, k3, n, 100 * k3 / n))
    say()
    strict_s = loose_s = any_s = 0
    rows = []
    for c in CONCEPTS:
        ws = words_for(c, tamil)
        hs = {w for w in ws if w in star or w + 'u' in star or w.rstrip('u') in star}
        hl = {w for w in ws if loosen(w) in lstar}
        ha = {w for w in ws if w in allk or w + 'u' in allk or w.rstrip('u') in allk}
        strict_s += bool(hs)
        loose_s += bool(hl)
        any_s += bool(ha)
        rows.append((c, len(ws), sorted(hs), sorted(hl - hs), sorted(ha)))
    n = len(CONCEPTS)
    say('- median Tamil words per concept: %d (the choice of synonym is part of the method).'
        % sorted(r[1] for r in rows)[n // 2])
    say()
    say('Hits by concept (any sense of the gloss):')
    say()
    say('| concept | Tamil words | star-name hits (strict) | extra hits (loose) |')
    say('|---|---|---|---|')
    for c, k, hs, hl, ha in rows:
        if hs or hl:
            say('| %s | %d | %s | %s |' % (c, k, ' '.join(hs) or '-', ' '.join(hl) or '-'))
    say()
    say('Numerals: the Tamil numeral forms used in compounds (hand list), against the star-name '
        'keys, exactly or through a homophone after simplification (e.g. nal "four" = nal "day"):')
    for v, forms in TAMIL_NUMERALS.items():
        hs = sorted({f for f in forms if simplify(f) in star})
        say('- %d (%s): %s' % (v, ', '.join(forms), ' '.join(hs) or 'no star name'))


# --------------------------------------------------------------------------- corpora
def m77_lines(path):
    return [r['sign_sequence'].split() for r in csv.DictReader(open(path, encoding='utf-8'))]


def pairs(lines, A, B):
    return sum(1 for ln in lines for a, b in zip(ln, ln[1:]) if a in A and b in B)


def shuffled_ge(lines, A, B, obs, n=300):
    k = 0
    for _ in range(n):
        c = 0
        for ln in lines:
            s = ln[:]
            random.shuffle(s)
            c += sum(1 for a, b in zip(s, s[1:]) if a in A and b in B)
        k += c >= obs
    return k


def expected(lines, A, B):
    first, second, nb = Counter(), Counter(), 0
    for ln in lines:
        for a, b in zip(ln, ln[1:]):
            first[a] += 1
            second[b] += 1
            nb += 1
    return sum(first[a] for a in A) * sum(second[b] for b in B) / nb


M = lambda *n: {'MSg%d' % i for i in n}
# Fig. 15.2, in reading order. ICIT glyph sets; M77 sets through align_m77.py (None = no
# counterpart found). 'squirrel' is unidentified in ICIT: 263 is the closest shape.
READINGS = [
    (1, 'fish', 'min', [{'220'}], [M(59)]),
    (2, 'fish + fish', 'min + min', [{'220'}, {'220'}], [M(59), M(59)]),
    (3, '3 + fish', 'mu-m-min', [{'3', '33'}, {'220'}], [M(102, 89), M(59)]),
    (4, '6 + fish', 'aru-min', [{'16'}, {'220'}], [M(109), M(59)]),
    (5, '7 + fish', 'elu-min', [{'17'}, {'220'}], [M(112), M(59)]),
    (6, 'roof + fish', 'mai-m-min', [{'235'}], [M(65)]),
    (7, 'halving + fish', 'pacu + min', [{'233'}], [M(72)]),
    (8, 'dot + fish', 'pottu + min', [{'231'}], [M(70)]),
    (9, 'eye', 'kan', [{'809', '832'}], [M(375)]),
    (10, 'eye + eye', 'kan-kani', [{'809', '832'}, {'809', '832'}], [M(375), M(375)]),
    (11, 'rings / bangles', 'muruku', [{'840'}], [M(403)]),
    (12, 'hearth + rings', 'cul + muruku', [{'13'}, {'840'}], [M(103), M(403)]),
    (13, 'rings + squirrel', 'muruku + pillai', [{'840'}, {'263'}], None),
    (14, 'rings + space', 'muruku + vel', [{'840'}, {'32'}], [M(403), M(87)]),
    (15, 'space + fish', 'vel-min', [{'32'}, {'220'}], [M(87), M(59)]),
    (16, 'fig + fish', 'vata-min', [{'772', '773', '776', '783', '784', '785', '786'}, {'220'}],
     [M(348, 367, 370, 371), M(59)]),
    (17, 'fig + space', 'vata + vel', [{'772', '773', '776', '783', '784', '785', '786'}, {'32'}],
     [M(348, 367, 370, 371), M(87)]),
    (18, '4 + fig', 'nal + vata', [{'4', '14'}, {'772', '773', '776', '783', '784', '785', '786'}],
     [M(104), M(348, 367, 370, 371)]),
    ('18b', '4 + branched sign 405/407 (if that is his fig)', 'nal + vata', [{'4', '14'}, {'405', '407'}],
     [M(104), M(169)]),
    (19, 'fig + crab (ligature)', 'koli', [{'777', '778', '782'}], None),
    (20, 'crab', 'kol', [{'798', '794'}], [M(53, 58)]),
    (21, 'crab + fish', 'kon-min', [{'798', '794'}, {'220'}], [M(53, 58), M(59)]),
    (22, 'pot', '-', [{'700'}], [M(328)]),
    (23, 'man', 'al', [{'90'}], [M(1)]),
    (24, 'cow head (the jar)', 'a (possessive)', [{'740'}], [M(342)]),
]


def r3(icit, m77):
    say('## R3 The 24 readings of Fig. 15.2 in the corpora')
    say()
    say('Counts in reading order; for two-sign readings, expected count if the two signs were '
        'independent, and how many of 300 within-line shuffles reach the observed count '
        '(0/300 = above chance, p < 0.004).')
    say()
    say('| no. | sign or sequence | Dravidian | ICIT | exp. | shuffles | M77 | exp. | shuffles |')
    say('|---|---|---|---|---|---|---|---|---|')
    for no, lab, dr, ic, mm in READINGS:
        cells = []
        for lines, sets in ((icit, ic), (m77, mm)):
            if sets is None:
                cells += ['n/a', '', '']
            elif len(sets) == 1:
                cells += [str(sum(1 for ln in lines for g in ln if g in sets[0])), '', '']
            else:
                obs = pairs(lines, sets[0], sets[1])
                cells += [str(obs), '%.1f' % expected(lines, sets[0], sets[1]),
                          '%d' % shuffled_ge(lines, sets[0], sets[1], obs)]
        say('| %s | %s | %s | %s |' % (no, lab, dr, ' | '.join(cells)))
    say()


def r1_r2(icit, m77):
    say('## R1 Numerals before the plain fish')
    say()
    say('Parpola 1994: 194: "the numbers actually attested before the \'fish\' sign in the Indus '
        'inscriptions are restricted to 3, 4, 6 and 7. The hypothesis of a Dravidian pun offers an '
        'alternative which explains this restriction". His Tamil list has star names in -min for '
        '3 (mu-m-min), 5 (ai-m-min), 6 (aru-min) and 7 (elu-min), and 4 only through the homophone '
        'nal "four" / nal "day" (nal-min "asterism"); none for 1, 2, 8 or 12. '
        'Two long strokes (ICIT 32, M77 87) are left out here: Parpola reads them as '
        '\'intermediate space\' (vel-min, Venus, R3 no. 15). The pair of short strokes (ICIT 2, '
        'M77 99) is his most frequent non-numeral sign.')
    say()
    icit_num = {k: v for k, v in NUMERAL.items() if k not in ('32', '2')}
    m77_num = {'MSg97': 1, 'MSg102': 3, 'MSg103': 3, 'MSg104': 4, 'MSg106': 5, 'MSg109': 6,
               'MSg112': 7, 'MSg114': 8, 'MSg86': 1, 'MSg89': 3, 'MSg96': 5, 'MSg121': 12}
    a = Counter(icit_num[x] for ln in icit for x, y in zip(ln, ln[1:]) if x in icit_num and y == '220')
    b = Counter(m77_num[x] for ln in m77 for x, y in zip(ln, ln[1:]) if x in m77_num and y == 'MSg59')
    say('| number | Tamil star name in -min | ICIT | M77 |')
    say('|---|---|---|---|')
    names = {3: 'mu-m-min (Mrgasiras)', 4: 'only through a homophone: nal-min "day-star, asterism"',
             5: 'ai-m-min (Hasta / Rohini)', 6: 'aru-min (Pleiades)', 7: 'elu-min (Ursa Major)'}
    for v in sorted(set(a) | set(b) | set(names)):
        say('| %d | %s | %d | %d |' % (v, names.get(v, 'none'), a[v], b[v]))
    sa = sum(a.values())
    sb = sum(b.values())
    ra = sum(a[v] for v in names)
    rb = sum(b[v] for v in names)
    say()
    say('- numeral + fish tokens whose number has a Tamil star name: ICIT %d of %d (%.0f%%), '
        'M77 %d of %d (%.0f%%).' % (ra, sa, 100 * ra / sa, rb, sb, 100 * rb / sb))
    say()
    say('## R2 Numerals before ligatured fish')
    say()
    lig = FISH - {'220', '219'}
    c = Counter((x, y) for ln in icit for x, y in zip(ln, ln[1:])
                if x in NUMERAL and x not in ('2', '32') and y in lig)
    say('- ICIT, stroke numerals other than the short and long pairs, before a ligatured fish: '
        '%d; %s' % (sum(c.values()), dict(c.most_common(8))))
    c = Counter((x, y) for ln in m77 for x, y in zip(ln, ln[1:])
                if x in m77_num and y in M(*range(60, 76)))
    say('- M77, same: %d; %s' % (sum(c.values()), dict(c.most_common(8))))
    say('- the short pair (ICIT 2) before a ligatured fish: %d; the plain fish doubled: ICIT %d, '
        'M77 %d; a ligatured fish doubled: ICIT %d.' % (
            sum(1 for ln in icit for x, y in zip(ln, ln[1:]) if x == '2' and y in lig),
            sum(1 for ln in icit for x, y in zip(ln, ln[1:]) if x == y == '220'),
            sum(1 for ln in m77 for x, y in zip(ln, ln[1:]) if x == y == 'MSg59'),
            sum(1 for ln in icit for x, y in zip(ln, ln[1:]) if x == y and x in lig)))
    say()


def main(dedr, m77path):
    icit = [ln for r in load() for ln in r['seq']]
    m77 = m77_lines(m77path)
    say('# Parpola 1994 rebus readings: corpus and lexical checks')
    say()
    r1_r2(icit, m77)
    r3(icit, m77)
    r4(load_tamil(dedr), load_min())
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'rebus_checks.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
