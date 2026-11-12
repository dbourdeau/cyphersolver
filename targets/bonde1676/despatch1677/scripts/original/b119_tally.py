import sys,re
# tally.py decodefile segfile : checks that the segments rebuild the decode output exactly, then classifies.
dec=''.join(re.sub(r'«[^»]*»','',l.split(' ',1)[1]).replace(' ','').strip() for l in open(sys.argv[1],encoding='utf-8') if l.strip())
units=open(sys.argv[2],encoding='utf-8').read().split()
segs=[]; 
for u in units:
    flag=None
    if u.endswith('!N') or u.endswith('!E'): flag=u[-1]; u=u[:-2]
    s,_,r=u.partition('=')
    segs.append((s,r,flag))
re_=''.join(s for s,_,_ in segs)
if re_!=dec:
    i=next((k for k in range(min(len(re_),len(dec))) if re_[k]!=dec[k]),min(len(re_),len(dec)))
    print('MISMATCH at',i,'\n seg:',re_[max(0,i-30):i+30],'\n dec:',dec[max(0,i-30):i+30]); sys.exit(1)
S=E=N=0; rows=[]
for s,r,flag in segs:
    weak=bool(re.search(r'[A-ZÅÄÖ<\[]',s))
    if flag=='N': c='N'
    elif flag=='E' or weak: c='E'
    else: c='S'
    S+=c=='S'; E+=c=='E'; N+=c=='N'; rows.append('%s\t%s\t%s'%(s,c,r))
open(sys.argv[2].replace('seg_','units_').replace('.txt','.tsv'),'w',encoding='utf-8').write('# unit\tclass\treading (if not S)\n'+'\n'.join(rows)+'\n')
T=S+E+N
print('%s: S %d + E %d + N %d = %d ; strict %d/%d = %.2f%% ; S+E %d/%d = %.2f%%'%(sys.argv[2].split('seg_')[1][:-4],S,E,N,T,S,T,100*S/T,S+E,T,100*(S+E)/T))
