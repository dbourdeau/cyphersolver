"""Description after the second test (not part of the test, changes no score): the best tiling of each held-out
run with the place of every hit and miss, written to test2/heldout_reading.tsv."""
import sys, json
sys.path.insert(0, 'scripts')
from wlib import MAXSEG, norm
T = 'transcriptions/'
keep = {}
for l in open('test2/table2_frozen.tsv').read().splitlines()[1:]:
    n, v, t = l.split('\t'); keep[n] = (v, t)
d = json.load(open(T + 'runs_f049.json'))
rows = []
for r in d['runs']:
    g = r['groups']; text = norm(''.join(r['print_words'])); k, n = len(g), len(text)
    best = [[-1] * (n + 1) for _ in range(k + 1)]; back = [[None] * (n + 1) for _ in range(k + 1)]
    best[0][0] = 0
    for i in range(k):
        v = keep.get(g[i], (None,))[0]
        for j in range(n + 1):
            a = best[i][j]
            if a < 0: continue
            if v and text.startswith(v, j):
                s = a + 1000 + len(v)
                if s > best[i + 1][j + len(v)]: best[i + 1][j + len(v)] = s; back[i + 1][j + len(v)] = (j, True)
            for L in range(1, MAXSEG + 1):
                if j + L > n: break
                if a > best[i + 1][j + L]: best[i + 1][j + L] = a; back[i + 1][j + L] = (j, False)
    j = n; out = []
    for i in range(k, 0, -1):
        j0, hit = back[i][j]; out.append((g[i - 1], text[j0:j], hit)); j = j0
    for num, piece, hit in reversed(out):
        v, t = keep.get(num, ('', ''))
        rows.append((r['run'], r['place'], num, v, t, 'hit' if hit else ('MISS' if v else 'not in table'), piece if hit else f'({piece})'))
with open('test2/heldout_reading.tsv', 'w') as f:
    f.write('run\tplace\tnumber\ttable_value\ttier\tresult\tprint_letters_in_best_tiling\n')
    for x in rows: f.write('\t'.join(map(str, x)) + '\n')
from collections import Counter
print(Counter((x[4] or '-', x[5]) for x in rows))
for x in rows:
    if x[5] == 'MISS': print(x)
