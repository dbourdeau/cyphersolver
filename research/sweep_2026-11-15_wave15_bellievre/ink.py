# ink.py: fraction of ink pixels on a canvas (local-background subtraction), used to leave blank and address-only pages off the sheets.
import numpy as np
from PIL import Image, ImageFilter
def ink(fn):
    im = Image.open(fn).convert('L'); im = im.resize((400, int(im.height * 400 / im.width)))
    A = np.asarray(im, dtype=np.int16); bg = np.asarray(im.filter(ImageFilter.BoxBlur(12)), dtype=np.int16)
    h, w = A.shape; m = (bg - A > 22)[int(h * .04):int(h * .96), int(w * .05):int(w * .95)]
    rows = m.mean(axis=1)
    return float(m.mean()), int((rows > 0.04).sum())   # ink fraction, number of pixel rows carrying writing
if __name__ == '__main__':
    import sys
    for f in sys.argv[1:]: print(f[-9:], ink(f))
