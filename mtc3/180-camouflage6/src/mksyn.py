import re,random,sys
seed=int(sys.argv[1]); off=int(sys.argv[2]); out=sys.argv[3]; G=int(sys.argv[4]) if len(sys.argv)>4 else 9; NL=int(sys.argv[5]) if len(sys.argv)>5 else 1522
t=open('camo_wp2012.txt',encoding='utf8').read()
i=t.find('== Camouflage by mimesis'); s=t[i:]
s=re.sub(r'<ref[^>]*/>','',s); s=re.sub(r'<ref.*?</ref>','',s,flags=re.S); s=re.sub(r'\{\{[^{}]*\}\}','',s)
s=re.sub(r'\[\[(?:File|Image):[^\n]*','',s); s=re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]',r'\1',s); s=re.sub(r'==[^=]*==','',s)
L=re.sub('[^A-Z]','',s.upper())[off:off+NL]
random.seed(seed)
w=[random.uniform(0.6,1.4) for _ in range(G)]; tot=sum(w)
lens=[int(NL*x/tot) for x in w]; lens[-1]=NL-sum(lens[:-1])
b=[0]
for x in lens: b.append(b[-1]+x)
pieces=[L[b[k]:b[k+1]] for k in range(G)]
seq=[]; ptr=[0]*G; rem=[len(p) for p in pieces]
while sum(rem):
    k=random.choices(range(G),weights=rem)[0]
    seq.append(26*k+ord(pieces[k][ptr[k]])-65); ptr[k]+=1; rem[k]-=1
perm=list(range(26*G)); random.shuffle(perm)
ct=bytes(perm[x] for x in seq); dec=[0]*(26*G)
for p,c in enumerate(perm): dec[c]=p
open(out+'.bin','wb').write(ct); open(out+'_key.bin','wb').write(bytes(dec))
print(lens,len(set(ct)))
