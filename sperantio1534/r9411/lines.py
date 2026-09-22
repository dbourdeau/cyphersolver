import sys, numpy as np
from PIL import Image, ImageOps
f,tag,x0,x1=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
im=Image.open(f).convert('L'); a=np.asarray(im).astype(float)
band=a[:,x0:x1]; ink=(band<110).sum(1)
k=np.convolve(ink,np.ones(25)/25,'same')
# peaks
pk=[i for i in range(30,len(k)-30) if k[i]==k[i-30:i+30].max() and k[i]>0.25*k.max()]
print(tag,len(pk),pk)
