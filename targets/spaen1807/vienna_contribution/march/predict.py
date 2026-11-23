import bisect
import csv
import hashlib
import json
import random
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

p=Path(__file__).resolve().parent

def rows(name):
    with (p/name).open() as f:
        return list(csv.DictReader(f,delimiter='\t'))

def write(name,header,data):
    with (p/name).open('w') as f:
        writer=csv.writer(f,delimiter='\t',lineterminator='\n')
        writer.writerow(header)
        writer.writerows(data)

def normalize(text):
    text=text.lower().replace('œ','oe').replace('æ','ae')
    text=''.join(c for c in unicodedata.normalize('NFD',text) if not unicodedata.combining(c))
    return re.findall('[a-z0-9]+',text)

def predict(key,groups):
    predictions=[]
    start=None
    parts=[]
    for ordinal,group in enumerate(groups,1):
        label=key.get(group,'')
        role,_,value=label.partition('|')
        if role=='E' and start is not None:
            word=''.join(parts)+value
            if len(word)>=2:predictions.append((start,ordinal,word))
        if role=='M' and start is not None:
            parts.append(value)
            continue
        start=None
        parts=[]
        if role=='B':
            start=ordinal
            parts=[value]
        if role in ('W','P'):
            for word in value.split('_'):
                if len(word)>=2:predictions.append((ordinal,ordinal,word))
    return predictions

def series(groups):
    result=defaultdict(list)
    for i in range(len(groups)-3):
        seq=tuple(groups[i:i+4])
        if '?' not in seq: result[seq].append(i+1)
    return result

def main():
    train=rows('groups23.tsv');held=rows('groups26.tsv')
    ct=[r['strict'] for r in train];ht=[r['strict'] for r in held]
    labels=(p/'labels.txt').read_text().splitlines()
    paths=[[labels[int(r['label'])] for r in rows(f'path_{mode}.tsv')] for mode in (1.5,3)]
    for seq in paths:assert len(seq)==len(ct)
    occurrence=defaultdict(list)
    for i,g in enumerate(ct):
        if g!='?':occurrence[g].append(i)
    key={}; candidates=[];agreed=[]
    for g,indices in sorted(occurrence.items()):
        decision=[]; counts=[]
        for path in paths:
            scores=Counter(path[i] for i in indices).most_common()
            value,n=scores[0]
            counts.append(f'{value} ({n}/{len(indices)})')
            decision.append(value if n>=2 and n*3>=2*len(indices) and (len(scores)==1 or n>scores[1][1]) else None)
        good=decision[0]==decision[1] and decision[0] not in (None,'NULL')
        candidates.append([g,len(indices),counts[0],counts[1],decision[0] if good else '',','.join(str(i+1) for i in indices)])
        if good:
            key[g]=decision[0]
            agreed.append([g,decision[0]])
    write('candidate_audit.tsv',['code','n23','fit1','fit2','accepted','ordinals23'],candidates)
    write('key.tsv',['code','value'],agreed)
    write('training_segments.tsv',['ordinal','location23','code','fit1','fit2'],[(i+1,train[i]['position'],g,paths[0][i],paths[1][i]) for i,g in enumerate(ct)])
    preds=predict(key,ht)
    write('predictions26.tsv',['first','last','start_location','end_location','word'],[(a,b,held[a-1]['position'],held[b-1]['position'],w) for a,b,w in preds])
    write('label_coverage26.tsv',['ordinal','position','code','candidate'],[(r['ordinal'],r['position'],r['strict'],key.get(r['strict'],'')) for r in held])
    first,second=series(ct),series(ht)
    intersect=sorted(first.keys()&second.keys())
    write('shared_sequences.tsv',['sequence','ordinals23','ordinals26'],[(' '.join(s),','.join(map(str,first[s])),','.join(map(str,second[s]))) for s in intersect])
    rng=random.Random(18070329)
    vocab=sorted((set(ct)|set(ht))-{'?'})
    sims=[]
    for _ in range(1000):
        vals=vocab.copy();rng.shuffle(vals);mapping=dict(zip(vocab,vals))
        sims.append(len(first.keys() & series([mapping.get(g,'?') for g in ht]).keys()))
    write('overlap_controls.tsv',['control','shared_distinct_fourgrams'],enumerate(sims,1))
    result=dict(slots23=len(ct),slots26=len(ht),strict23=len(ct)-ct.count('?'),strict26=len(ht)-ht.count('?'),recurring23=sum(len(indices)>=2 for indices in occurrence.values()),key_entries=len(key),fitted_roles=dict(Counter(v.split('|')[0] for v in key.values())),held_marked_slots_covered=sum(g in key for g in ht),predicted_words=len(preds),distinct_predicted_words=len({w for _,_,w in preds}),whole_prediction_slot_count=len({i for a,b,_ in preds for i in range(a,b+1)}),shared_distinct_quads=len(intersect),overlap_controls_max=max(sims),overlap_controls_equal_or_better=sum(s>=len(intersect) for s in sims),reference_sha256='f28deee28fe3e32e815e3a9fa4b6437b4d948ff5917aee5334e14d122b8bb1e7')
    (p/'pre_score.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
