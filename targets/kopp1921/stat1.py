"""First structure tests on the OCR messages: digit-position stats, stepping, depth by discriminant."""
import json,re,collections,itertools,sys
sys.stdout.reconfigure(encoding='utf-8')
M=[json.loads(l) for l in open('targets/kopp1921/messages_ocr.jsonl',encoding='utf-8')]
F=[m for m in M if m['len']==4 and m['n']>=30]
print('4-fig msgs',len(F),sum(m['n'] for m in F))
gs=[g for m in F for g in m['groups'] if len(g)==4]
for i in range(4): print('pos',i,[round(collections.Counter(g[i] for g in gs)[str(d)]/len(gs),3) for d in range(10)])
# first-digit step distribution per msg
d=collections.Counter()
for m in F:
    g=[x for x in m['groups'] if len(x)==4]
    for a,b in zip(g,g[1:]): d[(int(b[0])-int(a[0]))%10]+=1
print('step d1',[d[i] for i in range(10)])
d=collections.Counter()
for m in F:
    g=[x for x in m['groups'] if len(x)==4]
    for a,b in zip(g,g[1:]): d[(int(b[:2])-int(a[:2]))%100]+=1
print('top step d12',d.most_common(12))
for m in sorted(F,key=lambda m:-m['n'])[:6]:
    print(m['file'],m['n'],m['head'][-60:].replace('\n',' '));print(' '.join(m['groups'][:60]))
# pairs: split as dinomes
c=collections.Counter(x[:2] for x in gs); e=collections.Counter(x[2:] for x in gs)
print('hi',c.most_common(15));print('lo',e.most_common(15))
