# decompte.py — décompte façon Daniel sur LECTURE-p1-4.txt (Fable) + LECTURE-p5.txt (Opus). Post hoc, hors mesure.
import sys, os, re, collections
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = collections.Counter(); per = collections.defaultdict(collections.Counter)
for f in ('LECTURE-p1-4.txt', 'LECTURE-p5.txt'):
    for l in open(os.path.join(R, f)):
        if l.startswith('#') or not l.strip(): continue
        ref, txt = l.split(None, 1)
        txt = re.sub(r'\(suite.*', '', txt).replace('…', '')
        for w in txt.split():
            if w == '/': continue
            if re.fullmatch(r'\[\d+\]', w): k = 'irresolu'
            elif w.startswith('['): k = 'probable'
            elif w.startswith('<'): k = 'restitue'
            elif w.endswith('?'): k = 'probable'
            else: k = 'sur'
            C[k] += 1; per[ref[0]][k] += 1
tot = sum(C.values())
for p in sorted(per): print('p%s' % p, dict(per[p]), sum(per[p].values()))
print('TOTAL', dict(C), tot)
print('lu par le sens (surs+probables+restitues) = %.1f %% ; surs seuls = %.1f %% ; surs+probables = %.1f %%' % (
    100 * (tot - C['irresolu']) / tot, 100 * C['sur'] / tot, 100 * (C['sur'] + C['probable']) / tot))
