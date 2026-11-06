"""Cut one strip per detected text line and stack three lines per image, labelled with the line number."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw
import numpy as np
from scipy.signal import find_peaks

def lines(leaf):
    a = np.asarray(Image.open(f'img/{leaf}.jpg').convert('L'), dtype=float)
    H, W = a.shape
    band = a[300:H-200, int(W*.2):int(W*.8)]
    ink = (band < np.median(band) - 45).sum(axis=1).astype(float)
    sm = np.convolve(ink, np.ones(31)/31, mode='same')
    p, _ = find_peaks(sm, distance=75, height=sm.max()*0.15)
    return [int(y) + 300 for y in p]

if __name__ == '__main__':
    leaf = sys.argv[1]; scale = float(sys.argv[2]) if len(sys.argv) > 2 else 0.55
    im = Image.open(f'img/{leaf}.jpg')
    ys = lines(leaf)
    out = Path('crops/lines'); out.mkdir(parents=True, exist_ok=True)
    x0, x1 = 150, im.width - 120
    for i in range(0, len(ys), 3):
        strips = []
        for j, y in enumerate(ys[i:i+3]):
            s = im.crop((x0, y - 75, x1, y + 70))
            s = s.resize((int(s.width*scale), int(s.height*scale)))
            d = ImageDraw.Draw(s); d.text((2, 2), f'L{i+j+1:02d}', fill=(200, 0, 0))
            strips.append(s)
        o = Image.new('RGB', (strips[0].width, sum(s.height for s in strips)), 'white')
        y = 0
        for s in strips: o.paste(s, (0, y)); y += s.height
        o.save(out / f'{leaf}_L{i+1:02d}.jpg', quality=88)
    print(leaf, len(ys), ys)
