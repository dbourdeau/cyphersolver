"""strip.py frame side n k out : crop strip k of n (overlapping 4%) from leaf side L/R/F of M35 reel 3 frame; 1800 wide.
Reads images from ../../../../jqa/img03 (main checkout) or img03."""
import sys, os
from PIL import Image
fr, side, n, k, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
src = os.environ.get('JQA_IMG', 'C:/Users/dbour/cypher/jqa/img03')
im = Image.open(f'{src}/M35-03-{fr}.jpg').convert('L'); W, H = im.size
x0, x1 = {'L': (0, .52), 'R': (.48, 1), 'F': (0, 1)}[side]
y0 = max(0, k/n - .03); y1 = min(1, (k+1)/n + .03)
im = im.crop((int(x0*W), int(y0*H), int(x1*W), int(y1*H)))
if im.width > 1800: im = im.resize((1800, int(im.height*1800/im.width)))
im.save(out)
