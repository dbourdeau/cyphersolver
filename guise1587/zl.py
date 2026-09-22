import sys
from PIL import Image
im=Image.open('img/f119_cipher.jpg')
rows={21:(2250,2293,2299),22:(2358,2401,2398),24:(2554,2599,2601),30:(3190,3212,3203),31:(3277,3333,3308),36:(3822,3852,3827),37:(3938,3964,3941)}
k=int(sys.argv[1]); cs=rows[k]
parts=[(0,1450),(1350,2800),(2700,4135)]
o=Image.new('RGB',(2175,3*150),'white')
for p,((x0,x1),c) in enumerate(zip(parts,cs)):
    o.paste(im.crop((x0,c-55,x0+1450,c+45)).resize((2175,150)),(0,p*150))
o.save(f'img/w{k}.png')
