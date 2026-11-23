from pathlib import Path
p=Path(__file__).resolve().parent
first=p.parent/'modena/other_blind'
second=p.parent/'new_sources/other_blind/reading.txt'
btext=second.read_text()
def form(s):
 return [x.split() for x in s.strip().splitlines() if x.strip() and x.strip()!='|']
b=[form(btext.split('0001\n')[1].split('\n0002')[0]),form(btext.split('0002\n')[1].split('\nAmbiguity notes')[0])]
a=[form((first/f'page{i}.txt').read_text()) for i in [1,2]]
out=[];align=['page\tline\tposition\tvisual1\tvisual2\tagreed\treason']
for page,(rows1,rows2) in enumerate(zip(a,b),1):
 assert len(rows1)==len(rows2)
 for line,(r,s) in enumerate(zip(rows1,rows2),1):
  assert len(r)==len(s)
  pos=0
  for token1,token2 in zip(r,s):
   if token1=='|':
    assert token2=='|';out.append('|');continue
   pos+=1
   ok=token1==token2 and token1.isdigit()
   reason='agreement' if ok else 'different or unreadable'
   if (page,line,pos) in [(1,10,10),(2,3,2)]:
    ok=False;reason='second reader flags clipped 5 or 40/140 ambiguity'
   ag=token1 if ok else '?'
   out.append(ag)
   align.append(f'{page}\t{line}\t{pos}\t{token1}\t{token2}\t{ag}\t{reason}')
(p/'oct15_boundaries.tsv').write_text('\n'.join(align)+'\n')
(p/'oct15.runs').write_text('\n'.join(' '.join(run.split()) for run in ' '.join(out).split('|') if run.strip())+'\n')
