"""Decode the corrected transcription with Prizmic's key (key.json) and test it against shuffled keys.

Run from the repository root:  python targets/malatesta1428/dec.py
Signs are Tomokiyo's labels; an empty value is a null, "[?]" an unread sign.
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
from lang import lm

key = json.load(open(os.path.join(HERE, 'key.json'), encoding='utf8'))
rows = [l.strip(';\n') for l in open(os.path.join(HERE, 'transcription_tomokiyo_corrected.txt'), encoding='utf8')
        if l.strip() and not l.startswith('#')]
runs = [rows[0:3], rows[3:6], rows[6:10]]

def decode(k, toks):
    return ''.join('?' if k[t] == '[?]' else k[t] for t in toks)

all_toks = []
for n, r in enumerate(runs, 1):
    toks = [t for row in r for t in row.split(';') if t]
    all_toks += toks
    print('RUN %d  %d signs' % (n, len(toks)))
    print(decode(key, toks))
print('%d signs, %d distinct, %d nulls, %d unread' % (
    len(all_toks), len(set(all_toks)), sum(key[t] == '' for t in all_toks), sum(key[t] == '[?]' for t in all_toks)))

text = decode(key, all_toks).replace('?', '')
m = lm.load('la')
true = m.per_char(text)
signs = [s for s in key if key[s] not in ('', '[?]')]
vals = [key[s] for s in signs]
random.seed(1)
ctrl = []
for _ in range(300):
    random.shuffle(vals)
    k = dict(key); k.update(zip(signs, vals))
    ctrl.append(m.per_char(decode(k, all_toks).replace('?', '')))
print('Latin model "la", per letter: this key %.2f; 300 shuffled keys: best %.2f, mean %.2f' % (
    true, max(ctrl), sum(ctrl) / len(ctrl)))
print('best language:', lm.best_language(text)[:3])
