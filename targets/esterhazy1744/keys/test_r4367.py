k={}
for l in open('keys/R4367_sample_lookup.tsv',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a,b=(l.rstrip('\n').split('\t')+[''])[:2]; k[int(a)]=b
lines=[[int(x) for x in l.split()] for l in open('transcription/fig6_moscow_1744-10-05.txt',encoding='utf-8') if l.strip() and not l.startswith('#')]
ct=[g for L in lines for g in L]
miss=[g for g in set(ct) if g<3000 and g not in k]; print('missing lookups',miss)
lo=[g for g in ct if g<3000]
print('groups under 3000',len(lo),'on filled cell',sum(bool(k[g]) for g in lo))
print('groups 3xxx, outside the table',sum(g>=3000 for g in ct))
print('P(no group in 1738-2198 | uniform 1-2198, n=%d) = %.1e'%(len(lo),(1737/2198)**len(lo)))
for L in lines: print(' '.join((k[g].replace(' ','_') or '·') if g in k else str(g) for g in L))
