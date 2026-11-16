# every cipher-word window, short; usage: allc.py <id-regex> [width] [extra-filter-regex]
import re,os,sys
S=os.environ.get("RAW") or os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw")
if len(sys.argv)>1 and sys.argv[1].startswith("bho:"): S=os.path.join(S,"bho"); sys.argv[1]=sys.argv[1][4:]
C=re.compile(r"(?:c[iy]pher|chiffr|\bcifra|\bcifre\b|zifra|Ziffer|Chiffer|cijfer|in figures)",re.I)
idre=re.compile(sys.argv[1]); w=int(sys.argv[2]) if len(sys.argv)>2 else 200
flt=re.compile(sys.argv[3],re.I) if len(sys.argv)>3 else None
for f in sorted(os.listdir(S)):
    if not f.endswith(".txt") or not idre.search(f): continue
    t=open(os.path.join(S,f),encoding='utf-8',errors='replace').read(); last=-999
    for m in C.finditer(t):
        if m.start()-last<w: continue
        last=m.start(); c=re.sub(r"\s+"," ",t[max(0,m.start()-w):m.end()+w])
        if flt and not flt.search(c): continue
        print("%s @%d: %s\n"%(f[:-4],m.start(),c))
