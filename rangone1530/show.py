import json,sys
key=json.load(open(sys.argv[1]))
for l in open('cipher.txt',encoding='utf8'):
    if l[:1] in 'AB' and l[1].isdigit():
        k,v=l.split(':',1); toks=v.split()
        print(k, ''.join(key.get(t,'?') if t!='|' else ' | ' for t in toks))
        print('   ', ' '.join('%s=%s'%(t,key.get(t,'?')) for t in toks if t!='|'))
