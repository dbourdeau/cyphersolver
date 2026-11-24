import sys, json, re
T=json.load(open(sys.argv[1],encoding='utf-8'))
tot=cov=0
for line in open(sys.argv[2],encoding='utf-8'):
    if line.startswith('##'): print(line.strip()); continue
    if line.startswith('#'): continue
    out=[]
    for tok in line.split():
        m=re.match(r'(\d+)(\S*)',tok); c,mk=m.group(1),m.group(2)
        tot+=1
        if c in T:
            cov+=1; v=T[c]['v']; 
            if T[c]['statut']=='D': v=v+'?'
            out.append(v+mk.replace('?','¿'))
        else: out.append('‹'+c+mk+'›')
    print(' '.join(out))
print('couverture',cov,'/',tot,round(cov/tot,3))
