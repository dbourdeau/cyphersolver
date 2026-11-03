"""Cut a stitched page into bands of K text lines, numbered, for sign transcription.
Usage: python lines.py <page.jpg> <prefix> <x0> <x1> <y0> <y1> [K] [outwidth]
x/y as fractions of the page. Lines found by a smoothed horizontal ink profile."""
import sys, os, numpy as np
from PIL import Image, ImageDraw, ImageFont
p, pre = sys.argv[1], sys.argv[2]
fx0, fx1, fy0, fy1 = map(float, sys.argv[3:7]); K = int(sys.argv[7]) if len(sys.argv) > 7 else 4
OW = int(sys.argv[8]) if len(sys.argv) > 8 else 1800
im = Image.open(p).convert("L"); W, H = im.size
x0, x1, y0, y1 = int(fx0*W), int(fx1*W), int(fy0*H), int(fy1*H)
a = np.asarray(im.crop((x0, y0, x1, y1)), dtype=float)
ink = (a < a.mean() - 2.2*a.std()).sum(1).astype(float)
k = max(3, int(H/400)); prof = np.convolve(ink, np.ones(k*3)/(k*3), mode="same")
thr = prof.max()*0.12; on = prof > thr
runs = []; s = None
for i, v in enumerate(on):
    if v and s is None: s = i
    if not v and s is not None:
        if i - s > H/250: runs.append((s, i))
        s = None
if s is not None: runs.append((s, len(on)))
cent = [(a_+b_)//2 for a_, b_ in runs]
print(len(cent), "lines")
cuts = [0] + [(runs[i][1]+runs[i+1][0])//2 for i in range(len(runs)-1)] + [y1-y0]
d = os.path.dirname(p)
for b in range(0, len(cent), K):
    top, bot = cuts[b], cuts[min(b+K, len(cent))]
    c = Image.open(p).convert("RGB").crop((x0, y0+top-10, x1, y0+bot+10))
    sc = OW / c.width; c = c.resize((OW, int(c.height*sc)))
    pad = Image.new("RGB", (OW+60, c.height), "white"); pad.paste(c, (60, 0)); dr = ImageDraw.Draw(pad)
    for j in range(b, min(b+K, len(cent))):
        yy = int((cent[j]-top+10)*sc); dr.text((5, yy-8), f"L{j+1:02d}", fill=(200, 0, 0), font=ImageFont.load_default(size=22))
    out = os.path.join(d, f"{pre}_L{b+1:02d}-{min(b+K,len(cent)):02d}.jpg"); pad.save(out, quality=92); print(out, pad.size)
