import sys,json
p='transcription_p34.txt'; L=open(p,encoding='utf8').read().split('\n')
i=L.index('== P4 (f.258v, image rotated 180) ==')
fix=json.load(open(sys.argv[1],encoding='utf8'))
for j in range(i+1,len(L)):
    n=L[j][:2]
    if n in fix:
        for a,b in fix[n]:
            if a=='*': L[j]=n+' '+b; continue
            assert a in L[j],(n,a,L[j]); L[j]=L[j].replace(a,b,1)
open(p,'w',encoding='utf8').write('\n'.join(L))
