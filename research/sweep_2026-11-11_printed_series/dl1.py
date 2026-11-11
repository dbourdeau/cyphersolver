# download named identifiers' OCR to scratch; usage: dl1.py id ...
import os,sys,time,urllib.request
S="/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a4/ocr2"
os.makedirs(S,exist_ok=True)
for i in sys.argv[1:]:
    p=os.path.join(S,i+".txt")
    if os.path.exists(p): print("have",i); continue
    try:
        r=urllib.request.urlopen(urllib.request.Request("https://archive.org/download/%s/%s_djvu.txt"%(i,i),headers={"User-Agent":"Mozilla/5.0"}),timeout=240)
        open(p,"wb").write(r.read()); print("ok",i,os.path.getsize(p),flush=True)
    except Exception as e: print("fail",i,e,flush=True)
    time.sleep(2)
