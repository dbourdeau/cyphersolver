"""Crop a region of a scan and upscale. python crop.py img x0 y0 x1 y1 scale out"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image
im = Image.open(sys.argv[1])
x0, y0, x1, y1 = map(int, sys.argv[2:6]); s = float(sys.argv[6])
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
c.save(sys.argv[7], quality=93)
