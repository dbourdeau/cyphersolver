"""Escalation: the 1672 table differs from the 1666 one in at least one cell (55 = g, not h; glosser read 66 as r or z).
Let the two signs not confirmed elsewhere in this letter (117 and the 'bb' sign) take any letter or syllable value;
score 'und er X a Y in holstein' and 'und er X a Y in' joined, with de-1640s."""
import os, sys, itertools
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', '..'))
from lang import lm
m = lm.load('de-1640s')
V = list('abcdefghiklmnopqrstuwxyz') + ['au','eu','ei','ie','ch','ck','ff','ll','mm','nn','pp','rr','sch','ss','st','tt','tz','']
pre = 'die landstaende totaliter disgustirt und '; post = ' holstein nun sowol als in dennemarck adel buerger und bauern'
res = []
for x, y in itertools.product(V, V):
    for w in ('er%sa%s in' % (x, y), 'er%sa%sin' % (x, y)):
        s = pre + w + post
        res.append((m.per_char(lm.norm(s, 'early')), w))
res.sort(reverse=True)
for r in res[:40]: print('%.4f %s' % r)
