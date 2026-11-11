"""contact sheet of viewer screenshots: sheet.py <dir> [cols=4] [tile width=620] [first] [last]"""
import sys, glob
from PIL import Image
d = sys.argv[1]; cols = int(sys.argv[2]) if len(sys.argv) > 2 else 4; tw = int(sys.argv[3]) if len(sys.argv) > 3 else 620
fs = sorted(glob.glob(d + '/p*.png')); a = int(sys.argv[4]) if len(sys.argv) > 4 else 0; b = int(sys.argv[5]) if len(sys.argv) > 5 else len(fs); fs = fs[a:b]
ims = [Image.open(f).convert('RGB') for f in fs]; ims = [im.resize((tw, int(im.height * tw / im.width))) for im in ims]
rows = (len(ims) + cols - 1) // cols; h = ims[0].height; sh = Image.new('RGB', (cols * tw, rows * h), 'white')
for j, im in enumerate(ims): sh.paste(im, ((j % cols) * tw, (j // cols) * h))
fn = f'{d}/sheet_{a}_{b}.jpg'; sh.save(fn, quality=82); print(fn, len(ims))
