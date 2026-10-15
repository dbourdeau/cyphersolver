"""No. 43 (14 Oct 2026, one-key split): count the code groups and write validation.tsv for docs/_validate.py.

Sources, in text order: the unglossed opening (n43/opening_c245.txt, values as n43/decode_opening.py assigns them:
gloss majority, code structure, context) and the glossed body (n43/pairs_c245.txt ... pairs_c251.txt, each group with
the contemporary interlinear gloss). Clear words (#word) are skipped. A group with an empty gloss in the null range
99-250 is a null ('-'); any other empty or '?' gloss, or a number not read in the transcription, is unread ('?').
An underlined number (347_) is its own token type: it carries the reversed syllable."""
import re, sys
sys.path.insert(0, 'n43')
HERE = 'n43/'
G = {}
for l in open(HERE + 'key43.txt', encoding='utf-8'):
    n, rest = l.rstrip('\n').split('\t'); G[int(n)] = rest.split()[0].rsplit(':', 1)[0]
S = {37: 'o', 38: 'n', 46: 'e', 59: 'i', 80: 't', 81: 's', 86: 'n'}
NULL = {99, 119, 129, 150, 206, 207, 222, 229, 230, 237, 240}
C = {279: 'de', 277: 'do', 354: 'ne', 358: 'me', 364: 'la', 314: 'je', 321: 'gu', 390: 'ru', 398: 'que', 400: 'pu',
     407: 'e', 439: 'se', 442: 'ti', 443: 'te', 445: 'su'}
rows = []
for line in open(HERE + 'opening_c245.txt', encoding='utf-8'):
    if line.startswith('#'): continue
    body = re.sub(r'\^\[([^\]]*)\]', r'\1', line.split(':', 1)[1])
    for tok in body.split():
        if tok.startswith('#'): continue
        n = int(re.sub(r'\D', '', tok)); t = tok.rstrip('?')
        if n in NULL: rows.append((t, '-')); continue
        v = S.get(n) or C.get(n) or G.get(n)
        if not v: rows.append((t, '?')); continue
        if t.endswith('_') and len(v) == 2: v = v[::-1]
        rows.append((t, v))
nopen = len(rows)
for f in ['pairs_c245.txt', 'pairs_c246.txt', 'pairs_c247.txt', 'pairs_c248.txt', 'pairs_c249.txt',
          'pairs_c250.txt', 'pairs_c251.txt']:
    for line in open(HERE + f, encoding='utf-8'):
        m = re.match(r'L\d+:\s*(.*)', line.strip())
        if not m: continue
        for tok in m.group(1).split():
            if tok.startswith('#') or '=' not in tok: continue
            num, g = tok.split('=', 1)
            if num.startswith('?') or not re.sub(r'\D', '', num):
                rows.append((num.lstrip('?') or '?', '?')); continue
            n = int(re.sub(r'\D', '', num))
            if g in ('', '+'):
                rows.append((num, '-' if 99 <= n <= 250 else '?'))
            elif g == '?' or '?' in g:
                rows.append((num, '?'))
            else:
                rows.append((num, g.lower()))
total = len(rows); unread = sum(1 for _, v in rows if v == '?'); nulls = sum(1 for _, v in rows if v == '-')
print(f'opening {nopen} groups; whole mémoire {total} groups, {nulls} nulls, {unread} unread; '
      f'{total - unread} of {total} have a value or are nulls ({(total - unread) / total:.1%})')
op_unread = sum(1 for _, v in rows[:nopen] if v == '?')
print(f'opening: {nopen - op_unread} of {nopen} have a value or are nulls')
if '--write' in sys.argv:
    with open('validation.tsv', 'w', encoding='utf-8') as o:
        o.write('# model: fr-1600-letters\n# source: n43/opening_c245.txt (decode_opening.py values) + n43/pairs_c245-251.txt (interlinear glosses)\n')
        o.write('# note: underlined numbers are separate types; nulls 99-250 as -\n')
        for t, v in rows:
            o.write(f'{t}\t{v}\n')
