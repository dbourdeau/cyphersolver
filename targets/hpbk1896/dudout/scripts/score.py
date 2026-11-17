# score.py KEY.json SHEET... : agreement between frozen key and the clerk's glosses on held-out sheets,
# against 200 within-class shuffles of the key (letter values permuted over the key's numerals). Seed 2646.
import csv,sys,os,json,random
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CL=[set('بتثنیئپىي'),set('جحخچ'),set('دذ'),set('رزژ'),set('سش'),set('صض'),set('طظ'),set('عغ'),set('فق'),set('كکگ'),set('هةۀ')]
def sk(g):
    g=''.join(c for c in g if c not in '()/ .ـ').strip()
    if not g: return None
    if g.startswith('لا'): return 'لا'
    c=g[0]
    for i,s in enumerate(CL):
        if c in s: return 'C%d'%i
    return c
key=json.load(open(sys.argv[1],encoding='utf-8')); key={k:v for k,v in key.items() if not k.startswith('_')}
toks=[]; excl=0
for sid in sys.argv[2:]:
    for r in csv.DictReader(open(f'{D}/transcription/merged_{sid}.tsv',encoding='utf-8'),delimiter='\t'):
        if r['type']!='num2' or not r['numA'] or r['numA']!=r['numB']: continue
        refs={sk(g) for g in (r['glossA'],r['glossB']) if g.strip() not in ('','-','?','ـ')}
        refs.discard(None)
        if not refs: excl+=1; continue
        toks.append((r['numA'],refs))
def score(k):
    return sum(1 for n,refs in toks if n in k and sk(k[n]) in refs)/len(toks)
s=score(key)
rnd=random.Random(2646); nums=list(key); vals=[key[n] for n in nums]; ctrl=[]
for _ in range(200):
    v=vals[:]; rnd.shuffle(v); ctrl.append(score(dict(zip(nums,v))))
best=max(ctrl)
print(json.dumps({'tokens':len(toks),'excluded_no_gloss':excl,'score':round(s,4),'best_control':round(best,4),
 'mean_control':round(sum(ctrl)/len(ctrl),4),'pass':s>=0.85 and s>=best+0.30},ensure_ascii=False))
