"""crop_img.py <pages_dir> <out.jpg> <group>... : crops lines n-3..n+3 using image line detection.
Header handling: the first detected line in each column is the running head if it sits above the first line of the other column by < half a line, i.e. we drop lines whose y is above the top of the shared head row. We label rows as detected; the caller checks the head row visually."""
import sys,glob,os
sys.path.insert(0,os.path.dirname(__file__))
from imglines import analyse
from PIL import Image,ImageDraw,ImageFont
pdir,out=sys.argv[1:3]; groups=sys.argv[3:]
font=ImageFont.load_default(size=26)
tiles=[]
for g in groups:
    p=int(g[:3]); c=g[3]; n=int(g[4:6])
    fl=glob.glob(os.path.join(pdir,f"p{p:03d}_*.jpg"))
    if not fl: continue
    r=analyse(fl[0]); sc=r['scale']
    im=Image.open(fl[0]).convert('L'); small=im.resize((1600,int(im.size[1]*sc)))
    L=r['cols'][c]['lines']
    # running head = line 0: the first line of column a/b (head spans both); we treat first detected line as head
    body=L[1:]
    lo=max(0,n-4); hi=min(len(body),n+3)
    if lo>=len(body): continue
    ya=body[lo][0]-4; yb=body[hi-1][1]+4
    x0,x1=r['cols'][c]['x']
    cr=small.crop((x0-10,ya,x1+10,yb)).convert('RGB')
    lab=Image.new('RGB',(cr.size[0]+190,cr.size[1]),'white'); lab.paste(cr,(190,0)); d=ImageDraw.Draw(lab)
    for k in range(lo,hi):
        yy=(body[k][0]+body[k][1])//2-ya
        d.text((4,yy-13),(f"{g}>" if k+1==n else "")+f"L{k+1}",fill=(220,0,0) if k+1==n else (0,0,200),font=font)
    d.text((4,2),f"{len(body)} lines",fill=(0,140,0),font=font)
    tiles.append(lab)
w=max(t.size[0] for t in tiles); h=sum(t.size[1]+8 for t in tiles)
big=Image.new('RGB',(w,h),'gray'); y=0
for t in tiles: big.paste(t,(0,y)); y+=t.size[1]+8
big.save(out,quality=80)
