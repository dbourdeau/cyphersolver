"""Escalation for the five open signs 28 83 117 20 66 (passage 1).
Each sign may be any glyph look-alike in this hand (digit confusions 1/7, 2/7, 3/5/8, 6/0/8/b, 4/9)
or, for the 'bb' glyph, one or two of key 255's syllable signs whose shape is a stem with a loop
(au, mm, ch, st, tt). Up to two signs changed. Scored with lang de-1640s in context."""
import os, sys, itertools
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here); sys.path.insert(0, os.path.join(here, '..', '..'))
from decrypt import NUM, NULLS
from lang import lm
m = lm.load('de-1640s')
LOOK = {'1': '17', '7': '172', '2': '27', '3': '358', '5': '538', '8': '8360', '6': '608', '0': '06', '4': '49', '9': '94'}
def variants(tok):
    out = {}
    for i, ch in enumerate(tok):
        for alt in LOOK.get(ch, ch):
            t = tok[:i] + alt + tok[i+1:]
            n = int(t)
            if n in NUM: out.setdefault(NUM[n], t)
            elif n in NULLS or n < 20: out.setdefault('', t)
    return out
base = ['28', '83', '117', '20', '66']
opts = [variants(t) for t in base]
opts[4].update({'au': 'au', 'mm': 'mm', 'ch': 'ch', 'st': 'st', 'tt': 'tt', 'auau': 'au au', 'mmmm': 'mm mm'})
basev = ['e', 'r', 't', 'a', 'd']
pre, post = 'die landstaende totaliter disgustirt und ', ' in holstein nun sowol als in dennemarck adel buerger und bauern'
res = []
for k in (0, 1, 2):
    for pos in itertools.combinations(range(5), k):
        for vals in itertools.product(*[list(opts[p]) for p in pos]):
            w = basev[:]
            for p, v in zip(pos, vals): w[p] = v
            word = ''.join(w)
            s = pre + word + post
            res.append((m.per_char(lm.norm(s, 'early')), k, word, [(base[p], opts[p][v]) for p, v in zip(pos, vals)]))
res.sort(key=lambda r: -r[0])
seen = set()
for r in res:
    if r[2] in seen: continue
    seen.add(r[2]); print('%.4f %d %-12s %s' % r)
    if len(seen) >= 40: break
