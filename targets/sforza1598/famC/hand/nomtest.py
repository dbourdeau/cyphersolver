import json,collections,re
exec(open('nom2.py').read().split("k=json.load")[0])
k0=json.load(open('key_h4.json')); L=[l.split() for l in open('t7.txt').read().strip().split('\n')]
TR,HO=L[:38],L[38:]
def cov(k,lines):
    h=t=0
    for l in lines:
        s=''.join(k.get(x,'') for x in l); m=mask(s); h+=sum(m); t+=len(s)
    return h/t, h
b=(cov(k0,TR),cov(k0,HO)); print('base train %.3f holdout %.3f'%(b[0][0],b[1][0]))
for s in ['c','q','P','u','l','w','Q','D1','m','r','X','O','3']:
    res=[]
    for a in ['']+list('aeioulnrstcdmpbgfvq'):
        k=dict(k0);k[s]=a; tr,ho=cov(k,TR),cov(k,HO)
        res.append((tr[1]-b[0][1]+ho[1]-b[1][1],a or 'NULL',tr[1]-b[0][1],ho[1]-b[1][1]))
    res.sort(reverse=True); print(s,'now',k0.get(s),'| best:',res[:4])
