"""Shuffle control: permute the plain values among the cipher letters in use (one class: all are letters),
5,000 keys per seed, same language model (la-letters, order 5, spaces), real key vs shuffles."""
import sys, re, random, statistics
sys.path.insert(0, '/home/claude/keyless/_cs')
from lang import lm
D='/home/claude/keyless/cpp10a132/'
key={}
for ln in open(D+'KEY.tsv').read().splitlines()[1:]:
    c,p,_=ln.split('\t')
    if len(c)==1: key[c]=p
def text(pages):
    ws=[]
    for ln in open(D+'TRANSCRIPTION.tsv').read().splitlines()[1:]:
        p,l,t=ln.split('\t')
        if p not in pages: continue
        t=re.sub(r'\{[^}]*\}',' ',t); t=re.sub(r'<S\d\d>|\[\.+\]|\?','',t); t=re.sub(r'[./]',' ',t).lower()
        ws+=t.split()
    return ' '.join(ws)
M=lm.load('la-letters')
def sc(ct,k): return M.per_char(lm.norm(''.join(k.get(c,' ') for c in ct),'latin'))
for name,pages in (('FULL',{'p75r','p76r','p76v'}),('HELD-OUT p76v',{'p76v'}),('TRAIN',{'p75r','p76r'})):
    ct=text(pages); used=sorted(set(ct)-{' '}); real=sc(ct,key)
    for seed in (20261112,7):
        rnd=random.Random(seed); vals=[key[c] for c in used]; ss=[]
        for i in range(5000):
            v=vals[:]; rnd.shuffle(v); ss.append(sc(ct,dict(zip(used,v))))
        mu=statistics.mean(ss); sd=statistics.pstdev(ss); beat=sum(s>=real for s in ss)
        print(f'{name:14s} seed {seed:<9d} letters-in-use {len(used)}  real {real:.3f}  shuffles mean {mu:.3f} sd {sd:.3f} best {max(ss):.3f}  z {(real-mu)/sd:.1f}  shuffles>=real {beat}/5000')
