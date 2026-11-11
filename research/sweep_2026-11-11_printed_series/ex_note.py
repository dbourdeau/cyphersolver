# windows where a cipher word sits near an "unread" phrase; usage: ex_note.py <id-regex> [out.json]
import re,os,sys,json
S="/tmp/claude-0/-home-user-cyphersolver/b534c128-0c0f-5181-b92e-4d606efc3a8f/scratchpad/a4/ocr"
C=r"(?:c[iy]pher|chiffr|cifra|Ziffer|Chiffer|cijfer|in code\b)"
N=r"(?:undec[iy]pher|not (?:been |be |yet )?(?:dec[iy]pher|translat|interpret|read\b|made out)|untranslat|unintelligib|unable to (?:dec[iy]pher|translate|read)|can ?not (?:be )?(?:dec[iy]pher|translate|read|make)|could not (?:be )?(?:dec[iy]pher|translate|read|make)|no key|key (?:is |was |being )?(?:lost|wanting|missing|not found)|without (?:a |the )?key|non d[ée]chiffr|ind[ée]chiffr|nicht (?:aufgel|entziff|dechiff)|unaufgel|non decifr|sin descifr|niet ontcijf)"
pat=re.compile("(?:%s.{0,160}%s|%s.{0,160}%s)"%(C,N,N,C),re.I|re.S)
idre=re.compile(sys.argv[1]); out=[]
for f in sorted(os.listdir(S)):
    i=f[:-4]
    if not idre.search(i): continue
    t=open(os.path.join(S,f),encoding='utf-8',errors='replace').read()
    last=-1000
    for m in pat.finditer(t):
        if m.start()-last<400: continue
        last=m.start()
        out.append({"id":i,"pos":m.start(),"ctx":re.sub(r"\s+"," ",t[max(0,m.start()-350):m.end()+350])})
print(len(out))
json.dump(out,open(sys.argv[2] if len(sys.argv)>2 else "notes.json","w"),indent=0)
