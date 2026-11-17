"""lookup.py <table.tsv> <page_offset leaf=page-offset> <groups file or comma list> : show line and neighbours."""
import csv,sys
csv.field_size_limit(10**8)
T={}
for r in csv.reader(open(sys.argv[1],encoding='utf8'),delimiter='\t'):
    k=(int(r[0]),r[2],int(r[3])); T[k]=(T[k]+' ¦ ' if k in T else '')+r[5]
off=int(sys.argv[2])
src=sys.argv[3]
items=[l.rstrip('\n').split('\t') for l in open(src)][1:] if src.endswith('.tsv') else [[g,''] for g in src.split(',')]
for r in items:
    g=r[0];p=int(g[:3]);c=g[3];l=int(g[4:6])
    leaf=p-off
    ctx=[T.get((leaf,c,l+d),'-')[:30] for d in (-1,0,1)]
    print(f"{g} {r[1]:15.15s}| {ctx[1]:30s}| -1 {ctx[0]:22.22s}| +1 {ctx[2]:22.22s}")
