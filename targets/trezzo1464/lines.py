"""Cut a page region into text-line strips by its ink profile.

usage: python3 lines.py <image> <x0> <y0> <x1> <y1> <outprefix> [parts] [spacing_px]

Coordinates are fractions of the image width/height. Rows whose dark-pixel count is a local maximum of the smoothed
profile are taken as line centres; each strip runs halfway to the neighbouring centres, and is cut into `parts`
overlapping pieces along the line (default 2). Prints one row per line: index, centre y (pixels), strip height.
"""
import sys
import numpy as np
from PIL import Image


def main():
    path, x0, y0, x1, y1, out = sys.argv[1:7]
    parts = int(sys.argv[7]) if len(sys.argv) > 7 else 2
    spacing = int(sys.argv[8]) if len(sys.argv) > 8 else 0
    im = Image.open(path).convert('L')
    W, H = im.size
    box = (int(float(x0) * W), int(float(y0) * H), int(float(x1) * W), int(float(y1) * H))
    reg = np.asarray(im.crop(box), dtype=float)
    dark = (reg < 110).sum(axis=1).astype(float)
    k = max(5, spacing // 4 if spacing else reg.shape[0] // 120)
    sm = np.convolve(dark, np.ones(2 * k + 1) / (2 * k + 1), mode='same')
    thr = sm.max() * 0.25
    peaks = [i for i in range(1, len(sm) - 1) if sm[i] >= sm[i - 1] and sm[i] > sm[i + 1] and sm[i] > thr]
    merged = []
    for p in peaks:
        if merged and p - merged[-1] < (0.7 * spacing if spacing else 3 * k):
            if sm[p] > sm[merged[-1]]:
                merged[-1] = p
        else:
            merged.append(p)
    rgb = Image.open(path).convert('RGB').crop(box)
    w = rgb.width
    for n, c in enumerate(merged):
        up = (c - merged[n - 1]) // 2 if n else 3 * k * 2
        dn = (merged[n + 1] - c) // 2 if n + 1 < len(merged) else 3 * k * 2
        top, bot = max(0, c - int(up * 1.25)), min(rgb.height, c + int(dn * 1.1))
        strip = rgb.crop((0, top, w, bot))
        step = w // parts
        for j in range(parts):
            a, b = max(0, j * step - 60), min(w, (j + 1) * step + 60)
            strip.crop((a, 0, b, strip.height)).save('%s_%02d%s.jpg' % (out, n + 1, 'abcdef'[j]), quality=90)
        print(n + 1, box[1] + c, bot - top)


if __name__ == '__main__':
    main()
