import sys,random
sys.path.insert(0,'cyphersolver')
from lang import lm
N=int(sys.argv[1]); seed=int(sys.argv[2]) if len(sys.argv)>2 else 1
t=lm.norm(open('cyphersolver/lang/corpora/la-gutenberg.txt',errors='ignore').read(),'latin',spaces=False)
rng=random.Random(seed); st=rng.randrange(len(t)//2,len(t)-N); pt=t[st:st+N]
homs={'e':4,'i':4,'a':3,'u':3,'t':3,'s':3,'o':2,'n':2,'r':2,'m':2,'c':2,'l':1,'p':1,'d':1,'q':1,'b':1,'f':1,'g':1,'h':1,'x':1,'z':1}
signs={ch:[f'{ch.upper()}{i}' for i in range(n)] for ch,n in homs.items()}
open('ctl_pt.txt','w').write(pt); open('ctl_ct.txt','w').write(' '.join(rng.choice(signs[ch]) for ch in pt))
