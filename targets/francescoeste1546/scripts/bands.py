"""Cut one tight band per cipher line (centre +-HH rows), split in two overlapping halves stacked, for sign-first copying.
The band is tight so that the interlinear clear (about 85 rows above the centre) is mostly cut away.
usage: bands.py  -> scans/bands/<line>.jpg"""
import os
from PIL import Image, ImageOps
LINES = {
 'c0': [1765,1917,2100,2255,2397,2564,2712,2866,3029,3184,3338,3493,3666,3828],
 'c1': [727,874,1017,1154,1303,1455,1611,1768,1918,2087,2248,2397,2562,2712,2871,3026,3181,3330,3494,3654,3822],
 'c2': [738,880,1026,1161,1305,1462,1619,1771,1932,2108,2261,2411,2573,2736,2888,3042,3200,3357,3512],
}
HH_UP, HH_DN = 44, 55
X0, X1 = 330, 3020
def band(page, c, scale=0.8):
    im = Image.open(f'scans/{page}_full.jpg').convert('L')
    mid = (X0 + X1) // 2
    a = im.crop((X0, c - HH_UP, mid + 80, c + HH_DN)); b = im.crop((mid - 80, c - HH_UP, X1, c + HH_DN))
    o = Image.new('L', (max(a.width, b.width), a.height + b.height + 12), 255)
    o.paste(a, (0, 0)); o.paste(b, (0, a.height + 12))
    o = ImageOps.autocontrast(o, cutoff=1)
    return o.resize((int(o.width * scale), int(o.height * scale)), Image.LANCZOS).convert('RGB')
def names():
    for p, cs in LINES.items():
        for i, c in enumerate(cs):
            yield f'{p}L{i:02d}', p, c
if __name__ == '__main__':
    os.makedirs('scans/bands', exist_ok=True)
    for n, p, c in names():
        band(p, c).save(f'scans/bands/{n}.jpg', quality=92)
    print('ok')
