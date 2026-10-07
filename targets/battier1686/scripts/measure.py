"""measure.py: aggregate graded token tables reading/sNNNX.tsv -> per page and total H/C/M/I, read-as-sense share (H+C)."""
import glob,os,re,collections
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tot=collections.Counter(); rows=[]
for fn in sorted(glob.glob(f'{D}/readings/s[0-9][0-9][0-9][LR].tsv')):
    c=collections.Counter()
    for l in open(fn):
        p=l.rstrip('\n').split('\t')
        if len(p)<6 or not p[0].isdigit(): continue
        c[p[5] or '?']+=1
    n=sum(c.values()); tot+=c
    rows.append((os.path.basename(fn)[:-4],n,c))
print('%-6s %5s %4s %4s %4s %4s %4s %7s'%('page','tok','H','C','M','I','?','H+C%'))
for b,n,c in rows:
    print('%-6s %5d %4d %4d %4d %4d %4d %6.1f%%'%(b,n,c['H'],c['C'],c['M'],c['I'],c['?'],100*(c['H']+c['C'])/max(n,1)))
n=sum(tot.values())
print('%-6s %5d %4d %4d %4d %4d %4d %6.1f%%'%('TOTAL',n,tot['H'],tot['C'],tot['M'],tot['I'],tot['?'],100*(tot['H']+tot['C'])/max(n,1)))
print('H only: %.1f%%   H+C+M: %.1f%%'%(100*tot['H']/n,100*(tot['H']+tot['C']+tot['M'])/n))
