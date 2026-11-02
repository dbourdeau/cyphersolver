"""Tiltman's test: dinome substitution survives dinome transposition, so aligned dinome IC stays high. Any message, any group length."""
import json,re,collections,sys
sys.stdout.reconfigure(encoding='utf-8')
M=[json.loads(l) for l in open('targets/kopp1921/messages_ocr.jsonl',encoding='utf-8')]
def ic(c):
    n=sum(c.values());return sum(v*(v-1) for v in c.values())/(n*(n-1))*100 if n>1 else 0
rows=[];seen=set()
for m in M:
    L=m['len'];g=[x for x in m['groups'] if len(x)==L]
    if len(g)<30 or tuple(g[:10]) in seen: continue
    seen.add(tuple(g[:10]));s=''.join(g)
    v=[]
    for off in (0,1):
        c=collections.Counter(s[i:i+2] for i in range(off,len(s)-1,2));v.append((round(ic(c),2),len(c)))
    # trinomes too
    t=[]
    for off in (0,1,2):
        c=collections.Counter(s[i:i+3] for i in range(off,len(s)-2,3));t.append(round(ic(c)*10,2))
    rows.append((max(v)[0],v,t,len(g),L,m['file'][5:-4],m['disc'],' '.join(re.findall(r'[A-Za-z]{3,}',m['head'])[-3:])))
rows.sort(reverse=True)
print(len(rows))
for r in rows[:60]: print(r)
print(collections.Counter(round(r[0],0) for r in rows))
