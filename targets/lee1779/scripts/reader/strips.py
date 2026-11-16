"""strips.py <pages_dir> <outprefix> <per_image> <spec>...  spec = PAGEcol:l1/l2/...  e.g. 243a:17/30
Makes labelled column strips (headword part of the column, full height) with the detector's line index
printed beside each detected text line (index 0 = first detected line, normally the running head)."""
import sys,glob,os
sys.path.insert(0,os.path.dirname(__file__))
from imglines import analyse
from PIL import Image,ImageDraw,ImageFont
pdir,outp,per=sys.argv[1],sys.argv[2],int(sys.argv[3]); specs=sys.argv[4:]
font=ImageFont.load_default(size=22); bfont=ImageFont.load_default(size=26)
tiles=[]
for sp in specs:
    pc,ls=sp.split(':'); p=int(pc[:-1]); c=pc[-1]; targets=[int(x) for x in ls.split('/')] if ls else []
    fl=glob.glob(os.path.join(pdir,f"p{p:03d}_*.jpg"))
    if not fl: continue
    r=analyse(fl[0]); sc=r['scale']
    im=Image.open(fl[0]).convert('L'); small=im.resize((1600,int(im.size[1]*sc)))
    dv=r['divider']; bx0,bx1=r['cols']['b']['x']; colw=bx1-dv
    if c=='a': x0=max(0,int(dv-colw*1.08)); w=int(colw*0.75)
    else: x0=dv-15; w=int(colw*0.62)
    y0,y1=r['page'][1],r['page'][3]
    cr=small.crop((x0,y0,x0+w,y1)).convert('RGB')
    lab=Image.new('RGB',(cr.size[0]+70,cr.size[1]+40),'white'); lab.paste(cr,(70,40)); d=ImageDraw.Draw(lab)
    d.text((4,4),f"p{p}{c} want {ls}",fill=(0,120,0),font=bfont)
    for k,(s,e) in enumerate(r['cols']['b']['lines']):
        yy=(s+e)//2-y0+40
        d.text((2,yy-11),str(k),fill=(220,0,0) if k in targets else (0,0,200),font=font)
    tiles.append(lab)
for i in range(0,len(tiles),per):
    grp=tiles[i:i+per]; W=sum(t.size[0]+10 for t in grp); H=max(t.size[1] for t in grp)
    big=Image.new('RGB',(W,H),'gray'); x=0
    for t in grp: big.paste(t,(x,0)); x+=t.size[0]+10
    big.save(f"{outp}_{i//per:02d}.jpg",quality=82)
    print(f"{outp}_{i//per:02d}.jpg",big.size)
