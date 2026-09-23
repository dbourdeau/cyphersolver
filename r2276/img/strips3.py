from PIL import Image, ImageDraw
import glob,os
r=[512, 613, 721, 827, 937, 1039, 1140, 1242, 1348, 1449, 1562, 1682, 1790]
g=[506, 604, 707, 805, 908, 1010, 1114, 1219, 1321, 1417, 1526, 1643, 1760]
b=[479, 567, 671, 774, 864, 983, 1088, 1189, 1290, 1394, 1492, 1604, 1720]
im=Image.open('p3rot.png').convert('RGB'); H=170
for f in glob.glob('strips/p3_*'): os.remove(f)
for gi in range(0,13,3):
    idx=range(gi,min(gi+3,13))
    A=Image.new('RGB',(1600,H*len(idx)),'white'); B=Image.new('RGB',(1700,H*len(idx)),'white')
    da,db=ImageDraw.Draw(A),ImageDraw.Draw(B)
    for j,i in enumerate(idx):
        A.paste(im.crop((100,r[i]-85,1100,r[i]+85)),(50,j*H)); A.paste(im.crop((1100,g[i]-85,1650,g[i]+85)),(1050,j*H))
        B.paste(im.crop((1550,g[i]-85,2000,g[i]+85)),(50,j*H)); B.paste(im.crop((2000,b[i]-85,3180,b[i]+85)),(500,j*H))
        for d in (da,db): d.text((5,j*H+75),str(i+1),fill='black'); d.line([(0,j*H),(1700,j*H)],fill='black',width=2)
    da.line([(1500,0),(1500,A.size[1])],fill='red',width=2); db.line([(0+50+50,0),(100,B.size[1])],fill='red',width=2)
    A.save(f'strips/p3_L{gi+1:02d}_a.png'); B.save(f'strips/p3_L{gi+1:02d}_b.png')
