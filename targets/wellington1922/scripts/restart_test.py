"""Post hoc restart-rule test ("Test R" of our work plan PLAN_diaz_gaps.md, SHA-256 c17933f51479..., 23 Nov 2026, not
committed): may the 3-1-3 cycle restart at a word start inside an unread stretch? 1,000 shuffles of each stretch's
signs as controls; pass = coverage by dictionary words >= 0.8 and above the controls' 99th percentile.
The word list is the clear text of the Epistolario de Francisco I. Madero, t. II (Internet Archive item
afim-epistolario-t-2, its _djvu.txt; not committed, all rights reserved) plus the words already read in this letter,
so the stretches marked "seen" are not blind tests.
python3 -I targets/wellington1922/scripts/restart_test.py <AFIM_Epistolario_T2_djvu.txt>   (output: restart_test.txt)"""
import sys,os,unicodedata,collections,random,re
sys.stdout.reconfigure(encoding='utf-8')
A='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
K=[3,1,3]
def dec(s,ph=0): return ''.join(A[(A.index(c)-K[(i+ph)%3])%27] for i,c in enumerate(s))
def fold(t):
    o=[]
    for ch in t.upper():
        if ch=='Ñ': o.append(ch); continue
        d=unicodedata.normalize('NFD',ch)[0]
        o.append(d if d in A else ' ')
    return ''.join(o)
C=sys.argv[1]
cnt=collections.Counter(fold(open(C,encoding='utf-8').read()).split())
V={w for w,n in cnt.items() if len(w)>=2 and n>=3}|{'Y','A','O','E'}
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+os.sep
for l in open(W+'marked_DCXXI.6.588.1.txt',encoding='utf-8'):
    if l.startswith('#') or '\t' not in l: continue
    for w in re.sub(r'\{[^}]*\}|\[[^\]]*\]','',l.split('\t')[1]).replace('|','').split():
        if len(w)>=2: V.add(w)
ML=max(map(len,V))
def cov(s):
    n=len(s); best=[0]*(n+1)
    for i in range(1,n+1):
        best[i]=best[i-1]
        for L in range(1,min(ML,i)+1):
            if s[i-L:i] in V: best[i]=max(best[i],best[i-L]+L)
    return best[n]/n if n else 0
def seg(s):
    n=len(s); best=[(0,'')]*(n+1)
    for i in range(1,n+1):
        best[i]=(best[i-1][0],best[i-1][1]+s[i-1].lower())
        for L in range(1,min(ML,i)+1):
            if s[i-L:i] in V and best[i-L][0]+L>best[i][0]: best[i]=(best[i-L][0]+L,best[i-L][1]+' '+s[i-L:i]+' ')
    return ' '.join(best[n][1].split())
def best_restart(sig, start_ph):
    """sig: the stretch's signs; start_ph: key position of its first sign under the registered decode.
    Options: no change, or restart (key position 0) at any sign k>=0."""
    opts=[(cov(dec(sig,start_ph)),-1,dec(sig,start_ph))]
    for k in range(len(sig)):
        d=dec(sig[:k],start_ph)+dec(sig[k:],0)
        opts.append((cov(d),k,d))
    return max(opts)
T={}
for l in open(W+'transcription_DCXXI.6.588.1.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    r,_,_,s=l.rstrip('\n').split('\t'); T[r]=s.replace('/','').replace('?','Ñ')
# stretches: (name, run, first sign 1-based, last sign or None)
ST=[('a f3.07 tail','f3.07',10,None),('b f3.22 tail','f3.22',10,None),('c f3.20 after BONILLA','f3.20',21,None),
    ('seen f2.19 tail','f2.19',17,None),('seen f3.10 tail','f3.10',11,None),('seen f3.13 (alone)','f3.13',1,None)]
random.seed(20261123)
print('vocabulary size',len(V))
for name,r,a,b in ST:
    sig=T[r][a-1:b]; ph=(a-1)%3
    if name.startswith('c'):  # registered restart at BONILLA (index 20) is the post hoc one; rule R allows one more restart after it
        sig=T[r][20:]; ph=0
    c,k,d=best_restart(sig,ph)
    ctl=[]
    for _ in range(1000):
        s=list(sig); random.shuffle(s); ctl.append(best_restart(''.join(s),ph)[0])
    ctl.sort(); p99=ctl[989]
    print(f'{name}: {len(sig)} signs; best coverage {c:.2f} (restart at sign {a+k if k>=0 else "none"}); control 99th pct {p99:.2f}, max {ctl[-1]:.2f}; pass={c>=0.8 and c>p99}')
    print('   ',d,'|',seg(d))
# f3.13 as continuation of f3.12 (130 letters)
d=dec(T['f3.13'],len(T['f3.12'])%3); print('f3.13 continuing f3.12:',seg(d), f'{cov(d):.2f}')
