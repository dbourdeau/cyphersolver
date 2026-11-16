# download djvu OCR for every identifier in ids.json into raw/ ; usage: dl.py ids.json [<regex on q/title>]
import json,os,re,sys,time,urllib.request,urllib.parse
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw")
ids=json.load(open(sys.argv[1],encoding='utf-8')); p2=re.compile(sys.argv[2] if len(sys.argv)>2 else ".",re.I)
H={"User-Agent":"Mozilla/5.0"}
def get(u,t=240): return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=t).read()
for i,v in ids.items():
    if not p2.search(str(v.get("q"))+str(v.get("title"))): continue
    p=os.path.join(S,i+".txt")
    if os.path.exists(p) or os.path.exists(p+".fail"): continue
    try:
        try: b=get("https://archive.org/download/%s/%s_djvu.txt"%(i,urllib.parse.quote(i)))
        except Exception:
            m=json.loads(get("https://archive.org/metadata/%s/files"%i,60))
            n=[f["name"] for f in m.get("result",[]) if f["name"].endswith("_djvu.txt")]
            if not n: raise
            time.sleep(1); b=get("https://archive.org/download/%s/%s"%(i,urllib.parse.quote(n[0])))
        open(p,"wb").write(b); print("ok",i,len(b),flush=True)
    except Exception as e:
        open(p+".fail","w").write(str(e)); print("fail",i,e,flush=True)
    time.sleep(1)
