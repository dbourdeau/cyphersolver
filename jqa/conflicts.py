"""List code numbers whose values disagree across pairs_jqa.txt, clerk_*.tsv and ford_pairs.tsv.
python conflicts.py [numbers...]"""
import sys, glob, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
files = ['pairs_jqa.txt'] + sorted(glob.glob('clerk_*.tsv')) + sorted(glob.glob('ford_pairs*.tsv'))
d = {}
for f in files:
    for l in open(f, encoding='utf8'):
        p = l.rstrip('\n').split('\t')
        if l.startswith('#') or len(p) < 4 or not p[0].strip().isdigit(): continue
        d.setdefault(int(p[0]), []).append((p[1].strip(), p[3].strip()[:1], p[2].strip()))
want = set(map(int, sys.argv[1:]))
key = lambda s: re.sub(r'[^a-z]', '', re.sub(r'\(.*?\)', '', s.lower()))
for n in sorted(d):
    if want and n not in want: continue
    vals = {key(v) for v, g, s in d[n]}
    if want or len(vals) > 1:
        print(n, ' | '.join(f'{v} [{g} {s}]' for v, g, s in d[n]))
