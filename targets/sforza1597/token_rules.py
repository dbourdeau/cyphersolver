import sys, collections
rules = {('s15', 's15'): 's04', ('s07', 's15'): 's00', ('s37', 's46'): 's46', ('s57', 's15'): 's00'}
src, dst = sys.argv[1], sys.argv[2]
out = []; n = collections.Counter()
for line in open(src).read().strip().split('\n'):
    t = line.split(); r = []; i = 0
    while i < len(t):
        if i + 1 < len(t) and (t[i], t[i + 1]) in rules:
            n[(t[i], t[i + 1])] += 1; r.append(rules[(t[i], t[i + 1])]); i += 2
        else: r.append(t[i]); i += 1
    out.append(' '.join(r))
open(dst, 'w', newline=chr(10)).write(chr(10).join(out) + chr(10))
print('rule applications', dict(n), '| tokens', sum(len(l.split()) for l in open(src)), '->', sum(len(l.split()) for l in out))
