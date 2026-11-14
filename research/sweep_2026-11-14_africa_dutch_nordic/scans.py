"""IIIF thumbs and contact sheets for a Nationaal Archief scanned item.
usage: scans.py EAD INV OUTDIR [first=1] [last=N] [width=900]   (1-based scan order; one request per 2 s)
Images stay in OUTDIR (scratch, never in the repo)."""
import sys,os,json,time,urllib.request
ead,inv,out=sys.argv[1:4]; a=int(sys.argv[4]) if len(sys.argv)>4 else 1; b=int(sys.argv[5]) if len(sys.argv)>5 else 10**6; w=int(sys.argv[6]) if len(sys.argv)>6 else 900
os.makedirs(out,exist_ok=True)
H={'User-Agent':'Mozilla/5.0 (research)'}
d=json.load(urllib.request.urlopen(urllib.request.Request(f'https://zvt.nationaalarchief.nl/api/eads/{ead}/clevels/{inv}',headers=H),timeout=60))
sc=d['scans']; print(d['unittitle'],len(sc),'scans')
for s in sc[a-1:b]:
    fn=f"{out}/p{s['order']:04d}.jpg"
    if os.path.exists(fn): continue
    u=s['iiif']['url'].replace('/info.json','')+f'/full/{w},/0/default.jpg'
    try: open(fn,'wb').write(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=90).read())
    except Exception as e: print('ERR',s['order'],e)
    time.sleep(2)
