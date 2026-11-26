"""Keep both original readings and every unresolved numerical position."""
from pathlib import Path
import csv,re
from collections import Counter
p=Path(__file__).resolve().parent
root=p.parents[1]
notes23={'A02.02','A03.01','A04.04','A06.01','A06.13','A08.06','B03.08','B10.02','B11.01','B16.16','C01.10','C01.13','C02.17','C05.05','C05.11','C06.10','C10.02','C10.18','C11.08','C13.17','D01.09','D01.11','A10.04'}
notes26={'H1.04.09','H1.04.10','H1.05.05','H1.06.05','H1.07.03','H1.10.10','H1.12.15','H2.01.01','H2.01.03','H2.01.04','H2.02.10','H2.03.09','H2.04.13','H2.05.02','H2.05.03','H2.05.10','H2.07.09','H2.07.11','H2.08.05','H2.08.08','H2.09.05','H2.09.11','H2.10.13','H2.11.03'}
def read(no,reader):
    output={}
    section=None
    for line in (root/f'vienna{no}_{reader}.txt').read_text().splitlines():
        m=(re.fullmatch(r'([a-dA-D])(\d+) (.*)',line) if no==23 else re.fullmatch(r'(END23|H1|H2)\.(\d+) (.*)',line))
        if no==26 and reader=='a':
            s=re.match(r'^(end23|h1|h2) \(',line)
            if s: section=s[1].upper()
            k=re.fullmatch(r'(\d+) (.*)',line)
            m=(None,section,k[1],k[2]) if k else None
        if not m: continue
        page=m[1].upper()
        if no==23 and page=='D':continue
        row=(page if no==23 else page+'.')+m[2].zfill(2)
        words=[]
        for tok in m[3].split():
            if tok=='—': words[-1]+='~'
            else:
                tok=tok.replace('^','')
                if tok.isdigit():tok+='_'
                words.append(tok)
        output[row]=words
    return output
for no in [23,26]:
    a,b=[read(no,r) for r in ['a','b']]
    if no==23:
        a['D01']=read(26,'a')['END23.01'];b['D01']=read(26,'b')['END23.01']
    else: del a['END23.01'],b['END23.01']
    assert list(a)==list(b)
    rows=[]
    for line in a:
        assert len(a[line])==len(b[line]),line
        for i,(u,v) in enumerate(zip(a[line],b[line]),1):
            loc=line+'.'+str(i).zfill(2)
            reasons=[]
            if u!=v:reasons.append('readers differ')
            if loc in (notes23 if no==23 else notes26):reasons.append('position-specific qualification')
            rows.append([len(rows)+1,loc,u,v,'?' if reasons else u,', '.join(reasons)])
    with (p/f'groups{no}.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['ordinal','position','reader_a','reader_b','strict','qualification']);w.writerows(rows)
    print(no,len(rows),sum(r[4]!='?' for r in rows))
