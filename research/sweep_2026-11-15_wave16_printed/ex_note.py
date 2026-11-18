# windows where a cipher word sits near an "unread" phrase; usage: ex_note.py <id-regex> out.json
import re,os,sys,json
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw")
if len(sys.argv)>1 and sys.argv[1].startswith("bho:"): S=os.path.join(S,"bho"); sys.argv[1]=sys.argv[1][4:]
C=r"(?:c[iy]pher|chiffr|cifra|cifre\b|zifra|Ziffer|Chiffer|cijfer|in code\b|in figures|en chiffre)"
N=r"(?:undec[iy]pher|not (?:been |be |yet )?(?:dec[iy]pher|translat|interpret|read\b|made out)|untranslat|unintelligib|undecipherable|unable to (?:dec[iy]pher|translate|read)|can ?not (?:be )?(?:dec[iy]pher|translate|read|make)|could not (?:be )?(?:dec[iy]pher|translate|read|make)|no key|key (?:is |was |being |has been )?(?:lost|wanting|missing|not found)|without (?:a |the )?key|non d[ée]chiffr|pas (?:[ée]t[ée] )?d[ée]chiffr|ind[ée]chiffr|sans (?:le )?d[ée]chiffrement|n'a pu|n'avons pu|pas la clef|sans clef|clef (?:nous )?manque|nicht (?:aufgel|entziff|dechiff)|unaufgel|ohne Aufl|non decifr|sin descifr|niet ontcijf|inintelligible|inexpliqu)"
pat=re.compile("(?:%s.{0,160}%s|%s.{0,160}%s)"%(C,N,N,C),re.I|re.S)
idre=re.compile(sys.argv[1]); out=[]; stats={}
for f in sorted(os.listdir(S)):
    if not f.endswith(".txt"): continue
    i=f[:-4]
    if not idre.search(i): continue
    t=open(os.path.join(S,f),encoding='utf-8',errors='replace').read()
    stats[i]=[len(t),len(re.findall(C,t,re.I)),0]
    last=-1000
    for m in pat.finditer(t):
        if m.start()-last<400: continue
        last=m.start(); stats[i][2]+=1
        out.append({"id":i,"pos":m.start(),"ctx":re.sub(r"\s+"," ",t[max(0,m.start()-400):m.end()+400])})
print(len(out))
json.dump({"stats":stats,"hits":out},open(sys.argv[2],"w",encoding='utf-8'),indent=0,ensure_ascii=False)
