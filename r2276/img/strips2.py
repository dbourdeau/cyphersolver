from PIL import Image, ImageDraw
import json,glob,os
T=json.load(open('p2_thirds.json'))
r,g,b=T['900'][:40],T['1650'],T['2450'][:40]
im=Image.open('p16171_P2.png').convert('RGB')
H=170
for f in glob.glob('strips/p2_*'): os.remove(f)
for gi in range(0,40,3):
    idx=range(gi,min(gi+3,40))
    A=Image.new('RGB',(1700,H*len(idx)),'white'); B=Image.new('RGB',(1720,H*len(idx)),'white')
    da,db=ImageDraw.Draw(A),ImageDraw.Draw(B)
    for j,i in enumerate(idx):
        A.paste(im.crop((100,r[i]-85,1750,r[i]+85)),(50,j*H))
        B.paste(im.crop((1600,g[i]-85,2450,g[i]+85)),(50,j*H))
        B.paste(im.crop((2450,b[i]-85,3280,b[i]+85)),(900,j*H))
        for d in (da,db): d.text((5,j*H+75),str(i+1),fill='black'); d.line([(0,j*H),(1720,j*H)],fill='black',width=2)
    da.line([(1600,0),(1600,A.size[1])],fill='red',width=2); db.line([(100,0),(100,B.size[1])],fill='red',width=2)
    db.line([(900,0),(900,B.size[1])],fill=(0,200,0),width=1)
    A.save(f'strips/p2_L{gi+1:02d}_a.png'); B.save(f'strips/p2_L{gi+1:02d}_b.png')
