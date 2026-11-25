"""Mesure unique n° 2530 (protocole PROTOCOL.md + addendum 1). Usage : python3 -I mesure.py table_T.json H.txt"""
import sys, json, random, re, unicodedata
T=json.load(open(sys.argv[1]))['T']
rows=[]
for l in open(sys.argv[2],encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    g,gl=l.rstrip('\n').split('\t'); rows.append((g.split('.'),gl))
def norm(s):
    s=unicodedata.normalize('NFD',s.lower()); return re.sub('[^a-z]','',s)
def lev(a,b):
    prev=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        cur=[i]
        for j,cb in enumerate(b,1): cur.append(min(prev[j]+1,cur[j-1]+1,prev[j-1]+(ca!=cb)))
        prev=cur
    return prev[-1]
R=''.join(norm(gl) for _,gl in rows)
def run(tab):
    P=''.join(''.join(tab.get(x,'') for x in g) for g,_ in rows)
    return 1-lev(P,R)/max(len(P),len(R)), P
s,P=run(T)
words=sum(1 for g,gl in rows if ''.join(T.get(x,'') for x in g)==norm(gl))
keys=list(T); vals=[T[k] for k in keys]; wit=[]
for seed in range(1,201):
    r=random.Random(seed); v=vals[:]; r.shuffle(v); wit.append(run(dict(zip(keys,v)))[0])
best=max(wit)
print(json.dumps({'groupes':sum(len(g) for g,_ in rows),'suites':len(rows),'len_R':len(R),'len_P':len(P),'score_car':round(s,4),
 'meilleur_temoin':round(best,4),'moyenne_temoins':round(sum(wit)/200,4),'marge':round(s-best,4),
 'critere':'car>=0.85 et >= meilleur+0.30','valide':s>=0.85 and s>=best+0.30,'accord_mots_suites':'%d/%d'%(words,len(rows))},ensure_ascii=False,indent=1))
