from common import *
A=load(O+'transcription_T1.txt'); B=load(O+'transcription_T2.txt')
tot=same=0; diffs=[]
for k in sorted(A):
    a=[norm(t) for t in A[k]]; b=[norm(t) for t in B[k]]
    for x,y in align(a,b):
        tot+=1
        if x==y: same+=1
        else: diffs.append((k,x,y))
print('aligned positions',tot,'agree',same,round(same/tot,4))
print('signs T1',sum(len(v) for v in A.values()),'T2',sum(len(v) for v in B.values()))
for d in diffs: print(d)
