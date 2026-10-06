"""crop.py page line [a b]: crop line (1-based) of page from the DECODE PNG, x fraction a..b, to scratch/c.png"""
import sys, json
from PIL import Image
S='C:/Users/dbour/AppData/Local/Temp/claude/C--Users-dbour-cypher/6161e4a6-ee3b-46d9-a1bc-b3f7895b5b9b/scratchpad/'
p, ln = sys.argv[1], int(sys.argv[2]); a=float(sys.argv[3]) if len(sys.argv)>3 else 0; b=float(sys.argv[4]) if len(sys.argv)>4 else 1
f={'1':'IMG_R2276_I16170_P1.png','2':'IMG_R2276_I16171_P2.png','3':'p3_upright.png'}[p]
im=Image.open('sources/'+f).convert('L'); y=json.load(open(f'work/p{p}_peaks.json'))[ln-1]
W=im.size[0]; out=sys.argv[5] if len(sys.argv)>5 else 'c'
im.crop((int(a*W),y-75,int(b*W),y+65)).save(S+out+'.png')
