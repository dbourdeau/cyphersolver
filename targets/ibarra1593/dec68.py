"""Decode ct68.txt with keyM.tsv (Feria-Mansfeld key) or a key passed as JSON."""
import sys,json
K={}
for l in open('keyM.tsv',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    a,b=l.split('\t'); K[a.strip()]=b.strip()
K.update({'x':'a','2':'a','3':'e','r':'o','n':'e','∂':'y','∆':'s','6':'u','u':'u','ʃ':'e','ʒ':'a','∇':'o','5':'·','4':'a'})
if len(sys.argv)>1: K.update(json.load(open(sys.argv[1],encoding='utf-8')))
def lines():
    for l in open('ct68.txt',encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        n,t=l.rstrip('\n').split('\t'); yield n,t.split()
if __name__=='__main__':
    N=0
    for n,t in lines():
        N+=len(t); print(n,' '.join(K.get(x,'['+x+']') for x in t))
    print('tokens',N)
