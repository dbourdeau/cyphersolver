"""decode_once.py: decode TRANSCRIPTION.tsv once with the frozen KEY.tsv -> DECODE.txt and judge/decode.txt. Unknown labels -> '?'."""
import re,os
R='/home/claude/keyless/rosenkrantz1629'
key={l.split('\t')[0]:l.split('\t')[1] for l in open(R+'/KEY.tsv').read().splitlines()[1:]}
HELD={'N21','N22','N23'}; out=[]; jd=[]
for l in open(R+'/TRANSCRIPTION.tsv').read().splitlines()[1:]:
    let,img,ln,tk=l.split('\t'); o=[]; j=[]
    for part in re.split(r'(\{[^}]*\})',tk):
        if part.startswith('{'): o.append(part); j.append('/'); continue
        for t in part.split():
            if t in('.',',','[del]','[blot]'): o.append(t); continue
            v=key.get(t.rstrip('?'),'?')
            if v=='_': continue
            if o and len(v)==1 and len(o[-1])>=1 and not o[-1].startswith(('{','[','.',',')): o[-1]+=v
            else: o.append(v)
            j.append(v if len(v)==1 else ' '+v+' ')
    out.append(f"{let}\t{img}\t{ln}\t{'HELD-OUT' if let in HELD else 'train'}\t"+' '.join(o))
    jd.append(f"{let} {img} l{ln} {'[HELD-OUT] ' if let in HELD else ''}"+''.join(j))
open(R+'/DECODE.txt','w').write('\n'.join(out)+'\n'); os.makedirs(R+'/judge',exist_ok=True); open(R+'/judge/decode.txt','w').write('\n'.join(jd)+'\n')
