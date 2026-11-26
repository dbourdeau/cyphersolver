import csv,os,collections
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'judge.tsv')
rows=list(csv.DictReader(open(p,encoding='utf-8'),delimiter='\t'))
def tot(rs):
    a=[sum(int(r[k]) for r in rs) for k in ('letters','S','E','N')]
    assert a[0]==a[1]+a[2]+a[3]
    return a
def show(name,rs):
    L,S,E,N=tot(rs); print(f'{name:10} letters {L:5}  S {S:5}  E {E:4}  N {N:4}  S% {100*S/L:5.1f}  (S+E)% {100*(S+E)/L:5.1f}')
cards=collections.OrderedDict()
for r in rows: cards.setdefault(r['line_id'].split('_')[0],[]).append(r)
for c in ('j76','j77','j79','j80','j81','j84','j96'): show(c,cards[c])
show('TRAINING',[r for r in rows if r['set']=='T'])
show('HELD-OUT',[r for r in rows if r['set']=='H'])
show('ALL',rows)
sc=[r for r in rows if int(r['letters'])>0]
lo=min(sc,key=lambda r:int(r['S'])/int(r['letters']))
print('lowest line:',lo['line_id'],lo['set'],f"S {lo['S']}/{lo['letters']}",lo['reading'])
