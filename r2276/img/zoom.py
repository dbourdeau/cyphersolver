import sys,json
from PIL import Image
L=json.load(open('lines_auto.json'))
pg={'1':('p16170_P1',0),'2':('p16171_P2',0),'3':('p16172_P3',180)}
p,ln,x0,x1=sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
sc=float(sys.argv[5]) if len(sys.argv)>5 else 2
n,rot=pg[p]; im=Image.open(n+'.png').convert('L')
if rot: im=im.rotate(rot)
c=(L['p2'] if p=='2' else L[n][0])[ln-1]
im.crop((x0,c-70,x1,c+70)).resize((int((x1-x0)*sc),int(140*sc))).save('zz.png')
