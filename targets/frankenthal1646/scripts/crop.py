"""Rotate a thesis photograph upright and cut crops.

usage: python crop.py <frame> rot            -> work/<frame>_rot.jpg (rotated 90 deg clockwise)
       python crop.py <frame> <x0> <y0> <x1> <y1> <zoom> <name>   (coordinates on the rotated image)
"""
import sys, os
from PIL import Image, ImageOps, ImageEnhance

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCANS = os.path.join(BASE, 'scans')
WORK = os.path.join(BASE, 'work')
os.makedirs(WORK, exist_ok=True)

frame = sys.argv[1]
im = Image.open(os.path.join(SCANS, frame + '.jpg')).transpose(Image.ROTATE_270)
ang = float(os.environ.get('DESKEW', '0'))  # degrees, counterclockwise positive (PIL)
if ang:
    im = im.rotate(ang, resample=Image.BICUBIC, fillcolor=(200, 200, 200))
if sys.argv[2] == 'rot':
    im.save(os.path.join(WORK, frame + '_rot.jpg'), quality=90)
    print(im.size)
else:
    x0, y0, x1, y1 = map(int, sys.argv[2:6])
    z = float(sys.argv[6])
    name = sys.argv[7]
    c = im.crop((x0, y0, x1, y1)).convert('L')
    c = ImageOps.autocontrast(c, cutoff=1)
    c = ImageEnhance.Contrast(c).enhance(1.6)
    c = c.resize((int(c.width * z), int(c.height * z)), Image.LANCZOS)
    c.save(os.path.join(WORK, name + '.png'))
    print(c.size)
