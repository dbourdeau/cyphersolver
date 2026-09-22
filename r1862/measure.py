"""Read fraction: per cipher line, the LM score of its decipherment; a line counts as read when it scores
like real Italian. Tokens in unread lines, plus tokens with no key value, are the unread part."""
import sys,collections
sys.path.insert(0,'..')
from lang import lm
from decode import lines,KEY
M=lm.load('it-cinquecento',spaces=False)
tot=read=0; bad=[]
for lab,it in lines():
    gs=[v for k,v in it if k=='g']
    if not gs: continue
    txt=lm.norm(''.join(KEY.get(g,'') for g in gs),'early')
    unk=sum(1 for g in gs if g not in KEY)
    s=M.per_char(txt) if txt else -9
    tot+=len(gs)
    if s>=-2.4 and unk<=len(gs)*0.15: read+=len(gs)
    else: bad.append((lab,round(s,2),unk,len(gs),txt[:60]))
print(f'{read}/{tot} = {read/tot:.3f} of code groups in lines that read as Italian')
for b in bad: print(b)
