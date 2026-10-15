"""Build validation.tsv for swieten1759: the 1759 key (key.json) applied to runs.txt (R957, R956), group by group,
as dec.py does. Groups not in the key and the open name code 232 ('G?') are unread; '300' keeps its value without
the '?'. R955 (the 1757 table, a different key, read from its own decipherment) is left out."""
import json, pathlib
H = pathlib.Path(__file__).resolve().parent
K = json.load(open(H / 'key.json', encoding='utf-8'))
out = ['# model: fr-1750-nospace', '# source: runs.txt with key.json (as dec.py), mk_validation.py',
       '# note: R956+R957 only (1759 table); R955 uses a different 1757 table read from its own decipherment and is left out']
for line in open(H / 'runs.txt'):
    line = line.split('#')[0].strip()
    if not line: continue
    tag, g = line.split(':', 1)
    for x in g.split():
        v = K.get(x)
        if v is None or v == 'G?': v = '?'
        out.append(f'{x}\t{v.rstrip("?") or "?"}')
(H / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(out) - 3)
