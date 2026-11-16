# every editorial bracket note mentioning cipher in a BHO file, with the entry heading; usage: brk.py <file-regex> [filter]
import re,os,sys
sys.stdout.reconfigure(errors="replace")
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw","bho")
flt=re.compile(sys.argv[2],re.I) if len(sys.argv)>2 else None
for f in sorted(os.listdir(S)):
    if not re.search(sys.argv[1],f): continue
    t=open(os.path.join(S,f),encoding="utf-8").read(); n=0
    for m in re.finditer(r"\[[^\[\]]{0,300}c[iy]pher[^\[\]]{0,300}\]",t,re.I):
        note=re.sub(r"\s+"," ",m.group(0))
        if flt and not flt.search(note): continue
        # entry heading: last "\n<num>. " before
        h=[x for x in re.finditer(r"(?:^|\n)\s*(\d{1,4})\. ([^\n]{0,160})",t[max(0,m.start()-6000):m.start()])]
        hd=(h[-1].group(1)+". "+h[-1].group(2)[:150]) if h else "?"
        u=t.rfind("@@@",0,m.start()); n+=1
        print("%s | %s | %s\n   %s"%(f[:-4].replace("cal-state-papers_",""),t[u+4:u+60].split("\n")[0].split("/")[-1],hd,note))
    print("==",f,n)
