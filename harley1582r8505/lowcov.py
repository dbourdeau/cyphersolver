import os,json,glob,sys
os.environ['LAM']='1.0'; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
import word as W
key=json.load(open('key_w3.json'))
def cov(s):
    n=len(s); best=[-1e18]*(n+1); bp=[0]*(n+1); best[0]=0
    for i in range(1,n+1):
        b=best[i-1]+W.UNK; pp=i-1
        for j in range(max(0,i-W.MAXW),i):
            if best[j]<=-1e17: continue
            lp=W.VOC.get(s[j:i])
            if lp is not None and best[j]+lp-W.BCOST>b: b,pp=best[j]+lp-W.BCOST,j
        best[i]=b; bp[i]=pp
    c=0; i=n
    while i>0:
        j=bp[i]
        if s[j:i] in W.VOC: c+=i-j
        i=j
    return c
rows=[]
for fn in sorted(glob.glob('ct_p*.txt')):
    for line in open(fn,encoding='utf-8'):
        if line.startswith('#') or '|' not in line: continue
        p=[x.strip() for x in line.split('|')]
        if len(p)<3: continue
        sg=[]
        for field in p[2::2]:
            for t in field.replace('/',' ').split():
                t=t.rstrip('?')
                if t and t!=':' and not t.startswith('#') and t not in ('.','..','-'): sg.append(t.split('/')[0])
        if len(sg)<8: continue
        s=''.join(key.get(x,'?') for x in sg)
        rows.append((cov(s)/len(s), len(s), p[0]))
rows.sort()
for r in rows[:22]: print(f'{r[0]:.2f} {r[1]:4d} {r[2]}')
