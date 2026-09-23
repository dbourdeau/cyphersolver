import sys
from PIL import Image, ImageOps, ImageFilter
src,tag=sys.argv[1],sys.argv[2]; ys=list(map(int,sys.argv[3].split(',')))
im=Image.open(src).convert('L'); w,h=im.size
for n,y in enumerate(ys):
    parts=[]
    for a,b in [(60,w//2+40),(w//2-40,w-5)]:
        c=im.crop((a,y-17,b,y+15)); c=c.resize((c.width*4,c.height*4),Image.BICUBIC).filter(ImageFilter.UnsharpMask(3,150,2)); parts.append(ImageOps.autocontrast(c,cutoff=2))
    W=max(p.width for p in parts); C=Image.new('L',(W,sum(p.height for p in parts)+8),255); yy=0
    for p in parts: C.paste(p,(0,yy)); yy+=p.height+8
    C.save(f'sx/{tag}{n+1:02d}.png')
