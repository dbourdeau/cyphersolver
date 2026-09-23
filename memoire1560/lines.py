"""Split each page into line strips by horizontal ink projection; write contrast-enhanced strips to lines/."""
import os, glob, sys
import numpy as np
from PIL import Image, ImageOps, ImageFilter
os.makedirs("lines", exist_ok=True)
for fn in sorted(glob.glob("pages/f*.jpg")):
    fol = os.path.basename(fn)[1:-4]
    g = Image.open(fn).convert("L")
    a = np.asarray(g).astype(float)
    bg = np.asarray(g.filter(ImageFilter.BoxBlur(40))).astype(float)
    d = bg - a                      # darkness relative to local background
    h, w = a.shape
    x0, x1 = int(w * 0.12), int(w * 0.92)
    ink = (d[:, x0:x1] > 35).sum(1)
    sm = np.convolve(ink, np.ones(31) / 31, "same")
    y0, y1 = int(h * 0.03), int(h * 0.97)
    # local maxima spaced >= 120 px
    peaks = []
    thr = np.percentile(sm[y0:y1], 90) * 0.35
    for y in range(y0 + 60, y1 - 60):
        if sm[y] > thr and sm[y] == sm[y - 60:y + 61].max():
            if not peaks or y - peaks[-1] > 120: peaks.append(y)
    print(fol, len(peaks))
    en = ImageOps.autocontrast(g, cutoff=1)
    for k, c in enumerate(peaks):
        en.crop((int(w * 0.08), max(0, c - 120), int(w * 0.97), min(h, c + 110))).save(f"lines/{fol}_{k:02d}.png")
