"""ledger.py KEY TX OVERRIDES OUT.tsv -- strict S/E/N ledger per PARSER.md section 5. Prints totals per page-group and overall."""
import sys,collections,importlib.util
spec=importlib.util.spec_from_file_location('dec','/home/claude/en/trackB/b70_selvatico_read/scripts/dec.py');dec=importlib.util.module_from_spec(spec);spec.loader.exec_module(dec)
key,tx,ov,outp=sys.argv[1:5]
O={}
for l in open(ov,encoding='utf-8'):
    f=l.rstrip('\n').split('\t')
    if f[0]!='line' and len(f)>=3: O[(f[0],int(f[1]))]=f[2]
LET={'21r':'10Jun','21v':'10Jun','25r':'29Jul','25v':'29Jul','35r':'08Aug','35v':'08Aug','36r':'08Aug','36v':'08Aug','23r':'12Aug','23v':'12Aug'}
T=collections.defaultdict(collections.Counter); T2=collections.defaultdict(collections.Counter); used=set()
out=open(outp,'w',encoding='utf-8'); out.write('letter\tline\tidx\traw\tcanon\tclass\tvalue\tflags\tmark\treason\n')
for lid,items in dec.run(key,tx):
    let=LET.get(lid.split('.')[0],'other')
    for k,o in items:
        if k!='unit': continue
        m=o['mark']; why=''
        if o['cls']=='X': why='struck by writer'
        elif o['cls']=='ILL': why='illegible'
        elif o['cls']=='CODE': why='code'
        elif o['cls']=='UNK': why='unkeyed'
        elif o['flags']&{'D','C','ALT'}: why='transcription doubt'
        if (lid,o['idx']) in O:
            used.add((lid,o['idx']))
            if m=='S': m='E'; why=O[(lid,o['idx'])]
            else: why+='; '+O[(lid,o['idx'])]
        T[let][m]+=1
        m2=m
        if o['cls']=='CODE' and '=' in o['val'] and not (o['flags']&{'D','C','ALT'}): m2='S'
        T2[let][m2]+=1
        out.write('\t'.join([let,lid,str(o['idx']),o['raw'],o['canon'] or '',o['cls'],o['val'],''.join(sorted(o['flags'])),m,why])+'\n')
miss=set(O)-used
if miss: print('UNUSED OVERRIDES',sorted(miss))
def show(name,c,c2):
    d=c['S']+c['E']+c['N']
    if d: print(f"{name}: S {c['S']} + E {c['E']} + N {c['N']} = {d}; strict {c['S']}/{d} = {100*c['S']/d:.2f}% | struck excluded {c['X']} | codes-with-K3-value-as-S: {c2['S']}/{d} = {100*c2['S']/d:.2f}%")
tot=collections.Counter(); tot2=collections.Counter()
for let in sorted(T): show(let,T[let],T2[let]); tot+=T[let]; tot2+=T2[let]
show('ALL',tot,tot2)
