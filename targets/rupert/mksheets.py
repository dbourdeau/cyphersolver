"""mksheets.py rec... : contact sheets (2 content pages each) of a record's previews -> img/v/S<rec>_<n>.jpg"""
import sys, glob, os, subprocess
import numpy as np
from PIL import Image
def ink(p):
    im = np.asarray(Image.open(p).convert('L'), dtype=float); h, w = im.shape
    c = im[int(h*.1):int(h*.9), int(w*.1):int(w*.9)]; return (c < np.median(c)-40).mean()*1000
for r in sys.argv[1:]:
    ps = sorted(glob.glob('img/v/R%s_I*_P*.jpg' % r), key=lambda p: int(p.rsplit('_P', 1)[1][:-4]))
    ps = [p for p in ps if ink(p) >= 8]
    for k in range(0, len(ps), 2):
        out = 'img/v/S%s_%d.jpg' % (r, k//2+1)
        subprocess.run([sys.executable, 'sheet.py', out] + ps[k:k+2])
        print(out, [os.path.basename(p) for p in ps[k:k+2]])
