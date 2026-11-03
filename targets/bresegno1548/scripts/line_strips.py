"""Cut c. 15r cipher lines into labelled half-line strips and stack them, 6 per sheet.
Line centres from an ink profile (scripts run on the git-ignored full-size scan)."""
import sys
from PIL import Image, ImageDraw
src, outdir = sys.argv[1], sys.argv[2]
C = [1220,1323,1431,1543,1644,1731,1826,1932,2027,2123,2216,2320,2417,2505,2597,2694,2782,2881,2980,3070,3177,3268,3362,3458]
im = Image.open(src)
halves = [(250, 1720), (1580, 3000)]
strips = []
for i, c in enumerate(C, 1):
    for h, (x0, x1) in enumerate(halves):
        dy = 0 if h == 0 else -45
        s = im.crop((x0, c - 62 + dy, x1, c + 88 + dy))
        lab = Image.new('RGB', (s.width, s.height + 22), 'white')
        lab.paste(s, (0, 22))
        ImageDraw.Draw(lab).text((5, 3), f'L{i:02d}{"ab"[h]}', fill=(255, 0, 0))
        strips.append(lab)
for k in range(0, len(strips), 6):
    grp = strips[k:k + 6]
    sheet = Image.new('RGB', (max(g.width for g in grp), sum(g.height + 8 for g in grp)), (200, 200, 200))
    y = 0
    for g in grp:
        sheet.paste(g, (0, y)); y += g.height + 8
    sheet.save(f'{outdir}/sheet{k // 6:02d}.jpg', quality=93)
print(len(strips))
