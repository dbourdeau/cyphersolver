# Segment pages into signs; save per-sign crops as npz plus line/x index. 
import sys, json, numpy as np, cv2, pickle
from scipy import ndimage as ni
sys.path.insert(0,'work')
from seg import binarize, lines_of
BOX=json.load(open('work/boxes.json'))
def comps(b):
    lab,n=ni.label(b,structure=np.ones((3,3)))
    objs=ni.find_objects(lab)
    out=[]
    for i,s in enumerate(objs):
        h=s[0].stop-s[0].start; w=s[1].stop-s[1].start
        a=(lab[s]==i+1).sum()
        if a<4: continue
        out.append(dict(y0=s[0].start,y1=s[0].stop,x0=s[1].start,x1=s[1].stop,a=int(a),i=i+1))
    return lab,out
def run(p):
    x0,y0,x1,y1=BOX[p]
    g=cv2.imread(f'scans/c{p.rstrip("b")}.jpg',0)[y0:y1,x0:x1]
    b=binarize(g)
    pk=lines_of(b)
    lab,cs=comps(b)
    pk=np.array(pk)
    lines={i:[] for i in range(len(pk))}
    for c in cs:
        # centre of mass y
        ys,xs=np.nonzero(lab[c['y0']:c['y1'],c['x0']:c['x1']]==c['i'])
        cy=ys.mean()+c['y0']
        l=int(np.argmin(abs(pk-cy)))
        lines[l].append(c)
    signs=[]
    for l,cl in lines.items():
        cl.sort(key=lambda c:c['x0'])
        groups=[]
        for c in cl:
            placed=False
            for g2 in groups[-3:][::-1]:
                gx0=min(k['x0'] for k in g2); gx1=max(k['x1'] for k in g2)
                ov=min(gx1,c['x1'])-max(gx0,c['x0'])
                wmin=min(gx1-gx0,c['x1']-c['x0'])
                small=c['a']<40
                if ov>0.5*wmin or (small and ov>0):
                    g2.append(c); placed=True; break
            if not placed: groups.append([c])
        # merge a tall stroke with a following dot column (the sign I:)
        G=[];
        for g2 in groups:
            if G:
                pg=G[-1]
                px1=max(k['x1'] for k in pg); px0=min(k['x0'] for k in pg)
                py0=min(k['y0'] for k in pg); py1=max(k['y1'] for k in pg)
                gx0=min(k['x0'] for k in g2); gx1=max(k['x1'] for k in g2)
                gy0=min(k['y0'] for k in g2); gy1=max(k['y1'] for k in g2)
                if gx1-gx0<=9 and gy1-gy0<=30 and px1-px0<=12 and py1-py0>=20 and gx0-px1<=9:
                    pg.extend(g2); continue
            G.append(g2)
        groups=G
        for g2 in groups:
            a=sum(k['a'] for k in g2)
            if a<25: continue
            gx0=min(k['x0'] for k in g2); gx1=max(k['x1'] for k in g2)
            gy0=min(k['y0'] for k in g2); gy1=max(k['y1'] for k in g2)
            m=np.isin(lab[gy0:gy1,gx0:gx1],[k['i'] for k in g2]).astype(np.uint8)
            signs.append(dict(p=p,l=l,x0=gx0+x0,x1=gx1+x0,y0=gy0+y0,y1=gy1+y0,m=m))
    return signs,pk
if __name__=='__main__':
    allsigns=[]
    for p in sys.argv[1:]:
        s,pk=run(p); print(p,len(pk),'lines',len(s),'signs',len(s)/max(1,len(pk)))
        allsigns+=s
    pickle.dump(allsigns,open('work/signs.pkl','wb'))
