# synthetic ASAC ciphertext with MSVC rand() homophones. usage: mksyn.py mode(2|3|4|5) L1 L2 seed out [nchars]
import sys,random
from asac import *
from randtest import msvc
mode=int(sys.argv[1]); L1=int(sys.argv[2]); L2=int(sys.argv[3]); seed=int(sys.argv[4]); out=sys.argv[5]; nch=int(sys.argv[6]) if len(sys.argv)>6 else 1451
random.seed(seed)
t=open('../de_clean.txt').read(); st=random.randrange(len(t)-8000); pt=' '.join(t[st:st+6000].split())[:nch]
key=[random.randrange(10) for _ in range(40)]
sq=square(key[:10],key[10:20])
g=msvc(); cells=[]
for c in pt:
    r=next(g)%100; m=0
    while sq[(r+m)%100]!=c: m+=1
    i=(r+m)%100; cells.append(str(i%10)+str(i//10))
s=''.join(cells)
kst=prng(key[20:30],key[30:40])
if mode==5:
    blocks=[kst]; cur=[str(x) for x in kst]
    kk=[]; data=[str(x) for x in transpose(init_rng(),key[20:30],key[30:40])]
    out_s=[]
    for n,ch in enumerate(s):
        out_s.append(str((int(ch)+int(data[n%100]))%10))
        if n%100==99: data=transpose(data,key[20:30],key[30:40])
    s=''.join(out_s)
else: s=add_prng(s,kst)
o1=list(range(L1)); random.shuffle(o1)
if mode>=3: s=trans_enc(s,o1)
o2=list(range(L2)); random.shuffle(o2)
if mode==4: s=trans_enc(s,o2)
open(out,'w').write(s)
v=[(-kst_y)%10 for kst_y in key[30:40]]
open(out+'.key','w').write('key '+''.join(map(str,key))+'\nv '+''.join(str((-x)%10) for x in key[30:40])+' px '+''.join(str(key[20+x]) for x in (1,3,5,7,9))+'\norder1 '+' '.join(map(str,o1))+'\norder2 '+' '.join(map(str,o2))+'\n'+pt+'\n')
print(len(s),pt[:60])
