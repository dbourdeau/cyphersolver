"""Self-training: add to the training set the signs of new-page lines whose LM-corrected decryption scores
well as Latin (per-char > threshold), labelled with the beam's choice; retrain and reclassify."""
import pickle, sys, numpy as np, pathlib, glob
ROOT=pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT.parent.parent)); sys.path.insert(0,str(ROOT/'scripts'))
from lang import lm
from feat import feat
M=lm.load('la-letters',spaces=False)
P=pickle.load(open(ROOT/'work/pages.pkl','rb'))
thr=float(sys.argv[1]) if len(sys.argv)>1 else -2.1
tr=pickle.load(open(ROOT/'work/train2.pkl','rb'))
base=[x for x in tr]
add=0
for f in glob.glob(str(ROOT/'work/beam_*.tsv')):
    for l in open(f,encoding='utf8'):
        p,j,mach,ch,n,dec,ix=l.rstrip('\n').split('\t'); j=int(j); ix=[int(x) for x in ix.split()]
        d=''.join(c for c in dec if c.isalpha() and c.islower())
        if len(d)<12 or M.per_char(d)<thr: continue
        ss=sorted(P[p][j]['signs'],key=lambda s:s['x0'])
        for i,c in zip(ix,ch.split()): base.append((ss[i]['m'],c)); add+=1
print('added',add,'total',len(base))
pickle.dump(base,open(ROOT/'work/train3.pkl','wb'))
