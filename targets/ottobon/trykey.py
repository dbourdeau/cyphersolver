"""Decode ct_all.txt (or a given file) with a key TSV; print coverage and text."""
import sys,re,collections
keyf=sys.argv[1]; ctf=sys.argv[2] if len(sys.argv)>2 else 'ct_all.txt'
key={}
for l in open(keyf,encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    k,v=l.rstrip('\n').split('\t')[:2]; key[k]=v
toks=open(ctf,encoding='utf8').read().split()
n=len(toks); hit=sum(t in key for t in toks)
print('tokens',n,'in key',hit,'%.1f%%'%(100*hit/n))
out=[]
for t in toks:
    v=key.get(t)
    if v is None: out.append('['+t+']')
    elif v=='_': out.append('')
    else: out.append(v.lower() if len(v)<=4 else ' '+v+' ')
print(''.join(out))
