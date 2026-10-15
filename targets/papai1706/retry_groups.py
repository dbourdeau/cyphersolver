"""Retry every off-key group in the *_read.txt files: score each key value (and 'null') in its context with the
4-gram model from solve731.py, and report the best when it clearly beats the runner-up."""
import re, glob, math, collections, sys
from pathlib import Path
sys.argv = [sys.argv[0]]
R = Path(__file__).resolve().parent
exec(open(R/'decode.py', encoding='utf-8').read().split('if __name__')[0])
sys.path.insert(0, str(R.parent / 'papai1710'))   # solve731.py moved there on 14 Oct 2026 (split)
import solve731 as S
vals = sorted({v.lower() for v in KEY.values() if len(v) <= 3 and v.isalpha()} | {''})
def sc(t):
    t = S.clean(t); g = [S.LP.get(t[i:i+4], S.floor) for i in range(len(t)-3)]; return 10*sum(g)/max(1, len(g))
rows = []; counts = collections.Counter()
for f in sorted(glob.glob(str(R/'*read.txt'))):
    text = open(f, encoding='utf-8').read()
    flat = re.sub(r'\s*\n\s*', '', '\n'.join(l for l in text.splitlines() if not l.startswith(('#', '='))))
    for m in re.finditer(r'\s?\[([^\]]+)\]\s?', flat):
        g = m.group(1); L = re.sub(r'\[[^\]]*\]|[{} ]', '', flat[max(0, m.start()-12):m.start()])[-8:]
        Rr = re.sub(r'\[[^\]]*\]|[{} ]', '', flat[m.end():m.end()+12])[:8]
        if not re.fullmatch(r'\d+', g) or int(g) > 322:
            counts['clear numeral / garbled (not a cipher group)' if re.fullmatch(r'\d+', g) else 'slip marked ?'] += 1
            if not re.fullmatch(r'\d+', g): rows.append((Path(f).name, g, L, Rr, '?', 0))
            continue
        cand = sorted(((sc(L+v+Rr), v) for v in vals), reverse=True)
        (b, v1), (b2, v2) = cand[0], cand[1]
        rows.append((Path(f).name, g, L, Rr, v1 if v1 else '(null)', round(b-b2, 1)))
        counts['resolved (margin>=3)' if b-b2 >= 3 else 'open (margin<3)'] += 1
for r in rows: print(*r, sep='\t')
print(dict(counts), 'total', sum(counts.values()))
