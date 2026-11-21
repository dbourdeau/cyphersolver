"""Evaluate the two interior cipher strips under the frozen October comparison."""
import csv
import hashlib
import json
import random
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
KEY = BASE / 'crawford_rebase/targets/figueroa1534/validation/K4.tsv'
PLATE = BASE / 'priority_review/modena_shape_reference/shape_index.tsv'

def read_tsv(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        yield from csv.DictReader((s for s in stream if not s.startswith('#')), delimiter='\t')

def norm(value):
    decomp = unicodedata.normalize('NFD', value.lower())
    return ''.join(c for c in decomp if c.isalpha()).translate(str.maketrans('vj','ui'))

def nearest(x, others):
    if not others:
        return None
    dist = min(abs(x-y) for y in others)
    candidates = [y for y in others if abs(x-y) == dist]
    return candidates[0] if dist <= 10 and len(candidates) == 1 else None

def align(one, two):
    left = {x: nearest(x,two) for x in one}
    right = {x: nearest(x,one) for x in two}
    paired = {x:y for x,y in left.items() if y is not None and right[y] == x}
    union = [(x,y) for x,y in paired.items()]
    union += [(x,None) for x in one if x not in paired]
    union += [(None,y) for y in two if y not in paired.values()]
    return sorted(union,key=lambda p:sum(v for v in p if v is not None)/sum(v is not None for v in p))

def matches(text, reference):
    matches_by_start = set()
    for run in text.split('#'):
        for lo in range(len(run)):
            word = run[lo:lo+5]
            if len(word) < 5:
                break
            start = reference.find(word)
            while start >= 0:
                n = 5
                while lo+n<len(run) and start+n<len(reference) and run[lo+n]==reference[start+n]:
                    n += 1
                # Shorter matches can be needed to avoid overlap of the two rows.
                for size in range(5,n+1):
                    matches_by_start.add((start,start+size))
                start = reference.find(word,start+1)
    return sorted(matches_by_start)

def assess(consensus, mapping, reference):
    strings = []
    covered = 0
    for row in ['a','b']:
        parts = []
        for label in consensus[row]:
            values = mapping.get(label)
            if not values or len(values)!=1:
                parts.append('#')
            elif values[0] != 'NUL':
                reading=norm(values[0]) if all(c.isalpha() or c.isspace() for c in values[0]) else ''
                parts.append(reading or '#')
                covered+=int(bool(reading))
        strings.append(''.join(parts))
    hit_a,hit_b=(matches(s,reference) for s in strings)
    pairs=[(a,b) for a in hit_a for b in hit_b if a[1]<=b[0]]
    # The plan retains a lone row's score only when an ordered pair is unavailable.
    if not pairs:
        pairs = [(a,(0,0)) for a in hit_a] + [((0,0),b) for b in hit_b]
    winner=max(pairs,key=lambda pair:sum(r-l for l,r in pair),default=((0,0),(0,0)))
    return {'lines':strings,'covered':covered,'known':sum(c.isalpha() for s in strings for c in s),
            'score':sum(r-l for l,r in winner),'spans':winner,'pieces':[reference[l:r] for l,r in winner]}

def main():
    table=defaultdict(set)
    for row in read_tsv(KEY):
        table[row['label']].update(row['valeur'].split('|'))
    table={k:tuple(sorted(v)) for k,v in table.items()}
    specimens={int(r['number']):r['published_label'] for r in read_tsv(PLATE)}
    input_paths=[HERE / tag / 'reading.tsv' for tag in ['reader_a','reader_b']]
    # The plan and input hashes travel with the computed result.
    readers=[]
    for path in input_paths:
        rows={'a':{},'b':{}}
        for entry in read_tsv(path):
            key=entry['row'].strip().lower()
            x=int(entry['x'])
            assert 0<=x<800 and x not in rows[key]
            spec=entry['specimen'].strip()
            value=specimens[int(spec)] if spec.isdecimal() and entry['confidence'].lower() in ('high','medium') else None
            rows[key][x]=value
        readers.append(rows)
    positions=[]
    consensus={}
    for row in ('a','b'):
        one,two=(r[row] for r in readers)
        consensus[row]=[]
        for x,y in align(one,two):
            left,right=one.get(x),two.get(y)
            label=left if left is not None and left==right else None
            consensus[row].append(label)
            positions.append((row,x,y,left,right,label))
    raw_ref=(HERE/'reference.txt').read_text()
    ref=norm(re.sub(r'⟦.*?⟧|\[\?\]', '',raw_ref,flags=re.S))
    real=assess(consensus,table,ref)
    controls=[];rand=random.Random(1552100633);keys=sorted(table)
    for _ in range(1000):
        vs=[table[k] for k in keys];rand.shuffle(vs)
        controls.append(assess(consensus,dict(zip(keys,vs)),ref)['score'])
    real.update({'union':len(positions),'exact_labels':sum(bool(p[-1]) for p in positions),'coverage':real['covered']/len(positions),
                 'control_tie':controls.count(real['score']),'control_greater':sum(s>real['score'] for s in controls),
                 'control_max':max(controls),'inputs':{str(p.relative_to(HERE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in input_paths}})
    real['pass']=real['coverage']>=.55 and real['known']>=20 and all(real['pieces']) and real['score']>=14 and real['score']>max(controls)
    with (HERE/'positions.tsv').open('w',newline='') as stream:
        w=csv.writer(stream,delimiter='\t');w.writerow(['row','x_a','x_b','label_a','label_b','consensus']);w.writerows(positions)
    (HERE/'control_scores.txt').write_text('\n'.join(map(str,controls))+'\n')
    (HERE/'result.json').write_text(json.dumps(real,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(real,ensure_ascii=False))

if __name__=='__main__':
    main()
