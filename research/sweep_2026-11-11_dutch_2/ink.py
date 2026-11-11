"""ink measure per screenshot (dark-pixel share in the central area), to skip blank openings: ink.py <dir> first last"""
import sys, os
from PIL import Image
d=sys.argv[1]
for i in range(int(sys.argv[2]), int(sys.argv[3])+1):
    f=f'{d}/p{i:04d}.png'
    if not os.path.exists(f): print(i,'MISSING'); continue
    im=Image.open(f).convert('L'); w,h=im.size; im=im.crop((int(w*.05),int(h*.06),int(w*.80),int(h*.97))).resize((400,500))
    px=im.load(); n=sum(1 for x in range(400) for y in range(500) if px[x,y]<110)
    print(i, round(n/2000,2))
