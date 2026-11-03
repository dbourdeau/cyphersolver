import sys,json,random,re,subprocess
sys.path.insert(0,'scripts')
# held-out: blind pass tokens + frozen table against margins. name map fixed from the 14 Nov alignment.
def loadk(f):
    d={}
    for l in open(f,encoding='utf8'):
        if l.startswith('#') or not l.strip(): continue
        p=l.rstrip('\n').split('\t'); d[p[0]]=p[1]
    return d
def norm(s):
    s=s.lower().replace('v','u').replace('y','i').replace('h','').replace('ç','c').replace('z','c')
    return re.sub('[^a-z]','',s)
def lcs(a,b):
    n,m=len(a),len(b);prev=[0]*(m+1)
    for i in range(n):
        cur=[0]*(m+1)
        for j in range(m):
            cur[j+1]=max(prev[j]+1 if a[i]==b[j] else 0,prev[j+1],cur[j])
        prev=cur
    return prev[m]
def runs(a,b,L=4):
    cov=[0]*len(a);S=set(b[i:i+L] for i in range(len(b)-L+1))
    for i in range(len(a)-L+1):
        if a[i:i+L] in S:
            for j in range(i,i+L):cov[j]=1
    return sum(cov)/max(1,len(a))
m=json.load(open('scripts/align_map.json'))
m.update({'g':'g+','y':'Y','7+':'y+','7:':'y:','7^':'y^','7s':'y+s','e':'E','e^':'E^','T':'T+','To':'Tp','8o':'8p','op':'os','4':'l+','w':'w^','L:':'l:','-d':'b','L':'Lb'})
if len(sys.argv)>2 and sys.argv[2]=='fix':
    m.update({'8':'u','w':'w','L':'Lb'})
k=loadk(sys.argv[1])
toks={'K':[], 'N':[]}
seg={}
for l in open('transcription_ch1549_0930_1120_blind.txt',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    t=l.split();g=t[0][0]
    if g not in toks: continue
    for s in t[1:]:
        s=s.rstrip('?').strip('{}')
        s=m.get(s,s)
        if s.endswith('_'): continue
        toks[g].append(s)
clear={'K':'','N':''}
for l in open('clear_margins_charles.txt',encoding='utf8'):
    if l.startswith('#'): continue
    p=l.split(' ',1)
    clear['K' if p[0][0]=='M' else 'N']+=p[1]
for g in 'KN':
    c=norm(clear[g]);T=toks[g]
    dec=lambda q:''.join(norm(q[s]) if s in q else '#' for s in T)
    p=dec(k);q=p.replace('#','')
    a=lcs(q,c)/len(q);r=runs(p,c)
    keys=list(k);vals=list(k.values());R=random.Random(1);A=[];B=[]
    for i in range(200):
        v=vals[:];R.shuffle(v);x=dec(dict(zip(keys,v)));xx=x.replace('#','')
        A.append(lcs(xx,c)/max(1,len(xx)));B.append(runs(x,c))
    print(g,'signs',len(T),'with value',sum(1 for s in T if s in k),'clear letters',len(c),'LCS/decoded %.3f runs4 %.3f; shuffled LCS mean %.3f max %.3f runs mean %.3f max %.3f'%(a,r,sum(A)/200,max(A),sum(B)/200,max(B)))
