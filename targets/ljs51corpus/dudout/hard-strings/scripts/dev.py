"""Developpement (chaine de dev grillee) : salex sur une chaine, accord avec le decodage par la cle de Daniel.
usage: dev.py chaine lm lex rho lam R IT seed"""
import sys, subprocess, difflib
sys.path.insert(0, "../../blind-confirmation/scripts")
from common import LETTERS
from sigparse import read_sig
B="./"
AV="../../blind-confirmation/"
cid,lm,lex,rho,lam,R,IT,seed=sys.argv[1:9]; mode=sys.argv[9] if len(sys.argv)>9 else '0'
toks,K,labels=read_sig(AV+f"transcriptions/{cid}.sig")
inp=f"{len(toks)}\n{' '.join(map(str,toks))}\n{K}\n"
o=subprocess.run([B+"scripts/salex",lm,lex,rho,lam,R,IT,seed,mode],input=inp,capture_output=True,text=True).stdout.split('\n')
d,obj,oov=o[0].split(); key=list(map(int,o[1].split()))
s=toks[::-1] if d=='1' else toks
dec=''.join(' ' if t<0 else LETTERS[key[t]-1] for t in s)
ref={l.split('\t')[0]:l.rstrip('\n').split('\t')[9] for l in open(B+"diag/objectif_tout.tsv").read().split('\n')[1:] if l}.get(cid)
def acc(a,b):
    a=a.replace(' ','');b=b.replace(' ','')
    return sum(x.size for x in difflib.SequenceMatcher(None,a,b,autojunk=False).get_matching_blocks())/max(len(a),len(b),1)
print(cid,'mode',mode,'rho',rho,'lam',lam,'dir',d,'obj',obj,'oov',oov,'acc',round(acc(dec,ref),3) if ref else '-',dec,sep='\t')
