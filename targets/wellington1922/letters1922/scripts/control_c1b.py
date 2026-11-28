"""C1b (added after C1, decoder check only): this decoder, variant A, against the merged wellington1922 package's
own decryption of its 60 runs (targets/wellington1922/transcription_DCXXI.6.588.1.txt and
decryption_DCXXI.6.588.1.txt). Every run must match letter for letter.
python3 -I scripts/control_c1b.py <wellington1922 folder>"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f313 import decode
from pathlib import Path
d = Path(sys.argv[1])
T = {}
for l in open(d / 'transcription_DCXXI.6.588.1.txt', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    f = l.rstrip('\n').split('\t'); T[f[0]] = f[3]
n = bad = 0
for l in open(d / 'decryption_DCXXI.6.588.1.txt', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    f = l.rstrip('\n').split('\t'); n += 1
    mine = decode(T[f[0]].replace('?', '?'), 'A')
    theirs = f[2].replace('/', '')
    if mine != theirs:
        bad += 1; print('DIFF', f[0], mine, theirs)
print(f'C1b: {n} runs compared, {bad} differ ->', 'PASS' if bad == 0 else 'FAIL')
