# Letters of Delegates: one copy per volume; cipher/code word near any "unread" wording (wide net). usage: ex_lod.py
import re,os,json
S="raw"; ids=json.load(open("ids.json",encoding="utf-8"))
vol={}
for i,v in ids.items():
    if "delegates" not in v["q"] or not os.path.exists(S+"/"+i+".txt"): continue
    m=re.search(r"Volume (\d+)",v["title"] or "")
    k=str(v["volume"] or (m.group(1) if m else i))
    vol.setdefault(k,i)
print(sorted(vol.items(),key=lambda x:(len(x[0]),x[0])))
C=r"(?:c[iy]pher|\bcode[sd]?\b|encod|decod|in figures|numerical)"
N=r"(?:undec|not (?:been |be |yet )?(?:dec|translat|interpret|read\b|made out|found)|untranslat|unintelligib|unable|can ?not be|could not be|no key|key .{0,20}(?:lost|wanting|missing|not found|unknown)|without (?:a |the )?key|unknown|defie|remains? |never been|unidentified|unsolved|unbroken|conjectur|has not|have not)"
pat=re.compile("(?:%s.{0,120}%s|%s.{0,120}%s)"%(C,N,N,C),re.I|re.S)
out=[]
for k,i in vol.items():
    t=open(S+"/"+i+".txt",encoding="utf-8",errors="replace").read(); last=-999
    for m in pat.finditer(t):
        if m.start()-last<300: continue
        last=m.start(); out.append({"id":i,"vol":k,"pos":m.start(),"ctx":re.sub(r"\s+"," ",t[max(0,m.start()-300):m.end()+300])})
json.dump({"stats":{},"hits":out},open("n_lod2.json","w",encoding="utf-8"),indent=0,ensure_ascii=False); print(len(out))
