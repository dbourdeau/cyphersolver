import pickle, numpy as np, collections, sys
from sklearn.cluster import AgglomerativeClustering, KMeans
pages = ['R5464_P1_0', 'R5464_P2_0']; n_out = int(sys.argv[1]); outp = sys.argv[2]
meta, E = pickle.load(open('emb_f.pkl', 'rb')); E = E / (np.linalg.norm(E, axis=1, keepdims=True) + 1e-9)
recs = []; rows = []
for t in pages:
    r = pickle.load(open(f'sr_{t}/glyphs2.pkl', 'rb')); idx = [i for i, m in enumerate(meta) if m[0] == t]
    recs += r; rows += idx
H = np.array([g['feat'] for g in recs]); Em = E[rows]
asp = np.array([[np.log((g['w'] + 1) / (g['h'] + 1))] for g in recs])
Z = np.hstack([Em * 3, asp * 0.8]); HY = np.hstack([H, Em * 2])
n = len(recs); C = np.zeros((n, n), np.float32); runs = 0
for X in (H, Z, HY):
    for k in (50, 60, 70, 80):
        lab = AgglomerativeClustering(n_clusters=k, linkage='ward').fit(X).labels_
        C += (lab[:, None] == lab[None, :]); runs += 1
        lab = KMeans(n_clusters=k, n_init=1, random_state=k).fit(X).labels_
        C += (lab[:, None] == lab[None, :]); runs += 1
C /= runs
D = 1 - C
lab = AgglomerativeClustering(n_clusters=n_out, metric='precomputed', linkage='average').fit(D).labels_
cnt = collections.Counter(lab); rank = {c: i for i, (c, _) in enumerate(cnt.most_common())}
lines = collections.OrderedDict()
for g, l in zip(recs, lab): lines.setdefault((g['page'], g['line']), []).append(f's{rank[l]:02d}')
open(outp, 'w').write('\n'.join(' '.join(v) for v in lines.values()) + '\n')
print(n, 'glyphs', runs, 'clusterings ->', n_out, 'clusters; sizes', sorted(cnt.values(), reverse=True)[:10], '... smallest', sorted(cnt.values())[:5])
