import sys,json,random,itertools; sys.path.insert(0,'scripts'); from common import *
key=json.load(open(f'{W}/key.json'))['map']
V=set(vocab())
H=[w for w in load_words(f'{W}/H_21_0001.txt') if all(t.isdigit() and int(t)<100 for t in w)]
def ok_strict(s): return s in ('a','i') if len(s)==1 else s in V
def variants(s):
    opts=[('u','v') if c=='u' else ('i','j') if c=='i' else (c,) for c in s]
    for p in itertools.product(*opts): yield ''.join(p)
def ok_norm(s): return s in ('a','i') if len(s)==1 else any(v in V for v in variants(s))
def score(m,f):
    return sum(f(''.join(m.get(t,'?') for t in w)) for w in H)/len(H)
S=score(key,ok_strict); Sn=score(key,ok_norm)
random.seed(1808); nums=sorted(key,key=int); vals=[key[k] for k in nums]
C=[];Cn=[]
for _ in range(200):
    v=vals[:]; random.shuffle(v); m=dict(zip(nums,v))
    C.append(score(m,ok_strict)); Cn.append(score(m,ok_norm))
print('H counted words',len(H))
print('BINDING  S=%.4f  max control=%.4f  pass=%s'%(S,max(C),S>=0.85 and S>=max(C)+0.30))
print('EXPLORATORY normalized S=%.4f  max control=%.4f'%(Sn,max(Cn)))
for w in H:
    s=''.join(key.get(t,'?') for t in w); print(s, '' if ok_strict(s) else ('(norm ok)' if ok_norm(s) else '  <-- not in V'))
