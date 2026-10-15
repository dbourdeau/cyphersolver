"""Shuffle control for f. 88r (issue #32, tunarob). Decodes the contributor's R3-R6 cipher tokens (first variant of
each {a|b}) with corrected key no. 60, finds the longest lexicon word (>= 6 letters; lexicon = lang/corpora/fr-henri4.txt
plus the Instruction print, words seen >= 2 times) spelled by consecutive tokens, and compares it with 5000 random
permutations of the same tokens. Run: python -X utf8 shuffle_control.py
"""
import os, re, sys, random, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(HERE, '..'))
from decode60 import KEY

K = dict(KEY)
# copyist forms and contributor tags not in the decoder; 2+ taken as u (u|i is not a single letter); oo+ = word sign
K.update({'Ⱡ': 'so', 'ıı': 'o', '-///': 'si', 'ꝑ': 'so', 'e': 'to', '11': 'u', 'oꝛ': 'luy', 'w': 'fu',
          '2+': 'u', 'oo+': '', '30': 'x', '10': 'p', '12': 'du', '16': 'fe', '20': 'u'})
R = {'R3': "to g ı L x ‡ q λ q π ⊥ y v r 2+ Δ T R ꝺ o– Ⱡ ∂ ⱶⱶ ıı",
     'R4': "T ∂ ꝑ L σ f E ꝶ L T",
     'R5': "to oꝛ g ∂ o– Ⱡ ſ+ 20 8 ++ π ⊥",
     'R6': "12 –Δ (m 7 c 12 16 F oo+ ſ+ o w L x –o– e y 2+ ∞ ꝑ q 10 E q 4 x x ur f++ ∂ π c L x q 30 11 Δ ſ ıı"}
toks = [t for k in R for t in R[k].split()]

def strip(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if c.isalpha() and ord(c) < 128)

# lang/corpora is git-ignored; set CYPHER_CORPORA if this checkout has no copy
cdir = os.environ.get('CYPHER_CORPORA', os.path.join(ROOT, 'lang', 'corpora'))
txt = open(os.path.join(cdir, 'fr-henri4.txt'), encoding='utf8', errors='ignore').read()
txt += open(os.path.join(HERE, '..', '..', 'nevers1593', 'instruction_31aug_print.txt'), encoding='utf8').read()  # stays in nevers1593 (shared source)
wc = Counter(strip(w) for w in re.findall(r"\w+", txt))
lex = {w for w, c in wc.items() if len(w) >= 6 and c >= 2}

def dec(ts):
    return [K.get(t, '?') for t in ts]

def stat(ts):
    d = dec(ts); best = 0; word = ''
    for i in range(len(d)):
        s = ''
        for j in range(i, min(i + 14, len(d))):
            if not d[j].isalpha():
                break
            s += d[j]
            if len(s) >= 6 and s in lex and len(s) > best:
                best, word = len(s), s
    return best, word

print('lexicon words (>=6 letters):', len(lex))
print('tokens:', len(toks))
print('decode:', ' '.join(dec(toks)))
obs, w = stat(toks)
print('observed longest word:', obs, w)
random.seed(1); n = 5000; ge = 0
for _ in range(n):
    t = toks[:]; random.shuffle(t)
    if stat(t)[0] >= obs:
        ge += 1
print(f'shuffles >= observed: {ge}/{n}; P = {(ge + 1) / (n + 1):.5f}')
