import sys,json
from PIL import Image
im=Image.open('p16170_P1.png').convert('L'); C=json.load(open('lines_auto.json'))['p16170_P1'][0]
ln=int(sys.argv[1]); x0=int(sys.argv[2]); x1=int(sys.argv[3]); dy=int(sys.argv[4]) if len(sys.argv)>4 else 0
c=C[ln-1]+dy
r=im.crop((x0,c-70,x1,c+70)); s=2 if x1-x0<900 else 1.5
r.resize((int((x1-x0)*s),int(140*s))).save('zc.png')
