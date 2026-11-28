"""Reconcile two blind transcriptions that use different sign names.
usage: reconcile.py H1.txt H2.txt out_prefix
1. Name map H2->H1 from position-wise co-occurrence on lines with equal sign counts (most frequent partner).
2. H2 translated to H1 names; per line, difflib alignment; agreement = matched signs / max(len).
3. Consensus = H1's tokens (first reader), with a flag list of every position H2 does not support.
Writes out_prefix.map.tsv, out_prefix.log, out_prefix.consensus.txt (= H1 text) and out_prefix.flags.tsv."""
import sys, re, difflib, collections
def rd(f):
    d = {}
    for l in open(f, encoding='utf-8'):
        if '\t' in l and not l.startswith('#'):
            a, b = l.rstrip('\n').split('\t', 1); b = re.sub(r'\{[^}]*\}', ' {clear} ', b); d[a.strip()] = [t for t in b.split()]
    return d
h1, h2, out = rd(sys.argv[1]), rd(sys.argv[2]), sys.argv[3]
sig = lambda toks: [t.rstrip('?') for t in toks if not t.startswith('{')]
co = collections.defaultdict(collections.Counter)
for k in h1:
    if k in h2:
        a, b = sig(h1[k]), sig(h2[k])
        if len(a) == len(b):
            for x, y in zip(a, b): co[y][x] += 1
# second pass: use difflib with first map to collect more pairs
mp = {y: c.most_common(1)[0][0] for y, c in co.items()}
for _ in range(2):
    co2 = collections.defaultdict(collections.Counter)
    for k in h1:
        if k not in h2: continue
        a, b = sig(h1[k]), sig(h2[k]); bt = [mp.get(y, '#' + y) for y in b]
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, bt, autojunk=False).get_opcodes():
            if tag in ('equal', 'replace') and i2 - i1 == j2 - j1:
                for x, y in zip(a[i1:i2], b[j1:j2]): co2[y][x] += 1
    mp = {y: c.most_common(1)[0][0] for y, c in co2.items()}; co = co2
log = open(out + '.log', 'w'); fl = open(out + '.flags.tsv', 'w'); tot = agr = 0
with open(out + '.map.tsv', 'w') as f:
    for y in sorted(co): f.write(f"{y}\t{mp[y]}\t{dict(co[y].most_common(4))}\n")
for k in h1:
    a = sig(h1[k]); b = sig(h2.get(k, [])); bt = [mp.get(y, '#' + y) for y in b]
    sm = difflib.SequenceMatcher(None, a, bt, autojunk=False); m = sum(x.size for x in sm.get_matching_blocks())
    tot += max(len(a), len(bt)); agr += m
    log.write(f"{k}\t{m}/{max(len(a), len(bt))}\n")
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != 'equal': fl.write(f"{k}\t{i1}-{i2}\t{tag}\tH1={' '.join(a[i1:i2])}\tH2={' '.join(bt[j1:j2])}\n")
log.write(f"TOTAL\t{agr}/{tot}\t{agr / max(tot, 1):.3f}\n"); log.close()
with open(out + '.consensus.txt', 'w') as f:
    for k in h1: f.write(k + '\t' + ' '.join(h1[k]) + '\n')
print(open(out + '.log').read().splitlines()[-1])
