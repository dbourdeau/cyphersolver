# pass-2 helper: cut each line band into two overlapping halves, enlarge 2x, stack 8 halves per sheet.
# usage: python stack.py <bands.tsv> <outprefix>   (bands.tsv: scan  line_id  x0  x1  y0  y1)
import sys, os
from PIL import Image, ImageOps, ImageDraw
rows = [l.split() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
halves = []
for scan, lid, x0, x1, y0, y1 in rows:
    x0, x1, y0, y1 = map(int, (x0, x1, y0, y1)); mid = (x0 + x1) // 2
    im = Image.open(os.path.join(os.environ.get('SD', 'scans2'), f'p{int(scan):04d}.png')).convert('L')
    for k, (a, b) in enumerate(((x0, mid + 40), (mid - 40, x1))):
        c = ImageOps.autocontrast(im.crop((a, y0, b, y1)), cutoff=1)
        c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
        halves.append((f'{lid}{"ab"[k]}', c))
for s in range(0, len(halves), 8):
    part = halves[s:s + 8]; W = max(c.width for _, c in part) + 90; H = sum(c.height + 6 for _, c in part)
    sheet = Image.new('L', (W, H), 255); d = ImageDraw.Draw(sheet); y = 0
    for lab, c in part:
        sheet.paste(c, (90, y)); d.text((4, y + 10), lab, fill=0); y += c.height + 6
    sheet.save(f'{sys.argv[2]}_{s // 8 + 1}.png')
print(len(halves))
