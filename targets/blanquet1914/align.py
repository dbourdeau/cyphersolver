from pathlib import Path
p=Path(__file__).resolve().parent
items={'march25':['pres17.txt'],'may19':['DLXXIII.2.41.22-41.0001.txt','DLXXIII.2.41.22-41.0002.txt']}
for label,names in items.items():
    ledger=['page\tline\tgroup\treader1\treader2\tconsensus']; sequence=[]
    for page,name in enumerate(names,1):
        # The May page-one lower edge clips part of the final line. No adjacency across that edge.
        if page>1:sequence.append('|')
        one=(p/'read_one'/name).read_text().splitlines();two=(p/'read_two'/name).read_text().splitlines()
        assert len(one)==len(two)
        for line,(r,s) in enumerate(zip(one,two),1):
            if (label,page,line) in [('march25',1,6),('march25',1,7),('may19',2,3)]: sequence.append('|')
            def parse(row):
                tokens=[];breaks=set()
                for tok in row.split():
                    if tok=='|':breaks.add(len(tokens))
                    else:tokens.append(tok)
                return tokens,breaks
            a,ba=parse(r);b,bb=parse(s)
            assert len(a)==len(b)
            breaks=ba|bb
            for ix,(left,right) in enumerate(zip(a,b)):
                if ix in breaks:sequence.append('|')
                v=left if left==right and left.isdigit() else '?'
                ledger.append(f'{page}\t{line}\t{ix+1}\t{left}\t{right}\t{v}')
                sequence.append(v)
            if len(a) in breaks: sequence.append('|')
    (p/(label+'.runs')).write_text('\n'.join(' '.join(run.split()) for run in ' '.join(sequence).split('|') if run.strip())+'\n')
    (p/(label+'.alignment.tsv')).write_text('\n'.join(ledger)+'\n')
