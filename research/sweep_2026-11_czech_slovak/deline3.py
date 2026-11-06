"""Blank typed '=' underlines: a pixel row with >= N dark runs of length >= L is an underline row; blank those runs.
Usage: python deline3.py <src_dir> <dst_dir>"""
import os, sys
import numpy as np
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
L, N, F = 10, 4, 0.7
os.makedirs(dst, exist_ok=True)
for fn in sorted(os.listdir(src)):
    if not fn.endswith('.jpg') or os.path.exists(os.path.join(dst, fn)):
        continue
    g = np.asarray(Image.open(os.path.join(src, fn)).convert('L')).copy()
    d = g < 150
    for y in range(d.shape[0]):
        dd = np.diff(np.concatenate(([0], d[y].astype(np.int8), [0])))
        s, e = np.where(dd == 1)[0], np.where(dd == -1)[0]
        long_ = [(a, b) for a, b in zip(s, e) if b - a >= L]
        tot = int((e - s).sum()) if len(s) else 0
        if len(long_) >= N and sum(b - a for a, b in long_) >= F * tot:
            for a, b in long_:
                g[max(0, y - 1):y + 2, a:b] = 255
    Image.fromarray(g).save(os.path.join(dst, fn), quality=90)
