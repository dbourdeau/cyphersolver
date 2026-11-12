# Mesure UNIQUE sur la partie 4 (réserve). Écrit et figé (PREREG-C02.md) AVANT toute lecture du chiffré de la partie 4.
import sys, random, struct, math, hashlib
sys.path.insert(0, '.')
from dt import undo, key_to_order
K1=[9,14,17,1,12,6,18,3,16,10,4,8,19,13,7,2,11,15,5]
K2=[19,22,9,17,1,12,7,16,21,13,10,20,4,18,2,15,6,3,8,11,5,14]
PRED=("VIERFUENFDREIXVONXHORBXNAQXMARBACHXSEITXZWOEINSNULLNULLXUHRFEUERBEREITXROEMXEINSXSTRIQXDREIXSTRIQX"
      "AQTFUENFEINSXVONXICHENHEIMXNAQBAHNHOFXHORNBERGXSEITXZWOEINSNULLNULLXUHRFEUERBEREIT").lower()
o1,o2=key_to_order(K1),key_to_order(K2)
qg=struct.unpack('456976f',open('qg.bin','rb').read())
def lm(s): return sum(qg[((ord(s[i])-97)*26+ord(s[i+1])-97)*676+(ord(s[i+2])-97)*26+ord(s[i+3])-97] for i in range(len(s)-3))/(len(s)-3)
def lev(a,b):
    p=list(range(len(b)+1))
    for i,x in enumerate(a,1):
        c=[i]
        for j,y in enumerate(b,1): c.append(min(p[j]+1,c[j-1]+1,p[j-1]+(x!=y)))
        p=c
    return p[-1]
def agr(s): return 1-lev(s,PRED)/max(len(s),len(PRED))
line=[l for l in open('../../working/T863-867.txt') if l.startswith('P4')][0]
ct=''.join(line.split('|')[1].split()).lower()[5:]
dec=undo(undo(ct,o2),o1)
rng=random.Random(20261111); C=[]
for _ in range(200):
    a=list(range(19)); b=list(range(22)); rng.shuffle(a); rng.shuffle(b); C.append(undo(undo(ct,b),a))
for _ in range(200):
    c=list(ct); rng.shuffle(c); C.append(undo(undo(''.join(c),o2),o1))
cl=[lm(c) for c in C]; ca=[agr(c) for c in C]
L,Ag=lm(dec),agr(dec)
ok = L>=max(cl)+0.5 and Ag>=0.85 and Ag>=max(ca)+0.30
print('ct len',len(ct),'sha256(ct)',hashlib.sha256(ct.encode()).hexdigest())
print('decrypt',dec)
print(f'lm real {L:.3f} | controls max {max(cl):.3f} mean {sum(cl)/len(cl):.3f}')
print(f'agreement real {Ag:.3f} | controls max {max(ca):.3f} mean {sum(ca)/len(ca):.3f}')
print('VERDICT', 'VALIDE' if ok else 'NON VALIDE')
