"""Known-key convention checks on an unreliable transcription; no accepted reading.
Uses existing shared en-modern4gram model. Run from workspace/repository.
Tests Vigenere, Beaufort, variant Beaufort, reversed keys and constant shifts.
"""
from pathlib import Path
import sys,json
import numpy as np
ROOT=Path(__file__).resolve().parent;repo=ROOT.parents[1]
sys.path.insert(0,str(repo));from lang import lm
m=lm.load('en-modern',order=4,spaces=False)
KEYS=['COMERETRIBUTION','COMPLETEVICTORY','MANCHESTERBLUFF','THENAVYOURPRIDE','OURNAVYOURPRIDE']
raw='YXLNRFID AVA QEBT RFU HTTE VLSH YVS TBKY CALGTNGN SK KVRMAA TVQ WSILRIJ VBEU OY ILMWEE UM SV C PEFQV EMECKYSB RRQBKIZYYE HKHNL SJ HUCXIE'
# Working shape candidates only; false joins and folds may still change lengths.
def enc(s):return np.array([ord(c)-65 for c in s.upper() if 'A'<=c<='Z'])
def txt(x):return ''.join(chr(int(c)+65) for c in x)
def score(p):
 ix=p[:,:-3]*26**3+p[:,1:-2]*26**2+p[:,2:-1]*26+p[:,3:]
 return m.lp[ix].sum(axis=1)/(p.shape[1]-3)
def search(c):
 results=[];pos=np.arange(len(c))
 for key in KEYS:
  for reverse in [False,True]:
   k=enc(key[::-1] if reverse else key)
   for o in range(len(k)):
    ks=k[(pos+o)%len(k)]
    for mode,z in [('vig',c-ks),('beau',ks-c),('variant',c+ks)]:
     cand=(z[None,:]+np.arange(26)[:,None])%26;ss=score(cand);i=int(ss.argmax())
     results.append((float(ss[i]),key,reverse,o,mode,i,txt(cand[i])))
 return sorted(results,reverse=True)
def main():
 out=[];plain=enc('Send the troops to the railway station as soon as possible and have the transportation ready before morning the enemy is moving north and our stores must be removed at once')[:len(enc(raw))]
 k=enc('COMERETRIBUTION');ks=k[np.arange(len(plain))%len(k)]
 for mode,c in [('vig+1',plain+ks-1),('beau',ks-plain),('variant',plain-ks)]:
  best=search(c%26)[0];out.append('Synthetic same-length control '+mode+': '+str(best[:-1])+'\n  '+best[-1]);assert best[-1]==txt(plain)
 for name,c in [('whole',enc(raw)),('suffix',enc('RRQBKIZYYE HKHNL SJ HUCXIE'))]:
  out.append('\nReal '+name+' (unreliable transcription):')
  for row in search(c)[:8]:out.append(str(row[:-1])+'\n  '+row[-1])
 out.append('\nNo candidate is accepted. This checks conventions on this transcription only; negative output does not establish a different key or system. Controls do not model unknown segmentation errors.')
 (ROOT/'nov9_apr11_conventions_results.txt').write_text('\n'.join(out)+'\n');print('\n'.join(out))
if __name__=='__main__':main()
