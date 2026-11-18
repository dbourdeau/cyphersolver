# extra English placeholder phrases; usage: ex_eng2.py <id-regex>
import re,os,sys
sys.stdout.reconfigure(errors="replace")
S=os.environ.get("RAW") or os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw")
P=re.compile(r"(?:\[(?:in )?c[iy]pher\]|\((?:in )?c[iy]pher\)|c[iy]pher(?:s)? (?:omitted|not (?:given|printed|solved|explained|interpreted|read))|(?:figures|numbers|cipher groups?) (?:omitted|not deciphered|undeciphered)|remains? undec[iy]pher|still undec[iy]pher|key (?:to (?:this|the) c[iy]pher )?(?:has not been|is not|was not) (?:found|forthcoming|discovered)|no decipher|without (?:a |any )?decipher|not (?:yet )?been (?:dec[iy]phered|interpreted|explained)|have not (?:been able to )?(?:dec[iy]pher|interpret)|baffled|defied (?:all )?(?:attempts|interpretation))",re.I)
idre=re.compile(sys.argv[1]); n=0
for f in sorted(os.listdir(S)):
    if not f.endswith(".txt") or not idre.search(f): continue
    t=open(os.path.join(S,f),encoding='utf-8',errors='replace').read(); last=-999
    for m in P.finditer(t):
        if m.start()-last<300: continue
        c=t[max(0,m.start()-250):m.end()+150]
        if not re.search(r"c[iy]pher|figures|numbers|key",c,re.I): continue
        last=m.start(); n+=1; print("%s @%d: %s\n"%(f[:-4],m.start(),re.sub(r"\s+"," ",c)))
print("hits",n)
