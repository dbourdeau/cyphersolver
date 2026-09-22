import re,json,sys,collections,em
sys.argv=['x','fold']
exec(open('run1.py').read().split("txt=open")[0])
txt=open('tx/decipherment.txt',encoding='utf8').read()
P=dict((int(k),em.norm(v)) for k,v in re.findall(r'\[(\d+)\]\n([^\[]*)',txt))
i=P[5].index('ilmarchesespinola'); j=P[5].index('etgiasie')
pairs=[(prep(lines(55,67)),P[5][:i]),(prep(lines(74,117)),P[5][j:]+P[6]+P[7]),(prep(lines(276,285)),P[9]),
       (prep(lines(289,354)),P[11]+P[12]+P[13]+P[14]),(prep(lines(372,398)),P[15]+P[16])]
for G,A in pairs: print(len(G),len(A),round(len(A)/len(G),2))
t,cnt=em.run(pairs,iters=30)
key={g:(max(d,key=d.get),round(max(d.values()),2),round(sum(cnt[g].values()),1)) for g,d in t.items()}
json.dump(key,open('key2.json','w'),indent=0)
json.dump([(G,A) for G,A in pairs],open('pairs.json','w'))
