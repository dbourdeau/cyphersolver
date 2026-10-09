"""LM search for the unread word in passage 1 (tokens 28 83 117 20 BB = e r t a z before 'in Holstein'):
allow up to two of the five letter tokens to take any value (copy slips), score with de-1640s."""
import os, sys, itertools
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from lang import lm
m = lm.load('de-1640s')
pre, post = 'landstaende totaliter disgustirt und ', 'in holstein nun sowol als in dennemarck'
base = list('ertad')
alpha = 'abcdefghiklmnopqrstuwz'
res = []
for k in (0, 1, 2):
    for pos in itertools.combinations(range(5), k):
        for vals in itertools.product(alpha, repeat=k):
            w = base[:]
            for p, v in zip(pos, vals): w[p] = v
            for sp in ('', ' '):  # word may end before 'in' or 'in' continue the word
                s = pre + ''.join(w) + sp + post
                res.append((m.per_char(lm.norm(s, 'early')), k, ''.join(w) + sp))
res.sort(reverse=True)
for r in res[:40]: print('%.4f %d %r' % r)
