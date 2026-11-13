# b197 controls (vocabulary: keys/vocab_hmc_iv_v_5x.txt, words of 5+ letters seen 5+ times in the IA OCR of HMC Ormonde n.s. IV-V) for Ormond-Arran 24 Jan 1677/8. Run: python3 -I scripts/controls.py
import re, random, itertools, collections, hashlib, json, sys
import os
BASE=(sys.argv[1] if len(sys.argv)>1 else os.path.dirname(os.path.abspath(__file__))+'/..').rstrip('/')+'/'
def loadkey(f):
    d={}
    for l in open(BASE+'keys/'+f):
        n,v=l.rstrip('\n').split('\t'); d[int(n)]=[a for a in v.split('|') if a] if v else []
    return d
K1=loadkey('K1_tomokiyo_longford1.tsv'); K1c=loadkey('K1c_claim_variant.tsv'); K2=loadkey('K2_hmc_vi_xix.tsv'); K3=loadkey('K3_hmc_vii_xx.tsv')
RUNS=[[445],[342],[726,91,33,425,93,58,384,54,700,720],[732,573,526,32,643,214,55,440]]
FIGS=[x for r in RUNS for x in r]; assert len(FIGS)==20
# vocabulary: words of 5+ letters occurring 5+ times in HMC Ormonde n.s. IV-V OCR text
cnt={l.split('\t')[0]:int(l.split('\t')[1]) for l in open(BASE+'keys/vocab_hmc_iv_v_5x.txt').read().splitlines()}
VOC=set(cnt)
MAXW=max(len(w) for w in VOC)
def hits(key,figs,off):
    return sum(1 for f in figs if key.get(f+off))
def longest(key,runs,off):
    best=(0,None)
    for r in runs:
        vals=[key.get(f+off) or None for f in r]
        for i in range(len(r)):
            for j in range(i+3,len(r)+1):
                seg=vals[i:j]
                if any(v is None for v in seg): break
                for combo in itertools.product(*seg):
                    w=''.join(combo)
                    if len(w)>MAXW: continue
                    if len(w)>=5 and w in VOC and len(w)>best[0]: best=(len(w),(w,j-i))
    return best
OFFS=range(-150,151)
out={}
print('vocab size',len(VOC),'credible count',cnt['credible'])
for name,key in [('K1',K1),('K2',K2),('K3',K3),('K1c',K1c)]:
    hs={o:hits(key,FIGS,o) for o in OFFS}
    mx=max(hs.values()); top=sorted(hs.items(),key=lambda x:-x[1])[:6]
    ws={o:longest(key,RUNS,o) for o in OFFS}
    nz=[(o,w) for o,w in ws.items() if w[0]>0]
    print(f'{name}: hits at -7 = {hs[-7]}/20; at 0 = {hs[0]}/20; max {mx}; top {top}; offsets with any 5+ word: {len(nz)}/301 {nz}')
# Random figure sets, same run shape; low (<100) positions U[23,99], high U[100,850]
rng=random.Random(20261113)
def randset():
    return [[rng.randint(23,99) if f<100 else rng.randint(100,850) for f in r] for r in RUNS]
realbest=max((longest(k,RUNS,o)[0],kn,o) for kn,k in [('K1',K1),('K2',K2)] for o in OFFS)
print('real best over 2 keys x 301 offsets =',realbest)
N=2000; ge5=0; ge8=0; dist=collections.Counter(); hitmax=collections.Counter(); hit14=0
for t in range(N):
    rs=randset(); fl=[x for r in rs for x in r]
    b=max(longest(k,rs,o)[0] for k in (K1,K2) for o in OFFS)
    dist[b]+=1; ge5+= b>=5; ge8+= b>=8
    hm=max(hits(K1,fl,o) for o in OFFS); hitmax[hm]+=1; hit14+= hm>=14
print(f'random sets N={N} (decodes {N}*2*301={N*2*301}): best word length dist {sorted(dist.items())}; any 5+ word {ge5}/{N}; 8+ letters {ge8}/{N}')
print(f'random sets K1 max hits over 301 offsets dist {sorted(hitmax.items())}; >=14: {hit14}/{N}')
# Shuffles of the real 20 figures into the same run structure, offset -7, key K1
rng2=random.Random(7); S=3000; s5=0; s8=0; sd=collections.Counter()
for t in range(S):
    f=FIGS[:]; rng2.shuffle(f); rs=[f[0:1],f[1:2],f[2:12],f[12:20]]
    b=longest(K1,rs,-7)[0]; sd[b]+=1; s5+=b>=5; s8+=b>=8
print(f'shuffles N={S} at -7 K1: dist {sorted(sd.items())}; any 5+ word {s5}/{S}; 8+ letters {s8}/{S}')
