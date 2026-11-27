"""Pick the cipher run in every line: the longest stretch of signs in which >= 75% have nearest-neighbour
distance < 4.0 (to the 34r-35v training shapes), trimmed to start and end on such a sign; kept if >= 4 signs.
Writes work/runs.pkl {(page,line): (first, last+1)} and annotated page images in work/ann/."""
import pickle, numpy as np, cv2
out,probs=pickle.load(open('work/machine.pkl','rb')); dist=pickle.load(open('work/dist.pkl','rb'))
P=pickle.load(open('work/pages.pkl','rb'))
runs={}
for p,j,y,c,d,labs in out:
    dd=np.array(dist[(p,j)]); g=dd<4.0; n=len(g)
    best=None
    for a in range(n):
        if not g[a]: continue
        good=0
        for b in range(a,n):
            good+=g[b]
            if g[b] and good/(b-a+1)>=0.75 and good>=4:
                if best is None or good>best[0]: best=(good,a,b+1)
    if best and best[0]>=4: runs[(p,j)]=(best[1],best[2])
pickle.dump(runs,open('work/runs.pkl','wb'))
pages=sorted({p for p,_ in runs})
for p in pages:
    g=cv2.imread(f'scans/c{p}.jpg')
    for j,l in enumerate(P[p]):
        ss=sorted(l['signs'],key=lambda s:s['x0'])
        cv2.putText(g,str(j),(5,l['y']+10),cv2.FONT_HERSHEY_SIMPLEX,1.1,(0,0,255),3)
        if (p,j) in runs:
            a,b=runs[(p,j)]
            cv2.line(g,(ss[a]['x0'],l['y']+22),(ss[b-1]['x1'],l['y']+22),(0,170,0),4)
    cv2.imwrite(f'work/ann/{p}.jpg',cv2.resize(g,None,fx=0.55,fy=0.55))
print(len(runs))
