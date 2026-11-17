import csv,random,re
D={r['code']:r for r in csv.DictReader(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'prince_key_dictionary_v2.tsv')),delimiter='\t')}
N=[('135','ne'),('1040','compt-'),('155','ez'),('1344','pas'),('740','pour le'),('378','moment'),('1808','sur la'),('2079','division'),('2218',"d'Autemarre"),('1531','je'),('1682','ne'),('1299','puis'),('676',"l'"),('2136','envoyer'),('2041','par'),('1056','mer'),('913',';'),('512','vous'),('835','la'),('981','re'),('1384','ce'),('1905','vrez'),('194','plus'),('1162','tard'),('1308','par'),('543','terre'),('431','.')]
def norm(s): return re.sub(r"[~()\s\-]|\(gal\)","",s.lower())
def match(pred,truth):
    ps=[norm(x) for x in pred.split('|')]; t=norm(truth)
    return any(p and (p==t or p.startswith(t) or t.startswith(p) or (t=="ne" and p=="n'") ) for p in ps)
ov=[(c,w) for c,w in N if c in D]
hits=[(c,w,D[c]['meaning'],D[c]['tier'],match(D[c]['meaning'],w)) for c,w in ov]
for h in hits: print(h)
obs=sum(h[4] for h in hits); print('overlap',len(ov),'correct',obs)
# null: shuffle meanings among all v2 codes
codes=list(D); means=[D[c]['meaning'] for c in codes]; random.seed(1859)
cnt=[];
for _ in range(10000):
    random.shuffle(means); M=dict(zip(codes,means))
    cnt.append(sum(match(M[c],w) for c,w in ov))
import statistics
print('null mean',statistics.mean(cnt),'max',max(cnt),'p(>=obs)',sum(x>=obs for x in cnt)/len(cnt))
for t in 'ABC':
    sub=[h for h in hits if h[3]==t]; print(t,len(sub),sum(h[4] for h in sub))
