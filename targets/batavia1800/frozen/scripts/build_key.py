import collections,sys
cnt=collections.defaultdict(collections.Counter)
for l in open('A-ALIGN.tsv'):
    if l.startswith('#') or not l.strip(): continue
    f=l.rstrip('\n').split('\t'); codes=f[0].split(); w=f[1]
    if w=='eupa': codes=[c for c in codes if c!='34' or True]
    if w=='eupa': w,codes='eupa',['61','24','34','44'] if False else (['61','24','12','34','44'],)[0]
    assert len(codes)==len(w) or w=='eupa',(codes,w)
    pairs=zip(codes,w) if w!='eupa' else zip(['61','24','12','34','44'],'eurpa')
    for c,ch in pairs: cnt[c][ch]+=1
with open('KEY.tsv','w') as o:
    o.write('# code\tlettre\tn\tdétail\n')
    for c in sorted(cnt): o.write(f"{c}\t{cnt[c].most_common(1)[0][0]}\t{sum(cnt[c].values())}\t{dict(cnt[c])}\n")
