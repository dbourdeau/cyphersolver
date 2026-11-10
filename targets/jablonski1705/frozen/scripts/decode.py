import json,sys,re
key=json.load(open(sys.argv[1]))
out=[];n=0;unk=0
for line in open(sys.argv[2],encoding='utf-8'):
    if line.startswith('#') or not line.strip(): continue
    tag=' '.join(line.split()[:2]); body=' '.join(line.split()[2:])
    words=[]
    for seg in body.split('|'):
        seg=seg.replace('F',' ')
        for chunk in seg.split():
            gs=[g for g in chunk.split('.') if g]
            w=''
            for g in gs:
                n+=1; gg=g.rstrip('?')
                if gg=='' or gg not in key: w+='?'; unk+=1
                else: w+=key[gg]
            words.append(w)
    out.append(tag+' '+' '.join(words))
print('\n'.join(out)); print(f'# groups={n} unknown={unk}',file=sys.stderr)
