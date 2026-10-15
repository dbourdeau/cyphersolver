"""Build validation.tsv for the Vienna -> Schenck letter cipher (R7486-R7500), the part broken ciphertext-only:
every number of every run in transcr/RUNS_FINAL.txt, in file order, with the letter of the run's decoding column
(one letter per number; key_table rule of decode_out.py where the lengths differ). Runs measure.py counts as giving
no sense (NO_SENSE) are unread. The 3-digit codes (5 of 77 with a context value) and the Sieniawski letters (other
keys, mostly read at the time) are not included."""
import re, pathlib, sys
H = pathlib.Path(__file__).parent; sys.path.insert(0, str(H))
from measure import NO_SENSE
from key import letter
T = {'70': 'w', '76': 'y', '77': 'y', '78': 'y', '79': 'z'}
out = ['# model: de-1740s', '# source: transcr/RUNS_FINAL.txt runs (numbers | decoding), NO_SENSE runs from measure.py unread (mk_validation.py)',
       '# note: letter cipher of the Vienna-Schenck letters only; 3-digit codes and the Sieniawski letters (other keys) left out']
for l in (H / 'transcr' / 'RUNS_FINAL.txt').read_text(encoding='utf-8').splitlines():
    if not l.startswith('R74'): continue
    f = [x.strip() for x in l.split('|')]
    if len(f) < 5 or 'not a run' in f[4]: continue
    nums = re.findall(r'\d+', f[1])
    if f[2] in NO_SENSE:
        out += [f'{n}\t?' for n in nums]; continue
    dec = f[2]
    vals = list(dec) if len(dec) == len(nums) else [T.get(n) or letter(n) or '?' for n in nums]
    out += [f'{n}\t{v}' for n, v in zip(nums, vals)]
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
