import sys
from PIL import Image
tag=sys.argv[1]; ns=sys.argv[2].split(',')
ims=[]
for n in ns:
    for s in 'ab': ims.append(Image.open(f'lines/{tag}{int(n):02d}{s}.png'))
W=max(i.width for i in ims); H=sum(i.height for i in ims)+6*len(ims)
C=Image.new('L',(W,H),255); y=0
for i in ims: C.paste(i,(0,y)); y+=i.height+6
C.save(f'lines/S{tag}_{ns[0]}.png')
