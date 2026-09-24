import sys,re
c=open('bgs.txt').read().strip(); b=[c[i:i+2] for i in range(0,len(c),2)]
P=re.sub('[^A-Z]','',open(sys.argv[1]).read().upper())
print('len',len(P),'need',2*len(b))
pb=[P[i:i+2] for i in range(0,len(P),2)]
fwd={};bwd={};bad=0
for i,(x,y) in enumerate(zip(b,pb)):
    if x in fwd and fwd[x]!=y: print('CT',x,'->',fwd[x],'and',y,'at letter',2*i, P[max(0,2*i-20):2*i+20]); bad+=1
    if y in bwd and bwd[y]!=x: print('PT',y,'<-',bwd[y],'and',x,'at letter',2*i, P[max(0,2*i-20):2*i+20]); bad+=1
    fwd.setdefault(x,y); bwd.setdefault(y,x)
print('conflicts',bad,'distinct',len(fwd))
