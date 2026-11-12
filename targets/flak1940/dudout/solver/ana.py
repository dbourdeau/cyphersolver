import re,sys
def load(f):
    d={}
    for l in open(f):
        m=re.match(r'k1=(\d+) k2=(\d+) score=(-?[\d.]+) ord=(.*)',l)
        if m: d[(int(m[1]),int(m[2]))]=(float(m[3]),m[4].strip())
    return d
a=load(sys.argv[1]); b=load(sys.argv[2])
k=[x for x in a if x in b]
r=sorted(k,key=lambda x:-(a[x][0]-b[x][0]))
for x in r[:10]: print(x,round(a[x][0],3),round(b[x][0],3),round(a[x][0]-b[x][0],3))
import statistics
m=[a[x][0]-b[x][0] for x in k]; print('margin mean',round(statistics.mean(m),3),'sd',round(statistics.pstdev(m),3))
