import sys,json
from PIL import Image
im=Image.open('p16170_P1.png').convert('L'); C=json.load(open('lines_auto.json'))['p16170_P1'][0]
rows=[]
for ln in map(int,sys.argv[1:]):
    c=C[ln-1]
    for x0,x1 in [(100,1600),(1500,2950)]:
        rows.append(im.crop((x0,c-70,x1,c+70)))
out=Image.new('L',(1500,140*len(rows)),255)
for j,r in enumerate(rows): out.paste(r,(0,140*j))
out=out.resize((int(1500*1.1),int(out.size[1]*1.1))); out.save('z1.png')
