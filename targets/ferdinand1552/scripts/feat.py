import numpy as np, cv2
def feat(m,n=24):
    h,w=m.shape; s=max(h,w)
    c=np.zeros((s,s),np.float32); y=(s-h)//2; x=(s-w)//2
    c[y:y+h,x:x+w]=m
    f=cv2.GaussianBlur(cv2.resize(c,(n,n),interpolation=cv2.INTER_AREA),(0,0),1.0)
    return np.concatenate([f.ravel(),[h/40,w/40]])
