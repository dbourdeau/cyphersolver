import sys
from PIL import Image
base=sys.argv[1]
def run(img,s,items):
    im=Image.open(base+'/scans/'+img)
    for name,box in items:
        b=[int(v*s) for v in box]
        r=im.crop(b); r=r.resize((r.width*2,r.height*2)); r.save(base+'/work/crops/'+name)
run('MSC_VI_00052_085.jpg',2550/2184,[('85_a.png',(1180,760,2150,880)),('85_b.png',(1180,830,2150,980)),('85_c.png',(1180,880,2150,1030)),('85_d.png',(1180,1000,2150,1190)),('85_e.png',(1180,1150,2150,1220))])
run('MSC_VI_00052_086.jpg',2550/2184,[('86_a.png',(150,800,1060,930)),('86_b.png',(150,1050,1060,1210))])
