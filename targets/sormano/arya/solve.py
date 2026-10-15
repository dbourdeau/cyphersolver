"""Derive the key from the f.124r crib: segment, clean, cluster by shape, map 1:1 to the known plaintext."""
import sys, collections, statistics, json
sys.path.insert(0,'.')
from clean import pipeline
from glyphs6 import prep, dist, agglom

PLAIN = sys.argv[sys.argv.index('--plain')+1] if '--plain' in sys.argv else ''
K = int(sys.argv[sys.argv.index('--k')+1]) if '--k' in sys.argv else 34

bs, seq = pipeline('/tmp/crib.bmp', 2115, 3270, maxw=64)
flat = [c for s in seq for c in s]
print(f'per line {[len(s) for s in seq]} total {len(flat)} plaintext {len(PLAIN)}')
base, shft = prep(flat)
n = len(flat)
D = [[0.0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        d = min(dist(i,j,base,shft), dist(j,i,base,shft))
        D[i][j] = D[j][i] = d
off = [D[i][j] for i in range(n) for j in range(i+1,n)]
print(f'pair distance min={min(off):.3f} median={statistics.median(off):.3f}')
json.dump(D, open('/tmp/D161.json','w'))
for k in (int(x) for x in (sys.argv[sys.argv.index('--ks')+1].split(',') if '--ks' in sys.argv else [str(K)])):
    lab = agglom(n, D, k)
    cnt = collections.defaultdict(collections.Counter)
    for i, ch in enumerate(PLAIN[:n]):
        cnt[lab[i]][ch] += 1
    pure = sum(c.most_common(1)[0][1] for c in cnt.values())
    print(f'k={k}: clusters={len(cnt)} consistent={pure}/{n} ({100*pure/n:.1f}%)')
    if '--detail' in sys.argv:
        for g in sorted(cnt, key=lambda g:-sum(cnt[g].values())):
            c = cnt[g]; tot = sum(c.values()); best, bn = c.most_common(1)[0]
            flag = '' if bn == tot else '   <-- ' + str(dict(c))
            print(f'   cluster {g:3d} -> {best}  n={tot} pure={bn}/{tot}{flag}')
