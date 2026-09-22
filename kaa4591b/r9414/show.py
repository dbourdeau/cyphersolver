import re,sys
pg=sys.argv[1]
def load(f):
    d={};p=None
    for l in open(f,encoding='utf8'):
        m=re.match(r'== (P\d)',l)
        if m: p=m.group(1); continue
        m=re.match(r'(\d\d) (.*)',l)
        if m: d[(p,m.group(1))]=m.group(2).strip()
    return d
T=load('transcription_v2.txt');A=load('dec_b2.txt');B=load('dec_b3.txt');C=load('decrypt.txt')
for k in sorted(T):
    if k[0]!=pg: continue
    print(k[1],'T',T[k]); print('   old',C.get(k,'')); print('   b2 ',A.get(k,'')); print('   b3 ',B.get(k,''))
