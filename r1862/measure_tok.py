"""Token-level read fraction: a code group counts as read when it has a key value and the running text around it
scores like real Italian (a 25-character window centred on it, it-cinquecento, spaceless)."""
import sys
sys.path.insert(0,'..')
from lang import lm
from decode import lines, KEY
M=lm.load('it-cinquecento',spaces=False)
seq=[]      # (group, plaintext) in document order, clear passages included as context
for lab,it in lines():
    for k,v in it:
        if k=='clear':
            seq.append((None, lm.norm(v,'early')))
        else:
            seq.append((v, lm.norm(KEY.get(v,''),'early')))
text=''.join(p for _,p in seq)
pos=[]; i=0
for g,p in seq:
    pos.append((g,i,i+len(p))); i+=len(p)
read=tot=0; unread=[]
for g,a,b in pos:
    if g is None: continue
    tot+=1
    if g not in KEY: unread.append((g,'no value')); continue
    lo=max(0,(a+b)//2-12); hi=min(len(text),lo+25)
    w=text[lo:hi]
    s=M.per_char(w) if len(w)>8 else -1
    if s>=-2.4: read+=1
    else: unread.append((g,round(s,2)))
print(f'{read}/{tot} = {read/tot:.3f} of code groups read as sense (token level, 25-char window)')
import collections
c=collections.Counter(g for g,_ in unread)
print('unread tokens:',len(unread),'| most common:',c.most_common(12))
