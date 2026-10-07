"""Letter-level agreement between two sign-by-sign readings of f.276 (agent output format: 'L05: d e l e ...').
Word signs (=de) count as one token; x/y alternatives agree if they share a value; ? never agrees."""
import re, sys, difflib
def load(p):
    d = {}
    for l in open(p):
        m = re.match(r'^\s*(L\d\d):\s*(.+)$', l)
        if m and m.group(1) not in d and not m.group(2).startswith('['):
            d[m.group(1)] = [t for t in m.group(2).split() if t not in ('|',)]
    return d
def eq(a, b):
    if '?' in (a, b): return False
    sa = set(a.replace('?', '').split('/')); sb = set(b.replace('?', '').split('/'))
    return bool(sa & sb)
A, B = load(sys.argv[1]), load(sys.argv[2])
tot = agree = 0
for k in sorted(set(A) & set(B)):
    a, b = A[k], B[k]
    sm = difflib.SequenceMatcher(a=[x.split('/')[0] for x in a], b=[x.split('/')[0] for x in b], autojunk=False)
    m = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': m += i2 - i1
        elif op == 'replace':
            m += sum(eq(x, y) for x, y in zip(a[i1:i2], b[j1:j2]))
    n = max(len(a), len(b)); tot += n; agree += m
    print(f'{k}: {m}/{n} = {m/n:.0%}')
print(f'TOTAL {agree}/{tot} = {agree/tot:.1%}')
