import json,random
K=json.load(open('K1.json')); L={int(k):v for k,v in K['letters'].items()}; C=K['codes']
# Lettre tenue à l'écart (17 mars 1631, images 131R + 132L) : groupes et codes à glose lisible
LET=[("sudenburg","16.62.47.25.79.70.60.31.75"),("gering","75.25.30.52.79.77"),("stern","17.82.24.30.79"),
     ("diem","47.51.25.19"),("commius","48.65.20.19.51.62.15"),("tremisgewest","82.31.26.20.53.15.75.25.58.26.16.83")]
COD=[("705","capitain"),("3223","sparen"),("504","berg"),("2110","ekm"),("1328","feind"),("1328","feind"),("1328","feind"),
     ("3240","statt"),("1103","ein"),("1103","ein"),("3673","volk"),("2322","mangel"),("2843","proviant"),("3660","unser"),
     ("1455","für"),("2405","mittel"),("3778","wenig"),("2887","rath"),("2198","leben"),("258","anschlag"),("2399½","misslinge"),
     ("3101","schlagen"),("2101","können"),("3223","sparen"),("3088","schicken"),("2110","ekm"),("3328","tausend"),
     ("1925","hundert"),("2757","post"),("514","besetzen"),("3079","schantz"),("3748","was"),("3807","wir"),("3619","unter"),
     ("3240","statt"),("2666","paß"),("2597","offen"),("1762","halten"),("3594","will"),("429","bastant"),("1605","gesund")]
NORM={'ekm':'E.K.Mt','sparen':'Sparen(berg)','berg':'(Sparen)berg','mangel':'manquiren/mangel','feind':'feind','schlagen':'schlagen'}
def lscore(T):
    ok=tot=0
    for w,c in LET:
        for n,ch in zip(c.split('.'),w):
            tot+=1; ok+= (T.get(int(n))==ch)
    return ok/tot,ok,tot
def cscore(Cd):
    ok=tot=0; undef=0
    for k,w in COD:
        if k not in Cd: undef+=1; continue
        tot+=1; v=Cd[k].lower()
        ok+= (w[:4] in v) or (NORM.get(w,'#').lower()==v)
    return ok/tot if tot else 0,ok,tot,undef
print('letters',lscore(L)); print('codes',cscore(C))
random.seed(1126); ls=[];cs=[]
for i in range(200):
    vals=list(L.values()); random.shuffle(vals); T2=dict(zip(L.keys(),vals)); ls.append(lscore(T2)[0])
    cv=list(C.values()); random.shuffle(cv); C2=dict(zip(C.keys(),cv)); cs.append(cscore(C2)[0])
print('temoins letters max %.3f mean %.3f'%(max(ls),sum(ls)/200)); print('temoins codes max %.3f mean %.3f'%(max(cs),sum(cs)/200))
