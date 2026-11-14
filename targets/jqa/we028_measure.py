"""Held-out check of the M97 roll 13 code sheet (Weber WE028) against the clerk interlinear decodes of JQA despatches (clerk_*.tsv, grade H). Prereg frozen 14 Nov 2026 before the run (SHA-256 of key CSV 2ece5836...cd4d00c, of this script before this docstring b5e17515...7f9f69).
Usage: python we028_measure.py ../morris1813/beling/key/codebook_M97_13_transcription.csv .
Threshold written beforehand: agreement >= 0.80 and >= best of 200 shuffled keys + 0.30."""
import csv,glob,random,sys,hashlib
key,clerkdir=sys.argv[1],sys.argv[2]
wb={}
for r in csv.DictReader(open(key)):
    wb[int(r['code_number'])]=[r['reading'],r['numerical_sheet_1057_first_reading'],r['alphabetical_sheet_1056_reading_where_read']]
def n(s): return s.lower().replace('?','').replace(' ','').replace('.','').strip()
pairs=[]
for f in sorted(glob.glob(clerkdir+'/clerk_*.tsv')):
    for l in open(f,encoding='utf8'):
        p=l.rstrip('\n').split('\t')
        if l.startswith('#') or len(p)<4 or not p[0].isdigit() or p[3].strip()!='H': continue
        pairs.append((int(p[0]),n(p[1])))
def ok(v,vals):
    vals=[n(x) for x in vals if n(x)]
    return any(v==x or (len(v)>=2 and len(x)>=2 and (v.startswith(x) or x.startswith(v))) for x in vals)
def score(table): return sum(ok(v,table.get(k,[])) for k,v in pairs)/len(pairs)
real=score(wb)
rng=random.Random(20261114); ks=sorted(wb); vs=[wb[k] for k in ks]; nulls=[]
for _ in range(200):
    rng.shuffle(vs); nulls.append(score(dict(zip(ks,vs))))
nulls.sort()
print(f'pairs {len(pairs)}; agreement {real:.3f}; null max {nulls[-1]:.3f}, p99 {nulls[197]:.3f}, mean {sum(nulls)/200:.3f}')
print('PASS' if real>=0.80 and real>=nulls[-1]+0.30 else 'FAIL')
