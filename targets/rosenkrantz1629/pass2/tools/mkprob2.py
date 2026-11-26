"""mkprob2.py tx.tsv out_prefix letters [thresh=200]
Segments break only at clear text and unreadable tokens. Values < thresh: letter symbols (candidates a-z).
Values >= thresh: symbols whose candidates are a-z or '|' (word code = word break, decided by the solver).
Writes .prob .cands .segs .freq .rc (row/col on the 9-column grid for values < thresh; -1 for the rest)."""
import sys; sys.path.insert(0,'/home/claude/keyless/rosenkrantz1629/pass2/tools')
from numlib import load
import numpy as np
tx,pre,lets=sys.argv[1],sys.argv[2],set(sys.argv[3].split(','))
thr=int(sys.argv[4]) if len(sys.argv)>4 else 200
rows=load(tx); segs=[]; cur=[]; info=None
def flush():
    global cur
    if cur: segs.append((cur,info))
    cur=[]
for let,img,ln,items in rows:
    if let not in lets: continue
    for it in items:
        if it[0]=='n' and isinstance(it[1],int) and not it[2]:
            if not cur: info=f'{let}:{img}:{ln}'
            cur.append(it[1])
        elif it[0]=='n' and isinstance(it[1],int) and it[2]:   # doubtful digit: keep as its own symbol
            if not cur: info=f'{let}:{img}:{ln}'
            cur.append(it[1])
        elif it[0]=='n': flush()           # unreadable
        elif it[0]=='c': flush()
flush()
syms=sorted({t for s,_ in segs for t in s}); ix={t:i for i,t in enumerate(syms)}
cands=list('abcdefghijklmnopqrstuvwxyz')+['|']
open(pre+'.cands','w').write('\n'.join(cands)+'\n')
with open(pre+'.prob','w') as f:
    f.write(f'{len(syms)} {len(segs)}\n')
    for t in syms:
        if t<thr: f.write(f'{t} 26 '+' '.join(map(str,range(26)))+'\n')
        else: f.write(f'{t} 0\n')
    for s,_ in segs: f.write(f'1 1 {len(s)} '+' '.join(str(ix[t]) for t in s)+'\n')
open(pre+'.segs','w').write('\n'.join(f'{k}\t{inf}\t'+' '.join(map(str,s)) for k,(s,inf) in enumerate(segs))+'\n')
with open(pre+'.rc','w') as f:
    for t in syms: f.write(f'{(t-1)%9} {(t-1)//9}\n' if t<thr else '-1 0\n')
fr=np.load('/home/claude/keyless/rosenkrantz1629/pass2/lm/da1620.bin.freq.npy'); open(pre+'.freq','w').write(' '.join('%.6f'%x for x in fr)+'\n')
print('symbols',len(syms),'(low',sum(t<thr for t in syms),') segments',len(segs),'tokens',sum(len(s) for s,_ in segs))
