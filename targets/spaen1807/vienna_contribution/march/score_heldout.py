"""Run only after the predictions freeze. Expects the sealed No. 26 French body."""
import argparse
import bisect
import hashlib
import importlib.util
import json
import random
from collections import Counter
from pathlib import Path

p=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('march_predict',p/'predict.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
read=module.rows
parser=argparse.ArgumentParser()
parser.add_argument('reference',type=Path)
opt=parser.parse_args()
reference=opt.reference.read_bytes()
criterion=json.loads((p/'pre_score.json').read_text())
assert hashlib.sha256(reference).hexdigest()==criterion['reference_sha256'],'reference hash differs'
words=module.normalize(reference.decode('utf-8'))
codes=[r['strict'] for r in read('groups26.tsv')]
key={r['code']:r['value'] for r in read('key.tsv')}
predictions=module.predict(key,codes)
assert predictions==[(int(r['first']),int(r['last']),r['word']) for r in read('predictions26.tsv')]
L=sum(map(len,words));C=len(codes);den=2*C*L
by_word={}
letters=0
for j,w in enumerate(words,1):
    by_word.setdefault(w,[]).append((j,(2*letters+len(w))*C))
    letters+=len(w)

def score(preds,trace=False):
    # At most one match per predicted occurrence, strict increase in reference.
    choices={}
    for index,(a,b,w) in enumerate(preds):
        center=(a+b-1)*L
        opts=[j for j,loc in by_word.get(w,[]) if 25*abs(center-loc)<=den]
        if opts:choices[index]=opts
    if trace:
        best={0:()}
        for i,opts in choices.items():
            updated=best.copy()
            for j in opts:
                seq=min((v+((i,j),) for k,v in best.items() if k<j),key=lambda s:(-len(s),tuple(b for _,b in s),s))
                if j not in updated or (-len(seq),tuple(b for _,b in seq),seq)<(-len(updated[j]),tuple(b for _,b in updated[j]),updated[j]):updated[j]=seq
            best=updated
        return min(best.values(),key=lambda s:(-len(s),tuple(b for _,b in s),s))
    ends=[]
    for opts in choices.values():
        for j in reversed(opts):
            k=bisect.bisect_left(ends,j)
            if k==len(ends):ends.append(j)
            elif j<ends[k]:ends[k]=j
    return len(ends)

matches=score(predictions,True)
assert len(matches)==score(predictions)
rng=random.Random(18070328)
keys=sorted(key)
controls=[]
for _ in range(1000):
    values=[key[k] for k in keys];rng.shuffle(values)
    translated=module.predict(dict(zip(keys,values)),codes)
    controls.append((len(translated),score(translated)))
module.write('transfer_controls.tsv',['shuffle','predictions','matches'],[(i+1,*pair) for i,pair in enumerate(controls)])
module.write('transfer_matches.tsv',['first','last','prediction','clear_index','clear_word'],[(*predictions[i],j,words[j-1]) for i,j in matches])
distinct=len({predictions[i][2] for i,j in matches})
out=dict(reference_word_tokens=len(words),reference_letters=L,predictions=len(predictions),exact_matches=len(matches),distinct_matched_words=distinct,control_max=max(s for _,s in controls),controls_equal_or_better=sum(s>=len(matches) for _,s in controls),histogram=dict(Counter(s for _,s in controls)))
out['passed']=len(predictions)>=8 and len(matches)>=5 and distinct>=4 and len(matches)>out['control_max']
(p/'transfer_result.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
