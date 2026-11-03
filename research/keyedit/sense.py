"""Sense proxy (targets/martinique1778/measure_sense.py, strict) for a keyedit session's key on f.88. usage: sense.py SESSION"""
import json, sys
SES = sys.argv[1]
key = {g: v for g, v in json.load(open(SES + '/state.json', encoding='utf-8'))['key'].items() if v}

import os, re, sys, math, collections
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'targets', 'martinique1778'); M = os.path.join(HERE, '..', 'mercier1761')
sys.path.insert(0, M); sys.path.insert(0, os.path.join(HERE, '..', '..'))
from solve import norm
import wordscore
wordscore.HERE = r'C:/Users/dbour/cypher/targets/mercier1761'   # corpora are not checked out in cyph-merge; read-only use of the main checkout's lang/corpora
words = wordscore.load_words()
# declared additions: words of the letters (period spellings, proper nouns) missing from the corpus sample
for w in ['martinique', 'guadeloupe', 'garnison', 'hopital', 'hopitaux', 'recrues', 'recrue', 'escadre', 'deffense', 'deffendre',
          'moitie', 'troupes', 'premier', 'mois', 'etat', 'situation', 'colonie', 'critiques', 'honneur', 'compte', 'vous', 'isle']:
    words.setdefault(norm(w), -8.0)
for w in ['l', 'd', 'n', 's', 'c', 'j', 'm', 't']: words[w] = -9.0
toks = [t for l in open(os.path.join(HERE, 'transcription.txt'), encoding='utf8') if l[0] != '#' for t in l.split()]
# runs of valued tokens only
runs, cur = [], []
for g in toks:
    if g in key: cur.append(g)
    else:
        if cur: runs.append(cur); cur = []
if cur: runs.append(cur)
ok = 0; fails = []
for run in runs:
    text, spans = '', []
    for g in run:
        a = len(text); text += key[g]; spans.append((g, a, len(text)))
    n = len(text); best = [0.0] + [-math.inf] * n; back = [None] * (n + 1)
    for i in range(n):
        if best[i] == -math.inf: continue
        if best[i] - 12 > best[i + 1]: best[i + 1], back[i + 1] = best[i] - 12, (i, False)
        for j in range(i + 1, min(n, i + 25) + 1):
            w = words.get(text[i:j])
            if w is not None and (j - i >= 2 or text[i:j] in ('a', 'y') or (text[i:j] in 'ldnscjmt' and j < n and text[j] in 'aeiouyh')) and best[i] + w > best[j]:
                best[j], back[j] = best[i] + w, (i, True)
    good = [False] * n; k = n
    while k:
        i, isw = back[k]
        if isw:
            for c in range(i, k): good[c] = True
        k = i
    for g, a, b in spans:
        if b > a and all(good[a:b]): ok += 1
        else: fails.append(g)
tot = len(toks)
print('tokens', tot, 'valued', sum(t in key for t in toks), '= %.1f%%' % (100 * sum(t in key for t in toks) / tot))
print('sense proxy (strict, runs cut at unvalued groups): %d/%d tokens = %.1f%%' % (ok, tot, 100 * ok / tot))
print('valued but failing:', collections.Counter(fails).most_common(30))
