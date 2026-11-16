"""Palermo SAASSIPA inventory PDFs via Wayback (curl), the ones the 6 Nov sweep did not fetch. grep for cipher words."""
import json,re,os,sys,time,urllib.parse,subprocess,hashlib
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
D="_dl/wb"; os.makedirs(D,exist_ok=True)
rows=json.load(open("cdx_saassipa.json"))[1:]
old=set()
for f in ("../sweep_2026-11_naples_palermo/wbpa.log","../sweep_2026-11_naples_palermo/wbpa2.log"):
    for l in open(f,encoding="utf8",errors="replace"):
        p=l.split(None,2)
        if len(p)>1 and p[0] in("OK","FAIL","NOTEXT"): old.add(p[1])
EXC=re.compile(r"Assenze|Contratti-di|Codice_|bando|Procedimenti|Quaderni|Quaderno|Avviso|Decreto|Determina|CV-|Programma|Locandina|Curriculum",re.I)
PAT=re.compile(r"cifr|decifr|chiffr|ciphe|cypher|zifra|in cifra|scrittura segreta|alfabeto segreto|cifrar|geroglifi|criptogr|in codice|cifrario",re.I)
def fetch(url,ts):
    u=f"http://web.archive.org/web/{ts}if_/{url}"
    for a in range(2):
        r=subprocess.run(["curl","-s","-m","100","-w","%{http_code}","-o","_dl/tmp.bin",u],capture_output=True,text=True)
        c=r.stdout.strip()
        if c=="200": return open("_dl/tmp.bin","rb").read()
        if c in("404","403"): return None
        time.sleep(20*(a+1))
sel=[]
for orig,ts,mt,ln in rows:
    name=urllib.parse.unquote(orig).split("/")[-1]
    if name in old or EXC.search(name) or int(ln or 0)>30_000_000: continue
    sel.append((orig,ts,name,int(ln or 0)))
sel.sort(key=lambda r:r[3])
print(len(sel),flush=True)
out=open("wbpa4_hits.jsonl","a",encoding="utf8")
for orig,ts,name,ln in sel:
    fn=os.path.join(D,hashlib.md5(orig.encode()).hexdigest()[:8]+".txt")
    if os.path.exists(fn): continue
    print("GET",name,ln,flush=True)
    data=fetch(orig,ts); time.sleep(5)
    if not data: print("FAIL",name,flush=True); continue
    pdf=fn.replace(".txt",".pdf"); open(pdf,"wb").write(data)
    subprocess.run(["pdftotext","-layout",pdf,fn],capture_output=True)
    try: os.remove(pdf)
    except Exception: pass
    if not os.path.exists(fn): print("NOTEXT",name,flush=True); continue
    txt=open(fn,encoding="utf8",errors="replace").read(); n=0
    for m in PAT.finditer(txt):
        out.write(json.dumps({"file":name,"orig":orig,"ctx":re.sub(r"\s+"," ",txt[max(0,m.start()-220):m.end()+220])},ensure_ascii=False)+"\n"); n+=1
    out.flush(); print("OK",name,len(txt),n,flush=True)
print("DONE")
