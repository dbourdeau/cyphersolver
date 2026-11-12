"""Write validation.tsv for Dan's docs/_validate.py. Standard library only.

    python scripts/validation_pairs.py > validation.tsv

The cipher uses two alphabets that alternate within each run (odd and even places; the count restarts at each
run), so the token type for the test is the sign together with its place parity: 'x1' = sign x at an odd place,
'x2' = at an even place. Each token is paired with the letter the reading gives (marks resolved: quo{b/d} -> d,
wor{t?} -> t). The '?' of an uncertain sign is not a token.
"""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from decrypt import runs
md = (ROOT / 'reading_fuerstenberg1659.md').read_text(encoding='utf-8')
block = md.split('```marked')[1].split('```')[0]
read = {}
for line in block.strip().splitlines():
    run, txt = line.split(':', 1)
    t = re.sub(r'\{([a-z])\?\}', r'\1', txt)
    t = re.sub(r'\{([a-z]*)/([a-z]*)\}', r'\2', t)
    read[run.strip()] = re.sub(r'[^a-z]', '', t.lower().replace('j', 'i').replace('v', 'u'))
ct = {}
for lab, run, signs in runs(ROOT / 'transcription_fuerstenberg1659.txt'):
    ct[run] = ct.get(run, '') + signs.replace('?', '')
print('# model: de-1640s')
print('# source: transcription_fuerstenberg1659.txt and reading_fuerstenberg1659.md (scripts/validation_pairs.py)')
print('# note: token = sign + place parity in its run (1 odd, 2 even); the two alphabets alternate. German with Latin phrases.')
for run in sorted(ct):
    assert len(ct[run]) == len(read[run]), run
    for i, (c, p) in enumerate(zip(ct[run], read[run])):
        print(f'{c}{1 + i % 2}\t{p}')
