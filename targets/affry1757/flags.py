# flags.py R#### : decode with sense flags (lowercase=passes the window test, UPPER/[n]=fails)
import sys, glob, os
import measure_sense as m
from view import load
U = load('U')
for f in glob.glob('transcr/R*.txt'):
    U[os.path.basename(f)[:-4]] = [int(t.split('|')[0]) for l in open(f, encoding='utf8') if not l.startswith('#') for t in l.split()]
g = U[sys.argv[1]]; ok = m.sense_r(sys.argv[1], g, -3.0)
out = []
for i, (x, o) in enumerate(zip(g, ok)):
    v = m.val(x)
    out.append((v if o else ('[%d]' % x if v is None else v.upper() + '{%d}' % x)) if v != '' else '.')
for i in range(0, len(out), 14): print('%4d ' % i + ' '.join(out[i:i+14]))
