# every "undeciphered / not deciphered / undecipherable" note in BHO files, with entry number+heading and the next entry
# (to see a "Decipher of the above" sibling); usage: und.py <file-regex>
import re,os,sys
sys.stdout.reconfigure(errors="replace")
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw","bho")
P=re.compile(r"partly dec[iy]pher|partially dec[iy]pher|in part dec[iy]pher|undec[iy]pher|not (?:been )?dec[iy]pher|undecipherable|without (?:a )?decipher|no decipher",re.I)
H=re.compile(r"(?:^|\n|\. )\s*(\d{1,4})\. ([A-Z][^\n]{0,140})")
for f in sorted(os.listdir(S)):
    if not re.search(sys.argv[1],f): continue
    t=open(os.path.join(S,f),encoding="utf-8").read(); last=-999; n=0
    for m in P.finditer(t):
        if m.start()-last<200: continue
        last=m.start(); n+=1
        hs=list(H.finditer(t,max(0,m.start()-5000),m.start()))
        hd=(hs[-1].group(1)+". "+hs[-1].group(2)[:110]) if hs else "?"
        nx=H.search(t,m.end(),m.end()+1500)
        nxt=(nx.group(1)+". "+nx.group(2)[:90]) if nx else ""
        ctx=re.sub(r"\s+"," ",t[max(0,m.start()-160):m.end()+60])
        print("%s | %s\n   ...%s\n   NEXT: %s"%(f[:-4].replace("cal-state-papers_",""),hd,ctx,nxt))
    print("==",f,n)
