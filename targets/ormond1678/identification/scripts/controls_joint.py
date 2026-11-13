# Supplementary: same 2,000 random sets (same seed and generator order) scored on K1 alone and jointly
import random, collections, sys
sys.path.insert(0,'/nonexistent')
exec(open(__import__('os').path.dirname(__import__('os').path.abspath(__file__))+'/controls.py').read().split('OFFS=range')[0])
OFFS=range(-150,151)
rng=random.Random(20261113)
def randset():
    return [[rng.randint(23,99) if f<100 else rng.randint(100,850) for f in r] for r in RUNS]
N=2000; k1w8=0; k1w5=0; joint=0
for t in range(N):
    rs=randset(); fl=[x for r in rs for x in r]
    per={o:(hits(K1,fl,o),longest(K1,rs,o)[0]) for o in OFFS}
    b=max(w for h,w in per.values()); k1w5+=b>=5; k1w8+=b>=8
    if any(h>=14 and w>=8 for h,w in per.values()): joint+=1
print(f'K1 only, N={N}x301: any 5+ word {k1w5}/{N}; 8+ letters {k1w8}/{N}; same offset >=14 hits AND 8+ letter word: {joint}/{N}')
