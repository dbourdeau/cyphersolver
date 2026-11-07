import json,re,os,sys,time,urllib.parse,urllib.request,subprocess,hashlib
D="_dl/wb"; os.makedirs(D,exist_ok=True)
rows=json.load(open("cdx_saassipa.json"))[1:]
EXC=re.compile(r"Assenze|Contratti|Codice_|bando|Bando|Procedimenti|Quaderno|Quaderni|studi|Studi|Cinquecentine|SEICENTINE|Biblioteche|Notai|notai|Stato[-_ ]civile|Leggi|CV|Curriculum|Decreto|Avviso|Modulo|Piano|Regolamento|Carta|Relazione|Bilancio|Determin|Circolare|Programma|Disegni|Mostra|Catalogo|Locandina|Opuscolo",re.I)
INC=re.compile(r"REV|Repertorio|REPERTORIO|Inventario|INVENTARIO|Indice|INDICE|Real|Segret|Miscell|Ministero|Governo|Luogot|Tribunale|Carte|Archivio|Cancelleria|Conservatoria|Camera|Luogotenenza|Consulta|Intendenza|Prefettura|Commissione|Corrisp|Diplom|Famiglia|famiglia",re.I)
PAT=re.compile(r"cifr|decifr|chiffr|ciphe|cypher|zifra|in cifra|scrittura segreta|alfabeto segreto|cifrar|geroglifi",re.I)
def fetch(url,ts):
    u=f"http://web.archive.org/web/{ts}if_/{url}"
    for a in range(2):
        r=subprocess.run(["curl","-s","-m","90","-w","%{http_code}","-o","_dl/tmp.bin",u],capture_output=True,text=True)
        c=r.stdout.strip()
        if c=="200": return open("_dl/tmp.bin","rb").read()
        if c in("404","403"): return None
        time.sleep(40*(a+1))
sel=[r for r in rows if INC.search(urllib.parse.unquote(r[0]).split("/")[-1]) and not EXC.search(urllib.parse.unquote(r[0]).split("/")[-1]) and int(r[3] or 0)<6_000_000]
print(len(sel),flush=True)
out=open("wbpa_hits.jsonl","a",encoding="utf8")
for orig,ts,mt,ln in sel:
    name=urllib.parse.unquote(orig).split("/")[-1]
    print("GET",name,flush=True)
    fn=os.path.join(D,hashlib.md5(orig.encode()).hexdigest()[:8]+".txt")
    if not os.path.exists(fn):
        data=fetch(orig,ts); time.sleep(9)
        if not data: print("FAIL",name,flush=True); continue
        pdf=fn.replace(".txt",".pdf"); open(pdf,"wb").write(data)
        subprocess.run(["pdftotext","-layout",pdf,fn],capture_output=True)
        try: os.remove(pdf)
        except: pass
    if not os.path.exists(fn): print("NOTEXT",name,flush=True); continue
    txt=open(fn,encoding="utf8",errors="replace").read(); n=0
    for m in PAT.finditer(txt):
        out.write(json.dumps({"file":name,"orig":orig,"ctx":re.sub(r"\s+"," ",txt[max(0,m.start()-220):m.end()+220])},ensure_ascii=False)+"\n"); n+=1
    out.flush(); print("OK",name,len(txt),n,flush=True)
print("DONE")
