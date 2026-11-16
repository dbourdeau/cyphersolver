#!/usr/bin/env python3
"""After the held-out measurement: align each transcribed sign of doc. 114 with the reference letters and
tabulate, per label, which reference letter(s) it lines up with. usage: confusion.py transcription.tsv reference.tsv"""
import csv, json, sys, collections, re
import score as S
key = json.load(open('key-46dec7b.json'))['signs']; vs = S.valsets(key)
def rows(path):
    out = collections.defaultdict(list)
    for r in csv.DictReader((l for l in open(path) if not l.startswith('#')), delimiter='\t'):
        if r['kind'] == 'clear': continue
        for t in r['tokens'].split():
            out[r['block']].append((S.label(t), t, r['leaf'], r['line']))
    return out
def align(seq, ref):
    n, m = len(seq), len(ref)
    D = [[None]*(m+1) for _ in range(n+1)]
    D[0][0] = (0, 0, None)
    for j in range(1, m+1): D[0][j] = (j, 0, 'I')
    for i in range(1, n+1):
        D[i][0] = (i, 0, 'D')
        for j in range(1, m+1):
            hit = ref[j-1] in seq[i-1][0]
            D[i][j] = min((D[i-1][j-1][0]+(0 if hit else 1), D[i-1][j-1][1]-(1 if hit else 0), 'M'),
                          (D[i-1][j][0]+1, D[i-1][j][1], 'D'), (D[i][j-1][0]+1, D[i][j-1][1], 'I'))
    i, j, pairs = n, m, []
    while i or j:
        op = D[i][j][2]
        if op == 'M': pairs.append((seq[i-1], ref[j-1])); i -= 1; j -= 1
        elif op == 'D': pairs.append((seq[i-1], '-')); i -= 1
        else: j -= 1
    return pairs[::-1]
tr = rows(sys.argv[1]); refs = {r['block']: S.norm(r['text']) for r in csv.DictReader(open(sys.argv[2]), delimiter='\t')}
tab = collections.defaultdict(collections.Counter); detail = []
for b, toks in tr.items():
    seq = []   # one entry per output char: (valueset, sign index, char index within sign)
    for k, (lab, raw, leaf, line) in enumerate(toks):
        v = vs.get(lab, 'WILD')
        if v is None: continue
        if v == 'WILD': seq.append((frozenset(), k, 0)); continue
        n = max(len(x) for x in v)
        for i in range(n): seq.append((frozenset(x[i] for x in v if len(x) > i), k, i))
    cur = collections.defaultdict(str)
    for (s, k, i), ch in align(seq, refs[b]): cur[k] += ch
    for k, (lab, raw, leaf, line) in enumerate(toks):
        if k in cur:
            tab[lab][cur[k]] += 1; detail.append((b, leaf, line, k, lab, raw, cur[k]))
for lab in sorted(tab, key=lambda l: -sum(tab[l].values())):
    print(f"{lab:5s} {sum(tab[lab].values()):4d}  " + ' '.join(f"{c}:{n}" for c, n in tab[lab].most_common()))
with open('aligned-signs.tsv', 'w') as f:
    f.write('block\tleaf\tline\tsign_index\tlabel\traw\tref\n')
    for d in detail: f.write('\t'.join(map(str, d)) + '\n')
