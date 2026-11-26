"""Cut a line into overlapping reading windows. Usage: python mkwin.py <tag> x0 x1 y0 y1 [width=700] [scale=2.5] [mode=flat]
Writes img/w/<tag>_<k>.png. For sloping lines pass y0,y1 as 'ya:yb' pairs for the left and right ends (linear)."""
import os
import sys
import cv2
import win

tag = sys.argv[1]
x0, x1 = int(sys.argv[2]), int(sys.argv[3])
ys = [s.split(':') for s in (sys.argv[4], sys.argv[5])]
width = int(sys.argv[6]) if len(sys.argv) > 6 else 700
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.5
mode = sys.argv[8] if len(sys.argv) > 8 else 'flat'
step = width - 70
g = win.load()
k = 0
x = x0
while x < x1:
    xe = min(x + width, x1)
    f0 = (x - x0) / max(1, x1 - x0)
    f1 = (xe - x0) / max(1, x1 - x0)

    def yy(i, f):
        a = int(ys[i][0]) if len(ys[i]) == 1 else int(ys[i][0]) + f * (int(ys[i][1]) - int(ys[i][0]))
        return a
    ya = int(min(yy(0, f0), yy(0, f1)))
    yb = int(max(yy(1, f0), yy(1, f1)))
    c = win.render(g, x, ya, xe, yb, scale, mode)
    import numpy as np
    c = cv2.cvtColor(c, cv2.COLOR_GRAY2BGR)
    for xr in range((x // 50 + 1) * 50, xe, 50):
        px = int((xr - x) * scale)
        lg = xr % 100 == 0
        cv2.line(c, (px, 0), (px, 14 if lg else 7), (0, 0, 255), 1)
        if lg:
            cv2.putText(c, str(xr), (px + 2, 26), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    out = os.path.join(win.HERE, 'img', 'w', '%s_%d.png' % (tag, k))
    cv2.imwrite(out, c)
    print(out, x, xe, ya, yb, c.shape)
    k += 1
    x += step
