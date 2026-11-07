import re,sys,json,collections
sys.stdout.reconfigure(encoding="utf8")
t=open(r"C:\Users\dbour\enquete\gouvernementdela02favr.txt",encoding="utf8",errors="replace").read()
m=re.search(r"Nos\s+communications\s+par\s+ballon\s+sont\s+si\s+incertaines",t)
seg=t[m.start():m.start()+14000]
seg=re.sub(r"\n[ \t]*\d+[ \t]+SIMPLE R[ÉE]CIT\.[ \t]*(?=\n)","",seg)
seg=re.sub(r"\n[ \t]*CONF[ÉE]RENCE DE LONDRES\.[ \t]*\d+[ \t]*(?=\n)","",seg)
seg=re.sub(r"-\s*\n\s*(»|«|v|y)?\s*","",seg)
seg=re.sub(r"\n\s*(»|«|v|y)\s+"," ",seg)
seg=re.sub(r"\s+"," ",seg)
for a,b in [("com.» battaient","combattaient"),("lime semble","Il me semble"),("yavoird'hésitation","y avoir d'hésitation"),("con9 sentons","consentons"),("Ghanzy","Chanzy"),("interprêté","interprété"),("■»",""),("resCONFERENCE DE LONDRES. 269 ponsabilité","responsabilité"),("limite 268 SIMPLE RECIT. du","limite du"),("Nous 270 SIMPLE RECIT. allons","Nous allons"),("raison de croire 9 que","raison de croire que")]:
    seg=seg.replace(a,b)
seg=re.sub(r" 9 "," ",seg)
seg=re.sub(r"\b\d{3} SIMPLE RECIT\.","",seg); seg=re.sub(r"CONFERENCE DE LONDRES\. \d{3}","",seg)
seg=re.sub(r"\s+"," ",seg)
e=seg.find("Jules Favre.")
seg=seg[:e+len("Jules Favre.")]
open("chaudordy_18dec_plain.txt","w",encoding="utf8").write(seg)
words=[w.replace("’","'") for w in re.findall(r"[\wéèêëàâîïôùûüçœ'’]+",seg.lower())]
print(len(words),"tokens",sum(len(w) for w in words),"letters")
cipher=json.load(open("chaudordy_nums.json"))
print(len(cipher),"cipher groups; groups/word %.2f"%(len(cipher)/len(words)))
def rep(seq,n):
    c=collections.Counter(tuple(seq[i:i+n]) for i in range(len(seq)-n+1)); return sum(1 for v in c.values() if v>1)
for n in (2,3,4): print("n=%d repeated: plaintext words %d, cipher groups %d"%(n,rep(words,n),rep(cipher,n)))
print(collections.Counter(words).most_common(14)); print(collections.Counter(cipher).most_common(14))
print(seg[-300:])
