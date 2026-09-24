"""Linear B as a second known-answer control for the bench (bench.py).

Linear B (Mycenaean Greek, deciphered by Ventris 1952) is scored with the same method the Indus keys face: each
inscription line, read without its word dividers (the Indus script has none), is reduced to a skeleton and parsed into
Greek words; the real sign values against 100 shuffles of them among signs of similar frequency.

Data (scratchpad; not redistributed): DAMOS (Database of Mycenaean at Oslo, CC BY-NC-SA 4.0), the syllabic words of
every line, fragments left out; the syllabogram values of the standard grid; Greek word forms in Latin letters (LSJ
headwords and the Homeric forms, Perseus, CC BY-SA).

Lexicon versions: (1) the Greek forms as they are; (2) adjusted to Linear B spelling: l written r, final s / n / r
dropped (Linear B does not write them). Each scored consonant-only (bench.skel) and with vowels (bench.skelv).

Usage: python linb_control.py path/to/linb
Writes results/linb_control.md.
"""
import csv
import os
import random
import re
import sys
from collections import Counter

import bench

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = []
random.seed(167)


def say(s=''):
    OUT.append(s)
    print(s)


def adjust(w):
    w = w.lower().replace('l', 'r')
    return re.sub(r'[snr]+$', '', w) or w


def main(d):
    vals = {}
    for r in csv.DictReader(open(os.path.join(d, 'syllabograms.csv'), encoding='utf-8')):
        if r['value'] and r['value'] != '?':
            vals[r['sign']] = r['value']
    lines = []
    for ln in open(os.path.join(d, 'corpus_damos_lines.txt'), encoding='utf-8'):
        parts = ln.rstrip('\n').split('\t')
        if len(parts) < 3:
            continue
        signs = []
        for tok in parts[2].split():
            if tok.startswith('~') or not re.match(r'^[a-z0-9*]+(-[a-z0-9*]+)*$', tok) or tok.isdigit():
                continue
            signs.extend(tok.split('-'))
        if len(signs) >= 3:
            lines.append(signs)
    key = {g: vals[g] for g in {s for t in lines for s in t} if g in vals}
    freq = Counter(s for t in lines for s in t)
    words = [w.strip() for w in open(os.path.join(d, 'greek', 'greek_translit_wordlist.txt'), encoding='utf-8') if w.strip()]
    say('# Linear B as a known-answer control')
    say()
    say('- DAMOS lines with 3+ syllabic signs: %d (%d sign tokens, %d sign types, %d with a standard value, %.0f%% of '
        'tokens); Greek forms: %d.' % (len(lines), sum(freq.values()), len(freq), len(key),
                                       100 * sum(freq[g] for g in key) / sum(freq.values()), len(words)))
    say()
    say('| lexicon | scoring | real key | shuffles median (range) | shuffles as good |')
    say('|---|---|---|---|---|')
    for lab, ws in (('Greek forms as they are', words), ('adjusted to Linear B spelling (l > r, no final s/n/r)',
                                                         [adjust(w) for w in words])):
        for mode, sk, ends, ml in (('consonants only', bench.skel, set('snr'), 8),
                                   ('vowels kept', bench.skelv, set('SNR'), 12)):
            lex = {sk(w) for w in ws if sk(w)}
            real = bench.score(lines, key, lex, ends, sk, ml)
            sims = sorted(bench.score(lines, k2, lex, ends, sk, ml) for k2 in bench.shuffles(key, freq, n=100, band=10))
            say('| %s | %s | %.1f%% | %.1f%% (%.1f-%.1f) | %d of 100 |' % (
                lab, mode, 100 * real, 100 * sims[50], 100 * sims[0], 100 * sims[-1], sum(1 for x in sims if x >= real)))
    say()
    say('A correct key should beat its shuffles; the bench is trustworthy for Indus keys only in the settings where it '
        'does so here and on Linear Elamite.')
    os.makedirs(os.path.join(HERE, 'results'), exist_ok=True)
    with open(os.path.join(HERE, 'results', 'linb_control.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(OUT) + '\n')


if __name__ == '__main__':
    main(sys.argv[1])
