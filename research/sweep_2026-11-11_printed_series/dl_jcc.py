# JCC volumes: the text file name differs from the identifier, so look it up in the metadata first.
import json,os,re,time,urllib.request,urllib.parse
S="/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a4/ocr"
ids=[i for i in json.load(open("ids.json")) if i.startswith("journals-of-the-continental-congress-1774-1789-vol")]
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=240).read()
for i in sorted(ids):
    p=os.path.join(S,i+".txt")
    if os.path.exists(p): continue
    try:
        fs=json.loads(get("https://archive.org/metadata/%s/files"%i))["result"]
        n=[f["name"] for f in fs if f["name"].endswith("_djvu.txt")][0]
        open(p,"wb").write(get("https://archive.org/download/%s/%s"%(i,urllib.parse.quote(n)))); print("ok",i,flush=True)
    except Exception as e: print("fail",i,e,flush=True)
    time.sleep(2)
