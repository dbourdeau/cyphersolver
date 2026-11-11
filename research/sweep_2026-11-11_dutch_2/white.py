"""list screenshots with unloaded (pure white) viewer tiles: white.py <dir> [--rm]  (a fully white block of about 150x150 px inside the image area)"""
import sys, glob, os
import numpy as np
from PIL import Image
bad=[]
for f in sorted(glob.glob(sys.argv[1]+'/p*.png')):
    a=np.asarray(Image.open(f).convert('L').resize((250,340)))[30:325,12:238]==255
    c=a.cumsum(0).cumsum(1); k=30; hit=False
    s=c[k:,k:]-c[:-k,k:]-c[k:,:-k]+c[:-k,:-k]
    if (s==k*k).any(): bad.append(f)
print(len(bad), ' '.join(os.path.basename(b)[1:5] for b in bad))
if '--rm' in sys.argv:
    for b in bad: os.remove(b)
