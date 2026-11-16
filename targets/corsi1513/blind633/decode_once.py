# Doc 633: one decode with the frozen key. Run from corsi1513/: python3 -I blind633/decode_once.py
import json,csv,re,sys,os,hashlib
KEY='key_corsi_w17_frozen.json'; KH='5f56ad5879c6d53d9c865d52096fde97fbe831e6fcca924efe83a5247c732940'
OUT='blind633/decode_once.txt'; B='blind633/BLIND.tsv'
if os.path.exists(OUT): sys.exit('REFUSED: decode_once.txt exists; first pass is of record')
h=hashlib.sha256(open(KEY,'rb').read()).hexdigest()
if h!=KH: sys.exit('REFUSED: key hash mismatch '+h)
fb=open('blind633/FREEZE_blind.txt').read()
bh=hashlib.sha256(open(B,'rb').read()).hexdigest()
if bh not in fb: sys.exit('REFUSED: BLIND.tsv hash not in FREEZE_blind.txt')
k=json.load(open(KEY))
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
rows=[r for r in csv.reader(open(B),delimiter='\t') if len(r)>=3 and not r[0].startswith('image')]
st={'val':0,'num':0,'hole':0,'null':0}; out=[]
for r in rows:
    s=''
    for t in r[2].split():
        v,c=dec(t); st[c]+=1; s+=v if c!='hole' else '_'
    out.append(f"{r[0]}\t{r[1]}\t{s}")
open(OUT,'w').write('\n'.join(out)+'\n')
print('\n'.join(out)); print('key sha256 ok',h); print('blind sha256',bh); print(st)
