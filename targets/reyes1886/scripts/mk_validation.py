"""Write validation.tsv for docs/_validate.py.   python scripts/mk_validation.py

Pairs, in text order: (1) the usable rows of transcription_524.txt (rows tagged '!' and '??'/'8?' groups left out),
each group with the letter of the contemporary translation; (2) the 68 groups of transcription_634.txt with our
reading (key_frozen.tsv plus the seven context values of reading_634.md: 53 v, 82 ch, 40 j, 20 p, 12 ch, 23 n, 65 n~).
The writer's dropped a of "ranchero" has no group and is not in the pairs. A '|' token read '?' (unread) is put
between runs, so that no n-gram spans the clear words that separate them.
"""
import sys
from keylib import ROOT, pairs_524, load_key

sys.stdout.reconfigure(encoding='utf-8')
FILL = {'53': 'v', '82': 'ch', '40': 'j', '20': 'p', '12': 'ch', '23': 'n', '65': 'ñ'}
key = load_key(ROOT / 'key_frozen.tsv')
out = ['# model: es-modern',
       '# source: transcription_524.txt (usable rows, letters of the contemporary translation) + transcription_634.txt '
       'read with key_frozen.tsv and the seven context values of reading_634.md; scripts/mk_validation.py',
       '# note: the 524.1 pairs test the key against the contemporary translation; the 634.1 pairs are our reading '
       '(68 groups, 71 letters, too short alone). "|" marks a run boundary (clear words between runs), unread.']
last = None
for seg, g, p in pairs_524():
    if last is not None and seg != last:
        out.append('|\t?')
    out.append(f'{g}\t{p}')
    last = seg
for line in (ROOT / 'transcription_634.txt').read_text(encoding='utf-8').splitlines():
    if not line.startswith('R'):
        continue
    out.append('|\t?')
    for g in line.split()[1:]:
        out.append(f'{g}\t{key.get(g) or FILL[g]}')
(ROOT / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8', newline='\n')
print('validation.tsv:', sum(1 for l in out if not l.startswith(('#', '|'))), 'pairs')
