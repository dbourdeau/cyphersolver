import re,random,collections
k={}
for l in open('keys/R4366_filled_cells.tsv',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a,b=l.rstrip('\n').split('\t'); k[int(a)]=b
lines=[[int(x) for x in l.split()] for l in open('transcription/fig6_moscow_1744-10-05.txt',encoding='utf-8') if l.strip() and not l.startswith('#')]
ct=[g for L in lines for g in L]
rng=range(55,951)
fill=sum(v in k for v in rng)/len(rng)
inr=[g for g in ct if 55<=g<=950]; hit=sum(g in k for g in inr)
print(f'key cells 55-950: {len(k)} filled of {len(rng)} = {fill:.3f}')
print(f'sample groups in 55-950: {len(inr)}, on filled cell {hit} = {hit/len(inr):.3f}; groups above 950: {sum(g>950 for g in ct)}, of which above 1075: {sum(g>1075 for g in ct)}')
d=sorted(set(inr)); hd=sum(g in k for g in d); print(f'distinct {len(d)} filled {hd} = {hd/len(d):.3f}')
from math import comb
p=sum(comb(len(d),i)*fill**i*(1-fill)**(len(d)-i) for i in range(hd,len(d)+1)); print('binomial P(distinct filled >= observed)',round(p,4))
for L in lines: print(' '.join(k[g].replace(' ','_') if g in k else ('·' if g<=950 else str(g)) for g in L))
