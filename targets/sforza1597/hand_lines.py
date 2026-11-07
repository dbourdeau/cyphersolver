"""Hand review tooling: numbered-box line images (page frame) + cluster legend for R5464.
usage: python hand_lines.py legend | line <page P1|P2> <line_no>"""
import sys, pickle, collections, numpy as np, cv2, os
proj = 'ctts_proj/R5464'
recs, lab = pickle.load(open('ctts/p100_0.4.txt.pkl', 'rb')); lab = np.array(lab)
cnt = collections.Counter(lab); rank = {c: i for i, (c, _) in enumerate(cnt.most_common())}
tok = np.array([rank[l] for l in lab])
def legend():
    F = np.array([r['feat'] for r in recs]); tiles = []
    for c in range(len(rank)):
        idx = np.where(tok == c)[0]; cen = F[idx].mean(0); j = idx[np.argmin(np.linalg.norm(F[idx] - cen, axis=1))]
        m = 255 - recs[j]['mask']; h, w = m.shape; s = min(40 / h, 40 / w, 2.5)
        m = cv2.resize(m, (max(1, int(w * s)), max(1, int(h * s))), interpolation=cv2.INTER_AREA)
        t = np.full((64, 64), 255, np.uint8); t[2:2 + m.shape[0], 2:2 + m.shape[1]] = m
        cv2.putText(t, f's{c}', (2, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.38, 0, 1); cv2.rectangle(t, (0, 0), (63, 63), 190, 1); tiles.append(t)
    rows = [np.hstack(tiles[i:i + 10] + [np.full((64, 64), 255, np.uint8)] * (10 - len(tiles[i:i + 10]))) for i in range(0, len(tiles), 10)]
    cv2.imwrite('ctts/hand_legend.png', np.vstack(rows))
def lines_of(page):
    L = []; cur = []
    for l in open(f'{proj}/positions/R5464_{page}_positions.txt'):
        if l.strip(): cur.append(list(map(float, l.split())))
        elif cur: L.append(cur); cur = []
    if cur: L.append(cur)
    return L
def line(page, n):
    im = cv2.imread(f'{proj}/R5464_{page}.png'); L = lines_of(page)[n - 1]
    x0 = int(min(b[0] for b in L)) - 10; x1 = int(max(b[0] + b[2] for b in L)) + 10
    y0 = int(min(b[1] for b in L)) - 30; y1 = int(max(b[1] + b[3] for b in L)) + 30
    crop = im[max(0, y0):y1, max(0, x0):x1].copy()
    S = 2; crop = cv2.resize(crop, None, fx=S, fy=S, interpolation=cv2.INTER_CUBIC)
    for k, (x, y, w, h, c) in enumerate(L):
        a = (int((x - max(0, x0)) * S), int((y - max(0, y0)) * S)); b = (int((x + w - max(0, x0)) * S), int((y + h - max(0, y0)) * S))
        cv2.rectangle(crop, a, b, (0, 0, 255), 1)
        cv2.putText(crop, f'{k}', (a[0], a[1] - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (200, 0, 0), 1)
        cv2.putText(crop, f's{int(c)}', (a[0], b[1] + 14), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 120, 0), 1)
    H, W = crop.shape[:2]; k3 = 5; seg = W // k3 + 70; parts = []
    for i in range(k3):
        a = min(i * (W // k3), W - seg); p = crop[:, a:a + seg]; parts.append(p); parts.append(np.full((10, seg, 3), 255, np.uint8))
    out = np.vstack(parts[:-1])
    os.makedirs('ctts/hand', exist_ok=True); cv2.imwrite(f'ctts/hand/{page}_{n:02d}.png', out); print(len(L), 'boxes', out.shape)
if __name__ == '__main__':
    legend() if sys.argv[1] == 'legend' else line(sys.argv[2], int(sys.argv[3]))
