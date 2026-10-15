"""Decode the Spanish Cipher (1592-1593) with Tomokiyo's key."""
import sys
K={}
for line in open('keyM.tsv'):
    if line.startswith('#') or not line.strip(): continue
    a,b=line.split('\t'); K[a.strip()]=b.strip()
LET={'n':'e','f':'e','+':'e','9':'g','p':'i','h':'l','x':'n','4':'a','Z':'a',
     'y':'r','u':'t','r':'t','a':'u','6':'u','1':'x'}
FIN={'.':'n',':':'r','^':'s'}
def dec(tok):
    base=tok; fin=''
    while base and base[-1] in FIN:
        fin=FIN[base[-1]]+fin; base=base[:-1]
    if base in K: return K[base]+fin
    if base in LET: return LET[base]+fin
    if base=='?': return '·'
    return '{'+tok+'}'
toks=[]
for line in open(sys.argv[1]):
    if line.startswith('#'): continue
    toks+=line.split()
out=[dec(t) for t in toks]
print(' '.join(out)); print(); print(''.join(o for o in out if not o.startswith('{')))
