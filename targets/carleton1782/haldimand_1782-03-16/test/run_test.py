import sys,json,random,re
sys.path.insert(0,sys.argv[0].rsplit('/',1)[0])
from parse import parse
keyf,ctf,cribf=sys.argv[1:4]
lines={}
for l in open(keyf):
    if l.startswith('#') or not l.strip(): continue
    n,t=l.rstrip('\n').split('\t',1); lines[int(n)]=[c.lower() for c in t if c.isalpha() or c=='&']
words=parse(ctf)
crib={tuple(map(int,k.split('.'))):v for k,v in json.load(open(cribf)).items()}
dic=set(w.strip().lower() for w in open('/usr/share/dict/words'))
dic|={'routes','governor','robertson','sorel','sixteenth','received','reports','directly','days','wrote','entreat'} if False else set()
def dec(cell,L):
    if cell=='@': return 'q'
    if not isinstance(cell,tuple): return '?'
    l,p=cell; row=L.get(l)
    return row[p-1] if row and 1<=p<=len(row) else '?'
def score(L,tf=lambda c:c):
    agree=sum(1 for c,v in crib.items() if dec(tf(c),L)==v)/len(crib)
    ws=[w for w in words[:-1] if w[1]]
    ok=sum(1 for cl,cs in ws if ''.join(dec(tf(c) if isinstance(c,tuple) else c,L) for c in cs) in dic)
    return agree, ok/len(ws), len(ws)
mode=sys.argv[4] if len(sys.argv)>4 else 'test'
if mode=='decode':
    for i,(cl,cs) in enumerate(words,1):
        print(f'W{i:02d}',' '.join(cl),'|',''.join(dec(c,lines) for c in cs))
    sys.exit()
print('real', score(lines))
print('C1 line+1', score(lines, lambda c:((c[0]%29)+1,c[1]) if isinstance(c,tuple) else c))
print('C2 place+1', score(lines, lambda c:(c[0],c[1]+1) if isinstance(c,tuple) else c))
res=[]
for s in range(200):
    r=random.Random(s); L={k:r.sample(v,len(v)) for k,v in lines.items()}; res.append(score(L))
print('C3 shuffle mean agree %.3f max %.3f; mean words %.3f max %.3f'%(sum(x[0] for x in res)/200,max(x[0] for x in res),sum(x[1] for x in res)/200,max(x[1] for x in res)))
print('C4 reversed', score(lines, lambda c:(30-c[0],c[1]) if isinstance(c,tuple) else c))
