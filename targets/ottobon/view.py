"""Readable view of dec_out/<page>.txt: plaintext per line with low-margin units in [brackets] (margin < T)."""
import sys
pg = sys.argv[1]; T = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
tag = sys.argv[3] if len(sys.argv) > 3 else ''
L = open('dec_out/%s%s.txt' % (pg, tag), encoding='utf8').read().splitlines()
i = 1
while i < len(L):
    hdr = L[i]; rdct = L[i + 1].split()[1:]; de = L[i + 2].split()[1:]; va = L[i + 3].split()[1:]
    mg = [float(x) for x in L[i + 5].split()[1:]]; alt = L[i + 6].split()[1:]
    s = ''
    for v, m, a in zip(va, mg, alt):
        sp = v.startswith('_'); v = v.lstrip('_').replace('~', ' ')
        if v == '-': v = '·'
        s += (' ' if sp else '') + (v if m >= T else '[' + v + ']')
    print(hdr.replace('# ', '') + ':' + s)
    i += 7
