"""Find messages of the 'Karakhan' family: 4-figure groups whose first pair is d0 in 4-7 x odd d1 and whose last pair is two adjacent digits."""
import json,re,collections,sys
sys.stdout.reconfigure(encoding='utf-8')
M=[json.loads(l) for l in open('targets/kopp1921/messages_ocr.jsonl',encoding='utf-8')]
rows=[]
for m in M:
    g=[x for x in m['groups'] if len(x)==4]
    if len(g)<10: continue
    adj=sum(abs(int(x[2])-int(x[3]))==1 for x in g)/len(g)
    odd=sum(int(x[1])%2==1 for x in g)/len(g)
    adjh=sum(abs(int(x[0])-int(x[1]))==1 for x in g)/len(g)
    # any fixed structure: positional parity
    par=[round(sum(int(x[i])%2 for x in g)/len(g),2) for i in range(4)]
    rows.append((round(adj,2),round(odd,2),round(adjh,2),par,len(g),m['file'][5:-4],' '.join(re.findall(r'[A-Za-z]{3,}',m['head'])[-4:])))
rows.sort(reverse=True)
for r in rows[:14]: print(r)
print('by odd');rows.sort(key=lambda r:-abs(r[1]-.5))
for r in rows[:25]: print(r)
