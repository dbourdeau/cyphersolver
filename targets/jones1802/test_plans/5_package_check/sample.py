import random, sys, os
T = sys.argv[1]  # targets/jones1802 folder
OUT = sys.argv[2]

def rows(fn):
    L = [l.rstrip('\n').split('\t') for l in open(os.path.join(T, fn), encoding='utf-8') if not l.startswith('#') and l.strip()]
    return L[0], L[1:]

h, R = rows('entick_lines.tsv')
rng = random.Random(20261115)
rand = rng.sample(range(len(R)), 12)
targets = ['Superintendent', 'Silver', 'Mine', 'Bishop', 'Body', 'Gain', 'Fortify', 'Frontier', 'Winter']
fixed = {'Daniel': (442, 55), 'David': (442, 56), 'Joseph': (443, 48)}
pl = {}
for w in targets:
    for fn in ('entick_212.tsv', 'entick_49.tsv'):
        hh, rr = rows(fn)
        i = hh.index('dictionary_line_n'); g = hh.index('group')
        hit = [r for r in rr if len(r) > i and r[i].replace("'",'').lower() == w.lower()]
        if hit:
            p, l = hit[0][g].split(',')[:2]
            pl[w] = (int(p), int(l)); break
pl.update(fixed)
idx = {(int(r[0]), int(r[1])): k for k, r in enumerate(R)}
tg = []
for w in targets + list(fixed):
    tg.append((w, pl.get(w), idx.get(pl.get(w))))
with open(os.path.join(OUT, 'A_sample_full.tsv'), 'w') as f:  # holds the answers: not given to readers
    f.write('kind\tidx\tpage\tline\t' + '\t'.join(h) + '\n')
    for k in rand:
        f.write('random\t%d\t%s\t%s\t%s\n' % (k, R[k][0], R[k][1], '\t'.join(R[k])))
    for w, p, k in tg:
        f.write('target:%s\t%s\t%s\t%s\t%s\n' % (w, k, p[0] if p else '', p[1] if p else '', '\t'.join(R[k]) if k is not None else 'NOT FOUND'))
with open(os.path.join(OUT, 'A_tasks.tsv'), 'w') as f:
    f.write('task\tpage\tline\n')
    n = 0
    for k in rand:
        n += 1; f.write('A%02d\t%s\t%s\n' % (n, R[k][0], R[k][1]))
    for w, p, k in tg:
        n += 1; f.write('A%02d\t%s\t%s\n' % (n, p[0] if p else '', p[1] if p else ''))

h, R = rows('reread_49.tsv')
ic, ir, idb = h.index('group_ct'), h.index('group_reread'), h.index('doubtful')
ch = [r for r in R if r[ic] != r[ir] and r[idb].strip().lower() != 'yes']
rng = random.Random(20261115)
s = rng.sample(range(len(ch)), 20)
with open(os.path.join(OUT, 'B_sample.tsv'), 'w') as f:
    f.write('k\t' + '\t'.join(h) + '\n')
    for k in s:
        f.write('%d\t%s\n' % (k, '\t'.join(ch[k])))
print(len(ch), 'changed groups in frame;', len(R), 'rows')
