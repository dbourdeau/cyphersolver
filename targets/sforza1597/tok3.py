"""tokens from v2 glyphs: Ward init + k-means refinement. usage: tok3.py n pages out [seed]"""
import pickle, numpy as np, sys, collections
from sklearn.cluster import AgglomerativeClustering, KMeans
n = int(sys.argv[1]); pages = sys.argv[2].split(','); outp = sys.argv[3]
recs = []
for t in pages: recs += pickle.load(open(f'sr_{t}/glyphs2.pkl', 'rb'))
F = np.array([r['feat'] for r in recs])
w = AgglomerativeClustering(n_clusters=n, linkage='ward').fit(F).labels_
init = np.array([F[w == c].mean(0) for c in range(n)])
km = KMeans(n_clusters=n, init=init, n_init=1, max_iter=50).fit(F)
lab = km.labels_
print('reassigned by k-means', int((lab != w).sum()), 'of', len(w))
cnt = collections.Counter(lab); rank = {c: i for i, (c, _) in enumerate(cnt.most_common())}
lines = collections.OrderedDict()
for r, l in zip(recs, lab): lines.setdefault((r['page'], r['line']), []).append(f's{rank[l]:02d}')
open(outp, 'w').write('\n'.join(' '.join(v) for v in lines.values()) + '\n')
pickle.dump((recs, lab), open(outp + '.pkl', 'wb'))
print(len(recs), 'glyphs', n, 'clusters')
