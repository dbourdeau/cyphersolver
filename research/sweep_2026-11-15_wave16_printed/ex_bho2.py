# BHO calendars: notes that say the EDITOR could not read cipher (not the routine "cipher, undeciphered" endorsement,
# which in Lomas's volumes means "no contemporary decipher on the paper"; her summary gives the text).
# usage: ex_bho2.py <file-regex>
import re,os,sys
sys.stdout.reconfigure(errors="replace")
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw","bho")
C=r"(?:c[iy]phers?|symbols?|characters|figures|numbers)"
N=r"(?:can ?not be (?:dec[iy]pher|read|made out|interpret|explain)|could not be (?:dec[iy]pher|read|made out)|not (?:been |yet )?(?:dec[iy]phered|made out|identified|explained|interpreted)|no key|key (?:is |has been )?(?:lost|wanting|missing)|without (?:a |the |any )?key|unintelligib|undecipherable|unexplained|unable to (?:dec[iy]pher|read)|impossible to (?:dec[iy]pher|read)|baffl|defied|meaning (?:is )?(?:unknown|uncertain|doubtful|obscure)|which (?:I|we) (?:have not|cannot))"
A=re.compile("(?:%s.{0,140}%s|%s.{0,140}%s)"%(C,N,N,C),re.I|re.S)
for f in sorted(os.listdir(S)):
    if not re.search(sys.argv[1],f): continue
    t=open(os.path.join(S,f),encoding="utf-8").read(); last=-999; n=0
    for m in A.finditer(t):
        if m.start()-last<300: continue
        last=m.start(); n+=1
        u=t.rfind("@@@",0,m.start())
        print("# %s @%d %s\n%s\n"%(f[:-4],m.start(),t[u+4:u+70].split("\n")[0],re.sub(r"\s+"," ",t[max(0,m.start()-450):m.end()+350])))
    print("==",f,n)
