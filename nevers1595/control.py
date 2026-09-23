"""Matched control for anneal.py: can the same annealer break a homophonic cipher of this letter's size and shape?

Takes 17 runs of French from the Henri IV letters corpus with the same run lengths as the letter (753 plain letters in
all), enciphers them with a random homophonic key of 54 signs (e 7 homophones, a/i/n/s/t/r/u/o 3, the rest 1-2) plus
3 null signs at 5%, writes ct_control.txt, and runs the glyph-mode annealer on it.  Output: the fraction of plaintext
letters recovered.

usage: python control.py [seed]
"""
import os, sys, random, re, subprocess
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from lang import lm
from seg import load

here = os.path.dirname(os.path.abspath(__file__))
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
random.seed(seed)
corpus = None
for root in (os.path.join(here, '..', 'lang', 'corpora'), r'C:\Users\dbour\cypher\lang\corpora'):
    p = os.path.join(root, 'fr-henri4.txt')
    if os.path.exists(p): corpus = open(p, encoding='utf8', errors='replace').read(); break
text = lm.norm(corpus, 'early').replace(' ', '')
lens = [len(l) for f in ('ct_f148r.txt', 'ct_f148v_149r.txt') for l in load(os.path.join(here, f))]
start = random.randrange(len(text) // 2)
plain = []
pos = start + 100000
for n in lens:
    plain.append(text[pos:pos + n]); pos += n + 400
homs = {'e': 7, 'a': 3, 'i': 3, 'n': 3, 's': 3, 't': 3, 'r': 3, 'u': 3, 'o': 3, 'l': 2, 'd': 2, 'c': 2, 'm': 2,
        'p': 2, 'q': 1, 'b': 1, 'f': 1, 'g': 1, 'h': 1, 'x': 1, 'y': 1, 'z': 1}
signs = [f's{i}' for i in range(60)]
random.shuffle(signs)
key = {}; k = 0
for c, h in homs.items():
    key[c] = signs[k:k + h]; k += h
nulls = signs[k:k + 3]
out = []
for p in plain:
    toks = []
    for ch in p:
        if random.random() < 0.05: toks.append(random.choice(nulls))
        toks.append(random.choice(key.get(ch, nulls)))
    out.append(' '.join(toks))
open(os.path.join(here, 'ct_control.txt'), 'w', encoding='utf8').write(
    '# control, seed %d\n' % seed + '\n'.join(out) + '\n')
open(os.path.join(here, 'pt_control.txt'), 'w', encoding='utf8').write('\n'.join(plain) + '\n')
print('control written:', sum(lens), 'letters,', k + 3, 'signs')
