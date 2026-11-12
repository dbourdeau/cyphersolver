import sys,re,math,random,unicodedata,collections
tx,keyf,seg=sys.argv[1:4]; corp=sys.argv[4:]
key={}
for l in open(keyf):
    if l.startswith('#'): continue
    for p in l.split(): a,b=p.split('='); key[a]=b
def dec(w,k): return ''.join('-' if ch=='-' else k.get(ch,'?') for ch in w).replace('-','')
# tokens from frozen transcription
toks=[]
for l in open(tx,encoding='utf8'):
    if not re.match(r'\d\d ',l): continue
    body=re.sub(r'<[^>]*>',' ',l[3:])
    toks+=[(l[:2],t) for t in body.split()]
# join hyphenated line-end units
units=[];i=0
while i<len(toks):
    lid,t=toks[i]
    if t.endswith('-') and i+1<len(toks): units.append((lid,t+toks[i+1][1])); i+=2
    else: units.append((lid,t)); i+=1
units=[(l,u) for l,u in units if u not in('3000','20')]
segs=[l.rstrip('\n').split('|') for l in open(seg,encoding='utf8') if not l.startswith('#')]
assert [(s[0],s[1]) for s in segs]==units, [(a,b) for a,b in zip(segs,units) if (a[0],a[1])!=b][:3]
tally=collections.Counter(); per=collections.defaultdict(collections.Counter)
for (lid,u),s in zip(units,segs):
    d=u if u.isdigit() else dec(u,key)
    assert d==s[2],(u,d,s[2])
    if s[3]=='S': assert '?' not in d and not u.isdigit()
    tally[s[3]]+=1; per['A' if int(lid)<=10 else 'B'][s[3]]+=1
n=sum(tally.values())
print('units',n,dict(tally),'strict S/n = %d/%d = %.2f%%'%(tally['S'],n,100*tally['S']/n),'S+E = %.2f%%'%(100*(tally['S']+tally['E'])/n))
for h in 'AB':
    m=sum(per[h].values()); print(' half',h,'(lines 01-10)' if h=='A' else '(lines 11-19)',dict(per[h]),'%d/%d = %.2f%%'%(per[h]['S'],m,100*per[h]['S']/m))
cur=None;out=[]
for (lid,u),s in zip(units,segs):
    if lid!=cur: out.append('\n'+lid+' '); cur=lid
    out.append(s[2]+' ')
print(''.join(out))
if not corp: sys.exit()
def norm(s):
    s=s.lower().replace('ß','ss'); s=unicodedata.normalize('NFD',s); s=''.join(ch for ch in s if unicodedata.category(ch)!='Mn')
    return re.sub(r'[^a-z]','',s).replace('v','u').replace('j','i')
cs=[]
for f in corp:
    t=open(f,encoding='utf8',errors='replace').read()
    assert re.search(r'^Language: German',t,re.M),f
    i=t.find('*** START'); j=t.find('*** END'); t=t[i:j]
    cs+=[norm(w) for w in re.findall(r"[^\W\d_]+",t)]
cs='#'.join(w for w in cs if w)
N=4; cnt=collections.Counter(cs[i:i+N] for i in range(len(cs)-N+1)); ctx=collections.Counter(cs[i:i+N-1] for i in range(len(cs)-N+1))
def lp(s):
    tot=0;n=0
    for i in range(len(s)-N+1):
        g=s[i:i+N]; tot+=math.log((cnt.get(g,0)+0.1)/(ctx.get(g[:-1],0)+2.7)); n+=1
    return tot/n
cu=[u for l,u in units if not u.isdigit()]
def stream(k): return '#'+'#'.join(dec(u,k).replace('?','') for u in cu)+'#'
true=lp(stream(key)); print('corpus chars',len(cs),'true score %.4f'%true)
random.seed(20261112); syms=sorted(key); vals=[key[s] for s in syms]; ge=0; best=-9
for _ in range(5000):
    v=vals[:]; random.shuffle(v); sc=lp(stream(dict(zip(syms,v)))); best=max(best,sc); ge+=sc>=true
print('shuffled keys at or above true: %d/5000; best shuffled %.4f'%(ge,best))
# second control: random plain alphabets (21 distinct letters drawn from a-z minus v,j)
ge2=0;best2=-9; al='abcdefghiklmnopqrstuwxyz'
for _ in range(5000):
    v=[random.choice(al) for _ in syms]; sc=lp(stream(dict(zip(syms,v)))); best2=max(best2,sc); ge2+=sc>=true
print('random-value keys at or above true: %d/5000; best %.4f'%(ge2,best2))
