"""Conservative position-based comparison of two blind readings. No key or gloss."""
import csv
from pathlib import Path
from collections import Counter

here = Path(__file__).resolve().parent


def read_table(path):
    with path.open() as stream:
        return list(csv.DictReader((line for line in stream if not line.startswith('#')), delimiter='\t'))


def literal(value):
    if value in '0123456789' and len(value) == 1:
        return value
    if value in ('square-dot', 'square_outline_with_center_dot'):
        return 'square with central dot'
    return None


def score(first, second, tolerance, without=None):
    previous = [0] * (len(second) + 1)
    for i, (a, ax) in enumerate(first):
        current = [0]
        for j, (b, bx) in enumerate(second):
            n = max(previous[j+1], current[-1])
            if a is not None and a == b and abs(ax-bx) <= tolerance and (i,j) != without:
                n = max(n, previous[j]+1)
            current.append(n)
        previous = current
    return previous[-1]


ra = read_table(here/'a/position_inventory.tsv')
rb = read_table(here/'b/scan149_position_shapes.tsv')
runs = {'B1':'H0','B2':'H1','B3':'H2','B4':'H3','M3':'M1','M4':'M2','M5':'M3'}
records = []
for aid, bid in runs.items():
    a = [x for x in ra if x['run']==aid]
    b = [x for x in rb if x['run']==bid]
    tolerance = 15 if aid.startswith('B') else 20
    first = [(literal(x['diplomatic_shape']),int(x['approx_axis_pixel'])) for x in a]
    second = [(literal(x['shape']),int(x['coordinate'])) for x in b]
    maximum = score(first,second,tolerance)
    for i,(av,ax) in enumerate(first):
        for j,(bv,bx) in enumerate(second):
            if av is None or av != bv or abs(ax-bx)>tolerance:
                continue
            if score(first,second,tolerance,(i,j)) == maximum:
                continue
            records.append((aid,i+1,ax,bid,j+1,bx,av))
with (here/'agreed_positions.tsv').open('w',newline='') as out:
    w=csv.writer(out,delimiter='\t',lineterminator='\n')
    w.writerow(['reader_a_run','a_ordinal','a_axis_pixel','reader_b_run','b_ordinal','b_axis_pixel','agreed_shape'])
    w.writerows(records)
agreed = {(a,i):(b,j,v) for a,i,_,b,j,_,v in records}
with (here/'a_positions_with_holes.tsv').open('w',newline='') as out:
    w=csv.writer(out,delimiter='\t',lineterminator='\n')
    w.writerow(['a_run','a_observed_ordinal','a_coordinate','b_run','b_ordinal','consensus'])
    for row in ra:
        k=row['run'],int(row['ordinal_observed'])
        w.writerow([*k,row['approx_axis_pixel'],*agreed.get(k,('','','?'))])
adopted = {(b,j) for _,_,_,b,j,_,_ in records}
with (here/'b_positions_with_holes.tsv').open('w',newline='') as out:
    w=csv.writer(out,delimiter='\t',lineterminator='\n')
    w.writerow(['b_run','b_observed_ordinal','b_coordinate','b_shape','accepted'])
    seen=Counter()
    for row in rb:
        k=row['run'];seen[k]+=1
        w.writerow([k,seen[k],row['coordinate'],row['shape'],int((k,seen[k]) in adopted)])
print('Reader A rows',len(ra),'Reader B rows',len(rb),'accepted',len(records))
print(Counter(x[0] for x in records))
