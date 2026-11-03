"""Equal-pitch line bands: python bands.py <page.jpg> <prefix> <x0> <x1> <yfirst> <ylast> <nlines> <startno> [K] [outwidth]
yfirst/ylast = fractional y of the centre of the first and last line. Writes numbered crops of K lines."""
import sys, os
from PIL import Image, ImageDraw, ImageFont
p, pre = sys.argv[1], sys.argv[2]
fx0, fx1, ya, yb = map(float, sys.argv[3:7]); n = int(sys.argv[7]); st = int(sys.argv[8])
K = int(sys.argv[9]) if len(sys.argv) > 9 else 4; OW = int(sys.argv[10]) if len(sys.argv) > 10 else 1800
im = Image.open(p).convert("RGB"); W, H = im.size
pitch = (yb-ya)*H/(n-1) if n > 1 else 0.03*H
cent = [ya*H + i*pitch for i in range(n)]
for b in range(0, n, K):
    js = list(range(b, min(b+K, n)))
    top, bot = int(cent[js[0]]-0.62*pitch), int(cent[js[-1]]+0.62*pitch)
    c = im.crop((int(fx0*W), top, int(fx1*W), bot)); sc = OW/c.width; c = c.resize((OW, int(c.height*sc)))
    pad = Image.new("RGB", (OW+70, c.height), "white"); pad.paste(c, (70, 0)); dr = ImageDraw.Draw(pad)
    for j in js:
        dr.text((4, int((cent[j]-top)*sc)-10), f"L{st+j:02d}", fill=(220, 0, 0), font=ImageFont.load_default(size=24))
    out = os.path.join(os.path.dirname(p), f"{pre}_L{st+js[0]:02d}-{st+js[-1]:02d}.jpg"); pad.save(out, quality=92); print(out, pad.size)
