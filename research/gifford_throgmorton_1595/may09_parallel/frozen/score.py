"""Use only the prespecified ordinary prose anchors to locate the five positions."""
from pathlib import Path
import csv
import hashlib
import json
import random
import re
import sys
from collections import Counter

D=Path(__file__).resolve().parent
def rows(p):
    with p.open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))
def fold(t):
    return t.upper().replace('J','I').replace('U','V')
def compare(gold):
    w=[t.lower() for t,_,_ in gold]
    poss={k:set() for k in ['T02','T04','M04','M12','M13']}
    earnest={'earnest','earneste','ernest','erneste','earneste','earnesthe'}
    opinion={'opinion','oppinion','opinyon','oppinyon'}
    truly={'truly','truely','trulie','truelie','truelye','trewly','trewlie','trewlye','trueli','trulye'}
    were={'were','wer','weare','weere','weer','weir','neere','neer','neare','nere'}
    advices={'advice','advices','advise','advises','aduice','aduices','aduise','aduises','advertises'}
    for i in range(len(w)):
        if w[i]=='and' and i+3<len(w) and w[i+3] in {'had','hadd','hadde'}:
            number=w[max(0,i-2):i]==['93','94']
            context=bool(earnest.intersection(w[max(0,i-35):i]) and opinion.intersection(w[i+4:i+29]))
            if number or context:poss['T02'].add(i+1)
        if i and w[i]=='and' and i+1<len(w) and w[i+1] in truly:
            for n in (1,2,3):
                j=i+2+n
                if w[j:j+2]==['is','of'] and j+2<len(w) and w[j+2] in opinion:
                    if earnest.intersection(w[max(0,i-50):i]) or {'had','hadd','hadde'}.intersection(w[max(0,i-12):i]):poss['T04'].add(i-1)
        if w[i:i+1]==['with'] and i+3<len(w) and w[i+1] in {'sir','syr','sr','s'} and w[i+2]=='72':
            if any(w[k:k+2]==['in','102'] for k in range(max(0,i-12),i-1)):poss['M04'].add(i+3)
        if i>=3 and w[i]=='of' and w[i+1:i+2] in (['purpose'],['purpos'],['purposs'],['purposee']) and w[i+2:i+3]==['to']:
            if w[i-3] in were or advices.intersection(w[max(0,i-20):i-2]):
                poss['M12'].add(i-2);poss['M13'].add(i-1)
    return poss
def main():
    assert len(sys.argv)==2
    for line in (D/'FREEZE.sha256').read_text().splitlines():
        digest,name=line.split('  ',1);assert hashlib.sha256((D/name).read_bytes()).hexdigest()==digest,name
    ref=Path(sys.argv[1]); transcript=rows(ref);assert transcript and set(transcript[0])=={'folio','line','text'}
    gold=[]
    for v in transcript:
        assert v['folio'] in {'329r','329v'}
        for t in re.findall(r'[A-Za-z]+|[0-9]+|\?+',v['text']):
            gold.append((t,v['folio'],v['line']))
    pos=compare(gold)
    eligible=[];result=[]
    for r in rows(D/'predictions.tsv'):
        label=r['group'];p=pos[label];out=dict(r)
        if len(p)!=1:
            out.update(status='unmapped' if not p else 'ambiguous',possibilities=sorted(p))
        else:
            i,=p;t,folio,line=gold[i]
            # A transcription explicitly marked ?? is an unknown-length span.
            # A single ? represents one uncertain but bounded word.
            mate=(i+1 if label in {'T02','M12'} else i-1 if label=='M13' else i)
            if not re.fullmatch('[A-Za-z]+',t) or (0<=mate<len(gold) and gold[mate][0].startswith('??')):
                out.update(status='unresolved',folio=folio,line=line)
            else:
                out.update(reference=t,folio=folio,line=line,word_index=i+1,status='exact' if fold(t)==r['prediction'] else 'mismatch')
                eligible.append((label,r['prediction'],fold(t)))
            out['context']=' '.join(x[0] for x in gold[max(i-6,0):i+7])
        result.append(out)
    key=rows(D.parent/'nov20_william_transfer/alphabet.tsv')[0];assert key['marker']=='2'
    abc=key['header'];rng=random.Random(15950509)
    exact={a for _,a,b in eligible if a==b};metric=len(exact);letters=sum(map(len,exact));scores=[]
    for _ in range(1000):
        z=list(abc);rng.shuffle(z);table=str.maketrans(abc,''.join(z))
        scores.append(len({b for _,a,b in eligible if a.translate(table)==b}))
    status='unscorable' if not eligible else 'pass' if metric>=3 and letters>=12 and metric>max(scores) else 'miss'
    out={'status':status,'candidate_count':len(result),'mapped_secure':len(eligible),'exact_positions':sum(a==b for _,a,b in eligible),'distinct_exact':metric,'distinct_letters':letters,'control_max':max(scores),'control_histogram':dict(sorted(Counter(scores).items())),'controls_at_least_score':sum(x>=metric for x in scores),'reference_sha256':hashlib.sha256(ref.read_bytes()).hexdigest(),'positions':result}
    assert not (D/'result.json').exists() and not (D/'controls.tsv').exists()
    with (D/'controls.tsv').open('x') as f:f.write('replicate\tdistinct_exact\n'+''.join(f'{i}\t{n}\n' for i,n in enumerate(scores,1)))
    with (D/'result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
