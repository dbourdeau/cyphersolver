"""Coverage of frozen Vienna values on No. 6 only; never open any competing letter.

This is the script run on 19 November 2026 at 22:21 UTC. Only the three input paths
(now relative to this repository) and the explicit encoding/newline arguments differ.
Usage: python3 -I -B screen.py [output-directory]   (default: this folder)
"""
import csv
import json
import re
import sys
from collections import Counter,defaultdict
from pathlib import Path
p=Path(__file__).resolve().parent
out=Path(sys.argv[1]) if len(sys.argv)>1 else p
sources={
    'vienna':p.parent/'march/key.tsv',
    'old':p.parents[2]/'spaen1808/annex_groups.txt',
    'reread':p/'annex_pass2.txt',
}
def write(name,header,rows):
    with (out/name).open('w',encoding='utf-8',newline='') as f:
        writer=csv.writer(f,delimiter='\t',lineterminator='\n')
        writer.writerow(header)
        writer.writerows(rows)

by_number=defaultdict(list)
with sources['vienna'].open(encoding='utf-8',newline='') as f:
    for r in csv.DictReader(f,delimiter='\t'):
        num=re.fullmatch(r'(\d+)[ov#:+_](?:~)?',r['code']).group(1)
        by_number[num].append((r['code'],r['value']))
projection={}; detail=[]
for num,items in sorted(by_number.items(),key=lambda v:int(v[0])):
    values={s for _,s in items}
    if len(values)==1 and all(v.startswith('W|') and len(v[2:])>=2 for v in values):
        projection[num]=next(iter(values))[2:]
    detail.append((num,','.join(c for c,s in items),','.join(s for c,s in items),projection.get(num,'')))
write('bare_numbers.tsv',['number','vienna_codes','vienna_labels','eligible_form'],detail)
old=sources['old'].read_text(encoding='utf-8').split()
lines=[s.split() for s in sources['reread'].read_text(encoding='utf-8').splitlines() if s.strip() and not s.startswith('#')]
fresh=[s for line in lines for s in line]
assert len(old)==len(fresh)==75
rows=[]; counts=Counter(); pred=[]
for i,(a,b) in enumerate(zip(old,fresh),1):
    num=b.removesuffix('-').split('?')[0]
    same=(num==a)
    qualified='?' in b
    dash=b.endswith('-')
    counts['agreed_first_choice']+=same
    counts['digit_disagreements']+=not same
    counts['qualified_slots']+=qualified
    counts['trailing_stroke']+=dash
    counts['secure_agreement_including_stroke']+=same and not qualified
    strict=same and not qualified and not dash
    counts['strict_comparable']+=strict
    counts['strict_with_any_bare_number']+=strict and num in by_number
    word=projection.get(num,'') if strict else ''
    if word:pred.append((i,num,word))
    reasons=[]
    if not same:reasons.append('digit disagreement')
    if qualified:reasons.append('reader qualification')
    if dash:reasons.append('baseline stroke')
    if strict and not word: reasons.append('no eligible bare value')
    rows.append([i,a,b,int(strict),word,', '.join(reasons)])
write('slots.tsv',['ordinal','earlier','independent_reread','strict_comparable','prospective_word','qualification'],rows)
write('predictions.tsv',['ordinal','bare_number','prospective_word'],pred)
nforms=len({w for i,n,w in pred})
result=dict(key_entries=sum(map(len,by_number.values())),bare_number_types=len(by_number),eligible_bare_numbers=len(projection),target_slots=75,**counts,covered_slots=len(pred),distinct_forms=nforms,passes_coverage_gate=len(pred)>=8 and nforms>=4)
with (out/'result.json').open('w',encoding='utf-8',newline='') as f:
    f.write(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),pred)
