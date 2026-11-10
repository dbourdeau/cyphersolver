"""Compare the blind digit-only transcription of the bare second copy (bare_*.txt, images 332-342) with the groups of
the glossed copy (wordpairs_*.tsv, images 321-331), and take the bare copy's digit at every one-for-one difference where
the bare group is not doubtful. Each change is recorded in the note column. Lines that then agree with confirmed key
values throughout go from X to K. usage: python scripts/apply_bare.py [--write]"""
import re, sys, glob, difflib, unicodedata
def fold(s):
    s = unicodedata.normalize("NFD", s.lower()); return "".join(c for c in s if c.isalpha() or c.isdigit())
key = {l.split('\t')[0]: l.rstrip('\n').split('\t') for l in open('key.tsv', encoding='utf-8') if l[0] != '#'}
bare = []
for fn in ('bare_332_336.txt', 'bare_337_339.txt', 'bare_340_342.txt'):
    for l in open(fn, encoding='utf-8'):
        if '\t' in l: bare += [t for t in re.findall(r'\{[^}]*\}|\d[\d?]{3}\??', l.split('\t', 1)[1]) if t[0] != '{']
files = sorted(glob.glob('wordpairs_*.tsv'))
rows = {fn: [l.rstrip('\n').split('\t') for l in open(fn, encoding='utf-8') if l.strip()] for fn in files}
idx = [(fn, i, j) for fn in files for i, f in enumerate(rows[fn]) if f[0][0] != '#' and f[2] != 'C' for j, _ in enumerate(f[3].split())]
idx.sort(key=lambda t: rows[t[0]][t[1]][0])
gl = [rows[fn][i][3].split()[j].rstrip('?') for fn, i, j in idx]
a = [b.rstrip('?') for b in bare]
ops = difflib.SequenceMatcher(None, a, gl, autojunk=False).get_opcodes()
same = sum(i2 - i1 for op, i1, i2, j1, j2 in ops if op == 'equal')
print(f'bare groups {len(a)}; glossed groups {len(gl)}; identical in sequence {same}')
n = up = other = 0
for op, i1, i2, j1, j2 in ops:
    if op == 'equal': continue
    if op != 'replace' or i2 - i1 != j2 - j1:
        other += 1; print(op, bare[i1:i2], gl[j1:j2], rows[idx[min(j1, len(idx)-1)][0]][idx[min(j1, len(idx)-1)][1]][:2]); continue
    for t in range(i2 - i1):
        bg = bare[i1 + t]
        if '?' in bg: continue
        fn, i, j = idx[j1 + t]; f = rows[fn][i]
        while len(f) < 7: f.append('')
        gs = f[3].split(); old = gs[j]; gs[j] = bg; f[3] = ' '.join(gs)
        f[6] = (f[6] + ' ' if f[6] else '') + f'[{old} corrected to {bg} from the bare second copy]'; n += 1
for fn in files:
    for f in rows[fn]:
        if f[0][0] == '#' or f[2] != 'X': continue
        gs = f[3].split(); ps = f[5].split('|') if len(f) > 5 else []
        if len(ps) == len(gs) and all('?' not in g and g in key and key[g][4] == 'confirmed' and key[g][1] == fold(p) for g, p in zip(gs, ps)):
            f[2] = 'K'; up += 1
print(f'digits taken from the bare copy {n}; X lines now agreeing with confirmed values {up}; other differences {other}')
if '--write' in sys.argv:
    for fn in files: open(fn, 'w', encoding='utf-8').write('\n'.join('\t'.join(f) for f in rows[fn]) + '\n')
