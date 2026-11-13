"""reading.py KEY TX LEDGER : print the reading with holes. S and S? units as decoded, E units as [...], name signs as [sign], clear rows in {braces} as transcribed."""
import sys
k={}
for l in open(sys.argv[1]):
    if l.startswith('#'): continue
    for p in l.split(): x,y=p.split('='); k[x]=y
L=[r.split('\t') for r in open(sys.argv[3]).read().split('\n') if r.startswith('L')]
i=0; n=0; first=True
for l in open(sys.argv[2]):
    l=l.rstrip('\n')
    if l.startswith('#'):
        if l.startswith('# {') or l.startswith('# (') or l.startswith('# |') or l.startswith('# :'): print('  '+l[2:])
        continue
    n+=1; out=[]
    for w in l.split():
        if w=='|': out.append('[sign]'); continue
        r=L[i]; i+=1; assert r[1]==w
        out.append(r[2] if r[3] in('S','S?') else '[...]')
    print('%d  %s'%(n,' '.join(out)))
