"""band.py SRC.jpg OUTPREFIX y0 y1 step [scale]: for each band [y, y+step] (fractions), stack the left half (x 0.10-0.58)
over the right half (x 0.52-1.0) at the given scale (default 2.0), autocontrast; for close sign reading."""
import sys
from PIL import Image, ImageOps
src, pre = sys.argv[1], sys.argv[2]; y0, y1, st = map(float, sys.argv[3:6]); sc = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0
im = Image.open(src).convert('L'); W, H = im.size
k = 0; y = y0
while y < y1 - 1e-6:
    a, b = int(y * H), int(min(y + st + 0.008, 1) * H)
    L = im.crop((int(0.10 * W), a, int(0.58 * W), b)); R = im.crop((int(0.52 * W), a, W, b))
    L = ImageOps.autocontrast(L, cutoff=1); R = ImageOps.autocontrast(R, cutoff=1)
    w = max(L.width, R.width); S = Image.new('L', (w, L.height + R.height + 6), 0); S.paste(L, (0, 0)); S.paste(R, (0, L.height + 6))
    S = S.resize((int(S.width * sc), int(S.height * sc)), Image.LANCZOS); S.save(f'{pre}_{k:02d}.jpg', quality=92)
    k += 1; y += st
