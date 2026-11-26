"""Cut a window of the deskewed flat recto for reading, with a native-pixel ruler.
Usage: python win.py <line 1-10> <x0> <width> [scale] [out] [--cuts x1,x2,...] [--gray]
Line centres (deskewed native y) are in CY. Ruler ticks every 50 px, labels every 100 (native x)."""
import sys, os, cv2, numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
CY = [680, 945, 1170, 1404, 1664, 1881, 2124, 2348, 2616, 2828]
a = [x for x in sys.argv[1:] if not x.startswith('--')]
line, x0, w = int(a[0]), int(a[1]), int(a[2])
sc = float(a[3]) if len(a) > 3 else 2.0
out = a[4] if len(a) > 4 else 'img/w/win.png'
cuts = []
gray = '--gray' in sys.argv
for i, x in enumerate(sys.argv):
    if x == '--cuts':
        cuts = [int(v) for v in sys.argv[i + 1].split(',') if v]
src = cv2.imread('img/w/deskew_gray.png' if gray else 'img/w/flat.png', 0)
cy = CY[line - 1]
up, dn = 200, 160
if line == 1:
    up = 190
y0 = max(cy - up, 0)
crop = src[y0:cy + dn, x0:x0 + w]
im = cv2.resize(crop, None, fx=sc, fy=sc, interpolation=cv2.INTER_CUBIC)
im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
bar = np.full((28, im.shape[1], 3), 255, np.uint8)
for x in range((x0 // 50) * 50, x0 + w + 1, 50):
    if x < x0:
        continue
    px = int((x - x0) * sc)
    cv2.line(bar, (px, 18 if x % 100 == 0 else 24), (px, 28), (0, 0, 0), 1)
    if x % 100 == 0:
        cv2.putText(bar, str(x), (px + 2, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 160), 1)
for x in cuts:
    px = int((x - x0) * sc)
    if 0 <= px < im.shape[1]:
        cv2.line(im, (px, 0), (px, im.shape[0]), (0, 0, 255), 1)
        cv2.putText(bar, '|', (px - 3, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 0, 0), 1)
if '--ids' in sys.argv:
    import json
    comps = json.load(open('img/w/comps.json'))
    for c in comps:
        if c['x'] + c['w'] < x0 or c['x'] > x0 + w or c['y'] + c['h'] < y0 or c['y'] > cy + dn:
            continue
        px = int((c['cx'] - x0) * sc); py = int((c['y'] - y0) * sc) - 4
        py = max(py, 12)
        t = str(c['k']) if c['line'] == line else '%d:%d' % (c['line'], c['k'])
        col = (0, 0, 255) if c['line'] == line else (200, 100, 0)
        cv2.putText(im, t, (px - 8, py), cv2.FONT_HERSHEY_SIMPLEX, 0.5, col, 1 if c['line'] != line else 2)
if '--seg' in sys.argv:
    import json
    segs = json.load(open('segments_%s.json' % sys.argv[sys.argv.index('--seg') + 1])).get(str(line), [])
    for k, (a0, a1, lab, g) in enumerate(segs, 1):
        for xx in (a0, a1):
            px = int((xx - x0) * sc)
            if 0 <= px < im.shape[1]:
                cv2.line(im, (px, 0), (px, 14), (255, 0, 0), 1)
        pc = int(((a0 + a1) / 2 - x0) * sc)
        if 0 <= pc < im.shape[1]:
            cv2.putText(im, '%d%s' % (k, lab), (pc - 12, im.shape[0] - 6 - (k % 2) * 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1)
            cv2.line(im, (pc, im.shape[0] - 30), (pc, im.shape[0] - 24), (0, 0, 255), 1)
cv2.imwrite(out, np.vstack([bar, im]))
print(out, im.shape)
