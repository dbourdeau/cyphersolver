# French editions in ocr2: cipher notes; usage: ex_fr.py idregex [pattern] [width]
import re,sys,os
S="/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a4/ocr2"
pat=re.compile(sys.argv[2] if len(sys.argv)>2 and sys.argv[2] else r"(?:chiffr|cyphr|cijfer).{0,120}(?:non\s+d[ée]ch|ind[ée]chiff|pas\s+(?:[ée]t[ée]\s+)?d[ée]chiff|pu\s+(?:[êe]tre\s+)?d[ée]chiff|pas\s+la\s+clef|sans\s+clef|clef\s+manque|niet\s+ontcijf|inconnu)|(?:non\s+d[ée]ch|ind[ée]chiff|pas\s+(?:[ée]t[ée]\s+)?d[ée]chiff|pu\s+(?:[êe]tre\s+)?d[ée]chiff|pas\s+la\s+clef).{0,120}chiffr",re.I|re.S)
W=int(sys.argv[3]) if len(sys.argv)>3 else 350
for f in sorted(os.listdir(S)):
    if not re.search(sys.argv[1],f): continue
    t=open(os.path.join(S,f),encoding="utf-8",errors="replace").read(); last=-9999
    for m in pat.finditer(t):
        if m.start()-last<W: continue
        last=m.start()
        print(f[:-4],"@%d"%m.start(), re.sub(r"\s+"," ",t[max(0,m.start()-W):m.end()+W//2])); print()
