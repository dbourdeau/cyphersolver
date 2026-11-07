import pickle, numpy as np, cv2, collections, json
recs, lab = pickle.load(open('ctts/h64.txt.pkl', 'rb')); lab = np.array(lab)
F = np.array([r['feat'] for r in recs])
cnt = collections.Counter(lab); rank = {c: i for i, (c, _) in enumerate(cnt.most_common())}
tok = np.array([rank[l] for l in lab]); K = len(rank)
cent = np.array([F[tok == c].mean(0) for c in range(K)])
D = np.sqrt(((F[:, None, :] - cent[None]) ** 2).sum(2))
# medoid mask per cluster
med = {}
for c in range(K):
    idx = np.where(tok == c)[0]; j = idx[np.argmin(D[idx, c])]; med[c] = recs[j]['mask']
cand = []
for i in range(len(F)):
    o = np.argsort(D[i]); c0 = tok[i]; c1 = o[0] if o[0] != c0 else o[1]
    cand.append((D[i, c0] - D[i, c1], i, c0, c1))      # >0 when the other cluster is nearer; small abs = ambiguous
own=[(D[i,tok[i]],)+c for i,c in zip(range(len(F)),[(x[1],x[2],x[3]) for x in cand])]
own.sort(key=lambda x:-x[0])
sel=[(a,i,c0,c1) for a,i,c0,c1 in own[:360]]
json.dump([(int(i), int(c0), int(c1)) for _, i, c0, c1 in sel], open('ctts/review_items_out.json', 'w'))
def tile(m, S=54):
    m = 255 - m; h, w = m.shape; s = min((S - 4) / h, (S - 4) / w, 3.0)
    m = cv2.resize(m, (max(1, int(w * s)), max(1, int(h * s))), interpolation=cv2.INTER_AREA)
    t = np.full((S, S), 255, np.uint8); t[(S - m.shape[0]) // 2:(S - m.shape[0]) // 2 + m.shape[0], (S - m.shape[1]) // 2:(S - m.shape[1]) // 2 + m.shape[1]] = m; return t
for page in range(9):
    items = sel[page * 40:(page + 1) * 40]
    rows = []
    for r in range(10):
        row = []
        for c in range(4):
            k = r * 4 + c
            if k >= len(items): row.append(np.full((60, 190), 255, np.uint8)); continue
            _, i, c0, c1 = items[k]
            cell = np.full((60, 190), 255, np.uint8)
            cell[3:57, 28:82] = tile(recs[i]['mask']); cell[3:57, 84:138] = tile(med[c0]); cell[3:57, 138:190] = tile(med[c1])[:, :52]
            cv2.putText(cell, str(page * 40 + k), (1, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, 0, 1)
            cv2.putText(cell, 'A', (86, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.33, 120, 1); cv2.putText(cell, 'B', (140, 10), cv2.FONT_HERSHEY_SIMPLEX, 0.33, 120, 1)
            cv2.rectangle(cell, (0, 0), (189, 59), 200, 1)
            row.append(cell)
        rows.append(np.hstack(row))
    cv2.imwrite(f'ctts/reviewo_{page}.png', np.vstack(rows))
print(len(sel),'outliers; d1 range',round(sel[0][0],2),round(sel[-1][0],2))
