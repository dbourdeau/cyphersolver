import sys,json,urllib.request,time
sys.path.insert(0,'/tmp/om')
A="0123456789bcdfghjkmnpqrstvwxz"
def ark(core):
    t=sum(i*(A.index(c) if c in A else 0) for i,c in enumerate(core,1)); return core+A[t%29]
def label(a):
    u=f"https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/{a}/manifest.json"
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=60)
        d=json.load(r); return d['label'], len(d.get('items',[])), [m['value'] for m in d.get('metadata',[])][:0]
    except Exception as e: return str(e)
if __name__=="__main__":
    for n in range(int(sys.argv[1]),int(sys.argv[2])+1):
        a=ark(f"btv1b{n}"); print(a,label(a),flush=True); time.sleep(3)
