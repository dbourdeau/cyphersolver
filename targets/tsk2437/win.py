"""Reading windows for the K24.37 recto. Usage: python win.py <out> x0 y0 x1 y1 scale mode
mode: flat | clahe | unsharp | thresh | raw | tri (stack of raw,flat,clahe). Needs img/recto.jpg (git-ignored)."""
import os
import sys
import numpy as np
import cv2

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    return cv2.imread(os.path.join(HERE, 'img', 'recto.jpg'), cv2.IMREAD_GRAYSCALE)


def render(g, x0, y0, x1, y1, scale, mode):
    pad = 160
    X0, Y0 = max(0, x0 - pad), max(0, y0 - pad)
    sub = g[Y0:y1 + pad, X0:x1 + pad].astype(np.float32)
    bg = cv2.GaussianBlur(sub, (0, 0), 30)
    if mode == 'flat':
        o = np.clip(150 + (sub - bg) * 1.8, 0, 255)
    elif mode == 'clahe':
        o = cv2.createCLAHE(3.0, (8, 8)).apply(np.clip(150 + (sub - bg) * 1.2, 0, 255).astype(np.uint8)).astype(np.float32)
    elif mode == 'unsharp':
        bl = cv2.GaussianBlur(sub, (0, 0), 4)
        o = np.clip(sub + 2.0 * (sub - bl), 0, 255)
        o = np.clip(150 + (o - bg) * 1.4, 0, 255)
    elif mode == 'thresh':
        d = bg - cv2.GaussianBlur(sub, (0, 0), 1.2)
        o = np.where(d > 30, 0, 255).astype(np.float32)
    else:
        o = sub
    o = o.astype(np.uint8)
    c = o[y0 - Y0:y1 - Y0, x0 - X0:x1 - X0]
    return cv2.resize(c, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)


if __name__ == '__main__':
    out = sys.argv[1]
    x0, y0, x1, y1 = [int(v) for v in sys.argv[2:6]]
    scale = float(sys.argv[6])
    mode = sys.argv[7] if len(sys.argv) > 7 else 'flat'
    g = load()
    if mode == 'tri':
        c = np.vstack([render(g, x0, y0, x1, y1, scale, m) for m in ('raw', 'flat', 'clahe')])
    else:
        c = render(g, x0, y0, x1, y1, scale, mode)
    if '--ruler' in sys.argv or True:
        c = cv2.cvtColor(c, cv2.COLOR_GRAY2BGR)
        for x in range((x0 // 50 + 1) * 50, x1, 50):
            px = int((x - x0) * scale)
            long_ = (x % 100 == 0)
            cv2.line(c, (px, 0), (px, 14 if long_ else 7), (0, 0, 255), 1)
            if long_:
                cv2.putText(c, str(x), (px + 2, 26), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    cv2.imwrite(out, c)
    print(out, c.shape)
