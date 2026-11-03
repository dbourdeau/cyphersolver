import difflib, sys
def load(p):
    d = {}
    for l in open(p, encoding='utf-8'):
        if l.startswith('M'):
            k, _, v = l.rstrip('\n').partition('\t')
            d[k] = [t for t in v.replace('[questa cosa]', '[questa] [cosa]').split()]
    return d
a, b = load(sys.argv[1]), load(sys.argv[2]); tot = dis = 0
for k in sorted(a):
    x = [t for t in a[k] if not t.startswith('[')]; y = [t for t in b.get(k, []) if not t.startswith('[')]
    sm = difflib.SequenceMatcher(None, x, y, autojunk=False); tot += len(x); out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal':
            dis += max(i2 - i1, j2 - j1); out.append(f"@{i1}:{' '.join(x[i1:i2]) or '-'}|{' '.join(y[j1:j2]) or '-'}")
    print(k, len(x), len(y), '; '.join(out))
print('signs', tot, 'differing', dis)
