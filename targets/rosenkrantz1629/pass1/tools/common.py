import re,math,collections,json
R='/home/claude/keyless/rosenkrantz1629'
NUMW={'33','68','79','84','98'}; WORDSIGN={'MOON','XX','TBL'}
TRAIN={'N12','N13','N14','N20'}; HELD={'N21','N22','N23'}
def load():
    """rows: (letter,image,line,[segments]) ; a segment is a list of sign labels; segments break at clear words, number words, word signs"""
    rows=[]
    for l in open(__import__('os').environ.get('TX',f'{R}/TRANSCRIPTION.tsv')).read().splitlines()[1:]:
        let,img,ln,tk=l.split('\t')
        segs=[];cur=[]
        for part in re.split(r'(\{[^}]*\})',tk):
            if part.startswith('{'):
                if cur: segs.append(cur);cur=[]
                continue
            for t in part.split():
                if t in('.',',','[del]','[blot]'): continue
                t=t.rstrip('?')
                if t in NUMW or t in WORDSIGN:
                    if cur: segs.append(cur);cur=[]
                else: cur.append(t)
        if cur: segs.append(cur)
        rows.append((let,img,ln,segs))
    return rows
class LM:
    def __init__(s):
        t=open(f'{R}/lm/da1620.txt').read().replace(' ','')
        s.t={}
        for n in (3,5):
            c=collections.Counter(t[i:i+n] for i in range(len(t)-n+1)); tot=sum(c.values())
            s.t[n]=({k:math.log10(v/tot) for k,v in c.items()},math.log10(0.3/tot))
    def score(s,txt):
        n=5 if len(txt)>=5 else 3
        if len(txt)<3: return 0.0
        d,f=s.t[n]; sc=sum(d.get(txt[i:i+n],f) for i in range(len(txt)-n+1))
        return sc*(1.0 if n==5 else 0.6)
