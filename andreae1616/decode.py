import sys
key={}
for l in open('key.tsv',encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    s,v=l.split('\t')[:2]; key[s]=v
for l in open('ciphertext.txt',encoding='utf8'):
    l=l.rstrip('\n')
    if l.startswith('#'): print(l); continue
    print(' '.join(''.join(key.get(c,'?') for c in w) for w in l.split()))
