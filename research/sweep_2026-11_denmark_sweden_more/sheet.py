"""Resolve NAD ids to IIIF series, count images, make sampled contact sheets (every k-th image, 30 per sheet).
python sheet.py resolve id:label ...   -> units.json
python sheet.py sheet <man> [k]        -> sheets in SP/sheets"""
import json,os,re,sys,time,requests
from rik_common import SP,H,count,img,grid
U=os.path.join(os.path.dirname(os.path.abspath(__file__)),'units.json')
def units():
    return json.load(open(U,encoding='utf-8')) if os.path.exists(U) else {}
def resolve(args):
    u=units()
    for a in args:
        i,lab=a.split(':',1)
        r=requests.get(f'https://data.riksarkivet.se/archive/{i}.jsonld',headers=H,timeout=60).text
        m=re.search(r'arkis!(R\d+|[0-9A-Z]+)/manifest',r)
        if not m: print(i,'no manifest');continue
        man=m.group(1);n=count(man)
        u[man]=dict(id=i,label=lab,n=n);print(man,n,lab);time.sleep(2.5)
    json.dump(u,open(U,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
def sheet(man,k=None,tw=330,start=1):
    u=units()[man];n=u['n'];k=k or max(1,n//150)
    idx=list(range(start,n+1,k));os.makedirs(SP+'/sheets',exist_ok=True);out=[]
    for a in range(0,len(idx),30):
        ch=idx[a:a+30];tiles=[]
        for i in ch:
            tiles.append(img(man,i,tw));time.sleep(1)
        out.append(grid(tiles,ch,6,tw,f'{SP}/sheets/{man}_{ch[0]}-{ch[-1]}_k{k}.jpg'))
    print('\n'.join(out))
if __name__=='__main__':
    c=sys.argv[1]
    if c=='resolve':resolve(sys.argv[2:])
    else:sheet(sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else None)
