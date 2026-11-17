"""Control for the Lear 1807 decode: the second agent's (verifier's) script, control_test2.py of 14 Nov 2026, with only its
paths changed so that it runs from this folder; the scoring, the seed and the nulls are as the verifier wrote them.

Design, as the verifier wrote it before running (fixed seed 1807, 200 shuffles):
Measure: letters-only character 5-gram model of English (linear interpolation of orders 1-5, weights .01 .04 .1 .25 .6),
trained on the repository's en-gutenberg corpus (lang/sources.json; cached by lang/corpora.py, 24 Gutenberg texts incl.
US founding documents). Score = mean log10 P per letter over each run of consecutive decoded values (runs break at groups
with no table value), letters joined across group boundaries so the model sees whether neighbouring values make English.
Null A: values of the groups occurring in these passages that hold a value, permuted among themselves (coverage unchanged).
Null B: whole table (549 values) permuted among all its groups.
Neither this control nor the first agent's was declared before the passages had been seen in print (Founders Online prints
the numbers); this one was written after the first agent's decode was known.

usage, from targets/pinckney1793:
  python beling/round_2026-11-14_lear1807/scripts/control_char5.py            the verifier's transcription (280 groups, copy 1)
  python beling/round_2026-11-14_lear1807/scripts/control_char5.py reconciled the reconciled text (281 groups, with copy 2's 663)
Writes control/control_result_char5[_reconciled].json. Needs numpy; fetches the corpus once if it is not cached."""
import sys,csv,json,random,re
import numpy as np
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]; ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT)); from lang import corpora
MODE=sys.argv[1] if len(sys.argv)>1 else 'verifier'
txt=open(corpora.fetch('en-gutenberg'),encoding='utf-8',errors='ignore').read().lower()
idx=np.frombuffer(re.sub('[^a-z]','',txt).encode(),dtype=np.uint8)-97
idx=idx.astype(np.int64)
cnt=[]
for o in range(1,6):
    code=np.zeros(len(idx)-o+1,dtype=np.int64)
    for k in range(o): code=code*26+idx[k:len(idx)-o+1+k]
    cnt.append(np.bincount(code,minlength=26**o).astype(np.float64))
LAM=[.01,.04,.1,.25,.6]
def cond(o,ctxcode,ch):
    if o==1: return (cnt[0][ch]+.5)/(cnt[0].sum()+13)
    num=cnt[o-1][ctxcode*26+ch]; den=cnt[o-2][ctxcode]
    return num/den if den>0 else 0.0
def per_letter_sum(s):
    a=[ord(c)-97 for c in s]; tot=0.0
    for i,ch in enumerate(a):
        p=0.0
        for o in range(1,6):
            if i-(o-1)<0: 
                p+=LAM[o-1]*cond(1,0,ch) if o>1 else 0; 
                if o==1: p+=LAM[0]*cond(1,0,ch)
                continue
            ctx=0
            for c in a[i-o+1:i]: ctx=ctx*26+c
            p+=LAM[o-1]*cond(o,ctx,ch)
        tot+=np.log10(p)
    return tot,len(a)
key={}
for r in csv.DictReader(open(HERE.parent/'round_2026-11-11'/'code16_key_v5.tsv',encoding='utf-8'),delimiter='\t'):
    v=r['value'].lower()
    if v.isalpha(): key[int(r['group'])]=v
P={}
if MODE=='reconciled':
    for line in open(HERE/'transcriptions'/'reconciled.txt',encoding='utf-8'):
        if line.startswith('P') and '|' in line:
            f=line.rstrip('\n').split('|'); P[f[0]]=[int(x.rstrip('^')) for x in f[5].split() if x!='--']
else:
    for line in open(HERE/'transcriptions'/'copy1_and_2_reader2_blind.txt',encoding='utf-8'):
        if line.startswith('P') and '|' in line:
            pid,_,_,g=line.strip().split('|'); P[pid]=[int(x) for x in g.split('.')]
def score(k):
    T=0;Nn=0
    for gs in P.values():
        cur=''
        for g in gs+[None]:
            if g is not None and g in k: cur+=k[g]
            else:
                if cur: t,n=per_letter_sum(cur); T+=t; Nn+=n
                cur=''
    return T/Nn
real=score(key)
occ=sorted({g for gs in P.values() for g in gs if g in key})
rng=random.Random(1807); res={'real':real}
for mode in ('occ','all'):
    out=[]
    for _ in range(200):
        if mode=='occ':
            vals=[key[g] for g in occ]; rng.shuffle(vals); k=dict(key); k.update(zip(occ,vals))
        else:
            gs=list(key); vals=[key[g] for g in gs]; rng.shuffle(vals); k=dict(zip(gs,vals))
        out.append(score(k))
    a=np.array(out)
    res[mode]={'mean':a.mean(),'max':a.max(),'sd':a.std(),'rank_real':int(1+(a>=real).sum()),'z':(real-a.mean())/a.std()}
# reference points: Lear's own clear sentences from these despatches (verifier's reading of the images)
clear=["you may be assured that","until we could take care of them in another way",
       "besides when i had the best grounds to believe that","otherwise he might feel it necessary to comply with",
       "and commerce must naturally languish in proportion","the war with tunis will probably be suspended during the winter"]
t=n=0
for c in clear:
    a,b=per_letter_sum(re.sub('[^a-z]','',c)); t+=a; n+=b
res['lear_clear_text_reference']=t/n
print(json.dumps(res,indent=1)); res['text']=MODE; res['groups']=sum(map(len,P.values())); res['groups_occurring_with_value']=len(occ)
json.dump(res,open(HERE/'control'/('control_result_char5'+('_reconciled' if MODE=='reconciled' else '')+'.json'),'w'),indent=1)
