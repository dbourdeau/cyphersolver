import json,csv,re,sys
k=json.load(open('key_corsi_w17_frozen.json'))
bare,base,vow,num=k['bare'],k['base'],k['vowel'],k['num']
def dec(t):
    t=t.rstrip('?')
    if t in ('.',''): return '','null'
    if t.startswith('#'): return (num.get(t,'['+t+']'), 'num' if t in num else 'hole')
    if t in num: return num[t],'num'
    if t in bare: return bare[t],'val'
    m=re.match(r'^(.+?)(\d)$',t)
    if m and m.group(1) in base and m.group(2) in vow: return base[m.group(1)]+vow[m.group(2)],'val'
    return '_','hole'
rows=[r for r in csv.reader(open('blind/BLIND.tsv'),delimiter='\t') if len(r)>=3 and not r[0].startswith('image')]
st={'val':0,'num':0,'hole':0,'null':0}; out=[]
for r in rows:
    s=''
    for t in r[2].split():
        v,c=dec(t); st[c]+=1; s+=v if c!='hole' else '_'
    out.append(f"{r[0]}\t{r[1]}\t{s}")
open('blind/decode_once.txt','w').write('\n'.join(out)+'\n')
print('\n'.join(out)); print(st)
