"""Write ciphertext_schenck.txt: per letter, every cipher number in order (2-digit letter cipher from
transcr/RUNS_FINAL.txt runs, 3-digit codes from codes.json order), one line per letter, record id first."""
import json, os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__))
runs = collections.defaultdict(list)
for l in open(os.path.join(HERE, 'transcr', 'RUNS_FINAL.txt'), encoding='utf-8'):
    if not l.startswith('R74'): continue
    f = [x.strip() for x in l.split('|')]
    if len(f) < 5 or 'not a run' in f[4]: continue
    runs[f[0].split()[0]] += re.findall(r'\d+', f[1])
codes = json.load(open(os.path.join(HERE, 'codes.json'), encoding='utf-8'))
cod = collections.defaultdict(list)
for c, occ in codes.items():
    for o in occ: cod[o[0]].append(c)
with open(os.path.join(HERE, 'ciphertext_schenck.txt'), 'w', encoding='utf-8') as f:
    f.write('# Vienna -> Schenck 1706: per letter, the letter-cipher numbers (runs, in order) then the code numbers\n')
    for r in sorted(set(runs) | set(cod)):
        f.write(r + ' ' + ' '.join(runs[r]) + ' ' + ' '.join(cod[r]) + '\n')
