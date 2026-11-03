import sys,os
sys.path.insert(0,'scripts'); from parse import words
key=dict(kv.split('=') for kv in open(sys.argv[1]).read().split())
for p in sys.argv[2].split(','):
    out=[]
    for k,v in words(open(f'trans_final/p{p}.txt' if os.path.exists(f'trans_final/p{p}.txt') else f'trans_raw/p{p}_A.txt',encoding='utf8').read()):
        if k=='P': out.append(v)
        else: out.append('<'+''.join(key.get(t,'?') if len(t)<=2 else '['+t+']' for t in v)+'>')
    print('==',p,' '.join(out))
