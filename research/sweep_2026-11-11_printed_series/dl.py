# download djvu OCR for selected identifiers to scratch; usage: dl.py ids.json <regex on id> [<regex on q/contrib>]
import json,os,re,sys,time,urllib.request
S="/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a4/ocr"
ids=json.load(open(sys.argv[1])); pat=re.compile(sys.argv[2]); p2=re.compile(sys.argv[3] if len(sys.argv)>3 else ".")
for i,v in ids.items():
    if not pat.search(i) or not p2.search(str(v.get("q"))+str(v.get("contrib"))+str(v.get("title"))): continue
    p=os.path.join(S,i+".txt")
    if os.path.exists(p): continue
    try:
        r=urllib.request.urlopen(urllib.request.Request("https://archive.org/download/%s/%s_djvu.txt"%(i,i),headers={"User-Agent":"Mozilla/5.0"}),timeout=240)
        open(p,"wb").write(r.read()); print("ok",i,flush=True)
    except Exception as e: print("fail",i,e,flush=True)
    time.sleep(2)
