"""Apply the working key (key.tsv) to a token transcription (r8613_tokens.txt).
Usage: python decode.py r8613_tokens.txt [key.tsv]
Unknown tokens print as [tok]; nulls (value '-') print nothing; {clear text} is kept in capitals-free braces."""
import sys,re
tf=sys.argv[1]; kf=sys.argv[2] if len(sys.argv)>2 else 'key.tsv'
key={}
for l in open(kf,encoding='utf-8'):
    l=l.rstrip('\n')
    if not l or l.startswith("%%"): continue
    t,v=l.split('\t')[:2]; key[t]=v
for l in open(tf,encoding='utf-8'):
    l=l.rstrip('\n')
    if l.startswith('#'): print(l); continue
    out=[]
    for m in re.finditer(r'\{[^}]*\}|\S+',l):
        t=m.group(0)
        if t.startswith('{'): out.append(' '+t+' '); continue
        v=key.get(t)
        if v is None: out.append('['+t+']')
        elif v=='-': out.append('·')
        else: out.append(v)
    print(''.join(out))
