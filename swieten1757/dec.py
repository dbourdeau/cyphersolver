import json,sys,os
sys.stdout.reconfigure(encoding='utf-8')
H=os.path.dirname(os.path.abspath(__file__))
K=json.load(open(os.path.join(H,'key.json'),encoding='utf-8'))
for line in open(os.path.join(H,'runs.txt')):
    line=line.split('#')[0].strip()
    if not line: continue
    tag,g=line.split(':',1); g=g.split()
    if len(sys.argv)>1 and tag not in sys.argv[1:]: continue
    print(tag, ''.join(K.get(x,'['+x+']') for x in g))
    if '-v' in os.environ.get('V',''): print('   ',' '.join(f'{x}={K.get(x,"?")}' for x in g))
