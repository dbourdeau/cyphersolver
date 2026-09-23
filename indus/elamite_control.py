"""Linear Elamite as a control for the test bench: does a real decipherment beat its own shuffles?

Linear Elamite (Iran, late 3rd millennium BCE) was deciphered by Desset, Tabibzadeh, Kervran,
Basello and Marchesi (2022). The Elamicon/OCLEI corpus (59 texts, sign variants as Private Use
codepoints) and its table of 260 variants -> 70 sound values (Desset 2022, Maeder et al. 2018 and
others) give a real sign key. The lexicon is the headwords of Hallock's Glossary of Achaemenid
Elamite (OIP 92, 1969; the OCR text, parsed crudely) - a thousand years later than the texts, so
a conservative test.

E1  The key against 200 shuffles (values permuted among keyed signs of similar frequency), on the
    same consonant-skeleton parse as bench.py, with Elamite suffix consonants (r, k, p, n, m, t)
    as endings; and against the Sanskrit, Dravidian and Sumerian lexicons.
E2  The corpus beside the Indus corpus: texts, tokens, sign types, signs used once, mean text.

Usage: python elamite_control.py <elamicon texts csv> <elamicon signvalues csv> <hallock ocr txt>
       <mw.txt> <dedr forms.csv> <sux_gloss.tsv>
Writes results/elamite_control.md.
"""
import csv
import os
import random
import re
import sys
from collections import Counter

import bench
from signs import load

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
random.seed(101)


def say(s=''):
    OUT.append(s)
    print(s)


def load_le(texts_csv, values_csv):
    key = {}
    for r in csv.DictReader(open(values_csv, encoding='utf-8')):
        v = re.sub(r'[₀-₉0-9]', '', r['value'])
        for cp in r['pua_codepoints'].split():
            key[cp.replace('U+', '')] = v
    texts = []
    for r in csv.DictReader(open(texts_csv, encoding='utf-8')):
        for ln in r['codepoints'].split('/'):
            t = ln.split()
            if len(t) >= 3:
                texts.append(t)
    return key, texts


def hallock(path, sk=None):
    sk = sk or bench.skel
    words = set()
    for ln in open(path, encoding='utf-8'):
        m = re.match(r"^\s*(?:I{1,3}V?\.,?\s+)?([A-Za-zÀ-ž'’\-\[\]]{2,}(?:\(\?\))?)\s*\(", ln)
        if m:
            w = m.group(1).replace('(?)', '').replace('[', '').replace(']', '').strip("-'’")
            w = w.replace('S', 'š') if w[:1].islower() else w[0] + w[1:].replace('S', 'š')
            x = sk(w)
            if x:
                words.add(x)
    return words


def main(texts_csv, values_csv, hall, mw, dedr, sux):
    key = {}
    for r in csv.DictReader(open(values_csv, encoding='utf-8')):
        v = re.sub(r'[₀-₉0-9]', '', r['value'])
        for cp in r['pua_codepoints'].split():
            key[cp.replace('U+', '')] = v
    texts = []
    for r in csv.DictReader(open(texts_csv, encoding='utf-8')):
        for ln in r['codepoints'].split('/'):
            t = ln.split()
            if len(t) >= 3:
                texts.append(t)
    freq = Counter(g for t in texts for g in t)
    lex, _, _ = bench.lexicons(mw, dedr, sux)
    lex['elx'] = hallock(hall)
    ends = dict(bench.ENDINGS)
    ends['elx'] = set('rkpnmt')
    say('# Linear Elamite: a real decipherment on the bench')
    say()
    kt = sum(freq[g] for g in key)
    say('- %d lines of 3+ signs; %d sign tokens, %d sign variants; %d variants keyed (%d sound values), %.0f%% of '
        'tokens. Hallock headword skeletons: %d.' % (len(texts), sum(freq.values()), len(freq),
                                                     sum(1 for g in freq if g in key), len(set(key.values())),
                                                     100 * kt / sum(freq.values()), len(lex['elx'])))
    say()
    say('| lexicon | real key | shuffles median (range) | shuffles as good |')
    say('|---|---|---|---|')
    names = {'elx': 'Elamite (Hallock 1969)', 'sa': 'Sanskrit', 'dra': 'Dravidian', 'sux': 'Sumerian'}
    for L in ('elx', 'sa', 'dra', 'sux'):
        real = bench.score(texts, key, lex[L], ends[L])
        sims = sorted(bench.score(texts, k2, lex[L], ends[L]) for k2 in bench.shuffles(key, freq, n=200, band=10))
        ge = sum(1 for s in sims if s >= real)
        say('| %s | %.1f%% | %.1f%% (%.1f-%.1f) | %d of 200 |' % (names[L], 100 * real, 100 * sims[100], 100 * sims[0],
                                                                100 * sims[-1], ge))
    say()
    lxv = hallock(hall, bench.skelv)
    real = bench.score(texts, key, lxv, set('RKPNMT'), bench.skelv, 12)
    sims = sorted(bench.score(texts, k2, lxv, set('RKPNMT'), bench.skelv, 12)
                  for k2 in bench.shuffles(key, freq, n=200, band=10))
    say('- E1v with the vowels kept (bench.skelv, three vowel classes): Elamite %.1f%% against shuffles %.1f%% '
        '(%.1f-%.1f), %d of 200 as good. The consonant-only test cannot see this real key; the vowel-aware one '
        'can.' % (100 * real, 100 * sims[100], 100 * sims[0], 100 * sims[-1], sum(1 for s in sims if s >= real)))
    say()
    say('## E2 Beside the Indus corpus')
    say()
    for lab, tt in (('Linear Elamite (Elamicon)', texts),
                    ('Indus (ICIT-derived)', [ln for r in load() for ln in r['seq'] if len(ln) >= 3])):
        f = Counter(g for t in tt for g in t)
        n = sum(f.values())
        say('- %s: %d lines, %d tokens, %d sign types, %.0f%% of types used once, mean line %.1f signs.' % (
            lab, len(tt), n, len(f), 100 * sum(1 for c in f.values() if c == 1) / len(f), n / len(tt)))
    say()
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'elamite_control.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(*sys.argv[1:7])
