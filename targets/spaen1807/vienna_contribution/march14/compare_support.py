"""Compare existing independent score files without opening the French references."""
import csv
from collections import defaultdict
from pathlib import Path

p=Path(__file__).resolve().parent
old=p.parent/'march'
def read(folder,f):
    with (folder/f).open() as h:return list(csv.DictReader(h,delimiter='\t'))
def records(folder,doc):
    groups=read(folder,f'groups{doc}.tsv')
    matched={(int(r['first']),int(r['last']),r['prediction']) for r in read(folder,'transfer_matches.tsv')}
    stats=defaultdict(list)
    for r in read(folder,f'predictions{doc}.tsv'):
        start,end=int(r['first']),int(r['last']);word=r['word']
        group=' '.join(g['strict'] for g in groups[start-1:end])
        stats[group,word].append((start,(start,end,word) in matched))
    return stats
first,second=records(old,26),records(p,21)
original_six={r['code'] for r in read(old,'held_support_by_code.tsv') if r['all_match_nonoverlapping_windows']=='1'}
rows=[]
for code,word in sorted(set(first)|set(second)):
    a,b=first.get((code,word),[]),second.get((code,word),[])
    x=sum(ok for i,ok in a);y=sum(ok for i,ok in b)
    all_two=bool(a and b and x==len(a) and y==len(b))
    rows.append([code,word,x,len(a),y,len(b),int(code in original_six),int(all_two),','.join(str(i) for i,ok in a),','.join(str(i) for i,ok in b)])
with (p/'cross_letter_support.tsv').open('w') as h:
    w=csv.writer(h,delimiter='\t',lineterminator='\n');w.writerow(['code','word','matches26','attempts26','matches21','attempts21','original_six','matched_every_occurrence_in_both','ordinals26','ordinals21']);w.writerows(rows)
print('Former six',[(r[0],r[1],r[2:6]) for r in rows if r[6]])
print('Every prediction in both',[(r[0],r[1],r[2:6]) for r in rows if r[7]])
