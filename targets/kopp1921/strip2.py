import json,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
P=[g for f in ('lutowinoff417_ct.txt','kopp0876_ct.txt','kopp0877_ct.txt') for g in open(f).read().split() if '?' not in g]
V=set(P);VF={g[:2] for g in P};VS={g[2:] for g in P}
M=[json.loads(l) for l in open('messages_ocr.jsonl',encoding='utf-8')]
m=[m for m in M if '042-1265' in m['file'] and m['n']>=300][0]
g=[x for x in m['groups'] if len(x)==4]
def sub(a,k): return ''.join(str((int(x)-int(y))%10) for x,y in zip(a,k))
for key in (['7481','4561'],['7461','4561','7481','4563']):
    s=[sub(x,key[i%len(key)]) for i,x in enumerate(g)]
    print(key,'in vocab',round(sum(x in V for x in s)/len(s),3),'F ok',round(sum(x[:2] in VF for x in s)/len(s),3),'S ok',round(sum(x[2:] in VS for x in s)/len(s),3))
    print(' '.join(s[:70]))
    print(collections.Counter(s).most_common(20))
# by column: second digit etc
for i in range(2):
    c=g[i::2];print(i,collections.Counter(x[:2] for x in c).most_common(12),collections.Counter(x[2:] for x in c).most_common(12))
