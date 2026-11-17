# Build key v2 mechanically from TRAINING glosses (541, 585, 562), passes A and B.
# Rule (fixed before the held-out passes): num2 tokens whose numeral both passes read alike; each pass's gloss is one
# reading; drop bare tick/none/illegible and multi-letter glosses (except 'سه' and 'لا'); a numeral enters the key if
# its majority skeleton class has >= 2 readings and strictly more than the next class; its letter is the most frequent
# reading in that class. Override fixed by the coordinator: 27 = ه (gloss shape).
import csv,os,json,collections
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CL=[set('بتثنیئپىي'),set('جحخچ'),set('دذ'),set('رزژ'),set('سش'),set('صض'),set('طظ'),set('عغ'),set('فق'),set('كکگ'),set('هةۀ')]
def cls(c):
    if c=='لا': return 'لا'
    for i,s in enumerate(CL):
        if c in s: return 'C%d'%i
    return c
def clean(g):
    g=''.join(c for c in g if c not in '()/ .ـ').replace('ي','ی').replace('ک','ك').strip()
    if g=='سه': return 'ش'
    if g in ('لا',): return g
    return g if (len(g)==1 and g not in '-?') else None
R=collections.defaultdict(list)
for sid in ('541','585','562'):
    for r in csv.DictReader(open(f'{D}/transcription/merged_{sid}.tsv',encoding='utf-8'),delimiter='\t'):
        if r['type']!='num2' or not r['numA'] or r['numA']!=r['numB']: continue
        for g in (r['glossA'],r['glossB']):
            c=clean(g)
            if c: R[r['numA']].append(c)
key={'_about':'Key v2, system B. Built by scripts/build_key2.py from training glosses on HPBK 541, 585, 562 (passes A+B); override 27=ه. Frozen in prereg2/.'}
log=[]
for n in sorted(R,key=int):
    cc=collections.Counter(cls(x) for x in R[n]).most_common()
    top,k=cc[0]; nxt=cc[1][1] if len(cc)>1 else 0
    if k>=2 and k>nxt:
        key[n]=collections.Counter(x for x in R[n] if cls(x)==top).most_common(1)[0][0]
    log.append(f'{n}\t{"".join(R[n])}\t{cc}\t{key.get(n,"-")}')
key['27']='ه'
json.dump(key,open(f'{D}/key/key_systemB_v2.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
open(f'{D}/key/key_v2_evidence.tsv','w',encoding='utf-8').write('\n'.join(log)+'\n')
print(len(key)-1,'numerals'); print('\n'.join(log))
