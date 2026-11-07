import json,re,os,time,urllib.parse,subprocess,hashlib,sys
exec(open("wbpa.py",encoding="utf8").read().split("sel=")[0])
pat=re.compile(sys.argv[1],re.I)
sel=[r for r in rows if pat.search(urllib.parse.unquote(r[0]).split("/")[-1]) and int(r[3] or 0)<8_000_000]
sel=[r for r in sel if not os.path.exists(os.path.join(D,hashlib.md5(r[0].encode()).hexdigest()[:8]+".txt"))]
print(len(sel),flush=True)
out=open("wbpa_hits.jsonl","a",encoding="utf8")
for orig,ts,mt,ln in sel:
    name=urllib.parse.unquote(orig).split("/")[-1]; print("GET",name,flush=True)
    data=fetch(orig,ts)
    if not data: print("FAIL",name,flush=True); continue
    fn=os.path.join(D,hashlib.md5(orig.encode()).hexdigest()[:8]+".txt"); pdf=fn.replace(".txt",".pdf"); open(pdf,"wb").write(data)
    subprocess.run(["pdftotext","-layout",pdf,fn],capture_output=True)
    try: os.remove(pdf)
    except: pass
    txt=open(fn,encoding="utf8",errors="replace").read(); n=0
    for m in PAT.finditer(txt):
        out.write(json.dumps({"file":name,"orig":orig,"ctx":re.sub(r"\s+"," ",txt[max(0,m.start()-220):m.end()+220])},ensure_ascii=False)+"\n"); n+=1
    out.flush(); print("OK",name,len(txt),n,flush=True); time.sleep(9)
