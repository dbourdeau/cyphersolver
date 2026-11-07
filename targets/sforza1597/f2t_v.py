import pickle, numpy as np, sys, random
from sklearn.cluster import AgglomerativeClustering
pages = sys.argv[2].split(',')
n = int(sys.argv[1]); outp = sys.argv[3]
recs = []
for t in pages:
    r = pickle.load(open(f'sr_p70_0.55_{t}/glyphs2.pkl', 'rb')); recs += r
F = np.array([g['feat'] for g in recs])
lab = AgglomerativeClustering(n_clusters=n, linkage='ward').fit(F).labels_
cnt = {}
for l in lab: cnt[l] = cnt.get(l, 0) + 1
rank = {c: i for i, c in enumerate(sorted(cnt, key=lambda c: -cnt[c]))}
lines = {}
for g, l in zip(recs, lab): lines.setdefault((g['page'], g['line']), []).append(f's{rank[l]:02d}')
txt = '\n'.join(' '.join(v) for k, v in sorted(lines.items()))
open(outp, 'w').write(txt + '\n')
print(len(recs), n, 'lines', len(lines))
pickle.dump((recs, lab), open(outp + '.pkl', 'wb'))
# shuffled control (token order shuffled)
flat = [t for v in lines.values() for t in v]
random.seed(5); random.shuffle(flat)
i = 0; out = []
for v in lines.values():
    out.append(' '.join(flat[i:i + len(v)])); i += len(v)
open(outp.replace('.txt', '_shuf.txt'), 'w').write('\n'.join(out) + '\n')
