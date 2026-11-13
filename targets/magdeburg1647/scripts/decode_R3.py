"""decode.py KEY TX : decode every cipher word (rows not starting '#') with the frozen key; '|' = name sign kept; letters not in key -> '?'."""
import sys,re
k={}
for l in open(sys.argv[1]):
    if l.startswith('#'): continue
    for p in l.split(): x,y=p.split('='); k[x]=y
n=0
for l in open(sys.argv[2]):
    l=l.rstrip('\n')
    if l.startswith('#'): print(l); continue
    out=[]
    for w in l.split():
        if w=='|': out.append('|'); continue
        n+=1; out.append(''.join(k.get(c,'?') for c in w))
    print(' '.join(out))
print('# cipher words decoded:',n)
