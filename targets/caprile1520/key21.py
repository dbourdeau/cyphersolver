import em21, collections, ast, re, json
crib=open('crib_somogyi.md',encoding='utf8').read()
r38=crib.split('## V1919')[1].split('## V1920')[0].split('\n',2)[2]
caps=' '.join(re.findall(r"[A-ZÀ-Ú’'][A-ZÀ-Ú’' -]*[A-ZÀ-Ú]|\bet\b(?= [A-Z])",r38))
R38=em21.A.plain(caps.replace('et',' et '))
k=ast.literal_eval(open('f21_o4.txt',encoding='utf8').read().split('best')[1].split('\n',2)[1])
em21.DEF=0.01
pairs=[(em21.tk('V1920'),em21.V20),(em21.tk('R1138'),R38)]
P={(t,l):0.5 for t,l in k.items()}
for it in range(12):
    C=collections.Counter();tot=0;als=[]
    for T,L in pairs:
        sc,al=em21.viterbi(T,L,P,-3.0);tot+=sc;als.append(al)
        C.update((t,l) for t,l in al if t and l)
    P=em21.reest(C)
key=collections.defaultdict(collections.Counter)
for (t,l),c in C.items(): key[t][l]+=c
n=sum(C.values()); pure=sum(max(c.values()) for c in key.values())/n
print('matched',n,'purity',round(pure,3))
json.dump({t:dict(c) for t,c in key.items()},open('key21_counts.json','w'),indent=0)
best={t:c.most_common(1)[0][0] for t,c in key.items()}
json.dump(best,open('key21.json','w'),indent=0)
for t,c in sorted(key.items(),key=lambda x:-sum(x[1].values())): print(t,dict(c.most_common(3)))
for i,al in enumerate(als):
    print('--',['V1920','R1138'][i]); print(''.join((l if t and l else ('_' if t else '['+l+']')) for t,l in al))
