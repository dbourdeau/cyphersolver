"""In-sample reference only: decode the TRAIN leaves with the frozen key and score against the clear training text
(same letter scoring as score_clear.py). Not a held-out figure."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import decode_once as DO  # noqa (prints the held-out decode again; output ignored)
import score_clear as SC
from common import read_tx
D = '/home/claude/keyless/round40c/basel_anv9/'
d = ''
for f in ('tx/f004r.txt', 'tx/f004v.txt'):
    for lid, ws in read_tx(D + f):
        for w in ws:
            d += DO.decode_word(w)[0]
r = SC.letters(SC.norm(' '.join(l for l in open(D + 'tx/CLEAR_TRAIN.txt') if not l.startswith('#')), True))
e, m = SC.lev(SC.letters(SC.norm(d, True)), r)
print('TRAIN in-sample: clear letters %d, decoded letters %d, matches %d, edits %d -> %.1f%% of clear letters reproduced' % (len(r), len(d), m, e, 100.0 * m / len(r)))
