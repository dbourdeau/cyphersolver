import pickle, numpy as np, cv2, sys
from PIL import Image, ImageDraw, ImageFont
S=pickle.load(open(sys.argv[3] if len(sys.argv)>3 else 'work/signs_c.pkl','rb'))
p=sys.argv[1]; per=int(sys.argv[2]); scale=1.6
from collections import defaultdict
L=defaultdict(list)
for s in S:
    if s['p']==p: L[s['l']].append(s)
img=cv2.imread(f'scans/c{p.rstrip("b")}.jpg',0)
font=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',15)
keys=sorted(L)
for b in range(0,len(keys),per):
    rows=[]
    for l in keys[b:b+per]:
        ss=sorted(L[l],key=lambda s:s['x0'])
        ss=[s for s in ss if s['c']!='|' or s['y1']-s['y0']<60]
        y0=int(np.median([s['y0'] for s in ss]))-8; y1=int(np.median([s['y1'] for s in ss]))+14
        x0=min(s['x0'] for s in ss)-6; x1=max(s['x1'] for s in ss)+6
        c=img[y0:y1,x0:x1]
        lo,hi=np.percentile(c,1),np.percentile(c,99); c=np.clip((c-lo)*255/(hi-lo),0,255).astype(np.uint8)
        t=Image.fromarray(c).resize((int(c.shape[1]*scale),int(c.shape[0]*scale)),Image.LANCZOS).convert('RGB')
        R=Image.new('RGB',(1640,t.height+46),'white'); R.paste(t,(40,0))
        d=ImageDraw.Draw(R); d.text((0,10),f'{l+1}',fill='blue',font=font)
        for i,s in enumerate(ss):
            xc=40+(s['x0']+s['x1'])/2*scale-x0*scale
            yy=t.height+(0 if i%2==0 else 20)
            d.line([(40+(s['x0']-x0)*scale,t.height-2),(40+(s['x1']-x0)*scale,t.height-2)],fill='green')
            col='red' if s['pb']<0.8 else 'black'
            d.text((xc-8,yy),s['c'],fill=col,font=font)
        rows.append(R)
    H=sum(r.height for r in rows)
    out=Image.new('RGB',(1640,H),'white'); y=0
    for r in rows: out.paste(r,(0,y)); y+=r.height
    out.save(f'work/strip_{p}_{b//per}.png'); print(out.size)
