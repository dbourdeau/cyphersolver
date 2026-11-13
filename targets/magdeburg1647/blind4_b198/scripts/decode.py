import sys,re
pairs="a-z b-s c-q d-e f-n g-o h-u i-r k-y l-t m-x p-w".split()
K={}
for p in pairs:
    a,b=p.split('-'); K[a]=b; K[b]=a
def words(path):
    out=[]
    for line in open(path,encoding='utf-8'):
        if line.startswith('#') or not line.strip(): continue
        ln,rest=line.split(' ',1)
        rest=rest.replace('{del}','\x00D').replace('{ins}','')
        for tok in rest.split():
            if tok.startswith('{'): continue
            tok=tok.replace('\x00D','')
            if not tok: continue
            c=re.sub(r'\[(.)\?\]',r'\1',tok)
            out.append((ln,tok,c))
    return out
def dec(c,key=K): return ''.join(key.get(ch,ch) for ch in c.lower())
if __name__=='__main__':
    for ln,tok,c in words(sys.argv[1]):
        print(ln,tok,dec(c),sep='\t')
