import json,sys
A=json.load(open('ext/alignment.json')); P=A['path']
want=set(sys.argv[1:])
for k,p in enumerate(P):
    if p['type']!='skip' and p['sign'] in want:
        seg=P[max(0,k-7):k+8]
        print(p['line'],p['sign'],'|',' '.join((('['+q['sign']+'='+q['txt']+']') if q is p else (q['sign']+'='+q['txt'])) if q['type']!='skip' else '<SKIP '+A['L'][q['a']:q['b']]+'>' for q in seg))
