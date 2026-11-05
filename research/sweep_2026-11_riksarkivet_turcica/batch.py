"""python batch.py <ref-suffix> ... : contact sheet (24 samples) for each unit in units.json whose ref ends with a suffix.
Skips sheets already made. Logs to batch.log."""
import json
import os
import subprocess
import sys

from rik_common import SP

u = json.load(open('units.json', encoding='utf-8'))
for suf in sys.argv[1:]:
    x = next(x for x in u if x['ref'].endswith(suf))
    p = os.path.join(SP, f"{x['man']}_1_{x['n']}.jpg")
    if os.path.exists(p):
        continue
    r = subprocess.run([sys.executable, 'rik_sheet.py', x['man'], str(x['n'])], capture_output=True, text=True)
    with open('batch.log', 'a', encoding='utf-8') as f:
        f.write(f"{x['ref']}\t{x['man']}\t{x['n']}\t{r.stdout.strip()}{r.stderr.strip()[-200:]}\n")
