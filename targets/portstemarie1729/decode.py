import csv,collections,sys
# Strict count (12 Nov 2026): only values glossed in the sibling letters (pairs_A.tsv, pairs_B.tsv) count as read.
# pairs_zinf.tsv holds values inferred from the sense and the alphabetical order; they print as [?value] and are holes.
def load(files):
    K=collections.defaultdict(collections.Counter)
    for f in files:
        for r in csv.reader(open(f,encoding='utf8'),delimiter='\t'):
            if len(r)<4 or not r[2].strip().isdigit(): continue
            p=r[3].strip()
            if p and p!='?': K[r[2].strip()][p]+=1
    return K
K=load(['pairs_A.tsv','pairs_B.tsv'])
Z=load(['pairs_zinf.tsv'])
out=[];hit=inf=tot=0
for line in open('ct_p5.txt'):
    w=[]
    for c in line.split():
        tot+=1
        if c in K: hit+=1; w.append(K[c].most_common(1)[0][0]+('' if len(K[c])==1 else '*'))
        elif c in Z and c!='1250': inf+=1; w.append('[?'+Z[c].most_common(1)[0][0]+']')
        elif c in Z: inf+=1; w.append('[1250 separator?]')
        else: w.append('['+c+']')
    out.append(' '.join(w))
print('\n'.join(out)); print(f'{hit}/{tot} groups directly valued; {inf} more inferred from context [?]; {tot-hit-inf} unvalued; key size {len(K)} glossed values')
