"""Write the Cardona transcriptions as one token file for the vich1515 annealer (syl.py real): one written line per
row, block frame marks dropped. syl.py treats lower-case alphabetic tokens of 2+ letters as code groups and
everything else as signs, so sign labels that are lower-case letters get upper-case aliases."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from load import lines
ALIAS = {'gto': 'GTO', 'oo': 'OO', 'ff': 'FF', 'll': 'LL', 'ef': 'EF'}   # ef = barred o + loop stroke, a sign pair
DROP = {'ratio', '¶'}
out = ['# cardona1517 A-D for wsa4 (scripts/to_wsa.py); aliases ' + ' '.join(f'{a}={b}' for a, b in ALIAS.items())]
for b in 'ABCD':
    for tag, ts in lines(b):
        out.append(' '.join(ALIAS.get(t, t) for t in ts if t not in DROP))
open(sys.argv[1], 'w').write('\n'.join(out) + '\n')
