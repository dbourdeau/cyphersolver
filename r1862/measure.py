"""Read fraction: per cipher line, the LM score of its decipherment; a line counts as read when it scores
like real Italian. Tokens in unread lines, plus tokens with no key value, are the unread part."""
import sys,collections
sys.path.insert(0,'..')
from lang import lm
from decode import lines,KEY
M=lm.load('it-cinquecento',spaces=False)
rows=[(lab,[v for k,v in it if k=='g']) for lab,it in lines()]
rows=[(lab,gs) for lab,gs in rows if gs]
texts=[lm.norm(''.join(KEY.get(g,'') for g in gs),'early') for _,gs in rows]
tot=read=0; bad=[]
for i,((lab,gs),txt) in enumerate(zip(rows,texts)):
    unk=sum(1 for g in gs if g not in KEY)
    # score the line with the edges of its neighbours: a word split across a line end is an artifact
    left=texts[i-1][-10:] if i else ''
    right=texts[i+1][:10] if i+1<len(texts) else ''
    ctx=left+txt+right
    s=(M.per_char(ctx)*len(ctx)-M.per_char(left+right)*len(left+right))/max(len(txt),1) if txt else -9
    tot+=len(gs)
    if txt and s>=-2.4 and unk<=len(gs)*0.15: read+=len(gs)
    else: bad.append((lab,round(s,2),unk,len(gs),txt[:60]))
print(f'{read}/{tot} = {read/tot:.3f} of code groups in lines that read as Italian')
for b in bad: print(b)
