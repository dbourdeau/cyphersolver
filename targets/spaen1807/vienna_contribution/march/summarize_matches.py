"""Summarize the recorded result. Does not load the held-out text or run the scorer."""
import csv
from collections import defaultdict
from pathlib import Path

p=Path(__file__).resolve().parent

def read(f):
    with (p/f).open() as sig:return list(csv.DictReader(sig,delimiter='\t'))

groups=read('groups26.tsv');preds=read('predictions26.tsv');matches=read('transfer_matches.tsv')
occ=defaultdict(list)
oks={int(r['first']):int(r['clear_index']) for r in matches}
for r in preds:
    a=int(r['first']);b=int(r['last'])
    assert a==b
    code=groups[a-1]['strict']
    occ[code,r['word']].append(a)
f=(p/'held_support_by_code.tsv').open('w')
wr=csv.writer(f,delimiter='\t',lineterminator='\n')
wr.writerow(['code','word','matched','attempted','all_locations','matched_reference_indices','all_match_nonoverlapping_windows'])
for (c,w),o in sorted(occ.items()):
    hits=[i for i in o if i in oks]
    separated=bool(hits) and len(hits)==len(o) and max(hits)-min(hits)>0.08*len(groups)
    wr.writerow([c,w,len(hits),len(o),','.join(map(str,o)),','.join(str(oks[i]) for i in hits),int(separated)])
    print(c,w,len(hits),len(o),separated)
f.close()
