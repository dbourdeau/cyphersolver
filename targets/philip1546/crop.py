"""python crop.py <set> <canvas idx> x y w h out.jpg   (coords at 1200-px page width; fetched at native detail)"""
import json,subprocess,sys
sys.path.insert(0,'.')
exec(open('fetch.py').read().split('os.makedirs')[0])
k,n,x,y,w,h,out=sys.argv[1],int(sys.argv[2]),*map(int,sys.argv[3:7]),sys.argv[7]
m=json.load(open(f'man/{sets[k]}.json',encoding='utf8'))
c=m['sequences'][0]['canvases'][n]
rid=c['images'][0]['resource']['@id']
W=c['width'] if 'width' in c else 3000; f=W/1200
reg=f"{int(x*f)},{int(y*f)},{int(w*f)},{int(h*f)}"
subprocess.run(['curl','-sL','-m','90','-o',out,f"{rid}/{reg}/1800,/0/default.jpg"])
print(c.get('width'),c.get('height'),reg)
