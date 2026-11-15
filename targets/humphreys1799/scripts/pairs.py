"""Collect group=value pairs from the crib transcription files (../transcriptions/M*.txt, lines 'Lnn: tok tok ...').
Token forms: GROUP=VALUE with optional marks on VALUE: ! clerk's gloss on film, ~ aligned from print, ? uncertain.
Writes ../pairs.tsv (one row per occurrence: frame, line, pos, group, value, source_mark, uncertain) and prints
a per-group summary with conflicts. Files named in EXCLUDE (comma list in env HOLDOUT) are skipped, so a held-out
despatch can be kept out of the build. Usage: python3 -I pairs.py [--summary]"""
import os, re, sys, glob, collections
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HOLD = set(x for x in os.environ.get('HOLDOUT', '').split(',') if x)
rows = []
for f in sorted(glob.glob(BASE + '/transcriptions/M*.txt')):
    fr = os.path.basename(f)[:-4]
    if any(fr.startswith(h) for h in HOLD): continue
    for line in open(f):
        m = re.match(r'([LR]\d+\w*):\s*(.*)', line.strip())
        if not m: continue
        ln, body = m.groups()
        body = re.sub(r'\[(?:cut|struck|1791|Struck)[^\]]*\]', '', body)   # drop bracketed notes ([cut: ...], [struck ...]); keep [1/4] part markers
        for k, tok in enumerate(body.split()):
            if '=' not in tok: continue
            g, v = tok.split('=', 1)
            gunc = '?' in g
            unc = gunc or v.endswith('?')
            mark = '!' if '!' in v else ('~' if '~' in v else '')
            v = v.replace('!', '').replace('~', '').rstrip('?')
            g = g.replace('?', '')
            rows.append((fr, ln, k, g, v, mark, 'g' if gunc else ('u' if unc else '')))
with open(BASE + '/pairs.tsv', 'w') as o:
    o.write('frame\tline\tpos\tgroup\tvalue\tsource\tuncertain\n')
    for r in rows: o.write('\t'.join(map(str, r)) + '\n')
if '--summary' in sys.argv:
    d = collections.defaultdict(collections.Counter)
    for r in rows: d[r[3]][r[4]] += 1
    for g in sorted(d, key=lambda x: int(re.sub(r'\D', '', x) or 0)):
        vals = d[g]
        flag = 'CONFLICT' if len(vals) > 1 else ''
        print(g, dict(vals), flag)
print(len(rows), 'pairs;', len(set(r[3] for r in rows)), 'groups', file=sys.stderr)
