# Arbitrage mécanique H-A / H-B : lignes chiffrées appariées par (folio, ligne) ; jetons alignés (difflib) ; désaccord -> ?? ; douteux gardé.
import re, difflib, os, sys
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','transcriptions')
def load(p):
    d={}
    for l in open(os.path.join(B,p),encoding='utf-8'):
        m=re.match(r'(290[rv]) L(\d+) \| (.*)',l.strip())
        if m:
            s=re.sub(r'\{[^}]*\}',' ',m.group(3)); s=re.sub(r'\([^)]*\)',' ',s)
            d[(m.group(1),int(m.group(2)))]=re.findall(r'\?\?|\d+\??',s)
    return d
A=load('H-A-290.txt'); Bb=load('H-B-290.txt'); out=[]; agree=dis=0
for k in sorted(set(A)&set(Bb)):
    a=A[k]; b=Bb[k]; sa=[x.rstrip('?') for x in a]; sb=[x.rstrip('?') for x in b]; r=[]
    for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,sa,sb,autojunk=False).get_opcodes():
        if op=='equal':
            for i in range(i1,i2): r.append(a[i] if '?' in a[i] or '?' in b[j1+i-i1] and False else a[i]); agree+=i2-i1 if False else 0
            agree+=i2-i1
        else:
            n=max(i2-i1,j2-j1); r+=['??']*n; dis+=n
    out.append(f'{k[0]} L{k[1]:02d} | '+' '.join(r))
open(os.path.join(B,'ARBITRE-H-290.txt'),'w').write('# Arbitrage mécanique H-A/H-B (accord = gardé ; désaccord = ??)\n'+'\n'.join(out)+'\n')
print('lignes',len(out),'accord',agree,'désaccord',dis,'lignes seulement A',len(set(A)-set(Bb)),'seulement B',len(set(Bb)-set(A)))
