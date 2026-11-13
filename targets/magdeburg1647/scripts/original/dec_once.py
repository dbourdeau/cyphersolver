# dec_once.py key tx : decode cipher words with frozen key (md5 printed), word per word
import sys,hashlib
kf,tf=sys.argv[1],sys.argv[2]
print('key md5',hashlib.md5(open(kf,'rb').read()).hexdigest(),'tx md5',hashlib.md5(open(tf,'rb').read()).hexdigest())
k={}
for l in open(kf):
    if l.startswith('#'): continue
    for p in l.split(): a,b=p.split('='); k[a]=b
for l in open(tf):
    if l.startswith('#'): continue
    print(' '.join(w if w=='|' else w+'='+''.join(k.get(c,'?') for c in w) for w in l.split()))
