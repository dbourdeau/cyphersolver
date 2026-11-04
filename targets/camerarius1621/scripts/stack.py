"""stack.py OUT IMG... : stack images vertically"""
import sys
from PIL import Image
ims=[Image.open(f) for f in sys.argv[2:]]; W=max(i.width for i in ims)
S=Image.new('L',(W,sum(i.height for i in ims)),255); y=0
for i in ims: S.paste(i,(0,y)); y+=i.height
S.save(sys.argv[1],quality=90)
