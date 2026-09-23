import sys,os,json,glob,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
os.environ.setdefault('LAM','1.0')
import word as W
key=json.load(open(sys.argv[1]))
def segment(s):
    n=len(s); best=[-1e18]*(n+1); bp=[0]*(n+1); best[0]=0
    for i in range(1,n+1):
        b=best[i-1]+W.UNK; p=i-1
        for j in range(max(0,i-W.MAXW),i):
            if best[j]<=-1e17: continue
            lp=W.VOC.get(s[j:i])
            if lp is not None:
                v=best[j]+lp-W.BCOST
                if v>b: b,p=v,j
        best[i]=b; bp[i]=p
    out=[]; i=n
    while i>0:
        j=bp[i]; w=s[j:i]; out.append(w if w in W.VOC else w.upper()); i=j
    return ' '.join(reversed(out))
tot=cov=0
lines=[]
for fn in sorted(glob.glob(os.environ.get('CT','ct_p*.txt'))):
    for line in open(fn,encoding='utf-8',errors='replace'):
        if line.startswith('#') or '|' not in line: continue
        p=[x.strip() for x in line.split('|')]
        if len(p)<3: continue
        parts=[]
        for field in p[2::2]:
            seg=[]
            for t in field.replace('/',' ').split():
                t=t.rstrip('?')
                if t in (':','.','..',':2',':3',':4','::'):
                    seg.append('DOT'); continue
                if not t or t=='-':
                    if seg: parts.append(('c',seg)); seg=[]
                    continue
                if t.startswith('#'): 
                    if seg: parts.append(('c',seg)); seg=[]
                    parts.append(('n',t)); continue
                seg.append(t.split('/')[0])
            if seg: parts.append(('c',seg))
        out=[]
        for kind,v in parts:
            if kind=='n': out.append(f'[{v}]')
            else:
                s=''.join(key.get(x,'?') for x in v)
                tot+=len(s)
                seg=segment(s)
                cov+=sum(len(w) for w in seg.split() if not w.isupper())
                out.append(seg)
        lines.append(f'{p[0]:6s} <{p[1][:40]}>  ' + ' | '.join(out) + f'  <{p[-1][:40]}>')
open('reading.txt','w',encoding='utf-8').write('\n'.join(lines)+'\n')
print('cipher chars',tot,'in dictionary words',cov, f'{cov/tot:.3f}')
