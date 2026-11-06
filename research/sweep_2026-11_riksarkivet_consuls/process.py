"""python process.py <man> [strict=20] : after a volume is fetched, write its 300-px contact sheets (page_vol.sheets) and its
digit-run scores (digitscan -> <SP>/scan/<man>.tsv), and print the images whose strict score >= threshold (or whose relaxed
score >= 25), for viewing at 800 px."""
import os
import sys

from digitscan import scan_volume
from page_vol import HI, sheets
from rik_common import SP

man = sys.argv[1]
thr = int(sys.argv[2]) if len(sys.argv) > 2 else 20
os.makedirs(os.path.join(SP, 'scan'), exist_ok=True)
out = scan_volume(os.path.join(HI, man), os.path.join(SP, 'scan', f'{man}.tsv'))
rows = [tuple(int(v) for v in l.split('\t')) for l in open(out)]
flag = [r for r in rows if r[1] >= thr or r[3] >= 25]
print('sheets:', len(sheets(man)))
print('flagged', len(flag), 'of', len(rows))
print(' '.join(f'{r[0]}({r[1]}/{r[2]}/{r[3]})' for r in flag))
