"""python prep.py <tag> <first> <last> [width] : screening copies (img/v/<tag>_<idx>.jpg) of the fetched frames."""
import os, sys, glob
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
tag, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); W = int(sys.argv[4]) if len(sys.argv) > 4 else 1100
os.makedirs(os.path.join(here, 'img', 'v'), exist_ok=True)
for i in range(a, b + 1):
    g = glob.glob(os.path.join(here, 'img', tag, '%03d_*.jpg' % i))
    if not g: print(i, 'NOT FETCHED'); continue
    im = Image.open(g[0]); w, h = im.size
    im.resize((W, int(h * W / w)), Image.LANCZOS).save(os.path.join(here, 'img', 'v', '%s_%03d.jpg' % (tag, i)), quality=78)
    print(i, os.path.basename(g[0]))
