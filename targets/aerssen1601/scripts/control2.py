"""Random-key control: permute the key's top values among the token types of a passage, decode real order."""
import sys, random
sys.path.insert(0, __import__('os').path.dirname(__file__))
from measure import load_key, blocks, look
from frscore import coverage
K=load_key(sys.argv[1]); B=blocks(sys.argv[2]); N=int(sys.argv[3]) if len(sys.argv)>3 else 2000
toks=[t for b in B for t in b['tok']]
# Preserve seeded permutation order across the qF/42 transcription relabels.
types=sorted({look(K,t) for t in toks if look(K,t) and K[look(K,t)][1]!='I'}, key=lambda t: {'qF':'q_', '42':"42'"}.get(t,t))
vals=[K[t][0][0] for t in types]
def dec(m): return ''.join(m.get(look(K,t),'') for t in toks)
real=coverage(dec(dict(zip(types,vals))))
rnd=random.Random(7); sc=[]
for i in range(N):
    v=vals[:]; rnd.shuffle(v); sc.append(coverage(dec(dict(zip(types,v)))))
sc.sort()
print(f"random-key control: real {real:.3f}; permuted keys mean {sum(sc)/N:.3f}, max {sc[-1]:.3f}; real > all: {all(real>x for x in sc)} (n={N}, {len(types)} token types)")
