import sys
import numpy as np
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
src,x0,x1,y0,y1=sys.argv[1],*map(int,sys.argv[2:6])
a=np.asarray(Image.open(src).crop((x0,y0,x1,y1)),dtype=float)
ink=(a<110).sum(1)
k=15
s=np.convolve(ink,np.ones(k)/k,'same')
# local maxima
pk=[i for i in range(20,len(s)-20) if s[i]==s[i-20:i+21].max() and s[i]>s.max()*0.25]
print([y0+p for p in pk])
