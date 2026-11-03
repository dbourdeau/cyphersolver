"""Downscaled page with a y-ruler in fractions, to pick line centres: python ruler.py <page.jpg> <out.jpg> [y0 y1]"""
import sys
from PIL import Image, ImageDraw, ImageFont
im = Image.open(sys.argv[1]).convert("RGB"); y0, y1 = (float(sys.argv[3]), float(sys.argv[4])) if len(sys.argv) > 4 else (0, 1)
c = im.crop((0, int(y0*im.height), im.width, int(y1*im.height))); sc = 1100/c.width; c = c.resize((1100, int(c.height*sc)))
pad = Image.new("RGB", (1200, c.height), "white"); pad.paste(c, (100, 0)); d = ImageDraw.Draw(pad); f = ImageFont.load_default(size=16)
step = 0.005
y = y0
while y <= y1 + 1e-9:
    yy = int((y-y0)*im.height*sc); big = abs(round(y*100) - y*100) < 1e-6
    d.line((60 if big else 85, yy, 100, yy), fill=(255, 0, 0), width=1)
    if big: d.text((2, yy-8), f"{y:.2f}", fill=(255, 0, 0), font=f)
    y += step
pad.save(sys.argv[2], quality=90)
