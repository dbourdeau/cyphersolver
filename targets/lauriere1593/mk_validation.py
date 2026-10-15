"""Build validation.tsv for fr. 3985 f. 58 (the largest text in key no. 57): fr3985_f58/ct.txt decoded token by token
with decode58.dec (key no. 57 + words57.tsv); the tokens decode58.OPEN lists as not read are '?'."""
import re, sys, pathlib
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE / 'fr3985_f58'))
import decode58 as d
out = ['# model: fr-1600-letters',
       '# source: fr3985_f58/ct.txt decoded with fr3985_f58/decode58.py (key no. 57), OPEN tokens unread; mk_validation.py',
       '# note: f. 58 only (248 tokens); no. 55 (same key, other notation) and the two-digit alphabet of nos. 24/25/60 (another key) not included']
for tag, toks in d.runs():
    ct = [t for t in toks if not t.startswith('{')]
    for i, t in enumerate(ct):
        v = d.dec(t)
        if i in d.OPEN.get(tag, []) or t == '?' or v == '?':
            v = '?'
        else:
            v = re.sub(r'[\[\]<>]', '', v)
        out.append(f'{t}\t{v}')
(HERE / 'validation.tsv').write_text('\n'.join(out) + '\n', encoding='utf-8')
