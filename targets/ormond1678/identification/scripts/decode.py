# Decode the 1678 figures with the shifted key. python3 -I decode.py <folder identification/>
import sys,os
d=sys.argv[1] if len(sys.argv)>1 else '.'
key={}
for l in open(os.path.join(d,'key_shifted.tsv')).read().splitlines()[1:]:
    f=l.split('\t'); key[int(f[0])]=(int(f[1]),f[2],f[3])
runs=[[445],[342],[726,91,33,425,93,58,384,54,700,720],[732,573,526,32,643,214,55,440]]
clear=['If what he says of','and',', be true','but it seems','. This is a trial ...']
out=[];led=[]
for i,r in enumerate(runs):
    out.append('{'+clear[i]+'}')
    for f in r:
        n,v,s=key[f]; assert n==f-7
        out.append(v if v!='[hole]' else f'[{f}]'); led.append(f'{f}\t{n}\t{v}\t{s}')
out.append('{'+clear[4]+'}')
S=sum(1 for x in led if '[hole]' not in x)
open(os.path.join(d,'decryption.txt'),'w').write(' '.join(out)+'\n')
open(os.path.join(d,'ledger.tsv'),'w').write('fig_1678\tno_1680\tvalue\tstatus\n'+'\n'.join(led)+'\n')
print(' '.join(out)); print(f'given a value: {S}/20 = {S/20:.2%}')
from collections import Counter
print(Counter(x.split('\t')[3] for x in led))
