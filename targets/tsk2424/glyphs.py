"""Automatic first-pass token stream for T-S K24.24 recto: ink components -> lines -> shape clusters.
Usage: python glyphs.py <image> <outdir> [k]
Component = one connected ink stroke group (pen-lift level), not necessarily one sign. Writes comps_lines.json,
clusters sheet (sheet_k.png), tokens.txt (one line of cluster labels per text line, page order left to right)."""
import sys, json, os
import numpy as np
import cv2
from scipy.cluster.vq import kmeans2

img, out = sys.argv[1], sys.argv[2]
K = int(sys.argv[3]) if len(sys.argv) > 3 else 30
os.makedirs(out, exist_ok=True)
X0, Y0, X1, Y1 = 300, 520, 3380, 3150
g = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
sub = g[Y0:Y1, X0:X1].astype(np.float32)
bg = cv2.medianBlur(sub.astype(np.uint8), 101).astype(np.float32)
ink = ((bg - sub) > 45).astype(np.uint8)
ink = cv2.morphologyEx(ink, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
n, lab, st, cen = cv2.connectedComponentsWithStats(ink, 8)
comps = []
for i in range(1, n):
    x, y, w, h, a = st[i]
    if a >= 500:
        kind = 'g'
    elif a >= 200 and w < 70 and h < 70:
        kind = 'dot'
    else:
        continue
    comps.append(dict(i=i, x=int(x + X0), y=int(y + Y0), w=int(w), h=int(h), a=int(a), kind=kind))
gl = [c for c in comps if c['kind'] == 'g']
cy = np.array([c['y'] + c['h'] * 0.65 for c in comps])
cx = np.array([c['x'] + c['w'] / 2 for c in comps])
yy = cy - (-0.02) * cx  # slope 0.02 found best (lines rise to the left)
yy = cy + 0.02 * cx - 0  # same as before in correct sign: cy - slope*cx with slope=0.02 -> cy - 0.02 cx
yy = cy - 0.02 * cx
np.random.seed(0)
best = None
for seed in range(8):
    np.random.seed(seed)
    c_, l_ = kmeans2(yy.reshape(-1, 1), 10, minit='++')
    sse = sum(((yy[l_ == j] - c_[j]) ** 2).sum() for j in range(10))
    if best is None or sse < best[0]:
        best = (sse, c_.ravel(), l_)
order = np.argsort(best[1])
rank = {int(o): r for r, o in enumerate(order)}
for c, l in zip(comps, best[2]):
    c['line'] = rank[int(l)] + 1


def feat(c):
    m = (lab[c['y'] - Y0:c['y'] - Y0 + c['h'], c['x'] - X0:c['x'] - X0 + c['w']] == c['i']).astype(np.uint8)
    s = max(m.shape)
    sq = np.zeros((s, s), np.uint8)
    oy, ox = (s - m.shape[0]) // 2, (s - m.shape[1]) // 2
    sq[oy:oy + m.shape[0], ox:ox + m.shape[1]] = m
    sm = cv2.resize(sq.astype(np.float32), (14, 14), interpolation=cv2.INTER_AREA).ravel()
    aspect = c['w'] / max(c['h'], 1)
    return np.concatenate([sm, [min(aspect, 3) / 3 * 2, min(c['a'] / 6000, 1.5)]]), m


F = []
masks = {}
for c in gl:
    f, m = feat(c)
    F.append(f)
    masks[c['i']] = m
F = np.array(F)
np.random.seed(1)
best2 = None
for seed in range(10):
    np.random.seed(seed)
    c_, l_ = kmeans2(F, K, minit='++')
    sse = sum(((F[l_ == j] - c_[j]) ** 2).sum() for j in range(K) if (l_ == j).any())
    if best2 is None or sse < best2[0]:
        best2 = (sse, c_, l_)
labs = best2[2]
sizes = np.bincount(labs, minlength=K)
rankc = {int(j): r for r, j in enumerate(np.argsort(-sizes))}
for c, l in zip(gl, labs):
    c['cl'] = rankc[int(l)]
json.dump(comps, open(os.path.join(out, 'comps_lines.json'), 'w'))
with open(os.path.join(out, 'tokens.txt'), 'w') as fh:
    for ln in range(1, 11):
        row = sorted([c for c in comps if c['line'] == ln], key=lambda c: c['x'])
        fh.write(' '.join(('.' if c['kind'] == 'dot' else 'C%02d' % c['cl']) for c in row) + '\n')
# contact sheet: per cluster a row of up to 14 exemplars
cell = 70
rows = []
for r in range(K):
    mem = [c for c in gl if c['cl'] == r][:16]
    row = np.full((cell, cell * 17), 255, np.uint8)
    cv2.putText(row, 'C%02d n=%d' % (r, sum(1 for c in gl if c['cl'] == r)), (2, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.45, 0, 1)
    for j, c in enumerate(mem):
        m = masks[c['i']]
        s = max(m.shape)
        sq = np.zeros((s, s), np.uint8)
        sq[(s - m.shape[0]) // 2:(s - m.shape[0]) // 2 + m.shape[0], (s - m.shape[1]) // 2:(s - m.shape[1]) // 2 + m.shape[1]] = m
        t = cv2.resize(sq * 255, (cell - 8, cell - 8), interpolation=cv2.INTER_AREA)
        row[4:cell - 4, cell * (j + 1) + 4:cell * (j + 1) + cell - 4] = 255 - t
    rows.append(row)
sheet = np.vstack(rows)
half = K // 2 * cell
cv2.imwrite(os.path.join(out, 'sheet_a.png'), sheet[:half])
cv2.imwrite(os.path.join(out, 'sheet_b.png'), sheet[half:])
print(len(gl), 'glyph comps', sum(1 for c in comps if c['kind'] == 'dot'), 'dots; per line', [sum(1 for c in comps if c['line'] == l) for l in range(1, 11)])
