"""Decode the cipher runs of transcription.txt with key.tsv (the integration's own decoder, 13 Nov 2026).
Usage: python decode.py  (run from anywhere; reads ../key.tsv and ../transcription.txt, prints the decryption).
Marks: plain letter = table value; {x} = row-structure value; <x> = context / single-occurrence / typo value;
[?xy] = bigram with no value."""
import os
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')
K={}
for line in open(os.path.join(D,'key.tsv'),encoding='utf-8'):
    if line.startswith('#') or line.startswith('bigram'): continue
    b,p,s=line.rstrip('\n').split('\t'); K[b]=(p,s)
def dec(c):
    out=[]
    for w in c.split():
        s=''
        for i in range(0,len(w)-1,2):
            b=w[i:i+2]
            if b not in K: s+='[?'+b+']'; continue
            p,src=K[b]
            s+= p if src=='table' else ('{'+p+'}' if src=='row' else '<'+p+'>')
        if len(w)%2: s+='[odd:'+w[-1]+']'
        out.append(s)
    return ' '.join(out)
if __name__=='__main__':
    for line in open(os.path.join(D,'transcription.txt'),encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        n,pg,c=line.rstrip('\n').split('|')
        print(f"{n}|{pg}|{c}|{dec(c)}")
