import sys,json
from PIL import Image
p,ln=sys.argv[1],int(sys.argv[2])
if p=='1':
    im=Image.open('p16170_P1.png').convert('L'); c=json.load(open('lines_auto.json'))['p16170_P1'][0][ln-1]
    parts=[(100,c,1100,c),(1000,c,2000,c),(1900,c,2950,c)]
elif p=='2':
    im=Image.open('p16171_P2.png').convert('L'); T=json.load(open('p2_thirds.json'))
    r,g,b=T['900'][ln-1],T['1650'][ln-1],T['2450'][ln-1]
    parts=[(100,r,1100,r),(1000,(r+g)//2,1800,g),(1700,g,2500,b),(2400,b,3300,b)]
else:
    im=Image.open('p3rot.png').convert('L')
    r=[512,613,721,827,937,1039,1140,1242,1348,1449,1562,1682,1790][ln-1]
    g=[506,604,707,805,908,1010,1114,1219,1321,1417,1526,1643,1760][ln-1]
    b=[479,567,671,774,864,983,1088,1189,1290,1394,1492,1604,1720][ln-1]
    parts=[(100,r,1100,r),(1000,g,2000,b),(1950,b,3200,b)]
W=0;ims=[]
for x0,y0,x1,y1 in parts:
    y=(y0+y1)//2; ims.append(im.crop((x0,y-75,x1,y+75)))
out=Image.new('L',(max(i.size[0] for i in ims),150*len(ims)),255)
for j,i in enumerate(ims): out.paste(i,(0,150*j))
out=out.resize((int(out.size[0]*1.5),int(out.size[1]*1.5)))
out.save(sys.argv[3])
