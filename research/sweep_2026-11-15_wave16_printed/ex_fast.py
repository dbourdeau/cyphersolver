# faster ex_note: find "unread" phrases, keep those with a cipher word within 200 chars; usage: ex_fast.py <id-regex> out.json [bho]
import re,os,sys,json
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw")
if len(sys.argv)>3: S=os.path.join(S,"bho")
C=re.compile(r"(?:c[iy]pher|chiffr|cifra|cifre\b|zifra|Ziffer|Chiffer|cijfer|in code\b|in figures|en chiffre)",re.I)
N=re.compile(r"(?:undec[iy]pher|not (?:been |be |yet )?(?:dec[iy]pher|translat|interpret|read\b|made out)|untranslat|unintelligib|undecipherable|unable to (?:dec[iy]pher|translate|read)|can ?not (?:be )?(?:dec[iy]pher|translate|read|make)|could not (?:be )?(?:dec[iy]pher|translate|read|make)|no key|key (?:is |was |being |has been )?(?:lost|wanting|missing|not found)|without (?:a |the )?key|non d[ée]chiffr|pas (?:[ée]t[ée] )?d[ée]chiffr|ind[ée]chiffr|sans (?:le )?d[ée]chiffrement|n'a pu|n'avons pu|pas la clef|sans clef|clef (?:nous )?manque|nicht (?:aufgel|entziff|dechiff)|unaufgel|ohne Aufl|non decifr|sin descifr|niet ontcijf|inintelligible|inexpliqu)",re.I)
idre=re.compile(sys.argv[1]); out=[]; stats={}
for f in sorted(os.listdir(S)):
    if not f.endswith(".txt") or not idre.search(f[:-4]): continue
    i=f[:-4]; t=open(os.path.join(S,f),encoding='utf-8',errors='replace').read()
    last=-1000; n=0
    for m in N.finditer(t):
        if m.start()-last<400: continue
        if not C.search(t,max(0,m.start()-200),m.end()+200): continue
        last=m.start(); n+=1
        out.append({"id":i,"pos":m.start(),"ctx":re.sub(r"\s+"," ",t[max(0,m.start()-500):m.end()+400])})
    stats[i]=[len(t),n]
print(len(out))
json.dump({"stats":stats,"hits":out},open(sys.argv[2],"w",encoding='utf-8'),indent=0,ensure_ascii=False)
