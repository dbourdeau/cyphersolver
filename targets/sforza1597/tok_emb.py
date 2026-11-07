import pickle, numpy as np, sys, collections
from sklearn.cluster import AgglomerativeClustering
n = int(sys.argv[1]); outp = sys.argv[2]; pages = sys.argv[3].split(',')
meta, E = pickle.load(open('emb_f.pkl', 'rb'))
E = E / (np.linalg.norm(E, axis=1, keepdims=True) + 1e-9)
recs = []; rows = []
for t in pages:
    r = pickle.load(open(f'sr_{t}/glyphs2.pkl', 'rb'))
    if t == 'R5460': r = [g for g in r if g['line'] <= 8]
    idx = [i for i, m in enumerate(meta) if m[0] == t]
    assert len(idx) == len(r), (t, len(idx), len(r))
    recs += r; rows += idx
X = E[rows]
asp = np.array([[np.log((g['w'] + 1) / (g['h'] + 1))] for g in recs])
Z = np.hstack([X * 3, asp * 0.8])
lab = AgglomerativeClustering(n_clusters=n, linkage='ward').fit(Z).labels_
cnt = collections.Counter(lab); rank = {c: i for i, (c, _) in enumerate(cnt.most_common())}
lines = collections.OrderedDict()
for g, l in zip(recs, lab): lines.setdefault((g['page'], g['line']), []).append(f's{rank[l]:02d}')
open(outp, 'w').write('\n'.join(' '.join(v) for v in lines.values()) + '\n')
pickle.dump((recs, lab), open(outp + '.pkl', 'wb')); print(len(recs), n)
