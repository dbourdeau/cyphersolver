import json,re,collections,sys,math
sys.stdout.reconfigure(encoding='utf-8')
M=[json.loads(l) for l in open('targets/kopp1921/messages_ocr.jsonl',encoding='utf-8')]
K=[];seen=set()
for m in M:
    g=[x for x in m['groups'] if len(x)==4]
    if m['len']!=4 or len(g)<30 or tuple(g[:12]) in seen or re.search('AUSSENAMT|OESTER|RADIO|GAMOT|POLPRED',m['head']): continue
    c=collections.Counter(x[:2] for x in g)
    top=sum(c[k] for k in '64 74 75 85 86 84 65 62 76 96 57 58 47 48'.split())/len(g)
    if top>.3: seen.add(tuple(g[:12]));K.append((m,g,top))
gs=[x for _,g,_ in K for x in g]
print(len(K),len(gs),len(set(gs)))
C=collections.Counter(gs);print(C.most_common(70))
print('freq of freq',sorted(collections.Counter(C.values()).items())[:15])
H=collections.Counter(x[:2] for x in gs)
tab=[[H[f'{a}{b}'] for b in range(10)] for a in range(10)];print('hi grid');[print(a,r) for a,r in enumerate(tab)]
L=collections.Counter(x[2:] for x in gs)
print('lo grid');[print(a,[L[f'{a}{b}'] for b in range(10)]) for a in range(10)]
print('\nlo given hi')
for h,_ in H.most_common(10):
    print(h,collections.Counter(x[2:] for x in gs if x[:2]==h).most_common(14))
for m,g,t in K[:3]: print(m['file'],' '.join(g[:50]))
# MI hi lo
n=len(gs);J=collections.Counter((x[:2],x[2:]) for x in gs)
print('MI hi;lo',round(sum(v/n*math.log2((v/n)/(H[a]/n*L[b]/n)) for (a,b),v in J.items()),3),' sampled bias~',round((len(H)-1)*(len(L)-1)/(2*n*math.log(2)),3))
