"""python batch.py [ref-substring ...] : 600-px, 3-column contact sheet (rik_sheet3.py, 15 images from image 2 on) for each
unit in units.json (all, in file order, if no argument). Skips sheets already made. Logs to batch3.log in the scratch dir.
Sequential, ~1 request/s. (The first pass used 300-px tiles, 6 columns; they hid a page of mixed number groups and words,
so every volume was re-sheeted at 600 px.)"""
import json
import os
import subprocess
import sys

from rik_common import SP

HERE = os.path.dirname(os.path.abspath(__file__))
u = json.load(open(os.path.join(HERE, 'units.json'), encoding='utf-8'))
sel = [x for x in u if x.get('man') and x.get('n') and (len(sys.argv) < 2 or any(s in x['ref'] for s in sys.argv[1:]))]
for x in sel:
    p = os.path.join(SP, f"{x['man']}_2_{x['n']}_L.jpg")
    if os.path.exists(p):
        continue
    r = subprocess.run([sys.executable, os.path.join(HERE, 'rik_sheet3.py'), x['man'], str(x['n']), '15', '2', str(x['n'])],
                       capture_output=True, text=True, cwd=HERE)
    with open(os.path.join(SP, 'batch3.log'), 'a', encoding='utf-8') as f:
        f.write(f"{x['ref']}\t{x['man']}\t{x['n']}\t{r.stdout.strip()}{r.stderr.strip()[-200:]}\n")
