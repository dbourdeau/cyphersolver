"""synth.py ntypes seed: control. Danish text of the same segment lengths as the training text, enciphered with a random homophonic key of ntypes signs, written as TRANSCRIPTION-like rows to tmp/synth_<ntypes>.tsv; prints plaintext."""
import sys,random
sys.path.insert(0,'/home/claude/keyless/rosenkrantz1629/tools')
from common import *
nt=int(sys.argv[1]); rnd=random.Random(int(sys.argv[2]))
rows=load(); lens=[len(s) for r in rows if r[0] in TRAIN for s in r[3]]
t=open(R+'/lm/da1620.txt').read().split(); st=rnd.randrange(1000,len(t)-2000); txt=''.join(t[st:st+400])
A='abcdefghiklmnoprstuvy'; txt=''.join(c for c in txt if c in A)
freq={a:txt.count(a) for a in A}; order=sorted(A,key=lambda a:-freq[a])
hom={a:[f'S{i:02d}'] for i,a in enumerate(A)}; k=len(A)
while k<nt:
    a=rnd.choices(order[:10],weights=[freq[x] for x in order[:10]])[0]; hom[a].append(f'S{k:02d}'); k+=1
out=[];p=0;pl=[]
for L in lens:
    seg=txt[p:p+L]; p+=L; pl.append(seg); out.append(' '.join(rnd.choice(hom[c]) for c in seg))
open(R+f'/tmp/synth_{nt}.tsv','w').write('letter\timage\tline\ttokens\n'+'\n'.join(f'N12\tx\t{i}\t{o}' for i,o in enumerate(out))+'\n')
print(' | '.join(pl)[:300])
