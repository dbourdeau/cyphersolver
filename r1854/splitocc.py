"""Rename occurrences of SIGN listed in an occ.py output (value==VAL) to NEWSIGN.
python splitocc.py in.txt out.txt occfile SIGN VAL NEWSIGN"""
import sys
inp,outp,occf,S,VAL,NEW=sys.argv[1:7]
idx={int(l.split()[1]) for l in open(occf,encoding='utf-8') if l.split()[2]==VAL}
out=[];i=0
for l in open(inp,encoding='utf-8'):
    if not l.startswith('L'): out.append(l); continue
    lab,r=l.split(':',1); n=[]
    for t in r.split():
        if t in ('_','?'): n.append(t); continue
        if t==S and i in idx: t=NEW
        n.append(t); i+=1
    out.append(lab+': '+' '.join(n)+'\n')
open(outp,'w',encoding='utf-8').writelines(out)
