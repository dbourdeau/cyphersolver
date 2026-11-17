# English calendars: (a) cipher word near an "unread" phrase; (b) "in cipher/cypher" endorsement with no decipher word within 500 chars.
# usage: ex_cal.py [bho:]<id-regex> out.json
import re,os,sys,json
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),"raw")
if sys.argv[1].startswith("bho:"): S=os.path.join(S,"bho"); sys.argv[1]=sys.argv[1][4:]
C=r"(?:c[iy]pher|in figures|in numbers|in characters)"
N=r"(?:undec[iy]pher|not (?:been |be |yet )?(?:dec[iy]pher|translat|interpret|read\b|made out)|untranslat|unintelligib|unable to (?:dec[iy]pher|translate|read)|can ?not (?:be )?(?:dec[iy]pher|translate|read|make)|could not (?:be )?(?:dec[iy]pher|translate|read|make)|no (?:key|dec[iy]pher)|key (?:is |was |being |has been )?(?:lost|wanting|missing|not found)|without (?:a |the |any )?(?:key|dec[iy]pher)|unexplained|not explained|unsolved|illegible)"
A=re.compile("(?:%s.{0,160}%s|%s.{0,160}%s)"%(C,N,N,C),re.I|re.S)
B=re.compile(r"(?:(?:wholly|entirely|mostly|chiefly|partly|partially|all|principally|largely|almost all|nearly all|written|letter|paper|lines?|pages?|passages?|postscript|rest|remainder) (?:is |are |being |written )?in c[iy]pher|\[in c[iy]pher\.?\]|in c[iy]pher[.,;]? *(?:endd|add|\d|pp?\b|holog|copy|draft|lat|fr|ital|span|\]|\)))",re.I)
D=re.compile(r"dec[iy]pher|interlin|key\b|translat",re.I)
idre=re.compile(sys.argv[1]); out=[]; stats={}
for f in sorted(os.listdir(S)):
    if not f.endswith(".txt") or not idre.search(f): continue
    t=open(os.path.join(S,f),encoding='utf-8',errors='replace').read(); i=f[:-4]
    stats[i]=[len(t),len(re.findall(C,t,re.I)),0,0]; last=-1000
    for m in A.finditer(t):
        if m.start()-last<400: continue
        last=m.start(); stats[i][2]+=1
        out.append({"id":i,"k":"A","pos":m.start(),"ctx":re.sub(r"\s+"," ",t[max(0,m.start()-500):m.end()+300])})
    last=-1000
    for m in B.finditer(t):
        if m.start()-last<400: continue
        if D.search(t[max(0,m.start()-500):m.end()+500]): continue
        last=m.start(); stats[i][3]+=1
        out.append({"id":i,"k":"B","pos":m.start(),"ctx":re.sub(r"\s+"," ",t[max(0,m.start()-600):m.end()+250])})
for k,v in stats.items(): print(k,v)
json.dump({"stats":stats,"hits":out},open(sys.argv[2],"w",encoding='utf-8'),indent=0,ensure_ascii=False)
