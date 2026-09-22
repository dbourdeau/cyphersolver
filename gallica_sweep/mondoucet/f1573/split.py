# usage: split.py in.txt patterns.txt out.txt ; patterns lines "LAB: aαa" (sequence for each 'a' token in the line)
import sys
pat={}
for l in open(sys.argv[2],encoding='utf-8'):
    if ':' in l and not l.startswith('#'):
        a,b=l.split(':',1); pat[a.strip()]=b.strip()
out=[]
for l in open(sys.argv[1],encoding='utf-8'):
    if l.startswith('#') or ':' not in l: out.append(l); continue
    lab,rest=l.split(':',1); lab=lab.strip()
    toks=rest.split(); n=toks.count('a'); p=pat.get(lab,'')
    if n and len(p)!=n: print('MISMATCH',lab,n,p); 
    it=iter(p); toks=[(next(it,'a') if t=='a' else t) for t in toks]
    out.append('%s: %s\n'%(lab,' '.join(toks)))
open(sys.argv[3],'w',encoding='utf-8').writelines(out)
