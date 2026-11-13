"""Cut cipher lines into labelled part-line strips and stack them on sheets.
python strips.py img out_prefix x0 x1 parts scale per_sheet label_start c1,c2,...  (line centres, original px)"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw
img, out = sys.argv[1], sys.argv[2]
x0, x1, parts = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
scale, per = float(sys.argv[6]), int(sys.argv[7])
lab0 = int(sys.argv[8])
slope = float(sys.argv[10]) if len(sys.argv) > 10 else 0.0  # px drop per part
hh = int(sys.argv[11]) if len(sys.argv) > 11 else 48
C = [int(c) for c in sys.argv[9].split(',')]
im = Image.open(img)
w = (x1 - x0) / parts
strips = []
for i, c in enumerate(C):
    for p in range(parts):
        a = int(x0 + p * w - (25 if p else 0)); b = int(x0 + (p + 1) * w + (25 if p < parts - 1 else 0))
        d = int(slope * p)
        s = im.crop((a, c - hh + d, b, c + hh + d))
        s = s.resize((int(s.width * scale), int(s.height * scale)), Image.LANCZOS)
        lab = Image.new('RGB', (s.width, s.height + 22), 'white'); lab.paste(s, (0, 22))
        ImageDraw.Draw(lab).text((5, 3), f'L{lab0 + i:02d}{"abcd"[p]}', fill=(255, 0, 0))
        strips.append(lab)
for k in range(0, len(strips), per):
    g = strips[k:k + per]
    sh = Image.new('RGB', (max(x.width for x in g), sum(x.height + 8 for x in g)), (200, 200, 200))
    y = 0
    for x in g:
        sh.paste(x, (0, y)); y += x.height + 8
    sh.save(f'{out}_{k // per:02d}.jpg', quality=92)
print(len(strips), 'strips')
