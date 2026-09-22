import sys,numpy as np
from PIL import Image
c=sys.argv[1]; x0,x1=int(sys.argv[2]),int(sys.argv[3])
im=Image.open(f'full/c{c}.jpg').convert('L'); a=np.array(im)[:,x0:x1]
d=(a<110).sum(1); d=np.convolve(d,np.ones(40)/40,'same')
# find peaks
peaks=[];thr=d.max()*0.25
i=0
while i<len(d):
    if d[i]>thr:
        j=i
        while j<len(d) and d[j]>thr: j+=1
        peaks.append((i+j)//2); i=j
    else: i+=1
print(len(peaks),peaks)
