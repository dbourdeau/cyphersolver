"""Lead 1: the copper-tablet sign = image equations as rebus tests, in three languages.

The tablets fix, without any language, what four signs stand for: 777 (fig + crab ligature)
= markhor goat and horned archer; 749 (jar with limbs and three strokes) = markhor goat;
753 (jar with a wheel inside) = hare; 341 = rhinoceros (a drawing of a horned quadruped: a
logogram, no rebus needed). If a compound sign is a rebus, some word for its component
pictures (or two of them joined) should sound like a word for its animal, in the right language.

E1  For Dravidian (all DEDR languages), Sanskrit (Monier-Williams) and Sumerian (ePSD2):
    for each compound sign, the best sound match (1 - normalised edit distance on simplified
    forms) between component words and words for its animal, and its rank against the same
    score for 24 control animals. A language whose puns underlie the signs should rank the true
    animal near the top.
E2  The jar ligatures as abbreviations: how often the corpus writes the ligature's parts as
    a sequence (wheel 820 then jar 740; the fig + crab parts).

Usage: python equation_rebus.py dedr_entry_v11.csv mw.txt sux_gloss.tsv
Writes results/equation_rebus.md.
"""
import csv
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

import rebus_checks as rc
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
SIGNS = {'777': (['fig', 'crab'], ['goat', 'archer']),
         '749': (['jar', 'man', 'three'], ['goat']),
         '753': (['jar', 'wheel'], ['hare'])}
PAT = {'fig': r'\b(fig|banyan|ficus)', 'crab': r'\bcrabs?\b', 'jar': r'\b(jar|pot|pitcher|vessel)s?\b',
       'man': r'\b(man|person|male)\b', 'three': r'\bthree\b', 'wheel': r'\bwheels?\b',
       'goat': r'\b(goat|he-goat|she-goat)s?\b', 'archer': r'\b(archer|bowman)s?\b', 'hare': r'\b(hare|rabbit)s?\b'}
CONTROLS = ['dog', 'horse', 'cow', 'bull', 'buffalo', 'elephant', 'tiger', 'lion', 'deer', 'pig', 'sheep',
            'camel', 'cat', 'monkey', 'bear', 'wolf', 'snake', 'bird', 'rat', 'frog', 'tortoise', 'crocodile',
            'peacock', 'jackal']


def say(s=''):
    OUT.append(s)
    print(s)


def plain(w):
    w = unicodedata.normalize('NFD', w.lower().replace('r̤', 'l'))
    w = ''.join(c for c in w if not unicodedata.combining(c))
    return re.sub(r'(.)\1+', r'\1', re.sub(r'[^a-z]', '', w))


def ed(a, b):
    d = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, cb in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (ca != cb))
    return d[len(b)]


def sim(a, b):
    return 1 - ed(a, b) / max(len(a), len(b)) if a and b else 0


def lexicon_dedr(path):
    out = []
    for r in csv.DictReader(open(path, encoding='utf-8')):
        f = r['entry_str'].split('(')[0].split(',')[0].strip().strip('-').strip(')')
        f = f.split()[0] if f.split() else ''
        out.append((plain(f), re.split('[;,]', r['entry_meaning'].lower())[0]))
    return out


def lexicon_mw(path):
    out = []
    cur = None
    slp = str.maketrans({'A': 'a', 'I': 'i', 'U': 'u', 'f': 'r', 'F': 'r', 'x': 'l', 'E': 'ai', 'O': 'au',
                         'K': 'k', 'G': 'g', 'C': 'c', 'J': 'j', 'T': 't', 'D': 'd', 'P': 'p', 'B': 'b',
                         'w': 't', 'W': 't', 'q': 'd', 'Q': 'd', 'R': 'n', 'N': 'n', 'Y': 'n', 'M': 'm',
                         'S': 's', 'z': 's', 'H': 'h'})
    with open(path, encoding='utf-8') as f:
        for ln in f:
            if ln.startswith('<L>'):
                m = re.search(r'<k1>([^<]*)', ln)
                cur = [m.group(1) if m else '', '']
            elif ln.startswith('<LEND>'):
                if cur and cur[0]:
                    g = re.sub(r'<[^>]+>', ' ', cur[1].split('¦', 1)[-1])
                    first = re.split(r'[;,(]', g.strip())[0].lower()
                    if not re.match(r'^\s*((m|f|n|mfn|ind)\.\s*)*n\.\s*of\b', first):
                        out.append((re.sub(r'(.)\1+', r'\1', cur[0].translate(slp).lower()), first))
                cur = None
            elif cur is not None:
                cur[1] += ln
    return out


def lexicon_sux(path):
    return [(plain(r['cf']), (r['gw'] + ' ' + r['senses']).lower())
            for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t') if r['pos'] == 'N']


def words(lex, concept):
    pat = re.compile(PAT.get(concept, r'\b%ss?\b' % concept))
    return {w for w, g in lex if w and pat.search(g)}


def cap(ws, n=60):
    return sorted((w for w in ws if 3 <= len(w) <= 9), key=lambda w: (len(w), w))[:n]


def best(parts, targets):
    """Best sound match between a target word and a component word, or two component words
    joined, keeping only joins about the target's length that start with its first sound
    (the rebus principle: the pun has to begin where the word begins)."""
    parts = [cap(p) for p in parts]
    targets = cap(targets, 80)
    top = (0, '', '')
    for t in targets:
        for p in parts:
            for x in p:
                s = sim(x, t)
                if s > top[0]:
                    top = (s, x, t)
        for i, a in enumerate(parts):
            for j, b in enumerate(parts):
                if i == j:
                    continue
                for x in a:
                    if x[0] != t[0]:
                        continue
                    for y in b:
                        if abs(len(x) + len(y) - len(t)) <= 2:
                            s = sim(x + y, t)
                            if s > top[0]:
                                top = (s, x + y, t)
    return top


def main(dedr, mw, sux):
    say('# The tablet equations as rebus tests')
    say()
    langs = {'Dravidian (DEDR)': lexicon_dedr(dedr), 'Sanskrit (MW)': lexicon_mw(mw), 'Sumerian (ePSD2)': lexicon_sux(sux)}
    say('## E1 Sound match between the component pictures and the animal, ranked against 24 control animals')
    say()
    say('| language | sign | components | animal | best match | score | rank of the true animal (1 = best of 25; ties count against it) |')
    say('|---|---|---|---|---|---|---|')
    for lname, lex in langs.items():
        for s, (comp, animals) in SIGNS.items():
            parts = [words(lex, c) for c in comp]
            ctrl = {}
            for a in CONTROLS:
                ctrl[a] = best(parts, words(lex, a))[0]
            for a in animals:
                sc, c, t = best(parts, words(lex, a))
                rank = 1 + sum(1 for v in ctrl.values() if v >= sc)   # ties count against the true animal
                say('| %s | %s | %s (%s words) | %s (%d words) | %s ~ %s | %.2f | %d |' % (
                    lname, s, ' + '.join(comp), '/'.join(str(len(p)) for p in parts), a,
                    len(words(lex, a)), c, t, sc, rank))
    say()
    say('## E2 The jar ligatures as written-out sequences')
    say()
    L = [ln for r in load() if r['flat'] for ln in r['seq']]
    pairs = Counter((a, b) for ln in L for a, b in zip(ln, ln[1:]))
    tot = Counter(g for ln in L for g in ln)
    for a, b, lab in (('820', '740', 'wheel 820 then jar 740 (753 = jar with wheel inside)'),
                      ('33', '740', 'three long strokes then jar (749 has three strokes inside)'),
                      ('798', '740', 'crab then jar'), ('90', '740', 'man then jar'), ('740', '90', 'jar then man')):
        say('- %s: %d times (820 alone %d, 740 alone %d).' % (lab, pairs[(a, b)], tot['820'], tot['740'])
            if a == '820' else '- %s: %d times.' % (lab, pairs[(a, b)]))
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'equation_rebus.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:4])
