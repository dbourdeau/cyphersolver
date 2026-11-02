import json,sys
A=json.load(open('ext/alignment.json')); P=A['path'];W=A['words'];wid=A['wid']
want=set(sys.argv[1:])
for k,p in enumerate(P):
    if p['type']!='skip' and p['sign'] in want:
        a=P[max(0,k-6)]['a']; b=P[min(len(P)-1,k+6)]['b']
        ws=sorted({wid[i] for i in range(a,b)})
        print(p['line'],p['sign'],p['txt'],'|',' '.join(W[w] for w in ws),'|',' '.join(q.get('sign','<')+'='+q.get('txt',A['L'][q['a']:q['b']]) for q in P[max(0,k-4):k+5]))
