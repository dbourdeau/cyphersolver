import sys,json
p='reading_p34.txt'; L=open(p,encoding='utf8').read().split('\n')
d=json.load(open(sys.argv[1],encoding='utf8'))
for j,l in enumerate(L):
    for k,v in d.items():
        if l.startswith(f'P4.{k} '): L[j]=f'P4.{k} {v}'
open(p,'w',encoding='utf8').write('\n'.join(L))
