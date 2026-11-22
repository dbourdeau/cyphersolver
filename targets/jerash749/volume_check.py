"""Compare the locations suggested by three summaries of the same CT volume."""
import sys
import cv2
import numpy as np

raw = np.memmap(sys.argv[1],dtype="<f4",mode="r",shape=(16,1733,3898))
# Area downsampling each plane first keeps memory modest.
v = np.stack([cv2.resize(p.T,(520,1170),interpolation=cv2.INTER_AREA) for p in raw])
peak = v.max(0)
keep = v > .5 * peak
fields = [v.argmax(0), keep.argmax(0), 15 - keep[::-1].argmax(0)]
bands = [(14,120),(106,188),(170,253),(236,327),(297,409),(390,471),
         (452,550),(515,613),(579,668),(640,725),(698,789),(775,859),
         (840,944),(917,1018),(987,1088),(1043,1129),(1095,1169)]
for box in [(367,411,67,39),(367,416,35,35),(400,411,32,38),
            (393,650,83,52),(270,1113,58,45)]:
    x,y,w,h = box
    runs = []
    for f in fields:
        a = f.astype("float32")
        a -= cv2.GaussianBlur(a,(0,0),5)
        probe = a[y:y+h,x:x+w]
        candidates = []
        for index,(top,end) in enumerate(bands,1):
            if top<=y<end or not (y+h<=top or y>=end):
                continue
            valid = cv2.integral((peak[top:end]>.01).astype("uint8"))
            n = valid[h:,w:]-valid[:-h,w:]-valid[h:,:-w]+valid[:-h,:-w]
            score = cv2.matchTemplate(a[top:end],probe,cv2.TM_CCOEFF_NORMED)
            score[n<.98*w*h] = -2
            iy,ix = np.unravel_index(score.argmax(),score.shape)
            candidates.append((round(float(score[iy,ix]),3),index,int(ix),int(iy+top)))
        runs.append(max(candidates))
    print(box,runs)
