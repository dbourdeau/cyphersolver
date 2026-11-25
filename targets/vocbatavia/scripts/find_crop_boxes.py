"""Recover crop boxes (x, y, w, h in full-image pixels) of crops cut from NA IIIF full images by multi-scale template matching.
Usage: python3 -I find_crop_boxes.py <pairs.tsv> ; pairs.tsv: crop_path<TAB>full_path<TAB>iiif_label"""
import sys, cv2, numpy as np
for ln in open(sys.argv[1]):
    crop_p, full_p, lab = ln.rstrip('\n').split('\t')
    c = cv2.imread(crop_p, cv2.IMREAD_GRAYSCALE); f = cv2.imread(full_p, cv2.IMREAD_GRAYSCALE)
    best = None
    # crop may be scaled by s relative to the full image: crop = full_region * s
    for s in np.concatenate([np.arange(0.20, 1.0, 0.01), np.arange(1.0, 3.01, 0.02)]):
        k = 0.25  # search at quarter size for speed
        fs = cv2.resize(f, None, fx=k, fy=k, interpolation=cv2.INTER_AREA)
        cs = cv2.resize(c, None, fx=k/s, fy=k/s, interpolation=cv2.INTER_AREA)
        if cs.shape[0] >= fs.shape[0] or cs.shape[1] >= fs.shape[1] or min(cs.shape) < 8: continue
        r = cv2.matchTemplate(fs, cs, cv2.TM_CCOEFF_NORMED); _, mv, _, ml = cv2.minMaxLoc(r)
        if best is None or mv > best[0]: best = (mv, s, ml)
    mv, s, ml = best
    x, y = int(round(ml[0] / 0.25)), int(round(ml[1] / 0.25))
    w, h = int(round(c.shape[1] / s)), int(round(c.shape[0] / s))
    # refine at full resolution in a window
    cs = cv2.resize(c, (w, h), interpolation=cv2.INTER_AREA)
    x0, y0 = max(0, x - 20), max(0, y - 20)
    win = f[y0:y0 + h + 40, x0:x0 + w + 40]
    if win.shape[0] >= h and win.shape[1] >= w:
        r = cv2.matchTemplate(win, cs, cv2.TM_CCOEFF_NORMED); _, mv2, _, ml2 = cv2.minMaxLoc(r)
        x, y, mv = x0 + ml2[0], y0 + ml2[1], mv2
    print(f"{crop_p.split('/')[-1]}\t{lab}\t{x}\t{y}\t{w}\t{h}\t{c.shape[1]}x{c.shape[0]}\t{s:.2f}\t{mv:.3f}")
