import pickle,json,sys,numpy as np
from PIL import Image,ImageDraw
toks=sys.argv[1].split(','); out=sys.argv[2]
A=json.load(open('famC/hand/align.json'))
M={}
for p in set(a['page'] for a in A):
    for g in pickle.load(open(f'sr_{p}/glyphs2.pkl','rb')): M[(p,g['line'],g['k'])]=g['mask']
sel=[a for a in A if a['tok'] in toks]
C=12;S=64
img=Image.new('L',(C*S,((len(sel)+C-1)//C)*(S+12)),255);d=ImageDraw.Draw(img)
for i,a in enumerate(sel):
    m=M[(a['page'],a['line'],a['k'])];m=(255-(np.array(m)>0)*255).astype('uint8');im=Image.fromarray(m);im.thumbnail((S-4,S-4))
    x,y=(i%C)*S,(i//C)*(S+12);img.paste(im,(x+2,y+12));d.text((x+2,y),f'{i}{a["tok"]}',fill=0)
img.save(out);json.dump(sel,open(out+'.json','w'));print(len(sel))
