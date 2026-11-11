# windows for German/other "not resolved" cipher notes in ocr2; usage: ex_de.py id [regex]
import re,sys,os
S="/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a4/ocr2"
t=open(os.path.join(S,sys.argv[1]+".txt"),encoding="utf-8",errors="replace").read()
pat=re.compile(sys.argv[2] if len(sys.argv)>2 else r"unaufgel|nicht\s+aufgel|ohne\s+Aufl|nicht\s+de[cs]hiff|nicht\s+entziff|unentziff|unde[cs]hiff|nicht\s+ch?iffr",re.I)
W=int(sys.argv[3]) if len(sys.argv)>3 else 500
last=-9999
for m in pat.finditer(t):
    if m.start()-last<W: continue
    last=m.start()
    print("@%d"%m.start(), re.sub(r"\s+"," ",t[max(0,m.start()-W):m.end()+W//2])); print()
