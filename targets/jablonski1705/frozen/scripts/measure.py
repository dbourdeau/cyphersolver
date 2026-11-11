import json,sys,random,subprocess
def norm(s):
    s=s.lower().replace('j','i').replace('v','u').replace('w','u').replace('y','i')
    return ''.join(c for c in s if c.isalpha() or c=='?')
def lines(p):
    d={}
    for l in open(p,encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        t=l.split(); d[t[0]+' '+t[1]]=' '.join(t[2:])
    return d
def lev(a,b):
    prev=list(range(len(b)+1))
    for i,ca in enumerate(a,1):
        cur=[i]+[0]*len(b)
        for j,cb in enumerate(b,1):
            cur[j]=min(prev[j]+1,cur[j-1]+1,prev[j-1]+(ca!=cb))
        prev=cur
    return prev[-1]
key=json.load(open(sys.argv[1])); tr=sys.argv[2]; ref=lines(sys.argv[3])
def decode(k):
    out={}
    for l in open(tr,encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        t=l.split(); tag=t[0]+' '+t[1]; w=''
        for chunk in ' '.join(t[2:]).replace('|',' ').replace('F',' ').split():
            for g in chunk.split('.'):
                if not g: continue
                g=g.rstrip('?'); w+= k[g] if g in k else '?'
        out[tag]=w
    return out
def score(k):
    dec=decode(k); A=''.join(norm(dec[t]) for t in ref); B=''.join(norm(ref[t]) for t in ref)
    return 1-lev(A,B)/len(B),len(A),len(B)
s,la,lb=score(key)
rnd=random.Random(20261110); vals=list(key.values()); gs=list(key.keys()); best=0;ctl=[]
for i in range(200):
    v=vals[:]; rnd.shuffle(v); c,_,_=score(dict(zip(gs,v))); ctl.append(c); best=max(best,c)
print(f'accuracy={s:.4f} decode_chars={la} ref_chars={lb} best_control={best:.4f} mean_control={sum(ctl)/len(ctl):.4f}')
print('PASS' if s>=0.85 and s>=best+0.30 else 'FAIL')
