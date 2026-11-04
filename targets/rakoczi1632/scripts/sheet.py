"""sheet.py OUT.jpg IMG [IMG ...]: contact sheet, 4 per row, each scaled to 400 px wide, labelled"""
import sys
from PIL import Image, ImageDraw
ims = [Image.open(p).convert('L') for p in sys.argv[2:]]
w = 400; ims = [i.resize((w, int(i.height * w / i.width))) for i in ims]
h = max(i.height for i in ims); cols = 4; rows = (len(ims) + cols - 1) // cols
S = Image.new('L', (cols * w, rows * (h + 20)), 255); d = ImageDraw.Draw(S)
for k, (i, p) in enumerate(zip(ims, sys.argv[2:])):
    x, y = (k % cols) * w, (k // cols) * (h + 20); S.paste(i, (x, y + 20)); d.text((x + 5, y + 3), p.split('_p')[-1], fill=0)
S.save(sys.argv[1], quality=85)
