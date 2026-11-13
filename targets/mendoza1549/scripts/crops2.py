"""Line crops of 44r at full resolution, line centres per band from ink projection (measured 12 Nov)."""
import sys
from PIL import Image
B1=[622,892,1119,1338,1520,1732,1918,2125,2344,2554,2744,2960,3180,3386,3607,3831,4037]
B2=[620,862,1086,1301,1495,1704,1883,2081,2285,2503,2693,2930,3123,3365,3548,3750,3971]
B3=[605,826,1023,1224,1428,1626,1830,2011,2223,2404,2622,2807,3022,3246,3474,3692,3929]
B4=[605,812,1009,1214,1395,1590,1798,1987,2187,2381,2581,2778,2998,3216,3447,3665,3880]
bands=[(380,1700,B1),(1640,2960,B2),(2900,4220,B3),(4160,5300,B4)]
im=Image.open(sys.argv[1]); prefix=sys.argv[2]; H=int(sys.argv[3]) if len(sys.argv)>3 else 250
for i in range(17):
    out=Image.new('RGB',(1320,H*4),'white')
    for j,(a,b,Y) in enumerate(bands):
        y=Y[i]; out.paste(im.crop((a,y-H//2-20,b,y+H//2-20)),(0,H*j))
    out.save(f'{prefix}{i+1:02d}.jpg',quality=90)
