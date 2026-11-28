"""After the plan: compare the Danish held-out key (first line of work/runs/heldout_afterplan_da.txt, built from lines
1-6 of transcription_frozen.txt) with the final key (key.tsv) on the held-out lines 7-12, letter by letter.
usage: python3 -I targets/vind1647/work/scripts/agreement.py"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from common import read_lines
T = HERE.parents[1]
k2 = json.loads((T / 'work' / 'runs' / 'heldout_afterplan_da.txt').read_text(encoding='utf-8').splitlines()[0])['key']
key = {}
for line in open(T / 'key.tsv', encoding='utf-8'):
    if line.startswith('sign') or not line.strip(): continue
    s, p = line.split('\t')[:2]; key[s] = p
words = read_lines()
held = ''.join(w for ln, w in words if ln >= 7); train = ''.join(w for ln, w in words if ln <= 6)
agree = sum(k2.get(c) == key[c] for c in held)
diff = sorted(s for s in k2 if k2[s] != key[s])
print('held-out letters (lines 7-12 of transcription_frozen.txt) decoded as by key.tsv: %d of %d' % (agree, len(held)))
print('values of the lines 1-6 key equal to key.tsv: %d of %d; differing signs: %s' % (len(k2) - len(diff), len(k2), ', '.join(diff)))
print('occurrences of the differing signs in lines 1-6: %s' % ', '.join('%s %d' % (s, train.count(s)) for s in diff))
