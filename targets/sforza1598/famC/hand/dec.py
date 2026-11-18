import sys,json
K=json.load(open('key.json'))
for i,l in enumerate(open('t2.txt')):
    t=l.split(); s=''.join(K.get(x,'?') for x in t)
    print(f'{i+1:2d} {s}')
    if '-v' in sys.argv: print('   '+' '.join(f'{x}{K.get(x,"?")}' for x in t))
