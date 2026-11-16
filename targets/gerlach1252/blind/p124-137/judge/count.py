import re,sys
src=[l.rstrip('\n').split('\t') for l in open('judge_src.txt') if l.strip()]
dec=[l.rstrip('\n').split('\t') for l in open('decode.txt') if l.strip()]
def letters_dec(s):
    s=s.replace('[...1]','#').replace('<=?>','')
    return sum(1 for c in s if c.isalpha() or c in '#_')
out=['page\tline\tsegmented_reading\tS\tE\tN']
tot={}
bad=[]
for (p,l,m),d in zip(src,dec):
    S=E=N=0;mode=None
    for c in m:
        if c=='[':mode='E'
        elif c=='{':mode='N'
        elif c in ']}':mode=None
        elif c.isalpha() or c in '#_':
            if mode=='E':E+=1
            elif mode=='N':N+=1
            else:S+=1
    dl=letters_dec(d[1]); key=d[0].split()[0]+' '+d[0].split()[1]
    if 'p.'+p+' '+l!=key or S+E+N!=dl: bad.append((p,l,S+E+N,dl,key))
    out.append(f'{p}\t{l}\t{m}\t{S}\t{E}\t{N}')
    t=tot.setdefault(p,[0,0,0]);t[0]+=S;t[1]+=E;t[2]+=N
print(len(src),len(dec));print('mismatch',bad)
open('judge.tsv','w').write('\n'.join(out)+'\n')
a=[0,0,0]
for p,t in tot.items():
    n=sum(t);a=[x+y for x,y in zip(a,t)]
    print(f'p.{p}: S {t[0]} E {t[1]} N {t[2]} total {n}; strict {t[0]}/{n} = {100*t[0]/n:.1f}%')
n=sum(a);print(f'ALL: S {a[0]} E {a[1]} N {a[2]} total {n}; strict {a[0]}/{n} = {100*a[0]/n:.1f}%; S+E {a[0]+a[1]}/{n} = {100*(a[0]+a[1])/n:.1f}%')
