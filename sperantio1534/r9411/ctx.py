import re,sys
keyf,tf=sys.argv[1],sys.argv[2]; syms=sys.argv[3].split(',')
key=dict(kv.split('=',1) for kv in open(keyf,encoding='utf8').readline().split())
over=dict(kv.split('=',1) for kv in (sys.argv[4].split(',') if len(sys.argv)>4 else []))
key.update(over)
toks=[]
for l in open(tf,encoding='utf8'):
    if not re.match(r'\d+ ',l): continue
    for part in re.split(r'(\{[^}]*\})',l.split(None,1)[1]):
        if part.startswith('{'): toks.append('|'); continue
        toks+= [t for t in part.split() if t!=':']
    toks.append('/')
dflt={'n':'b','4':'e','E':'d','H':'u'}
def v(t): return key.get(t,dflt.get(t,'?')).replace('_','·')
for s in syms:
    print('==',s)
    for i,t in enumerate(toks):
        if t==s:
            L=''.join(v(x) for x in toks[max(0,i-6):i]); R=''.join(v(x) for x in toks[i+1:i+7])
            print(f'   {L:>14} [{s}] {R}')
