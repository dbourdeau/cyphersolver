"""Experimental noisy-transcription key test, 1 Nov2026. No accepted reading.
Uses the project's shared en-modern fourgram model. Run from workspace root.
A same-length synthetic control is tested before interpreting real output.
"""
import json,sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
repo=ROOT.parents[1]
if not (repo/'lang').is_dir(): repo=repo/'submission-681-pr'
sys.path.insert(0,str(repo))
from lang import lm
from continue_analysis import vig
m=lm.load('en-modern',order=4,spaces=False)
rng=np.random.default_rng(681)
raw='VXLJNREI AVA QEBT RFU HTTE VLSH YVS TBKY CALGTNGN SK KVRMAA TVQ WSILRIJ VBEU OY ILMWEE UM SV C PEFQV EMECKYSB RRQBKIZJYE HKHNL SJ HICXIE'
# This working transcription remains uncertain throughout, not an exact copy.
def enc(s):return np.array([ord(c)-65 for c in s.upper() if 'A'<=c<='Z'])
def dec(c,key):return (c-key[np.arange(len(c))%len(key)])%26
def txt(x):return ''.join(chr(int(i)+65) for i in x)
def scores(p):
 ix=p[:,:-3]*26**3+p[:,1:-2]*26**2+p[:,2:-1]*26+p[:,3:]
 return m.lp[ix].sum(axis=1)
def solve(c,length,restarts=25):
 inds=np.arange(len(c))%length;best=(-1e100,None,None)
 for restart in range(restarts):
  key=rng.integers(0,26,length)
  for sweep in range(10):
   changed=False
   for pos in rng.permutation(length):
    p=np.tile(dec(c,key),(26,1));mask=inds==pos
    p[:,mask]=(c[mask][None,:]-np.arange(26)[:,None])%26
    ss=scores(p);v=int(ss.argmax())
    if v!=key[pos]:key[pos]=v;changed=True
   if not changed:break
  p=dec(c,key);sc=m.score_idx(p)
  if sc>best[0]:best=(sc,key.copy(),p.copy())
 return best

def main():
 c=enc(raw);out=[f'Working real transcription length: {len(c)}; unreliable glyphs/segmentation.']
 control=enc('Send the troops to the railway station as soon as possible and have the transportation ready before morning the enemy is moving north and our stores must be removed at once')[:len(c)]
 # Repeat the independently written control if needed to match exact length.
 control=np.resize(control,len(c));true=enc('COMERETRIBUTION');synthetic=(control+true[np.arange(len(c))%len(true)])%26
 for noise in [0,0.05,0.15]:
  scipher=synthetic.copy();n=int(len(c)*noise);ids=rng.choice(len(c),n,replace=False);scipher[ids]=rng.integers(0,26,n)
  sc,key,p=solve(scipher,15,50)
  out.append(f'Control nominal noise {noise:.0%}, changed positions {n}: key {txt(key)}, recovered plaintext {np.mean(p==control):.3f}; score {sc/(len(c)-3):.3f}')
  out.append('  '+txt(p))
 for key in ['COMERETRIBUTION','COMPLETEVICTORY','MANCHESTERBLUFF','THENAVYOURPRIDE','OURNAVYOURPRIDE']:
  choices=[]
  for o in range(len(key)):
   d=vig(raw,key,offset=o);choices.append((m.per_char(lm.norm(d,'modern')),o,d))
  sc,o,d=max(choices);out.append(f'Known key {key}, best phase {o}, score {sc:.3f}: {d}')
 results=[]
 for length in range(2,25):
  sc,key,p=solve(c,length,25);results.append((sc/(len(c)-3),length,txt(key),txt(p)))
 for sc,length,key,p in sorted(results,reverse=True)[:10]:out.append(f'Experimental best length{length}, score{sc:.3f}, key{key}: {p}')
 out.append('No output is an accepted reading. Unstable transcription and optimized short noisy streams can yield spurious English fragments. This experiment cannot establish a new key.')
 (ROOT/'apr11_experiment_results.txt').write_text('\n'.join(out)+'\n');print('\n'.join(out))
if __name__=='__main__':main()
