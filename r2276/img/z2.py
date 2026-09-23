import sys,json
from PIL import Image
im=Image.open('p16170_P1.png').convert('L'); C=json.load(open('lines_auto.json'))['p16170_P1'][0]
ln=int(sys.argv[1]); c=C[ln-1]
rows=[im.crop((x0,c-60,x0+1000,c+60)) for x0 in (100,1030,1960)]
out=Image.new('L',(1000,120*3),255)
for j,r in enumerate(rows): out.paste(r,(0,120*j))
out.resize((1600,576)).save('z2.png')
