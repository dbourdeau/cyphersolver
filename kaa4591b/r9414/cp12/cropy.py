import sys
from PIL import Image, ImageOps, ImageDraw
# page x0 x1 rot first ys(comma, band0) offb offc H
p=int(sys.argv[1]); x0,x1=int(sys.argv[2]),int(sys.argv[3]); rot=sys.argv[4]=='r'; first=int(sys.argv[5])
ys=list(map(int,sys.argv[6].split(','))); ob,oc=int(sys.argv[7]),int(sys.argv[8]); H=int(sys.argv[9])
im=Image.open(f'../img/IMG_R9414_I44519_P{p}.jpg').convert('L')
if rot: im=im.rotate(180)
w=(x1-x0)//3; S=3
for k,y in enumerate(ys):
    ln=first+k; strips=[]
    for b,off in enumerate([0,ob,oc]):
        c=y+off; u=x0+b*w-(40 if b else 0); v=x0+(b+1)*w+40
        s=ImageOps.autocontrast(im.crop((u,c-H,v,c+H-15)),cutoff=1).convert('RGB')
        s=s.resize((s.width*S, s.height*S))
        dr=ImageDraw.Draw(s); dr.rectangle((0,0,70,24),fill='white'); dr.text((4,4),f'{ln:02d}{"abc"[b]}',fill='red')
        yc=H*S; dr.rectangle((0,yc-5,25,yc+5),fill='red')
        strips.append(s)
    W=max(s.width for s in strips); out=Image.new('RGB',(W,sum(s.height for s in strips)+10),'white'); yy=0
    for s in strips: out.paste(s,(0,yy)); yy+=s.height+5
    out.save(f'cp12/P{p}_{ln:02d}.png')
