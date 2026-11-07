import pickle, numpy as np, sys, json, collections
from sklearn.cluster import AgglomerativeClustering
pages = {'R5460': 'sr_R5460', 'R5459_P1_0': 'sr_R5459_P1_0', 'R5463_P_0': 'sr_R5463_P_0', 'R5464_P1_0': 'sr_R5464_P1_0', 'R5465_P1_0': 'sr_R5465_P1_0'}
recs = []
for t, d in pages.items():
    r = pickle.load(open(f'{d}/glyphs.pkl', 'rb'))
    if t == 'R5460': r = [g for g in r if g['line'] <= 8]
    recs += r
print({t: sum(1 for g in recs if g['page'] == t) for t in pages})
F = np.array([g['feat'] for g in recs])
n = int(sys.argv[1])
cl = AgglomerativeClustering(n_clusters=n, linkage='ward').fit(F)
lab = cl.labels_
tab = collections.defaultdict(collections.Counter)
for g, l in zip(recs, lab): tab[l][g['page']] += 1
order = sorted(tab, key=lambda c: -sum(tab[c].values()))
for c in order[:40]:
    tot = sum(tab[c].values())
    print(c, tot, {p[:5] + p[-4:] if len(p) > 5 else p: round(v / tot, 2) for p, v in tab[c].items()})
pickle.dump((recs, lab), open('pool_clusters.pkl', 'wb'))
