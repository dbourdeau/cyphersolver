"""Coherence of a transcription set under a key: share of deciphered chars inside dictionary words."""
import sys,os,json,glob
os.environ.setdefault('LAM','1.0'); sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))+'/..')
import word as W
key=json.load(open(sys.argv[1])); pats=sys.argv[2:] or ['ct_p*.txt']
def cov(s):
    n=len(s); best=[-1e18]*(n+1); bp=[0]*(n+1); best[0]=0
    for i in range(1,n+1):
        b=best[i-1]+W.UNK; p=i-1
        for j in range(max(0,i-W.MAXW),i):
            if best[j]<=-1e17: continue
            lp=W.VOC.get(s[j:i])
            if lp is not None and best[j]+lp-W.BCOST>b: b,p=best[j]+lp-W.BCOST,j
        best[i]=b; bp[i]=p
    c=0;i=n
    while i>0:
        j=bp[i]
        if s[j:i] in W.VOC: c+=i-j
        i=j
    return c
files=[]
for p in pats: files+=sorted(glob.glob(p))
T=C=0
for fn in files:
    t=c=0
    for line in open(fn,encoding='utf-8',errors='replace'):
        if line.startswith('#') or '|' not in line: continue
        p=[x.strip() for x in line.split('|')]
        if len(p)<3: continue
        for field in p[2::2]:
            seg=[]
            for tok in field.replace('/',' ').split():
                tok=tok.rstrip('?')
                if tok in (':','.','..',':2',':3',':4','::'):
                    seg.append('DOT'); continue
                if not tok or tok.startswith('#') or tok=='-':
                    if seg:
                        s=''.join(key.get(x,'?') for x in seg); t+=len(s); c+=cov(s); seg=[]
                    continue
                seg.append(tok.split('/')[0])
            if seg:
                s=''.join(key.get(x,'?') for x in seg); t+=len(s); c+=cov(s)
    print(f'{fn:14s} {t:5d} chars  {c/max(t,1):.3f}')
    T+=t; C+=c
print(f'{"TOTAL":14s} {T:5d} chars  {C/max(T,1):.3f}')
