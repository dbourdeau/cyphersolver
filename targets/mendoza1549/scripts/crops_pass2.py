"""Pass-2 crops of 44r: five bands per line (other cut points than pass 1), upscaled 1.2x."""
import numpy as np
from PIL import Image
B1=[622,892,1119,1338,1520,1732,1918,2125,2344,2554,2744,2960,3180,3386,3607,3831,4037]
B4=[605,812,1009,1214,1395,1590,1798,1987,2187,2381,2581,2778,2998,3216,3447,3665,3880]
xc1, xc4 = 1040, 4730
im=Image.open('scans/44r_full_top.jpg')
bands=[(380,1450),(1350,2420),(2320,3390),(3290,4360),(4260,5330)]
H=220
for i in range(17):
    out=Image.new('RGB',(int(1070*1.2),int(H*1.2)*5),'white')
    for j,(a,b) in enumerate(bands):
        xm=(a+b)/2; y=B1[i]+(B4[i]-B1[i])*(xm-xc1)/(xc4-xc1)
        c=im.crop((a,int(y-H/2-20),b,int(y+H/2-20))).resize((int(1070*1.2),int(H*1.2)))
        out.paste(c,(0,int(H*1.2)*j))
    out.save(f'work/crops/B{i+1:02d}.jpg',quality=90)
