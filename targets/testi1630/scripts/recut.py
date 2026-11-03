# recut.py : third pass strips. Cut each cipher line to the true edge of the paper at full resolution, with a pixel ruler, for a sign-first read.
# c. 7r from the block and its line list; cc. 73v-74r from the F blocks, to the width of the block, not to the old limit x=4993.
import json,sys
from PIL import Image,ImageDraw,ImageFont
Image.MAX_IMAGE_PIXELS=None
F=ImageFont.truetype('arial.ttf',20)
W=1650;SRC=1700;H=300;PER=6;SC=W/SRC
def sheets(name,jobs):
    rows=[]
    for lab,fn,cy,x0,x1 in jobs:
        im=Image.open(fn).convert('RGB'); n=0; x=x0
        while x<x1:
            e=min(x+SRC,x1); n+=1
            c=im.crop((x,max(0,cy-H//2),e,min(im.height,cy+H//2))); c=c.resize((int(c.width*SC),int(c.height*SC)),Image.LANCZOS)
            rows.append((f'{lab} part {n} x={x}-{e}',c))
            if e>=x1: break
            x=e-120
    s=0;k=0;out=[]
    while s<len(rows):
        ch=rows[s:s+PER]; S=Image.new('RGB',(W+8,sum(c.height+30 for _,c in ch)+6),'white'); d=ImageDraw.Draw(S); y=2
        for t,c in ch:
            d.text((6,y),t,fill=(0,0,200),font=F); S.paste(c,(4,y+24)); y+=c.height+30
        k+=1; fn=f'scans/work/{name}_{k:02d}.jpg'; S.save(fn,quality=92); out.append(fn); s+=PER
    print(name,len(rows),out)
if __name__=='__main__':
    ys=json.load(open('scans/work/c7r_lines.json'))[2:17]
    sheets('r7',[(f'c7r l{i+3}','scans/work/c7r_block.jpg',y,100,5390) for i,y in enumerate(ys)])
    B='scans/F/c74r_b.jpg';C='scans/F/c74r_c.jpg'
    J=[('c74r row8',B,946,150,5184),('c74r row9',B,1182,150,5184)]
    for n,(a,e) in zip(range(10,16),[(38,338),(294,594),(547,847),(789,1089),(1025,1325),(1241,1541)]):
        J.append((f'c74r row{n}',C,(a+e)//2,150,5184))
    sheets('r74',J)
    D='scans/F/c73v_d.jpg';K='scans/F/c73v_c.jpg'
    J=[('c73v row4',K,861,3700,5245)]
    for n,(a,e) in zip(range(5,11),[(0,264),(232,532),(521,821),(811,1111),(1101,1401),(1410,1710)]):
        J.append((f'c73v row{n}',D,(a+e)//2,3700,5245))
    sheets('r73',J)
