"""Held-out test: python scripts/heldout.py
The key was frozen from run R12 (the English sentence) alone. The other 16 runs are held out. Each held-out
run is decrypted with key_frozen.tsv and compared, letter by letter, with the name or phrase the clear text and the
history of the felicista exile point to (expected.tsv). The expected forms are standard spellings, unaccented, set
down from the decryption plus context; a run counts as exact when the mechanical decryption equals the expected
form (spaces ignored). Letter score: aligned matches (difflib) over expected letters."""
import difflib, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decrypt import load_key, dec
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
key = load_key(os.path.join(ROOT, 'key_frozen.tsv'))
runs = {}
for line in open(os.path.join(ROOT, 'transcription_DCXXI.3.231.1.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    rid, page, signs = line.rstrip('\n').split('\t'); runs[rid] = signs
exp = {}
for line in open(os.path.join(ROOT, 'expected.tsv'), encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    rid, e = line.rstrip('\n').split('\t'); exp[rid] = e
n = exact = lm = lt = 0
for rid, signs in runs.items():
    if rid == 'R12': continue
    d = dec(signs, key).replace(' ', ''); e = exp[rid].replace(' ', '')
    m = sum(b.size for b in difflib.SequenceMatcher(None, d, e, autojunk=False).get_matching_blocks())
    n += 1; exact += d == e; lm += m; lt += len(e)
    print(f'{rid}\t{"exact" if d == e else "slip "}\t{d}\t{e}\t{m}/{len(e)}')
print(f'held-out runs exact: {exact}/{n}; letters matched: {lm}/{lt} ({100*lm/lt:.1f}%)')
