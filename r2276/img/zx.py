import sys,json
from PIL import Image
# zx.py page line x0 x1 [scale]  -> zx.png
p,ln,x0,x1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
sc=float(sys.argv[5]) if len(sys.argv)>5 else 2
if p=='1':
    im=Image.open('p16170_P1.png').convert('L'); c=json.load(open('lines_auto.json'))['p16170_P1'][0][ln-1]; y=c
else:
    im=Image.open('p3rot.png').convert('L')
    r=[512,613,721,827,937,1039,1140,1242,1348,1449,1562,1682,1790][ln-1]
    g=[506,604,707,805,908,1010,1114,1219,1321,1417,1526,1643,1760][ln-1]
    b=[479,567,671,774,864,983,1088,1189,1290,1394,1492,1604,1720][ln-1]
    xm=(x0+x1)/2
    y=int(r if xm<1100 else (g if xm<2000 else b))
out=im.crop((x0,y-70,x1,y+70))
out=out.resize((int(out.size[0]*sc),int(out.size[1]*sc)))
out.save('zx.png')
print(im.size)
