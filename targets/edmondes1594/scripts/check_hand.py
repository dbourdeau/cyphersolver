"""Check the hand reading against the printed cipher: lengths, and the shift each printed letter needs
(24-letter alphabet; printed u tried as cipher n and as u, printed v as cipher u)."""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import poly, multishift as ms
A = ms.A
segs, labels = poly.read_ct(os.path.join(HERE, '..', 'transcription', 'pass1.txt'))
hand = {}
for l in open(os.path.join(HERE, '..', 'reading', 'reading_hand.tsv')).read().splitlines()[1:]:
    k, v = l.split('\t'); hand[k] = v
PREF = (7, 8, 10, 20, 11)
tot = collections.Counter(); per = collections.defaultdict(collections.Counter); nread = 0; nall = 0; odd = []
for lab, s in zip(labels, segs):
    p = hand.get(lab, '?' * len(s))
    if len(p) != len(s): print('LENGTH', lab, len(s), len(p)); continue
    for c, q in zip(s, p):
        nall += 1
        if q == '?': continue
        nread += 1
        q = q.lower().replace('j', 'i').replace('v', 'u')
        cands = {'u': ['n', 'u'], 'v': ['u']}.get(c, [c])
        sh = sorted(((A.index(q) - A.index(cc)) % 24 for cc in cands), key=lambda x: (x not in PREF, PREF.index(x) if x in PREF else 99))[0]
        tot[sh] += 1; per[c][sh] += 1
        if sh not in PREF: odd.append((lab, c, q, sh))
print(f'read {nread} of {nall} printed letters = {100*nread/nall:.1f}%')
print('shift use:', tot.most_common())
print('per printed letter:', {c: dict(per[c]) for c in sorted(per)})
print('letters outside 7/8/10/11/20:', odd)
