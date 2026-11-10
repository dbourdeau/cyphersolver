"""Compare the blind digit-only transcription of the bare second copy (bare_332_336.txt) with the groups of the
glossed copy (wordpairs_*.tsv). Prints the agreement and each place where the two differ, with the glossed word."""
import re, difflib, glob
bare = []
for l in open('bare_332_336.txt', encoding='utf-8'):
    if '\t' not in l: continue
    bare += [t for t in re.findall(r'\{[^}]*\}|\d[\d?]{3}\??', l.split('\t', 1)[1]) if t[0] != '{']
gl = []
for fn in ('wordpairs_322_323.tsv', 'wordpairs_324_325.tsv', 'wordpairs_326_327.tsv'):
    for l in open(fn, encoding='utf-8'):
        f = l.rstrip('\n').split('\t')
        if l[0] == '#' or f[2] == 'C': continue
        gl += [(g, f[0], f[1], f[2], f[4]) for g in f[3].split()]
a = [b.rstrip('?') for b in bare]; b = [g[0].rstrip('?') for g in gl]
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
ops = sm.get_opcodes(); first = next(o for o in ops if o[0] == 'equal' and o[2] - o[1] > 5); last = [o for o in ops if o[0] == 'equal' and o[2] - o[1] > 5][-1]
span = last[4] - first[3]
print(f'bare groups {len(a)}; overlap with the glossed copy: its groups {first[3]}..{last[4]} ({span}); identical in sequence {sum(o[2]-o[1] for o in ops if o[0]=="equal")}')
for op, i1, i2, j1, j2 in ops:
    if op == 'equal' or j1 < first[3] or j2 > last[4]: continue
    w = gl[j1] if j1 < len(gl) else gl[-1]
    print(op, 'bare', bare[i1:i2], 'glossed', [g[0] for g in gl[j1:j2]], w[1], w[2], w[3], w[4])
