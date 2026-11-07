import cv2, numpy as np, json
im=cv2.imread('png/R5460_x.png',0)
h,w=im.shape
# crop to text block: lines 1-7 cipher (line 8 clear), x range
x0,x1=int(w*.05),int(w*.97)
ys=[285+108*k for k in range(7)]
bg=cv2.GaussianBlur(im,(0,0),45)
norm=cv2.divide(im,bg,scale=255)
_,bw=cv2.threshold(norm,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
bw=cv2.morphologyEx(bw,cv2.MORPH_OPEN,np.ones((2,2),np.uint8))
out=[]
dbg=cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)
for li,y in enumerate(ys):
    band=bw[y-58:y+58,x0:x1]
    n,lab,st,cen=cv2.connectedComponentsWithStats(band,8)
    comps=[(st[i,0],st[i,1],st[i,2],st[i,3],st[i,4],i) for i in range(1,n) if st[i,4]>25]
    comps.sort()
    # merge components overlapping horizontally (gap<6px) into glyph boxes
    glyphs=[]
    for c in comps:
        x,yy,ww,hh,a,i=c
        if glyphs and x<=glyphs[-1]['x1']+7:
            g=glyphs[-1]; g['x1']=max(g['x1'],x+ww); g['y0']=min(g['y0'],yy); g['y1']=max(g['y1'],yy+hh); g['ids'].append(i)
        else: glyphs.append(dict(x0=x,x1=x+ww,y0=yy,y1=yy+hh,ids=[i]))
    for g in glyphs:
        out.append(dict(line=li+1,x0=int(g['x0']+x0),x1=int(g['x1']+x0),y0=int(g['y0']+y-58),y1=int(g['y1']+y-58)))
        cv2.rectangle(dbg,(g['x0']+x0,g['y0']+y-58),(g['x1']+x0,g['y1']+y-58),(0,0,255),2)
    print(li+1,len(glyphs))
cv2.imwrite('png/R5460_seg.png',dbg)
json.dump(out,open('t5460/glyphs.json','w'))
